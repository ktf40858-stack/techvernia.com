#!/usr/bin/env python3
import sys,io,re
if sys.platform=='win32':sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

T={
    "fr":{"overview":"Aperçu","is.a":"est une plateforme RH puissante et riche en fonctionnalités qui offre une valeur exceptionnelle pour les équipes de toutes tailles. Fortement recommandé.","platform":"La plateforme exploite des algorithmes d'apprentissage automatique avancés pour automatiser les tâches complexes, fournir des informations intelligentes et permettre aux équipes de travailler plus efficacement. Avec des intégrations transparentes et une interface intuitive, {N} est devenu une solution de confiance pour les organisations du monde entier.","startup":"Que vous soyez une petite startup ou une grande entreprise, {N} s'adapte à vos besoins tout en maintenant des performances et une fiabilité élevées."},
    "es":{"overview":"Descripción general","is.a":"es una plataforma de RRHH potente y rica en funciones que ofrece un valor excepcional para equipos de todos los tamaños. Altamente recomendado.","platform":"La plataforma aprovecha algoritmos avanzados de aprendizaje automático para automatizar tareas complejas, proporcionar información inteligente y permitir que los equipos trabajen de manera más eficiente. Con integraciones perfectas y una interfaz intuitiva, {N} se ha convertido en una solución confiable para organizaciones de todo el mundo.","startup":"Ya sea una pequeña startup o una gran empresa, {N} se escala para satisfacer sus necesidades manteniendo un alto rendimiento y confiabilidad."},
    "pt":{"overview":"Visão geral","is.a":"é uma plataforma de RH poderosa e rica em recursos que oferece valor excepcional para equipes de todos os tamanhos. Altamente recomendado.","platform":"A plataforma aproveita algoritmos avançados de aprendizado de máquina para automatizar tarefas complexas, fornecer insights inteligentes e permitir que as equipes trabalhem com mais eficiência. Com integrações perfeitas e uma interface intuitiva, {N} se tornou uma solução confiável para organizações em todo o mundo.","startup":"Seja uma pequena startup ou uma grande empresa, {N} escala para atender às suas necessidades, mantendo alto desempenho e confiabilidade."},
    "zh":{"overview":"概述","is.a":"是一个功能强大、功能丰富的人力资源平台，为各种规模的团队提供卓越的价值。强烈推荐。","platform":"该平台利用先进的机器学习算法来自动化复杂的任务，提供智能见解，并使团队能够更高效地工作。凭借无缝集成和直观的界面，{N}已成为全球组织值得信赖的解决方案。","startup":"无论您是小型初创公司还是大型企业，{N}都可以扩展以满足您的需求，同时保持高性能和可靠性。"},
    "ja":{"overview":"概要","is.a":"は、あらゆる規模のチームに卓越した価値を提供する、強力で機能豊富なHRプラットフォームです。強くお勧めします。","platform":"このプラットフォームは、高度な機械学習アルゴリズムを活用して複雑なタスクを自動化し、インテリジェントな洞察を提供し、チームがより効率的に作業できるようにします。シームレスな統合と直感的なインターフェースにより、{N}は世界中の組織から信頼されるソリューションとなっています。","startup":"小規模なスタートアップでも大企業でも、{N}はニーズに合わせてスケールし、高いパフォーマンスと信頼性を維持します。"},
    "ko":{"overview":"개요","is.a":"는 모든 규모의 팀에 탁월한 가치를 제공하는 강력하고 기능이 풍부한 HR 플랫폼입니다. 적극 권장합니다.","platform":"이 플랫폼은 고급 머신 러닝 알고리즘을 활용하여 복잡한 작업을 자동화하고 지능형 인사이트를 제공하며 팀이 보다 효율적으로 작업할 수 있도록 합니다. 원활한 통합과 직관적인 인터페이스를 통해 {N}는 전 세계 조직에서 신뢰할 수 있는 솔루션이 되었습니다.","startup":"소규모 스타트업이든 대기업이든 {N}는 높은 성능과 안정성을 유지하면서 요구 사항을 충족하도록 확장됩니다."},
    "ar":{"overview":"نظرة عامة","is.a":"هي منصة موارد بشرية قوية وغنية بالميزات توفر قيمة استثنائية للفرق بجميع الأحجام. موصى به بشدة.","platform":"تستفيد المنصة من خوارزميات التعلم الآلي المتقدمة لأتمتة المهام المعقدة وتوفير رؤى ذكية وتمكين الفرق من العمل بكفاءة أكبر. مع التكامل السلس والواجهة البديهية، أصبحت {N} حلاً موثوقًا للمؤسسات في جميع أنحاء العالم.","startup":"سواء كنت شركة ناشئة صغيرة أو مؤسسة كبيرة، تتوسع {N} لتلبية احتياجاتك مع الحفاظ على الأداء العالي والموثوقية."},
    "hi":{"overview":"अवलोकन","is.a":"एक शक्तिशाली, सुविधा-संपन्न HR प्लेटफ़ॉर्म है जो सभी आकारों की टीमों के लिए असाधारण मूल्य प्रदान करता है। अत्यधिक अनुशंसित।","platform":"प्लेटफ़ॉर्म जटिल कार्यों को स्वचालित करने, बुद्धिमान अंतर्दृष्टि प्रदान करने और टीमों को अधिक कुशलता से काम करने में सक्षम बनाने के लिए उन्नत मशीन लर्निंग एल्गोरिदम का लाभ उठाता है। सहज एकीकरण और सहज इंटरफ़ेस के साथ, {N} दुनिया भर के संगठनों के लिए एक विश्वसनीय समाधान बन गया है।","startup":"चाहे आप एक छोटा स्टार्टअप हों या एक बड़ा उद्यम, {N} उच्च प्रदर्शन और विश्वसनीयता बनाए रखते हुए आपकी आवश्यकताओं को पूरा करने के लिए स्केल करता है।"}
}

tools=['beamery','eightfold-ai','fetcher','findem','harver','hirevue','humanly','paradox-olivia','phenom','pymetrics','seekout','sense','textio','workable-ai']

with open('GenuisNet.ai/js/i18n.js','r',encoding='utf-8') as f:
    content=f.read()

# Trouver chaque section de langue
lang_positions={'fr':0,'es':0,'pt':0,'zh':0,'ja':0,'ko':0,'ar':0,'hi':0}
for lang in lang_positions:
    match=re.search(rf'\n\s+{lang}:\s*{{',content)
    if match:
        lang_positions[lang]=match.end()

# Préparer les insertions pour chaque langue
for lang,pos in sorted(lang_positions.items(),key=lambda x:x[1],reverse=True):
    if pos==0:continue
    t=T[lang]
    lines=[]
    for tool in tools:
        n=tool.replace('-',' ').title()
        lines.append(f'        "review.{tool}.overview": "{t["overview"]}",\n')
        lines.append(f'        "review.{tool}.{tool}.is.a": "{n} {t["is.a"]}",\n')
        lines.append(f'        "review.{tool}.the.platform.leverages.advanced.machine": "{t["platform"].replace("{N}",n)}",\n')
        lines.append(f'        "review.{tool}.whether.youre.a.small.startup": "{t["startup"].replace("{N}",n)}",\n')

    content=content[:pos]+'\n'+''.join(lines)+content[pos:]
    print(f'✓ {lang}: {len(lines)} lignes')

with open('GenuisNet.ai/js/i18n.js','w',encoding='utf-8') as f:
    f.write(content)

print('\n✅ Toutes les traductions HR ajoutées dans i18n.js')
