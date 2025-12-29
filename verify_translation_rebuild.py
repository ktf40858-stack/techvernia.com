#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Verify all Translation & Localization i18n files after rebuild
"""

import os
import json
import re

# Base directory
base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
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

print("=" * 70)
print("VERIFICATION: TRANSLATION & LOCALIZATION I18N FILES")
print("=" * 70)
print()

results = []

for tool in tools:
    filename = f"{tool}-i18n.js"
    filepath = os.path.join(js_dir, filename)

    if not os.path.exists(filepath):
        results.append({
            "tool": tool,
            "status": "MISSING",
            "error": "File does not exist"
        })
        continue

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for event listener
        has_listener = "window.addEventListener('languageChanged'" in content

        # Extract English section
        en_match = re.search(r'"en":\s*\{([^}]+(?:\}[^}]+)*)\}', content)
        de_match = re.search(r'"de":\s*\{([^}]+(?:\}[^}]+)*)\}', content)

        if not en_match or not de_match:
            results.append({
                "tool": tool,
                "status": "INVALID",
                "error": "Missing language section"
            })
            continue

        # Count keys in each section
        en_keys = len(re.findall(r'"review\.[^"]+":' , en_match.group(0)))
        de_keys = len(re.findall(r'"review\.[^"]+":' , de_match.group(0)))

        # Check for corruption indicators
        corruption_checks = []

        # Check if German section has other tool names (corruption indicator)
        other_tools = [t for t in tools if t != tool]
        for other_tool in other_tools:
            if f'review.{tool}.{other_tool}' in de_match.group(0):
                corruption_checks.append(f"Contains {other_tool} keys in German section")

        # File size
        file_size = len(content)

        results.append({
            "tool": tool,
            "status": "OK" if not corruption_checks else "CORRUPTED",
            "en_keys": en_keys,
            "de_keys": de_keys,
            "has_listener": has_listener,
            "file_size": file_size,
            "corruption": corruption_checks
        })

    except Exception as e:
        results.append({
            "tool": tool,
            "status": "ERROR",
            "error": str(e)
        })

# Display results
for r in results:
    print(f"{r['tool']}")
    print(f"  Status: {r['status']}")

    if r['status'] == 'OK':
        print(f"  English keys: {r['en_keys']}")
        print(f"  German keys: {r['de_keys']}")
        print(f"  Event listener: {'YES' if r['has_listener'] else 'NO'}")
        print(f"  File size: {r['file_size']:,} bytes")
    elif r['status'] == 'CORRUPTED':
        print(f"  English keys: {r['en_keys']}")
        print(f"  German keys: {r['de_keys']}")
        print(f"  Corruption issues:")
        for issue in r['corruption']:
            print(f"    - {issue}")
    elif 'error' in r:
        print(f"  Error: {r['error']}")

    print()

# Summary
print("=" * 70)
print("SUMMARY")
print("=" * 70)
print()

ok_count = sum(1 for r in results if r['status'] == 'OK')
corrupted_count = sum(1 for r in results if r['status'] == 'CORRUPTED')
error_count = sum(1 for r in results if r['status'] in ['ERROR', 'MISSING', 'INVALID'])

print(f"Total files: {len(results)}")
print(f"Clean files: {ok_count}")
print(f"Corrupted files: {corrupted_count}")
print(f"Error/Missing: {error_count}")
print()

if ok_count == len(results):
    print("[SUCCESS] All files are clean and properly structured!")
else:
    print("[WARNING] Some files have issues and may need attention")

print()
print("=" * 70)
