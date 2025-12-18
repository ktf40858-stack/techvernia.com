#!/usr/bin/env python3
"""
Implémenter les logos dans les pages de catégories et reviews
"""

import os
import re
from bs4 import BeautifulSoup
from pathlib import Path

def update_category_page_logos(category_file, category_name):
    """Mettre à jour les logos dans une page de catégorie"""

    try:
        with open(category_file, 'r', encoding='utf-8') as f:
            content = f.read()

        soup = BeautifulSoup(content, 'html.parser')
        updated = 0

        # Trouver toutes les cartes d'outils
        tool_cards = soup.find_all('a', class_='tool-card')

        for card in tool_cards:
            # Extraire le nom de l'outil
            h3 = card.find('h3')
            if not h3:
                continue

            tool_name = h3.get_text(strip=True)

            # Créer le slug
            tool_slug = tool_name.lower()
            tool_slug = tool_slug.replace(' ', '-')
            tool_slug = tool_slug.replace('.', '')
            tool_slug = tool_slug.replace('(', '').replace(')', '')
            tool_slug = tool_slug.replace('/', '-')

            # Vérifier si le logo existe
            logo_path = f'assets/images/logos/{tool_slug}.png'
            if not os.path.exists(logo_path):
                continue

            # Chercher le logo actuel dans la carte
            logo_div = card.find('div', class_='tool-logo')
            if logo_div:
                # Remplacer par une image
                logo_div.clear()
                img = soup.new_tag('img',
                    src=f'../../{logo_path}',
                    alt=f'{tool_name} logo',
                    style='width: 100%; height: 100%; object-fit: contain;')
                img['onerror'] = f"this.outerHTML='<div style=\\'display:flex;align-items:center;justify-content:center;width:100%;height:100%;font-size:1.5rem;font-weight:800;\\'>{ tool_name[0].upper()}</div>'"
                logo_div.append(img)
                updated += 1

        if updated > 0:
            # Sauvegarder
            with open(category_file, 'w', encoding='utf-8') as f:
                f.write(str(soup))

        return updated

    except Exception as e:
        print(f"   ❌ Erreur: {e}")
        return 0

def update_review_page_logo(review_file, tool_slug):
    """Mettre à jour le logo dans une page de review"""

    try:
        with open(review_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Vérifier si le logo existe
        logo_path = f'assets/images/logos/{tool_slug}.png'
        if not os.path.exists(logo_path):
            return False

        soup = BeautifulSoup(content, 'html.parser')

        # Trouver le div avec class="review-logo"
        logo_div = soup.find('div', class_='review-logo')
        if logo_div:
            # Extraire le nom de l'outil depuis le h1
            h1 = soup.find('h1')
            tool_name = h1.get_text().replace(' Review', '').strip() if h1 else tool_slug

            # Remplacer le contenu par une image
            logo_div.clear()
            img = soup.new_tag('img',
                src=f'../../../{logo_path}',
                alt=f'{tool_name} logo',
                style='width: 100%; height: 100%; object-fit: contain; padding: 15px;')
            img['onerror'] = f"this.outerHTML='<div style=\\'display:flex;align-items:center;justify-content:center;width:100%;height:100%;font-size:2rem;font-weight:800;color:white;\\'>{tool_name[0].upper()}</div>'"
            logo_div.append(img)

            # Sauvegarder
            with open(review_file, 'w', encoding='utf-8') as f:
                f.write(str(soup))

            return True

        return False

    except Exception as e:
        return False

def main():
    print("="*70)
    print("🖼️  IMPLÉMENTATION DES LOGOS")
    print("="*70)
    print()

    # Compter les logos disponibles
    logos_count = len([f for f in os.listdir('assets/images/logos') if f.endswith('.png')])
    print(f"📁 Logos disponibles: {logos_count}")
    print()

    # 1. Mettre à jour les pages de catégories
    print("📄 MISE À JOUR DES PAGES DE CATÉGORIES")
    print("-"*70)

    category_files = {
        'pages/categories/ai-analytics.html': 'analytics',
        'pages/categories/ai-customer-service.html': 'customer-service',
        'pages/categories/ai-education.html': 'education',
        'pages/categories/ai-gaming.html': 'gaming',
        'pages/categories/ai-hr.html': 'hr',
        'pages/categories/ai-legal.html': 'legal',
        'pages/categories/ai-quantum.html': 'quantum',
        'pages/categories/ai-research.html': 'research',
        'pages/categories/ai-sales.html': 'sales',
        'pages/categories/ai-translation.html': 'translation'
    }

    total_category_updates = 0

    for category_file, category_name in category_files.items():
        if os.path.exists(category_file):
            print(f"\n📁 {category_name.upper()}")
            updated = update_category_page_logos(category_file, category_name)
            total_category_updates += updated
            print(f"   ✅ {updated} logos mis à jour")

    # 2. Mettre à jour les pages de reviews
    print()
    print("="*70)
    print("📄 MISE À JOUR DES PAGES DE REVIEWS")
    print("-"*70)

    total_review_updates = 0

    for category in ['analytics', 'customer-service', 'education', 'gaming', 'hr', 'legal', 'quantum', 'research', 'sales', 'translation']:
        category_dir = f'pages/reviews/{category}'

        if not os.path.exists(category_dir):
            continue

        print(f"\n📁 {category.upper()}")

        for filename in sorted(os.listdir(category_dir)):
            if not filename.endswith('.html'):
                continue

            tool_slug = filename.replace('.html', '')
            review_file = f'{category_dir}/{filename}'

            if update_review_page_logo(review_file, tool_slug):
                print(f"   ✅ {tool_slug}")
                total_review_updates += 1

    print()
    print("="*70)
    print(f"✅ IMPLÉMENTATION TERMINÉE!")
    print(f"   Pages de catégories: {total_category_updates} logos")
    print(f"   Pages de reviews: {total_review_updates} logos")
    print(f"   Total: {total_category_updates + total_review_updates} logos implémentés")
    print("="*70)

if __name__ == '__main__':
    main()
