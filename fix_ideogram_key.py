#!/usr/bin/env python3
"""
Correction rapide de la clé ideogram problématique dans image_translations.json
"""
import json
import sys
sys.path.insert(0, '/home/komet/Desktop/Projekt/AI Tools/venv/lib/python3.13/site-packages')

import argostranslate.package
import argostranslate.translate

# Texte EN correct
correct_en = 'Ideogram has a separate "Text to include" field. Specify exact text here instead of just in the prompt for best results.'

key = "review.ideogram.ideogram.has.a.separate.text"

print("🔧 CORRECTION DE LA CLÉ IDEOGRAM")
print("="*60)

# Charger le JSON
with open('image_translations.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Corriger EN
print(f"\n✓ Correction EN:")
print(f"  Avant: {data['en'][key]}")
data['en'][key] = correct_en
print(f"  Après: {data['en'][key]}")

# Traduire dans les 9 langues
target_langs = {
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

print("\n📝 Traduction dans les 9 langues...")

installed_languages = argostranslate.translate.get_installed_languages()
from_lang = next((lang for lang in installed_languages if lang.code == 'en'), None)

for lang_code, lang_name in target_langs.items():
    to_lang = next((lang for lang in installed_languages if lang.code == lang_code), None)

    if from_lang and to_lang:
        translation = from_lang.get_translation(to_lang)
        translated = translation.translate(correct_en)

        print(f"  {lang_code.upper()}: {translated}")
        data[lang_code][key] = translated
    else:
        print(f"  ⚠️  {lang_code.upper()}: Langue non installée")

# Sauvegarder
with open('image_translations.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\n" + "="*60)
print("✅ CORRECTION TERMINÉE!")
print("📁 Fichier mis à jour: image_translations.json")
print("\n🎯 Prochaine étape: python3 step2_integrate_translations.py image")
