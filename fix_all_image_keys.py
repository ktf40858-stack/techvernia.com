#!/usr/bin/env python3
"""
Réextraction COMPLÈTE et CORRECTE de toutes les clés IMAGE depuis i18n.js
"""
import json
import re
import sys
sys.path.insert(0, '/home/komet/Desktop/Projekt/AI Tools/venv/lib/python3.13/site-packages')

import argostranslate.package
import argostranslate.translate

print("╔══════════════════════════════════════════════════════════╗")
print("║     RÉEXTRACTION COMPLÈTE DES CLÉS IMAGE DEPUIS i18n.js  ║")
print("╚══════════════════════════════════════════════════════════╝")
print()

# Liste des outils IMAGE
tools = [
    'adobe-firefly', 'artbreeder', 'bluewillow', 'clipdrop', 'craiyon',
    'dall-e-3', 'deepai', 'dreamstudio', 'getimg-ai', 'ideogram',
    'imagen', 'imgcreator', 'leonardo-ai', 'midjourney', 'nightcafe',
    'playground-ai', 'starryai', 'stockimg-ai', 'tensor-art'
]

# Lire i18n.js
with open('GenuisNet.ai/js/i18n.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Extraire section EN
en_match = re.search(r'en:\s*\{(.*?)\n\s*\},\s*\n\s*// ==+ FRENCH', content, re.DOTALL)

if not en_match:
    print("❌ Section EN non trouvée")
    sys.exit(1)

en_section = en_match.group(1)

# Extraire TOUTES les clés IMAGE (contenu + FAQ) avec regex robuste
all_keys = {}
lines = en_section.split('\n')

i = 0
while i < len(lines):
    line = lines[i].strip()

    # Chercher début de clé
    if line.startswith('"review.'):
        # Extraire le nom de la clé
        key_match = re.match(r'"(review\.[^"]+)":\s*"(.*)', line)
        if key_match:
            key = key_match.group(1)
            value_start = key_match.group(2)

            # Vérifier si c'est une clé IMAGE
            is_image_key = False
            for tool in tools:
                tool_key = tool.replace('-', '')
                if key.startswith(f'review.{tool_key}'):
                    is_image_key = True
                    break

            if is_image_key:
                # Construire la valeur complète (peut être multiligne)
                value = value_start

                # Si la ligne ne se termine pas par ", chercher la suite
                while not value.endswith('",') and not value.endswith('"'):
                    i += 1
                    if i >= len(lines):
                        break
                    value += '\n' + lines[i].strip()

                # Nettoyer: enlever ", ou " final
                if value.endswith('",'):
                    value = value[:-2]
                elif value.endswith('"'):
                    value = value[:-1]

                # Décoder les échappements
                value = value.replace('\\"', '"')
                value = value.replace("\\'", "'")
                value = value.replace('\\\\', '\\')

                all_keys[key] = value

    i += 1

print(f"✓ {len(all_keys)} clés IMAGE extraites depuis i18n.js")

# Charger le JSON existant pour garder les traductions déjà faites
with open('image_translations.json', 'r', encoding='utf-8') as f:
    existing_data = json.load(f)

# Mettre à jour la section EN avec les valeurs correctes
existing_data['en'] = all_keys

print(f"\n📝 Retraduction des {len(all_keys)} clés dans 9 langues...")
print("⏱️  Cela va prendre environ 50-60 minutes...")
print()

# Traduire
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

installed_languages = argostranslate.translate.get_installed_languages()
from_lang = next((lang for lang in installed_languages if lang.code == 'en'), None)

total_translations = len(all_keys) * 9
current = 0

for lang_code, lang_name in target_langs.items():
    print(f"  🌍 {lang_name}...", end='', flush=True)

    to_lang = next((lang for lang in installed_languages if lang.code == lang_code), None)

    if not from_lang or not to_lang:
        print(f" ⚠️  Non installée")
        continue

    translation = from_lang.get_translation(to_lang)

    # Créer dict pour cette langue si nécessaire
    if lang_code not in existing_data:
        existing_data[lang_code] = {}

    # Traduire chaque clé
    for key, text in all_keys.items():
        translated = translation.translate(text)
        existing_data[lang_code][key] = translated
        current += 1

        # Afficher progression tous les 50
        if current % 50 == 0:
            percentage = int(current * 100 / total_translations)
            print(f"\r  🌍 {lang_name}... {percentage}%", end='', flush=True)

    print(f"\r  ✓ {lang_name}: {len(all_keys)} clés traduites")

# Sauvegarder
with open('image_translations.json', 'w', encoding='utf-8') as f:
    json.dump(existing_data, f, ensure_ascii=False, indent=2)

print()
print("="*60)
print("✅ RÉEXTRACTION ET TRADUCTION TERMINÉES!")
print(f"📁 Fichier mis à jour: image_translations.json")
print(f"📊 {len(all_keys)} clés × 10 langues = {len(all_keys) * 10} traductions")
print()
print("🎯 Prochaine étape: python3 step2_integrate_translations.py image")
