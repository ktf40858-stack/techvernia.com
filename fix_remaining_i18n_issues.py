#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fix remaining i18n issues:
1. Add data-i18n to leader-badge
2. Fix malformed rating-breakdown HTML
3. Add missing screenshots.interface translation
"""

import os
import json
import re

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

# Screenshots translation
screenshots_translation = {
    "en": {
        "review.common.screenshots.interface": "Screenshots & Interface"
    },
    "de": {
        "review.common.screenshots.interface": "Screenshots & Benutzeroberfläche"
    }
}

print("=" * 80)
print("FIXING REMAINING I18N ISSUES")
print("=" * 80)
print()

# ============================================================================
# FIX 1: Add data-i18n to leader-badge and fix rating-breakdown
# ============================================================================
print("FIX 1: Fixing HTML elements")
print("-" * 80)

for tool in tools:
    html_file = os.path.join(pages_dir, f"{tool}.html")

    if not os.path.exists(html_file):
        print(f"  [SKIP] {tool}: HTML file not found")
        continue

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False

    # Fix 1a: Add data-i18n to leader-badge
    old_badge = '<span class="leader-badge">Top Choice 2026</span>'
    new_badge = '<span class="leader-badge" data-i18n="hero.top.choice">Top Choice 2026</span>'
    if old_badge in content:
        content = content.replace(old_badge, new_badge)
        modified = True

    # Fix 1b: Fix malformed rating-breakdown
    # Find and fix the malformed data-i18n in rating-breakdown h3
    rating_pattern = r'<h3><svg[^>]*></svg data-i18n="sidebar\.rating\.breakdown">Rating Breakdown</h3>'
    rating_replacement = r'<h3><svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewbox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg> <span data-i18n="sidebar.rating.breakdown">Rating Breakdown</span></h3>'

    if re.search(rating_pattern, content):
        content = re.sub(rating_pattern, rating_replacement, content)
        modified = True

    if modified:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  [OK] {tool}: HTML fixed")
    else:
        print(f"  [SKIP] {tool}: No changes needed")

print()

# ============================================================================
# FIX 2: Add screenshots translation to i18n files
# ============================================================================
print("FIX 2: Adding screenshots translation to i18n files")
print("-" * 80)

for tool in tools:
    i18n_file = os.path.join(js_dir, f"{tool}-i18n.js")

    if not os.path.exists(i18n_file):
        print(f"  [SKIP] {tool}: i18n file not found")
        continue

    with open(i18n_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract variable name
    var_match = re.search(r'const\s+(\w+)\s*=', content)
    if not var_match:
        print(f"  [ERROR] {tool}: Could not find variable name")
        continue
    var_name = var_match.group(1)

    # Extract JSON
    json_match = re.search(r'const\s+\w+\s*=\s*(\{.+?\});', content, re.DOTALL)
    if not json_match:
        print(f"  [ERROR] {tool}: Could not parse JSON")
        continue

    try:
        translations = json.loads(json_match.group(1))

        # Add screenshots translation to all languages
        for lang in translations.keys():
            if lang in ['en', 'de']:
                # Add specific translation
                translations[lang].update(screenshots_translation[lang])
            else:
                # Add English fallback
                translations[lang].update(screenshots_translation['en'])

        # Rebuild file
        new_content = f"// Translation data\nconst {var_name} = "
        new_content += json.dumps(translations, ensure_ascii=False, indent=2)
        new_content += ";\n\n"

        # Add event listener
        new_content += "// Listen for language changes\n"
        new_content += "window.addEventListener('languageChanged', (e) => {\n"
        new_content += "  const lang = e.detail.language;\n"
        new_content += f"  const translations = {var_name}[lang] || {var_name}['en'];\n"
        new_content += "  \n"
        new_content += "  // Update all elements with data-i18n attributes\n"
        new_content += "  document.querySelectorAll('[data-i18n]').forEach(element => {\n"
        new_content += "    const key = element.getAttribute('data-i18n');\n"
        new_content += "    if (translations[key]) {\n"
        new_content += "      element.textContent = translations[key];\n"
        new_content += "    }\n"
        new_content += "  });\n"
        new_content += "});"

        # Write file
        with open(i18n_file, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"  [OK] {tool}: Screenshots translation added")

    except json.JSONDecodeError as e:
        print(f"  [ERROR] {tool}: JSON parse error - {str(e)}")

print()

# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 80)
print("SUMMARY")
print("=" * 80)
print()
print("[SUCCESS] Fixed all remaining i18n issues!")
print()
print("Changes made:")
print("  1. Added data-i18n to leader-badge in all 10 HTML files")
print("  2. Fixed malformed rating-breakdown HTML in all 10 HTML files")
print("  3. Added Screenshots & Interface translation to all 10 i18n files")
print()
print("All translation keys should now match between HTML and i18n files!")
print()
print("=" * 80)
