"""
Replace underscore _ with space in visible text only (titles, sidebar_label, headings, body).
Do NOT change: slug, image paths ![](...), link URLs ](...), or filenames.
"""
import re
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs" / "guru-card-contents"


def replace_visible_underscores(line: str) -> str:
    # Protect image paths ![](...) and link URLs ](...) - do not replace _ inside them
    out = []
    i = 0
    while i < len(line):
        # ![]( or ](
        if (line[i : i + 3] == "![](" or (line[i : i + 2] == "](" and i > 0)):
            start = i
            j = i + (3 if line[i] == "!" else 2)
            depth = 1
            while j < len(line) and depth > 0:
                if line[j] == "(":
                    depth += 1
                elif line[j] == ")":
                    depth -= 1
                j += 1
            out.append(line[i:j])
            i = j
            continue
        if line[i] == "_":
            out.append(" ")
            i += 1
        else:
            out.append(line[i])
            i += 1
    return "".join(out)


def process_file(md_path: Path) -> bool:
    raw = md_path.read_text(encoding="utf-8", errors="replace")
    lines = raw.split("\n")
    out = []
    in_frontmatter = False
    changed = False

    for i, line in enumerate(lines):
        if line.strip() == "---":
            in_frontmatter = not in_frontmatter
            out.append(line)
            continue

        if in_frontmatter:
            if line.strip().startswith("title:") or line.strip().startswith("sidebar_label:"):
                # Replace _ only inside the quoted value
                m = re.match(r'^(\s*(?:title|sidebar_label):\s*)"([^"]*)"(.*)$', line)
                if m:
                    prefix, value, suffix = m.group(1), m.group(2), m.group(3)
                    new_value = value.replace("_", " ")
                    if new_value != value:
                        changed = True
                    out.append(f'{prefix}"{new_value}"{suffix}')
                else:
                    out.append(line)
            elif line.strip().startswith("slug:"):
                # Do NOT change slug
                out.append(line)
            else:
                out.append(line)
            continue

        # Headings
        if line.strip().startswith("#"):
            new_line = replace_visible_underscores(line)
            if new_line != line:
                changed = True
            out.append(new_line)
            continue

        # Body: replace _ but protect image/link URLs
        new_line = replace_visible_underscores(line)
        if new_line != line:
            changed = True
        out.append(new_line)

    if changed:
        md_path.write_text("\n".join(out), encoding="utf-8")
    return changed


def main():
    modified = 0
    for md in sorted(DOCS.glob("*.md")):
        if process_file(md):
            print(md.name)
            modified += 1
    print(f"\nReplaced _ with space in visible text in {modified} files.")


if __name__ == "__main__":
    main()
