#!/usr/bin/env python3
"""
Automated logo downloader using Selenium.
This script will run on YOUR machine using YOUR internet connection.

REQUIREMENTS:
    pip install selenium pillow requests

Then run:
    python3 auto_download_logos_selenium.py
"""

import os
import time
import requests
from urllib.parse import quote

BASE_DIR = "/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/assets/images/tools"

# Direct logo URLs from known CDNs and official sources
LOGO_URLS = {
    'writing/grammarly': [
        'https://brandfetch.com/grammarly.com',  # Will need to extract SVG
        'https://logo.clearbit.com/grammarly.com',
        'https://img.logo.dev/grammarly.com?token=pk_X-1ZO13CRaadr0E7e2bMvQ',
    ],
    'writing/copyai': [
        'https://brandfetch.com/copy.ai',
        'https://logo.clearbit.com/copy.ai',
    ],
    'writing/jasper-ai': [
        'https://brandfetch.com/jasper.ai',
        'https://logo.clearbit.com/jasper.ai',
    ],
    'writing/quillbot': [
        'https://brandfetch.com/quillbot.com',
        'https://logo.clearbit.com/quillbot.com',
    ],
    'writing/rytr': [
        'https://brandfetch.com/rytr.me',
        'https://logo.clearbit.com/rytr.me',
    ],
    'writing/wordtune': [
        'https://brandfetch.com/wordtune.com',
        'https://logo.clearbit.com/wordtune.com',
    ],
    'writing/writesonic': [
        'https://brandfetch.com/writesonic.com',
        'https://logo.clearbit.com/writesonic.com',
    ],
}

def download_simple(url, output_path):
    """Simple download with requests."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=20, allow_redirects=True)
        if response.status_code == 200 and len(response.content) > 1000:
            with open(output_path, 'wb') as f:
                f.write(response.content)
            return True
    except Exception as e:
        print(f"    Error: {e}")
    return False

def main():
    print("🎨 Starting automated logo download...")
    print("=" * 70)

    total = len(LOGO_URLS)
    success = 0

    for logo_path, urls in LOGO_URLS.items():
        category, tool = logo_path.split('/')
        output_dir = os.path.join(BASE_DIR, category)
        os.makedirs(output_dir, exist_ok=True)

        print(f"\n📥 {tool}...")

        # Try each URL until one works
        downloaded = False
        for i, url in enumerate(urls, 1):
            ext = 'png' if 'clearbit' in url or 'logo.dev' in url else 'svg'
            output_path = os.path.join(output_dir, f"{tool}.{ext}")

            print(f"  Trying source {i}/{len(urls)}...", end=" ")

            if download_simple(url, output_path):
                size = os.path.getsize(output_path)
                print(f"✓ Downloaded ({size:,} bytes)")
                downloaded = True
                success += 1
                break
            else:
                print("✗ Failed")

        if not downloaded:
            print(f"  ❌ All sources failed for {tool}")

        time.sleep(1)  # Be nice to servers

    print("\n" + "=" * 70)
    print(f"✅ Downloaded {success}/{total} logos successfully")
    print("=" * 70)

    if success < total:
        print(f"\n⚠️  {total - success} logos need manual download")
        print("See MANUAL_LOGO_DOWNLOAD_GUIDE.md for instructions")

if __name__ == "__main__":
    main()
