#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de correction des balises canonical pour les versions multilingues
Corrige les canonical pour qu'elles soient auto-référencées au lieu de pointer vers l'anglais
"""

import os
import re
import sys

def fix_canonical(file_path, lang):
    """Corrige la balise canonical d'un fichier HTML"""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern pour trouver la balise canonical
    canonical_pattern = r'<link rel="canonical" href="https://techvernia\.com/pages/([^"]+)" />'

    def replace_canonical(match):
        path = match.group(1)
        # Remplacer par la version avec la langue
        return f'<link rel="canonical" href="https://techvernia.com/{lang}/pages/{path}" />'

    # Remplacer le canonical
    new_content = re.sub(canonical_pattern, replace_canonical, content)

    # Vérifier si quelque chose a changé
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True

    return False


def fix_language_canonicals(lang, base_dir):
    """Corrige tous les canonicals pour une langue"""
    print(f"\n=== Correction des canonicals pour {lang} ===\n")

    lang_dir = os.path.join(base_dir, 'docs', lang)

    if not os.path.exists(lang_dir):
        print(f"Le dossier {lang_dir} n'existe pas")
        return

    count = 0

    # Parcourir tous les fichiers HTML
    for root, dirs, files in os.walk(lang_dir):
        # Ignorer certains dossiers
        dirs[:] = [d for d in dirs if d not in ['js', 'css', 'assets']]

        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)

                if fix_canonical(file_path, lang):
                    count += 1
                    print(f"[OK] {file_path}")

    print(f"\n[OK] {count} fichiers corriges pour {lang}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python fix_canonicals.py [langue]")
        print("Langues disponibles: fr, ar, es, de, pt, zh, ja, ko, hi, all")
        print("Exemple: python fix_canonicals.py ar")
        print("Exemple: python fix_canonicals.py all")
        sys.exit(1)

    lang = sys.argv[1]
    base_dir = os.path.dirname(os.path.abspath(__file__))

    languages = ['fr', 'ar', 'es', 'de', 'pt', 'zh', 'ja', 'ko', 'hi']

    if lang == 'all':
        for l in languages:
            fix_language_canonicals(l, base_dir)
    elif lang in languages:
        fix_language_canonicals(lang, base_dir)
    else:
        print(f"Langue non supportée: {lang}")
        print(f"Langues disponibles: {', '.join(languages)}")
        sys.exit(1)

    print("\n[OK] Correction terminee!")


if __name__ == '__main__':
    main()
