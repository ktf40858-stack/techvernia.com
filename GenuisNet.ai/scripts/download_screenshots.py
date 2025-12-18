#!/usr/bin/env python3
"""
Script pour télécharger automatiquement des screenshots d'outils IA
"""

import os
import re
import json
import time
import requests
from pathlib import Path
from urllib.parse import quote_plus, urlparse
from typing import List, Dict, Optional

# Configuration
BASE_DIR = Path(__file__).parent.parent
REVIEWS_DIR = BASE_DIR / "pages" / "reviews"
SCREENSHOTS_DIR = BASE_DIR / "assets" / "screenshots"
SCREENSHOTS_DIR.mkdir(exist_ok=True)

# Headers pour simuler un navigateur
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def extract_tools_from_html(category: str) -> List[Dict[str, str]]:
    """Extrait la liste des outils d'une catégorie"""
    tools = []
    category_dir = REVIEWS_DIR / category

    if not category_dir.exists():
        return tools

    for html_file in category_dir.glob("*.html"):
        tool_name = html_file.stem
        tools.append({
            'name': tool_name,
            'category': category,
            'file': str(html_file)
        })

    return tools

def get_all_tools() -> List[Dict[str, str]]:
    """Récupère tous les outils de toutes les catégories"""
    all_tools = []

    for category_dir in REVIEWS_DIR.iterdir():
        if category_dir.is_dir():
            category = category_dir.name
            tools = extract_tools_from_html(category)
            all_tools.extend(tools)

    return all_tools

def sanitize_filename(name: str) -> str:
    """Nettoie un nom pour en faire un nom de fichier valide"""
    # Remplace les caractères spéciaux
    name = re.sub(r'[^\w\s-]', '', name)
    name = re.sub(r'[-\s]+', '-', name)
    return name.lower()

def search_screenshot_url(tool_name: str, category: str) -> Optional[str]:
    """
    Recherche l'URL d'un screenshot via différentes sources
    Note: Cette fonction utilise des APIs publiques
    """
    # Stratégie 1: Recherche sur Unsplash (images de haute qualité)
    unsplash_query = f"{tool_name} AI screenshot interface"

    # Stratégie 2: Utiliser les screenshots officiels (URLs connues)
    official_screenshots = {
        'chatgpt': 'https://cdn.openai.com/chatgpt/draft-20230627/ChatGPT_Diagram.png',
        'claude': 'https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F35e31c46371c19952f20bf3e404f098a9ef0a2b2-2100x1405.png',
        'midjourney': 'https://docs.midjourney.com/img/quick-start/Web_Application.png',
        'github-copilot': 'https://github.githubassets.com/images/modules/site/copilot/copilot-editor.png',
    }

    clean_name = sanitize_filename(tool_name)
    if clean_name in official_screenshots:
        return official_screenshots[clean_name]

    return None

def download_image(url: str, output_path: Path) -> bool:
    """Télécharge une image depuis une URL"""
    try:
        response = requests.get(url, headers=HEADERS, timeout=30, stream=True)
        response.raise_for_status()

        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"✓ Downloaded: {output_path.name}")
        return True

    except Exception as e:
        print(f"✗ Failed to download {url}: {e}")
        return False

def download_screenshots_for_tool(tool: Dict[str, str]) -> bool:
    """Télécharge le screenshot pour un outil donné"""
    tool_name = tool['name']
    category = tool['category']

    # Cherche l'URL du screenshot
    screenshot_url = search_screenshot_url(tool_name, category)

    if not screenshot_url:
        print(f"⚠ No screenshot URL found for {tool_name}")
        return False

    # Détermine le nom du fichier
    filename = f"{sanitize_filename(tool_name)}.png"
    category_dir = SCREENSHOTS_DIR / category
    category_dir.mkdir(exist_ok=True)

    output_path = category_dir / filename

    # Télécharge l'image
    return download_image(screenshot_url, output_path)

def main():
    """Fonction principale"""
    print("=" * 60)
    print("Screenshot Downloader for AI Tools")
    print("=" * 60)

    # Récupère tous les outils
    print("\n📋 Scanning project for AI tools...")
    tools = get_all_tools()
    print(f"Found {len(tools)} tools across {len(set(t['category'] for t in tools))} categories")

    # Crée un rapport
    report = {
        'total': len(tools),
        'downloaded': 0,
        'failed': 0,
        'skipped': 0
    }

    # Télécharge les screenshots
    print("\n🔄 Starting downloads...")
    print("-" * 60)

    for i, tool in enumerate(tools, 1):
        print(f"\n[{i}/{len(tools)}] {tool['name']} ({tool['category']})")

        # Vérifie si le screenshot existe déjà
        filename = f"{sanitize_filename(tool['name'])}.png"
        category_dir = SCREENSHOTS_DIR / tool['category']
        output_path = category_dir / filename

        if output_path.exists():
            print(f"⊳ Already exists: {filename}")
            report['skipped'] += 1
            continue

        # Télécharge
        success = download_screenshots_for_tool(tool)

        if success:
            report['downloaded'] += 1
        else:
            report['failed'] += 1

        # Pause pour éviter le rate limiting
        time.sleep(0.5)

    # Affiche le rapport final
    print("\n" + "=" * 60)
    print("📊 Download Report")
    print("=" * 60)
    print(f"Total tools: {report['total']}")
    print(f"✓ Downloaded: {report['downloaded']}")
    print(f"✗ Failed: {report['failed']}")
    print(f"⊳ Skipped (already exists): {report['skipped']}")
    print("=" * 60)

    # Sauvegarde le rapport
    report_file = SCREENSHOTS_DIR / "download_report.json"
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2)

    print(f"\n📄 Report saved to: {report_file}")

if __name__ == "__main__":
    main()
