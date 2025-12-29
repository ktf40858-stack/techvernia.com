#!/usr/bin/env python3
"""Add i18n scripts to Legal HTML pages"""

import os
import sys

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

LEGAL_DIR = 'GenuisNet.ai/pages/reviews/legal'
TOOLS = ['blue-j-legal', 'casetext', 'cocounsel', 'everlaw', 'harvey-ai', 'kira-systems', 'lawgeex', 'lex-machina', 'luminance', 'primer', 'ravel-law', 'ross-intelligence']

print("=" * 70)
print("ADDING I18N SCRIPTS TO LEGAL PAGES")
print("=" * 70)

for tool in TOOLS:
    html_file = os.path.join(LEGAL_DIR, f"{tool}.html")

    if not os.path.exists(html_file):
        print(f"\n{tool}: [X] HTML file not found")
        continue

    # Read the HTML file
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if i18n script is already added
    if f'{tool}-i18n.js' in content:
        print(f"\n{tool}: [SKIP] Script already present")
        continue

    # Find the position to insert (after complete-translate.js)
    insert_marker = '<script src="../../../js/complete-translate.js"></script>'

    if insert_marker in content:
        # Add the tool-specific i18n script after complete-translate.js
        new_script = f'    <script src="../../../js/{tool}-i18n.js"></script>'
        new_content = content.replace(
            insert_marker,
            f'{insert_marker}\n{new_script}'
        )

        # Write back
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"\n{tool}: [OK] Script added")
    else:
        print(f"\n{tool}: [ERROR] Could not find insertion point")

print("\n" + "=" * 70)
print("Script addition complete!")
print("=" * 70)
