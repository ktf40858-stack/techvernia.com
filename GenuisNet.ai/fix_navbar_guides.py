#!/usr/bin/env python3
"""
Script pour:
1. Supprimer les liens nav-links dans les guides
2. Ajouter JS pour cacher le logo au scroll
"""

import os
import re
from pathlib import Path

# JS pour cacher le logo au scroll
SCROLL_SCRIPT = """
    <script>
        // Cacher le logo au scroll
        let lastScroll = 0;
        const navbar = document.querySelector('.navbar');
        const logo = document.querySelector('.logo');

        window.addEventListener('scroll', () => {
            const currentScroll = window.pageYOffset;

            if (currentScroll > 100) {
                // On a scrollé vers le bas - cacher le logo
                logo.style.opacity = '0';
                logo.style.pointerEvents = 'none';
            } else {
                // En haut de la page - montrer le logo
                logo.style.opacity = '1';
                logo.style.pointerEvents = 'auto';
            }

            lastScroll = currentScroll;
        });
    </script>"""

def fix_navbar_in_guide(file_path):
    """Supprime nav-links et ajoute le script de scroll."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Supprimer la section nav-links
        content = re.sub(
            r'<div class="nav-links">.*?</div>',
            '',
            content,
            flags=re.DOTALL
        )

        # Ajouter le script avant </body> si pas déjà présent
        if 'Cacher le logo au scroll' not in content:
            content = content.replace('</body>', f'{SCROLL_SCRIPT}\n</body>')

        # Ajouter transition CSS pour le logo si pas présent
        if 'logo { transition:' not in content and '<style>' in content:
            logo_transition = """
        .logo {
            transition: opacity 0.3s ease;
        }
"""
            content = content.replace('<style>', f'<style>\n{logo_transition}')

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
    """Corrige tous les guides."""
    base_dir = Path('/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai')
    guides_dir = base_dir / 'pages' / 'guides'

    files_modified = 0
    files_processed = 0

    print("🔧 Correction de la navbar dans les guides...\n")

    if guides_dir.exists():
        for html_file in guides_dir.glob('*.html'):
            files_processed += 1
            if fix_navbar_in_guide(html_file):
                files_modified += 1
                print(f"✓ Modifié: {html_file.name}")

    print(f"\n✅ Terminé!")
    print(f"📊 Fichiers traités: {files_processed}")
    print(f"📝 Fichiers modifiés: {files_modified}")
    print("\n🎯 Changements:")
    print("  ✓ Liens 'Guides' et 'Categories' supprimés")
    print("  ✓ Logo disparaît au scroll (après 100px)")

if __name__ == '__main__':
    main()
