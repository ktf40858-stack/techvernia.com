#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Comprehensive verification of the complete translation system
Checks:
1. All HTML files load correct i18n scripts
2. All i18n files have languageChanged event listener
3. All data-i18n keys in HTML exist in i18n files
4. All languages have same number of keys
"""

import os
import re
import json
from bs4 import BeautifulSoup

# Base directory
base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
pages_dir = os.path.join(base_dir, "pages", "reviews", "translation")
js_dir = os.path.join(base_dir, "js")

# All 10 Translation tools
tools = [
    "deepl-pro",
    "google-translate-ai",
    "lilt",
    "lokalise",
    "microsoft-translator",
    "modernmt",
    "phrase",
    "smartling",
    "systran",
    "unbabel"
]

print("=" * 80)
print("COMPLETE TRANSLATION SYSTEM VERIFICATION")
print("=" * 80)
print()

# ============================================================================
# CHECK 1: Verify all HTML files load correct scripts
# ============================================================================
print("CHECK 1: Verifying script tags in HTML files")
print("-" * 80)

html_script_issues = []

for tool in tools:
    html_file = os.path.join(pages_dir, f"{tool}.html")

    if not os.path.exists(html_file):
        html_script_issues.append(f"{tool}: HTML file not found")
        continue

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check for required scripts
    has_i18n = '<script src="../../../js/i18n.js"></script>' in content
    has_nav_i18n = '<script src="../../../js/nav-i18n.js"></script>' in content
    has_tool_i18n = f'<script src="../../../js/{tool}-i18n.js"></script>' in content

    if not has_i18n:
        html_script_issues.append(f"{tool}: Missing i18n.js")
    if not has_nav_i18n:
        html_script_issues.append(f"{tool}: Missing nav-i18n.js")
    if not has_tool_i18n:
        html_script_issues.append(f"{tool}: Missing {tool}-i18n.js")

    if has_i18n and has_nav_i18n and has_tool_i18n:
        print(f"  [OK] {tool}: All scripts loaded")

if html_script_issues:
    print()
    print("  [WARNING] Issues found:")
    for issue in html_script_issues:
        print(f"    - {issue}")
else:
    print()
    print("  [SUCCESS] All HTML files have correct script tags!")

print()

# ============================================================================
# CHECK 2: Verify all i18n files have languageChanged event listener
# ============================================================================
print("CHECK 2: Verifying languageChanged event listener in i18n files")
print("-" * 80)

i18n_listener_issues = []

for tool in tools:
    i18n_file = os.path.join(js_dir, f"{tool}-i18n.js")

    if not os.path.exists(i18n_file):
        i18n_listener_issues.append(f"{tool}: i18n file not found")
        continue

    with open(i18n_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check for event listener
    has_listener = "window.addEventListener('languageChanged'" in content or \
                   'window.addEventListener("languageChanged"' in content

    if has_listener:
        print(f"  [OK] {tool}: Has languageChanged listener")
    else:
        i18n_listener_issues.append(f"{tool}: Missing languageChanged listener")

if i18n_listener_issues:
    print()
    print("  [WARNING] Issues found:")
    for issue in i18n_listener_issues:
        print(f"    - {issue}")
else:
    print()
    print("  [SUCCESS] All i18n files have event listeners!")

print()

# ============================================================================
# CHECK 3: Verify all data-i18n keys exist in translation files
# ============================================================================
print("CHECK 3: Verifying data-i18n keys match translation files")
print("-" * 80)

key_mismatch_issues = []

for tool in tools:
    html_file = os.path.join(pages_dir, f"{tool}.html")
    i18n_file = os.path.join(js_dir, f"{tool}-i18n.js")

    if not os.path.exists(html_file) or not os.path.exists(i18n_file):
        continue

    # Extract data-i18n keys from HTML
    with open(html_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    html_keys = set()
    for elem in soup.find_all(attrs={'data-i18n': True}):
        key = elem.get('data-i18n')
        # Only check tool-specific keys (not sidebar/hero which are common)
        if key.startswith('review.') or key.startswith('sidebar.') or key.startswith('hero.'):
            html_keys.add(key)

    # Extract keys from i18n file
    with open(i18n_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract JSON
    json_match = re.search(r'const\s+\w+\s*=\s*(\{.+?\});', content, re.DOTALL)
    if not json_match:
        key_mismatch_issues.append(f"{tool}: Could not parse i18n file")
        continue

    try:
        translations = json.loads(json_match.group(1))

        # Get keys from English translation
        if 'en' in translations:
            i18n_keys = set(translations['en'].keys())
        else:
            key_mismatch_issues.append(f"{tool}: No English translations found")
            continue

        # Find missing keys
        missing_in_i18n = html_keys - i18n_keys
        missing_in_html = i18n_keys - html_keys

        if not missing_in_i18n and not missing_in_html:
            print(f"  [OK] {tool}: All keys match ({len(html_keys)} keys)")
        else:
            if missing_in_i18n:
                key_mismatch_issues.append(f"{tool}: {len(missing_in_i18n)} keys in HTML missing from i18n")
            if missing_in_html:
                key_mismatch_issues.append(f"{tool}: {len(missing_in_html)} keys in i18n missing from HTML")
            print(f"  [WARNING] {tool}: Key mismatch detected")

    except json.JSONDecodeError as e:
        key_mismatch_issues.append(f"{tool}: JSON parse error - {str(e)}")

if key_mismatch_issues:
    print()
    print("  [WARNING] Issues found:")
    for issue in key_mismatch_issues:
        print(f"    - {issue}")
else:
    print()
    print("  [SUCCESS] All keys match between HTML and i18n files!")

print()

# ============================================================================
# CHECK 4: Verify all languages have same number of keys
# ============================================================================
print("CHECK 4: Verifying all languages have consistent key counts")
print("-" * 80)

lang_consistency_issues = []

for tool in tools:
    i18n_file = os.path.join(js_dir, f"{tool}-i18n.js")

    if not os.path.exists(i18n_file):
        continue

    with open(i18n_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract JSON
    json_match = re.search(r'const\s+\w+\s*=\s*(\{.+?\});', content, re.DOTALL)
    if not json_match:
        continue

    try:
        translations = json.loads(json_match.group(1))

        # Count keys per language
        key_counts = {lang: len(keys) for lang, keys in translations.items()}

        # Check if all counts are the same
        if len(set(key_counts.values())) == 1:
            count = list(key_counts.values())[0]
            print(f"  [OK] {tool}: All {len(key_counts)} languages have {count} keys")
        else:
            lang_consistency_issues.append(f"{tool}: Inconsistent key counts - {key_counts}")
            print(f"  [WARNING] {tool}: Inconsistent key counts")

    except json.JSONDecodeError:
        continue

if lang_consistency_issues:
    print()
    print("  [WARNING] Issues found:")
    for issue in lang_consistency_issues:
        print(f"    - {issue}")
else:
    print()
    print("  [SUCCESS] All languages have consistent key counts!")

print()

# ============================================================================
# FINAL SUMMARY
# ============================================================================
print("=" * 80)
print("FINAL SUMMARY")
print("=" * 80)
print()

total_issues = len(html_script_issues) + len(i18n_listener_issues) + \
               len(key_mismatch_issues) + len(lang_consistency_issues)

if total_issues == 0:
    print("[SUCCESS] Complete translation system verified!")
    print()
    print("✓ All HTML files load correct scripts")
    print("✓ All i18n files have languageChanged listeners")
    print("✓ All data-i18n keys match translation files")
    print("✓ All languages have consistent key counts")
    print()
    print("READY FOR PRODUCTION!")
    print()
    print("How the system works:")
    print("1. User selects language from language selector")
    print("2. i18n.js dispatches 'languageChanged' event")
    print("3. nav-i18n.js updates navigation")
    print("4. tool-specific i18n.js updates page content")
    print("5. auto-translate.js translates remaining generic text")
else:
    print(f"[WARNING] Found {total_issues} issues that need attention")
    print()
    print(f"  HTML script issues: {len(html_script_issues)}")
    print(f"  Event listener issues: {len(i18n_listener_issues)}")
    print(f"  Key mismatch issues: {len(key_mismatch_issues)}")
    print(f"  Language consistency issues: {len(lang_consistency_issues)}")

print()
print("=" * 80)
