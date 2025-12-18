#!/usr/bin/env python3
"""
Met à jour l'import de Google Fonts partout pour inclure Space Grotesk
"""

from pathlib import Path
import re

def update_fonts_in_file(file_path):
    """Met à jour les imports de fonts dans un fichier HTML."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Pattern ancien import (Inter + JetBrains Mono)
        old_pattern = r'<link href="https://fonts\.googleapis\.com/css2\?family=Inter:wght@[^"]+&family=JetBrains\+Mono:wght@[^"]+&display=swap" rel="stylesheet">'

        # Nouveau import avec Space Grotesk en premier
        new_import = '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">'

        content = re.sub(old_pattern, new_import, content)

        # Si pas d'import de fonts du tout, l'ajouter après preconnect
        if 'fonts.googleapis.com/css2' not in content and 'fonts.googleapis.com' in content:
            # Trouver le preconnect et ajouter après
            preconnect_pattern = r'(<link rel="preconnect" href="https://fonts\.gstatic\.com" crossorigin>)'
            replacement = r'\1\n    ' + new_import
            content = re.sub(preconnect_pattern, replacement, content)

        # Écrire seulement si changé
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False

    except Exception as e:
        print(f"Erreur avec {file_path}: {e}")
        return False

def main():
    """Met à jour tous les imports de fonts."""
    base_dir = Path('/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai')

    files_to_update = []

    # Trouver tous les fichiers HTML
    files_to_update.extend(base_dir.glob('*.html'))
    files_to_update.extend(base_dir.glob('pages/*.html'))
    files_to_update.extend(base_dir.glob('pages/guides/*.html'))
    files_to_update.extend(base_dir.glob('pages/categories/*.html'))

    updated_count = 0
    total_count = 0

    print("🔄 Mise à jour des imports Google Fonts...\n")

    for file_path in files_to_update:
        total_count += 1
        if update_fonts_in_file(file_path):
            updated_count += 1
            print(f"✅ {file_path.name}")

    print(f"\n🎉 Terminé!")
    print(f"📊 {updated_count}/{total_count} fichiers mis à jour")
    print(f"\n✨ Space Grotesk maintenant chargée partout!")

if __name__ == '__main__':
    main()
