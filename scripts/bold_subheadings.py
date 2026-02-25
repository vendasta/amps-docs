# -*- coding: utf-8 -*-
"""
Bold standalone subheading-style lines in guru-card-contents .md files.
Strict: only lines that look like section titles (2-8 words, 4-60 chars,
blank before/after, followed by paragraph not list/table).
"""
import os
import re

DOCS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "docusaurus", "docs", "guru-card-contents"
)


def is_subheading_line(line: str, prev_blank: bool, next_blank: bool, next_line: str) -> bool:
    s = line.strip()
    if len(s) < 4 or len(s) > 60:
        return False
    if not re.search(r'[A-Za-z]', s):
        return False
    if s.startswith('**') and s.endswith('**'):
        return False
    # Skip markdown / special
    if re.match(r'^[\#\-\*\[\!\<\|\>\:]', s):
        return False
    if ':::' in s or 'http' in s.lower() or '![' in s:
        return False
    if not prev_blank or not next_blank:
        return False
    # Word count 2-8 (words = letters/numbers)
    words = re.findall(r'[A-Za-z0-9]+', s)
    if len(words) < 2 or len(words) > 8:
        return False
    # Next content line (after blank) should not start list/table
    next_stripped = next_line.strip()
    if next_stripped and next_stripped[0] in '*|-':
        return False
    if next_stripped and len(next_stripped) > 0 and next_stripped[0].isdigit():
        return False
    # Next content must look like a paragraph (long or many words), not another short title
    if next_stripped:
        next_words = len(re.findall(r'[A-Za-z0-9]+', next_stripped))
        if len(next_stripped) < 45 and next_words < 7:
            return False
    return True


def process_file(path: str) -> int:
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    in_frontmatter = False
    frontmatter_count = 0
    changes = 0
    new_lines = []
    for i, line in enumerate(lines):
        if line.strip() == '---':
            frontmatter_count += 1
            in_frontmatter = (frontmatter_count < 2)
            new_lines.append(line)
            continue
        if in_frontmatter:
            new_lines.append(line)
            continue
        stripped = line.strip()
        prev_blank = (i == 0 or lines[i - 1].strip() == '')
        next_blank = (i == len(lines) - 1 or lines[i + 1].strip() == '')
        # Line after the blank (content following subheading)
        follow_line = lines[i + 2] if i + 2 < len(lines) else ''
        if stripped and is_subheading_line(stripped, prev_blank, next_blank, follow_line):
            indent = line[: len(line) - len(line.lstrip())]
            new_lines.append(indent + '**' + stripped + '**\n')
            changes += 1
        else:
            new_lines.append(line)
    if changes:
        with open(path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
    return changes


def main():
    if not os.path.isdir(DOCS_DIR):
        print("Directory not found:", DOCS_DIR)
        return
    total = 0
    for name in sorted(os.listdir(DOCS_DIR)):
        if not name.endswith('.md'):
            continue
        path = os.path.join(DOCS_DIR, name)
        if not os.path.isfile(path):
            continue
        n = process_file(path)
        if n:
            print(name, ":", n, "subheadings bolded")
            total += n
    print("Total lines bolded:", total)


if __name__ == '__main__':
    main()
