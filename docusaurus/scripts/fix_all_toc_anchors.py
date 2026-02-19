"""Replace _ with - in all TOC anchors (#anchor) so Docusaurus links work."""
import re
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs" / "guru-card-contents"
ANCHOR_RE = re.compile(r"(\(#[^)]+\))")


def fix(match):
    return match.group(1).replace("_", "-")


def process(md_path: Path) -> bool:
    raw = md_path.read_text(encoding="utf-8")
    new_raw = ANCHOR_RE.sub(fix, raw)
    if new_raw != raw:
        md_path.write_text(new_raw, encoding="utf-8")
        return True
    return False


def main():
    n = sum(1 for md in DOCS.glob("*.md") if process(md))
    print(f"Fixed TOC anchors in {n} files.")


if __name__ == "__main__":
    main()
