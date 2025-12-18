#!/usr/bin/env python3
"""
Corrige correctement les icônes SVG des pages de guides en néon
"""

from pathlib import Path
import re

# Définition des différentes icônes SVG en version néon
ICON_TEMPLATES = {
    'book': '''<svg viewBox="0 0 72 72" fill="none" xmlns="http://www.w3.org/2000/svg" width="48" height="48">
                <defs>
                    <linearGradient id="neonGrad{id}" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:{color1}"/>
                        <stop offset="100%" style="stop-color:{color2}"/>
                    </linearGradient>
                    <filter id="neonGlow{id}">
                        <feGaussianBlur in="SourceGraphic" stdDeviation="2" result="blur1"/>
                        <feGaussianBlur in="SourceGraphic" stdDeviation="4" result="blur2"/>
                        <feMerge>
                            <feMergeNode in="blur2"/>
                            <feMergeNode in="blur1"/>
                            <feMergeNode in="SourceGraphic"/>
                        </feMerge>
                    </filter>
                </defs>
                <g transform="scale(3)" stroke="url(#neonGrad{id})" stroke-width="2.5" filter="url(#neonGlow{id})" fill="none">
                    <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/>
                    <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>
                </g>
            </svg>''',

    'chat': '''<svg viewBox="0 0 72 72" fill="none" xmlns="http://www.w3.org/2000/svg" width="48" height="48">
                <defs>
                    <linearGradient id="neonGrad{id}" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:{color1}"/>
                        <stop offset="100%" style="stop-color:{color2}"/>
                    </linearGradient>
                    <filter id="neonGlow{id}">
                        <feGaussianBlur in="SourceGraphic" stdDeviation="2" result="blur1"/>
                        <feGaussianBlur in="SourceGraphic" stdDeviation="4" result="blur2"/>
                        <feMerge>
                            <feMergeNode in="blur2"/>
                            <feMergeNode in="blur1"/>
                            <feMergeNode in="SourceGraphic"/>
                        </feMerge>
                    </filter>
                </defs>
                <g transform="scale(3)" stroke="url(#neonGrad{id})" stroke-width="2.5" filter="url(#neonGlow{id})" fill="none">
                    <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
                </g>
            </svg>''',

    'lightbulb': '''<svg viewBox="0 0 72 72" fill="none" xmlns="http://www.w3.org/2000/svg" width="48" height="48">
                <defs>
                    <linearGradient id="neonGrad{id}" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:{color1}"/>
                        <stop offset="100%" style="stop-color:{color2}"/>
                    </linearGradient>
                    <filter id="neonGlow{id}">
                        <feGaussianBlur in="SourceGraphic" stdDeviation="2" result="blur1"/>
                        <feGaussianBlur in="SourceGraphic" stdDeviation="4" result="blur2"/>
                        <feMerge>
                            <feMergeNode in="blur2"/>
                            <feMergeNode in="blur1"/>
                            <feMergeNode in="SourceGraphic"/>
                        </feMerge>
                    </filter>
                </defs>
                <g transform="scale(3)" stroke="url(#neonGrad{id})" stroke-width="2.5" filter="url(#neonGlow{id})" fill="none">
                    <circle cx="12" cy="12" r="5"/>
                    <path d="M12 1v1m0 18v1m11-11h-1M2 12H1m17.66-6.66l-.71.71M5.05 18.95l-.71.71m13.31 0l-.71-.71M5.05 5.05l-.71-.71"/>
                </g>
            </svg>''',

    'default': '''<svg viewBox="0 0 72 72" fill="none" xmlns="http://www.w3.org/2000/svg" width="48" height="48">
                <defs>
                    <linearGradient id="neonGrad{id}" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:{color1}"/>
                        <stop offset="100%" style="stop-color:{color2}"/>
                    </linearGradient>
                    <filter id="neonGlow{id}">
                        <feGaussianBlur in="SourceGraphic" stdDeviation="2" result="blur1"/>
                        <feGaussianBlur in="SourceGraphic" stdDeviation="4" result="blur2"/>
                        <feMerge>
                            <feMergeNode in="blur2"/>
                            <feMergeNode in="blur1"/>
                            <feMergeNode in="SourceGraphic"/>
                        </feMerge>
                    </filter>
                </defs>
                <g transform="scale(3)" stroke="url(#neonGrad{id})" stroke-width="2.5" filter="url(#neonGlow{id})" fill="none">
                    <circle cx="12" cy="12" r="8"/>
                    <path d="M12 8v8m-4-4h8"/>
                </g>
            </svg>'''
}

def fix_guide_icons(file_path, config):
    """Corrige les icônes dans un fichier de guide."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Trouver toutes les icônes et les remplacer une par une avec des IDs uniques
        icon_count = 0

        # Pattern pour trouver les div avec background gradient
        pattern = r'<div class="tool-logo-large" style="background: linear-gradient\(135deg, [^"]+\); font-size: var\(--text-lg\);">\s*<svg[^>]*>.*?</svg>\s*</div>'

        def replace_icon(match):
            nonlocal icon_count
            icon_count += 1

            # Déterminer le type d'icône basé sur le contenu
            icon_content = match.group(0)
            if 'M2 3h6a4 4 0 0 1 4 4v14' in icon_content:
                template = ICON_TEMPLATES['book']
            elif 'M21 15a2 2 0 0 1-2 2H7l-4 4V5' in icon_content:
                template = ICON_TEMPLATES['chat']
            elif 'M12 1v1m0 18v1m11-11h-1M2 12H1' in icon_content:
                template = ICON_TEMPLATES['lightbulb']
            else:
                template = ICON_TEMPLATES['default']

            # Remplacer les placeholders
            icon_html = template.format(
                id=f"{config['id']}{icon_count}",
                color1=config['color1'],
                color2=config['color2']
            )

            return f'<div class="tool-logo-large" style="background: rgba({config["rgb"]}, 0.1); border: 2px solid rgba({config["rgb"]}, 0.3);">\n                            {icon_html}\n                        </div>'

        content = re.sub(pattern, replace_icon, content, flags=re.DOTALL)

        # Écrire seulement si changé
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, icon_count
        return False, 0

    except Exception as e:
        print(f"Erreur avec {file_path}: {e}")
        return False, 0

def main():
    """Corrige les icônes dans les 3 pages de guides."""
    base_dir = Path('/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/categories')

    files_config = [
        {
            'file': base_dir / 'guides-beginner.html',
            'id': 'Beg',
            'color1': '#22C55E',
            'color2': '#10B981',
            'rgb': '34, 197, 94'
        },
        {
            'file': base_dir / 'guides-intermediate.html',
            'id': 'Int',
            'color1': '#3B82F6',
            'color2': '#2563EB',
            'rgb': '59, 130, 246'
        },
        {
            'file': base_dir / 'guides-advanced.html',
            'id': 'Adv',
            'color1': '#A855F7',
            'color2': '#7C3AED',
            'rgb': '168, 85, 247'
        }
    ]

    print("🔧 Correction des icônes néon...\n")

    total_icons = 0

    for config in files_config:
        file_path = config['file']
        if file_path.exists():
            updated, count = fix_guide_icons(file_path, config)
            if updated:
                total_icons += count
                print(f"✅ {file_path.name} - {count} icônes corrigées")
            else:
                print(f"⚠️  {file_path.name} - Aucun changement")
        else:
            print(f"❌ {file_path.name} - Fichier non trouvé")

    print(f"\n🎉 Terminé! {total_icons} icônes transformées en néon!")
    print("✨ Toutes les icônes sont maintenant parfaitement en néon!")

if __name__ == '__main__':
    main()
