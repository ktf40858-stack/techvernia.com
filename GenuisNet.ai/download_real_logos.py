#!/usr/bin/env python3
"""
Download real official logos for all AI tools
This script provides URLs where the official logos can be found
"""

import os
import subprocess
from pathlib import Path

BASE_DIR = Path("/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/assets/images/tools")

# Official logo URLs for all tools
LOGO_URLS = {
    'chatbots': {
        'chatgpt': 'https://upload.wikimedia.org/wikipedia/commons/0/04/ChatGPT_logo.svg',
        'claude': 'https://www.anthropic.com/images/icons/claude-logo.svg',
        'gemini': 'https://www.gstatic.com/lamda/images/gemini_sparkle_v002_d4735304ff6292a690345.svg',
        'copilot': 'https://upload.wikimedia.org/wikipedia/commons/2/2a/Microsoft_365_Copilot_Icon.svg',
        'perplexity': 'https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/perplexity-ai-icon.png',
        'grok': 'https://pbs.twimg.com/profile_images/1683325380441128960/yRsRRjGO_400x400.jpg',
        'deepseek': 'https://chat.deepseek.com/static/images/logo.png',
        'poe': 'https://psc2.cf2.poecdn.net/favicon.svg',
    },
    'coding': {
        'github-copilot': 'https://github.githubassets.com/assets/github-copilot-logo.png',
        'cursor': 'https://www.cursor.com/brand/icon.svg',
        'codeium': 'https://codeium.com/logo.svg',
        'tabnine': 'https://www.tabnine.com/wp-content/uploads/2021/06/tabnine-logo.svg',
        'replit': 'https://replit.com/public/images/logo-small.png',
        'codewhisperer': 'https://d1.awsstatic.com/product-marketing/CodeWhisperer/Product-Icon_Amazon-CodeWhisperer_icon_squid_ink.svg',
        'windsurf': 'https://windsurf.com/icon.svg',
        'deepseek-coder': 'https://chat.deepseek.com/static/images/logo.png',
    },
    'image': {
        'midjourney': 'https://cdn.worldvectorlogo.com/logos/midjourney.svg',
        'dall-e-3': 'https://openai.com/content/images/2022/05/openai-avatar.png',
        'stable-diffusion': 'https://stability.ai/brand/logo.svg',
        'leonardo-ai': 'https://leonardo.ai/logo.svg',
        'adobe-firefly': 'https://www.adobe.com/content/dam/cc/icons/firefly-app.svg',
        'canva-ai': 'https://static.canva.com/web/images/12487a1e0770d29351bd4ce4f87ec8fe.svg',
        'ideogram': 'https://ideogram.ai/assets/image/logo.svg',
        'clipdrop': 'https://clipdrop.co/logo.svg',
    },
    'audio': {
        'elevenlabs': 'https://elevenlabs.io/favicon.svg',
        'murf-ai': 'https://murf.ai/logo.svg',
        'descript': 'https://www.descript.com/hubfs/Brand/Logo/Descript-Logo-2022.svg',
        'speechify': 'https://speechify.com/logo.svg',
        'playht': 'https://play.ht/logo.svg',
        'resemble-ai': 'https://www.resemble.ai/logo.svg',
        'suno-ai': 'https://www.suno.ai/logo.svg',
        'udio': 'https://www.udio.com/logo.svg',
    },
    'video': {
        'runway': 'https://runwayml.com/logo.svg',
        'heygen': 'https://www.heygen.com/logo.svg',
        'synthesia': 'https://www.synthesia.io/logo.svg',
        'pictory': 'https://pictory.ai/logo.svg',
        'invideo': 'https://invideo.io/logo.svg',
        'lumen5': 'https://lumen5.com/logo.svg',
        'kapwing': 'https://www.kapwing.com/logo.svg',
        'kling-ai': 'https://klingai.com/logo.svg',
    },
    'writing': {
        'grammarly': 'https://static.grammarly.com/assets/files/efe57d016d9efff36da7884c193b646b/logo.svg',
        'jasper-ai': 'https://www.jasper.ai/logo.svg',
        'copyai': 'https://www.copy.ai/logo.svg',
        'writesonic': 'https://writesonic.com/logo.svg',
        'rytr': 'https://rytr.me/logo.svg',
        'quillbot': 'https://quillbot.com/logo.svg',
        'wordtune': 'https://www.wordtune.com/logo.svg',
    },
    'productivity': {
        'notion-ai': 'https://www.notion.so/front-static/logo-ios.png',
        'clickup-ai': 'https://clickup.com/logo.svg',
        'motion': 'https://www.usemotion.com/logo.svg',
        'zapier': 'https://cdn.zapier.com/zapier/images/logos/zapier-logo.svg',
        'otterai': 'https://otter.ai/logo.svg',
        'firefliesai': 'https://fireflies.ai/logo.svg',
        'reclaim-ai': 'https://reclaim.ai/logo.svg',
        'mem-ai': 'https://get.mem.ai/logo.svg',
    },
    'seo': {
        'semrush': 'https://www.semrush.com/logo.svg',
        'ahrefs': 'https://ahrefs.com/logo.svg',
        'surfer-seo': 'https://surferseo.com/logo.svg',
        'frase': 'https://www.frase.io/logo.svg',
        'clearscope': 'https://www.clearscope.io/logo.svg',
        'marketmuse': 'https://www.marketmuse.com/logo.svg',
        'neuronwriter': 'https://neuronwriter.com/logo.svg',
        'scalenut': 'https://www.scalenut.com/logo.svg',
    },
    'business': {
        'hubspot-ai': 'https://www.hubspot.com/hubfs/HubSpot_Logos/HubSpot-Inversed-Favicon.png',
        'salesforce-einstein': 'https://www.salesforce.com/content/dam/web/en_us/www/images/einstein/einstein-logo.svg',
        'gong': 'https://www.gong.io/wp-content/uploads/2021/03/gong-logo.svg',
        'drift': 'https://www.drift.com/wp-content/uploads/2021/01/drift-logo.svg',
        'tableau': 'https://www.tableau.com/sites/default/files/pages/tableaulogo_highres.png',
        'looker': 'https://looker.com/assets/img/images/logos/looker_logo.svg',
        'conversica': 'https://www.conversica.com/logo.svg',
        'chorusai': 'https://www.chorus.ai/logo.svg',
    },
    'architecture': {
        'arko-ai': 'https://www.arko.ai/logo.svg',
        'finch3d': 'https://www.finch3d.com/logo.svg',
        'maket-ai': 'https://www.maket.ai/logo.svg',
        'veras-ai': 'https://www.verasai.com/logo.svg',
        'spacemaker-ai': 'https://www.spacemakerai.com/logo.svg',
        'hypar': 'https://hypar.io/logo.svg',
        'testfit': 'https://testfit.io/logo.svg',
        'architechtures': 'https://www.architechtures.com/logo.svg',
    },
    'medical': {
        'butterfly-iq': 'https://www.butterflynetwork.com/logo.svg',
        'paige-ai': 'https://paige.ai/logo.svg',
        'zebra-medical': 'https://www.zebra-med.com/logo.svg',
        'aidoc': 'https://www.aidoc.com/logo.svg',
        'tempus': 'https://www.tempus.com/logo.svg',
        'nuance-dragon': 'https://www.nuance.com/content/dam/nuance/en_us/images/logo.svg',
        'pathai': 'https://www.pathai.com/logo.svg',
        'viz-ai': 'https://www.viz.ai/logo.svg',
    },
}

def download_logo(url, output_path):
    """Download a logo from URL using wget or curl"""
    try:
        # Try with wget first
        result = subprocess.run(
            ['wget', '-q', '-O', output_path, url],
            capture_output=True,
            timeout=10
        )
        if result.returncode == 0 and os.path.getsize(output_path) > 0:
            return True

        # If wget fails, try curl
        result = subprocess.run(
            ['curl', '-s', '-o', output_path, '-L', url],
            capture_output=True,
            timeout=10
        )
        return result.returncode == 0 and os.path.getsize(output_path) > 0

    except Exception as e:
        print(f"  Error downloading {url}: {e}")
        return False

def download_all_logos():
    """Download all official logos"""
    total = 0
    success = 0
    failed = []

    for category, tools in LOGO_URLS.items():
        category_dir = BASE_DIR / category
        category_dir.mkdir(parents=True, exist_ok=True)

        print(f"\n{category.upper()}:")
        for tool_id, url in tools.items():
            total += 1

            # Determine file extension from URL
            ext = 'svg' if url.endswith('.svg') else 'png'
            output_file = category_dir / f"{tool_id}.{ext}"

            print(f"  Downloading {tool_id}... ", end='', flush=True)

            if download_logo(url, output_file):
                print(f"✓ ({ext})")
                success += 1
            else:
                print(f"✗ FAILED")
                failed.append(f"{category}/{tool_id}")

    print(f"\n{'='*70}")
    print(f"Download Summary:")
    print(f"  Total: {total}")
    print(f"  Success: {success}")
    print(f"  Failed: {len(failed)}")

    if failed:
        print(f"\nFailed downloads:")
        for item in failed:
            print(f"  - {item}")

    return success, failed

if __name__ == "__main__":
    print("="*70)
    print("DOWNLOADING OFFICIAL LOGOS FOR ALL AI TOOLS")
    print("="*70)

    success, failed = download_all_logos()

    print(f"\n{'='*70}")
    print(f"✅ Successfully downloaded {success} official logos!")
    print("="*70)
