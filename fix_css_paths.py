#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour corriger les chemins CSS dans les pages multilingues
Corrige les chemins relatifs incorrects qui empêchent le chargement du CSS
"""

import os
import re
import sys

def fix_css_paths_in_file(file_path, lang):
    """Corrige les chemins CSS d'un fichier HTML"""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Patterns à corriger dans les pages de catégories/sous-dossiers
    # Ces pages sont à 3 niveaux de profondeur: docs/LANG/pages/categories/

    # Remplacer ../../css/ par ../../../css/ (pour pages dans sous-dossiers)
    # Mais seulement si le fichier est dans un sous-dossier (categories/, blog/, etc.)

    # Déterminer la profondeur
    relative_path = file_path.replace('\\', '/')

    # Compter les niveaux depuis docs/LANG/
    if f'/docs/{lang}/pages/' in relative_path:
        # Compter combien de / après /pages/
        parts_after_pages = relative_path.split(f'/docs/{lang}/pages/')[1]
        depth = parts_after_pages.count('/') + 1  # +1 pour le fichier lui-même

        # Si c'est dans un sous-dossier (depth > 1), on a besoin de 3 niveaux
        if depth > 1:
            # Corriger les chemins CSS
            content = content.replace('href="../../css/', 'href="../../../css/')
            content = content.replace('href="../css/', 'href="../../css/')

            # Aussi corriger les chemins dans les inline styles si présents
            # (moins probable mais par précaution)

    # Sauvegarder si modifié
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False


def fix_language_css_paths(lang, base_dir):
    """Corrige tous les chemins CSS pour une langue"""
    print(f"\n=== Correction des chemins CSS pour {lang} ===\n")

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

                if fix_css_paths_in_file(file_path, lang):
                    count += 1
                    print(f"[OK] {file_path}")

    print(f"\n[OK] {count} fichiers corriges pour {lang}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python fix_css_paths.py [langue]")
        print("Langues disponibles: fr, ar, es, de, pt, zh, ja, ko, hi, all")
        print("Exemple: python fix_css_paths.py ar")
        print("Exemple: python fix_css_paths.py all")
        sys.exit(1)

    lang = sys.argv[1]
    base_dir = os.path.dirname(os.path.abspath(__file__))

    languages = ['fr', 'ar', 'es', 'de', 'pt', 'zh', 'ja', 'ko', 'hi']

    if lang == 'all':
        for l in languages:
            fix_language_css_paths(l, base_dir)
    elif lang in languages:
        fix_language_css_paths(lang, base_dir)
    else:
        print(f"Langue non supportée: {lang}")
        print(f"Langues disponibles: {', '.join(languages)}")
        sys.exit(1)

    print("\n[OK] Correction terminee!")


if __name__ == '__main__':
    main()
