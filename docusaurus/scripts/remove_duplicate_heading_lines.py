"""
Remove duplicate title/heading lines: remove any line that exactly matches the text
of any # / ## / ### heading that appears earlier in the same file. Runs on all .md
in guru-card-contents. Only removes standalone duplicate lines; does not change anything else.
"""
import re
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs" / "guru-card-contents"

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")


def heading_text(line: str) -> str | None:
    """If line is a markdown heading, return the heading text (without #). Else None."""
    m = HEADING_RE.match(line)
    if not m:
        return None
    return m.group(2).strip()


def normalize(s: str) -> str:
    """Normalize for comparison: lowercase, treat _ and - as space."""
    s = s.strip().lower()
    s = s.replace("_", " ").replace("-", " ")
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def process_file(md_path: Path) -> bool:
    """Remove any line that duplicates a heading that appears earlier (exact or normalized match)."""
    raw = md_path.read_text(encoding="utf-8")
    lines = raw.split("\n")
    heading_texts_seen = set()
    heading_normalized_seen = set()
    out = []
    for line in lines:
        ht = heading_text(line)
        if ht is not None:
            heading_texts_seen.add(ht)
            heading_normalized_seen.add(normalize(ht))
            out.append(line)
            continue
        stripped = line.strip()
        if not stripped:
            out.append(line)
            continue
        if stripped in heading_texts_seen:
            continue
        if normalize(stripped) in heading_normalized_seen:
            continue
        out.append(line)

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
    print(f"\nDone. Removed duplicate heading lines in {modified} files.")


if __name__ == "__main__":
    print("Removing duplicate title/heading lines in guru-card-contents...")
    main()
