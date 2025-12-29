#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Summary of i18n system across ALL categories - simplified version
"""

import os
import re
import json

# Base directory
base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
pages_dir = os.path.join(base_dir, "pages", "reviews")
js_dir = os.path.join(base_dir, "js")

print("=" * 80)
print("I18N SYSTEM STATUS - ALL CATEGORIES")
print("=" * 80)
print()

# Get all categories
categories = [d for d in os.listdir(pages_dir) if os.path.isdir(os.path.join(pages_dir, d))]
categories.sort()

category_results = {}

for category in categories:
    category_path = os.path.join(pages_dir, category)
    html_files = [f for f in os.listdir(category_path) if f.endswith('.html') and not 'backup' in f]

    if not html_files:
        continue

    total = len(html_files)
    complete = 0
    partial = 0
    missing = 0

    for html_file in html_files:
        tool_name = html_file.replace('.html', '')
        i18n_path = os.path.join(js_dir, f"{tool_name}-i18n.js")

        # Check HTML
        html_path = os.path.join(category_path, html_file)
        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        has_html_i18n = html_content.count('data-i18n=') > 0

        # Check i18n file
        has_i18n_file = os.path.exists(i18n_path)
        has_event_listener = False
        has_translations = False

        if has_i18n_file:
            with open(i18n_path, 'r', encoding='utf-8') as f:
                i18n_content = f.read()
            has_event_listener = "window.addEventListener('languageChanged'" in i18n_content

            json_match = re.search(r'const\s+\w+\s*=\s*(\{.+?\});', i18n_content, re.DOTALL)
            if json_match:
                try:
                    translations = json.loads(json_match.group(1))
                    if translations and len(translations) > 0:
                        first_lang = list(translations.keys())[0]
                        if len(translations[first_lang]) > 0:
                            has_translations = True
                except:
                    pass

        # Categorize
        if has_html_i18n and has_i18n_file and has_event_listener and has_translations:
            complete += 1
        elif has_html_i18n and has_i18n_file:
            partial += 1
        else:
            missing += 1

    category_results[category] = {
        'total': total,
        'complete': complete,
        'partial': partial,
        'missing': missing
    }

# Display results
for category in sorted(category_results.keys()):
    result = category_results[category]
    total = result['total']
    complete = result['complete']
    partial = result['partial']
    missing = result['missing']

    percentage = (complete / total * 100) if total > 0 else 0

    if complete == total:
        status = "[OK]     "
    elif complete > 0:
        status = "[PARTIAL]"
    else:
        status = "[MISSING]"

    print(f"{status} {category.upper():25} {complete:3}/{total:3} complete ({percentage:5.1f}%) | {partial:2} partial | {missing:2} missing")

print()
print("=" * 80)
print("SUMMARY")
print("=" * 80)
print()

total_tools = sum(r['total'] for r in category_results.values())
total_complete = sum(r['complete'] for r in category_results.values())
total_partial = sum(r['partial'] for r in category_results.values())
total_missing = sum(r['missing'] for r in category_results.values())

overall_percentage = (total_complete / total_tools * 100) if total_tools > 0 else 0

print(f"Total tools: {total_tools}")
print(f"Complete i18n: {total_complete} ({overall_percentage:.1f}%)")
print(f"Partial i18n: {total_partial}")
print(f"Missing i18n: {total_missing}")
print()

# Categories breakdown
complete_categories = [cat for cat, res in category_results.items() if res['complete'] == res['total']]
partial_categories = [cat for cat, res in category_results.items() if res['complete'] > 0 and res['complete'] < res['total']]
missing_categories = [cat for cat, res in category_results.items() if res['complete'] == 0]

print(f"Categories 100% complete ({len(complete_categories)}):")
for cat in complete_categories:
    print(f"  - {cat}")

print()
print(f"Categories partially complete ({len(partial_categories)}):")
for cat in partial_categories:
    res = category_results[cat]
    print(f"  - {cat}: {res['complete']}/{res['total']}")

print()
print(f"Categories with no i18n ({len(missing_categories)}):")
for cat in missing_categories:
    print(f"  - {cat}")

print()
print("=" * 80)
