#!/usr/bin/env python3
"""Extract English content from Medical AI tool HTML files."""
import re
import json
from pathlib import Path

MEDICAL_TOOLS = [
    'aidoc', 'butterfly-iq', 'nuance-dragon', 'paige-ai',
    'pathai', 'tempus', 'viz-ai', 'zebra-medical'
]

HTML_DIR = Path("GenuisNet.ai/pages/reviews/medical")
OUTPUT_DIR = Path("GenuisNet.ai/pages/reviews/medical")

def extract_translations_from_html(html_path, tool_name):
    """Extract all data-i18n text from HTML file using regex."""
    translations = {}

    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to match: <span data-i18n="key">Text</span> (and other tags)
    pattern = r'data-i18n="([^"]+)"[^>]*>([^<]+)</(?:span|p|h[1-6]|li|div|a)'
    matches = re.findall(pattern, content)

    for key, text in matches:
        text = text.strip()
        if text and not key.startswith('nav.'):  # Skip navigation items
            # Clean up HTML entities
            text = text.replace('&amp;', '&')
            translations[key] = text

    return translations

def main():
    print("="*60)
    print("EXTRACTING ENGLISH CONTENT FROM MEDICAL AI TOOLS")
    print("="*60)

    total_keys = 0

    for tool in MEDICAL_TOOLS:
        html_file = HTML_DIR / f"{tool}.html"

        if not html_file.exists():
            print(f"[SKIP] {tool}: HTML file not found")
            continue

        translations = extract_translations_from_html(html_file, tool)

        # Save to JSON
        output_file = OUTPUT_DIR / f"{tool}-en.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(translations, f, ensure_ascii=False, indent=2)

        print(f"[OK] {tool}: {len(translations)} keys -> {output_file.name}")
        total_keys += len(translations)

    print("="*60)
    print(f"TOTAL KEYS EXTRACTED: {total_keys}")
    print(f"AVERAGE PER TOOL: {total_keys // len(MEDICAL_TOOLS)}")
    print("="*60)

if __name__ == "__main__":
    main()
