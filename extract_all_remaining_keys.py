#!/usr/bin/env python3
"""
Extraire TOUTES les clés restantes des outils image (titres, FAQs, etc.)
"""
import json
import os

print("=" * 80)
print("📝 EXTRACTION DE TOUTES LES CLÉS RESTANTES")
print("=" * 80)
print()

# Liste des outils image
image_tools = [
    'adobe_firefly',
    'canva_ai',
    'clipdrop',
    'dall_e_3',
    'ideogram',
    'leonardo_ai',
    'midjourney',
    'stable_diffusion'
]

# Charger les clés déjà traduites
with open('all_image_contents_to_translate.json', 'r', encoding='utf-8') as f:
    already_translated = json.load(f)

print(f"✅ Clés déjà traduites: {len(already_translated)}")
print()

# Collecter toutes les nouvelles clés
all_new_keys = {}

for tool in image_tools:
    content_file = f'{tool}_contents_only.json'

    if not os.path.exists(content_file):
        print(f"⚠️  {content_file} non trouvé")
        continue

    with open(content_file, 'r', encoding='utf-8') as f:
        tool_content = json.load(f)

    # Trouver les clés qui n'ont pas encore été traduites
    new_keys = {k: v for k, v in tool_content.items() if k not in already_translated}

    if new_keys:
        print(f"📦 {tool}: {len(new_keys)} nouvelles clés")
        all_new_keys.update(new_keys)

        # Afficher quelques exemples
        for i, (key, value) in enumerate(list(new_keys.items())[:3]):
            print(f"     - {key[:60]}...")
            print(f"       {value[:80]}...")
    else:
        print(f"✅ {tool}: Aucune nouvelle clé")

print()
print(f"📊 TOTAL nouvelles clés à traduire: {len(all_new_keys)}")

if all_new_keys:
    # Sauvegarder
    output_file = 'all_remaining_keys_to_translate.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_new_keys, f, ensure_ascii=False, indent=2)

    print(f"💾 Sauvegardé dans: {output_file}")
else:
    print("ℹ️  Toutes les clés ont déjà été traduites!")

print()
print("=" * 80)
