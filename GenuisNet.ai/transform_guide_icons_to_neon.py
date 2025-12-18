#!/usr/bin/env python3
"""
Transforme toutes les icônes SVG des pages de guides en version néon
"""

from pathlib import Path
import re

def add_neon_to_svg_icons(file_path, color_gradient):
    """Ajoute des effets néon aux icônes SVG dans un fichier."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Pattern pour les icônes principales des cartes (36x36)
        # Remplace: <svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" width="36" height="36">
        pattern_main = r'<svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" width="36" height="36">'

        # Remplacement avec version néon
        replacement_main = f'''<svg viewBox="0 0 72 72" fill="none" xmlns="http://www.w3.org/2000/svg" width="48" height="48">
                                <defs>
                                    <linearGradient id="neonGrad{color_gradient['id']}" x1="0%" y1="0%" x2="100%" y2="100%">
                                        <stop offset="0%" style="stop-color:{color_gradient['start']}"/>
                                        <stop offset="100%" style="stop-color:{color_gradient['end']}"/>
                                    </linearGradient>
                                    <filter id="neonGlow{color_gradient['id']}">
                                        <feGaussianBlur in="SourceGraphic" stdDeviation="2" result="blur1"/>
                                        <feGaussianBlur in="SourceGraphic" stdDeviation="4" result="blur2"/>
                                        <feMerge>
                                            <feMergeNode in="blur2"/>
                                            <feMergeNode in="blur1"/>
                                            <feMergeNode in="SourceGraphic"/>
                                        </feMerge>
                                    </filter>
                                </defs>
                                <g transform="scale(3)" stroke="url(#neonGrad{color_gradient['id']})" stroke-width="2.5" filter="url(#neonGlow{color_gradient['id']})">'''

        content = content.replace(pattern_main, replacement_main)

        # Fermer le groupe <g> avant </svg>
        # Pattern pour trouver les </svg> qui suivent nos icônes transformées
        content = re.sub(
            r'(</path>|</line>|</polyline>|</circle>|</rect>)\s*</svg>',
            r'\1</g></svg>',
            content
        )

        # Modifier les backgrounds des tool-logo-large pour utiliser fond transparent avec bordure
        bg_pattern = r'style="background: linear-gradient\(135deg, #22C55E, #10B981\);'
        bg_replacement = f'style="background: rgba({color_gradient["rgb"]}, 0.1); border: 2px solid rgba({color_gradient["rgb"]}, 0.3);'
        content = content.replace(bg_pattern, bg_replacement)

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
    """Transforme les icônes dans les 3 pages de guides."""
    base_dir = Path('/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/categories')

    files_config = [
        {
            'file': base_dir / 'guides-beginner.html',
            'gradient': {
                'id': 'Beginner',
                'start': '#22C55E',
                'end': '#10B981',
                'rgb': '34, 197, 94'
            }
        },
        {
            'file': base_dir / 'guides-intermediate.html',
            'gradient': {
                'id': 'Intermediate',
                'start': '#3B82F6',
                'end': '#2563EB',
                'rgb': '59, 130, 246'
            }
        },
        {
            'file': base_dir / 'guides-advanced.html',
            'gradient': {
                'id': 'Advanced',
                'start': '#A855F7',
                'end': '#7C3AED',
                'rgb': '168, 85, 247'
            }
        }
    ]

    print("🎨 Transformation des icônes en néon...\n")

    updated_count = 0

    for config in files_config:
        file_path = config['file']
        if file_path.exists():
            if add_neon_to_svg_icons(file_path, config['gradient']):
                updated_count += 1
                print(f"✅ {file_path.name}")
            else:
                print(f"⚠️  {file_path.name} - Aucun changement")
        else:
            print(f"❌ {file_path.name} - Fichier non trouvé")

    print(f"\n🎉 Terminé! {updated_count}/3 fichiers mis à jour")
    print("✨ Toutes les icônes sont maintenant en néon!")

if __name__ == '__main__':
    main()
