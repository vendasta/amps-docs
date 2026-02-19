"""
Remove duplicate title line(s) that appear immediately after the main # heading.
The duplicate is often the same text with different punctuation (_ vs | vs :).
Runs on all .md files in guru-card-contents. Does not change anything else.
"""
import re
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs" / "guru-card-contents"

H1_RE = re.compile(r"^#\s+(.+?)\s*$")
# Line that is a subsection (##) or list/image - not a duplicate title
OTHER_HEADING_RE = re.compile(r"^#{2,}\s+")


def normalize(s: str) -> str:
    s = s.strip().lower()
    # Punctuation that varies between title and duplicate: _ | : / ?
    s = re.sub(r"[\|_:/]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    # Treat trailing ? and . as optional for match
    s = s.rstrip("?.")
    return s


def find_content_start(lines: list) -> int:
    """Return index of first line after frontmatter (and first # heading is in content)."""
    i = 0
    if lines and lines[0].strip() == "---":
        i = 1
        while i < len(lines) and lines[i].strip() != "---":
            i += 1
        if i < len(lines):
            i += 1  # past closing ---
    return i


def process_file(md_path: Path) -> bool:
    raw = md_path.read_text(encoding="utf-8")
    lines = raw.split("\n")
    start = find_content_start(lines)
    if start >= len(lines):
        return False

    # Find first # line (main title)
    i = start
    while i < len(lines) and not H1_RE.match(lines[i]):
        i += 1
    if i >= len(lines):
        return False

    title_line = lines[i]
    m = H1_RE.match(title_line)
    assert m
    title = m.group(1).strip()
    title_norm = normalize(title)

    # Look at following lines (blanks allowed) for a duplicate block of 1, 2, or 3 lines
    j = i + 1
    # Skip blank lines
    while j < len(lines) and lines[j].strip() == "":
        j += 1
    if j >= len(lines):
        return False

    # Next non-empty line(s) - must not be another heading (## or #)
    if OTHER_HEADING_RE.match(lines[j]) or (lines[j].strip().startswith("#") and H1_RE.match(lines[j]) is None):
        return False

    def do_remove(end: int) -> None:
        # Keep: everything through the # title line, then one blank, then rest from end
        new_lines = lines[: i + 1] + [""] + lines[end:]
        md_path.write_text("\n".join(new_lines), encoding="utf-8")

    # Try 1-line duplicate
    line1 = lines[j].strip()
    if normalize(line1) == title_norm:
        end = j + 1
        while end < len(lines) and lines[end].strip() == "":
            end += 1
        do_remove(end)
        return True

    # Try 2-line duplicate
    if j + 1 < len(lines):
        line2 = lines[j + 1].strip()
        if line2 and not OTHER_HEADING_RE.match(lines[j + 1]) and not lines[j + 1].strip().startswith("#"):
            combined = " ".join([line1, line2])
            if normalize(combined) == title_norm:
                end = j + 2
                while end < len(lines) and lines[end].strip() == "":
                    end += 1
                do_remove(end)
                return True

    # Try 3-line duplicate
    if j + 2 < len(lines):
        line2 = lines[j + 1].strip()
        line3 = lines[j + 2].strip()
        if line2 and line3 and not OTHER_HEADING_RE.match(lines[j + 1]) and not OTHER_HEADING_RE.match(lines[j + 2]):
            combined = " ".join([line1, line2, line3])
            if normalize(combined) == title_norm:
                end = j + 3
                while end < len(lines) and lines[end].strip() == "":
                    end += 1
                do_remove(end)
                return True

    return False


def remove_later_duplicates(md_path: Path) -> bool:
    """Remove any later standalone line that duplicates the main # title (normalized)."""
    raw = md_path.read_text(encoding="utf-8")
    lines = raw.split("\n")
    start = find_content_start(lines)
    if start >= len(lines):
        return False
    i = start
    while i < len(lines) and not H1_RE.match(lines[i]):
        i += 1
    if i >= len(lines):
        return False
    title_norm = normalize(H1_RE.match(lines[i]).group(1).strip())
    out = []
    changed = False
    k = 0
    while k < len(lines):
        line = lines[k]
        stripped = line.strip()
        if not stripped:
            out.append(line)
            k += 1
            continue
        if k <= i:
            out.append(line)
            k += 1
            continue
        if OTHER_HEADING_RE.match(line) or (line.strip().startswith("#") and H1_RE.match(line)):
            out.append(line)
            k += 1
            continue
        if normalize(stripped) == title_norm:
            changed = True
            k += 1
            continue
        if k + 1 < len(lines):
            next_s = lines[k + 1].strip()
            if next_s and not OTHER_HEADING_RE.match(lines[k + 1]) and not lines[k + 1].strip().startswith("#"):
                if normalize(" ".join([stripped, next_s])) == title_norm:
                    changed = True
                    k += 2
                    continue
        out.append(line)
        k += 1
    if changed:
        md_path.write_text("\n".join(out), encoding="utf-8")
    return changed


def main():
    modified = 0
    for md in sorted(DOCS.glob("*.md")):
        if process_file(md):
            print(md.name)
            modified += 1
    print(f"\nRemoved duplicate title block after # in {modified} files.")
    later = 0
    for md in sorted(DOCS.glob("*.md")):
        if remove_later_duplicates(md):
            print(f"(later dup) {md.name}")
            later += 1
    if later:
        print(f"\nRemoved later duplicate title line(s) in {later} files.")


if __name__ == "__main__":
    main()
