#!/usr/bin/env python3
"""
Add cache-buster to all certification badge images in cybersecurity review pages
This forces browsers to reload the official Credly logos
"""

import re
from pathlib import Path

# Pages with certifications
PAGES = [
    'cisco-securex',
    'cortex-xdr',
    'crowdstrike',
    'cyberark',
    'darktrace',
    'fortinet',
    'ibm-qradar',
    'microsoft-sentinel',
    'okta',
    'palo-alto-ngfw',
    'qualys',
    'rapid7',
    'sentinelone',
    'sophos-interceptx',
    'splunk-security',
    'tenable',
    'trend-micro-vision-one'
]

def add_cache_buster(html_content):
    """Add ?v=credly to certification image URLs that don't have it yet"""

    # Pattern to match certification images without cache buster
    pattern = r'(assets/images/certifications/[^"\']+\.png)(?!\?v=)'

    # Replace with cache buster
    updated = re.sub(pattern, r'\1?v=credly', html_content)

    return updated

def main():
    review_dir = Path('pages/reviews/cybersecurity')
    updated_count = 0

    print("🔄 Adding cache-buster to certification logos...")
    print()

    for page_name in PAGES:
        html_file = review_dir / f"{page_name}.html"

        if not html_file.exists():
            print(f"⚠️  {page_name}.html - Not found")
            continue

        try:
            # Read file
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Check if already has cache buster
            if '?v=credly' in content:
                # Count how many cert images exist
                cert_count = len(re.findall(r'assets/images/certifications/[^"\']+\.png\?v=credly', content))
                print(f"✓ {page_name}.html - Already updated ({cert_count} certs)")
                continue

            # Add cache buster
            updated = add_cache_buster(content)

            # Count changes
            cert_count = len(re.findall(r'assets/images/certifications/[^"\']+\.png\?v=credly', updated))

            if updated != content:
                # Write back
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(updated)

                updated_count += 1
                print(f"✓ {page_name}.html - Updated ({cert_count} certs)")
            else:
                print(f"○ {page_name}.html - No changes needed")

        except Exception as e:
            print(f"✗ {page_name}.html - Error: {e}")

    print()
    print(f"✅ Updated {updated_count} pages with cache-busters!")
    print()
    print("📋 All certification logos now point to official Credly badges")

if __name__ == '__main__':
    main()
