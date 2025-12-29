#!/usr/bin/env python3
import sys, io, json, re

if sys.platform=='win32':
    sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

tools = [
    'beamery', 'eightfold-ai', 'fetcher', 'findem', 'harver', 'hirevue',
    'humanly', 'phenom', 'pymetrics', 'seekout', 'sense', 'textio', 'workable-ai'
]
languages = ['de', 'fr', 'es', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']

print("🔄 INTÉGRATION DE TOUTES LES TRADUCTIONS HR")
print("=" * 80)

for tool in tools:
    tool_var = tool.replace('-', '')
    tool_name = tool.replace('-', ' ').title()
    i18n_path = f'GenuisNet.ai/js/{tool}-i18n.js'

    print(f"\n🔧 {tool_name}...")

    # Charger le fichier i18n existant
    with open(i18n_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extraire les traductions actuelles
    current_translations = {}

    for lang in ['en'] + languages:
        current_translations[lang] = {}

        # Trouver la section de langue
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

    # Charger et fusionner les nouvelles traductions
    for lang in languages:
        trans_path = f'GenuisNet.ai/pages/reviews/hr/{tool}-trans-{lang}.json'
        try:
            with open(trans_path, 'r', encoding='utf-8') as f:
                updates = json.load(f)

            for key, value in updates.items():
                current_translations[lang][key] = value
        except:
            pass

    # Générer le nouveau fichier
    output_lines = [f'// {tool_name.upper()} I18N']
    output_lines.append(f'const {tool_var}Translations = {{')

    for lang in ['en'] + languages:
        if current_translations[lang]:
            output_lines.append(f'  "{lang}": {{')
            for key in sorted(current_translations[lang].keys()):
                value = current_translations[lang][key]
                output_lines.append(f'      "{key}": "{value}",')

            if output_lines[-1].endswith(','):
                output_lines[-1] = output_lines[-1][:-1]
            output_lines.append('  },')

    if output_lines[-1].endswith(','):
        output_lines[-1] = output_lines[-1][:-1]
    output_lines.append('};')

    # Sauvegarder
    with open(i18n_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_lines))

    total = sum(len(current_translations[lang]) for lang in ['en'] + languages)
    print(f"  ✅ {total} traductions totales")

print(f"\n{'='*80}")
print("✅ TOUS LES FICHIERS HR INTÉGRÉS!")
print(f"{'='*80}")
