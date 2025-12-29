#!/usr/bin/env python3
"""
Complete ALL translations for HR category i18n files
Applies the same comprehensive translation strategy as Translation category
"""

import re
import os
import sys

# Add parent directory to path to import from previous scripts
sys.path.insert(0, os.path.dirname(__file__))

# Reuse the same translation dictionaries from the translation category
from complete_all_translations import GENERIC_TRANSLATIONS
from final_translations import FINAL_TRANSLATIONS

# HR tool files
HR_FILES = [
    "beamery-i18n.js",
    "eightfold-ai-i18n.js",
    "fetcher-i18n.js",
    "findem-i18n.js",
    "harver-i18n.js",
    "hirevue-i18n.js",
    "humanly-i18n.js",
    "paradox-olivia-i18n.js",
    "phenom-i18n.js",
    "pymetrics-i18n.js",
    "seekout-i18n.js",
    "sense-i18n.js",
    "textio-i18n.js",
    "workable-ai-i18n.js"
]

# Tool name mappings for HR
HR_TOOL_NAMES = {
    "beamery": "Beamery",
    "eightfold-ai": "Eightfold.ai",
    "fetcher": "Fetcher",
    "findem": "Findem",
    "harver": "Harver",
    "hirevue": "HireVue",
    "humanly": "Humanly",
    "paradox-olivia": "Paradox (Olivia)",
    "phenom": "Phenom",
    "pymetrics": "Pymetrics",
    "seekout": "SeekOut",
    "sense": "Sense",
    "textio": "Textio",
    "workable-ai": "Workable"
}

def get_tool_name(filename):
    """Extract tool name from filename"""
    for key in HR_TOOL_NAMES:
        if filename.startswith(key):
            return HR_TOOL_NAMES[key]
    return "Tool"

def update_file(filepath, translations_dict):
    """Update a file with translations from a dictionary"""
    filename = os.path.basename(filepath)
    tool_name = get_tool_name(filename)

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    updates_count = 0

    for english_template, translations in translations_dict.items():
        english_text = english_template.replace("{TOOL}", tool_name)

        for lang_code, translation_template in translations.items():
            translated_text = translation_template.replace("{TOOL}", tool_name)
            english_escaped = re.escape(english_text)

            pattern = f'("{lang_code}":[\\s\\S]*?)(".*?":\\s*")({english_escaped})(")'

            def replacer(match):
                nonlocal updates_count
                updates_count += 1
                return match.group(1) + match.group(2) + translated_text + match.group(4)

            content = re.sub(pattern, replacer, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return updates_count

def main():
    base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\js"

    print("="*60)
    print("HR CATEGORY - COMPLETE TRANSLATION")
    print("="*60)
    print()

    # Apply translations in two passes
    total_updates = 0

    for filename in HR_FILES:
        filepath = os.path.join(base_dir, filename)
        if not os.path.exists(filepath):
            print(f"[SKIP] File not found: {filename}")
            continue

        print(f"Processing {filename}...")

        # Pass 1: Generic translations
        count1 = update_file(filepath, GENERIC_TRANSLATIONS)

        # Pass 2: Final translations
        count2 = update_file(filepath, FINAL_TRANSLATIONS)

        total_count = count1 + count2
        total_updates += total_count

        print(f"  [OK] {count1} + {count2} = {total_count} translations")

    print()
    print("="*60)
    print(f"TOTAL TRANSLATIONS UPDATED: {total_updates}")
    print(f"FILES PROCESSED: {len(HR_FILES)}")
    print("="*60)

if __name__ == "__main__":
    main()
