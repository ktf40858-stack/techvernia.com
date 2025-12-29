#!/usr/bin/env python3
import sys,io
if sys.platform=='win32':sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

HR_TRANS={
    "de":{
        "overview":"Übersicht",
        "is.a":"ist eine leistungsstarke, funktionsreiche HR-Plattform, die außergewöhnlichen Wert für Teams jeder Größe bietet. Sehr empfehlenswert.",
        "platform":"Die Plattform nutzt fortschrittliche Machine-Learning-Algorithmen zur Automatisierung komplexer Aufgaben, Bereitstellung intelligenter Erkenntnisse und effizienterer Teamarbeit. Mit nahtlosen Integrationen und intuitiver Benutzeroberfläche ist {N} zu einer vertrauenswürdigen Lösung für Unternehmen weltweit geworden.",
        "startup":"Ob kleines Startup oder Großunternehmen - {N} skaliert entsprechend Ihren Anforderungen bei hoher Leistung und Zuverlässigkeit."
    },
    "fr":{
        "overview":"Aperçu",
        "is.a":"est une plateforme RH puissante et riche en fonctionnalités qui offre une valeur exceptionnelle pour les équipes de toutes tailles. Fortement recommandé.",
        "platform":"La plateforme exploite des algorithmes d'apprentissage automatique avancés pour automatiser les tâches complexes, fournir des informations intelligentes et permettre aux équipes de travailler plus efficacement. Avec des intégrations transparentes et une interface intuitive, {N} est devenu une solution de confiance pour les organisations du monde entier.",
        "startup":"Que vous soyez une petite startup ou une grande entreprise, {N} s'adapte à vos besoins tout en maintenant des performances et une fiabilité élevées."
    }
}

tools=['beamery','eightfold-ai','fetcher','findem','harver','hirevue','humanly','paradox-olivia','phenom','pymetrics','seekout','sense','textio','workable-ai']

with open('GenuisNet.ai/js/i18n.js','r',encoding='utf-8') as f:
    lines=f.readlines()

# Trouver ligne de section de: (ligne 63042)
de_idx=next(i for i,l in enumerate(lines) if 'de: {' in l and i>60000)

# Insérer après la ligne de: {
insert_lines=[]
for tool in tools:
    n=tool.replace('-',' ').title()
    for lang,t in HR_TRANS.items():
        if lang=='de':
            insert_lines.append(f'        "review.{tool}.overview": "{t["overview"]}",\n')
            insert_lines.append(f'        "review.{tool}.{tool}.is.a": "{n} {t["is.a"]}",\n')
            insert_lines.append(f'        "review.{tool}.the.platform.leverages.advanced.machine": "{t["platform"].replace("{N}",n)}",\n')
            insert_lines.append(f'        "review.{tool}.whether.youre.a.small.startup": "{t["startup"].replace("{N}",n)}",\n')

lines[de_idx+1:de_idx+1]=insert_lines

with open('GenuisNet.ai/js/i18n.js','w',encoding='utf-8') as f:
    f.writelines(lines)

print(f'✓ Ajouté {len(insert_lines)} lignes à i18n.js (section DE)')
print(f'Position: ligne {de_idx+1}')
