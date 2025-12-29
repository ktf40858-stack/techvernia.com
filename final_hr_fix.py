#!/usr/bin/env python3
import sys,io,re
if sys.platform=='win32':sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

# Traductions HR complètes
T={
    "de":{"overview":"Übersicht","is.a":"ist eine leistungsstarke, funktionsreiche HR-Plattform, die außergewöhnlichen Wert für Teams jeder Größe bietet. Sehr empfehlenswert.","platform":"Die Plattform nutzt fortschrittliche Machine-Learning-Algorithmen zur Automatisierung komplexer Aufgaben, Bereitstellung intelligenter Erkenntnisse und effizienterer Teamarbeit. Mit nahtlosen Integrationen und intuitiver Benutzeroberfläche ist {N} zu einer vertrauenswürdigen Lösung für Unternehmen weltweit geworden.","startup":"Ob kleines Startup oder Großunternehmen - {N} skaliert entsprechend Ihren Anforderungen bei hoher Leistung und Zuverlässigkeit."},
    "fr":{"overview":"Aperçu","is.a":"est une plateforme RH puissante et riche en fonctionnalités qui offre une valeur exceptionnelle pour les équipes de toutes tailles. Fortement recommandé.","platform":"La plateforme exploite des algorithmes d'apprentissage automatique avancés pour automatiser les tâches complexes, fournir des informations intelligentes et permettre aux équipes de travailler plus efficacement. Avec des intégrations transparentes et une interface intuitive, {N} est devenu une solution de confiance pour les organisations du monde entier.","startup":"Que vous soyez une petite startup ou une grande entreprise, {N} s'adapte à vos besoins tout en maintenant des performances et une fiabilité élevées."},
    "es":{"overview":"Descripción general","is.a":"es una plataforma de RRHH potente y rica en funciones que ofrece un valor excepcional para equipos de todos los tamaños. Altamente recomendado.","platform":"La plataforma aprovecha algoritmos avanzados de aprendizaje automático para automatizar tareas complejas, proporcionar información inteligente y permitir que los equipos trabajen de manera más eficiente. Con integraciones perfectas y una interfaz intuitiva, {N} se ha convertido en una solución confiable para organizaciones de todo el mundo.","startup":"Ya sea una pequeña startup o una gran empresa, {N} se escala para satisfacer sus necesidades manteniendo un alto rendimiento y confiabilidad."},
    "pt":{"overview":"Visão geral","is.a":"é uma plataforma de RH poderosa e rica em recursos que oferece valor excepcional para equipes de todos os tamanhos. Altamente recomendado.","platform":"A plataforma aproveita algoritmos avançados de aprendizado de máquina para automatizar tarefas complexas, fornecer insights inteligentes e permitir que as equipes trabalhem com mais eficiência. Com integrações perfeitas e uma interface intuitiva, {N} se tornou uma solução confiável para organizações em todo o mundo.","startup":"Seja uma pequena startup ou uma grande empresa, {N} escala para atender às suas necessidades, mantendo alto desempenho e confiabilidade."}
}

tools=['beamery','eightfold-ai','fetcher','findem','harver','hirevue','humanly','paradox-olivia','phenom','pymetrics','seekout','sense','textio','workable-ai']

for tool in tools:
    n=tool.replace('-',' ').title()
    vn=tool.replace('-','')
    out=[f'// {tool.upper()} I18N',f'const {vn}Translations={{','  "en":{',
         f'    "review.{tool}.overview":"Overview",',
         f'    "review.{tool}.{tool}.is.a":"{n} is a powerful, feature-rich HR platform that delivers exceptional value for teams of all sizes. Highly recommended.",',
         f'    "review.{tool}.the.platform.leverages.advanced.machine":"The platform leverages advanced machine learning algorithms to automate complex tasks, provide intelligent insights, and enable teams to work more efficiently. With seamless integrations and an intuitive interface, {n} has become a trusted solution for organizations worldwide.",',
         f'    "review.{tool}.whether.youre.a.small.startup":"Whether you\'re a small startup or a large enterprise, {n} scales to meet your needs while maintaining high performance and reliability."',
         '  },']
    for lang in ['de','fr','es','pt']:
        t=T[lang]
        out+=[f'  "{lang}":{{"review.{tool}.overview":"{t["overview"]}","review.{tool}.{tool}.is.a":"{n} {t["is.a"]}","review.{tool}.the.platform.leverages.advanced.machine":"{t["platform"].replace("{N}",n)}","review.{tool}.whether.youre.a.small.startup":"{t["startup"].replace("{N}",n)}"}},']
    out.append('};')
    open(f'GenuisNet.ai/js/{tool}-i18n.js','w',encoding='utf-8').write('\n'.join(out))
    print(f'{tool} OK')
