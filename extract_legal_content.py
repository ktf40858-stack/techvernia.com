#!/usr/bin/env python3
"""Extract English content from Legal & Compliance tool pages"""

import os
import re
import json
import sys
import html

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

LEGAL_TOOLS = [
    'blue-j-legal', 'casetext', 'cocounsel', 'everlaw', 'harvey-ai',
    'kira-systems', 'lawgeex', 'lex-machina', 'luminance', 'primer',
    'ravel-law', 'ross-intelligence'
]

LEGAL_DIR = 'GenuisNet.ai/pages/reviews/legal'

def extract_i18n_content(html_file, tool_name):
    """Extract all data-i18n content from HTML file using regex"""

    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()

        translations = {}

        # Pattern to match: <span data-i18n="key">text</span>
        pattern = r'<span\s+data-i18n="(review\.' + re.escape(tool_name) + r'\.[^"]+)">([^<]+)</span>'

        matches = re.findall(pattern, content, re.DOTALL)

        for key, text in matches:
            # Clean up the text
            text = html.unescape(text.strip())
            text = re.sub(r'\s+', ' ', text)

            translations[key] = text

        return translations

    except Exception as e:
        print(f"[ERROR] {tool_name}: {str(e)[:100]}")
        return None

print("=" * 70)
print("LEGAL & COMPLIANCE TOOLS - CONTENT EXTRACTION")
print("=" * 70)

total_tools = 0
total_keys = 0

for tool_name in LEGAL_TOOLS:
    html_file = os.path.join(LEGAL_DIR, f"{tool_name}.html")

    if not os.path.exists(html_file):
        print(f"\n[SKIP] {tool_name}: HTML file not found")
        continue

    print(f"\n{tool_name}:")

    translations = extract_i18n_content(html_file, tool_name)

    if translations:
        key_count = len(translations)
        print(f"  Extracted {key_count} keys")

        # Save to -en.json file
        output_file = os.path.join(LEGAL_DIR, f"{tool_name}-en.json")

        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(translations, f, ensure_ascii=False, indent=2)

            file_size = os.path.getsize(output_file)
            print(f"  [CREATED] {tool_name}-en.json ({file_size:,} bytes)")

            total_tools += 1
            total_keys += key_count

        except Exception as e:
            print(f"  [ERROR] Could not save file: {str(e)[:50]}")
    else:
        print(f"  [ERROR] No content extracted")

print("\n" + "=" * 70)
print(f"EXTRACTION COMPLETE")
print("=" * 70)
print(f"Tools processed: {total_tools}/12")
print(f"Total keys extracted: {total_keys}")
print(f"Average keys per tool: {total_keys // total_tools if total_tools > 0 else 0}")
print("=" * 70)
