"""
Fix TOC and frontmatter broken by underscore revert:
- ___ -> --- (frontmatter and horizontal rules)
- Line starting with "_ [" -> "- [" (TOC/list items so they render as proper rows)
Runs on all .md in guru-card-contents.
"""
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs" / "guru-card-contents"


def process_file(md_path: Path) -> bool:
    raw = md_path.read_text(encoding="utf-8")
    new_raw = raw.replace("___", "---")
    # Fix list items: "_ [Title](...#anchor)" -> "- [Title](...#anchor)"
    lines = new_raw.split("\n")
    out = []
    for line in lines:
        if line.strip().startswith("_ [") and "](#" in line:
            line = line.replace("_ [", "- [", 1)
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
            print(f"  Fixed: {md.name}")
            modified += 1
    print(f"\nDone. Fixed TOC/frontmatter in {modified} files.")


if __name__ == "__main__":
    print("Fixing TOC list syntax and frontmatter (___ -> ---, _ [ -> - [)...")
    main()
