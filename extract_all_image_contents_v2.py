#!/usr/bin/env python3
"""
Extraire SEULEMENT les contenus (paragraphes) pour tous les outils image
À partir des fichiers *_content_to_translate.json individuels
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
    '.badge',
    '.btn',
    '.button',
    '.case',
    '.step',
    '.plan',
    '.tier',
    '.level',
    '.desc',  # Sauf si c'est dans une FAQ
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

    # Nom du fichier individuel
    json_file = f'{tool.replace("-", "_")}_content_to_translate.json'

    if not os.path.exists(json_file):
        print(f"  ⚠️  Fichier {json_file} non trouvé")
        print()
        continue

    # Charger le fichier
    with open(json_file, 'r', encoding='utf-8') as f:
        tool_keys = json.load(f)

    print(f"  ✓ Chargé {len(tool_keys)} clés totales")

    # Filtrer pour garder SEULEMENT les contenus
    content_keys = {}

    for key, value in tool_keys.items():
        # Vérifier si la clé contient un pattern à exclure
        is_standard = any(pattern in key for pattern in exclude_patterns)

        # Cas spécial: toujours inclure les FAQs (question et answer)
        is_faq = '.faq' in key and ('.question' in key or '.answer' in key)

        # Vérifier la longueur: les contenus sont généralement longs (>80 caractères)
        is_long = len(value) > 80

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

# Afficher statistiques détaillées
print("📊 Détails par outil:")
for tool, keys in all_contents.items():
    faq_count = sum(1 for k in keys.keys() if '.faq' in k)
    content_count = len(keys) - faq_count
    print(f"  {tool:20} → {len(keys):3} clés ({content_count} contenus + {faq_count} FAQs)")

print()
# Afficher un échantillon
print("📋 Échantillon de clés extraites:")
sample_count = 0
for tool, keys in all_contents.items():
    if len(keys) > 0 and sample_count < 2:
        print(f"\n{tool}:")
        for key in list(keys.keys())[:2]:
            value = keys[key][:80] + "..." if len(keys[key]) > 80 else keys[key]
            print(f"  • {key}")
            print(f"    {value}")
        sample_count += 1
