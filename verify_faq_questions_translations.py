import os
import re

base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
sales_dir = os.path.join(base_dir, "pages", "reviews", "sales")
js_dir = os.path.join(base_dir, "js")

tools = [
    "6sense", "apolloio", "attention", "chorusai", "clari", "conversica",
    "exceedai", "gong", "hubspot-ai", "insidesales", "lavender", "outreach",
    "peopleai", "regieai", "salesforce-einstein-gpt", "troopsai"
]

def check_faq_in_html(html_file):
    """Vérifie que les questions FAQ ont des data-i18n"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Trouver toutes les h4 dans la section FAQ
    faq_section = re.search(r'<section class="review-section" id="faq">(.*?)</section>', content, re.DOTALL)
    if not faq_section:
        return 0, 0

    faq_content = faq_section.group(1)

    # Compter les h4 au total
    total_h4 = len(re.findall(r'<h4>', faq_content))

    # Compter les h4 avec data-i18n
    h4_with_i18n = len(re.findall(r'<h4><span data-i18n=', faq_content))

    return total_h4, h4_with_i18n

def check_faq_in_i18n(js_file):
    """Vérifie que les traductions FAQ existent dans i18n.js"""
    if not os.path.exists(js_file):
        return 0, 0

    with open(js_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Compter les clés FAQ en anglais
    en_section = re.search(r'"en":\s*(\{[^}]+(?:\{[^}]*\}[^}]*)*\})', content, re.DOTALL)
    if not en_section:
        return 0, 0

    en_faq_keys = len(re.findall(r'"[^"]*\.faq\.[^"]*":', en_section.group(1)))

    # Compter les clés FAQ en allemand
    de_section = re.search(r'"de":\s*(\{[^}]+(?:\{[^}]*\}[^}]*)*\})', content, re.DOTALL)
    if not de_section:
        return en_faq_keys, 0

    de_faq_keys = len(re.findall(r'"[^"]*\.faq\.[^"]*":', de_section.group(1)))

    return en_faq_keys, de_faq_keys

# MAIN
print("=" * 80)
print(" " * 20 + "FAQ QUESTIONS TRANSLATION VERIFICATION")
print("=" * 80)

print("\n" + "-" * 80)
print(f"{'Tool':<30} {'HTML h4':<12} {'h4+i18n':<12} {'EN Keys':<12} {'DE Keys':<12}")
print("-" * 80)

total_tools = 0
complete_tools = 0

for tool in tools:
    html_file = os.path.join(sales_dir, f"{tool}.html")
    js_file = os.path.join(js_dir, f"{tool}-i18n.js")

    if os.path.exists(html_file) and os.path.exists(js_file):
        total_h4, h4_with_i18n = check_faq_in_html(html_file)
        en_keys, de_keys = check_faq_in_i18n(js_file)

        status = "[OK]" if (h4_with_i18n == total_h4 and en_keys > 0 and de_keys > 0) else "[!]"
        print(f"{tool:<30} {total_h4:<12} {h4_with_i18n:<12} {en_keys:<12} {de_keys:<12} {status}")

        total_tools += 1
        if h4_with_i18n == total_h4 and en_keys > 0 and de_keys > 0:
            complete_tools += 1
    else:
        print(f"{tool:<30} FILE NOT FOUND")

print("-" * 80)
print(f"\nComplete: {complete_tools}/{total_tools} tools have all FAQ questions translated")
print("=" * 80)
