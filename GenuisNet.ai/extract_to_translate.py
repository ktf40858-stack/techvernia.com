#!/usr/bin/env python3
"""
Extraire toutes les phrases à traduire
"""

import json
import sys
import os

PROJECT_ROOT = "/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai"

def extract_untranslated(input_file):
    """Extraire toutes les phrases marquées [TO TRANSLATE]"""

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return None

    keys = data.get('keys', {})

    # Extraire les phrases à traduire
    to_translate = []

    for key, translations in sorted(keys.items()):
        en_text = translations['en']

        # Vérifier si des traductions manquent
        needs_translation = False
        for lang in ['es', 'fr', 'de', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']:
            if translations[lang].startswith('[TO TRANSLATE]'):
                needs_translation = True
                break

        if needs_translation:
            to_translate.append({
                'key': key,
                'en': en_text
            })

    print(f"\n{'='*80}")
    print(f"📝 PHRASES À TRADUIRE")
    print(f"{'='*80}\n")
    print(f"Total: {len(to_translate)} phrases\n")

    # Afficher toutes les phrases
    for i, item in enumerate(to_translate, 1):
        print(f"{i:3}. [{item['key']}]")
        print(f"     EN: {item['en']}")
        print()

    # Sauvegarder dans un fichier texte
    output_file = input_file.replace('.json', '_to_translate.txt')
    with open(output_file, 'w', encoding='utf-8') as f:
        for item in to_translate:
            f.write(f"[{item['key']}]\n")
            f.write(f"EN: {item['en']}\n\n")

    print(f"✅ Liste sauvegardée: {output_file}")

    return to_translate

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 extract_to_translate.py <fichier.json>")
        sys.exit(1)

    input_file = sys.argv[1]
    if not os.path.isabs(input_file):
        input_file = os.path.join(PROJECT_ROOT, input_file)

    if not os.path.exists(input_file):
        print(f"❌ Fichier non trouvé: {input_file}")
        sys.exit(1)

    extract_untranslated(input_file)

if __name__ == "__main__":
    main()
