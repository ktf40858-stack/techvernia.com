#!/usr/bin/env python3
"""Monitor completion of Customer Service & Support translations"""

import os
import json
import sys

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

CUSTOMER_SERVICE_DIR = 'GenuisNet.ai/pages/reviews/customer-service'

# Exclude drift (already translated in business category)
TOOLS = [
    'ada', 'certainly', 'cognigy', 'forethought', 'freshdesk-ai',
    'helpshift', 'intercom-fin', 'kustomer', 'liveperson', 'netomi',
    'polyai', 'ultimateai', 'yellowai', 'zendesk-ai'
]

print("=" * 70)
print("CUSTOMER SERVICE & SUPPORT - TRANSLATION COMPLETION MONITOR")
print("=" * 70)

total_tools = 0
complete_tools = 0
partial_tools = 0
missing_tools = 0

for tool in TOOLS:
    print(f"\n{tool.upper()}:")
    print("-" * 70)

    batches_found = 0
    total_langs = 0

    for batch_num in [1, 2, 3]:
        batch_file = os.path.join(CUSTOMER_SERVICE_DIR, f"{tool}-batch{batch_num}.json")

        if os.path.exists(batch_file):
            try:
                with open(batch_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    langs = [lang for lang in data if data[lang]]
                    total_langs += len(langs)
                    print(f"  batch{batch_num}: {len(langs)} languages ({', '.join(langs)})")
                    batches_found += 1
            except:
                print(f"  batch{batch_num}: ERROR reading file")
        else:
            print(f"  batch{batch_num}: NOT FOUND")

    # Check for en.json
    en_file = os.path.join(CUSTOMER_SERVICE_DIR, f"{tool}-en.json")
    has_english = os.path.exists(en_file)
    if has_english:
        print(f"  English base: FOUND")

    # Calculate completion
    expected_langs = 9  # es, fr, de, pt, zh, ja, ko, ar, hi
    completion_pct = (total_langs / expected_langs * 100) if expected_langs > 0 else 0

    print(f"\n  Status: {total_langs}/9 languages ({completion_pct:.1f}%)")

    if batches_found == 3 and total_langs == 9:
        print(f"  [COMPLETE] All translations ready!")
        complete_tools += 1
    elif batches_found >= 1:
        print(f"  [PARTIAL] {3 - batches_found} batch(es) missing")
        partial_tools += 1
    else:
        print(f"  [MISSING] No translations found")
        missing_tools += 1

    total_tools += 1

print("\n" + "=" * 70)
print(f"SUMMARY:")
print(f"  Complete: {complete_tools}/{total_tools} tools")
print(f"  Partial:  {partial_tools}/{total_tools} tools")
print(f"  Missing:  {missing_tools}/{total_tools} tools")
print("=" * 70)
