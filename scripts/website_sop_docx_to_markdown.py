"""
Convert the three Website SOP docx files to Docusaurus markdown.
Reads from OneDrive GURU CARD CONTENT SOP's Website folder.
Saves images to static/img/sop-website-services/<doc-slug>/.
Preserves all links; TOC with bold clickable links like other SOPs.
Output: docs/sop/website-services/*.md
"""
import re
from pathlib import Path

try:
    import mammoth
    import html2text
except ImportError:
    raise SystemExit("Install: pip install mammoth html2text")

SOURCE_DIR = Path(r"C:\Users\dbalan\OneDrive\Desktop\GURU CARD CONTENT\SOP's\Website")
REPO = Path(__file__).resolve().parent.parent
OUT_MD_DIR = REPO / "docusaurus" / "docs" / "sop" / "website-services"
OUT_IMG_BASE = REPO / "docusaurus" / "static" / "img" / "sop-website-services"

# Order: 1 Accelerated Duda, 2 Express Divi, 3 Templated Divi
DOCS = [
    {
        "file": "Websites SOP - Accelerated Templated Website Build (Duda).docx",
        "slug": "accelerated-templated-website-build-duda",
        "title": "Accelerated Templated Website Build (Duda)",
        "sidebar_position": 1,
    },
    {
        "file": "Websites SOP - Express Website Build (Divi).docx",
        "slug": "express-website-build-divi",
        "title": "Express Website Build (Divi)",
        "sidebar_position": 2,
    },
    {
        "file": "Websites SOP - Templated Website Build (Divi).docx",
        "slug": "templated-website-build-divi",
        "title": "Templated Website Build (Divi)",
        "sidebar_position": 3,
    },
]


def slug(s):
    """Docusaurus-style anchor slug: lowercase, replace spaces/special with -."""
    s = s.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[-\s]+", "-", s)
    return s[:80] if len(s) > 80 else s


def process_doc(config):
    docx_path = SOURCE_DIR / config["file"]
    if not docx_path.exists():
        print(f"SKIP (not found): {docx_path}")
        return
    slug_name = config["slug"]
    img_dir = OUT_IMG_BASE / slug_name
    img_dir.mkdir(parents=True, exist_ok=True)
    img_url_prefix = f"/img/sop-website-services/{slug_name}"

    def image_converter(image):
        img_dir.mkdir(parents=True, exist_ok=True)
        ext = "png" if image.content_type == "image/png" else "jpg"
        if not hasattr(image_converter, "count"):
            image_converter.count = 0
        image_converter.count += 1
        num = image_converter.count
        fname = f"{num:02d}.{ext}"
        out_path = img_dir / fname
        with image.open() as image_bytes:
            with open(out_path, "wb") as f:
                f.write(image_bytes.read())
        return {"src": f"{img_url_prefix}/{fname}"}

    with open(docx_path, "rb") as f:
        result = mammoth.convert_to_html(f, convert_image=mammoth.images.img_element(image_converter))

    html = result.value
    html = re.sub(r'<a id="[^"]*"></a>\s*', "", html)

    h2t = html2text.HTML2Text()
    h2t.ignore_links = False
    h2t.ignore_images = False
    h2t.body_width = 0
    md_body = h2t.handle(html)

    md_body = re.sub(r"\\([#])", r"\1", md_body)
    md_body = re.sub(r"__\s*__", "", md_body)

    # Fix image paths: html2text may output (path) - ensure they're markdown images
    md_body = re.sub(r"!\[\]\((/img/[^)]+)\)", r"![](\1)", md_body)

    # Build TOC from ## and ### with BOLD titles (like other SOPs)
    toc_lines = []
    for m in re.finditer(r"^(#{2,3})\s+(.+)$", md_body, re.MULTILINE):
        level, title = m.group(1), m.group(2).strip()
        title_clean = re.sub(r"\s*\{#[-a-z0-9]+\}\s*$", "", title).strip()
        indent = "  " if level == "###" else ""
        anchor = slug(title_clean)
        toc_lines.append(f"{indent}- [**{title_clean}**](#{anchor})")

    toc_block = "\n".join(toc_lines) if toc_lines else ""

    if not md_body.strip().startswith("# "):
        md_body = f"# {config['title']}\n\n" + md_body

    first_heading_end = md_body.find("\n\n", md_body.find("# "))
    if first_heading_end != -1 and "## Table of Contents" not in md_body[:2000]:
        insert_pos = first_heading_end + 2
        toc_section = "\n## Table of Contents\n\n" + toc_block + "\n\n---\n\n"
        md_body = md_body[:insert_pos] + toc_section + md_body[insert_pos:]

    # Neat formatting: ensure consistent blank lines around headings
    md_body = re.sub(r"\n{3,}", "\n\n", md_body)

    frontmatter = f"""---
title: {config['title']}
sidebar_label: "{config['sidebar_position']}. {config['title']}"
sidebar_position: {config['sidebar_position']}
---

"""

    out_md = OUT_MD_DIR / f"{slug_name}.md"
    OUT_MD_DIR.mkdir(parents=True, exist_ok=True)
    with open(out_md, "w", encoding="utf-8") as f:
        f.write(frontmatter + md_body)

    print(f"Wrote {out_md} (TOC entries: {len(toc_lines)}, images in {img_dir})")


def main():
    for config in DOCS:
        process_doc(config)
    print("Done.")


if __name__ == "__main__":
    main()
