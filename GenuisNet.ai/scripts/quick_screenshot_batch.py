#!/usr/bin/env python3
"""
Version rapide et simple pour capturer des screenshots
Avec meilleure gestion des erreurs et timeout réduit
"""

import asyncio
import sys
from pathlib import Path
from playwright.async_api import async_playwright

BASE_DIR = Path(__file__).parent.parent
SCREENSHOTS_DIR = BASE_DIR / "assets" / "screenshots"

# Top 20 outils populaires pour commencer
PRIORITY_TOOLS = {
    # Chatbots (6)
    'chatbots/gemini': 'https://gemini.google.com/',
    'chatbots/perplexity': 'https://www.perplexity.ai/',
    'chatbots/poe': 'https://poe.com/',
    'chatbots/copilot': 'https://copilot.microsoft.com/',
    'chatbots/huggingchat': 'https://huggingface.co/chat/',

    # Image (4)
    'image/midjourney': 'https://www.midjourney.com/',
    'image/leonardo-ai': 'https://leonardo.ai/',
    'image/ideogram': 'https://ideogram.ai/',
    'image/adobe-firefly': 'https://www.adobe.com/products/firefly.html',

    # Coding (3)
    'coding/github-copilot': 'https://github.com/features/copilot',
    'coding/codeium': 'https://codeium.com/',
    'coding/tabnine': 'https://www.tabnine.com/',

    # Video (3)
    'video/runway': 'https://runwayml.com/',
    'video/synthesia': 'https://www.synthesia.io/',
    'video/pictory': 'https://pictory.ai/',

    # Audio (2)
    'audio/elevenlabs': 'https://elevenlabs.io/',
    'audio/murf-ai': 'https://murf.ai/',

    # Productivity (2)
    'productivity/notion-ai': 'https://www.notion.so/product/ai',
    'productivity/clickup-ai': 'https://clickup.com/ai',
}

async def capture_one(category: str, tool_name: str, url: str):
    """Capture un screenshot avec timeout court"""
    category_dir = SCREENSHOTS_DIR / category
    category_dir.mkdir(parents=True, exist_ok=True)
    output_file = category_dir / f"{tool_name}.png"

    if output_file.exists():
        print(f"  ⊳ Exists: {tool_name}")
        return True

    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(
                headless=True,
                args=['--disable-blink-features=AutomationControlled']
            )

            context = await browser.new_context(
                viewport={'width': 1920, 'height': 1080},
                user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
            )

            page = await context.new_page()

            print(f"  → Loading {url}...", end='', flush=True)

            # Navigation avec timeout court
            try:
                await page.goto(url, wait_until='domcontentloaded', timeout=20000)
            except:
                await page.goto(url, timeout=20000)

            # Attente minimale
            await asyncio.sleep(2)

            # Screenshot
            await page.screenshot(path=str(output_file), full_page=False)

            await browser.close()

            # Vérifier la taille
            size = output_file.stat().st_size / 1024  # KB
            print(f" ✓ ({size:.0f}KB)")
            return True

    except asyncio.TimeoutError:
        print(f" ✗ Timeout")
        return False
    except Exception as e:
        print(f" ✗ Error: {str(e)[:50]}")
        return False

async def main():
    print("=" * 70)
    print("Quick Screenshot Batch - Top 20 AI Tools")
    print("=" * 70)

    stats = {'total': len(PRIORITY_TOOLS), 'success': 0, 'failed': 0, 'skipped': 0}

    for i, (key, url) in enumerate(PRIORITY_TOOLS.items(), 1):
        category, tool_name = key.split('/')

        print(f"\n[{i}/{stats['total']}] {tool_name} ({category})")

        # Vérifie si existe
        output_file = SCREENSHOTS_DIR / category / f"{tool_name}.png"
        if output_file.exists():
            stats['skipped'] += 1
            print(f"  ⊳ Already exists")
            continue

        # Capture
        success = await capture_one(category, tool_name, url)

        if success:
            stats['success'] += 1
        else:
            stats['failed'] += 1

        # Pause entre requêtes
        await asyncio.sleep(1)

    # Rapport
    print("\n" + "=" * 70)
    print("📊 Results")
    print("=" * 70)
    print(f"Total: {stats['total']}")
    print(f"✓ Success: {stats['success']}")
    print(f"✗ Failed: {stats['failed']}")
    print(f"⊳ Skipped: {stats['skipped']}")
    print("=" * 70)

    # Liste les fichiers créés
    print(f"\n📁 Screenshots in: {SCREENSHOTS_DIR}")
    for cat_dir in sorted(SCREENSHOTS_DIR.iterdir()):
        if cat_dir.is_dir():
            pngs = list(cat_dir.glob("*.png"))
            if pngs:
                print(f"  {cat_dir.name}: {len(pngs)} files")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n⚠ Interrupted by user")
        sys.exit(1)
