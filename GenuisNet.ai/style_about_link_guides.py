#!/usr/bin/env python3
"""
Script pour ajouter le style CSS du lien About Us dans les guides
"""

import os
from pathlib import Path

# Style CSS pour le lien About
ABOUT_STYLE = """
        /* About Us link styling */
        .navbar .container {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .navbar .nav-links {
            display: flex;
            gap: var(--space-md);
        }

        .navbar .nav-links a {
            color: var(--text-primary);
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s ease;
            padding: 0.5rem 1rem;
            border-radius: var(--radius-md);
        }

        .navbar .nav-links a:hover {
            color: var(--accent-primary);
            background: rgba(0, 217, 255, 0.1);
        }
"""

def add_style_to_guide(file_path):
    """Ajoute le style CSS pour About Us."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Ajouter le style avant </style> si pas déjà présent
        if 'About Us link styling' not in content and '</style>' in content:
            content = content.replace('</style>', f'{ABOUT_STYLE}\n    </style>')

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
    """Ajoute le style à tous les guides."""
    base_dir = Path('/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai')
    guides_dir = base_dir / 'pages' / 'guides'

    files_modified = 0
    files_processed = 0

    print("🎨 Ajout du style pour 'About Us'...\n")

    if guides_dir.exists():
        for html_file in guides_dir.glob('*.html'):
            files_processed += 1
            if add_style_to_guide(html_file):
                files_modified += 1
                print(f"✓ Modifié: {html_file.name}")

    print(f"\n✅ Terminé!")
    print(f"📊 Fichiers traités: {files_processed}")
    print(f"📝 Fichiers modifiés: {files_modified}")

if __name__ == '__main__':
    main()
