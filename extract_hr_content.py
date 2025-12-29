#!/usr/bin/env python3
import sys, io, re
from bs4 import BeautifulSoup

if sys.platform=='win32':
    sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

# Outils HR
tools = [
    'beamery', 'eightfold-ai', 'fetcher', 'findem', 'harver', 'hirevue',
    'humanly', 'paradox-olivia', 'phenom', 'pymetrics', 'seekout', 'sense',
    'textio', 'workable-ai'
]

# Extraire le contenu anglais de chaque HTML
for tool in tools:
    html_path = f'GenuisNet.ai/pages/reviews/hr/{tool}.html'

    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')

        # Trouver tous les éléments avec data-i18n
        elements = soup.find_all(attrs={'data-i18n': re.compile(f'review\\.{tool}\\.')})

        # Extraire clés et texte
        content = {}
        for elem in elements:
            key = elem.get('data-i18n')
            text = elem.get_text(strip=True)
            if text:
                content[key] = text

        # Sauvegarder en JSON
        import json
        output = f'GenuisNet.ai/pages/reviews/hr/{tool}-content-en.json'
        with open(output, 'w', encoding='utf-8') as f:
            json.dump(content, f, indent=2, ensure_ascii=False)

        print(f'✓ {tool:20} → {len(content)} clés extraites')

    except Exception as e:
        print(f'❌ {tool}: {e}')

print(f'\n✅ Extraction terminée!')
