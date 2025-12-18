#!/usr/bin/env python3
"""
Met à jour tous les logos dans le site pour utiliser le nouveau logo néon
"""

from pathlib import Path
import re

def update_logo_in_file(file_path):
    """Met à jour le logo dans un fichier HTML."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Pattern 1: <img src="...logo.svg" ...>
        # Remplacer par le nouveau logo-neon.svg en conservant les chemins relatifs corrects

        # Pour les fichiers dans /pages/
        if '/pages/' in str(file_path) and '/pages/guides/' not in str(file_path) and '/pages/categories/' not in str(file_path):
            content = re.sub(
                r'src="[^"]*logo\.svg"',
                'src="../assets/images/logo-neon.svg"',
                content
            )
        # Pour les fichiers dans /pages/guides/
        elif '/pages/guides/' in str(file_path):
            content = re.sub(
                r'src="[^"]*logo\.svg"',
                'src="../../assets/images/logo-neon.svg"',
                content
            )
        # Pour les fichiers dans /pages/categories/
        elif '/pages/categories/' in str(file_path):
            content = re.sub(
                r'src="[^"]*logo\.svg"',
                'src="../../assets/images/logo-neon.svg"',
                content
            )
        # Pour index.html à la racine
        else:
            content = re.sub(
                r'src="[^"]*logo\.svg"',
                'src="assets/images/logo-neon.svg"',
                content
            )

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
    """Met à jour tous les logos."""
    base_dir = Path('/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai')

    files_to_update = []

    # Trouver tous les fichiers HTML
    files_to_update.extend(base_dir.glob('*.html'))
    files_to_update.extend(base_dir.glob('pages/*.html'))
    files_to_update.extend(base_dir.glob('pages/guides/*.html'))
    files_to_update.extend(base_dir.glob('pages/categories/*.html'))

    updated_count = 0
    total_count = 0

    print("🔄 Mise à jour des logos...\n")

    for file_path in files_to_update:
        total_count += 1
        if update_logo_in_file(file_path):
            updated_count += 1
            print(f"✅ {file_path.name}")

    print(f"\n🎉 Terminé!")
    print(f"📊 {updated_count}/{total_count} fichiers mis à jour")
    print(f"\n✨ Nouveau logo néon appliqué partout!")
    print(f"✨ Police Space Grotesk maintenant utilisée sur tout le site!")

if __name__ == '__main__':
    main()
