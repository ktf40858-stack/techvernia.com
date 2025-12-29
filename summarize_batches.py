#!/usr/bin/env python3
"""Summarize background task batch files"""

import json
import os

TOOLS = ['sisense-ai', 'power-bi-copilot', 'datarobot']
ANALYTICS_DIR = 'GenuisNet.ai/pages/reviews/analytics'

print("=" * 70)
print("Background Tasks Summary - Analytics Translations")
print("=" * 70)

for tool in TOOLS:
    print(f"\n{'='*70}")
    print(f"TASK: Translate {tool} batches 1-3")
    print(f"{'='*70}")
    
    total_langs = 0
    total_keys = 0
    all_languages = set()
    
    for batch_num in [1, 2, 3]:
        batch_file = os.path.join(ANALYTICS_DIR, f"{tool}-batch{batch_num}.json")
        
        if not os.path.exists(batch_file):
            print(f"  Batch {batch_num}: FILE NOT FOUND")
            continue
            
        try:
            with open(batch_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            non_empty_langs = {lang: len(content) for lang, content in data.items() if content}
            
            if non_empty_langs:
                print(f"  Batch {batch_num}: SUCCESS")
                for lang, key_count in non_empty_langs.items():
                    print(f"    - {lang.upper()}: {key_count} keys translated")
                    all_languages.add(lang)
                    total_keys += key_count
            else:
                print(f"  Batch {batch_num}: EMPTY (no translations)")
                
        except Exception as e:
            print(f"  Batch {batch_num}: ERROR - {str(e)[:50]}")
    
    if all_languages:
        print(f"\n  SUMMARY:")
        print(f"    Languages completed: {', '.join(sorted(all_languages))}")
        print(f"    Total translations: {total_keys} keys")
        print(f"    Status: PARTIAL (needs pt, zh, ja, ko, ar, hi)")
    else:
        print(f"\n  SUMMARY: NO TRANSLATIONS COMPLETED")

print("\n" + "=" * 70)
print("OVERALL STATUS")
print("=" * 70)
print("Completed languages across all tools: es, fr, de, pt (partial)")
print("Missing languages: zh, ja, ko, ar, hi")
print("=" * 70)
