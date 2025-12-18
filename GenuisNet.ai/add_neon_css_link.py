#!/usr/bin/env python3
"""
Ajouter le lien vers neon-icons.css dans toutes les pages HTML
"""

import os
import re
from bs4 import BeautifulSoup

def add_css_link(file_path):
    """Ajouter le lien CSS pour les icônes néon"""

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Vérifier si le lien CSS existe déjà
        if 'neon-icons.css' in content:
            return False

        soup = BeautifulSoup(content, 'html.parser')
        head = soup.find('head')

        if not head:
            return False

        # Calculer le chemin relatif vers le CSS
        depth = file_path.count('/') - file_path.count('pages/')
        if 'pages/reviews/' in file_path:
            css_path = '../../../css/neon-icons.css'
        elif 'pages/categories/' in file_path or 'pages/' in file_path:
            css_path = '../css/neon-icons.css'
        else:
            css_path = 'css/neon-icons.css'

        # Créer le nouveau lien CSS
        new_link = soup.new_tag('link', rel='stylesheet', href=css_path)

        # Trouver le dernier link CSS
        last_css = head.find_all('link', rel='stylesheet')
        if last_css:
            last_css[-1].insert_after(new_link)
        else:
            head.append(new_link)

        # Sauvegarder
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))

        return True

    except Exception as e:
        return False

def main():
    print("="*70)
    print("🔗 AJOUT DU LIEN CSS POUR LES ICÔNES NÉON")
    print("="*70)
    print()

    total_updated = 0
    files_to_process = []

    # Page d'accueil
    files_to_process.append('index.html')

    # Pages de catégories
    for file in os.listdir('pages/categories'):
        if file.endswith('.html'):
            files_to_process.append(f'pages/categories/{file}')

    # Pages de reviews
    for category in os.listdir('pages/reviews'):
        category_path = f'pages/reviews/{category}'
        if os.path.isdir(category_path):
            for file in os.listdir(category_path):
                if file.endswith('.html'):
                    files_to_process.append(f'{category_path}/{file}')

    # Pages autres
    for file in ['pages/about.html', 'pages/guides.html', 'pages/categories.html']:
        if os.path.exists(file):
            files_to_process.append(file)

    print(f"📁 Fichiers à traiter: {len(files_to_process)}")
    print()

    for file_path in files_to_process:
        if add_css_link(file_path):
            total_updated += 1

    print(f"✅ Lien CSS ajouté: {total_updated}/{len(files_to_process)} fichiers")
    print()
    print("="*70)
    print("✅ TERMINÉ!")
    print("="*70)

if __name__ == '__main__':
    main()
