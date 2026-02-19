"""Replace question-mark/replacement char in Reference Pro Tips file with en-dash and * bullets."""
from pathlib import Path
import re

DOCS = Path(__file__).resolve().parent.parent / "docs" / "guru-card-contents"
ref_file = next(DOCS.glob("Reference*Pro*Tips*.md"), None)
if not ref_file:
    print("File not found")
    exit(1)

text = ref_file.read_text(encoding="utf-8", errors="replace")

# Replace any char between Creatives and Digital with en-dash (covers U+FFFD, etc.)
text = re.sub(r"Creatives\s*.\s*Digital", "Creatives – Digital", text)

# Lines that start with replacement char, question mark ornament, or similar -> * bullet
for char in ("\ufffd", "\u2753", "\u2049", "\u2022"):
    text = re.sub(r"^" + re.escape(char) + r"\s*", "* ", text, flags=re.MULTILINE)

# Fix remaining replacement chars in body
text = text.replace("\ufffd", "—")

ref_file.write_text(text, encoding="utf-8")
print("Fixed:", ref_file.name)
