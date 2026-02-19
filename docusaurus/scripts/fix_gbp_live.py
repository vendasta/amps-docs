from pathlib import Path
import re
DOCS = Path(__file__).resolve().parent.parent / "docs" / "guru-card-contents"
for f in DOCS.glob("*Live*Video*Verification*"):
    text = f.read_text(encoding="utf-8", errors="replace")
    # Replace pattern: "Profile" + single non-ASCII/symbol + " Live" -> "Profile – Live"
    text = re.sub(r"(Profile)\s*.\s*(Live)", r"\1 – \2", text, count=0)
    f.write_text(text, encoding="utf-8")
    print("Fixed:", f.name)
