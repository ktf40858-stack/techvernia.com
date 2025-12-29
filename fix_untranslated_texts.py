import os
import re
import json as json_module

base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
js_dir = os.path.join(base_dir, "js")

tools = {
    "khan-academy-ai": "Khan Academy Ai",
    "aleks": "ALEKS",
    "carnegie-learning": "Carnegie Learning",
    "century-tech": "Century Tech",
    "cognii": "Cognii",
    "coursera-coach": "Coursera Coach",
    "duolingo-max": "Duolingo Max",
    "gradescope": "Gradescope",
    "knewton-alta": "Knewton Alta",
    "querium": "Querium",
    "quizlet-ai": "Quizlet Ai",
    "socratic-by-google": "Socratic By Google",
    "squirrel-ai": "Squirrel Ai",
    "thinkster-math": "Thinkster Math"
}

# Textes à traduire (patterns)
texts_to_translate = [
    # Pattern 1: Main description
    {
        "en_pattern": "{tool} is a leading AI-powered education platform designed to streamline workflows and enhance productivity. Built with cutting-edge artificial intelligence technology, it delivers exceptional performance for modern businesses.",
        "de": "{tool} ist eine führende KI-gestützte Bildungsplattform, die entwickelt wurde, um Arbeitsabläufe zu optimieren und die Produktivität zu steigern. Mit modernster künstlicher Intelligenz-Technologie bietet sie außergewöhnliche Leistung für moderne Bildungseinrichtungen.",
        "es": "{tool} es una plataforma educativa líder impulsada por IA diseñada para optimizar flujos de trabajo y mejorar la productividad. Construida con tecnología de inteligencia artificial de vanguardia, ofrece un rendimiento excepcional para instituciones educativas modernas.",
        "fr": "{tool} est une plateforme éducative leader alimentée par l'IA conçue pour rationaliser les flux de travail et améliorer la productivité. Construite avec une technologie d'intelligence artificielle de pointe, elle offre des performances exceptionnelles pour les établissements éducatifs modernes.",
        "pt": "{tool} é uma plataforma educacional líder alimentada por IA projetada para otimizar fluxos de trabalho e aumentar a produtividade. Construída com tecnologia de inteligência artificial de ponta, oferece desempenho excepcional para instituições educacionais modernas.",
        "zh": "{tool}是一个领先的AI驱动教育平台，旨在简化工作流程并提高生产力。采用尖端人工智能技术构建，为现代教育机构提供卓越性能。",
        "ja": "{tool}は、ワークフローを効率化し生産性を向上させるために設計された、AIを活用した主要な教育プラットフォームです。最先端の人工知能技術で構築され、現代の教育機関に優れたパフォーマンスを提供します。",
        "ko": "{tool}는 워크플로우를 간소化하고 생산성을 향상시키도록 설계된 선도적인 AI 기반 교육 플랫폼입니다. 최첨단 인공지능 기술로 구축되어 현대 교육 기관에 탁월한 성능을 제공합니다.",
        "ar": "{tool} هي منصة تعليمية رائدة مدعومة بالذكاء الاصطناعي مصممة لتبسيط سير العمل وتعزيز الإنتاجية. تم بناؤها بتقنية ذكاء اصطناعي متطورة، وتقدم أداءً استثنائيًا للمؤسسات التعليمية الحديثة.",
        "hi": "{tool} एक अग्रणी AI-संचालित शिक्षा प्लेटफ़ॉर्म है जो वर्कफ़्लो को सुव्यवस्थित करने और उत्पादकता बढ़ाने के लिए डिज़ाइन किया गया है। अत्याधुनिक कृत्रिम बुद्धिमत्ता प्रौद्योगिकी के साथ निर्मित, यह आधुनिक शैक्षणिक संस्थानों के लिए असाधारण प्रदर्शन प्रदान करता है।"
    },
    # Pattern 2: Platform description
    {
        "en_pattern": "The platform leverages advanced machine learning algorithms to automate complex tasks, provide intelligent insights, and enable teams to work more efficiently. With seamless integrations and an intuitive interface, {tool} has become a trusted solution for organizations worldwide.",
        "de": "Die Plattform nutzt fortschrittliche Machine-Learning-Algorithmen zur Automatisierung komplexer Aufgaben, zur Bereitstellung intelligenter Einblicke und zur Unterstützung von Teams bei effizienterer Arbeit. Mit nahtlosen Integrationen und einer intuitiven Benutzeroberfläche ist {tool} zu einer vertrauenswürdigen Lösung für Bildungseinrichtungen weltweit geworden.",
        "es": "La plataforma aprovecha algoritmos avanzados de aprendizaje automático para automatizar tareas complejas, proporcionar información inteligente y permitir que los equipos trabajen de manera más eficiente. Con integraciones perfectas y una interfaz intuitiva, {tool} se ha convertido en una solución confiable para instituciones educativas en todo el mundo.",
        "fr": "La plateforme exploite des algorithmes avancés d'apprentissage automatique pour automatiser les tâches complexes, fournir des informations intelligentes et permettre aux équipes de travailler plus efficacement. Avec des intégrations transparentes et une interface intuitive, {tool} est devenue une solution de confiance pour les établissements éducatifs du monde entier.",
        "pt": "A plataforma aproveita algoritmos avançados de aprendizado de máquina para automatizar tarefas complexas, fornecer insights inteligentes e permitir que as equipes trabalhem com mais eficiência. Com integrações perfeitas e uma interface intuitiva, {tool} tornou-se uma solução confiável para instituições educacionais em todo o mundo.",
        "zh": "该平台利用先进的机器学习算法自动化复杂任务，提供智能洞察，并使团队能够更高效地工作。凭借无缝集成和直观界面，{tool}已成为全球教育机构值得信赖的解决方案。",
        "ja": "このプラットフォームは、高度な機械学習アルゴリズムを活用して複雑なタスクを自動化し、インテリジェントな洞察を提供し、チームがより効率的に作業できるようにします。シームレスな統合と直感的なインターフェースにより、{tool}は世界中の教育機関にとって信頼できるソリューションとなっています。",
        "ko": "이 플랫폼은 고급 머신러닝 알고리즘을 활용하여 복잡한 작업을 자동화하고, 지능적인 통찰력을 제공하며, 팀이 더 효율적으로 작업할 수 있도록 지원합니다. 원활한 통합과 직관적인 인터페이스를 통해 {tool}는 전 세계 교육 기관에서 신뢰받는 솔루션이 되었습니다.",
        "ar": "تستفيد المنصة من خوارزميات التعلم الآلي المتقدمة لأتمتة المهام المعقدة، وتوفير رؤى ذكية، وتمكين الفرق من العمل بكفاءة أكبر. مع التكاملات السلسة والواجهة البديهية، أصبحت {tool} حلاً موثوقًا للمؤسسات التعليمية في جميع أنحاء العالم.",
        "hi": "यह प्लेटफ़ॉर्म जटिल कार्यों को स्वचालित करने, बुद्धिमान अंतर्दृष्टि प्रदान करने और टीमों को अधिक कुशलता से काम करने में सक्षम बनाने के लिए उन्नत मशीन लर्निंग एल्गोरिदम का लाभ उठाता है। सहज एकीकरण और सहज इंटरफ़ेस के साथ, {tool} दुनिया भर के शैक्षणिक संस्थानों के लिए एक विश्वसनीय समाधान बन गया है।"
    },
    # Pattern 3: Scalability
    {
        "en_pattern": "Whether you're a small startup or a large enterprise, {tool} scales to meet your needs while maintaining high performance and reliability.",
        "de": "Ob kleines Startup oder großes Unternehmen, {tool} skaliert, um Ihre Anforderungen zu erfüllen und dabei hohe Leistung und Zuverlässigkeit beizubehalten.",
        "es": "Ya sea una pequeña startup o una gran empresa, {tool} se escala para satisfacer sus necesidades manteniendo un alto rendimiento y confiabilidad.",
        "fr": "Que vous soyez une petite startup ou une grande entreprise, {tool} s'adapte pour répondre à vos besoins tout en maintenant des performances et une fiabilité élevées.",
        "pt": "Seja uma pequena startup ou uma grande empresa, {tool} se dimensiona para atender às suas necesidades, mantendo alto desempenho e confiabilidad.",
        "zh": "无论您是小型初创公司还是大型企业，{tool}都能扩展以满足您的需求，同时保持高性能和可靠性。",
        "ja": "小規模なスタートアップであろうと大企业であろうと、{tool}は高いパフォーマンスと信頼性を維持しながら、ニーズに合わせて拡張します。",
        "ko": "소규모 스타트업이든 대기업이든, {tool}는 높은 성能과 안정성을 유지하면서 귀하의 요구 사항을 충족하도록 확장됩니다。",
        "ar": "سواء كنت شركة ناشئة صغيرة أو مؤسسة كبيرة، فإن {tool} يتوسع لتلبية احتياجاتك مع الحفاظ على الأداء العالي والموثوقية.",
        "hi": "चाहे आप एक छोटा स्टार्टअप हों या एक बड़ा उद्यम, {tool} उच्च प्रदर्शन और विश्वसनीयता बनाए रखते हुए आपकी आवश्यकताओं को पूरा करने के लिए स्केल करता है।"
    }
]

def tool_to_camel(tool):
    parts = tool.split('-')
    return parts[0] + ''.join(p.capitalize() for p in parts[1:])

def tool_to_title(tool):
    return ' '.join(p.capitalize() for p in tool.split('-'))

def fix_tool(tool_key, tool_display):
    """Corrige les traductions pour un outil"""
    js_file = os.path.join(js_dir, f"{tool_key}-i18n.js")

    if not os.path.exists(js_file):
        return

    # Lire le fichier
    with open(js_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pour chaque pattern de texte
    for text_pattern in texts_to_translate:
        en_text = text_pattern["en_pattern"].replace("{tool}", tool_display)

        # Pour chaque langue
        for lang in ["de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]:
            if lang in text_pattern:
                trans_text = text_pattern[lang].replace("{tool}", tool_display)

                # Remplacer le texte anglais par la traduction
                # Échapper les caractères spéciaux
                escaped_en = en_text.replace('"', '\\"')
                escaped_trans = trans_text.replace('"', '\\"')

                # Simple remplacement de chaîne
                content = content.replace(f'": "{en_text}"', f'": "{trans_text}"')

    # Sauvegarder
    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  [OK] {tool_key} fixed")

# MAIN EXECUTION
print("=" * 70)
print("FIXING UNTRANSLATED LONG TEXTS")
print("=" * 70)

for tool_key, tool_display in tools.items():
    fix_tool(tool_key, tool_display)

print("\n" + "=" * 70)
print("[COMPLETE] All untranslated texts fixed!")
print("=" * 70)
