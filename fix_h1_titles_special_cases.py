#!/usr/bin/env python3
import sys, io, os

if sys.platform=='win32':
    sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

print("🔧 CORRECTION DES TITRES H1 (CAS SPÉCIAUX)")
print("=" * 100)

# Cas spéciaux avec le nom réel dans le HTML
special_cases = {
    'eightfold-ai': 'Eightfold AI',
    'hirevue': 'HireVue',
    'paradox-olivia': 'Paradox (Olivia)',
    'workable-ai': 'Workable AI',
}

for tool, real_name in special_cases.items():
    html_file = f'GenuisNet.ai/pages/reviews/hr/{tool}.html'

    if not os.path.exists(html_file):
        continue

    print(f"\n📄 {tool}...")

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern actuel (sans data-i18n)
    old_pattern = f'<h1>{real_name} Review</h1>'

    # Nouveau pattern (avec data-i18n)
    new_pattern = f'<h1><span data-i18n="review.{tool}.hero.title">{real_name} Review</span></h1>'

    if old_pattern in content:
        content = content.replace(old_pattern, new_pattern)

        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"  ✅ Titre H1 corrigé: {real_name} Review")
    else:
        print(f"  ⏭️  Déjà corrigé ou pattern non trouvé")

print(f"\n{'='*100}")
print("✅ CORRECTION TERMINÉE!")
print(f"{'='*100}")
