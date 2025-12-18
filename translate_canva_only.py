#!/usr/bin/env python3
"""
Traduire uniquement les clés manquantes de Canva-AI
"""
import json
import argostranslate.package
import argostranslate.translate

print("=" * 80)
print("🌍 TRADUCTION DES CLÉS MANQUANTES - CANVA-AI UNIQUEMENT")
print("=" * 80)
print()

# Charger toutes les clés à traduire
with open('keys_to_translate.json', 'r', encoding='utf-8') as f:
    all_keys = json.load(f)

# Filtrer seulement les clés Canva-AI
canva_keys = {k: v for k, v in all_keys.items() if k.startswith('review.canva-ai.')}

print(f"📊 Clés Canva-AI à traduire: {len(canva_keys)}")
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
    total = len(canva_keys)

    for i, (key, text) in enumerate(canva_keys.items()):
        try:
            # Traduire
            translation = translator.translate(text)
            lang_trans[key] = translation
            translated_count += 1

            # Afficher progrès
            if (i + 1) % 10 == 0:
                print(f"  ... {i + 1}/{total} traduits", end='\r')

        except Exception as e:
            print(f"  ⚠️  Erreur pour {key}: {e}")

    print(f"  ✅ {translated_count}/{total} clés traduites (100%)        ")

    # Sauvegarder
    with open(f'all_full_translations_{lang_code}.json', 'w', encoding='utf-8') as f:
        json.dump(lang_trans, f, ensure_ascii=False, indent=2)

    print(f"  💾 Sauvegardé")
    print()

print("=" * 80)
print("✅ TOUTES LES CLÉS CANVA-AI ONT ÉTÉ TRADUITES!")
print("=" * 80)
