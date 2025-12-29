#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Verify all Translation tools have complete translations
"""

import os
import re
from bs4 import BeautifulSoup

# Base directory
base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
pages_dir = os.path.join(base_dir, "pages", "reviews", "translation")
js_dir = os.path.join(base_dir, "js")

# All 10 Translation tools
tools = {
    "deepl-pro": "DeepL Pro",
    "google-translate-ai": "Google Translate AI",
    "lilt": "Lilt",
    "lokalise": "Lokalise",
    "microsoft-translator": "Microsoft Translator",
    "modernmt": "ModernMT",
    "phrase": "Phrase",
    "smartling": "Smartling",
    "systran": "SYSTRAN",
    "unbabel": "Unbabel"
}

def verify_tool(tool_key, tool_name):
    """Verify a single tool has complete translations"""

    html_file = os.path.join(pages_dir, f"{tool_key}.html")
    i18n_file = os.path.join(js_dir, f"{tool_key}-i18n.js")

    results = {
        "tool": tool_name,
        "html_exists": os.path.exists(html_file),
        "i18n_exists": os.path.exists(i18n_file),
        "html_keys": 0,
        "i18n_en_keys": 0,
        "i18n_de_keys": 0,
        "missing_keys": [],
        "english_in_german": [],
        "status": "UNKNOWN"
    }

    if not results["html_exists"] or not results["i18n_exists"]:
        results["status"] = "MISSING FILES"
        return results

    # Extract HTML keys
    with open(html_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    html_keys = set()
    elements = soup.find_all(attrs={'data-i18n': True})
    for elem in elements:
        key = elem.get('data-i18n')
        if key.startswith(f'review.{tool_key}'):
            html_keys.add(key)

    results["html_keys"] = len(html_keys)

    # Extract i18n keys
    with open(i18n_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract English keys
    en_match = re.search(r'"en":\s*\{([^}]+(?:\}[^}]+)*)\}', content, re.DOTALL)
    if en_match:
        en_keys = set(re.findall(r'"(review\.[^"]+)":', en_match.group(0)))
        results["i18n_en_keys"] = len(en_keys)
    else:
        en_keys = set()

    # Extract German keys
    de_match = re.search(r'"de":\s*\{([^}]+(?:\}[^}]+)*)\}', content, re.DOTALL)
    if de_match:
        de_section = de_match.group(0)
        de_keys = set(re.findall(r'"(review\.[^"]+)":', de_section))
        results["i18n_de_keys"] = len(de_keys)

        # Check for English text in German section
        # Look for common English phrases that should be translated
        english_patterns = [
            r'":\s*"[^"]*\bThe platform leverages\b',
            r'":\s*"[^"]*\bWhether you\'re a small startup\b',
            r'":\s*"[^"]*\bFor most organizations, yes\b',
            r'":\s*"[^"]*\bMost teams can get started\b',
            r'":\s*"[^"]*\bintegrates with 100\+\b',
            r'":\s*"[^"]*\bYes\. .+ uses bank-grade\b',
            r'":\s*"[^"]*\bAbsolutely\. .+ provides migration\b',
            r'":\s*"[^"]*\bProfessional plans include email\b',
            r'":\s*"[^"]*\bYes! You can try all\b',
            r'":\s*"[^"]*\bThe AI engine learns\b'
        ]

        for pattern in english_patterns:
            matches = re.findall(pattern, de_section)
            if matches:
                results["english_in_german"].extend(matches)
    else:
        de_keys = set()

    # Find missing keys
    results["missing_keys"] = list(html_keys - de_keys)

    # Determine status
    if results["missing_keys"]:
        results["status"] = "MISSING KEYS"
    elif results["english_in_german"]:
        results["status"] = "ENGLISH IN GERMAN"
    elif results["i18n_en_keys"] != results["i18n_de_keys"]:
        results["status"] = "KEY MISMATCH"
    else:
        results["status"] = "OK"

    return results

# Main execution
print("=" * 80)
print("VERIFICATION: ALL TRANSLATION TOOLS")
print("=" * 80)
print()

all_results = []

for tool_key, tool_name in tools.items():
    print(f"Checking {tool_name}...")
    result = verify_tool(tool_key, tool_name)
    all_results.append(result)

    if result["status"] == "OK":
        print(f"  [OK] HTML: {result['html_keys']} keys, i18n: EN={result['i18n_en_keys']}, DE={result['i18n_de_keys']}")
    elif result["status"] == "MISSING FILES":
        print(f"  [ERROR] Missing files - HTML: {result['html_exists']}, i18n: {result['i18n_exists']}")
    elif result["status"] == "MISSING KEYS":
        print(f"  [WARN] {len(result['missing_keys'])} keys missing in German section")
        print(f"         HTML: {result['html_keys']}, i18n EN: {result['i18n_en_keys']}, DE: {result['i18n_de_keys']}")
    elif result["status"] == "ENGLISH IN GERMAN":
        print(f"  [WARN] English text found in German section ({len(result['english_in_german'])} instances)")
        print(f"         HTML: {result['html_keys']}, i18n EN: {result['i18n_en_keys']}, DE: {result['i18n_de_keys']}")
    elif result["status"] == "KEY MISMATCH":
        print(f"  [WARN] EN/DE key count mismatch")
        print(f"         HTML: {result['html_keys']}, i18n EN: {result['i18n_en_keys']}, DE: {result['i18n_de_keys']}")

    print()

# Summary
print("=" * 80)
print("SUMMARY")
print("=" * 80)
print()

ok_count = sum(1 for r in all_results if r["status"] == "OK")
warn_count = sum(1 for r in all_results if r["status"] not in ["OK", "MISSING FILES"])
error_count = sum(1 for r in all_results if r["status"] == "MISSING FILES")

print(f"Total tools: {len(all_results)}")
print(f"OK: {ok_count}")
print(f"Warnings: {warn_count}")
print(f"Errors: {error_count}")
print()

if ok_count == len(all_results):
    print("[SUCCESS] All tools have complete translations!")
else:
    print("[ATTENTION] Some tools need fixes:")
    print()
    for r in all_results:
        if r["status"] != "OK":
            print(f"  {r['tool']}: {r['status']}")
            if r["missing_keys"]:
                print(f"    Missing keys: {len(r['missing_keys'])}")
                for key in r["missing_keys"][:5]:  # Show first 5
                    print(f"      - {key}")
                if len(r["missing_keys"]) > 5:
                    print(f"      ... and {len(r['missing_keys']) - 5} more")
            if r["english_in_german"]:
                print(f"    English in German: {len(r['english_in_german'])} instances")

print()
print("=" * 80)
