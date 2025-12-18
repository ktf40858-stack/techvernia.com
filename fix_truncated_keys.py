#!/usr/bin/env python3
"""
Correction RAPIDE: ne retraduire que les clés tronquées
"""
import json
import re
import sys
sys.path.insert(0, '/home/komet/Desktop/Projekt/AI Tools/venv/lib/python3.13/site-packages')

import argostranslate.package
import argostranslate.translate

print("╔══════════════════════════════════════════════════════════╗")
print("║      CORRECTION DES CLÉS TRONQUÉES - IMAGE               ║")
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
print("📖 Lecture de i18n.js...")
with open('GenuisNet.ai/js/i18n.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Extraire section EN
en_match = re.search(r'en:\s*\{(.*?)\n\s*\},\s*\n\s*// ==+ FRENCH', content, re.DOTALL)
if not en_match:
    print("❌ Section EN non trouvée")
    sys.exit(1)

en_section = en_match.group(1)

# Extraire TOUTES les clés IMAGE depuis i18n.js
correct_keys = {}
lines = en_section.split('\n')

i = 0
while i < len(lines):
    line = lines[i].strip()
    if line.startswith('"review.'):
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
                value = value_start
                while not value.endswith('",') and not value.endswith('"'):
                    i += 1
                    if i >= len(lines):
                        break
                    value += '\n' + lines[i].strip()

                if value.endswith('",'):
                    value = value[:-2]
                elif value.endswith('"'):
                    value = value[:-1]

                value = value.replace('\\"', '"')
                value = value.replace("\\'", "'")
                value = value.replace('\\\\', '\\')

                correct_keys[key] = value
    i += 1

print(f"✓ {len(correct_keys)} clés IMAGE trouvées dans i18n.js")

# Charger le JSON actuel
print("\n📖 Lecture de image_translations.json...")
with open('image_translations.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Comparer et identifier les clés à corriger
keys_to_fix = []
for key in correct_keys:
    if key not in data['en']:
        keys_to_fix.append(key)
        print(f"  + Clé manquante: {key}")
    elif data['en'][key] != correct_keys[key]:
        keys_to_fix.append(key)

print(f"\n🔧 {len(keys_to_fix)} clés à corriger")

if len(keys_to_fix) == 0:
    print("✅ Aucune correction nécessaire!")
    sys.exit(0)

# Afficher quelques exemples
print("\n📝 Exemples de corrections:")
for key in keys_to_fix[:3]:
    print(f"\n  Clé: {key}")
    if key in data['en']:
        print(f"  Avant: {data['en'][key][:80]}...")
    else:
        print(f"  Avant: (manquante)")
    print(f"  Après: {correct_keys[key][:80]}...")

# Mettre à jour EN
print(f"\n✓ Mise à jour de {len(keys_to_fix)} clés EN...")
for key in keys_to_fix:
    data['en'][key] = correct_keys[key]

# Traduire uniquement les clés corrigées
print(f"\n📝 Traduction de {len(keys_to_fix)} clés dans 9 langues...")
print(f"⏱️  Estimation: {int(len(keys_to_fix) * 9 * 0.6 / 60)} minutes")
print()

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

for lang_code, lang_name in target_langs.items():
    print(f"  🌍 {lang_name}...", end='', flush=True)

    to_lang = next((lang for lang in installed_languages if lang.code == lang_code), None)
    if not from_lang or not to_lang:
        print(f" ⚠️  Non installée")
        continue

    translation = from_lang.get_translation(to_lang)

    if lang_code not in data:
        data[lang_code] = {}

    for key in keys_to_fix:
        text = correct_keys[key]
        translated = translation.translate(text)
        data[lang_code][key] = translated

    print(f"\r  ✓ {lang_name}: {len(keys_to_fix)} clés traduites")

# Sauvegarder
with open('image_translations.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print()
print("="*60)
print(f"✅ CORRECTION TERMINÉE!")
print(f"📁 Fichier mis à jour: image_translations.json")
print(f"🔧 {len(keys_to_fix)} clés corrigées × 10 langues")
print()
print("🎯 Prochaine étape: python3 step2_integrate_translations.py image")
