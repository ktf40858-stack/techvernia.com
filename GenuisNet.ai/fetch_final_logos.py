#!/usr/bin/env python3
import requests
from pathlib import Path
import time

BASE_DIR = Path(__file__).parent
LOGOS_DIR = BASE_DIR / "assets" / "images" / "logos"

# Derniers logos avec URLs alternatives
FINAL_LOGOS = {
    'windsurf': 'https://raw.githubusercontent.com/Exafunction/codeium.vim/main/codeium.png',
    'looker': 'https://www.gstatic.com/pantheon/images/welcome/supercloud/looker_icon_new.svg',
    'looker-ai': 'https://www.gstatic.com/pantheon/images/welcome/supercloud/looker_icon_new.svg',
    'undermind': 'https://logo.clearbit.com/undermind.com',
    'arko-ai': 'https://logo.clearbit.com/arko.build',
    'architechtures': 'https://logo.clearbit.com/autodesk.com',  # Placeholder
}

def download_logo(name: str, url: str) -> bool:
    try:
        print(f"📥 {name}...", end=" ")
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(url, headers=headers, timeout=10, allow_redirects=True)

        if response.status_code == 200 and len(response.content) > 100:
            content_type = response.headers.get('content-type', '')
            if 'svg' in content_type or url.endswith('.svg'):
                ext = '.svg'
            elif 'png' in content_type or url.endswith('.png'):
                ext = '.png'
            else:
                ext = '.png'

            file_path = LOGOS_DIR / f"{name}{ext}"
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f"✅")
            return True
        else:
            print(f"❌ (status: {response.status_code}, size: {len(response.content)})")
            return False
    except Exception as e:
        print(f"❌ ({str(e)[:40]})")
        return False

print("🚀 Phase Finale - Derniers logos...\n")
LOGOS_DIR.mkdir(parents=True, exist_ok=True)

stats = {'success': 0, 'failed': 0}

for name, url in FINAL_LOGOS.items():
    existing = list(LOGOS_DIR.glob(f"{name}.*"))
    if existing:
        print(f"⏭️  {name} (existe)")
        continue

    if download_logo(name, url):
        stats['success'] += 1
    else:
        stats['failed'] += 1
    time.sleep(0.5)

print(f"\n{'='*60}")
print(f"✅ Téléchargés: {stats['success']}")
print(f"❌ Échoués: {stats['failed']}")
