#!/usr/bin/env python3
"""Monitor Legal & Compliance translation agent progress"""

import os
import glob
import json

LEGAL_DIR = 'GenuisNet.ai/pages/reviews/legal'

print("=" * 70)
print("LEGAL & COMPLIANCE - TRANSLATION AGENT MONITOR")
print("=" * 70)

tools = [
    'blue-j-legal', 'casetext', 'cocounsel', 'everlaw', 'harvey-ai',
    'kira-systems', 'lawgeex', 'lex-machina', 'luminance', 'primer',
    'ravel-law', 'ross-intelligence'
]

# Count batch files
print("\nBatch files created:")
batch_count = 0
for tool in tools:
    tool_batches = []
    for batch_num in [1, 2, 3]:
        filepath = os.path.join(LEGAL_DIR, f"{tool}-batch{batch_num}.json")
        if os.path.exists(filepath):
            size = os.path.getsize(filepath)
            if size > 100:
                tool_batches.append(f"batch{batch_num}")
                batch_count += 1

    if tool_batches:
        print(f"  {tool}: {', '.join(tool_batches)}")

print(f"\nTotal batch files: {batch_count}/36 (12 tools x 3 batches)")

# Check language coverage
print("\n" + "-" * 70)
print("Language Coverage Check:")

languages = ['es', 'fr', 'de', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']
lang_status = {lang: 0 for lang in languages}

for tool in tools:
    for batch_num in [1, 2, 3]:
        filepath = os.path.join(LEGAL_DIR, f"{tool}-batch{batch_num}.json")
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for lang in languages:
                        if lang in data and data[lang]:
                            lang_status[lang] += 1
            except:
                pass

print("\nLanguages completed (out of 12 tools):")
for lang, count in sorted(lang_status.items()):
    status = "[COMPLETE]" if count == 12 else f"[{count}/12]"
    print(f"  {lang.upper()}: {status}")

# Calculate completion percentage
total_possible = 12 * 9  # 12 tools x 9 languages
total_completed = sum(lang_status.values())
percentage = (total_completed / total_possible) * 100

print("\n" + "=" * 70)
print(f"OVERALL PROGRESS: {total_completed}/{total_possible} ({percentage:.1f}%)")
print("=" * 70)
