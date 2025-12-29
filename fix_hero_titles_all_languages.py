#!/usr/bin/env python3
import sys, io

if sys.platform=='win32':
    sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

print("🔧 CORRECTION DES HERO TITLES POUR TOUTES LES LANGUES")
print("=" * 100)

special_cases = {
    'eightfold-ai': 'Eightfold AI',
    'hirevue': 'HireVue',
    'paradox-olivia': 'Paradox (Olivia)',
    'workable-ai': 'Workable AI',
}

# Traductions du mot "Review" / "Bewertung" etc.
review_translations = {
    'en': 'Review',
    'de': 'Bewertung',
    'fr': 'Avis',
    'es': 'Revisión de',
    'pt': 'Avaliação',
    'zh': '评测',
    'ja': 'レビュー',
    'ko': '리뷰',
    'ar': 'مراجعة',
    'hi': 'समीक्षा',
}

for tool, real_name in special_cases.items():
    i18n_path = f'GenuisNet.ai/js/{tool}-i18n.js'

    print(f"\n🔧 {tool} ({real_name})...")

    with open(i18n_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    current_lang = None
    new_lines = []
    changes = 0

    for line in lines:
        # Détecter la langue actuelle
        if '"en": {' in line:
            current_lang = 'en'
        elif '"de": {' in line:
            current_lang = 'de'
        elif '"fr": {' in line:
            current_lang = 'fr'
        elif '"es": {' in line:
            current_lang = 'es'
        elif '"pt": {' in line:
            current_lang = 'pt'
        elif '"zh": {' in line:
            current_lang = 'zh'
        elif '"ja": {' in line:
            current_lang = 'ja'
        elif '"ko": {' in line:
            current_lang = 'ko'
        elif '"ar": {' in line:
            current_lang = 'ar'
        elif '"hi": {' in line:
            current_lang = 'hi'

        # Remplacer hero.title si on le trouve
        if current_lang and f'"review.{tool}.hero.title"' in line:
            # Construire la bonne traduction
            if current_lang == 'es':
                translation = f'{review_translations[current_lang]} {real_name}'
            elif current_lang in ['ar']:
                translation = f'{review_translations[current_lang]} {real_name}'
            else:
                translation = f'{real_name} {review_translations[current_lang]}'

            # Remplacer la ligne
            line = f'      "review.{tool}.hero.title": "{translation}",\n'
            changes += 1

        new_lines.append(line)

    with open(i18n_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

    print(f"  ✅ {changes} traductions corrigées")

print(f"\n{'='*100}")
print("✅ TOUTES LES TRADUCTIONS HERO.TITLE CORRIGÉES!")
print(f"{'='*100}")
