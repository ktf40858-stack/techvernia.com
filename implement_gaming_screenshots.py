#!/usr/bin/env python3
"""
Implement real screenshots for Gaming category
Copy screenshots from source folder and update HTML files
"""

import os
import shutil
import re

# Screenshot mappings: source filename -> (destination filename, tool name)
SCREENSHOT_MAPPINGS = {
    "artomatix.webp": ("artomatix.webp", "Artomatix"),
    "Charisma.ai.webp": ("charismaai.webp", "Charisma.ai"),
    "Hidden Door.jpg": ("hidden-door.jpg", "Hidden Door"),
    "inworld-ai.jpg": ("inworld-ai.jpg", "Inworld AI"),
    "Latitude (AI Dungeon)": ("latitude-ai-dungeon.jpg", "Latitude (AI Dungeon)"),
    "Ludo.ai.jpg": ("ludoai.jpg", "Ludo.ai"),
    "Promethean AI": ("promethean-ai.jpg", "Promethean AI"),
    "Rct AI.jpg": ("rct-ai.jpg", "RCT AI"),
    "Replika.png": ("replika.png", "Replika"),
    "Rosebud_AI_screenshot.png": ("rosebud-ai.png", "Rosebud AI"),
    "Scenario.png": ("scenario.png", "Scenario")
}

# HTML file mappings: html filename -> screenshot filename
HTML_SCREENSHOT_MAP = {
    "artomatix.html": "artomatix.webp",
    "charismaai.html": "charismaai.webp",
    "hidden-door.html": "hidden-door.jpg",
    "inworld-ai.html": "inworld-ai.jpg",
    "latitude-ai-dungeon.html": "latitude-ai-dungeon.jpg",
    "ludoai.html": "ludoai.jpg",
    "promethean-ai.html": "promethean-ai.jpg",
    "rct-ai.html": "rct-ai.jpg",
    "replika.html": "replika.png",
    "rosebud-ai.html": "rosebud-ai.png",
    "scenario.html": "scenario.png"
}

def copy_screenshots():
    """Copy screenshots from source to destination with correct names"""

    source_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\screenshot\AI Gaming"
    dest_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\assets\screenshots\gaming"

    print("="*60)
    print("COPYING GAMING SCREENSHOTS")
    print("="*60)
    print()

    copied = 0

    for source_file, (dest_file, tool_name) in SCREENSHOT_MAPPINGS.items():
        source_path = os.path.join(source_dir, source_file)
        dest_path = os.path.join(dest_dir, dest_file)

        if not os.path.exists(source_path):
            print(f"[SKIP] Source not found: {source_file}")
            continue

        # Copy file
        shutil.copy2(source_path, dest_path)
        file_size = os.path.getsize(dest_path) / 1024  # Size in KB
        print(f"[OK] {tool_name}: {dest_file} ({file_size:.1f} KB)")
        copied += 1

    print()
    print(f"Total screenshots copied: {copied}")
    return copied

def update_html_screenshots():
    """Update HTML files to use the correct screenshot files"""

    html_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\pages\reviews\gaming"

    print()
    print("="*60)
    print("UPDATING HTML FILES WITH SCREENSHOTS")
    print("="*60)
    print()

    updated = 0

    for html_file, screenshot_file in HTML_SCREENSHOT_MAP.items():
        html_path = os.path.join(html_dir, html_file)

        if not os.path.exists(html_path):
            print(f"[SKIP] HTML not found: {html_file}")
            continue

        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Pattern to match the screenshot img tag
        # Current: src="../../../assets/screenshots/gaming/SOMETHING.png"
        # Update to: src="../../../assets/screenshots/gaming/CORRECT_FILE.EXT"

        pattern = r'(src="../../../assets/screenshots/gaming/)([^"]+)(")'
        replacement = f'\\1{screenshot_file}\\3'

        content = re.sub(pattern, replacement, content)

        if content != original_content:
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[OK] {html_file} -> {screenshot_file}")
            updated += 1
        else:
            print(f"[NO CHANGE] {html_file}")

    print()
    print(f"Total HTML files updated: {updated}")
    return updated

def main():
    print("GAMING SCREENSHOTS IMPLEMENTATION")
    print()

    # Step 1: Copy screenshots
    copied = copy_screenshots()

    # Step 2: Update HTML files
    updated = update_html_screenshots()

    print()
    print("="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Screenshots copied: {copied}")
    print(f"HTML files updated: {updated}")
    print()
    print("Gaming screenshots implementation complete!")

if __name__ == "__main__":
    main()
