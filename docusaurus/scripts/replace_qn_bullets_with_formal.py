"""Replace question-mark bullet character with formal * bullets. Run on guru-card-contents."""
from pathlib import Path
import re

DOCS = Path(__file__).resolve().parent.parent / "docs" / "guru-card-contents"

# Character that renders as diamond with question mark (U+FFFD replacement char)
BULLET_CHAR = "\ufffd"


def process_file(md_path: Path) -> bool:
    text = md_path.read_text(encoding="utf-8", errors="replace")
    original = text

    # Pattern: line with only bullet char, then blank, then line starting with space + content
    # Step 1: replace "\n<char>\n\n " with "\n* \n\n" so we have "* " on its own line and content on next
    text = text.replace(f"\n{BULLET_CHAR}\n\n ", "\n* \n\n ")

    # Step 2: merge "* " line with next line (content): "\n* \n\n " -> "\n* " (content follows on same line)
    # So we want: "\n* \n\n Turnaround Time: ..." -> "\n* Turnaround Time: ..."
    text = re.sub(r"\n\* \n\n (.+)", r"\n* \1", text, flags=re.MULTILINE)

    # Step 3: remove any remaining standalone lines that are just the bullet char
    text = re.sub(rf"\n{BULLET_CHAR}\s*\n", "\n", text)

    # Step 4: lines that start with bullet char + space -> * 
    text = re.sub(rf"^{re.escape(BULLET_CHAR)}\s*", "* ", text, flags=re.MULTILINE)

    # Collapse 4+ newlines to 2
    text = re.sub(r"\n{3,}", "\n\n", text)

    if text != original:
        md_path.write_text(text, encoding="utf-8")
        return True
    return False


def main():
    count = 0
    for md in sorted(DOCS.glob("*.md")):
        if process_file(md):
            print(md.name)
            count += 1
    print(f"\nReplaced question-mark bullets with * in {count} files.")


if __name__ == "__main__":
    main()
