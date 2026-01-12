#!/usr/bin/env python3
"""
Script pour ajouter le lien mobile-fixes.css a toutes les pages HTML
"""

import os
import re
from pathlib import Path

def add_mobile_css_link(file_path):
    """Ajoute le lien vers mobile-fixes.css si absent"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Verifier si le lien existe deja
        if 'mobile-fixes.css' in content:
            print(f"OK {file_path.name} - deja a jour")
            return False

        # Verifier si c'est un fichier HTML valide avec une section <head>
        if '</head>' not in content:
            print(f"SKIP {file_path.name} - pas de balise </head> trouvee")
            return False

        # Determiner le chemin relatif correct vers le CSS
        # Compter le nombre de niveaux de dossiers
        depth = len(file_path.relative_to(Path('docs')).parts) - 1
        css_path = '../' * depth + 'css/mobile-fixes.css' if depth > 0 else 'css/mobile-fixes.css'

        # Creer le lien CSS
        css_link = f'<link href="{css_path}" rel="stylesheet"/>'

        # Inserer juste avant </head>
        new_content = content.replace('</head>', f'{css_link}\n</head>')

        # Ecrire le fichier modifie
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"ADDED {file_path.name}")
        return True

    except Exception as e:
        print(f"ERROR {file_path.name} - {e}")
        return False

def main():
    print("Adding mobile-fixes.css to all HTML pages...\n")

    docs_path = Path('docs')
    modified_count = 0
    total_count = 0

    # Parcourir tous les fichiers HTML
    for html_file in docs_path.rglob('*.html'):
        total_count += 1
        if add_mobile_css_link(html_file):
            modified_count += 1

    print(f"\nDone! {modified_count}/{total_count} files modified")

if __name__ == '__main__':
    main()
