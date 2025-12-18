#!/usr/bin/env python3
"""
Script Semi-Automatisé d'Ajout i18n
Phase 1: Pages Principales

Ce script analyse une page HTML et suggère l'ajout de data-i18n de manière intelligente.
"""

import re
import json
import os
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString
import argparse

PROJECT_ROOT = "/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai"
I18N_FILE = os.path.join(PROJECT_ROOT, "js/i18n.js")

# Patterns de contexte pour générer des clés logiques
CONTEXT_PATTERNS = {
    'nav': ['nav', 'navbar', 'navigation', 'menu'],
    'hero': ['hero', 'jumbotron', 'banner'],
    'footer': ['footer'],
    'section': ['section'],
    'card': ['card', 'tool-card'],
    'btn': ['button', 'btn', 'cta'],
    'form': ['form', 'input-group'],
    'modal': ['modal'],
    'contact': ['contact'],
    'about': ['about'],
    'guide': ['guide'],
    'blog': ['blog'],
}

# Textes à ignorer
IGNORE_PATTERNS = [
    r'^\s*$',
    r'^[\d\s\+\-\(\)]+$',
    r'^[©®™]+$',
    r'^\w+\.(jpg|png|svg|gif|webp|css|js)$',
    r'^https?://',
    r'^[\d\.]+%?$',
    r'^\d{4}$',
    r'^[\.,:;!\?]+$',
]

def should_ignore_text(text):
    """Vérifier si un texte doit être ignoré"""
    if not text or not text.strip():
        return True

    text = text.strip()

    for pattern in IGNORE_PATTERNS:
        if re.match(pattern, text):
            return True

    if len(text) <= 2 and text not in ['AI', 'vs', 'or']:
        return True

    return False

def get_context_from_classes(element):
    """Extraire le contexte depuis les classes CSS"""
    classes = element.get('class', [])
    if isinstance(classes, str):
        classes = classes.split()

    all_classes = ' '.join(classes).lower()

    for context, patterns in CONTEXT_PATTERNS.items():
        for pattern in patterns:
            if pattern in all_classes:
                return context

    return None

def get_context_from_hierarchy(element):
    """Extraire le contexte depuis la hiérarchie HTML"""
    current = element
    while current and hasattr(current, 'parent'):
        context = get_context_from_classes(current)
        if context:
            return context
        current = current.parent
    return None

def generate_key_name(text, context, existing_keys):
    """Générer un nom de clé i18n logique"""
    # Nettoyer le texte pour créer une clé
    clean_text = text.lower()
    clean_text = re.sub(r'[^\w\s-]', '', clean_text)
    clean_text = re.sub(r'\s+', '-', clean_text)
    clean_text = clean_text[:30]  # Limiter la longueur

    # Créer la clé de base
    if context:
        base_key = f"{context}.{clean_text}"
    else:
        base_key = clean_text

    # Vérifier les doublons
    key = base_key
    counter = 2
    while key in existing_keys:
        key = f"{base_key}-{counter}"
        counter += 1

    return key

def load_existing_keys():
    """Charger les clés i18n existantes depuis i18n.js"""
    try:
        with open(I18N_FILE, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extraire les clés de la section en (English)
        pattern = r'en:\s*\{(.*?)\n    \},'
        match = re.search(pattern, content, re.DOTALL)

        if match:
            en_block = match.group(1)
            key_pattern = r'"([^"]+)":\s*"'
            keys = re.findall(key_pattern, en_block)
            return set(keys)
    except Exception as e:
        print(f"⚠️ Erreur lors du chargement de i18n.js: {e}")

    return set()

def analyze_page(html_file):
    """Analyser une page HTML et suggérer les ajouts i18n"""
    print(f"\n{'='*80}")
    print(f"🔍 Analyse: {html_file}")
    print(f"{'='*80}\n")

    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Erreur lecture fichier: {e}")
        return None

    soup = BeautifulSoup(content, 'html.parser')
    existing_keys = load_existing_keys()
    suggestions = []
    new_keys = {}

    # Éléments à analyser
    text_elements = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'span', 'a', 'button', 'label', 'li']

    for tag_name in text_elements:
        for element in soup.find_all(tag_name):
            # Vérifier si déjà traduit
            if element.get('data-i18n'):
                continue

            # Vérifier les parents pour data-i18n
            has_parent_i18n = False
            current = element.parent
            while current and hasattr(current, 'name'):
                if current.get('data-i18n'):
                    has_parent_i18n = True
                    break
                current = current.parent if hasattr(current, 'parent') else None

            if has_parent_i18n:
                continue

            # Extraire le texte
            # Pour les liens, prendre uniquement le texte direct, pas les enfants
            if tag_name == 'a':
                text_parts = []
                for child in element.children:
                    if isinstance(child, NavigableString):
                        text_parts.append(str(child).strip())
                    elif child.name == 'span' and child.get('data-i18n'):
                        # Si le span a déjà data-i18n, on skip
                        continue
                text = ' '.join(text_parts).strip()
            else:
                # Pour les autres éléments, obtenir le texte direct
                text = element.get_text(strip=True)

            if should_ignore_text(text):
                continue

            # Obtenir le contexte
            context = get_context_from_hierarchy(element)

            # Générer la clé
            key = generate_key_name(text, context, existing_keys | set(new_keys.keys()))

            # Ajouter à existing_keys pour éviter les doublons
            existing_keys.add(key)

            # Sauvegarder la suggestion
            suggestions.append({
                'element': element,
                'tag': tag_name,
                'text': text,
                'context': context or 'general',
                'key': key,
                'classes': ' '.join(element.get('class', [])),
                'id': element.get('id', ''),
            })

            new_keys[key] = text

    # Analyser les attributs (placeholder, title, alt, aria-label)
    attr_suggestions = []
    for attr_name in ['placeholder', 'title', 'alt', 'aria-label']:
        for element in soup.find_all(attrs={attr_name: True}):
            attr_value = element.get(attr_name, '').strip()

            if should_ignore_text(attr_value):
                continue

            # Vérifier si déjà traduit
            i18n_attr = f'data-i18n-{attr_name}'
            if element.get(i18n_attr):
                continue

            # Obtenir le contexte
            context = get_context_from_hierarchy(element)

            # Générer la clé
            key = generate_key_name(attr_value, context, existing_keys | set(new_keys.keys()))
            existing_keys.add(key)

            attr_suggestions.append({
                'element': element,
                'tag': element.name,
                'attribute': attr_name,
                'value': attr_value,
                'context': context or 'general',
                'key': key,
            })

            new_keys[key] = attr_value

    return {
        'file': html_file,
        'soup': soup,
        'content': content,
        'suggestions': suggestions,
        'attr_suggestions': attr_suggestions,
        'new_keys': new_keys
    }

def preview_suggestions(analysis):
    """Afficher un aperçu des suggestions"""
    if not analysis:
        return

    suggestions = analysis['suggestions']
    attr_suggestions = analysis['attr_suggestions']
    new_keys = analysis['new_keys']

    print(f"📊 Résumé:")
    print(f"   - {len(suggestions)} éléments de texte à traduire")
    print(f"   - {len(attr_suggestions)} attributs à traduire")
    print(f"   - {len(new_keys)} nouvelles clés i18n nécessaires")
    print()

    # Grouper par contexte
    by_context = {}
    for s in suggestions:
        context = s['context']
        if context not in by_context:
            by_context[context] = []
        by_context[context].append(s)

    print("📋 Suggestions par contexte:\n")
    for context, items in sorted(by_context.items()):
        print(f"  [{context.upper()}] - {len(items)} éléments")
        for item in items[:5]:  # Afficher les 5 premiers
            print(f"    • <{item['tag']}> \"{item['text'][:60]}...\" → data-i18n=\"{item['key']}\"")
        if len(items) > 5:
            print(f"    ... et {len(items) - 5} autres")
        print()

    if attr_suggestions:
        print(f"  [ATTRIBUTES] - {len(attr_suggestions)} attributs")
        for item in attr_suggestions[:5]:
            print(f"    • <{item['tag']} {item['attribute']}> \"{item['value'][:50]}...\" → data-i18n-{item['attribute']}=\"{item['key']}\"")
        if len(attr_suggestions) > 5:
            print(f"    ... et {len(attr_suggestions) - 5} autres")
        print()

    print(f"\n{'='*80}")
    print(f"📝 Nouvelles clés à ajouter à i18n.js:")
    print(f"{'='*80}\n")

    for key, value in sorted(new_keys.items())[:20]:
        print(f'  "{key}": "{value}",')

    if len(new_keys) > 20:
        print(f"  ... et {len(new_keys) - 20} autres clés")

def apply_suggestions(analysis, output_file=None):
    """Appliquer les suggestions à la page HTML"""
    if not analysis:
        return False

    soup = analysis['soup']
    suggestions = analysis['suggestions']
    attr_suggestions = analysis['attr_suggestions']

    # Appliquer les suggestions d'éléments
    for s in suggestions:
        element = s['element']
        element['data-i18n'] = s['key']

    # Appliquer les suggestions d'attributs
    for s in attr_suggestions:
        element = s['element']
        attr_name = s['attribute']
        i18n_attr = f"data-i18n-{attr_name}"
        element[i18n_attr] = s['key']

    # Sauvegarder
    output = output_file or analysis['file']

    try:
        with open(output, 'w', encoding='utf-8') as f:
            f.write(str(soup.prettify()))

        print(f"\n✅ Fichier modifié sauvegardé: {output}")
        print(f"   - {len(suggestions)} attributs data-i18n ajoutés")
        print(f"   - {len(attr_suggestions)} attributs data-i18n-* ajoutés")
        return True
    except Exception as e:
        print(f"\n❌ Erreur lors de la sauvegarde: {e}")
        return False

def save_new_keys(analysis, output_file):
    """Sauvegarder les nouvelles clés dans un fichier JSON"""
    if not analysis:
        return

    new_keys = analysis['new_keys']

    # Créer un objet avec les nouvelles clés
    keys_data = {
        'source_file': analysis['file'],
        'total_keys': len(new_keys),
        'keys': {}
    }

    for key, value in sorted(new_keys.items()):
        keys_data['keys'][key] = {
            'en': value,  # Texte original (anglais)
            'es': '',     # À traduire
            'fr': '',
            'de': '',
            'pt': '',
            'zh': '',
            'ja': '',
            'ko': '',
            'ar': '',
            'hi': ''
        }

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(keys_data, f, indent=2, ensure_ascii=False)

        print(f"\n✅ Nouvelles clés sauvegardées: {output_file}")
        print(f"   - {len(new_keys)} clés à traduire")
    except Exception as e:
        print(f"\n❌ Erreur lors de la sauvegarde des clés: {e}")

def main():
    parser = argparse.ArgumentParser(description='Script semi-automatisé d\'ajout i18n')
    parser.add_argument('file', help='Fichier HTML à analyser')
    parser.add_argument('--apply', action='store_true', help='Appliquer les modifications')
    parser.add_argument('--output', help='Fichier de sortie (par défaut: remplace l\'original)')
    parser.add_argument('--keys-output', help='Fichier JSON pour les nouvelles clés')

    args = parser.parse_args()

    html_file = args.file
    if not os.path.isabs(html_file):
        html_file = os.path.join(PROJECT_ROOT, html_file)

    if not os.path.exists(html_file):
        print(f"❌ Fichier non trouvé: {html_file}")
        return

    # Analyser la page
    analysis = analyze_page(html_file)

    if not analysis:
        return

    # Afficher l'aperçu
    preview_suggestions(analysis)

    # Sauvegarder les nouvelles clés
    if args.keys_output:
        keys_file = args.keys_output
        if not os.path.isabs(keys_file):
            keys_file = os.path.join(PROJECT_ROOT, keys_file)
        save_new_keys(analysis, keys_file)
    else:
        # Par défaut, sauvegarder avec le nom du fichier
        base_name = os.path.splitext(os.path.basename(html_file))[0]
        keys_file = os.path.join(PROJECT_ROOT, f"i18n_keys_{base_name}.json")
        save_new_keys(analysis, keys_file)

    # Appliquer si demandé
    if args.apply:
        print(f"\n{'='*80}")
        print("⚠️  APPLICATION DES MODIFICATIONS")
        print(f"{'='*80}\n")

        confirm = input("Voulez-vous vraiment appliquer ces modifications? (oui/non): ")
        if confirm.lower() in ['oui', 'yes', 'y', 'o']:
            apply_suggestions(analysis, args.output)
        else:
            print("❌ Modifications annulées")
    else:
        print(f"\n{'='*80}")
        print("ℹ️  MODE PRÉVISUALISATION")
        print(f"{'='*80}")
        print("\nPour appliquer les modifications, ajoutez --apply:")
        print(f"  python3 add_i18n_smart.py {args.file} --apply")

if __name__ == "__main__":
    main()
