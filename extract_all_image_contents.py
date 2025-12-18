#!/usr/bin/env python3
"""
Extraire SEULEMENT les contenus (paragraphes) pour tous les outils image
PAS les clés standards comme overview, key.features, etc.
"""
import json
import os

print("=" * 80)
print("📥 EXTRACTION DES CONTENUS POUR TOUS LES OUTILS IMAGE")
print("=" * 80)
print()

# Liste des outils image
image_tools = [
    'adobe-firefly',
    'canva-ai',
    'clipdrop',
    'dall-e-3',
    'ideogram',
    'leonardo-ai',
    'midjourney',
    'stable-diffusion'
]

# Charger all_full_translations_en.json
if not os.path.exists('all_full_translations_en.json'):
    print("❌ all_full_translations_en.json non trouvé")
    exit(1)

with open('all_full_translations_en.json', 'r', encoding='utf-8') as f:
    all_en = json.load(f)

print(f"✓ Chargé {len(all_en)} clés en anglais")
print()

# Patterns à EXCLURE (clés standards - SAUF FAQs)
exclude_patterns = [
    '.overview',
    '.key.features',
    '.pros.cons',
    '.pros',
    '.cons',
    '.pricing',
    '.getting.started',
    '.verdict',
    '.comparison',
    '.use.cases',
    '.use.case',
    '.limitations',
    '.alternatives',
    # '.faq',  # ← GARDÉ: on veut traduire les FAQs
    # '.question',  # ← GARDÉ: partie des FAQs
    # '.answer',  # ← GARDÉ: partie des FAQs
    '.badge',
    '.btn',
    '.button',
    '.case',
    '.step',
    '.plan',
    '.tier',
    '.level',
    '.title',
    '.desc',
    '.label',
    '.name',
    '.subtitle',
    '.feature'
]

# Pour chaque outil
all_contents = {}
total_keys = 0

for tool in image_tools:
    print(f"📝 Extraction: {tool}")

    # Convertir tool-name en tool.name
    tool_key = tool.replace('-', '.')
    prefix = f'review.{tool_key}.'

    # Extraire toutes les clés de cet outil
    tool_keys = {k: v for k, v in all_en.items() if k.startswith(prefix)}

    # Filtrer pour garder SEULEMENT les contenus (exclure les standards)
    content_keys = {}

    for key, value in tool_keys.items():
        # Vérifier si la clé contient un pattern à exclure
        is_standard = any(pattern in key for pattern in exclude_patterns)

        # Cas spécial: toujours inclure les FAQs (question et answer)
        is_faq = '.faq' in key and ('.question' in key or '.answer' in key)

        # Vérifier aussi la longueur: les contenus sont généralement longs (>100 caractères)
        is_long = len(value) > 100

        # Inclure si: (pas standard ET long) OU est une FAQ
        if (not is_standard and is_long) or is_faq:
            content_keys[key] = value

    all_contents[tool] = content_keys
    total_keys += len(content_keys)

    print(f"  ✓ {len(content_keys)} clés de contenu extraites")

    # Sauvegarder dans un fichier séparé
    output_file = f'{tool.replace("-", "_")}_contents_only.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(content_keys, f, ensure_ascii=False, indent=2)

    print(f"  ✓ Sauvegardé: {output_file}")
    print()

# Créer un fichier combiné
with open('all_image_contents_to_translate.json', 'w', encoding='utf-8') as f:
    combined = {}
    for tool, keys in all_contents.items():
        combined.update(keys)
    json.dump(combined, f, ensure_ascii=False, indent=2)

print()
print("=" * 80)
print(f"✅ EXTRACTION TERMINÉE!")
print(f"📊 Total: {total_keys} clés de contenu à traduire")
print(f"📄 Fichier combiné: all_image_contents_to_translate.json")
print("=" * 80)
print()

# Afficher un échantillon
print("📋 Échantillon de clés extraites:")
for tool, keys in list(all_contents.items())[:2]:
    print(f"\n{tool}:")
    for key in list(keys.keys())[:3]:
        value = keys[key][:100] + "..." if len(keys[key]) > 100 else keys[key]
        print(f"  • {key}")
        print(f"    {value}")
