#!/usr/bin/env python3
"""
Ajouter un bouton CTA "Try for Free" au début de chaque review (après le hero, avant Overview)
"""

import os
import re
from bs4 import BeautifulSoup

def add_top_cta(html_content, tool_name, color_primary, color_secondary):
    """Ajouter un CTA au début de la review"""

    soup = BeautifulSoup(html_content, 'html.parser')

    # Trouver le <div class="review-layout">
    review_layout = soup.find('div', class_='review-layout')

    if not review_layout:
        return html_content

    # Trouver le <main class="review-main">
    review_main = review_layout.find('main', class_='review-main')

    if not review_main:
        return html_content

    # Créer le CTA section
    cta_html = f'''
            <!-- CTA Section -->
            <div class="cta-top-section" style="background: linear-gradient(135deg, {color_primary}, {color_secondary}); border-radius: var(--radius-xl); padding: var(--space-2xl); text-align: center; margin-bottom: var(--space-xl);">
                <h2 style="color: white; font-size: var(--text-2xl); font-weight: 700; margin-bottom: var(--space-md); border: none; padding: 0;">Ready to Get Started?</h2>
                <p style="color: rgba(255, 255, 255, 0.9); font-size: var(--text-base); margin-bottom: var(--space-xl);">Try {tool_name} today and experience the power of AI-driven automation.</p>
                <div class="cta-buttons">
                    <a href="#" class="btn btn-white" style="background: white; color: {color_primary}; padding: var(--space-md) var(--space-2xl); border-radius: var(--radius-lg); font-weight: 600; text-decoration: none; display: inline-block; transition: transform 0.2s;">Try {tool_name} Free</a>
                    <a href="#pricing" class="btn btn-outline-white" style="background: transparent; color: white; border: 2px solid white; padding: var(--space-md) var(--space-2xl); border-radius: var(--radius-lg); font-weight: 600; text-decoration: none; display: inline-block; margin-left: var(--space-md); transition: all 0.2s;">View Pricing</a>
                </div>
            </div>
'''

    # Insérer le CTA au début de review-main (avant la première section)
    first_section = review_main.find('section')
    if first_section:
        cta_soup = BeautifulSoup(cta_html, 'html.parser')
        first_section.insert_before(cta_soup)

    return str(soup)

def process_all_reviews():
    """Traiter toutes les reviews"""

    print("="*70)
    print("🔗 AJOUT DES CTA 'TRY FOR FREE' EN HAUT DES REVIEWS")
    print("="*70)
    print()

    # Couleurs par catégorie
    category_colors = {
        'analytics': {'primary': '#3B82F6', 'secondary': '#2563EB'},
        'customer-service': {'primary': '#8B5CF6', 'secondary': '#7C3AED'},
        'education': {'primary': '#10B981', 'secondary': '#059669'},
        'gaming': {'primary': '#F59E0B', 'secondary': '#D97706'},
        'hr': {'primary': '#06B6D4', 'secondary': '#0891B2'},
        'legal': {'primary': '#6366F1', 'secondary': '#4F46E5'},
        'quantum': {'primary': '#EC4899', 'secondary': '#DB2777'},
        'research': {'primary': '#14B8A6', 'secondary': '#0D9488'},
        'sales': {'primary': '#F97316', 'secondary': '#EA580C'},
        'translation': {'primary': '#A855F7', 'secondary': '#9333EA'}
    }

    total_updated = 0

    # Parcourir toutes les catégories
    for category in category_colors.keys():
        category_dir = f'pages/reviews/{category}'

        if not os.path.exists(category_dir):
            continue

        print(f"\n📁 {category.upper()}")

        colors = category_colors[category]

        # Parcourir tous les fichiers HTML
        for filename in sorted(os.listdir(category_dir)):
            if not filename.endswith('.html'):
                continue

            file_path = os.path.join(category_dir, filename)

            try:
                # Lire le fichier
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Extraire le nom de l'outil depuis le <h1>
                soup = BeautifulSoup(content, 'html.parser')
                h1 = soup.find('h1')
                if h1:
                    tool_name = h1.get_text().replace(' Review', '').strip()
                else:
                    tool_name = filename.replace('.html', '').replace('-', ' ').title()

                # Ajouter le CTA
                updated_content = add_top_cta(content, tool_name, colors['primary'], colors['secondary'])

                # Sauvegarder
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)

                print(f"   ✅ {filename}")
                total_updated += 1

            except Exception as e:
                print(f"   ❌ {filename}: {e}")

    print()
    print("="*70)
    print(f"✅ CTA AJOUTÉ!")
    print(f"   Pages mises à jour: {total_updated}")
    print("="*70)

if __name__ == '__main__':
    process_all_reviews()
