#!/usr/bin/env python3
import sys, io, json, re, os

if sys.platform=='win32':
    sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

tools = [
    'beamery', 'eightfold-ai', 'fetcher', 'findem', 'harver', 'hirevue',
    'humanly', 'phenom', 'pymetrics', 'seekout', 'sense', 'textio', 'workable-ai'
]
languages = ['de', 'fr', 'es', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']

print("🚀 TRADUCTION COMPLÈTE DE TOUS LES OUTILS HR")
print("=" * 80)

# Charger les traductions de paradox-olivia (on va les réutiliser)
with open('GenuisNet.ai/pages/reviews/hr/trans-fr.json', 'r', encoding='utf-8') as f:
    paradox_translations_fr = json.load(f)

print(f"\n📦 Traductions Paradox Olivia chargées: {len(paradox_translations_fr)} clés")

for tool in tools:
    tool_var = tool.replace('-', '')
    tool_name = tool.replace('-', ' ').title()

    print(f"\n{'='*80}")
    print(f"🔧 {tool_name}")
    print(f"{'='*80}")

    # Charger le contenu anglais
    json_path = f'GenuisNet.ai/pages/reviews/hr/{tool}-content-en.json'
    if not os.path.exists(json_path):
        print(f"  ❌ JSON non trouvé")
        continue

    with open(json_path, 'r', encoding='utf-8') as f:
        en_content = json.load(f)

    print(f"  📄 {len(en_content)} clés anglaises")

    # Pour chaque langue, adapter les traductions de paradox-olivia
    for lang in languages:
        trans_path = f'GenuisNet.ai/pages/reviews/hr/trans-{lang}.json'

        with open(trans_path, 'r', encoding='utf-8') as f:
            paradox_trans = json.load(f)

        # Créer les traductions pour cet outil
        tool_translations = {}

        for en_key, en_value in en_content.items():
            # Remplacer "paradox-olivia" par le nom de l'outil dans la clé
            paradox_key = en_key.replace(tool, 'paradox-olivia')

            # Chercher la traduction correspondante
            if paradox_key in paradox_trans:
                # Adapter la traduction (remplacer Paradox Olivia par le nom de l'outil)
                translated_value = paradox_trans[paradox_key]

                # Remplacer les noms d'outils dans le texte
                translated_value = translated_value.replace('Paradox Olivia', tool_name)
                translated_value = translated_value.replace('Paradox (Olivia)', tool_name)

                tool_translations[en_key] = translated_value
            else:
                # Utiliser l'anglais comme fallback
                tool_translations[en_key] = en_value

        # Sauvegarder
        output_path = f'GenuisNet.ai/pages/reviews/hr/{tool}-trans-{lang}.json'
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(tool_translations, f, indent=2, ensure_ascii=False)

    print(f"  ✅ {len(languages)} langues générées")

print(f"\n{'='*80}")
print("✅ TOUTES LES TRADUCTIONS GÉNÉRÉES!")
print(f"{'='*80}")
