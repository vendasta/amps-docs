"""
Format newly converted guru-card-contents (exclude original 11):
1. Remove repeated doc title as standalone lines in body
2. TOC: convert link text to title case (first letter caps, rest small), keep #anchors
3. Wrap Note:/Important:/Tip:/Please Note: lines in :::tip (green)
Run from docusaurus: python scripts/format_new_guru_docs.py
"""
import re
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs" / "guru-card-contents"

# Original 11 files - do not modify
ORIGINAL_11 = {
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


def to_title_case(s: str) -> str:
    """First letter of each word caps, rest lowercase. Preserve acronyms in all-caps if 2-4 chars."""
    words = s.split()
    out = []
    for w in words:
        if not w:
            out.append(w)
            continue
        # Keep short all-caps (e.g. GBP, FAQ, SMS) as-is if 2-4 chars
        if len(w) <= 4 and w.isupper() and w.isalpha():
            out.append(w)
        else:
            out.append(w.capitalize())
    return " ".join(out)


def remove_repeated_title(lines: list[str], title_variants: set[str]) -> list[str]:
    """Drop lines that are exactly a title variant (with/without period)."""
    # Normalize for comparison: strip and lower
    norm_variants = set()
    for t in title_variants:
        n = t.strip().rstrip(".").strip().lower()
        if n:
            norm_variants.add(n)
    out = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            out.append(line)
            continue
        norm_line = stripped.rstrip(".").strip().lower()
        if norm_line in norm_variants:
            continue
        if stripped in title_variants:
            continue
        out.append(line)
    return out


def get_title_variants(body: str, frontmatter_title: str | None) -> set[str]:
    """Build set of title strings to remove when they appear as standalone lines."""
    variants = set()
    if frontmatter_title:
        t = frontmatter_title.strip()
        variants.add(t)
        variants.add(t.rstrip("."))
        if not t.endswith("."):
            variants.add(t + ".")
    # From # heading (first # line in body)
    m = re.search(r"^#\s+(.+?)\s*$", body, re.MULTILINE)
    if m:
        t = m.group(1).strip()
        variants.add(t)
        variants.add(t.rstrip("."))
        if not t.endswith("."):
            variants.add(t + ".")
    return variants


def toc_to_title_case(body: str) -> str:
    """Replace TOC entries - [ALL CAPS TEXT](#anchor) -> [Title Case Text](#anchor)."""
    def repl(m):
        link_text = m.group(1)
        anchor = m.group(2)
        anchor = "#" + anchor.lstrip("#")  # single # for link
        # Don't change if already mixed case (like MS-Communications)
        if link_text != link_text.upper():
            return m.group(0)
        new_text = to_title_case(link_text.lower())
        return f"- [{new_text}]({anchor})"

    return re.sub(r"^-\s+\[([^\]]+)\]\((#+[^)]+)\)", repl, body, flags=re.MULTILINE)


def wrap_note_important_in_tip(body: str) -> str:
    """Wrap standalone lines starting with Note:/Important:/Tip:/Please Note: in :::tip ... :::"""
    lines = body.split("\n")
    out = []
    i = 0
    tip_start = re.compile(
        r"^(Note|Important|Tip|Pro tip|Please Note|PLEASE NOTE|Important Note|!!\s*Note)\s*:",
        re.IGNORECASE
    )
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        # Already inside :::tip - keep as is
        if stripped.startswith(":::"):
            out.append(line)
            i += 1
            continue
        if tip_start.match(stripped):
            block = [line]
            j = i + 1
            # Collect until blank line or ## or ::: (one paragraph)
            while j < len(lines):
                next_line = lines[j]
                next_stripped = next_line.strip()
                if not next_stripped or next_stripped.startswith(":::") or next_stripped.startswith("##"):
                    break
                block.append(next_line)
                j += 1
            out.append(":::tip")
            out.extend(block)
            out.append(":::")
            out.append("")
            i = j
            continue
        out.append(line)
        i += 1
    return "\n".join(out)


def process_file(md_path: Path) -> bool:
    """Apply all three formatting steps. Returns True if file was modified."""
    raw = md_path.read_text(encoding="utf-8")
    if "---" not in raw or raw.find("---", 3) < 0:
        return False
    end_fm = raw.find("---", 3)
    front = raw[: end_fm + 3]
    body = raw[end_fm + 3 :].lstrip()

    # Extract frontmatter title
    fm_title = None
    mt = re.search(r'title:\s*["\']?([^"\'\n]+)["\']?', front)
    if mt:
        fm_title = mt.group(1).strip()

    title_variants = get_title_variants(body, fm_title)
    lines = body.split("\n")
    lines = remove_repeated_title(lines, title_variants)
    body = "\n".join(lines)

    body = toc_to_title_case(body)
    body = wrap_note_important_in_tip(body)

    new_raw = front + "\n\n" + body.rstrip() + "\n"
    if new_raw != raw:
        md_path.write_text(new_raw, encoding="utf-8")
        return True
    return False


def main():
    modified = 0
    for md in sorted(DOCS.glob("*.md")):
        stem = md.stem
        if stem in ORIGINAL_11:
            continue
        if process_file(md):
            print(f"  Updated: {md.name}")
            modified += 1
    print(f"\nDone. Updated {modified} files (excluding original 11).")


if __name__ == "__main__":
    print("Formatting new guru-card-contents (remove repeated title, TOC title case, :::tip for Note/Important)...")
    main()
