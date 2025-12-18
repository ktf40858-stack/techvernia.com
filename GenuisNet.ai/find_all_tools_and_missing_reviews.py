#!/usr/bin/env python3
"""
Extraire TOUS les outils depuis les catégories et vérifier leurs pages de review
"""

import os
import re
from bs4 import BeautifulSoup
from pathlib import Path

def extract_tools_from_category(html_file):
    """Extraire tous les outils depuis une page de catégorie"""
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')

        tools = []

        # Chercher toutes les cartes d'outils
        tool_cards = soup.find_all('a', class_='tool-card')

        for card in tool_cards:
            # Extraire le nom de l'outil
            h3 = card.find('h3')
            if not h3:
                continue

            tool_name = h3.get_text(strip=True)

            # Extraire le lien href
            href = card.get('href', '')

            # Déterminer la catégorie depuis le nom du fichier
            category_file = os.path.basename(html_file)
            category = category_file.replace('ai-', '').replace('.html', '')

            # Si le href pointe vers une review, extraire le chemin
            if '../reviews/' in href:
                # Format: ../reviews/category/toolname.html
                parts = href.split('/')
                review_category = parts[-2] if len(parts) >= 3 else category
                review_file = parts[-1] if len(parts) >= 1 else f"{tool_name.lower().replace(' ', '-')}.html"
                review_path = f"pages/reviews/{review_category}/{review_file}"
            else:
                # Pas de lien review, construire le chemin attendu
                tool_slug = tool_name.lower().replace(' ', '-').replace('.', '')
                review_path = f"pages/reviews/{category}/{tool_slug}.html"

            exists = os.path.exists(review_path)

            tools.append({
                'name': tool_name,
                'category': category,
                'href': href,
                'review_path': review_path,
                'exists': exists,
                'has_link': '../reviews/' in href
            })

        return tools

    except Exception as e:
        print(f"❌ Erreur: {html_file}: {e}")
        return []

def main():
    print("="*70)
    print("🔍 EXTRACTION DE TOUS LES OUTILS ET VÉRIFICATION DES REVIEWS")
    print("="*70)
    print()

    all_tools = []

    # Scanner toutes les catégories
    for cat_file in sorted(os.listdir('pages/categories')):
        if cat_file.startswith('ai-') and cat_file.endswith('.html'):
            file_path = f'pages/categories/{cat_file}'

            print(f"📄 Scan: {cat_file}")
            tools = extract_tools_from_category(file_path)
            all_tools.extend(tools)
            print(f"   Trouvés: {len(tools)} outils")

    print()
    print("="*70)
    print("📊 RÉSULTATS")
    print("="*70)
    print()

    # Statistiques
    total = len(all_tools)
    with_review = len([t for t in all_tools if t['exists']])
    without_review = len([t for t in all_tools if not t['exists']])
    with_link = len([t for t in all_tools if t['has_link']])
    without_link = len([t for t in all_tools if not t['has_link']])

    print(f"📊 TOTAL: {total} outils")
    print(f"✅ Avec page de review existante: {with_review}")
    print(f"❌ Sans page de review: {without_review}")
    print(f"🔗 Avec lien vers review: {with_link}")
    print(f"⚠️  Sans lien vers review: {without_link}")
    print()

    # Grouper par catégorie
    by_category = {}
    for tool in all_tools:
        cat = tool['category']
        if cat not in by_category:
            by_category[cat] = []
        by_category[cat].append(tool)

    # Afficher les outils manquants par catégorie
    print("="*70)
    print("❌ OUTILS SANS PAGE DE REVIEW")
    print("="*70)
    print()

    missing_count = 0
    for category in sorted(by_category.keys()):
        tools = by_category[category]
        missing = [t for t in tools if not t['exists']]

        if missing:
            print(f"\n📁 {category.upper()} ({len(missing)} manquants sur {len(tools)})")
            for tool in missing:
                print(f"   ❌ {tool['name']}")
                print(f"      Chemin attendu: {tool['review_path']}")
                print(f"      A un lien: {'Oui' if tool['has_link'] else 'Non'}")
            missing_count += len(missing)

    if missing_count == 0:
        print("✅ Aucune page de review manquante!")

    print()
    print("="*70)
    print(f"TOTAL À CRÉER: {missing_count} pages de review")
    print("="*70)

    # Sauvegarder la liste
    if missing_count > 0:
        with open('tools_missing_reviews.txt', 'w', encoding='utf-8') as f:
            f.write("OUTILS SANS PAGE DE REVIEW\n")
            f.write("="*70 + "\n\n")

            for category in sorted(by_category.keys()):
                tools = by_category[category]
                missing = [t for t in tools if not t['exists']]

                if missing:
                    f.write(f"\n{category.upper()}:\n")
                    for tool in missing:
                        f.write(f"  - {tool['name']}\n")
                        f.write(f"    Path: {tool['review_path']}\n")
                        f.write(f"    Has link: {tool['has_link']}\n\n")

        print(f"\n💾 Liste sauvegardée: tools_missing_reviews.txt")

if __name__ == '__main__':
    main()
