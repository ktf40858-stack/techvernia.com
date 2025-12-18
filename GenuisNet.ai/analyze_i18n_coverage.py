#!/usr/bin/env python3
"""
Script d'analyse de couverture i18n
Étape 3: Identifier tous les textes HTML qui nécessitent data-i18n
"""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup
import json

PROJECT_ROOT = "/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai"

# Éléments HTML qui contiennent généralement du texte à traduire
TEXT_ELEMENTS = [
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
    'p', 'span', 'a', 'button', 'label',
    'li', 'td', 'th', 'div', 'strong', 'em',
    'blockquote', 'figcaption', 'legend'
]

# Attributs à vérifier pour les traductions
TEXT_ATTRIBUTES = ['placeholder', 'title', 'alt', 'aria-label']

# Textes à ignorer (génériques, techniques, etc.)
IGNORE_PATTERNS = [
    r'^\s*$',  # Texte vide
    r'^[\d\s\+\-\(\)]+$',  # Seulement chiffres et symboles
    r'^[©®™]+$',  # Symboles de copyright
    r'^\w+\.(jpg|png|svg|gif|webp)$',  # Noms de fichiers images
    r'^https?://',  # URLs
    r'^[\d\.]+%?$',  # Pourcentages ou nombres
    r'^\d{4}$',  # Années
]

def should_ignore_text(text):
    """Vérifier si un texte doit être ignoré"""
    if not text or not text.strip():
        return True

    text = text.strip()

    for pattern in IGNORE_PATTERNS:
        if re.match(pattern, text):
            return True

    # Ignorer les textes très courts (1-2 caractères) sauf s'ils sont significatifs
    if len(text) <= 2 and text not in ['AI', 'vs', 'or', 'en', 'fr', 'de']:
        return True

    return False

def find_html_files():
    """Trouver tous les fichiers HTML dans le projet"""
    html_files = []

    # Pages principales
    for file in Path(PROJECT_ROOT).glob('*.html'):
        html_files.append(str(file))

    # Sous-répertoires
    for subdir in ['pages', 'pages/categories', 'pages/reviews']:
        dir_path = Path(PROJECT_ROOT) / subdir
        if dir_path.exists():
            for file in dir_path.rglob('*.html'):
                html_files.append(str(file))

    return sorted(html_files)

def analyze_html_file(file_path):
    """Analyser un fichier HTML pour trouver les textes non traduits"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return {
            'error': str(e),
            'untranslated_elements': [],
            'untranslated_attributes': [],
            'total_text_elements': 0,
            'total_with_i18n': 0
        }

    soup = BeautifulSoup(content, 'html.parser')

    untranslated_elements = []
    untranslated_attributes = []
    total_text_elements = 0
    total_with_i18n = 0

    # Analyser les éléments de texte
    for tag_name in TEXT_ELEMENTS:
        for element in soup.find_all(tag_name):
            # Obtenir le texte direct (pas les enfants)
            text = element.get_text(strip=True)

            if should_ignore_text(text):
                continue

            total_text_elements += 1

            # Vérifier si l'élément ou un parent a data-i18n
            has_i18n = False
            current = element

            while current and not has_i18n:
                if current.get('data-i18n'):
                    has_i18n = True
                    total_with_i18n += 1
                    break
                current = current.parent if hasattr(current, 'parent') else None

            if not has_i18n and text:
                # Obtenir le contexte (chemin HTML)
                path_parts = []
                current = element
                while current and current.name:
                    class_str = '.'.join(current.get('class', []))
                    id_str = f"#{current.get('id')}" if current.get('id') else ''
                    tag_info = f"{current.name}{class_str}{id_str}"
                    path_parts.insert(0, tag_info)
                    current = current.parent if hasattr(current, 'parent') else None
                    if len(path_parts) > 5:  # Limiter la profondeur
                        break

                path = ' > '.join(path_parts[-5:])

                untranslated_elements.append({
                    'tag': tag_name,
                    'text': text[:100] + ('...' if len(text) > 100 else ''),
                    'path': path,
                    'line': content[:content.find(str(element))].count('\n') + 1 if str(element) in content else 0
                })

    # Analyser les attributs
    for attr_name in TEXT_ATTRIBUTES:
        for element in soup.find_all(attrs={attr_name: True}):
            attr_value = element.get(attr_name, '')

            if should_ignore_text(attr_value):
                continue

            # Vérifier si l'attribut de traduction existe
            i18n_attr = f'data-i18n-{attr_name}'
            if not element.get(i18n_attr):
                untranslated_attributes.append({
                    'tag': element.name,
                    'attribute': attr_name,
                    'value': attr_value[:100] + ('...' if len(attr_value) > 100 else ''),
                    'line': content[:content.find(str(element))].count('\n') + 1 if str(element) in content else 0
                })

    coverage = (total_with_i18n / total_text_elements * 100) if total_text_elements > 0 else 0

    return {
        'untranslated_elements': untranslated_elements,
        'untranslated_attributes': untranslated_attributes,
        'total_text_elements': total_text_elements,
        'total_with_i18n': total_with_i18n,
        'coverage': round(coverage, 2)
    }

def main():
    """Fonction principale"""
    print("\n" + "="*70)
    print("🔍 ANALYSE DE COUVERTURE i18n")
    print("="*70 + "\n")

    print("Recherche des fichiers HTML...")
    html_files = find_html_files()
    print(f"✅ {len(html_files)} fichiers HTML trouvés\n")

    results = {}
    total_untranslated = 0
    total_elements = 0
    total_with_i18n = 0

    print("Analyse en cours...")
    for i, file_path in enumerate(html_files, 1):
        relative_path = file_path.replace(PROJECT_ROOT + '/', '')
        print(f"  [{i}/{len(html_files)}] {relative_path}...", end='\r')

        result = analyze_html_file(file_path)
        results[relative_path] = result

        total_untranslated += len(result.get('untranslated_elements', []))
        total_elements += result.get('total_text_elements', 0)
        total_with_i18n += result.get('total_with_i18n', 0)

    print("\n\n" + "="*70)
    print("📊 RÉSULTATS DE L'ANALYSE")
    print("="*70 + "\n")

    global_coverage = (total_with_i18n / total_elements * 100) if total_elements > 0 else 0

    print(f"Fichiers analysés: {len(html_files)}")
    print(f"Total d'éléments de texte: {total_elements}")
    print(f"Éléments avec data-i18n: {total_with_i18n}")
    print(f"Éléments sans data-i18n: {total_untranslated}")
    print(f"Couverture globale: {global_coverage:.1f}%\n")

    # Trier par nombre d'éléments non traduits
    sorted_files = sorted(
        results.items(),
        key=lambda x: len(x[1].get('untranslated_elements', [])),
        reverse=True
    )

    print("="*70)
    print("📄 FICHIERS NÉCESSITANT LE PLUS D'ATTENTION")
    print("="*70 + "\n")

    for file_path, result in sorted_files[:20]:
        untranslated = len(result.get('untranslated_elements', []))
        untranslated_attrs = len(result.get('untranslated_attributes', []))
        coverage = result.get('coverage', 0)

        if untranslated > 0 or untranslated_attrs > 0:
            status = "🔴" if coverage < 50 else "🟡" if coverage < 80 else "🟢"
            print(f"{status} {file_path}")
            print(f"   Couverture: {coverage:.1f}% | "
                  f"Éléments non traduits: {untranslated} | "
                  f"Attributs non traduits: {untranslated_attrs}")

            # Afficher quelques exemples
            if result.get('untranslated_elements'):
                print(f"   Exemples:")
                for elem in result['untranslated_elements'][:3]:
                    print(f"     - <{elem['tag']}> ligne {elem['line']}: \"{elem['text']}\"")
            print()

    # Sauvegarder le rapport détaillé
    report_file = os.path.join(PROJECT_ROOT, 'i18n_coverage_report.json')
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump({
            'summary': {
                'total_files': len(html_files),
                'total_elements': total_elements,
                'total_with_i18n': total_with_i18n,
                'total_untranslated': total_untranslated,
                'global_coverage': round(global_coverage, 2)
            },
            'files': results
        }, f, indent=2, ensure_ascii=False)

    print("="*70)
    print(f"✅ Rapport détaillé sauvegardé: i18n_coverage_report.json")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()
