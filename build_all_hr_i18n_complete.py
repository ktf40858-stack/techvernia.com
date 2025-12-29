#!/usr/bin/env python3
import sys, io, re, json

if sys.platform=='win32':
    sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

tools = [
    'beamery', 'eightfold-ai', 'fetcher', 'findem', 'harver', 'hirevue',
    'humanly', 'paradox-olivia', 'phenom', 'pymetrics', 'seekout', 'sense',
    'textio', 'workable-ai'
]
languages = ['en', 'de', 'fr', 'es', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']

print("📖 Lecture de i18n.js...")
with open('GenuisNet.ai/js/i18n.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for tool in tools:
    tool_var = tool.replace('-', '')
    tool_name = tool.replace('-', ' ').title()
    print(f'\n🔍 {tool_name}...')

    # Charger le contenu anglais extrait
    json_path = f'GenuisNet.ai/pages/reviews/hr/{tool}-content-en.json'
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            en_content = json.load(f)
    except:
        print(f'  ❌ Pas de JSON trouvé')
        continue

    # Extraire de i18n.js
    translations = {lang: {} for lang in languages}
    current_lang = None

    for i, line in enumerate(lines):
        # Détecter changement de langue
        for lang in languages:
            if re.match(rf'^\s*{lang}:\s*{{', line):
                current_lang = lang
                break

        # Extraire les clés
        if current_lang:
            pattern = rf'"(review\.{re.escape(tool)}\.[^"]+)":\s*"((?:[^"\\]|\\.)*)"'
            match = re.search(pattern, line)
            if match:
                key = match.group(1)
                value = match.group(2)
                translations[current_lang][key] = value

    # Ajouter les clés anglaises manquantes
    for key, value in en_content.items():
        if key not in translations['en']:
            translations['en'][key] = value

    # Pour les clés manquantes dans les autres langues, utiliser l'anglais (temporaire)
    all_keys = set(en_content.keys())
    for lang in languages:
        if lang != 'en':
            for key in all_keys:
                if key not in translations[lang]:
                    # Utiliser la traduction anglaise comme fallback
                    translations[lang][key] = en_content[key]

    # Générer le fichier
    output_lines = [f'// {tool_name.upper()} I18N']
    output_lines.append(f'const {tool_var}Translations = {{')

    for lang in languages:
        if translations[lang]:
            output_lines.append(f'  "{lang}": {{')
            for key in sorted(translations[lang].keys()):
                value = translations[lang][key]
                output_lines.append(f'      "{key}": "{value}",')
            if output_lines[-1].endswith(','):
                output_lines[-1] = output_lines[-1][:-1]
            output_lines.append('  },')

    if output_lines[-1].endswith(','):
        output_lines[-1] = output_lines[-1][:-1]
    output_lines.append('};')

    # Sauvegarder
    output_path = f'GenuisNet.ai/js/{tool}-i18n.js'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_lines))

    total = sum(len(translations[lang]) for lang in languages)
    print(f'  ✓ {total} traductions ({len(translations["en"])} clés)')

print(f'\n✅ Tous les fichiers HR générés!')
