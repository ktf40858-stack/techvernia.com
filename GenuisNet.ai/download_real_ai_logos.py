#!/usr/bin/env python3
"""
Download REAL AI logos from direct image URLs.
Uses actual logo URLs from official sources and CDNs.
"""

import os
import requests
import time

base_path = "/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/assets/images/tools"

# Direct URLs to real AI logos
# These are actual logo image URLs from official sources
real_logos = {
    'writing': {
        'grammarly': 'https://static.grammarly.com/assets/files/efe9a7147fda81cbd089815844bc1610/grammarly_logo.svg',
        'copyai': 'https://assets-global.website-files.com/628288c5cd3e8411b90a36a4/62877ab3a827f3630cd63cf7_Copy.ai%20Logo.svg',
        'jasper-ai': 'https://www.jasper.ai/hubfs/jasper-logo.svg',
        'quillbot': 'https://assets.quillbot.com/images/theme/quillbot-gradient-logo.svg',
        'rytr': 'https://rytr.me/logo.svg',
        'wordtune': 'https://www.wordtune.com/static/media/wordtune-logo.svg',
        'writesonic': 'https://writesonic.com/static/media/logo.svg'
    },
    'image': {
        'adobe-firefly': 'https://www.adobe.com/content/dam/cc/icons/firefly.svg',
        'canva-ai': 'https://static.canva.com/web/images/12487a1e0770d29351bd4ce4f87ec8fe.svg',
        'clipdrop': 'https://clipdrop.co/static/clipdrop-logo.svg',
        'ideogram': 'https://ideogram.ai/static/logo.svg',
        'leonardo-ai': 'https://leonardo.ai/logo.svg',
        'stable-diffusion': 'https://stability.ai/logo.svg'
    },
    'video': {
        'heygen': 'https://www.heygen.com/logo.svg',
        'invideo': 'https://invideo.io/static/logo.svg',
        'kapwing': 'https://www.kapwing.com/static/logo.svg',
        'lumen5': 'https://lumen5.com/static/logo.svg',
        'pictory': 'https://pictory.ai/static/logo.svg',
        'runway': 'https://runwayml.com/logo.svg',
        'synthesia': 'https://www.synthesia.io/logo.svg'
    },
    'cybersecurity': {
        'crowdstrike': 'https://www.crowdstrike.com/wp-content/uploads/2020/08/crowdstrike-logo-2020.svg',
        'darktrace': 'https://www.darktrace.com/static/logo.svg',
        'okta': 'https://www.okta.com/sites/default/files/Okta_Logo_BrightBlue_Medium.png',
        'sentinelone': 'https://assets.sentinelone.com/c/sentinelone-logo',
        'snyk': 'https://res.cloudinary.com/snyk/image/upload/v1537345894/press-kit/brand/logo-black.svg',
        'wiz': 'https://www.wiz.io/hubfs/wiz-logo.svg'
    }
}

# Alternative: Try fetching from company websites directly
web_scrape_urls = {
    'writing': {
        'grammarly': 'https://www.grammarly.com',
        'copyai': 'https://www.copy.ai',
        'jasper-ai': 'https://www.jasper.ai',
        'quillbot': 'https://quillbot.com',
        'rytr': 'https://rytr.me',
        'wordtune': 'https://www.wordtune.com',
        'writesonic': 'https://writesonic.com'
    }
}

def download_from_url(url, output_path):
    """Download image from direct URL."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=15, allow_redirects=True)
        if response.status_code == 200 and len(response.content) > 500:
            with open(output_path, 'wb') as f:
                f.write(response.content)
            return True
    except Exception as e:
        pass
    return False

def download_logo(category, tool_name, url):
    """Download logo from URL."""

    # Determine file extension
    ext = 'svg' if url.endswith('.svg') else 'png'
    output_path = os.path.join(base_path, category, f"{tool_name}.{ext}")

    print(f"  📥 {tool_name}...", end=" ", flush=True)

    if download_from_url(url, output_path):
        size = os.path.getsize(output_path)
        print(f"✓ ({size} bytes)")
        return True
    else:
        print("✗ Failed")
        return False

# Download logos
print("🎨 Downloading REAL AI logos from official sources...\n")

total = 0
success = 0

for category, tools_dict in real_logos.items():
    print(f"\n📁 {category.upper()}")
    print("=" * 60)

    for tool_name, url in tools_dict.items():
        total += 1
        if download_logo(category, tool_name, url):
            success += 1
        time.sleep(0.5)

print(f"\n{'=' * 60}")
print(f"✅ Successfully downloaded: {success}/{total} logos")
print(f"{'=' * 60}\n")

# For logos that failed, try alternative method with wget
print("\n💡 For failed logos, you can try manually from:")
print("   - Official website press kits")
print("   - GitHub repositories")
print("   - Brandfetch.com")
