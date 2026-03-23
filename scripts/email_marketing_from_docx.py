"""
Regenerate Email Marketing Process Mapping from Word: list levels (ilvl), images, skips.

NOTE: docs/sop/social-content/email-marketing-process-mapping/index.md may be hand-edited
(table layout). Back up before running this script — it overwrites the file.
"""
from __future__ import annotations

import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

from docx import Document
from docx.document import Document as DocumentClass
from docx.oxml.ns import qn
from docx.table import Table
from docx.text.paragraph import Paragraph

DOCX = Path(
    r"C:\Users\dbalan\OneDrive\Desktop\GURU CARD CONTENT\SOP's\Social&Content\Email Marketing Process Mapping.docx"
)
REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "docusaurus/docs/sop/social-content/email-marketing-process-mapping/index.md"
STATIC_SUB = "sop-social-content/email-marketing-process-mapping"
DOC_KEY = "em"
TITLE = "Email Marketing Process Mapping"


def load_rels(docx_path: Path) -> dict[str, str]:
    with zipfile.ZipFile(docx_path) as z:
        rels_data = z.read("word/_rels/document.xml.rels")
    root = ET.fromstring(rels_data)
    rels: dict[str, str] = {}
    for rel in root:
        rid = rel.get("Id") or rel.get(
            "{http://schemas.openxmlformats.org/package/2006/relationships}Id"
        )
        target = rel.get("Target")
        if not rid or not target:
            continue
        if target.startswith("../"):
            target = "word/" + target[3:]
        elif not target.startswith("word/"):
            target = "word/" + target
        rels[rid] = target.replace("\\", "/")
    return rels


def iter_block_items(parent):
    if isinstance(parent, DocumentClass):
        parent_elm = parent.element.body
    else:
        raise ValueError("parent must be Document")
    for child in parent_elm.iterchildren():
        if child.tag == qn("w:p"):
            yield Paragraph(child, parent)
        elif child.tag == qn("w:tbl"):
            yield Table(child, parent)


def paragraph_run_chunks(p: Paragraph):
    BLIP = "{http://schemas.openxmlformats.org/drawingml/2006/main}blip"
    for run in p.runs:
        for blip in run._element.findall(f".//{BLIP}"):
            embed = blip.get(qn("r:embed"))
            if embed:
                yield ("image", embed)
        if run.text:
            yield ("text", run.text)


def paragraph_plain_text(p: Paragraph) -> str:
    return "".join(r.text for r in p.runs).replace("\r", "").strip()


def get_ilvl(p: Paragraph) -> int | None:
    pPr = p._element.find(qn("w:pPr"))
    if pPr is None:
        return None
    numPr = pPr.find(qn("w:numPr"))
    if numPr is None:
        return None
    ilvl_el = numPr.find(qn("w:ilvl"))
    if ilvl_el is None:
        return 0
    v = ilvl_el.get(qn("w:val"))
    return int(v) if v is not None else 0


def heading_level(p: Paragraph) -> int | None:
    style = p.style.name if p.style else ""
    if style.startswith("Heading"):
        try:
            return int(style.replace("Heading", "").strip() or "1")
        except ValueError:
            return 1
    return None


def should_skip_paragraph(text: str) -> bool:
    s = text.strip()
    if s == "X":
        return True
    if "^---" in s and "logo" in s.lower() and "website link" in s.lower():
        return True
    if s.lower() == "fsfsd":
        return True
    if "BUG MaRK" in s or s.upper().startswith("BUG MARK ABOUT"):
        return True
    return False


def main():
    rels = load_rels(DOCX)
    dest_dir = REPO / "docusaurus/static/img" / STATIC_SUB
    dest_dir.mkdir(parents=True, exist_ok=True)
    n_img = [0]

    def copy_image(rid: str) -> str | None:
        target = rels.get(rid)
        if not target:
            return None
        with zipfile.ZipFile(DOCX) as z:
            data = z.read(target)
        ext = Path(target).suffix.lower() or ".png"
        n_img[0] += 1
        fname = f"{DOC_KEY}-{n_img[0]:02d}{ext}"
        (dest_dir / fname).write_bytes(data)
        return f"/img/{STATIC_SUB}/{fname}".replace("\\", "/")

    doc = Document(DOCX)
    lines: list[str] = []

    for block in iter_block_items(doc):
        if isinstance(block, Table):
            continue
        p = block
        full = paragraph_plain_text(p)
        if should_skip_paragraph(full):
            continue

        hl = heading_level(p)
        if hl is not None and full:
            lines.append("")
            lines.append(f"{'#' * min(hl, 6)} {full}")
            continue

        ilvl = get_ilvl(p)
        chunks = list(paragraph_run_chunks(p))

        if ilvl is not None:
            text_parts: list[str] = []

            def flush_bullet():
                if not text_parts:
                    return
                t = "".join(text_parts).strip()
                text_parts.clear()
                if not t:
                    return
                indent = "  " * ilvl
                lines.append(f"{indent}- {t}")

            for kind, payload in chunks:
                if kind == "image":
                    flush_bullet()
                    url = copy_image(payload)
                    if url:
                        lines.append("")
                        lines.append(f"![]({url})")
                        lines.append("")
                else:
                    text_parts.append(payload)
            flush_bullet()
            continue

        # Plain paragraph / no list numbering
        text_parts: list[str] = []
        for kind, payload in chunks:
            if kind == "image":
                if text_parts:
                    tt = "".join(text_parts).strip()
                    text_parts = []
                    if tt:
                        lines.append("")
                        lines.append(tt)
                url = copy_image(payload)
                if url:
                    lines.append("")
                    lines.append(f"![]({url})")
                    lines.append("")
            else:
                text_parts.append(payload)
        if text_parts:
            t = "".join(text_parts).strip()
            if t:
                lines.append("")
                lines.append(t)

    # Collapse 3+ blank lines to 2
    cleaned: list[str] = []
    blank = 0
    for line in lines:
        if line.strip() == "":
            blank += 1
            if blank <= 2:
                cleaned.append(line)
        else:
            blank = 0
            cleaned.append(line)

    body = "\n".join(cleaned).strip() + "\n"

    # Page title (sidebar) + Word’s first heading is usually H2
    if body.startswith("##"):
        body = f"# {TITLE}\n\n" + body
    elif not body.startswith("#"):
        body = f"# {TITLE}\n\n" + body

    fm = f"""---
title: {TITLE}
sidebar_label: {TITLE}
---

"""
    wrapped = f'<div class="email-marketing-process-doc">\n\n{body}\n</div>\n'
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(fm + wrapped, encoding="utf-8")
    print("Wrote", OUT, "images", n_img[0])


if __name__ == "__main__":
    main()
