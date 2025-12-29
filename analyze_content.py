#!/usr/bin/env python3
"""Analyze i18n content breakdown"""

import json
import os

TOOLS = [
    'datarobot',
    'domo-ai',
    'h2oai',
    'microstrategy-ai',
    'power-bi-copilot',
    'qlik-sense-ai',
    'sisense-ai',
    'yellowfin-ai'
]

ANALYTICS_DIR = 'GenuisNet.ai/pages/reviews/analytics'

print("=" * 70)
print("Analytics Tools Content Breakdown")
print("=" * 70)

for tool in TOOLS:
    en_file = os.path.join(ANALYTICS_DIR, f"{tool}-en.json")

    try:
        with open(en_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        total_keys = len(data)
        faq_keys = len([k for k in data.keys() if '.faq.' in k or 'frequently.asked' in k.lower()])
        other_keys = total_keys - faq_keys

        print(f"\n{tool}:")
        print(f"  Total keys: {total_keys}")
        print(f"  FAQ keys: {faq_keys} ({faq_keys*100//total_keys}%)")
        print(f"  Other content: {other_keys} ({other_keys*100//total_keys}%)")

    except Exception as e:
        print(f"\n{tool}: ERROR - {e}")

print("\n" + "=" * 70)
print("Ces fichiers contiennent TOUT le contenu des pages, pas seulement les FAQs!")
print("=" * 70)
