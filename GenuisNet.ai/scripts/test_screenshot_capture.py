#!/usr/bin/env python3
"""
Script de test pour capturer quelques screenshots
"""

import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

BASE_DIR = Path(__file__).parent.parent
SCREENSHOTS_DIR = BASE_DIR / "assets" / "screenshots"

# Quelques outils pour tester
TEST_TOOLS = {
    'chatbots/chatgpt': 'https://openai.com/chatgpt',
    'image/stable-diffusion': 'https://stability.ai/stable-image',
    'coding/cursor': 'https://cursor.com/',
}

async def capture_screenshot(category: str, tool_name: str, url: str):
    """Capture un screenshot"""
    category_dir = SCREENSHOTS_DIR / category
    category_dir.mkdir(parents=True, exist_ok=True)
    output_file = category_dir / f"{tool_name}.png"

    if output_file.exists():
        print(f"⊳ Already exists: {output_file.name}")
        return True

    try:
        async with async_playwright() as p:
            print(f"\n🌐 Launching browser...")
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(
                viewport={'width': 1920, 'height': 1080}
            )
            page = await context.new_page()

            print(f"📍 Navigating to: {url}")
            await page.goto(url, wait_until='networkidle', timeout=30000)

            print(f"⏳ Waiting for page to stabilize...")
            await asyncio.sleep(3)

            print(f"📸 Taking screenshot...")
            await page.screenshot(path=str(output_file), full_page=False)

            await browser.close()

            print(f"✓ Saved to: {output_file}")
            return True

    except Exception as e:
        print(f"✗ Error: {e}")
        return False

async def main():
    print("=" * 60)
    print("Screenshot Capture Test")
    print("=" * 60)

    for key, url in TEST_TOOLS.items():
        category, tool_name = key.split('/')
        print(f"\n▶ Testing: {tool_name} ({category})")
        await capture_screenshot(category, tool_name, url)
        await asyncio.sleep(1)

    print("\n" + "=" * 60)
    print(f"✓ Test complete! Check {SCREENSHOTS_DIR}")
    print("=" * 60)

if __name__ == "__main__":
    asyncio.run(main())
