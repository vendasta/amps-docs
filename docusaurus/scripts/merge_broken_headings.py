"""
Merge consecutive ## heading lines into a single ## line.
Only run on guru-card-contents files EXCEPT the original 11 (MS-Websites, MS-Communications,
MS-Core-Services, MS-General, MS-Internal-Management, Facebook, Zendesk-Management-Admins,
Legacy-Cards-not-on-a-Board, email-marketing, Website-Content-Creation-Form, Websites-Incoming-Process).
Reference: MS-General, MS-Communications have one ## per section (single line).
"""
import re
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs" / "guru-card-contents"

ORIGINAL_11_STEMS = {
    "MS-Websites",
    "MS-Communications",
    "MS-Core-Services",
    "MS-General",
    "MS-Internal-Management",
    "Facebook",
    "Zendesk-Management-Admins",
    "Legacy-Cards-not-on-a-Board",
    "email-marketing",
    "Website-Content-Creation-Form",
    "Websites-Incoming-Process",
}

HEADING_RE = re.compile(r"^##\s+(.+?)\s*$")


def process_file(md_path: Path) -> bool:
    stem = md_path.stem
    if stem in ORIGINAL_11_STEMS:
        return False
    raw = md_path.read_text(encoding="utf-8")
    lines = raw.split("\n")
    out = []
    i = 0
    changed = False
    while i < len(lines):
        line = lines[i]
        m = HEADING_RE.match(line)
        if not m:
            out.append(line)
            i += 1
            continue
        # Start of a possible run of ## lines
        run = [m.group(1).strip()]
        j = i + 1
        while j < len(lines):
            next_line = lines[j]
            next_stripped = next_line.strip()
            if not next_stripped:
                j += 1
                continue
            m2 = HEADING_RE.match(next_line)
            if m2:
                run.append(m2.group(1).strip())
                j += 1
                continue
            break
        if len(run) > 1:
            merged = "## " + " ".join(run)
            out.append(merged)
            i = j
            changed = True
        else:
            out.append(line)
            i += 1
    if changed:
        md_path.write_text("\n".join(out), encoding="utf-8")
        return True
    return False


def main():
    modified = 0
    for md in sorted(DOCS.glob("*.md")):
        if process_file(md):
            print(f"  Merged broken headings: {md.name}")
            modified += 1
    print(f"\nDone. Merged consecutive ## lines in {modified} files (excluding original 11).")


if __name__ == "__main__":
    print("Merging broken multi-line ## headings into single lines (excluding original 11)...")
    main()
