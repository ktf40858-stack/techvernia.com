#!/usr/bin/env python3
"""
Script pour ajouter le CSS guides-reviews.css à tous les guides et reviews
"""

import os
from pathlib import Path

def add_css_link(file_path):
    """Ajoute le lien CSS guides-reviews.css si pas déjà présent."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Vérifier si le CSS est déjà inclus
        if 'guides-reviews.css' in content:
            return False

        # Déterminer le chemin relatif correct
        if 'pages/guides' in str(file_path):
            css_path = '../../css/guides-reviews.css'
        elif 'pages/reviews' in str(file_path):
            css_path = '../../../css/guides-reviews.css'
        else:
            return False

        # Ajouter le lien CSS après style.css
        css_link = f'    <link rel="stylesheet" href="{css_path}">\n'

        if 'css/style.css' in content:
            content = content.replace(
                'css/style.css">',
                f'css/style.css">\n{css_link}'
            )
        elif '</head>' in content:
            content = content.replace('</head>', f'{css_link}    </head>')
        else:
            return False

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        return True
    except Exception as e:
        print(f"Erreur avec {file_path}: {e}")
        return False

def main():
    """Ajoute le CSS à tous les guides et reviews."""
    base_dir = Path('/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai')

    # Dossiers cibles
    target_dirs = [
        base_dir / 'pages' / 'guides',
        base_dir / 'pages' / 'reviews',
    ]

    files_modified = 0
    files_processed = 0

    print("🎨 Ajout du CSS guides-reviews.css aux fichiers...\n")

    for target_dir in target_dirs:
        if not target_dir.exists():
            continue

        for html_file in target_dir.rglob('*.html'):
            files_processed += 1
            if add_css_link(html_file):
                files_modified += 1
                print(f"✓ Modifié: {html_file.relative_to(base_dir)}")

    print(f"\n✅ Terminé!")
    print(f"📊 Fichiers traités: {files_processed}")
    print(f"📝 Fichiers modifiés: {files_modified}")

if __name__ == '__main__':
    main()
