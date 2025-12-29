#!/usr/bin/env python3
import sys, io, re, json

if sys.platform=='win32':
    sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

tools = [
    'beamery', 'eightfold-ai', 'fetcher', 'findem', 'harver', 'hirevue',
    'humanly', 'paradox-olivia', 'phenom', 'pymetrics', 'seekout', 'sense',
    'textio', 'workable-ai'
]

# Lire i18n.js
print("📖 Lecture de i18n.js...")
with open('GenuisNet.ai/js/i18n.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Extraire chaque section de langue
languages = ['en', 'de', 'fr', 'es', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']

for tool in tools:
    tool_var = tool.replace('-', '')
    translations = {}

    for lang in languages:
        translations[lang] = {}

        # Trouver la section de langue dans i18n.js
        lang_pattern = rf'{lang}:\s*{{'
        match = re.search(lang_pattern, content)

        if match:
            # Extraire tout le contenu entre { et }
            start = match.end()
            # Chercher toutes les clés pour cet outil dans cette langue
            key_pattern = rf'"review\.{re.escape(tool)}\.([^"]+)":\s*"([^"]+)"'

            # Chercher dans une fenêtre raisonnable après la langue
            lang_section = content[start:start+500000]

            for key_match in re.finditer(key_pattern, lang_section):
                full_key = f"review.{tool}.{key_match.group(1)}"
                value = key_match.group(2)
                translations[lang][full_key] = value

    # Générer le fichier i18n pour cet outil
    if translations['en']:  # Si on a trouvé des traductions
        output_lines = [f'// {tool.upper()} I18N']
        output_lines.append(f'const {tool_var}Translations = {{')

        for lang in languages:
            if translations[lang]:
                output_lines.append(f'  "{lang}": {{')
                for key, value in sorted(translations[lang].items()):
                    # Échapper les guillemets et backslashes
                    escaped_value = value.replace('\\', '\\\\').replace('"', '\\"')
                    output_lines.append(f'    "{key}": "{escaped_value}",')
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

        total_keys = sum(len(translations[lang]) for lang in languages)
        print(f'✓ {tool:20} → {total_keys} traductions ({len(translations["en"])} clés)')
    else:
        print(f'❌ {tool:20} → Aucune traduction trouvée')

print(f'\n✅ Extraction terminée depuis i18n.js!')
