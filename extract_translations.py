#!/usr/bin/env python3
import sys, io, json

if sys.platform=='win32':
    sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

languages = ['de', 'fr', 'es', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']

print("📦 Extraction des traductions...")

for lang in languages:
    input_path = f'GenuisNet.ai/pages/reviews/hr/translations-{lang}.json'
    output_path = f'GenuisNet.ai/pages/reviews/hr/trans-{lang}.json'

    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Extraire seulement les traductions (gérer les 2 formats possibles)
    if 'translations' in data:
        translations = data['translations']
    else:
        translations = data

    # Sauvegarder format propre
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(translations, f, indent=2, ensure_ascii=False)

    print(f"  ✓ {lang}: {len(translations)} clés")

print("\n✅ Toutes les traductions extraites!")
