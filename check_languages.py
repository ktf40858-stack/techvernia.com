#!/usr/bin/env python3
"""Check which languages are in each i18n file"""

import re
import os

TOOLS = [
    'datarobot',
    'domo-ai',
    'h2oai',
    'microstrategy-ai',
    'power-bi-copilot',
    'qlik-sense-ai',
    'sisense-ai',
    'yellowfin-ai'
]

JS_DIR = 'GenuisNet.ai/js'
ALL_LANGUAGES = ['en', 'es', 'fr', 'de', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']

def check_languages(filepath):
    """Extract language codes from i18n file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find all language declarations
        pattern = r'"([a-z]{2})":\s*\{'
        languages = re.findall(pattern, content)

        return sorted(set(languages))
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return []

print("=" * 70)
print("Analytics Tools i18n Language Coverage Report")
print("=" * 70)

total_complete = 0
total_incomplete = 0

for tool in TOOLS:
    filepath = os.path.join(JS_DIR, f"{tool}-i18n.js")

    if not os.path.exists(filepath):
        print(f"\n{tool}: FILE NOT FOUND")
        continue

    languages = check_languages(filepath)
    missing = [lang for lang in ALL_LANGUAGES if lang not in languages]

    print(f"\n{tool}:")
    print(f"  Languages present ({len(languages)}): {', '.join(languages)}")

    if missing:
        print(f"  Languages missing ({len(missing)}): {', '.join(missing)}")
        total_incomplete += 1
    else:
        print(f"  [COMPLETE] All 10 languages present!")
        total_complete += 1

print("\n" + "=" * 70)
print(f"Summary: {total_complete} complete, {total_incomplete} incomplete")
print("=" * 70)
