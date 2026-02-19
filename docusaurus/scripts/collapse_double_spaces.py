"""Collapse 2+ spaces to 1 in frontmatter title/sidebar_label values and in # heading lines."""
import re
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs" / "guru-card-contents"


def process_file(md_path: Path) -> bool:
    raw = md_path.read_text(encoding="utf-8", errors="replace")
    lines = raw.split("\n")
    out = []
    in_fm = False
    changed = False

    for line in lines:
        if line.strip() == "---":
            in_fm = not in_fm
            out.append(line)
            continue
        if in_fm:
            m = re.match(r'^(\s*(?:title|sidebar_label):\s*)"([^"]*)"(.*)$', line)
            if m:
                prefix, value, suffix = m.group(1), m.group(2), m.group(3)
                new_val = re.sub(r"  +", " ", value)
                if new_val != value:
                    changed = True
                out.append(f'{prefix}"{new_val}"{suffix}')
            else:
                out.append(line)
            continue
        if line.strip().startswith("#"):
            new_line = re.sub(r"  +", " ", line)
            if new_line != line:
                changed = True
            out.append(new_line)
        else:
            out.append(line)

    if changed:
        md_path.write_text("\n".join(out), encoding="utf-8")
    return changed


def main():
    n = sum(1 for md in DOCS.glob("*.md") if process_file(md))
    print(f"Collapsed double spaces in {n} files.")


if __name__ == "__main__":
    main()
