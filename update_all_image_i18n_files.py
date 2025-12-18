#!/usr/bin/env python3
"""
Mettre à jour tous les fichiers *-i18n.js avec les nouvelles traductions
"""
import json
import os

print("=" * 80)
print("🔄 MISE À JOUR DES FICHIERS I18N")
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

# Langues
languages = ['es', 'fr', 'de', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']

# Charger toutes les traductions
print("📥 Chargement des traductions...")
all_translations = {}
for lang in languages:
    try:
        with open(f'all_full_translations_{lang}.json', 'r', encoding='utf-8') as f:
            all_translations[lang] = json.load(f)
        print(f"  ✓ {lang.upper()}: {len(all_translations[lang])} clés")
    except FileNotFoundError:
        print(f"  ❌ {lang.upper()}: Fichier non trouvé")
        all_translations[lang] = {}

print()

# Pour chaque outil
for tool in image_tools:
    print(f"🔧 Mise à jour: {tool}-i18n.js")

    i18n_file = f'GenuisNet.ai/js/{tool}-i18n.js'

    if not os.path.exists(i18n_file):
        print(f"  ⚠️  Fichier non trouvé")
        continue

    # Lire le fichier actuel
    with open(i18n_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extraire l'objet JavaScript translations
    # Trouver const xxxTranslations = { ... };
    import re

    # Trouver le nom de la variable
    var_match = re.search(r'const (\w+Translations) = ', content)
    if not var_match:
        print(f"  ❌ Variable translations non trouvée")
        continue

    var_name = var_match.group(1)

    # Construire le nouvel objet translations
    # IMPORTANT: Ne PAS remplacer les tirets car les clés utilisent des tirets!
    prefix = f'review.{tool}.'

    tool_translations = {'en': {}}

    # Charger l'anglais
    en_file = f'{tool.replace("-", "_")}_contents_only.json'
    if os.path.exists(en_file):
        with open(en_file, 'r', encoding='utf-8') as f:
            tool_translations['en'] = json.load(f)

    # Charger les autres langues
    for lang in languages:
        if lang not in all_translations:
            continue

        # Filtrer les clés de cet outil
        tool_keys = {k: v for k, v in all_translations[lang].items() if k.startswith(prefix)}
        tool_translations[lang] = tool_keys

    # Remplacer l'objet dans le fichier
    # Pattern: const xxxTranslations = { ... };
    pattern = rf'const {var_name} = {{.*?}};'

    new_obj = f'const {var_name} = {json.dumps(tool_translations, ensure_ascii=False, indent=2)};'

    new_content = re.sub(pattern, new_obj, content, flags=re.DOTALL)

    if new_content == content:
        print(f"  ⚠️  Aucun changement détecté")
    else:
        # Sauvegarder
        with open(i18n_file, 'w', encoding='utf-8') as f:
            f.write(new_content)

        # Compter les clés par langue
        for lang in ['en'] + languages:
            count = len(tool_translations.get(lang, {}))
            if count > 0:
                print(f"    {lang.upper()}: {count} clés")

        print(f"  ✅ Fichier mis à jour")

    print()

print()
print("=" * 80)
print("✅ TOUS LES FICHIERS I18N ONT ÉTÉ MIS À JOUR!")
print("=" * 80)
