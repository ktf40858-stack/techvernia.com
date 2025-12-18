#!/usr/bin/env python3
"""
Corrige les en-têtes de sections et ajoute les h2 manquants
"""

from pathlib import Path

def main():
    """Corrige les en-têtes."""
    file_path = Path('/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/guides.html')

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remplacer les divs fermantes suivies des boutons View All par h2 + bouton
    replacements = [
        (
            '</div>\n                <a href="../categories/guides-beginner.html" target="_blank"',
            '<h2>Beginner Guides</h2>\n                </div>\n                <a href="../categories/guides-beginner.html" target="_blank"'
        ),
        (
            '</div>\n                <a href="../categories/guides-intermediate.html" target="_blank"',
            '<h2>Intermediate Guides</h2>\n                </div>\n                <a href="../categories/guides-intermediate.html" target="_blank"'
        ),
        (
            '</div>\n                <a href="../categories/guides-advanced.html" target="_blank"',
            '<h2>Advanced Guides</h2>\n                </div>\n                <a href="../categories/guides-advanced.html" target="_blank"'
        )
    ]

    for old, new in replacements:
        content = content.replace(old, new)

    # Écrire le fichier
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ En-têtes de sections corrigés")
    print("✅ Les titres h2 sont maintenant présents")

if __name__ == '__main__':
    main()
