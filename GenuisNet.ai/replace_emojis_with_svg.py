#!/usr/bin/env python3
"""
Remplacer tous les emojis par des icônes SVG néon cohérentes avec le style du site
"""

import os
import re
from bs4 import BeautifulSoup
from pathlib import Path

# Bibliothèque d'icônes SVG néon
SVG_ICONS = {
    # Emojis courants
    '🤖': '''<svg class="neon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="10" rx="2"/><circle cx="8" cy="15" r="1"/><circle cx="16" cy="15" r="1"/><path d="M9 7L9 9M15 7L15 9M12 2v5"/></svg>''',

    '🎙️': '''<svg class="neon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/><line x1="8" y1="23" x2="16" y2="23"/></svg>''',

    '🎤': '''<svg class="neon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/><line x1="8" y1="23" x2="16" y2="23"/></svg>''',

    '📊': '''<svg class="neon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>''',

    '💬': '''<svg class="neon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>''',

    '💻': '''<svg class="neon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>''',

    '🎨': '''<svg class="neon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a10 10 0 0 0 0 20 2.5 2.5 0 0 0 2.5-2.5c0-.654-.253-1.248-.656-1.688a.75.75 0 0 1 .656-1.312h1.5A6 6 0 0 0 22 10a10 10 0 0 0-10-8z"/><circle cx="7.5" cy="10.5" r="1.5"/><circle cx="10" cy="7.5" r="1.5"/><circle cx="14" cy="7.5" r="1.5"/><circle cx="16.5" cy="10.5" r="1.5"/></svg>''',

    '✍️': '''<svg class="neon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"/></svg>''',

    '✏️': '''<svg class="neon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"/></svg>''',

    '🖼️': '''<svg class="neon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>''',

    '🎬': '''<svg class="neon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="2.18" ry="2.18"/><line x1="7" y1="2" x2="7" y2="22"/><line x1="17" y1="2" x2="17" y2="22"/><line x1="2" y1="12" x2="22" y2="12"/><line x1="2" y1="7" x2="7" y2="7"/><line x1="2" y1="17" x2="7" y2="17"/><line x1="17" y1="17" x2="22" y2="17"/><line x1="17" y1="7" x2="22" y2="7"/></svg>''',

    '🎮': '''<svg class="neon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 12h4M8 10v4M15 11h.01M18 13h.01M18 6a4 4 0 0 1 4 4 7 7 0 0 1-7 7h-2a7 7 0 0 1-7-7 4 4 0 0 1 4-4z"/></svg>''',

    '🎓': '''<svg class="neon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>''',

    '🎵': '''<svg class="neon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/></svg>''',

    '👥': '''<svg class="neon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>''',

    '⚖️': '''<svg class="neon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/><line x1="4" y1="22" x2="4" y2="15"/></svg>''',

    '⚛️': '''<svg class="neon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="1"/><path d="M20.2 20.2c2.04-2.03.02-7.36-4.5-11.9-4.54-4.52-9.87-6.54-11.9-4.5-2.04 2.03-.02 7.36 4.5 11.9 4.54 4.52 9.87 6.54 11.9 4.5z"/><path d="M15.7 15.7c4.52-4.54 6.54-9.87 4.5-11.9-2.03-2.04-7.36-.02-11.9 4.5-4.52 4.54-6.54 9.87-4.5 11.9 2.03 2.04 7.36.02 11.9-4.5z"/></svg>''',

    '🔬': '''<svg class="neon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 3v9l-6 6a3 3 0 1 0 4.24 4.24L13 16.5V3"/><path d="M9 3h6v6"/><path d="M11 19.5L18.5 12"/></svg>''',

    '💼': '''<svg class="neon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>''',

    '🌐': '''<svg class="neon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>''',

    '🔍': '''<svg class="neon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>''',

    '⚡': '''<svg class="neon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>''',

    '🛡️': '''<svg class="neon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>''',

    '🎧': '''<svg class="neon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 18v-6a9 9 0 0 1 18 0v6"/><path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3zM3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3z"/></svg>''',

    '🏗️': '''<svg class="neon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 21h18"/><path d="M9 8h10"/><path d="M9 14h10"/><path d="M9 20h10"/><path d="M3 8l3-3 3 3"/></svg>''',

    '🏥': '''<svg class="neon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2L2 7v10c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V7l-10-5z"/><line x1="12" y1="8" x2="12" y2="16"/><line x1="8" y1="12" x2="16" y2="12"/></svg>''',

    '📣': '''<svg class="neon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 11l18-5v12L3 13v-2z"/><path d="M11.6 16.8a3 3 0 1 1-5.8-1.6"/></svg>''',

    '📋': '''<svg class="neon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1" ry="1"/></svg>''',

    '📅': '''<svg class="neon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>''',

    '⭐': '''<svg class="neon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>''',

    '🏆': '''<svg class="neon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"/><path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"/><path d="M4 22h16"/><path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22"/><path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22"/><path d="M18 2H6v7a6 6 0 0 0 12 0V2z"/></svg>''',

    '💡': '''<svg class="neon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/></svg>''',

    '❓': '''<svg class="neon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>''',

    '✅': '''<svg class="neon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>''',

    '⚙️': '''<svg class="neon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M12 1v6m0 6v6m5.66-16.35l-3.87 3.88m-3.78 3.79l-3.87 3.88m13.52 0l-3.87-3.88m-3.78-3.79l-3.87-3.88"/></svg>''',
}

def create_svg_css():
    """Créer le CSS pour les icônes SVG néon"""
    css = '''
/* Icônes SVG Néon */
.neon-icon {
    display: inline-block;
    width: 1.2em;
    height: 1.2em;
    vertical-align: middle;
    margin-right: 0.3em;
    stroke: currentColor;
    stroke-width: 2;
    fill: none;
    stroke-linecap: round;
    stroke-linejoin: round;
    filter: drop-shadow(0 0 3px currentColor);
    transition: all 0.3s ease;
}

.neon-icon:hover {
    filter: drop-shadow(0 0 8px currentColor);
}

/* Icônes dans les titres */
h1 .neon-icon, h2 .neon-icon, h3 .neon-icon {
    width: 1.5em;
    height: 1.5em;
    margin-right: 0.5em;
}

/* Icônes dans les badges */
.hero-badge .neon-icon,
.badge .neon-icon {
    width: 1em;
    height: 1em;
    margin-right: 0.25em;
}
'''
    return css

def replace_emojis_in_content(content):
    """Remplacer les emojis par des SVG dans le contenu HTML"""

    for emoji, svg in SVG_ICONS.items():
        # Remplacer l'emoji par le SVG
        content = content.replace(emoji, svg)

    return content

def process_file(file_path):
    """Traiter un fichier HTML"""

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remplacer les emojis
        updated_content = replace_emojis_in_content(content)

        # Vérifier si le fichier a changé
        if updated_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            return True

        return False

    except Exception as e:
        print(f"   ❌ Erreur: {e}")
        return False

def main():
    print("="*70)
    print("🎨 REMPLACEMENT DES EMOJIS PAR DES ICÔNES SVG NÉON")
    print("="*70)
    print()

    # 1. Créer le fichier CSS pour les icônes
    print("📝 Création du CSS pour les icônes SVG...")
    css_content = create_svg_css()

    css_file = 'css/neon-icons.css'
    with open(css_file, 'w', encoding='utf-8') as f:
        f.write(css_content)
    print(f"   ✅ {css_file} créé")
    print()

    # 2. Traiter tous les fichiers HTML
    print("🔄 Traitement des fichiers HTML...")
    print("-"*70)

    total_updated = 0

    # Fichiers à traiter
    files_to_process = []

    # Page d'accueil
    files_to_process.append('index.html')

    # Pages de catégories
    for file in os.listdir('pages/categories'):
        if file.endswith('.html'):
            files_to_process.append(f'pages/categories/{file}')

    # Pages de reviews
    for category in os.listdir('pages/reviews'):
        category_path = f'pages/reviews/{category}'
        if os.path.isdir(category_path):
            for file in os.listdir(category_path):
                if file.endswith('.html'):
                    files_to_process.append(f'{category_path}/{file}')

    # Pages autres
    for file in ['pages/about.html', 'pages/guides.html', 'pages/categories.html']:
        if os.path.exists(file):
            files_to_process.append(file)

    print(f"📁 Fichiers à traiter: {len(files_to_process)}")
    print()

    for file_path in files_to_process:
        if process_file(file_path):
            print(f"✅ {file_path}")
            total_updated += 1

    print()
    print("="*70)
    print(f"✅ REMPLACEMENT TERMINÉ!")
    print(f"   Fichiers mis à jour: {total_updated}/{len(files_to_process)}")
    print(f"   Emojis remplacés par {len(SVG_ICONS)} types d'icônes SVG néon")
    print("="*70)
    print()
    print("⚠️  N'oubliez pas d'ajouter le lien CSS dans vos pages:")
    print('   <link rel="stylesheet" href="css/neon-icons.css">')

if __name__ == '__main__':
    main()
