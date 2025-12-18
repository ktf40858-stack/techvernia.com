#!/usr/bin/env python3
"""
Traduire toutes les clés manquantes dans toutes les langues
"""
import json
import argostranslate.package
import argostranslate.translate
import time

print("=" * 80)
print("🌍 TRADUCTION DES CLÉS MANQUANTES - TOUTES LANGUES")
print("=" * 80)
print()

# Charger les clés à traduire
with open('keys_to_translate.json', 'r', encoding='utf-8') as f:
    keys_to_translate = json.load(f)

print(f"📊 Clés à traduire: {len(keys_to_translate)}")
print()

# Langues cibles
languages = {
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
    'pt': 'Portuguese',
    'zh': 'Chinese',
    'ja': 'Japanese',
    'ko': 'Korean',
    'ar': 'Arabic',
    'hi': 'Hindi'
}

# Pour chaque langue
for lang_code, lang_name in languages.items():
    print(f"🌍 {lang_name.upper()} ({lang_code})")

    # Charger les traductions existantes
    with open(f'all_full_translations_{lang_code}.json', 'r', encoding='utf-8') as f:
        lang_trans = json.load(f)

    # Obtenir le traducteur
    translator = argostranslate.translate.get_translation_from_codes('en', lang_code)

    if not translator:
        print(f"  ⚠️  Traducteur non disponible pour {lang_code}")
        print()
        continue

    # Traduire
    translated_count = 0
    total = len(keys_to_translate)

    for i, (key, text) in enumerate(keys_to_translate.items()):
        try:
            # Traduire
            translation = translator.translate(text)
            lang_trans[key] = translation
            translated_count += 1

            # Afficher progrès
            if (i + 1) % 50 == 0:
                print(f"  ... {i + 1}/{total} traduits ({100*(i+1)//total}%)", end='\r')

        except Exception as e:
            print(f"  ⚠️  Erreur pour {key}: {e}")

    print(f"  ✅ {translated_count}/{total} clés traduites ({100*translated_count//total}%)        ")

    # Sauvegarder
    with open(f'all_full_translations_{lang_code}.json', 'w', encoding='utf-8') as f:
        json.dump(lang_trans, f, ensure_ascii=False, indent=2)

    print(f"  💾 Sauvegardé dans all_full_translations_{lang_code}.json")
    print()

print("=" * 80)
print("✅ TOUTES LES CLÉS MANQUANTES ONT ÉTÉ TRADUITES!")
print("=" * 80)
