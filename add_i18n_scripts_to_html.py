#!/usr/bin/env python3
"""
Ajouter les scripts i18n dans chaque fichier HTML des outils image
"""
import os

print("=" * 80)
print("🔧 AJOUT DES SCRIPTS I18N DANS LES FICHIERS HTML")
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

for tool in image_tools:
    html_file = f'GenuisNet.ai/pages/reviews/image/{tool}.html'

    if not os.path.exists(html_file):
        print(f"⚠️  {tool}.html non trouvé")
        continue

    print(f"🔧 Traitement: {tool}.html")

    # Lire le fichier
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Vérifier si le script est déjà ajouté
    script_tag = f'<script src="../../../js/{tool}-i18n.js"></script>'

    if script_tag in content:
        print(f"  ✓ Script déjà présent")
        continue

    # Trouver la ligne avec i18n.js et ajouter notre script juste après
    search_pattern = '<script src="../../../js/i18n.js"></script>'

    if search_pattern in content:
        # Ajouter notre script juste après i18n.js
        new_line = f'<script src="../../../js/i18n.js"></script>\n{script_tag}'
        content = content.replace(search_pattern, new_line)

        # Sauvegarder
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"  ✅ Script ajouté")
    else:
        print(f"  ❌ Pattern i18n.js non trouvé")

    print()

print()
print("=" * 80)
print("✅ TOUS LES SCRIPTS ONT ÉTÉ AJOUTÉS!")
print("=" * 80)
