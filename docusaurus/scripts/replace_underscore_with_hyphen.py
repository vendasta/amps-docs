"""
Replace every underscore (_) with hyphen (-) in markdown content.
Runs on all .md files in guru-card-contents. Does not rename files or folders.
"""
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs" / "guru-card-contents"


def process_file(md_path: Path) -> bool:
    raw = md_path.read_text(encoding="utf-8")
    new_raw = raw.replace("_", "-")
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
    print(f"\nDone. Replaced _ with - in {modified} files.")


if __name__ == "__main__":
    print("Replacing underscore (_) with hyphen (-) in guru-card-contents...")
    main()
