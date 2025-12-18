#!/usr/bin/env python3
"""
Update all HTML files to use the real downloaded logos (PNG/SVG)
instead of the generated SVG with initials
"""

import re
from pathlib import Path

BASE_DIR = Path("/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai")
REVIEWS_DIR = BASE_DIR / "pages" / "reviews"
ASSETS_DIR = BASE_DIR / "assets" / "images" / "tools"

def find_logo_file(category, tool_name):
    """Find the actual logo file (PNG or SVG)"""
    category_dir = ASSETS_DIR / category

    # Check for PNG first
    png_file = category_dir / f"{tool_name}.png"
    if png_file.exists():
        return f"{tool_name}.png"

    # Then check for SVG
    svg_file = category_dir / f"{tool_name}.svg"
    if svg_file.exists():
        return f"{tool_name}.svg"

    return None

def update_review_file(html_file):
    """Update a review file to use the real logo"""
    try:
        content = html_file.read_text(encoding='utf-8')
        original_content = content

        category = html_file.parent.name
        tool_name = html_file.stem

        # Find the actual logo file
        logo_file = find_logo_file(category, tool_name)

        if not logo_file:
            return False, "No logo file found"

        logo_path = f"../../../assets/images/tools/{category}/{logo_file}"

        # Update the img src in tool-logo-xl div
        pattern = r'(<div class="tool-logo-xl">\s*<img src=")[^"]+(" alt="[^"]+")'
        replacement = rf'\1{logo_path}\2'

        content = re.sub(pattern, replacement, content)

        # Also update any other references to the logo
        old_svg_pattern = rf'assets/images/tools/{category}/{tool_name}\.svg'
        content = re.sub(old_svg_pattern, f'assets/images/tools/{category}/{logo_file}', content)

        if content != original_content:
            html_file.write_text(content, encoding='utf-8')
            return True, f"Updated to {logo_file}"

        return False, "No changes needed"

    except Exception as e:
        return False, f"Error: {e}"

def update_all_reviews():
    """Update all review files with real logos"""
    updated = 0
    skipped = 0
    errors = 0

    for category_dir in sorted(REVIEWS_DIR.iterdir()):
        if category_dir.is_dir() and not category_dir.name.startswith('.'):
            print(f"\n{category_dir.name.upper()}:")

            for html_file in sorted(category_dir.glob('*.html')):
                success, message = update_review_file(html_file)

                if success:
                    print(f"  ✓ {html_file.name} - {message}")
                    updated += 1
                elif "Error" in message:
                    print(f"  ✗ {html_file.name} - {message}")
                    errors += 1
                else:
                    skipped += 1

    return updated, skipped, errors

if __name__ == "__main__":
    print("=" * 70)
    print("UPDATING ALL REVIEWS TO USE REAL OFFICIAL LOGOS")
    print("=" * 70)

    updated, skipped, errors = update_all_reviews()

    print()
    print("=" * 70)
    print(f"Summary:")
    print(f"  ✅ Updated: {updated} files")
    print(f"  ⊘  Skipped: {skipped} files (no changes)")
    print(f"  ✗  Errors: {errors} files")
    print("=" * 70)
