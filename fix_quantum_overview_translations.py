#!/usr/bin/env python3
"""
Fix overview translations for Quantum Computing category
Add proper translations for the first paragraph and key sections
"""

import re
import os

QUANTUM_TOOLS = {
    "amazon-braket-i18n.js": "Amazon Braket",
    "azure-quantum-i18n.js": "Azure Quantum",
    "d-wave-leap-i18n.js": "D-Wave Leap",
    "google-cirq-i18n.js": "Google Cirq",
    "ibm-quantum-i18n.js": "IBM Quantum",
    "ionq-i18n.js": "IonQ",
    "rigetti-qcs-i18n.js": "Rigetti QCS",
    "xanadu-pennylane-i18n.js": "Xanadu PennyLane"
}

# Correct translations for key sections
OVERVIEW_TRANSLATIONS = {
    "{TOOL} is a leading AI-powered quantum platform designed to streamline workflows and enhance productivity. Built with cutting-edge artificial intelligence technology, it delivers exceptional performance for modern businesses.": {
        "de": "{TOOL} ist eine führende KI-gestützte Quantenplattform, die entwickelt wurde, um Workflows zu optimieren und die Produktivität zu steigern. Mit modernster Technologie der künstlichen Intelligenz bietet sie außergewöhnliche Leistung für moderne Unternehmen.",
        "fr": "{TOOL} est une plateforme quantique alimentée par l'IA de premier plan, conçue pour rationaliser les flux de travail et améliorer la productivité. Construite avec une technologie d'intelligence artificielle de pointe, elle offre des performances exceptionnelles pour les entreprises modernes.",
        "es": "{TOOL} es una plataforma cuántica impulsada por IA líder diseñada para optimizar flujos de trabajo y mejorar la productividad. Construida con tecnología de inteligencia artificial de vanguardia, ofrece un rendimiento excepcional para las empresas modernas.",
        "pt": "{TOOL} é uma plataforma quântica alimentada por IA líder projetada para otimizar fluxos de trabalho e aumentar a produtividade. Construída com tecnologia de inteligência artificial de ponta, oferece desempenho excepcional para empresas modernas.",
        "zh": "{TOOL} 是一个领先的AI驱动量子平台，旨在简化工作流程并提高生产力。采用尖端人工智能技术构建，为现代企业提供卓越性能。",
        "ja": "{TOOL}は、ワークフローを合理化し生産性を向上させるために設計された、AI駆動の主要な量子プラットフォームです。最先端の人工知能技術で構築され、現代のビジネスに卓越したパフォーマンスを提供します。",
        "ko": "{TOOL}는 워크플로우를 간소화하고 생산성을 향상시키도록 설계된 선도적인 AI 기반 양자 플랫폼입니다. 최첨단 인공지능 기술로 구축되어 현대 비즈니스에 탁월한 성능을 제공합니다.",
        "ar": "{TOOL} هي منصة كمومية رائدة مدعومة بالذكاء الاصطناعي مصممة لتبسيط سير العمل وتعزيز الإنتاجية. مبنية بتكنولوجيا الذكاء الاصطناعي المتطورة، توفر أداءً استثنائيًا للشركات الحديثة.",
        "hi": "{TOOL} एक अग्रणी AI-संचालित क्वांटम प्लेटफ़ॉर्म है जो वर्कफ़्लो को सुव्यवस्थित करने और उत्पादकता बढ़ाने के लिए डिज़ाइन किया गया है। अत्याधुनिक आर्टिफिशियल इंटेलिजेंस तकनीक से निर्मित, यह आधुनिक व्यवसायों के लिए असाधारण प्रदर्शन प्रदान करता है।"
    },
    "The platform leverages advanced machine learning algorithms to automate complex tasks, provide intelligent insights, and enable teams to work more efficiently. With seamless integrations and an intuitive interface, {TOOL} has become a trusted solution for organizations worldwide.": {
        "de": "Die Plattform nutzt fortschrittliche Machine-Learning-Algorithmen, um komplexe Aufgaben zu automatisieren, intelligente Einblicke zu liefern und Teams zu ermöglichen, effizienter zu arbeiten. Mit nahtlosen Integrationen und einer intuitiven Benutzeroberfläche ist {TOOL} zu einer vertrauenswürdigen Lösung für Organisationen weltweit geworden.",
        "fr": "La plateforme exploite des algorithmes d'apprentissage automatique avancés pour automatiser les tâches complexes, fournir des informations intelligentes et permettre aux équipes de travailler plus efficacement. Avec des intégrations transparentes et une interface intuitive, {TOOL} est devenue une solution de confiance pour les organisations du monde entier.",
        "es": "La plataforma aprovecha algoritmos avanzados de aprendizaje automático para automatizar tareas complejas, proporcionar información inteligente y permitir que los equipos trabajen de manera más eficiente. Con integraciones perfectas e interfaz intuitiva, {TOOL} se ha convertido en una solución confiable para organizaciones en todo el mundo.",
        "pt": "A plataforma aproveita algoritmos avançados de aprendizado de máquina para automatizar tarefas complexas, fornecer insights inteligentes e permitir que as equipes trabalhem com mais eficiência. Com integrações contínuas e uma interface intuitiva, {TOOL} tornou-se uma solução confiável para organizações em todo o mundo.",
        "zh": "该平台利用先进的机器学习算法来自动化复杂任务，提供智能见解，并使团队能够更高效地工作。凭借无缝集成和直观的界面，{TOOL} 已成为全球组织值得信赖的解决方案。",
        "ja": "このプラットフォームは高度な機械学習アルゴリズムを活用して、複雑なタスクを自動化し、知的な洞察を提供し、チームがより効率的に働くことを実現します。シームレスな統合と直感的なインターフェースにより、{TOOL}は世界中の組織から信頼されるソリューションになっています。",
        "ko": "이 플랫폼은 고급 머신러닝 알고리즘을 활용하여 복잡한 작업을 자동화하고, 지능적인 인사이트를 제공하며, 팀이 더 효율적으로 작업할 수 있도록 합니다. 원활한 통합과 직관적인 인터페이스로 {TOOL}는 전 세계 조직에서 신뢰받는 솔루션이 되었습니다.",
        "ar": "تستفيد المنصة من خوارزميات التعلم الآلي المتقدمة لأتمتة المهام المعقدة، وتوفير رؤى ذكية، وتمكين الفرق من العمل بكفاءة أكبر. مع التكامل السلس والواجهة البديهية، أصبحت {TOOL} حلاً موثوقًا للمؤسسات في جميع أنحاء العالم.",
        "hi": "यह प्लेटफ़ॉर्म जटिल कार्यों को स्वचालित करने, बुद्धिमान अंतर्दृष्टि प्रदान करने और टीमों को अधिक कुशलता से काम करने में सक्षम बनाने के लिए उन्नत मशीन लर्निंग एल्गोरिदम का लाभ उठाता है। निर्बाध एकीकरण और सहज इंटरफ़ेस के साथ, {TOOL} दुनिया भर के संगठनों के लिए एक विश्वसनीय समाधान बन गया है।"
    },
    "Whether you're a small startup or a large enterprise, {TOOL} scales to meet your needs while maintaining high performance and reliability.": {
        "de": "Ob Sie ein kleines Startup oder ein großes Unternehmen sind, {TOOL} skaliert, um Ihre Bedürfnisse zu erfüllen und dabei hohe Leistung und Zuverlässigkeit beizubehalten.",
        "fr": "Que vous soyez une petite startup ou une grande entreprise, {TOOL} s'adapte pour répondre à vos besoins tout en maintenant des performances et une fiabilité élevées.",
        "es": "Ya sea que seas una pequeña startup o una gran empresa, {TOOL} se adapta a tus necesidades manteniendo alto rendimiento y confiabilidad.",
        "pt": "Seja você uma pequena startup ou uma grande empresa, {TOOL} se dimensiona para atender suas necessidades mantendo alto desempenho e confiabilidade.",
        "zh": "无论您是小型初创公司还是大型企业，{TOOL} 都能扩展以满足您的需求，同时保持高性能和可靠性。",
        "ja": "小規模なスタートアップであろうと大企業であろうと、{TOOL}は高いパフォーマンスと信頼性を保ちながら、あらゆるニーズに対応するようにスケーリングします。",
        "ko": "소규模 스타트업이든 대기업이든, {TOOL}는 높은 성능과 안정성을 유지하면서 귀하의 요구사항을 충족하도록 확장됩니다.",
        "ar": "سواء كنت شركة ناشئة صغيرة أو مؤسسة كبيرة، فإن {TOOL} يتوسع لتلبية احتياجاتك مع الحفاظ على الأداء العالي والموثوقية.",
        "hi": "चाहे आप एक छोटा स्टार्टअप हों या एक बड़ा उद्यम, {TOOL} उच्च प्रदर्शन और विश्वसनीयता बनाए रखते हुए आपकी आवश्यकताओं को पूरा करने के लिए स्केल करता है।"
    },
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

def get_tool_key(filename):
    """Get tool key from filename"""
    return filename.replace("-i18n.js", "")

def fix_translations(filepath, tool_name):
    """Fix translations in i18n file"""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    updates = 0

    for english_template, translations in OVERVIEW_TRANSLATIONS.items():
        english_text = english_template.replace("{TOOL}", tool_name)

        # For each language
        for lang_code, translation_template in translations.items():
            translation = translation_template.replace("{TOOL}", tool_name)

            # Find the key in the file
            # The key might be like "review.ibm-quantum.ibm.quantum.is.a.leading"
            # We need to find it and replace the value

            # Pattern to match the English text and replace with translation
            # Look for the text in the language section
            lang_section_pattern = f'("{lang_code}":[\\s\\S]*?)"([^"]*{re.escape(english_text[:50])}[^"]*)"'

            def replacer(match):
                return match.group(1) + f'"{translation}"'

            new_content = re.sub(lang_section_pattern, replacer, content, count=1)
            if new_content != content:
                content = new_content
                updates += 1

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    return updates

def main():
    js_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\js"

    print("="*60)
    print("FIXING QUANTUM OVERVIEW TRANSLATIONS")
    print("="*60)
    print()

    total_updates = 0

    for filename, tool_name in QUANTUM_TOOLS.items():
        filepath = os.path.join(js_dir, filename)

        if not os.path.exists(filepath):
            print(f"[SKIP] File not found: {filename}")
            continue

        updates = fix_translations(filepath, tool_name)
        print(f"[OK] {filename}: {updates} translations updated")
        total_updates += updates

    print()
    print("="*60)
    print(f"TOTAL TRANSLATIONS UPDATED: {total_updates}")
    print("="*60)
    print()
    print("Overview translations fixed!")

if __name__ == "__main__":
    main()
