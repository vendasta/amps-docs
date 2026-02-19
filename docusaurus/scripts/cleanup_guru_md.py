"""
Clean up guru-card-contents MD files: remove Image N junk, normalize spacing, trim lines.
Run from docusaurus: python scripts/cleanup_guru_md.py
"""
import re
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs" / "guru-card-contents"


def cleanup_content(text: str) -> str:
    # Remove standalone "Image N" / "image N" lines (caption junk)
    lines = text.split("\n")
    out = []
    for line in lines:
        stripped = line.strip()
        if re.match(r"^[-*]?\s*(Image\s+\d+|image\s+\d+)\s*\.?\s*$", stripped, re.IGNORECASE):
            continue
        out.append(line.rstrip())
    # Normalize: max 2 consecutive newlines, trim trailing whitespace per line
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def main():
    for md in sorted(DOCS.glob("*.md")):
        raw = md.read_text(encoding="utf-8")
        if "---" in raw:
            end = raw.find("---", 3)
            if end > 0:
                front = raw[: end + 3]
                body = raw[end + 3 :].lstrip()
            else:
                front = ""
                body = raw
        else:
            front = ""
            body = raw
        new_body = cleanup_content(body)
        new_raw = (front + "\n\n" + new_body).strip() + "\n" if front else new_body
        if new_raw != raw:
            md.write_text(new_raw, encoding="utf-8")
            print(f"  Cleaned: {md.name}")


if __name__ == "__main__":
    print("Cleaning guru-card-contents...")
    main()
    print("Done.")
