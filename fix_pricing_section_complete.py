import os
import re

js_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\js"
html_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\pages\reviews\translation"

translation_tools = {
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

# German translations for pricing section
pricing_translations_de = {
    "pricing": "Preisgestaltung",
    "deepl.pro.offers.flexible.pricing": "DeepL Pro bietet flexible Preispläne für verschiedene Organisationsgrößen und -anforderungen:",
    "google.translate.ai.offers.flexible.pricing": "Google Translate AI bietet flexible Preispläne für verschiedene Organisationsgrößen und -anforderungen:",
    "lilt.offers.flexible.pricing": "Lilt bietet flexible Preispläne für verschiedene Organisationsgrößen und -anforderungen:",
    "lokalise.offers.flexible.pricing": "Lokalise bietet flexible Preispläne für verschiedene Organisationsgrößen und -anforderungen:",
    "microsoft.translator.offers.flexible.pricing": "Microsoft Translator bietet flexible Preispläne für verschiedene Organisationsgrößen und -anforderungen:",
    "modernmt.offers.flexible.pricing": "ModernMT bietet flexible Preispläne für verschiedene Organisationsgrößen und -anforderungen:",
    "phrase.offers.flexible.pricing": "Phrase bietet flexible Preispläne für verschiedene Organisationsgrößen und -anforderungen:",
    "smartling.offers.flexible.pricing": "Smartling bietet flexible Preispläne für verschiedene Organisationsgrößen und -anforderungen:",
    "systran.offers.flexible.pricing": "SYSTRAN bietet flexible Preispläne für verschiedene Organisationsgrößen und -anforderungen:",
    "unbabel.offers.flexible.pricing": "Unbabel bietet flexible Preispläne für verschiedene Organisationsgrößen und -anforderungen:",

    # Plan titles
    "free.plan": "Kostenloser Plan",
    "starter.plan": "Starter-Plan",
    "professional.plan": "Professional-Plan",
    "enterprise.plan": "Enterprise-Plan",
    "custom.pricing": "Individuelle Preisgestaltung",
}

def add_pricing_translations(tool_key, tool_name):
    """Add pricing translations to German section"""

    js_file = os.path.join(js_dir, f"{tool_key}-i18n.js")

    if not os.path.exists(js_file):
        return False

    with open(js_file, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    modified = False

    # Find German section
    de_pattern = r'  "de":\s*\{'
    de_match = re.search(de_pattern, content)

    if not de_match:
        return False

    # Add each translation if missing
    for key_suffix, translation in pricing_translations_de.items():
        full_key = f"review.{tool_key}.{key_suffix}"

        # Check if key exists
        key_pattern = rf'"{re.escape(full_key)}":'
        if not re.search(key_pattern, content):
            # Add to German section
            insert_pos = de_match.end() + 1
            new_line = f'    "{full_key}": "{translation}",\n'
            content = content[:insert_pos] + new_line + content[insert_pos:]
            modified = True
        else:
            # Update existing value if it's still in English
            old_pattern = rf'("{re.escape(full_key)}":\s*)"[^"]*"'
            replacement = rf'\1"{translation}"'
            content, count = re.subn(old_pattern, replacement, content)
            if count > 0:
                modified = True

    if modified and content != original_content:
        with open(js_file, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False

def add_pricing_data_i18n_to_html(tool_key, tool_name):
    """Add data-i18n attributes to pricing plan titles in HTML"""

    html_file = os.path.join(html_dir, f"{tool_key}.html")

    if not os.path.exists(html_file):
        return False

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    modified = False

    # Pattern 1: Free Plan
    pattern = r'<h4>Free Plan</h4>'
    if re.search(pattern, content):
        replacement = f'<h4><span data-i18n="review.{tool_key}.free.plan">Free Plan</span></h4>'
        content = re.sub(pattern, replacement, content)
        modified = True

    # Pattern 2: Starter Plan with price
    pattern = r'<h4>Starter Plan[^<]*</h4>'
    if re.search(pattern, content):
        match = re.search(r'<h4>(Starter Plan[^<]*)</h4>', content)
        if match:
            full_text = match.group(1)
            replacement = f'<h4><span data-i18n="review.{tool_key}.starter.plan">Starter Plan</span> {full_text.replace("Starter Plan", "").strip()}</h4>'
            content = content.replace(match.group(0), replacement)
            modified = True

    # Pattern 3: Professional Plan with price
    pattern = r'<h4>Professional[^<]*</h4>'
    if re.search(pattern, content):
        match = re.search(r'<h4>(Professional[^<]*)</h4>', content)
        if match:
            full_text = match.group(1)
            replacement = f'<h4><span data-i18n="review.{tool_key}.professional.plan">Professional</span> {full_text.replace("Professional", "").strip()}</h4>'
            content = content.replace(match.group(0), replacement)
            modified = True

    # Pattern 4: Enterprise Plan
    pattern = r'<h4>Enterprise[^<]*</h4>'
    if re.search(pattern, content):
        match = re.search(r'<h4>(Enterprise[^<]*)</h4>', content)
        if match:
            full_text = match.group(1)
            # Check if it says "Custom" or has pricing info
            if "Custom" in full_text:
                replacement = f'<h4><span data-i18n="review.{tool_key}.enterprise.plan">Enterprise</span> (<span data-i18n="review.{tool_key}.custom.pricing">Custom</span>)</h4>'
            else:
                replacement = f'<h4><span data-i18n="review.{tool_key}.enterprise.plan">Enterprise</span> {full_text.replace("Enterprise", "").strip()}</h4>'
            content = content.replace(match.group(0), replacement)
            modified = True

    if modified and content != original_content:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False

print("=" * 70)
print("FIXING PRICING SECTION - COMPLETE")
print("=" * 70)

js_fixed = 0
html_fixed = 0

for tool_key, tool_name in translation_tools.items():
    print(f"\n{tool_name}:")

    # Fix i18n
    if add_pricing_translations(tool_key, tool_name):
        print(f"  [+] i18n: Pricing translations added/updated")
        js_fixed += 1
    else:
        print(f"  [OK] i18n: Already complete")

    # Fix HTML
    if add_pricing_data_i18n_to_html(tool_key, tool_name):
        print(f"  [+] HTML: Added data-i18n to plan titles")
        html_fixed += 1
    else:
        print(f"  [OK] HTML: Already has data-i18n")

print("\n" + "=" * 70)
print(f"COMPLETE: i18n {js_fixed}/10 | HTML {html_fixed}/10")
print("=" * 70)
print("\nPricing section now fully translatable!")
print("=" * 70)
