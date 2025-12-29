#!/usr/bin/env python3
import sys, io, json, re

if sys.platform=='win32':
    sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

print("📝 AJOUT DES TRADUCTIONS DES TITRES")
print("=" * 100)

tools = [
    'beamery', 'eightfold-ai', 'fetcher', 'findem', 'harver', 'hirevue',
    'humanly', 'paradox-olivia', 'phenom', 'pymetrics', 'seekout', 'sense',
    'textio', 'workable-ai'
]

# Traductions de référence
reference_translations = {
    'en': {
        'hero.title': '{tool} Review',
        'hero.subtitle': 'AI-Powered Hr Solution',
        'hero.badge': 'Top Choice 2026',
        'hero.updated': 'Updated',
        'hero.ai-powered': 'AI-Powered',
        'feature.ai-powered-automation': 'AI-Powered Automation',
        'feature.advanced-analytics': 'Advanced Analytics',
        'feature.seamless-integrations': 'Seamless Integrations',
        'feature.enterprise-security': 'Enterprise Security',
        'feature.real-time-collaboration': 'Real-Time Collaboration',
        'feature.mobile-first-design': 'Mobile-First Design',
    },
    'de': {
        'hero.title': '{tool} Bewertung',
        'hero.subtitle': 'KI-gestützte HR-Lösung',
        'hero.badge': 'Top-Wahl 2026',
        'hero.updated': 'Aktualisiert',
        'hero.ai-powered': 'KI-gestützt',
        'feature.ai-powered-automation': 'KI-gestützte Automatisierung',
        'feature.advanced-analytics': 'Erweiterte Analysen',
        'feature.seamless-integrations': 'Nahtlose Integrationen',
        'feature.enterprise-security': 'Unternehmenssicherheit',
        'feature.real-time-collaboration': 'Echtzeit-Zusammenarbeit',
        'feature.mobile-first-design': 'Mobile-First Design',
    },
    'fr': {
        'hero.title': 'Avis {tool}',
        'hero.subtitle': 'Solution RH basée sur l\'IA',
        'hero.badge': 'Meilleur Choix 2026',
        'hero.updated': 'Mis à jour',
        'hero.ai-powered': 'Propulsé par l\'IA',
        'feature.ai-powered-automation': 'Automatisation Intelligente',
        'feature.advanced-analytics': 'Analyses Avancées',
        'feature.seamless-integrations': 'Intégrations Transparentes',
        'feature.enterprise-security': 'Sécurité Entreprise',
        'feature.real-time-collaboration': 'Collaboration Temps Réel',
        'feature.mobile-first-design': 'Design Mobile-First',
    },
    'es': {
        'hero.title': 'Revisión de {tool}',
        'hero.subtitle': 'Solución de RRHH con IA',
        'hero.badge': 'Mejor Opción 2026',
        'hero.updated': 'Actualizado',
        'hero.ai-powered': 'Impulsado por IA',
        'feature.ai-powered-automation': 'Automatización Inteligente',
        'feature.advanced-analytics': 'Análisis Avanzados',
        'feature.seamless-integrations': 'Integraciones Perfectas',
        'feature.enterprise-security': 'Seguridad Empresarial',
        'feature.real-time-collaboration': 'Colaboración en Tiempo Real',
        'feature.mobile-first-design': 'Diseño Mobile-First',
    },
    'pt': {
        'hero.title': 'Avaliação {tool}',
        'hero.subtitle': 'Solução de RH com IA',
        'hero.badge': 'Melhor Escolha 2026',
        'hero.updated': 'Atualizado',
        'hero.ai-powered': 'Alimentado por IA',
        'feature.ai-powered-automation': 'Automação Inteligente',
        'feature.advanced-analytics': 'Análises Avançadas',
        'feature.seamless-integrations': 'Integrações Perfeitas',
        'feature.enterprise-security': 'Segurança Empresarial',
        'feature.real-time-collaboration': 'Colaboração em Tempo Real',
        'feature.mobile-first-design': 'Design Mobile-First',
    },
    'zh': {
        'hero.title': '{tool} 评测',
        'hero.subtitle': 'AI 驱动的人力资源解决方案',
        'hero.badge': '2026 年最佳选择',
        'hero.updated': '更新时间',
        'hero.ai-powered': 'AI 驱动',
        'feature.ai-powered-automation': 'AI 自动化',
        'feature.advanced-analytics': '高级分析',
        'feature.seamless-integrations': '无缝集成',
        'feature.enterprise-security': '企业级安全',
        'feature.real-time-collaboration': '实时协作',
        'feature.mobile-first-design': '移动优先设计',
    },
    'ja': {
        'hero.title': '{tool} レビュー',
        'hero.subtitle': 'AI搭載のHRソリューション',
        'hero.badge': '2026年トップチョイス',
        'hero.updated': '更新日',
        'hero.ai-powered': 'AI搭載',
        'feature.ai-powered-automation': 'AI自動化',
        'feature.advanced-analytics': '高度な分析',
        'feature.seamless-integrations': 'シームレスな統合',
        'feature.enterprise-security': 'エンタープライズセキュリティ',
        'feature.real-time-collaboration': 'リアルタイムコラボレーション',
        'feature.mobile-first-design': 'モバイルファーストデザイン',
    },
    'ko': {
        'hero.title': '{tool} 리뷰',
        'hero.subtitle': 'AI 기반 HR 솔루션',
        'hero.badge': '2026년 최고의 선택',
        'hero.updated': '업데이트됨',
        'hero.ai-powered': 'AI 기반',
        'feature.ai-powered-automation': 'AI 자동화',
        'feature.advanced-analytics': '고급 분석',
        'feature.seamless-integrations': '완벽한 통합',
        'feature.enterprise-security': '엔터프라이즈 보안',
        'feature.real-time-collaboration': '실시간 협업',
        'feature.mobile-first-design': '모바일 우선 디자인',
    },
    'ar': {
        'hero.title': 'مراجعة {tool}',
        'hero.subtitle': 'حل موارد بشرية مدعوم بالذكاء الاصطناعي',
        'hero.badge': 'الخيار الأفضل 2026',
        'hero.updated': 'تم التحديث',
        'hero.ai-powered': 'مدعوم بالذكاء الاصطناعي',
        'feature.ai-powered-automation': 'الأتمتة الذكية',
        'feature.advanced-analytics': 'تحليلات متقدمة',
        'feature.seamless-integrations': 'تكاملات سلسة',
        'feature.enterprise-security': 'أمان المؤسسات',
        'feature.real-time-collaboration': 'التعاون في الوقت الفعلي',
        'feature.mobile-first-design': 'تصميم الجوال أولاً',
    },
    'hi': {
        'hero.title': '{tool} समीक्षा',
        'hero.subtitle': 'AI-संचालित HR समाधान',
        'hero.badge': '2026 की शीर्ष पसंद',
        'hero.updated': 'अपडेट किया गया',
        'hero.ai-powered': 'AI-संचालित',
        'feature.ai-powered-automation': 'AI स्वचालन',
        'feature.advanced-analytics': 'उन्नत विश्लेषण',
        'feature.seamless-integrations': 'सहज एकीकरण',
        'feature.enterprise-security': 'एंटरप्राइज़ सुरक्षा',
        'feature.real-time-collaboration': 'वास्तविक समय सहयोग',
        'feature.mobile-first-design': 'मोबाइल-प्रथम डिज़ाइन',
    },
}

languages = ['en', 'de', 'fr', 'es', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']

for tool in tools:
    tool_var = tool.replace('-', '')
    tool_display = tool.replace('-', ' ').title()
    i18n_path = f'GenuisNet.ai/js/{tool}-i18n.js'

    print(f"\n🔧 {tool}...")

    # Lire le fichier i18n existant
    with open(i18n_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extraire les traductions actuelles
    current_translations = {}

    for lang in languages:
        current_translations[lang] = {}

        # Trouver la section de langue
        lang_section_pattern = rf'  "{lang}": {{\n(.*?)\n  }}'
        match = re.search(lang_section_pattern, content, re.DOTALL)

        if match:
            section = match.group(1)

            # Extraire toutes les clés
            for line in section.split('\n'):
                key_match = re.match(r'\s+"([^"]+)":\s+"((?:[^"\\\\]|\\\\.)*)",?', line)
                if key_match:
                    key = key_match.group(1)
                    value = key_match.group(2)
                    current_translations[lang][key] = value

        # Ajouter les nouvelles traductions
        for short_key, translation in reference_translations[lang].items():
            full_key = f'review.{tool}.{short_key}'
            if full_key not in current_translations[lang]:
                # Remplacer {tool} par le nom de l'outil
                translated = translation.replace('{tool}', tool_display)
                current_translations[lang][full_key] = translated

    # Générer le nouveau fichier
    output_lines = []

    # Trouver où commence l'objet de traductions
    const_match = re.search(rf'const {tool_var}Translations = {{', content)
    if const_match:
        # Ajouter tout avant l'objet de traductions
        output_lines.append(content[:const_match.end()])
        output_lines.append('')

        # Ajouter les traductions
        for lang in languages:
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

        # Ajouter le code d'application (après l'objet)
        function_match = re.search(r'\n\nfunction get', content, re.DOTALL)
        if function_match:
            output_lines.append(content[function_match.start():])

        # Sauvegarder
        with open(i18n_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(output_lines))

        total = sum(len(current_translations[lang]) for lang in languages)
        print(f"  ✅ {total} traductions (incluant 110 nouvelles)")

print(f"\n{'='*100}")
print("✅ TOUTES LES TRADUCTIONS DES TITRES AJOUTÉES!")
print(f"{'='*100}")
