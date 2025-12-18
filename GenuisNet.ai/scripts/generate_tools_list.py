#!/usr/bin/env python3
"""
Génère une liste complète de tous les outils IA du projet
avec leurs métadonnées et URLs
"""

import json
import csv
from pathlib import Path
from typing import List, Dict
import re

# Configuration
BASE_DIR = Path(__file__).parent.parent
REVIEWS_DIR = BASE_DIR / "pages" / "reviews"
SCREENSHOTS_DIR = BASE_DIR / "assets" / "screenshots"

def extract_tools_info() -> List[Dict]:
    """Extrait les informations de tous les outils"""
    tools = []

    for category_dir in sorted(REVIEWS_DIR.iterdir()):
        if not category_dir.is_dir():
            continue

        category = category_dir.name

        for html_file in sorted(category_dir.glob("*.html")):
            tool_name = html_file.stem

            # Vérifie si le screenshot existe
            screenshot_exists = False
            screenshot_path = SCREENSHOTS_DIR / category / f"{tool_name}.png"
            if screenshot_path.exists():
                screenshot_exists = True

            # Essaie d'extraire l'URL depuis le fichier HTML
            url = extract_url_from_html(html_file)

            tools.append({
                'name': tool_name,
                'category': category,
                'html_file': str(html_file.relative_to(BASE_DIR)),
                'url': url or '',
                'screenshot_exists': screenshot_exists,
                'screenshot_path': str(screenshot_path.relative_to(BASE_DIR)) if screenshot_exists else ''
            })

    return tools

def extract_url_from_html(html_file: Path) -> str:
    """Extrait l'URL officielle depuis un fichier HTML"""
    try:
        content = html_file.read_text(encoding='utf-8')

        # Cherche un lien "Visit Website" ou "Official Site"
        patterns = [
            r'href=["\'](https?://[^"\']+)["\'].*(?:visit|official|website)',
            r'<meta\s+property=["\']og:url["\']\s+content=["\'](https?://[^"\']+)["\']',
            r'<link\s+rel=["\']canonical["\']\s+href=["\'](https?://[^"\']+)["\']',
        ]

        for pattern in patterns:
            match = re.search(pattern, content, re.IGNORECASE)
            if match:
                return match.group(1)

    except Exception as e:
        pass

    return ''

def main():
    """Fonction principale"""
    print("=" * 70)
    print("AI Tools List Generator")
    print("=" * 70)

    print("\n📋 Scanning project for AI tools...")
    tools = extract_tools_info()

    print(f"Found {len(tools)} tools across {len(set(t['category'] for t in tools))} categories\n")

    # Statistiques
    with_screenshot = sum(1 for t in tools if t['screenshot_exists'])
    without_screenshot = len(tools) - with_screenshot
    with_url = sum(1 for t in tools if t['url'])

    print("📊 Statistics:")
    print(f"  Total tools: {len(tools)}")
    print(f"  ✓ With screenshot: {with_screenshot} ({with_screenshot/len(tools)*100:.1f}%)")
    print(f"  ✗ Without screenshot: {without_screenshot} ({without_screenshot/len(tools)*100:.1f}%)")
    print(f"  🔗 With URL: {with_url} ({with_url/len(tools)*100:.1f}%)")

    # Sauvegarde en JSON
    json_file = BASE_DIR / "tools_list.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(tools, f, indent=2, ensure_ascii=False)

    print(f"\n✓ JSON saved to: {json_file}")

    # Sauvegarde en CSV
    csv_file = BASE_DIR / "tools_list.csv"
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'category', 'url', 'screenshot_exists', 'screenshot_path', 'html_file'])
        writer.writeheader()
        writer.writerows(tools)

    print(f"✓ CSV saved to: {csv_file}")

    # Affiche les catégories
    print("\n📂 Categories:")
    categories = {}
    for tool in tools:
        cat = tool['category']
        if cat not in categories:
            categories[cat] = {'total': 0, 'with_screenshot': 0}
        categories[cat]['total'] += 1
        if tool['screenshot_exists']:
            categories[cat]['with_screenshot'] += 1

    for cat in sorted(categories.keys()):
        total = categories[cat]['total']
        with_ss = categories[cat]['with_screenshot']
        percent = (with_ss / total * 100) if total > 0 else 0
        print(f"  {cat:20s}: {total:3d} tools, {with_ss:3d} screenshots ({percent:5.1f}%)")

    # Génère une liste Markdown
    md_file = BASE_DIR / "TOOLS_LIST.md"
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write("# Liste des outils IA\n\n")
        f.write(f"**Total**: {len(tools)} outils dans {len(categories)} catégories\n\n")

        for cat in sorted(categories.keys()):
            f.write(f"\n## {cat.replace('-', ' ').title()}\n\n")

            cat_tools = [t for t in tools if t['category'] == cat]
            for tool in sorted(cat_tools, key=lambda x: x['name']):
                status = "✓" if tool['screenshot_exists'] else "✗"
                url_link = f"[🔗]({tool['url']})" if tool['url'] else "⚠️ No URL"
                f.write(f"- {status} **{tool['name']}** - {url_link}\n")

    print(f"✓ Markdown saved to: {md_file}")

    # Génère un fichier de tâches pour les screenshots manquants
    missing_file = BASE_DIR / "screenshots_missing.txt"
    with open(missing_file, 'w', encoding='utf-8') as f:
        f.write("# Screenshots manquants\n\n")
        for tool in sorted(tools, key=lambda x: (x['category'], x['name'])):
            if not tool['screenshot_exists']:
                f.write(f"{tool['category']}/{tool['name']}\n")

    missing_count = sum(1 for t in tools if not t['screenshot_exists'])
    print(f"✓ Missing screenshots list saved to: {missing_file} ({missing_count} items)")

    print("\n" + "=" * 70)
    print("Done! Files generated:")
    print(f"  - {json_file}")
    print(f"  - {csv_file}")
    print(f"  - {md_file}")
    print(f"  - {missing_file}")
    print("=" * 70)

if __name__ == "__main__":
    main()
