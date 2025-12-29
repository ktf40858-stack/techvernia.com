#!/usr/bin/env python3
"""Extract English content from Customer Service & Support tools"""

import os
import json
import re
from bs4 import BeautifulSoup
import sys

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

CUSTOMER_SERVICE_DIR = 'GenuisNet.ai/pages/reviews/customer-service'
OUTPUT_DIR = CUSTOMER_SERVICE_DIR

# List of tools to process (excluding drift which already has translations)
TOOLS = [
    'ada', 'certainly', 'cognigy', 'forethought', 'freshdesk-ai',
    'helpshift', 'intercom-fin', 'kustomer', 'liveperson', 'netomi',
    'polyai', 'ultimateai', 'yellowai', 'zendesk-ai'
]

def extract_english_content(html_file):
    """Extract all translatable content from HTML file"""

    with open(html_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    translations = {}

    # Find all elements with data-i18n attribute
    for element in soup.find_all(attrs={'data-i18n': True}):
        key = element.get('data-i18n')
        text = element.get_text(strip=True)

        if key and text:
            translations[key] = text

    return translations

def save_english_file(tool_name, translations):
    """Save English translations to JSON file"""

    output_file = os.path.join(OUTPUT_DIR, f'{tool_name}-en.json')

    # Wrap in language object
    output = {
        'en': translations
    }

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    return len(translations)

print("=" * 70)
print("CUSTOMER SERVICE & SUPPORT - ENGLISH CONTENT EXTRACTION")
print("=" * 70)

total_tools = 0
total_keys = 0

for tool in TOOLS:
    html_file = os.path.join(CUSTOMER_SERVICE_DIR, f'{tool}.html')

    if not os.path.exists(html_file):
        print(f"\n❌ {tool}: HTML file not found")
        continue

    try:
        translations = extract_english_content(html_file)

        if translations:
            num_keys = save_english_file(tool, translations)
            print(f"\n✅ {tool}: {num_keys} keys extracted")
            total_tools += 1
            total_keys += num_keys
        else:
            print(f"\n⚠️  {tool}: No translatable content found")

    except Exception as e:
        print(f"\n❌ {tool}: Error - {str(e)}")

print("\n" + "=" * 70)
print(f"SUMMARY: {total_tools} tools processed, {total_keys} total keys")
print("=" * 70)
