#!/usr/bin/env python3
"""
Complete ALL translations for Gaming & Entertainment category i18n files
Applies the same comprehensive translation strategy as Translation and HR categories
"""

import re
import os
import sys

# Add parent directory to path to import from previous scripts
sys.path.insert(0, os.path.dirname(__file__))

# Reuse the same translation dictionaries from previous categories
from complete_all_translations import GENERIC_TRANSLATIONS
from final_translations import FINAL_TRANSLATIONS

# Gaming & Entertainment tool files
GAMING_FILES = [
    "artomatix-i18n.js",
    "charismaai-i18n.js",
    "hidden-door-i18n.js",
    "inworld-ai-i18n.js",
    "latitude-ai-dungeon-i18n.js",
    "ludoai-i18n.js",
    "promethean-ai-i18n.js",
    "rct-ai-i18n.js",
    "replika-i18n.js",
    "rosebud-ai-i18n.js",
    "scenario-i18n.js"
]

# Tool name mappings for Gaming
GAMING_TOOL_NAMES = {
    "artomatix": "Artomatix",
    "charismaai": "Charisma.ai",
    "hidden-door": "Hidden Door",
    "inworld-ai": "Inworld AI",
    "latitude-ai-dungeon": "AI Dungeon",
    "ludoai": "Ludo.ai",
    "promethean-ai": "Promethean AI",
    "rct-ai": "RCT AI",
    "replika": "Replika",
    "rosebud-ai": "Rosebud AI",
    "scenario": "Scenario"
}

def get_tool_name(filename):
    """Extract tool name from filename"""
    for key in GAMING_TOOL_NAMES:
        if filename.startswith(key):
            return GAMING_TOOL_NAMES[key]
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

            pattern = f'("{lang_code}":[\\s\\S]*?)(".*?":\\s*)("{english_escaped}")'

            def replacer(match):
                nonlocal updates_count
                updates_count += 1
                return match.group(1) + match.group(2) + '"' + translated_text + '"'

            content = re.sub(pattern, replacer, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return updates_count

def main():
    base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\js"

    print("="*60)
    print("GAMING & ENTERTAINMENT CATEGORY - COMPLETE TRANSLATION")
    print("="*60)
    print()

    # Apply translations in two passes
    total_updates = 0

    for filename in GAMING_FILES:
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
    print(f"FILES PROCESSED: {len(GAMING_FILES)}")
    print("="*60)

if __name__ == "__main__":
    main()
