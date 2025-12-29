#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Verify i18n system across ALL categories and ALL tools
"""

import os
import re
import json
from collections import defaultdict

# Base directory
base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
pages_dir = os.path.join(base_dir, "pages", "reviews")
js_dir = os.path.join(base_dir, "js")

print("=" * 80)
print("VERIFICATION OF I18N SYSTEM ACROSS ALL CATEGORIES")
print("=" * 80)
print()

# Get all categories
categories = [d for d in os.listdir(pages_dir) if os.path.isdir(os.path.join(pages_dir, d))]
categories.sort()

print(f"Found {len(categories)} categories")
print()

# Track statistics
total_tools = 0
tools_with_i18n = 0
tools_without_i18n = 0
category_stats = {}

for category in categories:
    category_path = os.path.join(pages_dir, category)

    # Get all HTML files in this category
    html_files = [f for f in os.listdir(category_path) if f.endswith('.html') and not 'backup' in f]

    if not html_files:
        continue

    category_stats[category] = {
        'total': len(html_files),
        'with_i18n': 0,
        'without_i18n': 0,
        'tools': []
    }

    print(f"Category: {category.upper()}")
    print("-" * 80)

    for html_file in html_files:
        tool_name = html_file.replace('.html', '')
        html_path = os.path.join(category_path, html_file)
        i18n_path = os.path.join(js_dir, f"{tool_name}-i18n.js")

        total_tools += 1

        # Check if HTML has data-i18n attributes
        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()

        data_i18n_count = html_content.count('data-i18n=')
        has_html_i18n = data_i18n_count > 0

        # Check if i18n.js file exists
        has_i18n_file = os.path.exists(i18n_path)

        # If i18n file exists, get language count and key count
        lang_count = 0
        key_count = 0
        has_event_listener = False

        if has_i18n_file:
            with open(i18n_path, 'r', encoding='utf-8') as f:
                i18n_content = f.read()

            # Check for event listener
            has_event_listener = "window.addEventListener('languageChanged'" in i18n_content

            # Extract JSON to count languages and keys
            json_match = re.search(r'const\s+\w+\s*=\s*(\{.+?\});', i18n_content, re.DOTALL)
            if json_match:
                try:
                    translations = json.loads(json_match.group(1))
                    lang_count = len(translations)
                    if translations:
                        first_lang = list(translations.keys())[0]
                        key_count = len(translations[first_lang])
                except:
                    pass

        # Determine status
        if has_html_i18n and has_i18n_file and has_event_listener:
            status = "OK"
            tools_with_i18n += 1
            category_stats[category]['with_i18n'] += 1
        else:
            status = "MISSING"
            tools_without_i18n += 1
            category_stats[category]['without_i18n'] += 1

        # Store tool info
        category_stats[category]['tools'].append({
            'name': tool_name,
            'status': status,
            'data_i18n_count': data_i18n_count,
            'has_i18n_file': has_i18n_file,
            'has_event_listener': has_event_listener,
            'lang_count': lang_count,
            'key_count': key_count
        })

        # Print status
        if status == "OK":
            print(f"  [OK] {tool_name}: {data_i18n_count} data-i18n, {key_count} keys, {lang_count} langs")
        else:
            issues = []
            if not has_html_i18n:
                issues.append("no data-i18n in HTML")
            if not has_i18n_file:
                issues.append("no i18n.js file")
            if has_i18n_file and not has_event_listener:
                issues.append("no event listener")
            print(f"  [MISSING] {tool_name}: {', '.join(issues)}")

    print()

# Summary
print("=" * 80)
print("SUMMARY BY CATEGORY")
print("=" * 80)
print()

for category in sorted(category_stats.keys()):
    stats = category_stats[category]
    total = stats['total']
    with_i18n = stats['with_i18n']
    without_i18n = stats['without_i18n']
    percentage = (with_i18n / total * 100) if total > 0 else 0

    status_icon = "✅" if with_i18n == total else "⚠️" if with_i18n > 0 else "❌"

    print(f"{status_icon} {category.upper()}: {with_i18n}/{total} tools ({percentage:.0f}%)")

print()
print("=" * 80)
print("OVERALL SUMMARY")
print("=" * 80)
print()

overall_percentage = (tools_with_i18n / total_tools * 100) if total_tools > 0 else 0

print(f"Total tools: {total_tools}")
print(f"With complete i18n: {tools_with_i18n} ({overall_percentage:.1f}%)")
print(f"Without i18n: {tools_without_i18n} ({100-overall_percentage:.1f}%)")
print()

if tools_without_i18n == 0:
    print("[SUCCESS] All tools have complete i18n system!")
else:
    print(f"[WARNING] {tools_without_i18n} tools need i18n implementation")

print()
print("=" * 80)
