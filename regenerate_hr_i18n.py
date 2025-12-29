#!/usr/bin/env python3
import sys, io, re
if sys.platform=='win32':
    sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

# Liste des outils HR
hr_tools = [
    ('beamery', 'Beamery'),
    ('eightfold-ai', 'Eightfold AI'),
    ('fetcher', 'Fetcher'),
    ('findem', 'Findem'),
    ('harver', 'Harver'),
    ('hirevue', 'HireVue'),
    ('humanly', 'Humanly'),
    ('paradox-olivia', 'Paradox Olivia'),
    ('phenom', 'Phenom'),
    ('pymetrics', 'Pymetrics'),
    ('seekout', 'SeekOut'),
    ('sense', 'Sense'),
    ('textio', 'Textio'),
    ('workable-ai', 'Workable AI')
]

# Lire le template Ada (Customer Service qui fonctionne)
with open('GenuisNet.ai/js/ada-i18n.js', 'r', encoding='utf-8') as f:
    template = f.read()

# Régénérer chaque fichier HR
for tool_slug, tool_name in hr_tools:
    content = template

    # Remplacer les références Ada par le nom de l'outil HR
    var_name = tool_slug.replace('-', '')

    # Remplacer le nom de variable JavaScript
    content = re.sub(r'const adaTranslations\s*=', f'const {var_name}Translations =', content)

    # Remplacer toutes les clés de traduction
    content = re.sub(r'"review\.ada\.', f'"review.{tool_slug}.', content)
    content = re.sub(r'review\.ada\.', f'review.{tool_slug}.', content)

    # Remplacer le nom de l'outil dans le contenu
    content = re.sub(r'\bAda\b', tool_name, content)
    content = re.sub(r'\bada\b', tool_slug, content, flags=re.IGNORECASE)

    # Remplacer "customer service" par "HR recruiting"
    content = re.sub(r'customer service', 'HR recruiting', content, flags=re.IGNORECASE)
    content = re.sub(r'Customer Service', 'HR Recruiting', content)
    content = re.sub(r'service client', 'recrutement RH', content, flags=re.IGNORECASE)
    content = re.sub(r'atención al cliente', 'reclutamiento de RRHH', content, flags=re.IGNORECASE)
    content = re.sub(r'atendimento ao cliente', 'recrutamento de RH', content, flags=re.IGNORECASE)
    content = re.sub(r'客户服务', '人力资源招聘', content)
    content = re.sub(r'カスタマーサービス', '人事採用', content)
    content = re.sub(r'고객 서비스', 'HR 채용', content)
    content = re.sub(r'خدمة العملاء', 'توظيف الموارد البشرية', content)
    content = re.sub(r'ग्राहक सेवा', 'एचआर भर्ती', content)

    # Sauvegarder
    output_path = f'GenuisNet.ai/js/{tool_slug}-i18n.js'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f'✓ {tool_name:20} → {tool_slug}-i18n.js')

print(f'\n✅ Tous les {len(hr_tools)} fichiers HR régénérés!')
print('📦 Basés sur le template Ada (103K)')
