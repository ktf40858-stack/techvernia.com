#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Find exactly which keys are mismatched between HTML and i18n files
"""

import os
import re
import json
from bs4 import BeautifulSoup

# Base directory
base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
pages_dir = os.path.join(base_dir, "pages", "reviews", "translation")
js_dir = os.path.join(base_dir, "js")

# Check one tool as example
tool = "deepl-pro"

print("=" * 80)
print(f"FINDING MISMATCHED KEYS FOR {tool.upper()}")
print("=" * 80)
print()

html_file = os.path.join(pages_dir, f"{tool}.html")
i18n_file = os.path.join(js_dir, f"{tool}-i18n.js")

# Extract data-i18n keys from HTML
print("Extracting keys from HTML...")
with open(html_file, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

html_keys = set()
for elem in soup.find_all(attrs={'data-i18n': True}):
    key = elem.get('data-i18n')
    html_keys.add(key)

print(f"Found {len(html_keys)} data-i18n keys in HTML")
print()

# Extract keys from i18n file
print("Extracting keys from i18n file...")
with open(i18n_file, 'r', encoding='utf-8') as f:
    content = f.read()

json_match = re.search(r'const\s+\w+\s*=\s*(\{.+?\});', content, re.DOTALL)
if json_match:
    translations = json.loads(json_match.group(1))
    if 'en' in translations:
        i18n_keys = set(translations['en'].keys())
        print(f"Found {len(i18n_keys)} keys in i18n file (English)")
        print()

        # Find differences
        missing_in_i18n = html_keys - i18n_keys
        missing_in_html = i18n_keys - html_keys

        if missing_in_i18n:
            print(f"KEYS IN HTML BUT MISSING FROM I18N ({len(missing_in_i18n)}):")
            print("-" * 80)
            for key in sorted(missing_in_i18n):
                # Find the element to see its text
                elem = soup.find(attrs={'data-i18n': key})
                text = elem.get_text(strip=True)[:50] if elem else "N/A"
                print(f"  {key}")
                print(f"    Text: {text}")
                print()

        if missing_in_html:
            print(f"KEYS IN I18N BUT MISSING FROM HTML ({len(missing_in_html)}):")
            print("-" * 80)
            for key in sorted(missing_in_html):
                value = translations['en'].get(key, 'N/A')[:50]
                print(f"  {key}")
                print(f"    Value: {value}")
                print()

        if not missing_in_i18n and not missing_in_html:
            print("[SUCCESS] All keys match perfectly!")
    else:
        print("[ERROR] No English translations found in i18n file")
else:
    print("[ERROR] Could not parse i18n file")

print("=" * 80)
