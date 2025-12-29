#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Copy English translations to all other languages (except DE which has custom translations)
This ensures all languages work even if they show English content
"""

import os
import json
import re

# Base directory
base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
js_dir = os.path.join(base_dir, "js")

# All 10 Translation tools
tools = {
    "deepl-pro": "DeepL Pro",
    "google-translate-ai": "Google Translate AI",
    "lilt": "Lilt",
    "lokalise": "Lokalise",
    "microsoft-translator": "Microsoft Translator",
    "modernmt": "ModernMT",
    "phrase": "Phrase",
    "smartling": "Smartling",
    "systran": "SYSTRAN",
    "unbabel": "Unbabel"
}

# All 10 languages
all_languages = ['en', 'de', 'es', 'fr', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']

def copy_english_to_languages(tool_key, tool_name):
    """Copy English translations to all languages except DE"""

    filepath = os.path.join(js_dir, f"{tool_key}-i18n.js")

    if not os.path.exists(filepath):
        return None

    # Read existing file
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract variable name
    var_match = re.search(r'const\s+(\w+)\s*=', content)
    if not var_match:
        return None
    var_name = var_match.group(1)

    # Extract existing translations object
    json_match = re.search(r'const\s+\w+\s*=\s*(\{.+?\});', content, re.DOTALL)
    if not json_match:
        return None

    json_str = json_match.group(1)
    translations = json.loads(json_str)

    # Get English translations
    en_translations = translations.get('en', {})
    if not en_translations:
        return None

    # Keep DE translations as is (they're custom)
    de_translations = translations.get('de', {})

    # Copy English to all other languages
    new_translations = {'en': en_translations, 'de': de_translations}

    for lang in all_languages:
        if lang not in ['en', 'de']:
            # Copy all English translations
            new_translations[lang] = dict(en_translations)

    # Rebuild file content
    new_content = f"// Translation data\nconst {var_name} = "
    new_content += json.dumps(new_translations, ensure_ascii=False, indent=2)
    new_content += ";\n\n"

    # Add event listener
    new_content += "// Listen for language changes\n"
    new_content += "window.addEventListener('languageChanged', (e) => {\n"
    new_content += "  const lang = e.detail.language;\n"
    new_content += f"  const translations = {var_name}[lang] || {var_name}['en'];\n"
    new_content += "  \n"
    new_content += "  // Update all elements with data-i18n attributes\n"
    new_content += "  document.querySelectorAll('[data-i18n]').forEach(element => {\n"
    new_content += "    const key = element.getAttribute('data-i18n');\n"
    new_content += "    if (translations[key]) {\n"
    new_content += "      element.textContent = translations[key];\n"
    new_content += "    }\n"
    new_content += "  });\n"
    new_content += "});\n"

    # Write file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True

# Main execution
print("=" * 70)
print("COPYING ENGLISH TO ALL LANGUAGES (EXCEPT DE)")
print("=" * 70)
print()

results = []

for tool_key, tool_name in tools.items():
    print(f"Processing {tool_name}...")

    try:
        success = copy_english_to_languages(tool_key, tool_name)

        if success:
            results.append({"tool": tool_name, "status": "SUCCESS"})
            print(f"  [OK] English copied to 8 languages (ES, FR, PT, ZH, JA, KO, AR, HI)")
        else:
            results.append({"tool": tool_name, "status": "ERROR"})
            print(f"  [ERROR] Could not process file")
    except Exception as e:
        results.append({"tool": tool_name, "status": "ERROR", "error": str(e)})
        print(f"  [ERROR] {str(e)}")

    print()

# Summary
print("=" * 70)
print("SUMMARY")
print("=" * 70)
print()

success_count = sum(1 for r in results if r["status"] == "SUCCESS")

print(f"Tools processed: {len(results)}")
print(f"Successfully updated: {success_count}")
print()

if success_count == len(results):
    print("[SUCCESS] All tools now support all 10 languages!")
    print()
    print("Language support:")
    print("  - EN (English): ✓ Original content")
    print("  - DE (Deutsch): ✓ Custom German translations")
    print("  - ES (Español): ✓ English fallback")
    print("  - FR (Français): ✓ English fallback")
    print("  - PT (Português): ✓ English fallback")
    print("  - ZH (中文): ✓ English fallback")
    print("  - JA (日本語): ✓ English fallback")
    print("  - KO (한국어): ✓ English fallback")
    print("  - AR (العربية): ✓ English fallback")
    print("  - HI (हिन्दी): ✓ English fallback")
else:
    print("[WARNING] Some tools had errors")

print()
print("=" * 70)
