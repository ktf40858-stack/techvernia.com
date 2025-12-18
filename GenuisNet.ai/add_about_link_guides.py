#!/usr/bin/env python3
"""
Script pour ajouter le lien About Us dans la navbar des guides
"""

import os
import re
from pathlib import Path

def add_about_link(file_path):
    """Ajoute le lien About Us dans la navbar."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Trouver la navbar et ajouter le lien About après le logo
        # Pattern: après </a> du logo et avant </div> du container
        pattern = r'(<a href="[^"]*index\.html" class="logo">.*?</a>)\s*(</div>\s*</nav>)'

        about_link = '''
            <div class="nav-links">
                <a href="../../pages/about.html">About Us</a>
            </div>
        '''

        replacement = r'\1' + about_link + r'\2'

        content = re.sub(pattern, replacement, content, flags=re.DOTALL)

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
    """Ajoute About Us à tous les guides."""
    base_dir = Path('/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai')
    guides_dir = base_dir / 'pages' / 'guides'

    files_modified = 0
    files_processed = 0

    print("🔧 Ajout du lien 'About Us' dans les guides...\n")

    if guides_dir.exists():
        for html_file in guides_dir.glob('*.html'):
            files_processed += 1
            if add_about_link(html_file):
                files_modified += 1
                print(f"✓ Modifié: {html_file.name}")

    print(f"\n✅ Terminé!")
    print(f"📊 Fichiers traités: {files_processed}")
    print(f"📝 Fichiers modifiés: {files_modified}")

if __name__ == '__main__':
    main()
