#!/usr/bin/env python3
"""
Fix remaining missing translations in Gaming category i18n files
Specifically targets the main description and key features that weren't translated
"""

import re
import os

# Additional translations that were missed
ADDITIONAL_GAMING_TRANSLATIONS = {
    # Main description (is.a.leading)
    "{TOOL} is a leading AI-powered gaming platform designed to streamline workflows and enhance productivity. Built with cutting-edge artificial intelligence technology, it delivers exceptional performance for modern businesses.": {
        "de": "{TOOL} ist eine führende KI-gestützte Gaming-Plattform, die entwickelt wurde, um Arbeitsabläufe zu optimieren und die Produktivität zu steigern. Mit modernster künstlicher Intelligenz-Technologie bietet sie außergewöhnliche Leistung für moderne Unternehmen.",
        "fr": "{TOOL} est une plateforme de gaming alimentée par l'IA, conçue pour rationaliser les flux de travail et améliorer la productivité. Construite avec une technologie d'intelligence artificielle de pointe, elle offre des performances exceptionnelles pour les entreprises modernes.",
        "es": "{TOOL} es una plataforma de gaming impulsada por IA diseñada para optimizar flujos de trabajo y mejorar la productividad. Construida con tecnología de inteligencia artificial de vanguardia, ofrece un rendimiento excepcional para empresas modernas.",
        "pt": "{TOOL} é uma plataforma de gaming alimentada por IA projetada para otimizar fluxos de trabalho e melhorar a produtividade. Construída com tecnologia de inteligência artificial de ponta, oferece desempenho excepcional para empresas modernas.",
        "zh": "{TOOL} 是一个领先的AI驱动游戏平台，旨在简化工作流程并提高生产力。采用尖端人工智能技术构建，为现代企业提供卓越性能。",
        "ja": "{TOOL}は、ワークフローを合理化し生産性を向上させるために設計された、AI駆動の主要なゲーミングプラットフォームです。最先端の人工知能技術で構築され、現代のビジネスに卓越したパフォーマンスを提供します。",
        "ko": "{TOOL}는 워크플로우를 간소화하고 생산성을 향상시키기 위해 설계된 선도적인 AI 기반 게이밍 플랫폼입니다. 최첨단 인공지능 기술로 구축되어 현대 비즈니스를 위한 탁월한 성능을 제공합니다.",
        "ar": "{TOOL} هي منصة ألعاب رائدة مدعومة بالذكاء الاصطناعي مصممة لتبسيط سير العمل وتعزيز الإنتاجية. مبنية بتكنولوجيا ذكاء اصطناعي متطورة، توفر أداءً استثنائيًا للشركات الحديثة.",
        "hi": "{TOOL} एक अग्रणी AI-संचालित गेमिंग प्लेटफ़ॉर्म है जो कार्यप्रवाह को सुव्यवस्थित करने और उत्पादकता बढ़ाने के लिए डिज़ाइन किया गया है। अत्याधुनिक कृत्रिम बुद्धिमत्ता तकनीक से निर्मित, यह आधुनिक व्यवसायों के लिए असाधारण प्रदर्शन प्रदान करता है।"
    },

    # Platform leverages
    "The platform leverages advanced machine learning algorithms to automate complex tasks, provide intelligent insights, and enable teams to work more efficiently. With seamless integrations and an intuitive interface, {TOOL} has become a trusted solution for organizations worldwide.": {
        "de": "Die Plattform nutzt fortschrittliche Machine-Learning-Algorithmen, um komplexe Aufgaben zu automatisieren, intelligente Einblicke zu bieten und Teams zu ermöglichen, effizienter zu arbeiten. Mit nahtlosen Integrationen und einer intuitiven Benutzeroberfläche ist {TOOL} zu einer vertrauenswürdigen Lösung für Organisationen weltweit geworden.",
        "fr": "La plateforme exploite des algorithmes d'apprentissage automatique avancés pour automatiser les tâches complexes, fournir des insights intelligents et permettre aux équipes de travailler plus efficacement. Avec des intégrations transparentes et une interface intuitive, {TOOL} est devenu une solution de confiance pour les organisations du monde entier.",
        "es": "La plataforma aprovecha algoritmos avanzados de aprendizaje automático para automatizar tareas complejas, proporcionar insights inteligentes y permitir que los equipos trabajen de manera más eficiente. Con integraciones perfectas y una interfaz intuitiva, {TOOL} se ha convertido en una solución confiable para organizaciones en todo el mundo.",
        "pt": "A plataforma aproveita algoritmos avançados de aprendizado de máquina para automatizar tarefas complexas, fornecer insights inteligentes e permitir que as equipes trabalhem com mais eficiência. Com integrações perfeitas e uma interface intuitiva, {TOOL} tornou-se uma solução confiável para organizações em todo o mundo.",
        "zh": "该平台利用先进的机器学习算法来自动化复杂任务，提供智能洞察，并使团队能够更高效地工作。凭借无缝集成和直观的界面，{TOOL} 已成为全球组织信赖的解决方案。",
        "ja": "このプラットフォームは高度な機械学習アルゴリズムを活用して、複雑なタスクを自動化し、知的な洞察を提供し、チームがより効率的に働くことを実現します。シームレスな統合と直感的なインターフェースにより、{TOOL}は世界中の組織から信頼されるソリューションになっています。",
        "ko": "이 플랫폼은 고급 머신러닝 알고리즘을 활용하여 복잡한 작업을 자동화하고, 지능적인 통찰력을 제공하며, 팀이 보다 효율적으로 작업할 수 있도록 합니다. 원활한 통합과 직관적인 인터페이스를 통해 {TOOL}는 전 세계 조직에서 신뢰받는 솔루션이 되었습니다.",
        "ar": "تستفيد المنصة من خوارزميات التعلم الآلي المتقدمة لأتمتة المهام المعقدة، وتوفير رؤى ذكية، وتمكين الفرق من العمل بكفاءة أكبر. مع التكامل السلس والواجهة البديهية، أصبحت {TOOL} حلاً موثوقًا للمؤسسات في جميع أنحاء العالم.",
        "hi": "प्लेटफ़ॉर्म जटिल कार्यों को स्वचालित करने, बुद्धिमान अंतर्दृष्टि प्रदान करने और टीमों को अधिक कुशलता से काम करने में सक्षम बनाने के लिए उन्नत मशीन लर्निंग एल्गोरिदम का लाभ उठाता है। निर्बाध एकीकरण और सहज इंटरफ़ेस के साथ, {TOOL} दुनिया भर के संगठनों के लिए एक विश्वसनीय समाधान बन गया है।"
    },

    # Key Features
    "Key Features": {
        "de": "Hauptmerkmale",
        "fr": "Fonctionnalités Clés",
        "es": "Características Clave",
        "pt": "Recursos Principais",
        "zh": "主要功能",
        "ja": "主な機能",
        "ko": "주요 기능",
        "ar": "الميزات الرئيسية",
        "hi": "मुख्य विशेषताएं"
    }
}

GAMING_FILES = [
    "artomatix-i18n.js",
    "charismaai-i18n.js",
    "hidden-door-i18n.js",
    "inworld-ai-i18n.js",
    "latitude-ai-dungeon-i18n.js",
    "ludoai-i18n.js",
    "promethean-ai-i18n.js",
    "rct-ai-i18n.js",
    "replika-i18n.js",
    "rosebud-ai-i18n.js",
    "scenario-i18n.js"
]

GAMING_TOOL_NAMES = {
    "artomatix": "Artomatix",
    "charismaai": "Charisma.ai",
    "hidden-door": "Hidden Door",
    "inworld-ai": "Inworld AI",
    "latitude-ai-dungeon": "AI Dungeon",
    "ludoai": "Ludo.ai",
    "promethean-ai": "Promethean AI",
    "rct-ai": "RCT AI",
    "replika": "Replika",
    "rosebud-ai": "Rosebud AI",
    "scenario": "Scenario"
}

def get_tool_name(filename):
    for key in GAMING_TOOL_NAMES:
        if filename.startswith(key):
            return GAMING_TOOL_NAMES[key]
    return "Tool"

def fix_file(filepath):
    filename = os.path.basename(filepath)
    tool_name = get_tool_name(filename)

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    updates = 0

    for english_template, translations in ADDITIONAL_GAMING_TRANSLATIONS.items():
        english_text = english_template.replace("{TOOL}", tool_name)

        for lang_code, translation_template in translations.items():
            translated_text = translation_template.replace("{TOOL}", tool_name)
            english_escaped = re.escape(english_text)

            # Pattern to match the English text within the language section
            pattern = f'("{lang_code}":[\\s\\S]*?)(".*?":\\s*)("{english_escaped}")'

            def replacer(match):
                nonlocal updates
                updates += 1
                return match.group(1) + match.group(2) + '"' + translated_text + '"'

            content = re.sub(pattern, replacer, content)

    if updates > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    return updates

def main():
    base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\js"
    total = 0

    print("="*60)
    print("FIXING MISSING GAMING TRANSLATIONS")
    print("="*60)
    print()

    for filename in GAMING_FILES:
        filepath = os.path.join(base_dir, filename)
        if os.path.exists(filepath):
            count = fix_file(filepath)
            if count > 0:
                print(f"[OK] {filename}: {count} translations")
                total += count
            else:
                print(f"[SKIP] {filename}: already complete")

    print()
    print("="*60)
    print(f"TOTAL TRANSLATIONS ADDED: {total}")
    print("="*60)

if __name__ == "__main__":
    main()
