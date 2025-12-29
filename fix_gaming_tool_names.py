#!/usr/bin/env python3
"""
Fix incorrect tool names in Gaming i18n translations
Some translations reference wrong tool names (e.g., "Paradox (Olivia)" instead of "Inworld AI")
"""

import re
import os

GAMING_FILES = {
    "artomatix-i18n.js": "Artomatix",
    "charismaai-i18n.js": "Charisma.ai",
    "hidden-door-i18n.js": "Hidden Door",
    "inworld-ai-i18n.js": "Inworld AI",
    "latitude-ai-dungeon-i18n.js": "AI Dungeon",
    "ludoai-i18n.js": "Ludo.ai",
    "promethean-ai-i18n.js": "Promethean AI",
    "rct-ai-i18n.js": "RCT AI",
    "replika-i18n.js": "Replika",
    "rosebud-ai-i18n.js": "Rosebud AI",
    "scenario-i18n.js": "Scenario"
}

# List of all tool names that might appear incorrectly
ALL_TOOL_NAMES = [
    "Artomatix", "Charisma.ai", "Hidden Door", "Inworld AI", "AI Dungeon",
    "Ludo.ai", "Promethean AI", "RCT AI", "Replika", "Rosebud AI", "Scenario",
    # Also include variations
    "Inworld Ai", "Paradox (Olivia)", "Paradox（Olivia）",  # Common mistakes
    "Beamery", "Eightfold.ai", "Fetcher", "Findem", "Harver", "HireVue",  # HR tools
    "DeepL Pro", "Google Translate", "Lilt", "Lokalise"  # Translation tools
]

def fix_tool_names(filepath, correct_tool_name):
    """Replace incorrect tool names with the correct one"""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    fixes = 0

    # Replace any incorrect tool name with the correct one
    for wrong_name in ALL_TOOL_NAMES:
        if wrong_name != correct_tool_name:
            # Only replace within translation values (after :)
            # This regex finds tool names in translation values, not in keys
            pattern = r'(:\s*")([^"]*?)' + re.escape(wrong_name) + r'([^"]*?)(")'

            def replacer(match):
                nonlocal fixes
                # Check if this is really a tool name replacement context
                before = match.group(2)
                after = match.group(3)

                # Replace the tool name
                fixes += 1
                return match.group(1) + before + correct_tool_name + after + match.group(4)

            content = re.sub(pattern, replacer, content)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return fixes

    return 0

def main():
    base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\js"

    print("="*60)
    print("FIXING INCORRECT TOOL NAMES IN GAMING TRANSLATIONS")
    print("="*60)
    print()

    total_fixes = 0

    for filename, correct_name in GAMING_FILES.items():
        filepath = os.path.join(base_dir, filename)
        if not os.path.exists(filepath):
            print(f"[SKIP] File not found: {filename}")
            continue

        fixes = fix_tool_names(filepath, correct_name)
        if fixes > 0:
            print(f"[OK] {filename}: {fixes} tool name corrections")
            total_fixes += fixes
        else:
            print(f"[SKIP] {filename}: no incorrect names found")

    print()
    print("="*60)
    print(f"TOTAL TOOL NAME CORRECTIONS: {total_fixes}")
    print("="*60)

if __name__ == "__main__":
    main()
