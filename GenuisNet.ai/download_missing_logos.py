#!/usr/bin/env python3
"""
Télécharge les logos manquants avec des URLs alternatives
"""

from pathlib import Path
import requests
import time

# URLs alternatives pour les logos manquants
ALTERNATIVE_LOGO_URLS = {
    # AI Chatbots
    'Microsoft Copilot': 'https://img.logo dev/microsoft.com',
    'Character.AI': 'https://avatars.githubusercontent.com/u/102937211?s=200&v=4',
    'Pi': 'https://pi.ai/favicon.png',
    'YouChat': 'https://you.com/apple-touch-icon.png',
    'Mistral Chat': 'https://mistral.ai/favicon.svg',

    # AI Writing
    'Jasper': 'https://www.jasper.ai/apple-touch-icon.png',
    'Copy.ai': 'https://img.logoipsum.com/244.svg',  # Placeholder
    'Writesonic': 'https://app.writesonic.com/favicon.svg',
    'Wordtune': 'https://www.wordtune.com/apple-touch-icon.png',
    'Sudowrite': 'https://assets.sudowrite.com/favicon.ico',
    'Scalenut': 'https://www.scalenut.com/wp-content/uploads/2022/01/scalenut-icon.png',
    'Frase': 'https://www.frase.io/favicon-32x32.png',
    'Grammarly': 'https://static.grammarly.com/assets/files/efe8d9d0a30566208c3ff9b3b12e5447/favicon.svg',

    # AI Coding
    'GitHub Copilot': 'https://github.com/github-copilot.png',
    'Replit AI': 'https://replit.com/public/icons/apple-touch-icon-180x180.png',
    'Blackbox AI': 'https://www.useblackbox.io/favicon.ico',
    'Phind': 'https://www.phind.com/apple-touch-icon.png',
    'Bito AI': 'https://alpha.bito.ai/wp-content/uploads/2023/01/bito-logo-v1.png',
    'AlphaCode': 'https://deepmind.google/static/documents/alphacode-a-competitive-level-code-generation-system.pdf',  # Fallback

    # AI Image
    'Midjourney': 'https://cdn.discordapp.com/attachments/1008571220776316978/1070553771024957440/midjourney-logo.png',
    'DALL-E 3': 'https://openai.com/content/images/2023/01/openai-avatar.png',
    'Ideogram': 'https://ideogram.ai/assets/progressive-image.png',
    'Runway ML': 'https://assets-global.website-files.com/6502f2947448aa18a3e1aef4/650362fee8bb25ad0be7d5e0_Logo%20SVG%20White.svg',

    # AI Video
    'Runway Gen-2': 'https://assets-global.website-files.com/6502f2947448aa18a3e1aef4/650362fee8bb25ad0be7d5e0_Logo%20SVG%20White.svg',
    'Synthesia': 'https://www.synthesia.io/hubfs/Synthesia%202023/favicon.png',
    'Descript': 'https://www.descript.com/assets/favicon-48x48.png',
    'Lumen5': 'https://lumen5.com/learn/wp-content/uploads/2019/12/Lumen5-icon-128x128-1.png',
    'OpusClip': 'https://www.opus.pro/logo.svg',

    # AI Audio
    'Murf AI': 'https://murf.ai/static/murf-logo.svg',
    'Descript Overdub': 'https://www.descript.com/assets/favicon-48x48.png',
    'WellSaid Labs': 'https://wellsaidlabs.com/wp-content/uploads/2021/09/wellsaid-labs-icon.png',
    'LOVO': 'https://lovo.ai/static/lovo-icon.svg',
    'Krisp': 'https://cdn.krisp.ai/logos/krisp-logo-primary.svg',

    # AI Productivity
    'Reclaim AI': 'https://reclaim.ai/favicon-32x32.png',
    'Mem': 'https://get.mem.ai/assets/mem-app-icon.png',
    'Tactiq': 'https://tactiq.io/logo192.png',
    'Clockwise': 'https://www.getclockwise.com/apple-touch-icon.png',
    'Sunsama': 'https://www.sunsama.com/images/logo-symbol.svg',
    'Superhuman': 'https://superhuman.com/apple-touch-icon.png',

    # AI SEO
    'Surfer SEO': 'https://surferseo.com/wp-content/themes/surfer/img/favicon/apple-touch-icon.png',
    'LongShot AI': 'https://www.longshot.ai/images/logo.svg',
    'SEO.ai': 'https://seo.ai/logo.svg',

    # AI Business
    'Salesforce Einstein': 'https://www.salesforce.com/content/dam/sfdc-docs/www/logos/logo-salesforce.svg',
    'UiPath': 'https://www.uipath.com/hubfs/UiPath-Logo.svg',
    'Workday AI': 'https://www.workday.com/content/dam/web/images/icons/wd-touch-icon-228x228.png',

    # AI Networking
    'Juniper Mist AI': 'https://www.juniper.net/etc/designs/juniper/favicon-32x32.png',
    'Aruba AI': 'https://www.arubanetworks.com/assets/img/aruba-logo.svg',
    'Datadog': 'https://imgix.datadoghq.com/img/dd_logo_70x75.png',
    'Auvik': 'https://www.auvik.com/wp-content/themes/auvik2018/assets/img/logo.svg',

    # AI Cybersecurity
    'CrowdStrike Falcon': 'https://www.crowdstrike.com/wp-content/uploads/2021/06/cropped-cropped-CrowdStrike-Logomark-1-32x32.png',
    'Darktrace': 'https://www.darktrace.com/hubfs/raw_assets/public/Darktrace_August2021/images/darktrace-logo.svg',
    'Palo Alto Cortex': 'https://www.paloaltonetworks.com/content/dam/pan/en_US/images/logos/brand/primary-company-logo/Parent-logo.png',
    'Vectra AI': 'https://www.vectra.ai/hubfs/Vectra_Logo_2023.svg',
    'Cylance': 'https://www.cylance.com/content/dam/cylance-www/global/en/images/logos/cylance-logo.svg',

    # AI Medical
    'Zebra Medical Vision': 'https://www.zebra-med.com/wp-content/uploads/2020/03/logo.svg',
    'Viz.ai': 'https://www.viz.ai/hubfs/Viz-ai-logo.svg',
    'Tempus': 'https://www.tempus.com/wp-content/uploads/2021/09/tempus-logo.svg',
    'Babylon Health': 'https://www.babylonhealth.com/static/images/babylon-logo.svg',

    # AI Architecture
    'TestFit': 'https://testfit.io/wp-content/uploads/2021/06/testfit-logo.svg',
    'Finch3D': 'https://www.finch3d.com/assets/finch-logo.svg',
    'Archistar': 'https://archistar.ai/wp-content/uploads/2021/09/archistar-logo.svg',
    'Augmenta': 'https://www.augmenta.ai/assets/augmenta-logo.svg',
    'Doxel': 'https://www.doxel.ai/images/doxel-logo.svg',
}

def download_logo(name, url, save_dir):
    """Télécharge un logo."""
    try:
        # Créer un nom de fichier sûr
        import re
        safe_name = re.sub(r'[^\w\s-]', '', name.lower())
        safe_name = re.sub(r'[-\s]+', '-', safe_name)

        # Déterminer l'extension
        if '.svg' in url.lower():
            ext = '.svg'
        elif '.png' in url.lower():
            ext = '.png'
        elif '.jpg' in url.lower() or '.jpeg' in url.lower():
            ext = '.jpg'
        else:
            ext = '.png'  # Default

        filename = f"{safe_name}{ext}"
        filepath = save_dir / filename

        # Télécharger
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=15, allow_redirects=True)
        response.raise_for_status()

        # Vérifier que c'est bien une image
        content_type = response.headers.get('content-type', '')
        if 'image' not in content_type and 'svg' not in content_type:
            print(f"      ⚠️  Pas une image: {content_type}")
            return None, False

        with open(filepath, 'wb') as f:
            f.write(response.content)

        return filename, True

    except Exception as e:
        print(f"      ⚠️  Échec: {e}")
        return None, False

def main():
    """Programme principal."""
    logos_dir = Path('/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/assets/images/logos')
    logos_dir.mkdir(parents=True, exist_ok=True)

    print("📥 TÉLÉCHARGEMENT DES LOGOS MANQUANTS\n")

    downloaded = 0
    failed = 0

    for name, url in ALTERNATIVE_LOGO_URLS.items():
        print(f"  {name}...", end=' ')
        filename, success = download_logo(name, url, logos_dir)
        if success:
            print(f"✅ {filename}")
            downloaded += 1
        else:
            print(f"❌")
            failed += 1
        time.sleep(0.5)

    print(f"\n{'='*60}")
    print(f"🎉 Terminé!")
    print(f"📊 Logos téléchargés: {downloaded}")
    print(f"⚠️  Échecs: {failed}")

if __name__ == '__main__':
    main()
