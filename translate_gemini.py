#!/usr/bin/env python3
"""
Traduction des clés Gemini avec Argos Translate
"""
import json
import argostranslate.translate
from pathlib import Path
from tqdm import tqdm
import time

print("📝 60 clés Gemini à traduire")
print("🌍 9 langues cibles")
print("📊 Total: 540 traductions\n")

# Charger le contenu à traduire
with open('gemini_content_to_translate.json', 'r', encoding='utf-8') as f:
    content = json.load(f)

# Langues cibles
languages = {
    'es': 'Espagnol',
    'fr': 'Français',
    'de': 'Allemand',
    'pt': 'Portugais',
    'zh': 'Chinois',
    'ja': 'Japonais',
    'ko': 'Coréen',
    'ar': 'Arabe',
    'hi': 'Hindi'
}

# Résultats
all_results = {}
start_time = time.time()

# Traduire pour chaque langue
for lang_code, lang_name in languages.items():
    print(f"\n🌍 {lang_name} ({lang_code})...")

    translated = {}

    # Traduire chaque clé
    for key, text in tqdm(content.items(), desc=lang_code.upper(), unit='clé'):
        try:
            translation = argostranslate.translate.translate(text, 'en', lang_code)
            translated[key] = translation
        except Exception as e:
            print(f"\n⚠️  Erreur pour {key}: {e}")
            translated[key] = text  # Garder l'anglais en cas d'erreur

    all_results[lang_code] = translated
    print(f"   ✅ {len(translated)} clés traduites")

# Calculer le temps total
elapsed_time = time.time() - start_time
minutes = int(elapsed_time // 60)
seconds = int(elapsed_time % 60)

# Sauvegarder
output_file = 'gemini_translations_all_langs.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(all_results, f, indent=2, ensure_ascii=False)

print("\n" + "="*60)
print("✅ TRADUCTION GEMINI TERMINÉE!")
print(f"⏱️  Temps total: {minutes}.{seconds//6} minutes")
print(f"📁 Sauvegardé: {output_file}")
print("="*60)

# Afficher quelques exemples
print("\n🔍 Exemples de traductions:\n")
example_key = list(content.keys())[0]
print(f"📌 Clé: {example_key}")
print(f"🇬🇧 EN: {content[example_key]}")
for lang_code in ['es', 'fr', 'de']:
    print(f"   {languages[lang_code]}: {all_results[lang_code][example_key]}")
