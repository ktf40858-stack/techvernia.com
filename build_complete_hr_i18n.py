#!/usr/bin/env python3
import sys, io, re

if sys.platform=='win32':
    sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

tools = ['paradox-olivia']  # Commencer avec un seul pour tester
languages = ['en', 'de', 'fr', 'es', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']

print("📖 Lecture de i18n.js...")
with open('GenuisNet.ai/js/i18n.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for tool in tools:
    tool_var = tool.replace('-', '')
    print(f'\n🔍 Extraction de {tool}...')

    # Structure: {langue: {clé: valeur}}
    translations = {lang: {} for lang in languages}
    current_lang = None

    # Parcourir toutes les lignes
    for i, line in enumerate(lines):
        # Détecter changement de langue
        for lang in languages:
            if re.match(rf'^\s*{lang}:\s*{{', line):
                current_lang = lang
                print(f'  → Langue détectée: {lang} (ligne {i+1})')
                break

        # Extraire les clés pour cet outil
        if current_lang:
            pattern = rf'"(review\.{re.escape(tool)}\.[^"]+)":\s*"((?:[^"\\]|\\.)*)"'
            match = re.search(pattern, line)
            if match:
                key = match.group(1)
                value = match.group(2)
                translations[current_lang][key] = value

    # Générer le fichier
    output_lines = [f'// {tool.upper().replace("-", " ")} I18N']
    output_lines.append(f'const {tool_var}Translations = {{')

    for lang in languages:
        if translations[lang]:
            output_lines.append(f'  "{lang}": {{')
            for key in sorted(translations[lang].keys()):
                value = translations[lang][key]
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
    output_path = f'GenuisNet.ai/js/{tool}-i18n.js'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_lines))

    # Statistiques
    total = sum(len(translations[lang]) for lang in languages)
    print(f'\n✅ {tool}:')
    for lang in languages:
        count = len(translations[lang])
        if count > 0:
            print(f'   {lang}: {count} clés')
    print(f'   TOTAL: {total} traductions')

print(f'\n✅ Terminé!')
