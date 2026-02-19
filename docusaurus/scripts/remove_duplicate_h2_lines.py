"""Remove duplicate ## heading lines: when same ## Title appears again, skip the line."""
import re
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs" / "guru-card-contents"
HEADING_RE = re.compile(r"^##\s+(.+?)\s*$")


def process_file(md_path: Path) -> bool:
    raw = md_path.read_text(encoding="utf-8")
    lines = raw.split("\n")
    seen = set()
    out = []
    for line in lines:
        m = HEADING_RE.match(line)
        if m:
            title = m.group(1).strip()
            if title in seen:
                continue
            seen.add(title)
        out.append(line)
    new_raw = "\n".join(out)
    if new_raw != raw:
        md_path.write_text(new_raw, encoding="utf-8")
        return True
    return False


def main():
    n = sum(1 for md in sorted(DOCS.glob("*.md")) if process_file(md))
    print(f"Removed duplicate ## lines in {n} files.")


if __name__ == "__main__":
    main()
