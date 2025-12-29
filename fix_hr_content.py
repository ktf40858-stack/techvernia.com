#!/usr/bin/env python3
import sys, io, re
if sys.platform=='win32':
    sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

# Liste des outils HR
hr_tools = [
    'beamery', 'eightfold-ai', 'fetcher', 'findem', 'harver', 'hirevue',
    'humanly', 'paradox-olivia', 'phenom', 'pymetrics', 'seekout', 'sense',
    'textio', 'workable-ai'
]

replacements = {
    # English
    'customer-service platform': 'HR recruiting platform',
    'customer service platform': 'HR recruiting platform',
    'customer-service solutions': 'HR recruiting solutions',
    'customer service solutions': 'HR recruiting solutions',
    'customer-service needs': 'HR recruiting needs',
    'customer service needs': 'HR recruiting needs',
    'customer support': 'talent acquisition',
    'support customers': 'recruit talent',
    'help customers': 'recruit candidates',

    # French
    'plateforme de service client': 'plateforme de recrutement RH',
    'service client': 'recrutement RH',
    'solutions de service client': 'solutions de recrutement RH',
    'besoins de service client': 'besoins en recrutement RH',

    # Spanish
    'plataforma de atención al cliente': 'plataforma de reclutamiento de RRHH',
    'plataforma de servicio al cliente': 'plataforma de reclutamiento de RRHH',
    'atención al cliente': 'reclutamiento de RRHH',
    'servicio al cliente': 'reclutamiento de RRHH',

    # Portuguese
    'plataforma de atendimento ao cliente': 'plataforma de recrutamento de RH',
    'atendimento ao cliente': 'recrutamento de RH',

    # German
    'Kundenservice-Plattform': 'HR-Rekrutierungsplattform',
    'Kundenservice': 'HR-Rekrutierung',
    'Kundensupport': 'Talentakquise',

    # Chinese
    '客户服务平台': '人力资源招聘平台',
    '客户服务': '人力资源招聘',
    '客户支持': '人才招聘',

    # Japanese
    'カスタマーサービスプラットフォーム': '人事採用プラットフォーム',
    'カスタマーサービス': '人事採用',
    'カスタマーサポート': '人材獲得',

    # Korean
    '고객 서비스 플랫폼': 'HR 채용 플랫폼',
    '고객 서비스': 'HR 채용',
    '고객 지원': '인재 확보',

    # Arabic
    'منصة خدمة العملاء': 'منصة توظيف الموارد البشرية',
    'خدمة العملاء': 'توظيف الموارد البشرية',
    'دعم العملاء': 'اكتساب المواهب',

    # Hindi
    'ग्राहक सेवा मंच': 'एचआर भर्ती मंच',
    'ग्राहक सेवा': 'एचआर भर्ती',
    'ग्राहक सहायता': 'प्रतिभा अधिग्रहण'
}

for tool in hr_tools:
    filepath = f'GenuisNet.ai/js/{tool}-i18n.js'

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Appliquer tous les remplacements
    for old, new in replacements.items():
        content = content.replace(old, new)

    # Sauvegarder
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f'✓ {tool}')

print(f'\n✅ Contenu HR corrigé pour les {len(hr_tools)} outils!')
