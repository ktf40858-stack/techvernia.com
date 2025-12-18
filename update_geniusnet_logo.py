#!/usr/bin/env python3
"""
Script to update GenuisNet.ai logo in all review pages
Replace inline SVG with logo-neon.svg image
"""

import os
import re
from pathlib import Path

# Base directory
BASE_DIR = Path("/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai")
REVIEWS_DIR = BASE_DIR / "pages" / "reviews"

# Old logo pattern (inline SVG)
OLD_LOGO_PATTERN = r'<a href="\.\.\/\.\.\/\.\.\/index\.html" class="logo">\s*<span class="logo-icon"><svg[^>]*>.*?<\/svg><\/span>\s*<span class="logo-text">Genuis<span class="highlight">Net<\/span>\.ai<\/span>\s*<\/a>'

# New logo HTML
NEW_LOGO_HTML = '''<a href="../../../index.html" class="logo">
                <img src="../../../assets/images/logo-neon.svg" alt="GenuisNet.ai" style="height: 50px; width: auto;">
            </a>'''

def update_logo_in_file(file_path):
    """Update the GenuisNet.ai logo in a review file"""
    try:
        # Read file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if already has the new logo
        if 'logo-neon.svg' in content:
            return False, "Already updated"

        # Check if has old logo pattern
        if not re.search(OLD_LOGO_PATTERN, content, re.DOTALL):
            return False, "No logo pattern found"

        # Replace old logo with new one
        new_content = re.sub(OLD_LOGO_PATTERN, NEW_LOGO_HTML, content, flags=re.DOTALL)

        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        return True, "Updated"

    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    """Main function to update all review logos"""
    print("🔄 Updating GenuisNet.ai logo in all review pages...\n")

    updated_count = 0
    skipped_count = 0
    error_count = 0

    # Process each category
    for category_dir in sorted(REVIEWS_DIR.iterdir()):
        if not category_dir.is_dir():
            continue

        category_updated = 0
        print(f"📁 Processing {category_dir.name}/")

        # Process each review file
        for review_file in sorted(category_dir.glob("*.html")):
            success, message = update_logo_in_file(review_file)

            if success:
                print(f"  ✅ {review_file.stem}")
                updated_count += 1
                category_updated += 1
            elif "Error" in message:
                print(f"  ❌ {review_file.stem} - {message}")
                error_count += 1
            else:
                skipped_count += 1

        if category_updated > 0:
            print(f"  → {category_updated} files updated in {category_dir.name}")
        print()

    print("=" * 60)
    print(f"✅ Updated: {updated_count} files")
    print(f"⏭️  Skipped: {skipped_count} files (already updated)")
    print(f"❌ Errors: {error_count} files")
    print("=" * 60)

if __name__ == "__main__":
    main()
