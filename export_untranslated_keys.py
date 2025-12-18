#!/usr/bin/env python3
"""
Exporter toutes les clés non traduites qui sont utilisées dans les HTML
"""
import json
import os

# Charger les traductions
with open('all_full_translations_en.json', 'r', encoding='utf-8') as f:
    en_trans = json.load(f)

with open('all_full_translations_es.json', 'r', encoding='utf-8') as f:
    es_trans = json.load(f)

# Outils (sans adobe qui fonctionne)
tools_html = {
    'canva-ai': 'GenuisNet.ai/pages/reviews/image/canva-ai.html',
    'clipdrop': 'GenuisNet.ai/pages/reviews/image/clipdrop.html',
    'dall-e-3': 'GenuisNet.ai/pages/reviews/image/dall-e-3.html',
    'ideogram': 'GenuisNet.ai/pages/reviews/image/ideogram.html',
    'leonardo-ai': 'GenuisNet.ai/pages/reviews/image/leonardo-ai.html',
    'midjourney': 'GenuisNet.ai/pages/reviews/image/midjourney.html',
    'stable-diffusion': 'GenuisNet.ai/pages/reviews/image/stable-diffusion.html'
}

print("=" * 80)
print("📊 EXTRACTION DES CLÉS NON TRADUITES UTILISÉES")
print("=" * 80)
print()

all_untranslated = {}
summary = {}

for tool, html_path in tools_html.items():
    tool_prefix = f'review.{tool}.'

    # Trouver les clés non traduites
    untranslated = {}
    for key in en_trans:
        if key.startswith(tool_prefix) and key in es_trans:
            if en_trans[key] == es_trans[key]:
                untranslated[key] = en_trans[key]

    # Lire le HTML pour vérifier l'utilisation
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Filtrer les clés utilisées
    used_untranslated = {}
    for key, text in untranslated.items():
        if f'data-i18n="{key}"' in html_content or f"data-i18n='{key}'" in html_content:
            used_untranslated[key] = text

    all_untranslated.update(used_untranslated)
    summary[tool] = len(used_untranslated)

    print(f"{tool}: {len(used_untranslated)} clés non traduites utilisées")

print()
print(f"TOTAL: {len(all_untranslated)} clés à traduire")
print()

# Sauvegarder dans un fichier JSON
output_file = 'keys_to_translate.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(all_untranslated, f, ensure_ascii=False, indent=2)

print(f"💾 Sauvegardé dans: {output_file}")
print()
print("=" * 80)
