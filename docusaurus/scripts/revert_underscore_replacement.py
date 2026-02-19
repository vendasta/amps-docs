"""
Revert the underscore-to-hyphen replacement: replace hyphen with underscore in image paths
and in title/heading contexts so image paths match folder names on disk and build succeeds.
- In image paths: "-/" -> "_/" (folder name segment we changed)
- Everywhere else: "-" -> "_" to restore original underscores (titles, body, etc.)
"""
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs" / "guru-card-contents"


def process_file(md_path: Path) -> bool:
    raw = md_path.read_text(encoding="utf-8")
    # First fix image paths: hyphen before / in path (e.g. team-/01.png) -> underscore
    new_raw = raw.replace("-/", "_/")
    # Revert all other hyphens that we had introduced (were underscores) back to underscore
    # This restores titles like "team_" and path segments
    new_raw = new_raw.replace("-", "_")
    if new_raw != raw:
        md_path.write_text(new_raw, encoding="utf-8")
        return True
    return False


def main():
    modified = 0
    for md in sorted(DOCS.glob("*.md")):
        if process_file(md):
            print(f"  Reverted: {md.name}")
            modified += 1
    print(f"\nDone. Reverted - to _ in {modified} files.")


if __name__ == "__main__":
    print("Reverting hyphen (-) back to underscore (_) in guru-card-contents...")
    main()
