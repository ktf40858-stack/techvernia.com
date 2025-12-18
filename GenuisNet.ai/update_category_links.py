#!/usr/bin/env python3
"""
Mettre à jour les liens dans les pages de catégories pour pointer vers les reviews
"""

import os
import re
from bs4 import BeautifulSoup

def update_category_page(html_file, category_name):
    """Mettre à jour les liens vers les reviews dans une page de catégorie"""

    try:
        with open(html_file, 'r', encoding='utf-8') as f:
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

            # Construire le lien vers la review
            review_link = f"../reviews/{category_name}/{tool_slug}.html"

            # Vérifier si le fichier existe
            review_path = f"pages/reviews/{category_name}/{tool_slug}.html"

            if os.path.exists(review_path):
                # Mettre à jour le href
                current_href = card.get('href', '')

                # Si le lien ne pointe pas déjà vers une review, le mettre à jour
                if not current_href.startswith('../reviews/'):
                    card['href'] = review_link
                    updated += 1
                    print(f"      ✅ {tool_name} → {review_link}")

        if updated > 0:
            # Sauvegarder le fichier
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(str(soup))

        return updated

    except Exception as e:
        print(f"   ❌ Erreur: {e}")
        return 0

def main():
    print("="*70)
    print("🔗 MISE À JOUR DES LIENS VERS LES REVIEWS")
    print("="*70)
    print()

    categories_to_update = {
        'ai-analytics.html': 'analytics',
        'ai-customer-service.html': 'customer-service',
        'ai-education.html': 'education',
        'ai-gaming.html': 'gaming',
        'ai-hr.html': 'hr',
        'ai-legal.html': 'legal',
        'ai-quantum.html': 'quantum',
        'ai-research.html': 'research',
        'ai-sales.html': 'sales',
        'ai-translation.html': 'translation'
    }

    total_updated = 0

    for html_file, category in categories_to_update.items():
        file_path = f'pages/categories/{html_file}'

        if os.path.exists(file_path):
            print(f"📄 {html_file}")
            updated = update_category_page(file_path, category)
            total_updated += updated

            if updated == 0:
                print(f"   ℹ️  Aucun lien à mettre à jour")
        else:
            print(f"⚠️  Fichier non trouvé: {file_path}")

    print()
    print("="*70)
    print(f"✅ Total de liens mis à jour: {total_updated}")
    print("="*70)

if __name__ == '__main__':
    main()
