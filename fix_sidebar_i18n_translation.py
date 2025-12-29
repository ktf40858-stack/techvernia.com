#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fix sidebar i18n for Translation tools
Add data-i18n attributes and translations for:
- Quick Info section
- Rating Breakdown section
- Table of Contents section
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

# Common sidebar translations
sidebar_translations = {
    "en": {
        "sidebar.rating.breakdown": "Rating Breakdown",
        "sidebar.features": "Features",
        "sidebar.ease.of.use": "Ease of Use",
        "sidebar.value": "Value",
        "sidebar.support": "Support",
        "sidebar.performance": "Performance",
        "sidebar.quick.info": "Quick Info",
        "sidebar.category": "Category",
        "sidebar.pricing": "Pricing",
        "sidebar.from.free": "From Free",
        "sidebar.free.trial": "Free Trial",
        "sidebar.platform": "Platform",
        "sidebar.web.mobile": "Web, Mobile",
        "sidebar.table.of.contents": "Table of Contents",
        "sidebar.overview": "Overview",
        "sidebar.key.features": "Key Features",
        "sidebar.pros.cons": "Pros & Cons",
        "sidebar.pricing.section": "Pricing",
        "sidebar.use.cases": "Use Cases",
        "sidebar.comparison": "Comparison",
        "sidebar.faq": "FAQ",
        "sidebar.final.verdict": "Final Verdict"
    },
    "de": {
        "sidebar.rating.breakdown": "Bewertungsaufschlüsselung",
        "sidebar.features": "Funktionen",
        "sidebar.ease.of.use": "Benutzerfreundlichkeit",
        "sidebar.value": "Preis-Leistungs-Verhältnis",
        "sidebar.support": "Support",
        "sidebar.performance": "Leistung",
        "sidebar.quick.info": "Kurzinfo",
        "sidebar.category": "Kategorie",
        "sidebar.pricing": "Preise",
        "sidebar.from.free": "Ab kostenlos",
        "sidebar.free.trial": "Kostenlose Testversion",
        "sidebar.platform": "Plattform",
        "sidebar.web.mobile": "Web, Mobil",
        "sidebar.table.of.contents": "Inhaltsverzeichnis",
        "sidebar.overview": "Übersicht",
        "sidebar.key.features": "Hauptmerkmale",
        "sidebar.pros.cons": "Vor- und Nachteile",
        "sidebar.pricing.section": "Preisgestaltung",
        "sidebar.use.cases": "Anwendungsfälle",
        "sidebar.comparison": "Vergleich",
        "sidebar.faq": "FAQ",
        "sidebar.final.verdict": "Abschließendes Urteil"
    }
}

def fix_sidebar_html(tool_key):
    """Fix sidebar HTML by adding data-i18n attributes"""

    html_file = os.path.join(pages_dir, f"{tool_key}.html")

    if not os.path.exists(html_file):
        return False

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix Rating Breakdown
    content = content.replace(
        '> Rating Breakdown</h3>',
        ' data-i18n="sidebar.rating.breakdown">Rating Breakdown</h3>'
    )

    # Fix rating labels
    replacements = [
        ('<span class="label">Features</span>', '<span class="label" data-i18n="sidebar.features">Features</span>'),
        ('<span class="label">Ease of Use</span>', '<span class="label" data-i18n="sidebar.ease.of.use">Ease of Use</span>'),
        ('<span class="label">Value</span>', '<span class="label" data-i18n="sidebar.value">Value</span>'),
        ('<span class="label">Support</span>', '<span class="label" data-i18n="sidebar.support">Support</span>'),
        ('<span class="label">Performance</span>', '<span class="label" data-i18n="sidebar.performance">Performance</span>'),
    ]

    for old, new in replacements:
        content = content.replace(old, new)

    # Fix Quick Info
    content = re.sub(
        r'<h3>ℹ️ Quick Info</h3>',
        '<h3><span data-i18n="sidebar.quick.info">Quick Info</span></h3>',
        content
    )

    # Fix Quick Info labels
    quick_info_replacements = [
        ('<span class="stat-label">Category</span>', '<span class="stat-label" data-i18n="sidebar.category">Category</span>'),
        ('<span class="stat-label">Pricing</span>', '<span class="stat-label" data-i18n="sidebar.pricing">Pricing</span>'),
        ('<span class="stat-value">From Free</span>', '<span class="stat-value" data-i18n="sidebar.from.free">From Free</span>'),
        ('<span class="stat-label">Free Trial</span>', '<span class="stat-label" data-i18n="sidebar.free.trial">Free Trial</span>'),
        ('<span class="stat-label">Platform</span>', '<span class="stat-label" data-i18n="sidebar.platform">Platform</span>'),
        ('<span class="stat-value">Web, Mobile</span>', '<span class="stat-value" data-i18n="sidebar.web.mobile">Web, Mobile</span>'),
    ]

    for old, new in quick_info_replacements:
        content = content.replace(old, new)

    # Fix Table of Contents
    content = re.sub(
        r'<h3>📑 Table of Contents</h3>',
        '<h3><span data-i18n="sidebar.table.of.contents">Table of Contents</span></h3>',
        content
    )

    # Fix TOC links
    toc_replacements = [
        ('>Overview</a>', ' data-i18n="sidebar.overview">Overview</a>'),
        ('>Key Features</a>', ' data-i18n="sidebar.key.features">Key Features</a>'),
        ('>Pros &amp; Cons</a>', ' data-i18n="sidebar.pros.cons">Pros &amp; Cons</a>'),
        ('>Pricing</a>', ' data-i18n="sidebar.pricing.section">Pricing</a>'),
        ('>Use Cases</a>', ' data-i18n="sidebar.use.cases">Use Cases</a>'),
        ('>Comparison</a>', ' data-i18n="sidebar.comparison">Comparison</a>'),
        ('>FAQ</a>', ' data-i18n="sidebar.faq">FAQ</a>'),
        ('>Final Verdict</a>', ' data-i18n="sidebar.final.verdict">Final Verdict</a>'),
    ]

    for old, new in toc_replacements:
        content = content.replace(old, new)

    # Write back
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)

    return True

def add_sidebar_translations_to_i18n(tool_key):
    """Add sidebar translations to i18n file"""

    i18n_file = os.path.join(js_dir, f"{tool_key}-i18n.js")

    if not os.path.exists(i18n_file):
        return False

    with open(i18n_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract variable name
    var_match = re.search(r'const\s+(\w+)\s*=', content)
    if not var_match:
        return False
    var_name = var_match.group(1)

    # Extract existing translations
    json_match = re.search(r'const\s+\w+\s*=\s*(\{.+?\});', content, re.DOTALL)
    if not json_match:
        return False

    json_str = json_match.group(1)
    translations = json.loads(json_str)

    # Add sidebar translations to all languages
    for lang in translations.keys():
        if lang in ['en', 'de']:
            # Add specific translations for EN and DE
            translations[lang].update(sidebar_translations[lang])
        else:
            # Add English fallback for other languages
            translations[lang].update(sidebar_translations['en'])

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
    new_content += "});\n"

    # Write file
    with open(i18n_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True

# Main execution
print("=" * 70)
print("FIXING SIDEBAR I18N FOR TRANSLATION TOOLS")
print("=" * 70)
print()

results = []

for tool in tools:
    print(f"Processing {tool}...")

    try:
        html_fixed = fix_sidebar_html(tool)
        i18n_fixed = add_sidebar_translations_to_i18n(tool)

        if html_fixed and i18n_fixed:
            results.append({"tool": tool, "status": "SUCCESS"})
            print(f"  [OK] HTML and i18n updated")
        else:
            results.append({"tool": tool, "status": "ERROR"})
            print(f"  [ERROR] Failed to update files")
    except Exception as e:
        results.append({"tool": tool, "status": "ERROR", "error": str(e)})
        print(f"  [ERROR] {str(e)}")

    print()

# Summary
print("=" * 70)
print("SUMMARY")
print("=" * 70)
print()

success_count = sum(1 for r in results if r["status"] == "SUCCESS")

print(f"Tools processed: {len(results)}")
print(f"Successfully updated: {success_count}")
print()

if success_count == len(results):
    print("[SUCCESS] All sidebars now have complete i18n support!")
    print()
    print("Sidebar elements now translating:")
    print("  - Rating Breakdown")
    print("  - Quick Info")
    print("  - Table of Contents")
else:
    print("[WARNING] Some tools had errors")

print()
print("=" * 70)
