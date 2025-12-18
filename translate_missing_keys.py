#!/usr/bin/env python3
"""
Traduire toutes les clés manquantes qui sont restées en anglais
"""
import json
import argostranslate.package
import argostranslate.translate
import time

print("=" * 80)
print("🌍 TRADUCTION DES CLÉS MANQUANTES")
print("=" * 80)
print()

# Charger les traductions anglaises
with open('all_full_translations_en.json', 'r', encoding='utf-8') as f:
    en_trans = json.load(f)

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

# Outils
tools = ['canva-ai', 'adobe-firefly', 'clipdrop', 'dall-e-3', 'ideogram', 'leonardo-ai', 'midjourney', 'stable-diffusion']

# Pour chaque langue
for lang_code, lang_name in languages.items():
    print(f"🌍 {lang_name.upper()} ({lang_code})")

    # Charger les traductions existantes
    with open(f'all_full_translations_{lang_code}.json', 'r', encoding='utf-8') as f:
        lang_trans = json.load(f)

    # Compter les clés à traduire
    to_translate = {}
    for tool in tools:
        tool_prefix = f'review.{tool}.'
        for key in en_trans:
            if key.startswith(tool_prefix) and key in lang_trans:
                if en_trans[key] == lang_trans[key]:
                    to_translate[key] = en_trans[key]

    if not to_translate:
        print(f"  ✅ Aucune clé à traduire\n")
        continue

    print(f"  📊 {len(to_translate)} clés à traduire")

    # Obtenir le traducteur
    from_lang = 'en'
    to_lang = lang_code

    translator = argostranslate.translate.get_translation_from_codes(from_lang, to_lang)

    if not translator:
        print(f"  ⚠️  Traducteur non disponible pour {lang_code}\n")
        continue

    # Traduire
    translated_count = 0
    for i, (key, text) in enumerate(to_translate.items()):
        try:
            translation = translator.translate(text)
            lang_trans[key] = translation
            translated_count += 1

            if (i + 1) % 10 == 0:
                print(f"  ... {i + 1}/{len(to_translate)} traduits", end='\r')
        except Exception as e:
            print(f"  ⚠️  Erreur pour {key}: {e}")

    print(f"  ✅ {translated_count}/{len(to_translate)} clés traduites")

    # Sauvegarder
    with open(f'all_full_translations_{lang_code}.json', 'w', encoding='utf-8') as f:
        json.dump(lang_trans, f, ensure_ascii=False, indent=2)

    print(f"  💾 Sauvegardé dans all_full_translations_{lang_code}.json\n")

print("=" * 80)
print("✅ TOUTES LES CLÉS MANQUANTES ONT ÉTÉ TRADUITES!")
print("=" * 80)
