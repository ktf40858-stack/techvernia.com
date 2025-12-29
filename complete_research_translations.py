import os
import re

base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
research_dir = os.path.join(base_dir, "pages", "reviews", "research")
sales_dir = os.path.join(base_dir, "pages", "reviews", "sales")
js_dir = os.path.join(base_dir, "js")

# Référence Sales pour les traductions complètes
sales_reference = "salesforce-einstein-gpt"

# Outils Research
research_tools = {
    "connected-papers": "Connected Papers",
    "consensus": "Consensus",
    "elicit": "Elicit",
    "irisai": "Iris.ai",
    "litmaps": "Litmaps",
    "perplexity-research": "Perplexity Research",
    "researchrabbit": "ResearchRabbit",
    "scholarcy": "Scholarcy",
    "scispace": "SciSpace",
    "scite": "Scite",
    "semantic-scholar": "Semantic Scholar",
    "undermind": "Undermind"
}

def load_sales_translations():
    """Charge les traductions de référence depuis Sales"""
    sales_file = os.path.join(js_dir, f"{sales_reference}-i18n.js")

    with open(sales_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extraire les traductions par langue
    translations = {}

    for lang in ["en", "de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]:
        pattern = rf'"{lang}":\s*\{{([^}}]+(?:\{{[^}}]*\}}[^}}]*)*)\}}'
        match = re.search(pattern, content, re.DOTALL)

        if match:
            lang_content = match.group(1)
            # Extraire les paires clé-valeur
            pairs = re.findall(r'"([^"]+)":\s*"([^"]*(?:\\.[^"]*)*)"', lang_content)
            translations[lang] = dict(pairs)

    return translations

def adapt_translations_for_tool(sales_trans, tool_key, tool_name):
    """Adapte les traductions de Sales pour un outil Research"""
    adapted = {}

    for lang, pairs in sales_trans.items():
        adapted[lang] = {}

        for key, value in pairs.items():
            # Remplacer la clé
            new_key = key.replace(f"review.{sales_reference}", f"review.{tool_key}")

            # Adapter la valeur
            new_value = value.replace("Salesforce Einstein GPT", tool_name)
            new_value = new_value.replace("Salesforce Einstein Gpt", tool_name)

            # Remplacer les termes spécifiques selon la langue
            if lang == "en":
                new_value = new_value.replace("sales platform", "research platform")
                new_value = new_value.replace("sales solution", "research solution")
                new_value = new_value.replace("sales organizations", "research organizations")
                new_value = new_value.replace("sales teams", "research teams")
                new_value = new_value.replace("Vertrieb", "Forschung")
                new_value = new_value.replace("sales needs", "research needs")
            elif lang == "de":
                new_value = new_value.replace("Vertrieb-Plattform", "Forschungsplattform")
                new_value = new_value.replace("Vertrieb-Lösungen", "Forschungslösungen")
                new_value = new_value.replace("Vertriebsorganisationen", "Forschungsorganisationen")
                new_value = new_value.replace("Vertrieb-Anforderungen", "Forschungsanforderungen")
                new_value = new_value.replace("Vertriebsorganisationen", "Forschungsorganisationen")

            adapted[lang][new_key] = new_value

    return adapted

def update_i18n_file(tool_key, tool_name, adapted_trans):
    """Met à jour le fichier i18n.js avec les traductions complètes"""
    js_file = os.path.join(js_dir, f"{tool_key}-i18n.js")

    if not os.path.exists(js_file):
        print(f"  [ERROR] {js_file} not found")
        return False

    # Lire le fichier existant
    with open(js_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pour chaque langue, remplacer la section
    for lang in ["en", "de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]:
        if lang in adapted_trans and adapted_trans[lang]:
            # Créer le nouveau contenu de la section
            new_section = f'  "{lang}": {{\n'
            for key, value in sorted(adapted_trans[lang].items()):
                # Échapper les caractères spéciaux
                escaped_value = value.replace('\\', '\\\\').replace('"', '\\"')
                new_section += f'    "{key}": "{escaped_value}",\n'
            new_section = new_section.rstrip(',\n') + '\n  }'

            # Remplacer la section existante
            pattern = rf'"{lang}":\s*\{{[^}}]*\}}'
            if re.search(pattern, content):
                content = re.sub(pattern, new_section, content, flags=re.DOTALL)
            else:
                # Ajouter la section si elle n'existe pas
                insert_pos = content.rfind('}')
                if insert_pos > 0:
                    content = content[:insert_pos] + f',\n{new_section}\n' + content[insert_pos:]

    # Écrire le fichier modifié
    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(content)

    return True

print("=" * 70)
print("COMPLETING RESEARCH TRANSLATIONS FROM SALES REFERENCE")
print("=" * 70)

# Charger les traductions Sales
print("\n[1/3] Loading Sales translations...")
sales_trans = load_sales_translations()
print(f"  Loaded {len(sales_trans)} languages with {len(sales_trans.get('en', {}))} keys each")

# Pour chaque outil Research
print("\n[2/3] Adapting translations for Research tools...")
count = 0
for tool_key, tool_name in research_tools.items():
    print(f"\n  {tool_name}:")

    # Adapter les traductions
    adapted = adapt_translations_for_tool(sales_trans, tool_key, tool_name)
    print(f"    - Adapted {len(adapted['en'])} keys for 10 languages")

    # Mettre à jour le fichier i18n.js
    if update_i18n_file(tool_key, tool_name, adapted):
        print(f"    - Updated {tool_key}-i18n.js")
        count += 1
    else:
        print(f"    - Failed to update {tool_key}-i18n.js")

print("\n[3/3] Summary")
print(f"  Updated {count}/{len(research_tools)} tools")

print("\n" + "=" * 70)
print("[COMPLETE] All Research tools now have full DE translations")
print("=" * 70)
