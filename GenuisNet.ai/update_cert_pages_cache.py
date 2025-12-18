#!/usr/bin/env python3
"""
Add cache-buster to all certification badge images in certification detail pages
This forces browsers to reload the official Credly logos
"""

import re
from pathlib import Path

def add_cache_buster(html_content):
    """Add ?v=credly to certification image URLs that don't have it yet"""

    # Pattern to match certification images without cache buster
    pattern = r'(assets/images/certifications/[^"\']+\.png)(?!\?v=)'

    # Replace with cache buster
    updated = re.sub(pattern, r'\1?v=credly', html_content)

    return updated

def main():
    cert_dir = Path('pages/certifications')
    updated_count = 0

    print("🔄 Adding cache-buster to certification detail pages...")
    print()

    for html_file in sorted(cert_dir.glob('*.html')):
        try:
            # Read file
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Check if already has cache buster
            if '?v=credly' in content:
                print(f"✓ {html_file.name} - Already updated")
                continue

            # Add cache buster
            updated = add_cache_buster(content)

            if updated != content:
                # Write back
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(updated)

                updated_count += 1
                print(f"✓ {html_file.name} - Updated")
            else:
                print(f"○ {html_file.name} - No changes needed")

        except Exception as e:
            print(f"✗ {html_file.name} - Error: {e}")

    print()
    print(f"✅ Updated {updated_count} certification pages with cache-busters!")
    print()
    print("📋 All certification logos will now reload from cache")

if __name__ == '__main__':
    main()
