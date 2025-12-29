#!/usr/bin/env python3
import sys, io, json

if sys.platform=='win32':
    sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

tools = ['paradox-olivia']  # Commencer avec un seul
languages = ['de', 'fr', 'es', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']

# Charger le fichier i18n existant
with open('GenuisNet.ai/js/paradox-olivia-i18n.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Charger le JSON avec toutes les clés anglaises
with open('GenuisNet.ai/pages/reviews/hr/paradox-olivia-content-en.json', 'r', encoding='utf-8') as f:
    en_content = json.load(f)

print(f"📊 Total de clés anglaises: {len(en_content)}")

# Pour chaque langue, identifier ce qui manque
missing_by_lang = {}
for lang in languages:
    missing_by_lang[lang] = {}

    for key, en_value in en_content.items():
        # Chercher si cette clé existe avec une traduction différente de l'anglais
        pattern = f'"{key}": "{en_value}"'

        # Si on trouve exactement le texte anglais, c'est qu'il n'est pas traduit
        if pattern in content:
            # Vérifier si c'est dans la section de cette langue
            lang_section_start = content.find(f'"{lang}": {{')
            if lang_section_start > -1:
                lang_section_end = content.find('  },', lang_section_start)
                lang_section = content[lang_section_start:lang_section_end]

                if pattern in lang_section:
                    missing_by_lang[lang][key] = en_value

# Afficher les stats
print(f"\n📋 Traductions manquantes par langue:")
for lang in languages:
    count = len(missing_by_lang[lang])
    percent = 100 * count / len(en_content)
    print(f"  {lang}: {count}/{len(en_content)} ({percent:.0f}%)")

# Sauvegarder pour traduction
for lang in languages:
    if missing_by_lang[lang]:
        output = {
            'source_lang': 'en',
            'target_lang': lang,
            'tool': 'paradox-olivia',
            'translations': missing_by_lang[lang]
        }

        with open(f'GenuisNet.ai/pages/reviews/hr/missing-{lang}.json', 'w', encoding='utf-8') as f:
            json.dump(output, f, indent=2, ensure_ascii=False)

print(f"\n✅ Fichiers de traduction créés!")
