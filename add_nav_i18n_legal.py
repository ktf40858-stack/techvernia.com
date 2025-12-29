#!/usr/bin/env python3
"""Add nav-i18n.js script to Legal tool pages"""

import os
import sys

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

LEGAL_DIR = 'GenuisNet.ai/pages/reviews/legal'
TOOLS = ['blue-j-legal', 'casetext', 'cocounsel', 'everlaw', 'harvey-ai', 'kira-systems', 'lawgeex', 'lex-machina', 'luminance', 'primer', 'ravel-law', 'ross-intelligence']

print("=" * 70)
print("ADDING NAV-I18N SCRIPT TO LEGAL PAGES")
print("=" * 70)

for tool in TOOLS:
    html_file = os.path.join(LEGAL_DIR, f"{tool}.html")

    if not os.path.exists(html_file):
        print(f"\n{tool}: [X] HTML file not found")
        continue

    # Read the HTML file
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if nav-i18n script is already added
    if 'nav-i18n.js' in content:
        print(f"\n{tool}: [SKIP] nav-i18n.js already present")
        continue

    # Find the position to insert (after i18n.js)
    insert_marker = '<script src="../../../js/i18n.js"></script>'

    if insert_marker in content:
        # Add the nav-i18n script after i18n.js
        new_script = '    <script src="../../../js/nav-i18n.js"></script>'
        new_content = content.replace(
            insert_marker,
            f'{insert_marker}\n{new_script}'
        )

        # Write back
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"\n{tool}: [OK] nav-i18n.js added")
    else:
        print(f"\n{tool}: [ERROR] Could not find insertion point")

print("\n" + "=" * 70)
print("Script addition complete!")
print("=" * 70)
