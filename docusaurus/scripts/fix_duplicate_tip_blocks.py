"""
Merge duplicate :::tip / ::: blocks into single TIP boxes across all guru-card-contents.
Pattern to fix:
  :::tip
  :::tip
  content
  :::
  :::
-> becomes
  :::tip
  content
  :::
"""
import re
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs" / "guru-card-contents"

def fix_file(md_path: Path) -> bool:
    raw = md_path.read_text(encoding="utf-8")
    original = raw
    # Remove duplicate opening :::tip (:::tip newline :::tip -> :::tip)
    raw = re.sub(r"(:::tip)\s*\n\s*\1", r"\1", raw)
    # Remove duplicate closing ::: (::: newline optional spaces ::: -> :::)
    raw = re.sub(r"(:::)\s*\n\s*\n\s*\1", r"\1", raw)
    # Also catch :::\n::: (no blank line)
    raw = re.sub(r"(:::)\s*\n\s*\1", r"\1", raw)
    if raw != original:
        md_path.write_text(raw, encoding="utf-8")
        return True
    return False

def main():
    modified = 0
    for md in sorted(DOCS.glob("*.md")):
        if fix_file(md):
            print(f"  Fixed: {md.name}")
            modified += 1
    print(f"\nDone. Merged duplicate TIP blocks in {modified} files.")

if __name__ == "__main__":
    print("Fixing duplicate :::tip blocks (single TIP box only)...")
    main()
