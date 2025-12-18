#!/usr/bin/env python3
"""
Copier les titres communs de i18n.js vers tous les fichiers *-i18n.js
"""
import json
import re

print("=" * 80)
print("📋 COPIE DES TITRES COMMUNS")
print("=" * 80)
print()

# Lire i18n.js et extraire les clés review.common.*
print("📥 Extraction des clés communes de i18n.js...")

with open('GenuisNet.ai/js/i18n.js', 'r', encoding='utf-8') as f:
    i18n_content = f.read()

# Langues à extraire
languages = ['en', 'es', 'fr', 'de', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']

# Extraire les clés review.common.* pour chaque langue
common_translations = {}

for lang in languages:
    common_translations[lang] = {}

    # Pattern pour trouver la section de langue
    lang_pattern = rf'{lang}:\s*\{{([^}}]+(?:\}}[^}}]+)*?)"review\.common\.'

    # Trouver toutes les clés review.common.* dans cette langue
    pattern = r'"(review\.common\.[^"]+)":\s*"([^"]+)"'

    for match in re.finditer(pattern, i18n_content):
        key = match.group(1)
        value = match.group(2)
        # Décoder les échappements
        value = value.replace('\\\'', "'").replace('\\"', '"')
        common_translations[lang][key] = value

print(f"✅ Trouvé {len(common_translations['en'])} clés communes")
print()

# Afficher quelques exemples
print("Exemples de clés communes extraites:")
for key in list(common_translations['en'].keys())[:5]:
    print(f"  EN: {key} = {common_translations['en'][key]}")
    print(f"  ES: {key} = {common_translations['es'].get(key, 'N/A')}")
    print(f"  FR: {key} = {common_translations['fr'].get(key, 'N/A')}")
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

print("=" * 80)
print("📝 AJOUT DES TITRES AUX FICHIERS I18N")
print("=" * 80)
print()

for tool in image_tools:
    i18n_file = f'GenuisNet.ai/js/{tool}-i18n.js'

    print(f"🔧 Traitement: {tool}-i18n.js")

    # Lire le fichier
    with open(i18n_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pour chaque langue, ajouter les clés communes
    modified = False

    for lang in languages:
        # Trouver la section de cette langue dans le fichier
        # Pattern: "lang": { ... }
        lang_pattern = rf'"{lang}":\s*\{{'

        if re.search(lang_pattern, content):
            # Chercher la fin de l'objet pour cette langue
            # On va insérer juste avant le dernier }

            # Vérifier si les clés communes existent déjà
            has_common = bool(re.search(rf'"{lang}":\s*{{[^}}]*"review\.common\.', content))

            if not has_common:
                # Ajouter les clés communes
                common_keys_json = ',\n    '.join([
                    f'"{key}": "{value}"'
                    for key, value in common_translations[lang].items()
                ])

                # Trouver la section de langue et ajouter avant la fermeture
                pattern = rf'("{lang}":\s*{{)([^}}]+?)(  \}})'

                def replacer(match):
                    return f'{match.group(1)}{match.group(2)},\n    {common_keys_json}\n{match.group(3)}'

                new_content = re.sub(pattern, replacer, content, count=1)

                if new_content != content:
                    content = new_content
                    modified = True
                    print(f"  ✅ Ajouté {len(common_translations[lang])} clés communes pour {lang.upper()}")

    if modified:
        # Sauvegarder
        with open(i18n_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  💾 Fichier mis à jour")
    else:
        print(f"  ℹ️  Clés communes déjà présentes")

    print()

print("=" * 80)
print("✅ TOUS LES TITRES COMMUNS ONT ÉTÉ COPIÉS!")
print("=" * 80)
