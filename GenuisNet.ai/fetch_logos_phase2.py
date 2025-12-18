#!/usr/bin/env python3
import os
import requests
from pathlib import Path
import time

BASE_DIR = Path(__file__).parent
LOGOS_DIR = BASE_DIR / "assets" / "images" / "logos"

LOGOS_PHASE2 = {
    # Education
    'aleks': 'https://logo.clearbit.com/aleks.com',
    'carnegie-learning': 'https://logo.clearbit.com/carnegielearning.com',
    'knewton-alta': 'https://logo.clearbit.com/knewton.com',
    'querium': 'https://logo.clearbit.com/querium.com',
    'socratic-by-google': 'https://logo.clearbit.com/google.com',
    'squirrel-ai': 'https://logo.clearbit.com/squirrelai.com',
    'thinkster-math': 'https://logo.clearbit.com/hellothinkster.com',
    'cognii': 'https://logo.clearbit.com/cognii.com',

    # Analytics
    'looker': 'https://logo.clearbit.com/looker.com',
    'amazon-quicksight-q': 'https://logo.clearbit.com/aws.amazon.com',
    'prophet-meta': 'https://logo.clearbit.com/meta.com',

    # Sales
    'attention': 'https://logo.clearbit.com/attention.com',
    'exceedai': 'https://logo.clearbit.com/exceed.ai',
    'insidesales': 'https://logo.clearbit.com/insidesales.com',
    'regieai': 'https://logo.clearbit.com/regie.ai',
    'troopsai': 'https://logo.clearbit.com/troops.ai',

    # HR
    'fetcher': 'https://logo.clearbit.com/fetcher.ai',
    'findem': 'https://logo.clearbit.com/findem.ai',
    'humanly': 'https://logo.clearbit.com/humanly.io',
    'seekout': 'https://logo.clearbit.com/seekout.com',
    'sense': 'https://logo.clearbit.com/sense.com',

    # Legal
    'blue-j-legal': 'https://logo.clearbit.com/bluejlegal.com',
    'kira-systems': 'https://logo.clearbit.com/kirasystems.com',
    'lex-machina': 'https://logo.clearbit.com/lexmachina.com',
    'primer': 'https://logo.clearbit.com/primer.ai',
    'ravel-law': 'https://logo.clearbit.com/ravellaw.com',
    'ross-intelligence': 'https://logo.clearbit.com/rossintelligence.com',

    # Medical
    'butterfly-iq': 'https://logo.clearbit.com/butterflynetwork.com',
    'nuance-dragon': 'https://logo.clearbit.com/nuance.com',
    'tempus': 'https://logo.clearbit.com/tempus.com',
    'viz-ai': 'https://logo.clearbit.com/viz.ai',
    'zebra-medical': 'https://logo.clearbit.com/zebra-med.com',

    # Architecture
    'finch3d': 'https://logo.clearbit.com/finch3d.com',
    'arko-ai': 'https://logo.clearbit.com/arkoai.com',
    'testfit': 'https://logo.clearbit.com/testfit.io',
    'maket-ai': 'https://logo.clearbit.com/maket.ai',
    'veras-ai': 'https://logo.clearbit.com/evolvelab.io',

    # Gaming
    'artomatix': 'https://logo.clearbit.com/artomatix.com',
    'charismaai': 'https://logo.clearbit.com/charisma.ai',
    'hidden-door': 'https://logo.clearbit.com/hiddendoor.co',
    'latitude-ai-dungeon': 'https://logo.clearbit.com/latitude.io',
    'promethean-ai': 'https://logo.clearbit.com/prometheanai.com',
    'rct-ai': 'https://logo.clearbit.com/rct-studio.com',
    'rosebud-ai': 'https://logo.clearbit.com/rosebud.ai',

    # Research
    'connected-papers': 'https://logo.clearbit.com/connectedpapers.com',
    'irisai': 'https://logo.clearbit.com/iris.ai',
    'perplexity-research': 'https://logo.clearbit.com/perplexity.ai',
    'semantic-scholar': 'https://logo.clearbit.com/semanticscholar.org',
    'undermind': 'https://logo.clearbit.com/undermind.ai',

    # Translation
    'modernmt': 'https://logo.clearbit.com/modernmt.com',
    'systran': 'https://logo.clearbit.com/systran.com',

    # Quantum
    'xanadu-pennylane': 'https://logo.clearbit.com/xanadu.ai',

    # Others
    'windsurf': 'https://logo.clearbit.com/codeium.com',
    'looker-ai': 'https://logo.clearbit.com/looker.com',
    'cisco-ai': 'https://logo.clearbit.com/cisco.com',
}

def download_logo(name: str, url: str) -> bool:
    try:
        print(f"📥 {name}...", end=" ")
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200 and len(response.content) > 100:
            content_type = response.headers.get('content-type', '')
            if 'svg' in content_type:
                ext = '.svg'
            elif 'png' in content_type:
                ext = '.png'
            else:
                ext = '.png'

            file_path = LOGOS_DIR / f"{name}{ext}"
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f"✅")
            return True
        else:
            print(f"❌ (status: {response.status_code})")
            return False
    except Exception as e:
        print(f"❌ ({str(e)[:30]})")
        return False

def main():
    print("🚀 Phase 2 - Téléchargement des logos restants...\n")
    LOGOS_DIR.mkdir(parents=True, exist_ok=True)

    stats = {'success': 0, 'failed': 0, 'skipped': 0}

    for name, url in LOGOS_PHASE2.items():
        existing = list(LOGOS_DIR.glob(f"{name}.*"))
        if existing:
            print(f"⏭️  {name} (existe)")
            stats['skipped'] += 1
            continue

        if download_logo(name, url):
            stats['success'] += 1
        else:
            stats['failed'] += 1
        time.sleep(0.3)

    print(f"\n{'='*60}")
    print(f"✅ Téléchargés: {stats['success']}")
    print(f"❌ Échoués: {stats['failed']}")
    print(f"⏭️  Ignorés: {stats['skipped']}")
    print(f"✨ Terminé!")

if __name__ == "__main__":
    main()
