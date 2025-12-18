#!/usr/bin/env python3
"""
Corriger les préfixes dans tous les fichiers *-i18n.js
Remplacer review.tool.name. par review.tool-name.
"""
import re
import os

print("=" * 80)
print("🔧 CORRECTION DES PRÉFIXES I18N")
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

js_dir = 'GenuisNet.ai/js'

for tool in image_tools:
    i18n_file = f'{js_dir}/{tool}-i18n.js'

    if not os.path.exists(i18n_file):
        print(f"⚠️  {tool}-i18n.js non trouvé")
        continue

    print(f"🔧 Correction: {tool}-i18n.js")

    # Lire le fichier
    with open(i18n_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Préfixe incorrect (avec points) vs correct (avec tirets)
    wrong_prefix = f'review.{tool.replace("-", ".")}.'
    correct_prefix = f'review.{tool}.'

    # Compter les occurrences
    count = content.count(wrong_prefix)

    if count > 0:
        print(f"  ❌ Trouvé {count} occurrences de '{wrong_prefix}'")

        # Remplacer toutes les occurrences
        new_content = content.replace(wrong_prefix, correct_prefix)

        # Sauvegarder
        with open(i18n_file, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"  ✅ Remplacé par '{correct_prefix}'")
    else:
        print(f"  ✅ Déjà correct (utilise '{correct_prefix}')")

    print()

print()
print("=" * 80)
print("✅ TOUS LES PRÉFIXES ONT ÉTÉ CORRIGÉS!")
print("=" * 80)
