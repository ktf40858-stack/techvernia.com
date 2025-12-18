#!/usr/bin/env python3
"""
Supprimer les titres communs existants des fichiers i18n
"""
import re

print("=" * 80)
print("🧹 SUPPRESSION DES TITRES COMMUNS EXISTANTS")
print("=" * 80)
print()

tools = [
    'adobe-firefly',
    'canva-ai',
    'clipdrop',
    'dall-e-3',
    'ideogram',
    'leonardo-ai',
    'midjourney',
    'stable-diffusion'
]

for tool in tools:
    i18n_file = f'GenuisNet.ai/js/{tool}-i18n.js'
    print(f"🧹 {tool}-i18n.js")

    with open(i18n_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Filtrer les lignes qui contiennent des titres communs
    new_lines = []
    removed_count = 0

    for line in lines:
        # Si la ligne contient une clé review.common.*, on la saute
        if re.search(r'"review\.common\.[^"]+"\s*:', line):
            removed_count += 1
            continue
        new_lines.append(line)

    # Sauvegarder
    with open(i18n_file, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

    print(f"  ✅ Supprimé {removed_count} lignes de titres communs\n")

print("=" * 80)
print("✅ TOUS LES TITRES COMMUNS ONT ÉTÉ SUPPRIMÉS!")
print("=" * 80)
