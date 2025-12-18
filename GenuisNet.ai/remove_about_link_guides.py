#!/usr/bin/env python3
"""
Script pour supprimer le lien About Us de tous les guides
"""

import os
import re
from pathlib import Path

def remove_about_link(file_path):
    """Supprime le lien About Us de la navbar."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Supprimer la div nav-links avec About Us
        content = re.sub(
            r'<div class="nav-links">\s*<a href="[^"]*about\.html">About Us</a>\s*</div>',
            '',
            content,
            flags=re.DOTALL
        )

        # Supprimer aussi le style CSS About Us
        content = re.sub(
            r'/\* About Us link styling \*/.*?\.navbar \.nav-links a:hover \{[^}]+\}',
            '',
            content,
            flags=re.DOTALL
        )

        # Écrire seulement si des changements ont été faits
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Erreur avec {file_path}: {e}")
        return False

def main():
    """Supprime About Us de tous les guides."""
    base_dir = Path('/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai')
    guides_dir = base_dir / 'pages' / 'guides'

    files_modified = 0
    files_processed = 0

    print("🗑️  Suppression du lien 'About Us' des guides...\n")

    if guides_dir.exists():
        for html_file in guides_dir.glob('*.html'):
            files_processed += 1
            if remove_about_link(html_file):
                files_modified += 1
                print(f"✓ Modifié: {html_file.name}")

    print(f"\n✅ Terminé!")
    print(f"📊 Fichiers traités: {files_processed}")
    print(f"📝 Fichiers modifiés: {files_modified}")
    print("\n🎯 Le lien 'About Us' a été supprimé de tous les guides")

if __name__ == '__main__':
    main()
