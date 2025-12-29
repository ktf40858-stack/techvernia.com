#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Script pour diagnostiquer le problème i18n dans la catégorie HR"""

import re
import os
from pathlib import Path

hr_tools = [
    'beamery', 'eightfold-ai', 'fetcher', 'findem', 'harver', 'hirevue',
    'humanly', 'paradox-olivia', 'phenom', 'pymetrics', 'seekout',
    'sense', 'textio', 'workable-ai'
]

base_path = Path('GenuisNet.ai/js')

import sys
import io
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("="*80)
print("DIAGNOSTIC - Problème de traduction catégorie AI HR & Recruiting")
print("="*80)
print()

for tool in hr_tools:
    i18n_file = base_path / f'{tool}-i18n.js'

    if not i18n_file.exists():
        print(f"❌ {tool}: Fichier i18n MANQUANT")
        continue

    with open(i18n_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extraire la section chinoise
    zh_match = re.search(r'"zh":\s*{([^}]+(?:}[^}]+)*)}(?=\s*,\s*"[a-z]{2}":|$)', content, re.DOTALL)

    if not zh_match:
        print(f"❌ {tool}: Section chinoise (zh) INTROUVABLE")
        continue

    zh_section = zh_match.group(1)

    # Vérifier si Overview est traduit
    overview_match = re.search(r'"review\.' + tool.replace('-', r'[-\.]') + r'\.overview":\s*"([^"]+)"', zh_section)

    if overview_match:
        translation = overview_match.group(1)
        if translation == "Overview":
            print(f"⚠️  {tool}: PROBLÈME - 'Overview' non traduit (reste en anglais)")
        elif '概述' in translation or '概览' in translation:
            print(f"✅ {tool}: OK - Overview correctement traduit")
        else:
            print(f"⚠️  {tool}: INCERTAIN - Overview = '{translation}'")
    else:
        print(f"❌ {tool}: Clé 'overview' NON TROUVÉE")

print()
print("="*80)
print("Analyse terminée")
print("="*80)
