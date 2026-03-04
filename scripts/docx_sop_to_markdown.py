"""
Extract Digital Ads - Campaign Process docx to Docusaurus markdown.
- Saves images to static/img/sop-digital-ads-campaign/
- Preserves all links
- Generates TOC from headings
"""
import base64
import re
import os
from pathlib import Path

import mammoth
import html2text

# Paths
REPO = Path(__file__).resolve().parent.parent
DOCX_PATH = REPO / "sop_source.docx"
IMG_OUT_DIR = REPO / "docusaurus" / "static" / "img" / "sop-digital-ads-campaign"
MD_OUT_PATH = REPO / "docusaurus" / "docs" / "review-response-management" / "sop" / "digital-ads-campaign-process.md"

def slug(s):
    """Docusaurus-style slug: lowercase, replace spaces/special with -."""
    s = s.strip().lower()
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[-\s]+', '-', s)
    return s[:50] if len(s) > 50 else s

def image_converter(image):
    """Save image to IMG_OUT_DIR and return src path for HTML."""
    IMG_OUT_DIR.mkdir(parents=True, exist_ok=True)
    ext = "png" if image.content_type == "image/png" else "jpg"
    if not hasattr(image_converter, "count"):
        image_converter.count = 0
    image_converter.count += 1
    num = image_converter.count
    fname = f"{num:02d}.{ext}"
    out_path = IMG_OUT_DIR / fname
    with image.open() as image_bytes:
        with open(out_path, "wb") as f:
            f.write(image_bytes.read())
    return {"src": f"/img/sop-digital-ads-campaign/{fname}"}

def main():
    IMG_OUT_DIR.mkdir(parents=True, exist_ok=True)
    (MD_OUT_PATH.parent).mkdir(parents=True, exist_ok=True)

    with open(DOCX_PATH, "rb") as f:
        result = mammoth.convert_to_html(
            f,
            convert_image=mammoth.images.img_element(image_converter),
        )

    html = result.value
    # Strip Word bookmark anchors we don't need at start; keep section anchors if useful
    html = re.sub(r'<a id="[^"]*"></a>\s*', "", html)

    # HTML to Markdown
    h2t = html2text.HTML2Text()
    h2t.ignore_links = False
    h2t.ignore_images = False
    h2t.body_width = 0  # no wrap
    md_body = h2t.handle(html)

    # Fix escaped brackets in links (e.g. [text](https://...\#gid=...) -> keep URL)
    md_body = re.sub(r'\\([#])', r'\1', md_body)
    # Fix double-underscore emphasis that was bold
    md_body = re.sub(r"__\s*__", "", md_body)

    # Build TOC from ## and ### headings (skip title and TOC line)
    toc_lines = []
    for m in re.finditer(r"^(#{2,3})\s+(.+)$", md_body, re.MULTILINE):
        level, title = m.group(1), m.group(2).strip()
        title_clean = re.sub(r"\s*\{#[-a-z0-9]+\}\s*$", "", title)
        indent = "  " if level == "###" else ""
        anchor = slug(title_clean)
        toc_lines.append(f"{indent}- [{title_clean}](#{anchor})")

    toc_block = "\n".join(toc_lines) if toc_lines else ""

    # Ensure first heading is the doc title
    if not md_body.strip().startswith("# "):
        md_body = "# Digital Ads - Campaign Process\n\n" + md_body

    # Insert TOC after first heading
    first_heading_end = md_body.find("\n\n", md_body.find("# "))
    if first_heading_end != -1 and "## Table of Contents" not in md_body[:2000]:
        insert_pos = first_heading_end + 2
        toc_section = "\n## Table of Contents\n\n" + toc_block + "\n\n---\n\n"
        md_body = md_body[:insert_pos] + toc_section + md_body[insert_pos:]

    frontmatter = """---
title: Digital Ads - Campaign Process
sidebar_label: Digital Ads - Campaign Process
---

"""

    full_md = frontmatter + md_body
    with open(MD_OUT_PATH, "w", encoding="utf-8") as f:
        f.write(full_md)

    print("Wrote", MD_OUT_PATH)
    print("Images in", IMG_OUT_DIR)
    print("TOC entries:", len(toc_lines))

if __name__ == "__main__":
    main()
