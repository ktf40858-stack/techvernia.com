#!/usr/bin/env python3
"""
Script étendu pour capturer plus de screenshots
Couvre Writing, Research, Business, Customer Service, Sales, etc.
"""

import asyncio
import sys
from pathlib import Path
from playwright.async_api import async_playwright

BASE_DIR = Path(__file__).parent.parent
SCREENSHOTS_DIR = BASE_DIR / "assets" / "screenshots"

# 50+ outils supplémentaires à capturer
EXTENDED_TOOLS = {
    # Writing (7 outils)
    'writing/jasper-ai': 'https://www.jasper.ai/',
    'writing/copy-ai': 'https://www.copy.ai/',
    'writing/grammarly': 'https://www.grammarly.com/',
    'writing/writesonic': 'https://writesonic.com/',
    'writing/quillbot': 'https://quillbot.com/',
    'writing/wordtune': 'https://www.wordtune.com/',
    'writing/rytr': 'https://rytr.me/',

    # Research (12 outils)
    'research/consensus': 'https://consensus.app/',
    'research/elicit': 'https://elicit.com/',
    'research/scispace': 'https://scispace.com/',
    'research/researchrabbit': 'https://www.researchrabbit.ai/',
    'research/scite': 'https://scite.ai/',
    'research/scholarcy': 'https://www.scholarcy.com/',
    'research/litmaps': 'https://www.litmaps.com/',
    'research/semantic-scholar': 'https://www.semanticscholar.org/',
    'research/connected-papers': 'https://www.connectedpapers.com/',
    'research/inciteful': 'https://inciteful.xyz/',
    'research/iris-ai': 'https://iris.ai/',
    'research/paper-digest': 'https://www.paperdigest.org/',

    # Customer Service (15 outils - top 10)
    'customer-service/intercom-fin': 'https://www.intercom.com/fin',
    'customer-service/zendesk-ai': 'https://www.zendesk.com/',
    'customer-service/drift': 'https://www.drift.com/',
    'customer-service/ada': 'https://www.ada.cx/',
    'customer-service/liveperson': 'https://www.liveperson.com/',
    'customer-service/freshdesk-ai': 'https://www.freshworks.com/freshdesk/',
    'customer-service/kustomer': 'https://www.kustomer.com/',
    'customer-service/forethought': 'https://forethought.ai/',
    'customer-service/ultimate-ai': 'https://www.ultimate.ai/',
    'customer-service/boost-ai': 'https://www.boost.ai/',

    # Sales (16 outils - top 10)
    'sales/gong': 'https://www.gong.io/',
    'sales/outreach': 'https://www.outreach.io/',
    'sales/clari': 'https://www.clari.com/',
    'sales/6sense': 'https://6sense.com/',
    'sales/salesforce-einstein-gpt': 'https://www.salesforce.com/products/einstein/overview/',
    'sales/people-ai': 'https://www.people.ai/',
    'sales/chorus-ai': 'https://www.chorus.ai/',
    'sales/conversica': 'https://www.conversica.com/',
    'sales/apollo-io': 'https://www.apollo.io/',
    'sales/lavender': 'https://www.lavender.ai/',

    # Business/Analytics (8 outils)
    'business/tableau': 'https://www.tableau.com/',
    'business/power-bi': 'https://powerbi.microsoft.com/',
    'business/looker': 'https://cloud.google.com/looker',
    'business/qlik': 'https://www.qlik.com/',
    'analytics/mixpanel': 'https://mixpanel.com/',
    'analytics/amplitude': 'https://amplitude.com/',
    'analytics/heap': 'https://heap.io/',
    'analytics/pendo': 'https://www.pendo.io/',

    # Education (14 outils - top 8)
    'education/duolingo-max': 'https://www.duolingo.com/',
    'education/khan-academy-ai': 'https://www.khanacademy.org/',
    'education/coursera-coach': 'https://www.coursera.org/',
    'education/quizlet-ai': 'https://quizlet.com/',
    'education/gradescope': 'https://www.gradescope.com/',
    'education/century-tech': 'https://www.century.tech/',
    'education/cognii': 'https://www.cognii.com/',
    'education/squirrel-ai': 'https://squirrelai.com/',

    # SEO (8 outils)
    'seo/semrush': 'https://www.semrush.com/',
    'seo/ahrefs': 'https://ahrefs.com/',
    'seo/surfer-seo': 'https://surferseo.com/',
    'seo/clearscope': 'https://www.clearscope.io/',
    'seo/frase': 'https://www.frase.io/',
    'seo/marketmuse': 'https://www.marketmuse.com/',
    'seo/jasper-seo': 'https://www.jasper.ai/',
    'seo/neuronwriter': 'https://neuronwriter.com/',

    # HR (14 outils - top 8)
    'hr/workday': 'https://www.workday.com/',
    'hr/beamery': 'https://beamery.com/',
    'hr/pymetrics': 'https://www.pymetrics.ai/',
    'hr/eightfold-ai': 'https://eightfold.ai/',
    'hr/paradox': 'https://www.paradox.ai/',
    'hr/seekout': 'https://seekout.com/',
    'hr/humanly': 'https://www.humanly.io/',
    'hr/phenom': 'https://www.phenom.com/',
}

async def capture_one(category: str, tool_name: str, url: str):
    """Capture un screenshot avec timeout court"""
    category_dir = SCREENSHOTS_DIR / category
    category_dir.mkdir(parents=True, exist_ok=True)
    output_file = category_dir / f"{tool_name}.png"

    if output_file.exists():
        print(f"  ⊳ Exists: {tool_name}")
        return 'skipped'

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

            try:
                await page.goto(url, wait_until='domcontentloaded', timeout=20000)
            except:
                await page.goto(url, timeout=20000)

            await asyncio.sleep(2)

            await page.screenshot(path=str(output_file), full_page=False)

            await browser.close()

            size = output_file.stat().st_size / 1024
            print(f" ✓ ({size:.0f}KB)")
            return 'success'

    except asyncio.TimeoutError:
        print(f" ✗ Timeout")
        return 'failed'
    except Exception as e:
        print(f" ✗ Error: {str(e)[:50]}")
        return 'failed'

async def main():
    print("=" * 70)
    print("Extended Screenshot Batch - 70+ Additional AI Tools")
    print("=" * 70)

    stats = {
        'total': len(EXTENDED_TOOLS),
        'success': 0,
        'failed': 0,
        'skipped': 0
    }

    category_stats = {}

    for i, (key, url) in enumerate(EXTENDED_TOOLS.items(), 1):
        category, tool_name = key.split('/')

        if category not in category_stats:
            category_stats[category] = {'success': 0, 'failed': 0, 'skipped': 0}

        print(f"\n[{i}/{stats['total']}] {tool_name} ({category})")

        result = await capture_one(category, tool_name, url)

        stats[result] += 1
        category_stats[category][result] += 1

        await asyncio.sleep(1)

    # Rapport final
    print("\n" + "=" * 70)
    print("📊 Global Results")
    print("=" * 70)
    print(f"Total: {stats['total']}")
    print(f"✓ Success: {stats['success']}")
    print(f"✗ Failed: {stats['failed']}")
    print(f"⊳ Skipped: {stats['skipped']}")

    # Rapport par catégorie
    print("\n" + "=" * 70)
    print("📂 Results by Category")
    print("=" * 70)
    for cat in sorted(category_stats.keys()):
        s = category_stats[cat]
        total = s['success'] + s['failed'] + s['skipped']
        print(f"{cat:20s}: {s['success']:2d} ✓  {s['failed']:2d} ✗  {s['skipped']:2d} ⊳  ({total} total)")

    print("=" * 70)

    # Liste les dossiers
    print(f"\n📁 Screenshots in: {SCREENSHOTS_DIR}")
    for cat_dir in sorted(SCREENSHOTS_DIR.iterdir()):
        if cat_dir.is_dir():
            pngs = list(cat_dir.glob("*.png"))
            if pngs:
                print(f"  {cat_dir.name:20s}: {len(pngs)} files")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n⚠ Interrupted by user")
        sys.exit(1)
