#!/usr/bin/env python3
"""
Script d'automatisation pour capturer des screenshots d'outils IA
Utilise Playwright pour visiter les sites et capturer l'interface
"""

import asyncio
import json
from pathlib import Path
from typing import Dict, List
import re

# Configuration
BASE_DIR = Path(__file__).parent.parent
REVIEWS_DIR = BASE_DIR / "pages" / "reviews"
SCREENSHOTS_DIR = BASE_DIR / "assets" / "screenshots"
SCREENSHOTS_DIR.mkdir(exist_ok=True)

# URLs officielles des outils IA (à compléter)
TOOL_URLS = {
    # Chatbots
    'chatbots/chatgpt': 'https://chat.openai.com/',
    'chatbots/claude': 'https://claude.ai/',
    'chatbots/gemini': 'https://gemini.google.com/',
    'chatbots/perplexity': 'https://www.perplexity.ai/',
    'chatbots/poe': 'https://poe.com/',
    'chatbots/character-ai': 'https://character.ai/',
    'chatbots/huggingchat': 'https://huggingface.co/chat/',
    'chatbots/copilot': 'https://copilot.microsoft.com/',

    # Image Generation
    'image/midjourney': 'https://www.midjourney.com/',
    'image/stable-diffusion': 'https://stability.ai/',
    'image/dall-e': 'https://openai.com/dall-e-3',
    'image/leonardo-ai': 'https://leonardo.ai/',
    'image/ideogram': 'https://ideogram.ai/',
    'image/adobe-firefly': 'https://www.adobe.com/products/firefly.html',
    'image/canva-ai': 'https://www.canva.com/ai-image-generator/',

    # Coding
    'coding/github-copilot': 'https://github.com/features/copilot',
    'coding/cursor': 'https://cursor.com/',
    'coding/codeium': 'https://codeium.com/',
    'coding/tabnine': 'https://www.tabnine.com/',
    'coding/codewhisperer': 'https://aws.amazon.com/codewhisperer/',

    # Video
    'video/runway': 'https://runwayml.com/',
    'video/synthesia': 'https://www.synthesia.io/',
    'video/pictory': 'https://pictory.ai/',
    'video/descript': 'https://www.descript.com/',
    'video/invideo': 'https://invideo.io/',
    'video/elai': 'https://elai.io/',

    # Audio
    'audio/elevenlabs': 'https://elevenlabs.io/',
    'audio/murf-ai': 'https://murf.ai/',
    'audio/play-ht': 'https://play.ht/',
    'audio/speechify': 'https://speechify.com/',
    'audio/descript': 'https://www.descript.com/',

    # Productivity
    'productivity/notion-ai': 'https://www.notion.so/product/ai',
    'productivity/clickup-ai': 'https://clickup.com/ai',
    'productivity/motion': 'https://www.usemotion.com/',
    'productivity/firefliesai': 'https://fireflies.ai/',
    'productivity/otterai': 'https://otter.ai/',

    # Writing
    'writing/jasper-ai': 'https://www.jasper.ai/',
    'writing/copy-ai': 'https://www.copy.ai/',
    'writing/grammarly': 'https://www.grammarly.com/',
    'writing/writesonic': 'https://writesonic.com/',
    'writing/quillbot': 'https://quillbot.com/',
    'writing/wordtune': 'https://www.wordtune.com/',
    'writing/rytr': 'https://rytr.me/',

    # Research
    'research/consensus': 'https://consensus.app/',
    'research/elicit': 'https://elicit.com/',
    'research/scispace': 'https://scispace.com/',
    'research/researchrabbit': 'https://www.researchrabbit.ai/',
    'research/scite': 'https://scite.ai/',
    'research/scholarcy': 'https://www.scholarcy.com/',

    # Business/Analytics
    'business/tableau': 'https://www.tableau.com/',
    'business/salesforce-einstein': 'https://www.salesforce.com/products/einstein/overview/',
    'analytics/amplitude': 'https://amplitude.com/',
    'analytics/mixpanel': 'https://mixpanel.com/',

    # Customer Service
    'customer-service/intercom-fin': 'https://www.intercom.com/fin',
    'customer-service/zendesk-ai': 'https://www.zendesk.com/service/ticketing-system/ai/',
    'customer-service/drift': 'https://www.drift.com/',
    'customer-service/ada': 'https://www.ada.cx/',

    # Sales
    'sales/gong': 'https://www.gong.io/',
    'sales/outreach': 'https://www.outreach.io/',
    'sales/clari': 'https://www.clari.com/',
    'sales/6sense': 'https://6sense.com/',

    # Education
    'education/duolingo-max': 'https://www.duolingo.com/',
    'education/khan-academy-ai': 'https://www.khanacademy.org/',
    'education/coursera-coach': 'https://www.coursera.org/',
    'education/quizlet-ai': 'https://quizlet.com/',

    # Legal
    'legal/harvey-ai': 'https://www.harvey.ai/',
    'legal/casetext': 'https://casetext.com/',
    'legal/luminance': 'https://www.luminance.com/',

    # Cybersecurity
    'cybersecurity/crowdstrike': 'https://www.crowdstrike.com/',
    'cybersecurity/darktrace': 'https://darktrace.com/',
    'cybersecurity/cortex-xdr': 'https://www.paloaltonetworks.com/cortex/cortex-xdr',
}

def check_playwright_installed():
    """Vérifie si Playwright est installé"""
    try:
        from playwright.async_api import async_playwright
        return True
    except ImportError:
        return False

async def capture_screenshot(category: str, tool_name: str, url: str, timeout: int = 30000):
    """Capture un screenshot d'un site web"""
    from playwright.async_api import async_playwright

    category_dir = SCREENSHOTS_DIR / category
    category_dir.mkdir(parents=True, exist_ok=True)

    output_file = category_dir / f"{tool_name}.png"

    # Skip si existe déjà
    if output_file.exists():
        print(f"⊳ Already exists: {category}/{tool_name}")
        return True

    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(
                viewport={'width': 1920, 'height': 1080},
                user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
            )

            page = await context.new_page()

            print(f"⬇ Capturing: {category}/{tool_name} from {url}")

            # Navigue vers la page
            await page.goto(url, wait_until='networkidle', timeout=timeout)

            # Attend un peu pour que tout se charge
            await asyncio.sleep(2)

            # Prend le screenshot
            await page.screenshot(path=str(output_file), full_page=False)

            await browser.close()

            print(f"✓ Captured: {output_file}")
            return True

    except Exception as e:
        print(f"✗ Failed to capture {category}/{tool_name}: {e}")
        return False

async def main():
    """Fonction principale"""
    print("=" * 70)
    print("AI Tools Screenshot Automation (Playwright)")
    print("=" * 70)

    # Vérifie si Playwright est installé
    if not check_playwright_installed():
        print("\n❌ Playwright n'est pas installé!")
        print("\nPour installer Playwright:")
        print("  pip install playwright")
        print("  playwright install")
        return

    print(f"\n📸 Capturing screenshots for {len(TOOL_URLS)} tools...")
    print(f"📁 Output directory: {SCREENSHOTS_DIR}\n")

    stats = {'total': len(TOOL_URLS), 'success': 0, 'failed': 0, 'skipped': 0}

    # Capture les screenshots
    for i, (key, url) in enumerate(TOOL_URLS.items(), 1):
        category, tool_name = key.split('/')

        print(f"\n[{i}/{stats['total']}] {tool_name} ({category})")

        # Vérifie si existe
        output_file = SCREENSHOTS_DIR / category / f"{tool_name}.png"
        if output_file.exists():
            stats['skipped'] += 1
            print(f"⊳ Already exists: {tool_name}")
            continue

        # Capture
        success = await capture_screenshot(category, tool_name, url)

        if success:
            stats['success'] += 1
        else:
            stats['failed'] += 1

        # Pause entre les requêtes
        await asyncio.sleep(1)

    # Rapport final
    print("\n" + "=" * 70)
    print("📊 Capture Report")
    print("=" * 70)
    print(f"Total tools: {stats['total']}")
    print(f"✓ Captured: {stats['success']}")
    print(f"✗ Failed: {stats['failed']}")
    print(f"⊳ Skipped (exists): {stats['skipped']}")
    print("=" * 70)

    # Sauvegarde le rapport
    report_file = SCREENSHOTS_DIR / "capture_report.json"
    with open(report_file, 'w') as f:
        json.dump({
            'stats': stats,
            'tools': list(TOOL_URLS.keys())
        }, f, indent=2)

    print(f"\n📄 Report saved to: {report_file}")

if __name__ == "__main__":
    asyncio.run(main())
