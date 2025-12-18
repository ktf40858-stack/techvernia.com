#!/usr/bin/env python3
"""
Script pour mettre à jour les logos dans tous les guides avec le vrai logo SVG
"""

import os
import re
from pathlib import Path

# Ancien logo SVG à remplacer
OLD_LOGO_PATTERN = r'<a href="[^"]*" class="logo">\s*<span class="logo-icon">\s*<svg[^>]*>.*?</svg>\s*</span>\s*<span class="logo-text">Genuis<span class="highlight">Net</span>\.ai</span>\s*</a>'

# Nouveau logo
NEW_LOGO = '''<a href="../../index.html" class="logo">
                <img src="../../assets/images/logo.svg" alt="GenuisNet.ai Logo" class="logo-image">
            </a>'''

def update_logo_in_file(file_path):
    """Remplace l'ancien logo par le nouveau dans un fichier."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Remplacer l'ancien logo par le nouveau
        content = re.sub(OLD_LOGO_PATTERN, NEW_LOGO, content, flags=re.DOTALL)

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
    """Met à jour les logos dans tous les guides."""
    base_dir = Path('/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai')
    guides_dir = base_dir / 'pages' / 'guides'

    files_modified = 0
    files_processed = 0

    print("🔄 Mise à jour des logos dans les guides...\n")

    if guides_dir.exists():
        for html_file in guides_dir.glob('*.html'):
            files_processed += 1
            if update_logo_in_file(html_file):
                files_modified += 1
                print(f"✓ Modifié: {html_file.name}")

    print(f"\n✅ Terminé!")
    print(f"📊 Fichiers traités: {files_processed}")
    print(f"📝 Fichiers modifiés: {files_modified}")

if __name__ == '__main__':
    main()
