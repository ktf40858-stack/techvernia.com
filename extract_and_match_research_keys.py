import os
import re

base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
research_dir = os.path.join(base_dir, "pages", "reviews", "research")
sales_dir = os.path.join(base_dir, "pages", "reviews", "sales")
js_dir = os.path.join(base_dir, "js")

# Référence
sales_reference = "salesforce-einstein-gpt"
sales_name = "Salesforce Einstein GPT"

research_tools = {
    "consensus": "Consensus"
}

def extract_html_keys(html_file):
    """Extrait toutes les clés data-i18n du HTML"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Trouver tous les data-i18n
    pattern = r'data-i18n="([^"]+)"'
    keys = re.findall(pattern, content)

    return list(set(keys))  # Unique

def load_sales_i18n():
    """Charge toutes les traductions de Sales"""
    sales_file = os.path.join(js_dir, f"{sales_reference}-i18n.js")

    with open(sales_file, 'r', encoding='utf-8') as f:
        content = f.read()

    translations = {}

    for lang in ["en", "de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]:
        pattern = rf'"{lang}":\s*\{{([^}}]+(?:\{{[^}}]*\}}[^}}]*)*)\}}'
        match = re.search(pattern, content, re.DOTALL)

        if match:
            lang_content = match.group(1)
            pairs = re.findall(r'"([^"]+)":\s*"([^"]*(?:\\.[^"]*)*)"', lang_content)
            translations[lang] = dict(pairs)

    return translations

def create_research_translations(html_keys, sales_trans, tool_key, tool_name):
    """Crée les traductions Research basées sur les clés HTML et Sales"""
    research_trans = {}

    for lang in ["en", "de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]:
        research_trans[lang] = {}

        for html_key in html_keys:
            # Convertir la clé Research en clé Sales
            sales_key = html_key.replace(f"review.{tool_key}", f"review.{sales_reference}")

            # Chercher dans les traductions Sales
            if lang in sales_trans and sales_key in sales_trans[lang]:
                value = sales_trans[lang][sales_key]

                # Adapter la valeur
                value = value.replace(sales_name, tool_name)

                # Remplacer les termes spécifiques
                if lang == "en":
                    value = value.replace("sales platform", "research platform")
                    value = value.replace("sales solution", "research solution")
                    value = value.replace("sales organizations", "research organizations")
                    value = value.replace("sales teams", "research teams")
                    value = value.replace("sales needs", "research needs")
                elif lang == "de":
                    value = value.replace("Vertrieb-Plattform", "Forschungsplattform")
                    value = value.replace("Vertrieb-Lösungen", "Forschungslösungen")
                    value = value.replace("Vertriebsorganisationen", "Forschungsorganisationen")
                    value = value.replace("Vertrieb-Anforderungen", "Forschungsanforderungen")

                research_trans[lang][html_key] = value

    return research_trans

def update_i18n_file(tool_key, research_trans):
    """Met à jour le fichier i18n.js avec toutes les traductions"""
    js_file = os.path.join(js_dir, f"{tool_key}-i18n.js")

    # Lire le fichier actuel
    with open(js_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pour chaque langue, remplacer ou ajouter les traductions
    for lang in ["en", "de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]:
        if lang in research_trans and research_trans[lang]:
            # Créer le nouveau contenu de la section
            new_section = f'  "{lang}": {{\n'
            for key, value in sorted(research_trans[lang].items()):
                escaped_value = value.replace('\\', '\\\\').replace('"', '\\"')
                new_section += f'    "{key}": "{escaped_value}",\n'
            new_section = new_section.rstrip(',\n') + '\n  }'

            # Remplacer la section
            pattern = rf'"{lang}":\s*\{{[^}}]*(?:\{{[^}}]*\}}[^}}]*)*\}}'
            content = re.sub(pattern, new_section, content, flags=re.DOTALL)

    # Écrire
    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(content)

    return True

print("=" * 70)
print("EXTRACTING HTML KEYS AND MATCHING WITH SALES TRANSLATIONS")
print("=" * 70)

# Charger Sales
print("\n[1/4] Loading Sales translations...")
sales_trans = load_sales_i18n()
print(f"  Loaded {len(sales_trans['en'])} keys in {len(sales_trans)} languages")

# Pour chaque outil
for tool_key, tool_name in research_tools.items():
    print(f"\n[2/4] Processing {tool_name}...")

    # Extraire les clés HTML
    html_file = os.path.join(research_dir, f"{tool_key}.html")
    html_keys = extract_html_keys(html_file)
    print(f"  Extracted {len(html_keys)} unique keys from HTML")

    # Créer les traductions
    print(f"\n[3/4] Creating translations...")
    research_trans = create_research_translations(html_keys, sales_trans, tool_key, tool_name)
    print(f"  Created {len(research_trans['en'])} translations in {len(research_trans)} languages")

    # Mettre à jour le fichier
    print(f"\n[4/4] Updating i18n file...")
    if update_i18n_file(tool_key, research_trans):
        print(f"  [OK] Updated {tool_key}-i18n.js")

print("\n" + "=" * 70)
print("[COMPLETE] Consensus should now translate properly")
print("=" * 70)
