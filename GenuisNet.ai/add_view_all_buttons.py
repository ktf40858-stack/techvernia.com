#!/usr/bin/env python3
"""
Ajoute des boutons "View All" aux sections Beginner, Intermediate et Advanced
"""

import re
from pathlib import Path

def main():
    """Ajoute les boutons View All."""
    file_path = Path('/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/guides.html')

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pour chaque section, ajouter un bouton "View All" après le h2
    sections = {
        'Beginner Guides': ('beginner', '#22C55E'),
        'Intermediate Guides': ('intermediate', '#3B82F6'),
        'Advanced Guides': ('advanced', '#A855F7')
    }

    for title, (level, color) in sections.items():
        # Trouver la section divider avec ce titre
        pattern = rf'(<h2>{title}</h2>\s*</div>)'

        button_html = f'''</div>
                <a href="../categories/guides-{level}.html" target="_blank" class="btn btn-outline" style="border-color: {color}; color: {color}; margin-top: var(--space-md);">
                    View All {title.split()[0]} Guides
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width: 16px; height: 16px; display: inline-block; vertical-align: middle; margin-left: 6px;">
                        <path d="M5 12h14M12 5l7 7-7 7"/>
                    </svg>
                </a>'''

        content = re.sub(pattern, button_html, content)

    # Écrire le fichier
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ Boutons 'View All' ajoutés aux 3 sections")
    print("\n🎉 Les utilisateurs peuvent maintenant cliquer pour voir tous les guides!")

if __name__ == '__main__':
    main()
