#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys,io
if sys.platform=='win32':sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

LANGS = {
    "de": {
        "desc1": "ist eine leistungsstarke, funktionsreiche HR-Plattform, die außergewöhnlichen Wert für Teams jeder Größe bietet. Sehr empfehlenswert.",
        "desc2": "Die Plattform nutzt fortschrittliche Machine-Learning-Algorithmen zur Automatisierung komplexer Aufgaben, Bereitstellung intelligenter Erkenntnisse und effizienterer Teamarbeit. Mit nahtlosen Integrationen und intuitiver Benutzeroberfläche ist {TOOL} zu einer vertrauenswürdigen Lösung für Unternehmen weltweit geworden.",
        "desc3": "Ob kleines Startup oder Großunternehmen - {TOOL} skaliert entsprechend Ihren Anforderungen bei hoher Leistung und Zuverlässigkeit."
    },
    "fr": {
        "desc1": "est une plateforme RH puissante et riche en fonctionnalités qui offre une valeur exceptionnelle pour les équipes de toutes tailles. Fortement recommandé.",
        "desc2": "La plateforme exploite des algorithmes d'apprentissage automatique avancés pour automatiser les tâches complexes, fournir des informations intelligentes et permettre aux équipes de travailler plus efficacement. Avec des intégrations transparentes et une interface intuitive, {TOOL} est devenu une solution de confiance pour les organisations du monde entier.",
        "desc3": "Que vous soyez une petite startup ou une grande entreprise, {TOOL} s'adapte à vos besoins tout en maintenant des performances et une fiabilité élevées."
    },
    "es": {
        "desc1": "es una plataforma de RRHH potente y rica en funciones que ofrece un valor excepcional para equipos de todos los tamaños. Altamente recomendado.",
        "desc2": "La plataforma aprovecha algoritmos avanzados de aprendizaje automático para automatizar tareas complejas, proporcionar información inteligente y permitir que los equipos trabajen de manera más eficiente. Con integraciones perfectas y una interfaz intuitiva, {TOOL} se ha convertido en una solución confiable para organizaciones de todo el mundo.",
        "desc3": "Ya sea una pequeña startup o una gran empresa, {TOOL} se escala para satisfacer sus necesidades manteniendo un alto rendimiento y confiabilidad."
    },
    "pt": {
        "desc1": "é uma plataforma de RH poderosa e rica em recursos que oferece valor excepcional para equipes de todos os tamanhos. Altamente recomendado.",
        "desc2": "A plataforma aproveita algoritmos avançados de aprendizado de máquina para automatizar tarefas complexas, fornecer insights inteligentes e permitir que as equipes trabalhem com mais eficiência. Com integrações perfeitas e uma interface intuitiva, {TOOL} se tornou uma solução confiável para organizações em todo o mundo.",
        "desc3": "Seja uma pequena startup ou uma grande empresa, {TOOL} escala para atender às suas necessidades, mantendo alto desempenho e confiabilidade."
    },
    "zh": {
        "desc1": "是一个功能强大、功能丰富的人力资源平台，为各种规模的团队提供卓越的价值。强烈推荐。",
        "desc2": "该平台利用先进的机器学习算法来自动化复杂的任务，提供智能见解，并使团队能够更高效地工作。凭借无缝集成和直观的界面，{TOOL}已成为全球组织值得信赖的解决方案。",
        "desc3": "无论您是小型初创公司还是大型企业，{TOOL}都可以扩展以满足您的需求，同时保持高性能和可靠性。"
    },
    "ja": {
        "desc1": "は、あらゆる規模のチームに卓越した価値を提供する、強力で機能豊富なHRプラットフォームです。強くお勧めします。",
        "desc2": "このプラットフォームは、高度な機械学習アルゴリズムを活用して複雑なタスクを自動化し、インテリジェントな洞察を提供し、チームがより効率的に作業できるようにします。シームレスな統合と直感的なインターフェースにより、{TOOL}は世界中の組織から信頼されるソリューションとなっています。",
        "desc3": "小規模なスタートアップでも大企業でも、{TOOL}はニーズに合わせてスケールし、高いパフォーマンスと信頼性を維持します。"
    },
    "ko": {
        "desc1": "는 모든 규모의 팀에 탁월한 가치를 제공하는 강력하고 기능이 풍부한 HR 플랫폼입니다. 적극 권장합니다.",
        "desc2": "이 플랫폼은 고급 머신 러닝 알고리즘을 활용하여 복잡한 작업을 자동화하고 지능형 인사이트를 제공하며 팀이 보다 효율적으로 작업할 수 있도록 합니다. 원활한 통합과 직관적인 인터페이스를 통해 {TOOL}는 전 세계 조직에서 신뢰할 수 있는 솔루션이 되었습니다.",
        "desc3": "소규모 스타트업이든 대기업이든 {TOOL}는 높은 성능과 안정성을 유지하면서 요구 사항을 충족하도록 확장됩니다."
    },
    "ar": {
        "desc1": "هي منصة موارد بشرية قوية وغنية بالميزات توفر قيمة استثنائية للفرق بجميع الأحجام. موصى به بشدة.",
        "desc2": "تستفيد المنصة من خوارزميات التعلم الآلي المتقدمة لأتمتة المهام المعقدة وتوفير رؤى ذكية وتمكين الفرق من العمل بكفاءة أكبر. مع التكامل السلس والواجهة البديهية، أصبحت {TOOL} حلاً موثوقًا للمؤسسات في جميع أنحاء العالم.",
        "desc3": "سواء كنت شركة ناشئة صغيرة أو مؤسسة كبيرة، تتوسع {TOOL} لتلبية احتياجاتك مع الحفاظ على الأداء العالي والموثوقية."
    },
    "hi": {
        "desc1": "एक शक्तिशाली, सुविधा-संपन्न HR प्लेटफ़ॉर्म है जो सभी आकारों की टीमों के लिए असाधारण मूल्य प्रदान करता है। अत्यधिक अनुशंसित।",
        "desc2": "प्लेटफ़ॉर्म जटिल कार्यों को स्वचालित करने, बुद्धिमान अंतर्दृष्टि प्रदान करने और टीमों को अधिक कुशलता से काम करने में सक्षम बनाने के लिए उन्नत मशीन लर्निंग एल्गोरिदम का लाभ उठाता है। सहज एकीकरण और सहज इंटरफ़ेस के साथ, {TOOL} दुनिया भर के संगठनों के लिए एक विश्वसनीय समाधान बन गया है।",
        "desc3": "चाहे आप एक छोटा स्टार्टअप हों या एक बड़ा उद्यम, {TOOL} उच्च प्रदर्शन और विश्वसनीयता बनाए रखते हुए आपकी आवश्यकताओं को पूरा करने के लिए स्केल करता है।"
    }
}

tools = ['beamery','eightfold-ai','fetcher','findem','harver','hirevue','humanly','paradox-olivia','phenom','pymetrics','seekout','sense','textio','workable-ai']

for tool in tools:
    name = tool.replace('-',' ').title()
    lines = [f'// {tool.upper().replace("-"," ")} I18N',
             f'const {tool.replace("-","")}Translations = {{',
             '  "en": {',
             f'    "review.{tool}.{tool}.is.a": "{name} is a powerful, feature-rich HR platform that delivers exceptional value for teams of all sizes. Highly recommended.",',
             f'    "review.{tool}.the.platform.leverages.advanced.machine": "The platform leverages advanced machine learning algorithms to automate complex tasks, provide intelligent insights, and enable teams to work more efficiently. With seamless integrations and an intuitive interface, {name} has become a trusted solution for organizations worldwide.",',
             f'    "review.{tool}.whether.youre.a.small.startup": "Whether you\'re a small startup or a large enterprise, {name} scales to meet your needs while maintaining high performance and reliability."',
             '  },']

    for lang, trans in LANGS.items():
        lines.append(f'  "{lang}": {{')
        lines.append(f'    "review.{tool}.{tool}.is.a": "{name} {trans["desc1"]}",')
        lines.append(f'    "review.{tool}.the.platform.leverages.advanced.machine": "{trans["desc2"].replace("{TOOL}", name)}",')
        lines.append(f'    "review.{tool}.whether.youre.a.small.startup": "{trans["desc3"].replace("{TOOL}", name)}"')
        lines.append('  },')

    lines.append('};')

    with open(f'GenuisNet.ai/js/{tool}-i18n.js', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    print(f'✓ {tool}')
print('\n=== TERMINÉ ===')
