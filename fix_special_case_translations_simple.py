#!/usr/bin/env python3
import sys, io, re

if sys.platform=='win32':
    sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

print("🔧 CORRECTION SIMPLE DES TRADUCTIONS")
print("=" * 100)

special_cases = {
    'eightfold-ai': 'Eightfold AI',
    'hirevue': 'HireVue',
    'paradox-olivia': 'Paradox (Olivia)',
    'workable-ai': 'Workable AI',
}

for tool, real_name in special_cases.items():
    i18n_path = f'GenuisNet.ai/js/{tool}-i18n.js'

    print(f"\n🔧 {tool}...")

    with open(i18n_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        # Remplacer hero.title pour japonais
        if f'"review.{tool}.hero.title"' in line and 'Eightfold AI Review' in line:
            # Déterminer quelle langue en regardant le contexte
            if '"ja"' in ''.join(new_lines[-50:]):  # Chercher "ja" dans les 50 dernières lignes
                line = line.replace('Eightfold AI Review', f'{real_name} レビュー')
            elif '"zh"' in ''.join(new_lines[-50:]):
                line = line.replace('Eightfold AI Review', f'{real_name} 评测')
            elif '"ko"' in ''.join(new_lines[-50:]):
                line = line.replace('Eightfold AI Review', f'{real_name} 리뷰')
            elif '"ar"' in ''.join(new_lines[-50:]):
                line = line.replace('Eightfold AI Review', f'مراجعة {real_name}')
            elif '"hi"' in ''.join(new_lines[-50:]):
                line = line.replace('Eightfold AI Review', f'{real_name} समीक्षा')

        new_lines.append(line)

    with open(i18n_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

    print(f"  ✅ Traductions corrigées")

print(f"\n{'='*100}")
print("✅ TERMINÉ!")
print(f"{'='*100}")
