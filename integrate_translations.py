#!/usr/bin/env python3
import sys, io, json, re

if sys.platform=='win32':
    sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

tool = 'paradox-olivia'
tool_var = tool.replace('-', '')
languages = ['de', 'fr', 'es', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']

print(f"🔄 Intégration des traductions pour {tool}...")

# Charger le fichier i18n existant
i18n_path = f'GenuisNet.ai/js/{tool}-i18n.js'
with open(i18n_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Pour chaque langue, charger les nouvelles traductions
updates = {}
for lang in languages:
    trans_path = f'GenuisNet.ai/pages/reviews/hr/trans-{lang}.json'
    try:
        with open(trans_path, 'r', encoding='utf-8') as f:
            updates[lang] = json.load(f)
        print(f"  ✓ {lang}: {len(updates[lang])} nouvelles traductions")
    except FileNotFoundError:
        print(f"  ⚠️  {lang}: fichier non trouvé")
        updates[lang] = {}

# Extraire les traductions actuelles du fichier JS
current_translations = {}

for lang in ['en'] + languages:
    current_translations[lang] = {}

    # Pattern pour trouver la section de langue
    lang_section_pattern = rf'  "{lang}": {{\n(.*?)\n  }}'
    match = re.search(lang_section_pattern, content, re.DOTALL)

    if match:
        section = match.group(1)

        # Extraire toutes les clés
        for line in section.split('\n'):
            key_match = re.match(r'\s+"([^"]+)":\s+"((?:[^"\\]|\\.)*)",?', line)
            if key_match:
                key = key_match.group(1)
                value = key_match.group(2)
                current_translations[lang][key] = value

print(f"\n📊 Traductions actuelles:")
for lang in ['en'] + languages:
    print(f"  {lang}: {len(current_translations[lang])} clés")

# Fusionner les nouvelles traductions
for lang in languages:
    for key, value in updates[lang].items():
        current_translations[lang][key] = value

# Générer le nouveau fichier
output_lines = [f'// {tool.upper().replace("-", " ")} I18N']
output_lines.append(f'const {tool_var}Translations = {{')

for lang in ['en'] + languages:
    if current_translations[lang]:
        output_lines.append(f'  "{lang}": {{')
        for key in sorted(current_translations[lang].keys()):
            value = current_translations[lang][key]
            output_lines.append(f'      "{key}": "{value}",')

        # Enlever la dernière virgule
        if output_lines[-1].endswith(','):
            output_lines[-1] = output_lines[-1][:-1]
        output_lines.append('  },')

# Enlever la dernière virgule
if output_lines[-1].endswith(','):
    output_lines[-1] = output_lines[-1][:-1]
output_lines.append('};')

# Sauvegarder
with open(i18n_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(output_lines))

# Stats finales
print(f"\n✅ Traductions finales:")
for lang in ['en'] + languages:
    count = len(current_translations[lang])
    print(f"  {lang}: {count} clés")

total = sum(len(current_translations[lang]) for lang in ['en'] + languages)
print(f"\n🎉 Fichier mis à jour: {total} traductions totales!")
