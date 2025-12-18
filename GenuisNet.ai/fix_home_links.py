#!/usr/bin/env python3
"""
Fix Home Links in All Pages
This script fixes broken home/index.html links to use correct relative paths
"""

import os
import re
from pathlib import Path

def get_relative_path_to_root(file_path):
    """Calculate relative path from file to root"""
    depth = len(Path(file_path).relative_to('.').parts) - 1
    return '../' * depth if depth > 0 else './'

def fix_home_links(content, file_path):
    """Fix home/index.html links to use correct relative path"""
    relative_root = get_relative_path_to_root(file_path)
    index_path = f"{relative_root}index.html"

    changes_made = False

    # Fix navigation Home links that are incorrect
    # Pattern: href="index.html" when not in root
    if file_path != 'index.html' and 'href="index.html"' in content:
        # Replace href="index.html" with correct path
        content = re.sub(
            r'href="index\.html"',
            f'href="{index_path}"',
            content
        )
        changes_made = True
        print(f"  ✅ Fixed href='index.html' -> href='{index_path}'")

    # Fix logo links
    if file_path != 'index.html':
        # Check if logo link is wrong
        if re.search(r'class="logo"[^>]*href="[^"]*index\.html"', content):
            # Should already be correct (../../index.html), verify
            pass

    return content, changes_made

def process_file(file_path):
    """Process a single HTML file"""
    print(f"\nProcessing: {file_path}")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        content, changes_made = fix_home_links(content, file_path)

        if changes_made:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  💾 Saved changes")
            return True
        else:
            print(f"  ℹ️  No changes needed")
            return False

    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False

def main():
    """Main function"""
    print("=" * 70)
    print("Fixing Home Links in All Pages")
    print("=" * 70)

    fixed_count = 0
    total_count = 0

    # Process all HTML files
    for root, dirs, files in os.walk('pages'):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                total_count += 1
                if process_file(file_path):
                    fixed_count += 1

    print("\n" + "=" * 70)
    print(f"✅ Complete! Fixed {fixed_count} out of {total_count} files")
    print("=" * 70)

    print("\n🧪 Test Instructions:")
    print("1. Open http://localhost:8000")
    print("2. Navigate to any category page")
    print("3. Click on 'Home' in the navigation")
    print("4. You should return to the homepage! ✅")

if __name__ == '__main__':
    main()
