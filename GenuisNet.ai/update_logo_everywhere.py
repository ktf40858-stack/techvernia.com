#!/usr/bin/env python3
"""
Met à jour le logo néon ULTRA HD partout sur le site web
"""

from pathlib import Path
import re

def update_logo_in_file(file_path):
    """Met à jour le logo dans un fichier HTML."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Pattern 1: Logo simple avec SVG dans navbar
        pattern1 = r'<a href="[^"]*" class="logo">\s*<span class="logo-icon">.*?</span>\s*<span class="logo-text">.*?</span>\s*</a>'

        # Déterminer le chemin relatif vers le logo selon la profondeur du fichier
        if '/pages/categories/' in str(file_path):
            logo_path = '../../assets/images/logo-neon.svg'
        elif '/pages/guides/' in str(file_path):
            logo_path = '../../assets/images/logo-neon.svg'
        elif '/pages/' in str(file_path):
            logo_path = '../assets/images/logo-neon.svg'
        else:
            logo_path = 'assets/images/logo-neon.svg'

        # Déterminer le lien de retour
        if '/pages/categories/' in str(file_path):
            home_link = '../../index.html'
        elif '/pages/guides/' in str(file_path):
            home_link = '../../index.html'
        elif '/pages/' in str(file_path):
            home_link = '../index.html'
        else:
            home_link = 'index.html'

        # Nouveau logo
        new_logo = f'<a href="{home_link}" class="logo">\n                <img src="{logo_path}" alt="GenuisNet.ai" style="height: 50px; width: auto;">\n            </a>'

        # Remplacer le pattern 1
        content = re.sub(pattern1, new_logo, content, flags=re.DOTALL)

        # Pattern 2: Logo avec juste <img> (déjà mis à jour)
        pattern2 = r'<a href="[^"]*" class="logo">\s*<img src="[^"]*" alt="GenuisNet\.ai"[^>]*>\s*</a>'

        if re.search(pattern2, content):
            # Mettre à jour le chemin si différent
            content = re.sub(
                r'<img src="[^"]*logo[^"]*" alt="GenuisNet\.ai"[^>]*>',
                f'<img src="{logo_path}" alt="GenuisNet.ai" style="height: 50px; width: auto;">',
                content
            )

        # Pattern 3: Logo dans footer
        footer_pattern = r'<a href="[^"]*" class="footer-logo">\s*<span class="logo-text">.*?</span>\s*</a>'
        footer_logo = f'<a href="{home_link}" class="footer-logo">\n                        <img src="{logo_path}" alt="GenuisNet.ai Logo" style="height: 40px; width: auto;">\n                    </a>'

        content = re.sub(footer_pattern, footer_logo, content, flags=re.DOTALL)

        # Pattern 4: Footer logo déjà en img
        content = re.sub(
            r'<img src="[^"]*logo[^"]*" alt="GenuisNet\.ai Logo"[^>]*>',
            f'<img src="{logo_path}" alt="GenuisNet.ai Logo" style="height: 40px; width: auto;">',
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
    """Met à jour le logo dans tous les fichiers HTML."""
    base_dir = Path('/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai')

    files_to_update = []

    # Fichiers à la racine
    files_to_update.extend(base_dir.glob('*.html'))

    # Fichiers dans pages/
    files_to_update.extend(base_dir.glob('pages/*.html'))

    # Fichiers dans pages/categories/
    files_to_update.extend(base_dir.glob('pages/categories/*.html'))

    # Fichiers dans pages/guides/
    files_to_update.extend(base_dir.glob('pages/guides/*.html'))

    print("🎨 Mise à jour du logo ULTRA HD néon partout...\n")

    updated_count = 0
    total_count = 0

    for file_path in files_to_update:
        # Ignorer les backups
        if '.backup' in str(file_path) or '.bak' in str(file_path) or '.temp' in str(file_path):
            continue

        total_count += 1
        if update_logo_in_file(file_path):
            updated_count += 1
            print(f"✅ {file_path.name}")

    print(f"\n{'='*50}")
    print(f"🎉 Terminé!")
    print(f"📊 {updated_count}/{total_count} fichiers mis à jour")
    print(f"✨ Logo ULTRA HD néon maintenant partout!")

if __name__ == '__main__':
    main()
