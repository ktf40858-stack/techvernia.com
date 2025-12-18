#!/usr/bin/env python3
"""
Update all review HTML files to use SVG logos instead of text placeholders
"""

import re
from pathlib import Path

BASE_DIR = Path("/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai")
REVIEWS_DIR = BASE_DIR / "pages" / "reviews"

def update_review_file(html_file):
    """Update a single review file to use SVG logo"""
    try:
        content = html_file.read_text(encoding='utf-8')
        original_content = content

        # Get category and tool name from path
        category = html_file.parent.name
        tool_name = html_file.stem

        # Build the logo path
        logo_path = f"../../../assets/images/tools/{category}/{tool_name}.svg"

        # Pattern 1: Replace the onerror fallback pattern
        # Old: onerror="this.style.display='none'; this.parentElement.innerHTML='XX';"
        # New: Just remove the onerror, as SVG will always work
        pattern1 = r'<img src="[^"]*" alt="([^"]*)" onerror="[^"]*">'
        replacement1 = f'<img src="{logo_path}" alt="\\1">'
        content = re.sub(pattern1, replacement1, content)

        # Pattern 2: Update any existing logo src paths
        pattern2 = r'<img src="[^"]*assets/images/tools/[^"]*"'
        replacement2 = f'<img src="{logo_path}"'
        content = re.sub(pattern2, replacement2, content)

        # Pattern 3: Handle cases where img might not exist yet
        # Look for tool-logo-xl div without img
        if '<div class="tool-logo-xl">' in content and '<img' not in content[content.find('<div class="tool-logo-xl">'):content.find('</div>', content.find('<div class="tool-logo-xl">'))]:
            # Find the tool name from the h1
            h1_match = re.search(r'<h1>([^<]+?)\s+Review', content)
            if h1_match:
                tool_display_name = h1_match.group(1)
                # Replace the div content
                old_pattern = r'(<div class="tool-logo-xl">)([^<]*)(</div>)'
                new_content = f'\\1\n                    <img src="{logo_path}" alt="{tool_display_name} Logo">\n                \\3'
                content = re.sub(old_pattern, new_content, content)

        # Only write if content changed
        if content != original_content:
            html_file.write_text(content, encoding='utf-8')
            return True
        return False

    except Exception as e:
        print(f"Error updating {html_file}: {e}")
        return False

def update_all_reviews():
    """Update all review files"""
    updated = 0
    skipped = 0

    for category_dir in REVIEWS_DIR.iterdir():
        if category_dir.is_dir() and not category_dir.name.startswith('.'):
            print(f"\nProcessing {category_dir.name}...")

            for html_file in category_dir.glob('*.html'):
                if update_review_file(html_file):
                    print(f"  ✓ Updated {html_file.name}")
                    updated += 1
                else:
                    skipped += 1

    return updated, skipped

if __name__ == "__main__":
    print("=" * 70)
    print("UPDATING ALL REVIEW PAGES TO USE SVG LOGOS")
    print("=" * 70)

    updated, skipped = update_all_reviews()

    print()
    print("=" * 70)
    print(f"✅ Updated: {updated} files")
    print(f"⊘  Skipped: {skipped} files (no changes needed)")
    print("=" * 70)
