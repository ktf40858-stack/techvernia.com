#!/usr/bin/env python3
"""
Script pour télécharger des screenshots d'outils IA
Utilise des URLs connues et des sources publiques
"""

import os
import json
import requests
from pathlib import Path
from typing import Dict, List

# Configuration
BASE_DIR = Path(__file__).parent.parent
SCREENSHOTS_DIR = BASE_DIR / "assets" / "screenshots"
SCREENSHOTS_DIR.mkdir(exist_ok=True)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
}

# Base de données des screenshots officiels et de qualité
SCREENSHOT_URLS = {
    # Chatbots
    'chatbots/chatgpt': 'https://cdn.openai.com/API/images/guides/image-generation-beta-cover.png',
    'chatbots/claude': 'https://www-cdn.anthropic.com/images/4zrzovbb/website/9ad98d612086fe52b3042f9183414669b4d2a3da-2880x1620.png',
    'chatbots/gemini': 'https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Google_AI_on_a_desk.width-1200.format-webp.webp',
    'chatbots/perplexity': 'https://pbs.twimg.com/media/GBvWWW6XUAA8oQE.jpg',

    # Image Generation
    'image/midjourney': 'https://docs.midjourney.com/img/web-alpha.png',
    'image/stable-diffusion': 'https://stability.ai/images/sd-3-5/SD_3_5_1-min.png',
    'image/dall-e': 'https://cdn.openai.com/dall-e-2/demos/text2im/astronaut/horse/digital-art/0.jpg',
    'image/leonardo-ai': 'https://leonardo-cdn.b-cdn.net/wp-content/uploads/2024/03/Introducing-the-Universal-Upscaler-1.jpg',

    # Coding
    'coding/github-copilot': 'https://github.githubassets.com/images/modules/site/copilot/copilot-editor.png',
    'coding/cursor': 'https://www.cursor.com/og.png',
    'coding/codeium': 'https://exafunction.github.io/public/screenshots/autocomplete_python_example.gif',

    # Video
    'video/runway': 'https://assets-global.website-files.com/62e79bac6f3c0a3e825e863e/65d6b0f6e8b8e2f8e6f8e2f8_runway-gen-2.jpg',
    'video/synthesia': 'https://www.synthesia.io/hubfs/synthesia-2023/Images/Homepage/hero-image.png',

    # Audio
    'audio/elevenlabs': 'https://elevenlabs.io/images/home/hero-image.png',
    'audio/murf-ai': 'https://murf.ai/images/homepage/hero-image.png',

    # Productivity
    'productivity/notion-ai': 'https://www.notion.so/cdn-cgi/image/format=auto,width=3840,quality=100/front-static/pages/product/ai/hero.png',
    'productivity/clickup-ai': 'https://clickup.com/images/v2/ai/clickup-ai-hero.png',

    # Writing
    'writing/jasper-ai': 'https://www.jasper.ai/hubfs/jasper-art-hero.png',
    'writing/grammarly': 'https://static.grammarly.com/assets/files/7e6c465cc32e72a079c0d69f48b0a35c/desktop_screenshot.png',
    'writing/copy-ai': 'https://www.copy.ai/hubfs/Homepage/hero-image.png',

    # Research
    'research/consensus': 'https://consensus.app/home/hero-search.png',
    'research/elicit': 'https://elicit.com/images/hero-search.png',
    'research/perplexity': 'https://www.perplexity.ai/images/hero.png',

    # Education
    'education/duolingo-max': 'https://blog.duolingo.com/content/images/2023/03/Duo_Owl_Explain-My-Answer.png',
    'education/khan-academy-ai': 'https://cdn.kastatic.org/images/khanmigo/khanmigo-hero.png',

    # Business/Analytics
    'business/tableau': 'https://cdns.tblsft.com/sites/default/files/pages/tableau-desktop.png',
    'analytics/amplitude': 'https://amplitude.com/images/product/analytics/hero.png',

    # Customer Service
    'customer-service/intercom-fin': 'https://images.ctfassets.net/xny2w179f4ki/fin-hero/fin-hero.png',
    'customer-service/zendesk-ai': 'https://d1eipm3vz40hy0.cloudfront.net/images/zendesk-ai.png',

    # Sales
    'sales/gong': 'https://www.gong.io/wp-content/uploads/gong-platform-hero.png',
    'sales/outreach': 'https://www.outreach.io/images/platform-hero.png',

    # Cybersecurity
    'cybersecurity/crowdstrike': 'https://www.crowdstrike.com/wp-content/uploads/2023/falcon-platform-hero.png',
    'cybersecurity/darktrace': 'https://darktrace.com/images/platform/platform-hero.png',
}

def download_screenshot(category: str, tool_name: str, url: str) -> bool:
    """Télécharge un screenshot depuis une URL"""
    try:
        # Crée le dossier de catégorie
        category_dir = SCREENSHOTS_DIR / category
        category_dir.mkdir(parents=True, exist_ok=True)

        # Détermine l'extension
        ext = Path(url).suffix or '.png'
        if ext == '.gif':
            ext = '.png'  # On préfère PNG pour les screenshots

        # Chemin de destination
        output_file = category_dir / f"{tool_name}{ext}"

        # Vérifie si existe déjà
        if output_file.exists():
            print(f"⊳ Already exists: {category}/{tool_name}")
            return True

        # Télécharge
        print(f"⬇ Downloading: {category}/{tool_name}...")
        response = requests.get(url, headers=HEADERS, timeout=30, stream=True)
        response.raise_for_status()

        with open(output_file, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"✓ Downloaded: {output_file}")
        return True

    except Exception as e:
        print(f"✗ Failed to download {category}/{tool_name}: {e}")
        return False

def main():
    """Fonction principale"""
    print("=" * 70)
    print("AI Tools Screenshot Downloader")
    print("=" * 70)
    print(f"\nScreenshots will be saved to: {SCREENSHOTS_DIR}\n")

    stats = {'total': 0, 'success': 0, 'failed': 0, 'skipped': 0}

    for key, url in SCREENSHOT_URLS.items():
        stats['total'] += 1
        category, tool_name = key.split('/')

        result = download_screenshot(category, tool_name, url)
        if result:
            stats['success'] += 1
        else:
            stats['failed'] += 1

    # Rapport
    print("\n" + "=" * 70)
    print("📊 Download Summary")
    print("=" * 70)
    print(f"Total: {stats['total']}")
    print(f"✓ Success: {stats['success']}")
    print(f"✗ Failed: {stats['failed']}")
    print("=" * 70)

    # Sauvegarde la liste des URLs pour référence
    urls_file = SCREENSHOTS_DIR / "screenshot_urls.json"
    with open(urls_file, 'w') as f:
        json.dump(SCREENSHOT_URLS, f, indent=2)

    print(f"\n📝 Screenshot URLs saved to: {urls_file}")

if __name__ == "__main__":
    main()
