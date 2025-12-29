#!/usr/bin/env python3
"""
Add tool-specific i18n scripts to Gaming category HTML files
"""

import os
import re

# Mapping of HTML files to their i18n script files
GAMING_SCRIPTS = {
    "artomatix.html": "artomatix-i18n.js",
    "charismaai.html": "charismaai-i18n.js",
    "hidden-door.html": "hidden-door-i18n.js",
    "inworld-ai.html": "inworld-ai-i18n.js",
    "latitude-ai-dungeon.html": "latitude-ai-dungeon-i18n.js",
    "ludoai.html": "ludoai-i18n.js",
    "promethean-ai.html": "promethean-ai-i18n.js",
    "rct-ai.html": "rct-ai-i18n.js",
    "replika.html": "replika-i18n.js",
    "rosebud-ai.html": "rosebud-ai-i18n.js",
    "scenario.html": "scenario-i18n.js"
}

def add_i18n_script(filepath, script_name):
    """Add tool-specific i18n script to HTML file"""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if script already exists
    if script_name in content:
        return False  # Already exists

    # Add the script after nav-i18n.js
    pattern = r'(<script src="../../../js/nav-i18n\.js"></script>)'
    replacement = f'\\1\n<script src="../../../js/{script_name}"></script>'

    updated_content = re.sub(pattern, replacement, content)

    # If no nav-i18n.js found, add before </body>
    if updated_content == content:
        pattern = r'(</body>)'
        replacement = f'<script src="../../../js/{script_name}"></script>\n\\1'
        updated_content = re.sub(pattern, replacement, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    return True

def main():
    base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\pages\reviews\gaming"

    print("="*60)
    print("ADDING TOOL-SPECIFIC i18n SCRIPTS TO GAMING CATEGORY")
    print("="*60)
    print()

    added_count = 0
    skipped_count = 0

    for html_file, script_file in GAMING_SCRIPTS.items():
        filepath = os.path.join(base_dir, html_file)
        if not os.path.exists(filepath):
            print(f"[SKIP] File not found: {html_file}")
            continue

        try:
            if add_i18n_script(filepath, script_file):
                print(f"[ADDED] {html_file} -> {script_file}")
                added_count += 1
            else:
                print(f"[EXISTS] {html_file} (script already present)")
                skipped_count += 1
        except Exception as e:
            print(f"[ERROR] {html_file}: {str(e)}")

    print()
    print("="*60)
    print(f"SCRIPTS ADDED: {added_count}")
    print(f"ALREADY EXISTS: {skipped_count}")
    print(f"TOTAL PROCESSED: {added_count + skipped_count}/{len(GAMING_SCRIPTS)}")
    print("="*60)

if __name__ == "__main__":
    main()
