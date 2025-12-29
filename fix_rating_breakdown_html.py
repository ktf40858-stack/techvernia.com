#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fix the malformed rating-breakdown HTML
The data-i18n attribute is incorrectly on the </svg> closing tag
"""

import os

# Base directory
base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
pages_dir = os.path.join(base_dir, "pages", "reviews", "translation")

# All 10 Translation tools
tools = [
    "deepl-pro",
    "google-translate-ai",
    "lilt",
    "lokalise",
    "microsoft-translator",
    "modernmt",
    "phrase",
    "smartling",
    "systran",
    "unbabel"
]

print("=" * 80)
print("FIXING RATING BREAKDOWN HTML")
print("=" * 80)
print()

for tool in tools:
    html_file = os.path.join(pages_dir, f"{tool}.html")

    if not os.path.exists(html_file):
        print(f"  [SKIP] {tool}: HTML file not found")
        continue

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find and replace the malformed HTML
    # Old: </svg data-i18n="sidebar.rating.breakdown">Rating Breakdown</h3>
    # New: </svg> <span data-i18n="sidebar.rating.breakdown">Rating Breakdown</span></h3>

    old_html = '</svg data-i18n="sidebar.rating.breakdown">Rating Breakdown</h3>'
    new_html = '</svg> <span data-i18n="sidebar.rating.breakdown">Rating Breakdown</span></h3>'

    if old_html in content:
        content = content.replace(old_html, new_html)

        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"  [OK] {tool}: Fixed rating-breakdown HTML")
    else:
        print(f"  [SKIP] {tool}: Pattern not found (may already be fixed)")

print()
print("=" * 80)
print("DONE")
print("=" * 80)
