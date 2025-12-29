#!/usr/bin/env python3
import sys, io, re

if sys.platform=='win32':
    sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

print("🔧 CORRECTION DES TRADUCTIONS TITRES (CAS SPÉCIAUX)")
print("=" * 100)

# Cas spéciaux avec le nom réel
special_cases = {
    'eightfold-ai': 'Eightfold AI',
    'hirevue': 'HireVue',
    'paradox-olivia': 'Paradox (Olivia)',
    'workable-ai': 'Workable AI',
}

for tool, real_name in special_cases.items():
    tool_var = tool.replace('-', '')
    i18n_path = f'GenuisNet.ai/js/{tool}-i18n.js'

    print(f"\n🔧 {tool}...")

    with open(i18n_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Corriger les traductions hero.title pour toutes les langues
    # EN
    content = re.sub(
        r'"review\.' + tool + r'\.hero\.title":\s*"[^"]*"',
        f'"review.{tool}.hero.title": "{real_name} Review"',
        content
    )

    # DE
    content = re.sub(
        r'("de":.{1,2000}?"review\.' + tool + r'\.hero\.title":\s*)"[^"]*"',
        rf'\1"{real_name} Bewertung"',
        content,
        flags=re.DOTALL
    )

    # FR
    content = re.sub(
        r'("fr":.{1,2000}?"review\.' + tool + r'\.hero\.title":\s*)"[^"]*"',
        rf'\1"Avis {real_name}"',
        content,
        flags=re.DOTALL
    )

    # ES
    content = re.sub(
        r'("es":.{1,2000}?"review\.' + tool + r'\.hero\.title":\s*)"[^"]*"',
        rf'\1"Revisión de {real_name}"',
        content,
        flags=re.DOTALL
    )

    # PT
    content = re.sub(
        r'("pt":.{1,2000}?"review\.' + tool + r'\.hero\.title":\s*)"[^"]*"',
        rf'\1"Avaliação {real_name}"',
        content,
        flags=re.DOTALL
    )

    # ZH
    content = re.sub(
        r'("zh":.{1,2000}?"review\.' + tool + r'\.hero\.title":\s*)"[^"]*"',
        rf'\1"{real_name} 评测"',
        content,
        flags=re.DOTALL
    )

    # JA
    content = re.sub(
        r'("ja":.{1,2000}?"review\.' + tool + r'\.hero\.title":\s*)"[^"]*"',
        rf'\1"{real_name} レビュー"',
        content,
        flags=re.DOTALL
    )

    # KO
    content = re.sub(
        r'("ko":.{1,2000}?"review\.' + tool + r'\.hero\.title":\s*)"[^"]*"',
        rf'\1"{real_name} 리뷰"',
        content,
        flags=re.DOTALL
    )

    # AR
    content = re.sub(
        r'("ar":.{1,2000}?"review\.' + tool + r'\.hero\.title":\s*)"[^"]*"',
        rf'\1"مراجعة {real_name}"',
        content,
        flags=re.DOTALL
    )

    # HI
    content = re.sub(
        r'("hi":.{1,2000}?"review\.' + tool + r'\.hero\.title":\s*)"[^"]*"',
        rf'\1"{real_name} समीक्षा"',
        content,
        flags=re.DOTALL
    )

    with open(i18n_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  ✅ Traductions corrigées pour: {real_name}")

print(f"\n{'='*100}")
print("✅ TOUTES LES TRADUCTIONS CORRIGÉES!")
print(f"{'='*100}")
