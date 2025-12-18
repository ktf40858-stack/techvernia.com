#!/usr/bin/env python3
"""
Traduire tous les contenus des outils image avec Argos Translate
"""
import json
import time
import argostranslate.translate
from tqdm import tqdm

print("\n" + "="*80)
print("🚀 TRADUCTION DES CONTENUS IMAGE - 318 CLÉS × 9 LANGUES")
print("="*80 + "\n")

# Charger les clés à traduire
print("📝 Chargement des contenus à traduire...")
with open('all_image_contents_to_translate.json', 'r', encoding='utf-8') as f:
    contents_to_translate = json.load(f)

num_keys = len(contents_to_translate)
total_translations = num_keys * 9

print(f"✅ {num_keys} clés à traduire → {total_translations} traductions à générer\n")

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

print(f"🌍 Traduction de {num_keys} clés en 9 langues...")
start_time = time.time()

# Pour chaque langue
for lang_code, lang_name in languages.items():
    print(f"\n  🌍 {lang_name} ({lang_code})...")

    # Charger le fichier de traduction existant
    translation_file = f'all_full_translations_{lang_code}.json'
    try:
        with open(translation_file, 'r', encoding='utf-8') as f:
            all_translations = json.load(f)
    except FileNotFoundError:
        print(f"  ⚠️  Fichier {translation_file} non trouvé, création...")
        all_translations = {}

    # Traduire chaque clé
    translated_count = 0
    skipped_count = 0

    for key, text in tqdm(contents_to_translate.items(), desc=f"     {lang_code.upper()}", unit='clé'):
        # Si la traduction existe déjà et n'est pas en anglais, skip
        if key in all_translations and all_translations[key] != text:
            skipped_count += 1
            continue

        try:
            # Traduire avec Argos
            translation = argostranslate.translate.translate(text, 'en', lang_code)
            all_translations[key] = translation
            translated_count += 1
        except Exception as e:
            print(f"\n  ⚠️  Erreur pour {key}: {e}")
            # Garder le texte en anglais en cas d'erreur
            all_translations[key] = text

    # Sauvegarder le fichier mis à jour
    with open(translation_file, 'w', encoding='utf-8') as f:
        json.dump(all_translations, f, ensure_ascii=False, indent=2)

    print(f"     ✅ {translated_count} nouvelles traductions, {skipped_count} déjà existantes")
    print(f"     ✅ Sauvegardé dans {translation_file}")

elapsed_time = time.time() - start_time
minutes = int(elapsed_time // 60)
seconds = int(elapsed_time % 60)

print(f"\n✅ Traduction terminée en {minutes}m {seconds}s\n")

# Vérification
print("="*80)
print("🔍 VÉRIFICATION DES TRADUCTIONS")
print("="*80 + "\n")

# Afficher un échantillon de traductions
sample_key = list(contents_to_translate.keys())[0]
sample_text = contents_to_translate[sample_key]

print(f"Échantillon - Clé: {sample_key}")
print(f"EN: {sample_text[:150]}...")
print()

for lang_code, lang_name in languages.items():
    with open(f'all_full_translations_{lang_code}.json', 'r', encoding='utf-8') as f:
        translations = json.load(f)

    if sample_key in translations:
        translated = translations[sample_key][:150]
        print(f"{lang_code.upper()}: {translated}...")

print("\n" + "="*80)
print("✅ CONTENUS IMAGE TRADUITS!")
print(f"📊 {num_keys} clés × 9 langues = {total_translations} traductions")
print(f"⏱️  Temps total: {minutes}m {seconds}s")
print("="*80 + "\n")
