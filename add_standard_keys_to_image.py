#!/usr/bin/env python3
"""
Script pour ajouter automatiquement les 108 clés standards aux outils image
"""
import json

# Load standard patterns
with open('standard_patterns.json', 'r', encoding='utf-8') as f:
    standard_patterns = json.load(f)

# Load review content
with open('review_content_to_translate.json', 'r', encoding='utf-8') as f:
    review = json.load(f)

# Image tools
image_tools = ['adobe-firefly', 'canva-ai', 'clipdrop', 'dall-e-3',
               'ideogram', 'leonardo-ai', 'midjourney', 'stable-diffusion']

print("="*70)
print("AJOUT AUTOMATIQUE DES CLÉS STANDARDS AUX OUTILS IMAGE")
print("="*70)

# Track changes
total_added = 0
tool_stats = {}

for tool in image_tools:
    prefix = f'review.{tool}.'

    # Get existing patterns for this tool
    existing_keys = {k for k in review.keys() if k.startswith(prefix)}

    def get_pattern(key):
        parts = key.split('.')
        if len(parts) >= 3 and parts[0] == 'review':
            return '.'.join(parts[2:])
        return None

    existing_patterns = {get_pattern(k) for k in existing_keys if get_pattern(k)}

    # Find missing patterns
    missing_patterns = set(standard_patterns.keys()) - existing_patterns

    # Add missing keys
    added_count = 0
    for pattern in missing_patterns:
        new_key = f'review.{tool}.{pattern}'
        # Use the example value from standard patterns
        review[new_key] = standard_patterns[pattern]
        added_count += 1

    tool_stats[tool] = {
        'existing': len(existing_patterns),
        'added': added_count,
        'total': len(existing_patterns) + added_count
    }
    total_added += added_count

    print(f"\n🎨 {tool}:")
    print(f"   Clés existantes: {len(existing_patterns)}")
    print(f"   Clés ajoutées:   {added_count}")
    print(f"   Total final:     {len(existing_patterns) + added_count}")

# Save updated review content
with open('review_content_to_translate.json', 'w', encoding='utf-8') as f:
    json.dump(review, f, indent=2, ensure_ascii=False)

print(f"\n{'='*70}")
print(f"✅ TERMINÉ!")
print(f"   Total de clés ajoutées: {total_added}")
print(f"   Fichier mis à jour: review_content_to_translate.json")
print(f"{'='*70}")

# Generate summary report
print(f"\n📊 RAPPORT DÉTAILLÉ:")
for tool, stats in tool_stats.items():
    coverage = (stats['existing'] / (stats['existing'] + stats['added']) * 100) if stats['added'] > 0 else 100
    print(f"   {tool:20s}: {stats['total']:3d} clés (était {stats['existing']}, +{stats['added']})")
