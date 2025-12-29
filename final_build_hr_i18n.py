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

# Extraire TOUTES les traductions de i18n.js par langue et clé
i18n_data = {lang: {} for lang in languages}
current_lang = None

for line in lines:
    # Détecter changement de langue
    for lang in languages:
        if re.match(rf'^\s*{lang}:\s*{{', line):
            current_lang = lang
            break

    # Extraire toutes les clés review.*
    if current_lang:
        pattern = rf'"(review\.[^"]+)":\s*"((?:[^"\\]|\\.)*)"'
        match = re.search(pattern, line)
        if match:
            key = match.group(1)
            value = match.group(2)
            i18n_data[current_lang][key] = value

print(f"✅ {sum(len(i18n_data[lang]) for lang in languages)} traductions chargées")

for tool in tools:
    tool_var = tool.replace('-', '')
    tool_name = tool.replace('-', ' ').title()
    print(f'\n🔍 {tool_name}...')

    # Charger le contenu anglais du HTML (source de vérité)
    json_path = f'GenuisNet.ai/pages/reviews/hr/{tool}-content-en.json'
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            en_content = json.load(f)
    except:
        print(f'  ❌ Pas de JSON')
        continue

    # Construire les traductions pour chaque langue
    translations = {}
    for lang in languages:
        translations[lang] = {}
        for key in en_content.keys():
            # Chercher la traduction dans i18n.js
            if key in i18n_data[lang]:
                translations[lang][key] = i18n_data[lang][key]
            else:
                # Utiliser l'anglais comme fallback
                translations[lang][key] = en_content[key]

    # Générer le fichier
    output_lines = [f'// {tool_name.upper()} I18N']
    output_lines.append(f'const {tool_var}Translations = {{')

    for lang in languages:
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

    # Stats
    en_keys = len(translations['en'])
    translated = sum(1 for lang in languages if lang != 'en' for key in translations[lang] if translations[lang][key] != en_content.get(key))
    total_keys = en_keys * len(languages)

    print(f'  ✓ {en_keys} clés, {total_keys} total')
    print(f'  📊 {translated}/{total_keys - en_keys} traductions trouvées ({100*translated/(total_keys-en_keys):.0f}%)')

print(f'\n✅ Tous les fichiers générés!')
