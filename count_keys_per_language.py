#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Count translation keys per language in deepl-pro-i18n.js
"""

import json
import re

filepath = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\js\deepl-pro-i18n.js"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract translations object
json_match = re.search(r'const\s+\w+\s*=\s*(\{.+?\});', content, re.DOTALL)
if json_match:
    json_str = json_match.group(1)
    translations = json.loads(json_str)

    print("Translation keys per language:")
    print("=" * 50)

    for lang in ['en', 'de', 'es', 'fr', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']:
        if lang in translations:
            count = len(translations[lang])
            print(f"{lang.upper()}: {count} keys")

    # Check if all languages have the same number of keys
    counts = [len(translations[lang]) for lang in translations.keys()]
    if len(set(counts)) == 1:
        print()
        print(f"[OK] All languages have {counts[0]} keys")
    else:
        print()
        print("[WARNING] Languages have different key counts!")
        for lang, count in zip(translations.keys(), counts):
            print(f"  {lang}: {count}")
