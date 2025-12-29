import os
import re

base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
edu_dir = os.path.join(base_dir, "pages", "reviews", "education")
sales_dir = os.path.join(base_dir, "pages", "reviews", "sales")

edu_tools = [
    "aleks", "carnegie-learning", "century-tech", "cognii",
    "coursera-coach", "duolingo-max", "gradescope", "khan-academy-ai",
    "knewton-alta", "querium", "quizlet-ai", "socratic-by-google",
    "squirrel-ai", "thinkster-math"
]

sales_tools = [
    "6sense", "apolloio", "attention", "chorusai", "clari", "conversica",
    "exceedai", "gong", "hubspot-ai", "insidesales", "lavender", "outreach",
    "peopleai", "regieai", "salesforce-einstein-gpt", "troopsai"
]

def verify_tool(html_file, tool_name):
    """Vérifie qu'un outil a tous les éléments nécessaires"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    checks = {
        'navbar': '<nav class="navbar"' in content,
        'language_selector': 'language-selector' in content,
        'i18n_js': 'i18n.js' in content,
        'nav_i18n_js': 'nav-i18n.js' in content,
        'tool_i18n_js': f'{tool_name}-i18n.js' in content,
        'complete_translate_js': 'complete-translate.js' in content
    }

    return checks

def print_status(checks):
    """Affiche le statut des vérifications"""
    symbols = {True: '[OK]', False: '[NO]'}
    status_line = f"  Navbar: {symbols[checks['navbar']]} | "
    status_line += f"Lang Selector: {symbols[checks['language_selector']]} | "
    status_line += f"i18n.js: {symbols[checks['i18n_js']]} | "
    status_line += f"nav-i18n.js: {symbols[checks['nav_i18n_js']]} | "
    status_line += f"tool-i18n.js: {symbols[checks['tool_i18n_js']]} | "
    status_line += f"complete-translate.js: {symbols[checks['complete_translate_js']]}"
    return status_line

# MAIN
print("=" * 90)
print(" " * 30 + "I18N SETUP VERIFICATION")
print("=" * 90)

print("\n" + "=" * 90)
print("EDUCATION TOOLS (14)")
print("=" * 90)

edu_issues = []
for tool in edu_tools:
    html_file = os.path.join(edu_dir, f"{tool}.html")
    if os.path.exists(html_file):
        checks = verify_tool(html_file, tool)
        print(f"\n{tool}:")
        print(print_status(checks))

        # Vérifier s'il y a des problèmes
        if not all(checks.values()):
            edu_issues.append(tool)
    else:
        print(f"\n{tool}: FILE NOT FOUND")

print("\n" + "=" * 90)
print("SALES TOOLS (16)")
print("=" * 90)

sales_issues = []
for tool in sales_tools:
    html_file = os.path.join(sales_dir, f"{tool}.html")
    if os.path.exists(html_file):
        checks = verify_tool(html_file, tool)
        print(f"\n{tool}:")
        print(print_status(checks))

        # Vérifier s'il y a des problèmes
        if not all(checks.values()):
            sales_issues.append(tool)
    else:
        print(f"\n{tool}: FILE NOT FOUND")

print("\n" + "=" * 90)
print("SUMMARY")
print("=" * 90)
print(f"Education Tools: {len(edu_tools) - len(edu_issues)}/{len(edu_tools)} complete")
if edu_issues:
    print(f"  Issues: {', '.join(edu_issues)}")

print(f"Sales Tools: {len(sales_tools) - len(sales_issues)}/{len(sales_tools)} complete")
if sales_issues:
    print(f"  Issues: {', '.join(sales_issues)}")

print("=" * 90)
