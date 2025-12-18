#!/usr/bin/env python3
"""
Script pour remplacer tous les emojis par des icônes SVG high-tech professionnelles
et ajouter une nouvelle police moderne pour l'IA (Space Grotesk).
"""

import os
import re
from pathlib import Path

# Mapping des emojis vers des icônes SVG high-tech
EMOJI_TO_ICON = {
    '📑': '<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>',
    '👋': '<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7 13l5 5 5-5M7 6l5 5 5-5"/></svg>',
    '🤔': '<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>',
    '🚀': '<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5M2 12l10 5 10-5"/></svg>',
    '🛠️': '<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z"/></svg>',
    '❌': '<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="15" y1="9" x2="9" y2="15"/><line x1="9" y1="9" x2="15" y2="15"/></svg>',
    '✅': '<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 11-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>',
    '💼': '<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 00-2-2h-4a2 2 0 00-2 2v16"/></svg>',
    '🎁': '<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 12 20 22 4 22 4 12"/><rect x="2" y="7" width="20" height="5"/><line x1="12" y1="22" x2="12" y2="7"/><path d="M12 7H7.5a2.5 2.5 0 010-5C11 2 12 7 12 7z"/><path d="M12 7h4.5a2.5 2.5 0 000-5C13 2 12 7 12 7z"/></svg>',
    '⚠️': '<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>',
    '🎯': '<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>',
    '🔥': '<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2s-4 4.5-4 8a4 4 0 008 0c0-3.5-4-8-4-8z"/><path d="M8.5 8.5S10 6 12 6s3.5 2.5 3.5 2.5"/></svg>',
    '💡': '<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18h6"/><path d="M10 22h4"/><path d="M15.09 14c.18-.98.65-1.74 1.41-2.5A4.65 4.65 0 0018 8a6 6 0 10-12 0c0 1.33.47 2.48 1.5 3.5.76.76 1.23 1.52 1.41 2.5"/></svg>',
    '⭐': '<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>',
    '🎨': '<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a10 10 0 017.38 16.75 2 2 0 01-3.5.54l-.9-1.34a2 2 0 00-1.65-.88H9.87a2 2 0 01-1.99-2.33L8.53 12a2 2 0 00-.26-1.5L6.8 8.53a10 10 0 015.2-6.53z"/><circle cx="7.5" cy="10.5" r=".5"/><circle cx="18.5" cy="7.5" r=".5"/><circle cx="16.5" cy="13.5" r=".5"/></svg>',
    '🔧': '<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z"/></svg>',
    '📊': '<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>',
    '💰': '<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"/></svg>',
    '🌟': '<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>',
    '✨': '<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>',
    '🎮': '<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="6" y1="12" x2="10" y2="12"/><line x1="8" y1="10" x2="8" y2="14"/><line x1="15" y1="13" x2="15.01" y2="13"/><line x1="18" y1="11" x2="18.01" y2="11"/><rect x="2" y="6" width="20" height="12" rx="2"/></svg>',
    '🖥️': '<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>',
    '📱': '<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="5" y="2" width="14" height="20" rx="2" ry="2"/><line x1="12" y1="18" x2="12.01" y2="18"/></svg>',
    '⚡': '<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>',
    '🔒': '<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0110 0v4"/></svg>',
    '🌐': '<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 014 10 15.3 15.3 0 01-4 10 15.3 15.3 0 01-4-10 15.3 15.3 0 014-10z"/></svg>',
    '📈': '<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/></svg>',
    '🎵': '<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/></svg>',
    '🎬': '<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="2.18" ry="2.18"/><line x1="7" y1="2" x2="7" y2="22"/><line x1="17" y1="2" x2="17" y2="22"/><line x1="2" y1="12" x2="22" y2="12"/><line x1="2" y1="7" x2="7" y2="7"/><line x1="2" y1="17" x2="7" y2="17"/><line x1="17" y1="17" x2="22" y2="17"/><line x1="17" y1="7" x2="22" y2="7"/></svg>',
    '📸': '<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M23 19a2 2 0 01-2 2H3a2 2 0 01-2-2V8a2 2 0 012-2h4l2-3h6l2 3h4a2 2 0 012 2z"/><circle cx="12" cy="13" r="4"/></svg>',
}

# Style CSS pour les icônes inline
ICON_STYLE = """
        .inline-icon {
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
        }

        h2 .inline-icon {
            width: 1.5em;
            height: 1.5em;
            stroke: url(#icon-gradient);
        }

        /* Gradient pour les icônes dans les titres */
        .icon-gradient-def {
            position: absolute;
            width: 0;
            height: 0;
        }
"""

# Définition du gradient SVG
SVG_GRADIENT_DEF = """
        <svg class="icon-gradient-def" aria-hidden="true">
            <defs>
                <linearGradient id="icon-gradient" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" style="stop-color:#00D9FF;stop-opacity:1" />
                    <stop offset="100%" style="stop-color:#A855F7;stop-opacity:1" />
                </linearGradient>
            </defs>
        </svg>
"""

# Nouvelle police Google Fonts pour AI (Space Grotesk - moderne et tech)
FONT_IMPORT = 'https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap'

def replace_emojis_in_file(file_path):
    """Remplace tous les emojis par des icônes SVG dans un fichier."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Remplacer chaque emoji par son icône SVG
        for emoji, icon in EMOJI_TO_ICON.items():
            content = content.replace(emoji, icon)

        # Ajouter le style pour les icônes si nécessaire
        if '<style>' in content and '.inline-icon' not in content:
            content = content.replace('<style>', f'<style>\n{ICON_STYLE}')

        # Ajouter le gradient SVG avant </body> si nécessaire
        if '</body>' in content and 'icon-gradient-def' not in content:
            content = content.replace('</body>', f'{SVG_GRADIENT_DEF}\n    </body>')

        # Mettre à jour la police Google Fonts
        if 'fonts.googleapis.com' in content:
            # Trouver et remplacer l'import de police existant
            font_pattern = r'<link href="https://fonts\.googleapis\.com/css2\?[^"]*" rel="stylesheet">'
            if re.search(font_pattern, content):
                new_font_link = f'<link href="{FONT_IMPORT}" rel="stylesheet">'
                content = re.sub(font_pattern, new_font_link, content)

        # Ajouter Space Grotesk comme police principale pour les guides/reviews
        if 'guide-section' in content or 'review-content' in content:
            # Ajouter ou mettre à jour la police de la famille
            if 'font-family: var(--font-sans)' in content:
                content = content.replace(
                    'font-family: var(--font-sans)',
                    "font-family: 'Space Grotesk', var(--font-sans)"
                )

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
    """Parcourt tous les fichiers HTML et remplace les emojis."""
    base_dir = Path('/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai')

    # Dossiers à traiter
    target_dirs = [
        base_dir / 'pages' / 'guides',
        base_dir / 'pages' / 'reviews',
    ]

    files_modified = 0
    files_processed = 0

    print("🔄 Remplacement des emojis par des icônes SVG high-tech...")
    print("📝 Ajout de la police Space Grotesk pour un look moderne AI...\n")

    for target_dir in target_dirs:
        if not target_dir.exists():
            continue

        # Parcourir récursivement tous les fichiers HTML
        for html_file in target_dir.rglob('*.html'):
            files_processed += 1
            if replace_emojis_in_file(html_file):
                files_modified += 1
                print(f"✓ Modifié: {html_file.relative_to(base_dir)}")

    print(f"\n✅ Terminé!")
    print(f"📊 Fichiers traités: {files_processed}")
    print(f"📝 Fichiers modifiés: {files_modified}")

    print("\n🎨 Police principale pour AI: Space Grotesk")
    print("💡 Tous les emojis ont été remplacés par des icônes SVG professionnelles")

if __name__ == '__main__':
    main()
