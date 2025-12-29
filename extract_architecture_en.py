#!/usr/bin/env python3
"""Extract English content from Architecture tool HTML files."""
import json
import re
from pathlib import Path

ARCHITECTURE_TOOLS = [
    'architechtures', 'arko-ai', 'finch3d', 'hypar', 'maket-ai',
    'spacemaker-ai', 'testfit', 'veras-ai'
]

BASE_DIR = Path("GenuisNet.ai/pages/reviews/architecture")

def extract_translations_from_html(html_path, tool_name):
    """Extract all data-i18n text from HTML file using regex."""
    translations = {}

    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to match: <span data-i18n="key">Text</span>
    # Or: <element data-i18n="key">Text</element>
    pattern = r'data-i18n="([^"]+)"[^>]*>([^<]+)</(?:span|p|h[1-6]|li|div|a)'

    matches = re.findall(pattern, content)

    for key, text in matches:
        text = text.strip()
        # Skip empty texts and nav items (handled by common i18n)
        if text and not key.startswith('nav.'):
            # Clean up HTML entities
            text = text.replace('&amp;', '&')
            translations[key] = text

    return translations

def main():
    print("="*60)
    print("ARCHITECTURE EN CONTENT EXTRACTION")
    print("="*60)

    total_tools = 0
    total_keys = 0

    for tool in ARCHITECTURE_TOOLS:
        print(f"\nExtracting {tool}...")

        html_file = BASE_DIR / f"{tool}.html"

        if not html_file.exists():
            print(f"  [SKIP] HTML not found")
            continue

        # Extract translations
        translations = extract_translations_from_html(html_file, tool)

        # Separate main content and FAQs
        main_content = {}
        faq_content = {}

        for key, value in translations.items():
            if '.faq.' in key:
                faq_content[key] = value
            else:
                main_content[key] = value

        # Save main content
        if main_content:
            en_file = BASE_DIR / f"{tool}-en.json"
            with open(en_file, 'w', encoding='utf-8') as f:
                json.dump(main_content, f, ensure_ascii=False, indent=2)
            print(f"  [OK] Main content: {len(main_content)} keys -> {en_file.name}")

        # Save FAQ content separately
        if faq_content:
            faq_file = BASE_DIR / f"{tool}-faqs-en.json"
            with open(faq_file, 'w', encoding='utf-8') as f:
                json.dump(faq_content, f, ensure_ascii=False, indent=2)
            print(f"  [OK] FAQs: {len(faq_content)} keys -> {faq_file.name}")

        tool_total = len(main_content) + len(faq_content)
        print(f"  [OK] Total: {tool_total} translation keys extracted")

        total_tools += 1
        total_keys += tool_total

    print("\n" + "="*60)
    print(f"EXTRACTION COMPLETE")
    print(f"  Tools processed: {total_tools}")
    print(f"  Total keys extracted: {total_keys}")
    print("="*60)

if __name__ == "__main__":
    main()
