#!/usr/bin/env python3
"""
Vérifier quels outils IA n'ont PAS de page de review
"""

import os
import re
from bs4 import BeautifulSoup
from pathlib import Path

def extract_review_links(html_file):
    """Extraire tous les liens vers les reviews depuis une page de catégorie"""
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')

        links = []
        # Chercher tous les liens vers ../reviews/
        for a in soup.find_all('a', href=True):
            href = a['href']
            if '../reviews/' in href and href.endswith('.html'):
                # Extraire le nom de l'outil depuis le lien
                tool_name = href.split('/')[-1].replace('.html', '')
                category = href.split('/')[-2]

                # Construire le chemin complet
                full_path = os.path.join('pages/reviews', category, tool_name + '.html')

                # Extraire le nom affiché
                display_name = a.get_text(strip=True) or tool_name
                if display_name == 'Full Review':
                    # Chercher le nom dans un h3 parent
                    parent = a.find_parent('a')
                    if parent:
                        h3 = parent.find('h3')
                        if h3:
                            display_name = h3.get_text(strip=True)

                links.append({
                    'category': category,
                    'tool_name': tool_name,
                    'display_name': display_name,
                    'path': full_path,
                    'exists': os.path.exists(full_path)
                })

        return links
    except Exception as e:
        print(f"Erreur lors de la lecture de {html_file}: {e}")
        return []

def main():
    print("="*70)
    print("🔍 VÉRIFICATION DES PAGES DE REVIEW MANQUANTES")
    print("="*70)
    print()

    all_tools = {}

    # Scanner toutes les catégories
    category_dir = 'pages/categories'
    for file in os.listdir(category_dir):
        if file.endswith('.html') and not file.startswith('guides'):
            file_path = os.path.join(category_dir, file)

            # Ignorer les backups
            if 'backup' in file_path:
                continue

            print(f"📄 Scan: {file}")
            links = extract_review_links(file_path)

            for link in links:
                key = f"{link['category']}/{link['tool_name']}"
                if key not in all_tools:
                    all_tools[key] = link

    print()
    print("="*70)
    print("📊 RÉSULTATS")
    print("="*70)
    print()

    # Trier par catégorie
    by_category = {}
    for tool in all_tools.values():
        cat = tool['category']
        if cat not in by_category:
            by_category[cat] = []
        by_category[cat].append(tool)

    total_tools = 0
    total_missing = 0

    for category in sorted(by_category.keys()):
        tools = by_category[category]
        missing = [t for t in tools if not t['exists']]

        total_tools += len(tools)
        total_missing += len(missing)

        status = "✅" if len(missing) == 0 else f"❌ {len(missing)} manquants"
        print(f"\n📁 {category.upper()} ({len(tools)} outils) - {status}")

        if missing:
            for tool in missing:
                print(f"   ❌ {tool['display_name']}")
                print(f"      → {tool['path']}")

    print()
    print("="*70)
    print(f"📊 TOTAL: {total_tools} outils")
    print(f"✅ Existants: {total_tools - total_missing}")
    print(f"❌ Manquants: {total_missing}")
    print("="*70)

    # Sauvegarder la liste des manquants
    if total_missing > 0:
        with open('missing_reviews.txt', 'w', encoding='utf-8') as f:
            f.write("PAGES DE REVIEW MANQUANTES\n")
            f.write("="*70 + "\n\n")

            for category in sorted(by_category.keys()):
                tools = by_category[category]
                missing = [t for t in tools if not t['exists']]

                if missing:
                    f.write(f"\n{category.upper()}:\n")
                    for tool in missing:
                        f.write(f"  - {tool['display_name']} ({tool['tool_name']})\n")
                        f.write(f"    Path: {tool['path']}\n")

        print(f"\n💾 Liste sauvegardée dans: missing_reviews.txt")

if __name__ == '__main__':
    main()
