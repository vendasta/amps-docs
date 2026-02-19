"""
1. Fix TOC anchors: replace _ with - in (#anchor) so links match Docusaurus slug (kebab-case).
2. Remove standalone lines that duplicate the immediately preceding ## or # heading.
3. Remove duplicate ## heading lines (same ## Section Name repeated - keep first only).
4. If doc has < 3 ## sections (excluding # title, ## Overview, ## Table of Contents), remove TOC block.
5. TOC format: match MS-Communications - ## Table of Contents then - [Title](#anchor) list then ---
"""
import re
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs" / "guru-card-contents"

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
TOC_ANCHOR_RE = re.compile(r"(\(#[^)]+\))")
TOC_BLOCK_START = re.compile(r"^## Table of Contents\s*$")
TOC_LIST_ITEM = re.compile(r"^-\s+\[.+\]\(#[^)]+\)\s*$")


def slug_from_heading(text: str) -> str:
    """Docusaurus-style slug: lowercase, spaces and punctuation to hyphen."""
    s = text.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[-\s]+", "-", s)
    return s.strip("-")


def fix_anchor(anchor: str) -> str:
    """Replace underscores with hyphens in #anchor for Docusaurus."""
    return anchor.replace("_", "-")


def process_file(md_path: Path) -> bool:
    raw = md_path.read_text(encoding="utf-8")
    lines = raw.split("\n")

    # First pass: count unique ## sections (excluding ## Overview, ## Table of Contents)
    section_titles = set()
    for line in lines:
        m = HEADING_RE.match(line)
        if m and m.group(1).startswith("##"):
            ht = m.group(2).strip()
            if ht != "Overview" and ht != "Table of Contents":
                section_titles.add(ht)
    section_count = len(section_titles)
    remove_toc = section_count < 3

    out = []
    i = 0
    heading_texts_seen = set()
    last_heading_text = None
    toc_start_idx = None
    in_toc = False

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        m = HEADING_RE.match(line)
        if m:
            ht = m.group(2).strip()
            # Skip duplicate ## heading (same title already seen)
            if stripped.startswith("##") and ht in heading_texts_seen:
                i += 1
                continue
            if stripped.startswith("##"):
                heading_texts_seen.add(ht)
                last_heading_text = ht

            if TOC_LIST_ITEM.match(line):
                line = TOC_ANCHOR_RE.sub(lambda m: fix_anchor(m.group(1)), line)

            if TOC_BLOCK_START.match(stripped):
                toc_start_idx = len(out)
                in_toc = True

            out.append(line)
            i += 1
            continue

        if last_heading_text and stripped == last_heading_text:
            i += 1
            continue

        if in_toc and stripped == "---":
            in_toc = False
        out.append(line)
        i += 1

    # Remove TOC block if < 3 sections
    if remove_toc and toc_start_idx is not None:
        out2 = []
        j = 0
        while j < len(out):
            if j == toc_start_idx:
                j += 1
                while j < len(out) and out[j].strip() != "---":
                    j += 1
                if j < len(out):
                    j += 1
                continue
            out2.append(out[j])
            j += 1
        out = out2

    new_raw = "\n".join(out)
    if new_raw != raw:
        md_path.write_text(new_raw, encoding="utf-8")
        return True
    return False


def main():
    modified = 0
    for md in sorted(DOCS.glob("*.md")):
        if process_file(md):
            print(f"  Updated: {md.name}")
            modified += 1
    print(f"\nDone. Updated {modified} files.")


if __name__ == "__main__":
    print("Fixing TOC anchors, removing duplicate titles, removing TOC when < 3 sections...")
    main()
