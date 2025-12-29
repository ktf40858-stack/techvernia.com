#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Extract all data-i18n keys from Translation HTML files
"""

import os
import re

# Base directory
base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
pages_dir = os.path.join(base_dir, "pages", "reviews", "translation")

# Check DeepL Pro first
deepl_html = os.path.join(pages_dir, "deepl-pro.html")

print("=" * 70)
print("EXTRACTING DATA-I18N KEYS FROM DEEPL PRO HTML")
print("=" * 70)
print()

with open(deepl_html, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract all data-i18n attributes
pattern = r'data-i18n="([^"]+)"'
keys = re.findall(pattern, content)

# Filter for review.deepl-pro keys only
deepl_keys = [k for k in keys if k.startswith('review.deepl-pro')]

print(f"Found {len(deepl_keys)} DeepL Pro keys:")
print()

for i, key in enumerate(deepl_keys, 1):
    print(f"{i:3d}. {key}")

print()
print("=" * 70)
print(f"Total unique keys: {len(set(deepl_keys))}")
print("=" * 70)
