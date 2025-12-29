import os
import re

base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
research_dir = os.path.join(base_dir, "pages", "reviews", "research")
js_dir = os.path.join(base_dir, "js")

tools = [
    "connected-papers", "consensus", "elicit", "irisai", "litmaps",
    "perplexity-research", "researchrabbit", "scholarcy", "scispace",
    "scite", "semantic-scholar", "undermind"
]

print("=" * 80)
print(" " * 20 + "AI RESEARCH & ACADEMIA - VERIFICATION REPORT")
print("=" * 80)

print("\n" + "-" * 80)
print(f"{'Tool':<25} {'Navbar':<10} {'Scripts':<10} {'FAQ h4':<10} {'i18n EN':<10} {'i18n DE':<10}")
print("-" * 80)

complete_tools = 0

for tool in tools:
    html_file = os.path.join(research_dir, f"{tool}.html")
    js_file = os.path.join(js_dir, f"{tool}-i18n.js")

    # Vérifications
    has_navbar = False
    has_scripts = False
    faq_count = 0
    en_keys = 0
    de_keys = 0

    if os.path.exists(html_file):
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()

        # Vérifier la navbar avec le sélecteur de langue
        has_navbar = 'class="language-selector"' in html_content and 'id="lang-btn"' in html_content

        # Vérifier les scripts i18n
        has_scripts = (f'src="../../../js/{tool}-i18n.js"' in html_content and
                      'src="../../../js/nav-i18n.js"' in html_content)

        # Compter les questions FAQ avec data-i18n
        faq_section = re.search(r'<section[^>]*id="faq"[^>]*>(.*?)</section>', html_content, re.DOTALL)
        if faq_section:
            faq_count = len(re.findall(r'<h4><span data-i18n=', faq_section.group(1)))

    if os.path.exists(js_file):
        with open(js_file, 'r', encoding='utf-8') as f:
            js_content = f.read()

        # Compter les clés FAQ en anglais
        en_section = re.search(r'"en":\s*\{([^}]+(?:\{[^}]*\}[^}]*)*)\}', js_content, re.DOTALL)
        if en_section:
            en_keys = len(re.findall(r'"[^"]*\.faq\.[^"]*":', en_section.group(1)))

        # Compter les clés FAQ en allemand
        de_section = re.search(r'"de":\s*\{([^}]+(?:\{[^}]*\}[^}]*)*)\}', js_content, re.DOTALL)
        if de_section:
            de_keys = len(re.findall(r'"[^"]*\.faq\.[^"]*":', de_section.group(1)))

    # Déterminer si l'outil est complet
    is_complete = has_navbar and has_scripts and faq_count == 8 and en_keys == 8 and de_keys == 8

    if is_complete:
        complete_tools += 1

    # Affichage
    status = "[OK]" if is_complete else "[!]"
    print(f"{tool:<25} {'YES' if has_navbar else 'NO':<10} {'YES' if has_scripts else 'NO':<10} {faq_count:<10} {en_keys:<10} {de_keys:<10} {status}")

print("-" * 80)
print(f"\n[SUMMARY] {complete_tools}/{len(tools)} tools fully implemented")

if complete_tools == len(tools):
    print("[SUCCESS] All Research tools have complete i18n implementation!")
else:
    print(f"[WARNING] {len(tools) - complete_tools} tools need attention")

print("=" * 80)
