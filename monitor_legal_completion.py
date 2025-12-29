#!/usr/bin/env python3
"""Monitor completion of kira-systems and luminance translations"""

import os
import json
import sys

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

LEGAL_DIR = 'GenuisNet.ai/pages/reviews/legal'

print("=" * 70)
print("LEGAL TOOLS - TRANSLATION COMPLETION MONITOR")
print("=" * 70)

tools = ['kira-systems', 'luminance']

for tool in tools:
    print(f"\n{tool.upper()}:")
    print("-" * 70)

    batches_found = 0
    total_langs = 0

    for batch_num in [1, 2, 3]:
        batch_file = os.path.join(LEGAL_DIR, f"{tool}-batch{batch_num}.json")

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

    # Calculate completion
    expected_langs = 9  # es, fr, de, pt, zh, ja, ko, ar, hi
    completion_pct = (total_langs / expected_langs * 100) if expected_langs > 0 else 0

    print(f"\n  Status: {total_langs}/9 languages ({completion_pct:.1f}%)")

    if batches_found == 3 and total_langs == 9:
        print(f"  [COMPLETE] All translations ready!")
    elif batches_found >= 2:
        print(f"  [PARTIAL] {3 - batches_found} batch(es) missing")
    else:
        print(f"  [INCOMPLETE] Only batch1 available")

print("\n" + "=" * 70)
