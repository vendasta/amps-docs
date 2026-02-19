"""
Fix image paths in guru-card-contents: URL-encode spaces so images load in Docusaurus.
Replaces ![](/img/guru/.../file.png) with ![](/img/guru/...%20.../file.png)
"""
import re
from pathlib import Path
from urllib.parse import quote

DOCS = Path(__file__).resolve().parent.parent / "docs" / "guru-card-contents"

def encode_path(path: str) -> str:
    """URL-encode path: space -> %20, keep slashes. Strip trailing dots from segments (folder names)."""
    # Encode each path segment (between /) to handle spaces and special chars
    parts = path.split("/")
    # Strip trailing dots so folder name matches static/img/guru/ (no dot)
    encoded = [quote(p.rstrip("."), safe="") for p in parts]
    return "/".join(encoded)

def normalize_trailing_dot(path: str) -> str:
    """Remove trailing dot before slash in folder name (e.g. Access./01.png -> Access/01.png)."""
    path = re.sub(r"\./(\d+\.(?:png|jpg|jpeg|gif))", r"/\1", path)
    path = re.sub(r"\.%2F(\d+\.(?:png|jpg|jpeg|gif))", r"/\1", path)
    return path

def fix_file(md_path: Path) -> int:
    """Replace image paths with URL-encoded versions. Returns count of replacements."""
    text = md_path.read_text(encoding="utf-8")
    # Match ![](/img/guru/...anything including ).../NN.png) or .jpg etc
    pattern = re.compile(r'!\[\]\((/img/guru/.+?\.(?:png|jpg|jpeg|gif))\)')
    count = 0
    def repl(m):
        nonlocal count
        raw = normalize_trailing_dot(m.group(1))
        if "%" in raw:
            if raw != m.group(1):
                count += 1
            return f"![]({raw})"
        if " " in raw or "(" in raw or ")" in raw or "&" in raw or "'" in raw:
            encoded = encode_path(raw)
            count += 1
            return f"![]({encoded})"
        return m.group(0) if raw == m.group(1) else f"![]({raw})"
    new_text = pattern.sub(repl, text)
    if count > 0:
        md_path.write_text(new_text, encoding="utf-8")
    return count

def main():
    total = 0
    for md in sorted(DOCS.glob("*.md")):
        n = fix_file(md)
        if n:
            print(f"  {md.name}: {n} paths encoded")
            total += n
    print(f"\nTotal: {total} image paths fixed.")

def fix_trailing_dots_in_paths():
    """Remove trailing dot before / in image paths (e.g. Access./01.png -> Access/01.png)."""
    count = 0
    for md in sorted(DOCS.glob("*.md")):
        text = md.read_text(encoding="utf-8")
        # Match /img/guru/...Something./NN.png and remove the dot
        new_text = re.sub(r"(/img/guru/[^)]*?)\./(\d+\.(?:png|jpg|jpeg|gif))", r"\1/\2", text)
        if new_text != text:
            n = len(re.findall(r"\./(\d+\.(?:png|jpg|jpeg|gif))", text))
            md.write_text(new_text, encoding="utf-8")
            print(f"  {md.name}: removed {text.count('./') - new_text.count('./')} trailing dots")
            count += 1
    return count


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "trailing-dots":
        print("Fixing trailing dots in image paths...")
        fix_trailing_dots_in_paths()
    else:
        main()
