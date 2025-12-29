import os
import json
import re

base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
sales_dir = os.path.join(base_dir, "pages", "reviews", "sales")
js_dir = os.path.join(base_dir, "js")

# Tous les outils AI Sales & CRM
tools = [
    "6sense",
    "apolloio",
    "attention",
    "chorusai",
    "clari",
    "conversica",
    "exceedai",
    "gong",
    "hubspot-ai",
    "insidesales",
    "lavender",
    "outreach",
    "peopleai",
    "regieai",
    "salesforce-einstein-gpt",
    "troopsai"
]

def tool_to_camel(tool):
    """Convertit le nom de l'outil en camelCase"""
    # Cas spéciaux
    if tool == "6sense":
        return "sixSense"
    if tool == "apolloio":
        return "apolloio"
    if tool == "salesforce-einstein-gpt":
        return "salesforceEinsteinGpt"

    parts = tool.split('-')
    return parts[0] + ''.join(p.capitalize() for p in parts[1:])

def tool_to_title(tool):
    """Convertit le nom de l'outil en Title Case"""
    if tool == "6sense":
        return "6sense"
    if tool == "apolloio":
        return "Apollo.io"
    if tool == "chorusai":
        return "Chorus.ai"
    if tool == "exceedai":
        return "Exceed.ai"
    if tool == "peopleai":
        return "People.ai"
    if tool == "regieai":
        return "Regie.ai"
    if tool == "troopsai":
        return "Troops.ai"
    if tool == "salesforce-einstein-gpt":
        return "Salesforce Einstein GPT"
    if tool == "hubspot-ai":
        return "HubSpot AI"
    if tool == "insidesales":
        return "InsideSales"

    return ' '.join(p.capitalize() for p in tool.split('-'))

def load_ada_i18n():
    """Charge toutes les traductions d'Ada depuis le fichier i18n.js"""
    ada_js = os.path.join(base_dir, "js", "ada-i18n.js")

    with open(ada_js, 'r', encoding='utf-8') as f:
        content = f.read()

    all_translations = {}
    languages = ["en", "de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]

    for lang in languages:
        pattern = rf'"{lang}":\s*(\{{[^}}]+(?:\{{[^}}]*\}}[^}}]*)*\}})'
        match = re.search(pattern, content, re.DOTALL)

        if match:
            lang_dict = {}
            key_pattern = r'"([^"]+)":\s*"([^"]*(?:\\.[^"]*)*)"'
            matches = re.findall(key_pattern, match.group(1))
            for key, value in matches:
                clean_value = value.replace('\\"', '"')
                lang_dict[key] = clean_value
            all_translations[lang] = lang_dict

    return all_translations

def extract_html_translations(html_file):
    """Extrait toutes les clés et textes anglais du HTML"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern pour extraire data-i18n avec le texte
    pattern = r'<span data-i18n="([^"]+)">([^<]+)</span>'
    matches = re.findall(pattern, content)

    en_translations = {}
    for key, text in matches:
        en_translations[key] = text.strip()

    return en_translations

def find_best_ada_match(en_text, ada_translations):
    """Trouve la meilleure correspondance Ada pour un texte anglais"""
    en_text_normalized = en_text.lower().strip()

    # Chercher dans les traductions Ada EN
    if "en" in ada_translations:
        for ada_key, ada_en_text in ada_translations["en"].items():
            ada_normalized = ada_en_text.lower().strip()

            # Remplacer "Ada" et "customer service" pour comparer
            ada_normalized = ada_normalized.replace("ada", "")
            ada_normalized = ada_normalized.replace("customer service", "")
            ada_normalized = ada_normalized.replace("customer-service", "")

            en_text_comp = en_text_normalized.replace("sales", "").replace("crm", "")

            # Si les textes sont similaires
            if ada_normalized in en_text_comp or en_text_comp in ada_normalized:
                return ada_key

            # Vérifier les premiers 50 caractères
            if len(ada_normalized) > 50 and len(en_text_comp) > 50:
                if ada_normalized[:50] in en_text_comp or en_text_comp[:50] in ada_normalized:
                    return ada_key

    return None

def adapt_for_sales(text, tool_display):
    """Adapte le texte pour Sales & CRM"""
    adapted = text.replace("Ada", tool_display)
    adapted = adapted.replace("ada", tool_display.lower())

    replacements = {
        # English
        "customer service": "sales",
        "customer-service": "sales",
        "modern businesses": "modern sales teams",
        "organizations": "sales organizations",

        # German
        "Kundenservice": "Vertrieb",
        "Kundendienst": "Vertrieb",
        "moderne Unternehmen": "moderne Vertriebsteams",
        "Organisationen": "Vertriebsorganisationen",

        # Spanish
        "servicio al cliente": "ventas",
        "atención al cliente": "ventas",
        "empresas modernas": "equipos de ventas modernos",
        "organizaciones": "organizaciones de ventas",

        # French
        "service client": "ventes",
        "entreprises modernes": "équipes de vente modernes",
        "organisations": "organisations de vente",

        # Portuguese
        "atendimento ao cliente": "vendas",
        "empresas modernas": "equipes de vendas modernas",
        "organizações": "organizações de vendas",

        # Chinese
        "客户服务": "销售",
        "现代企业": "现代销售团队",
        "组织": "销售组织",

        # Japanese
        "カスタマーサービス": "セールス",
        "現代の企業": "現代の営業チーム",
        "組織": "営業組織",

        # Korean
        "고객 서비스": "영업",
        "현대 기업": "현대 영업 팀",
        "조직": "영업 조직",

        # Arabic
        "خدمة العملاء": "المبيعات",
        "الشركات الحديثة": "فرق المبيعات الحديثة",
        "المنظمات": "منظمات المبيعات",

        # Hindi
        "ग्राहक सेवा": "बिक्री",
        "आधुनिक व्यवसाय": "आधुनिक बिक्री टीमें",
        "संगठन": "बिक्री संगठन"
    }

    for old, new in replacements.items():
        adapted = adapted.replace(old, new)

    return adapted

def create_complete_translations(tool):
    """Crée les traductions complètes basées sur le HTML et Ada"""
    html_file = os.path.join(sales_dir, f"{tool}.html")
    tool_display = tool_to_title(tool)

    # Vérifier si le fichier HTML existe
    if not os.path.exists(html_file):
        print(f"  [SKIP] {tool}.html not found")
        return None

    # Extraire les clés et textes du HTML
    html_en_trans = extract_html_translations(html_file)

    if not html_en_trans:
        print(f"  [SKIP] {tool}.html has no data-i18n attributes")
        return None

    # Charger Ada
    ada_translations = load_ada_i18n()

    # Créer les traductions pour toutes les langues
    all_translations = {}
    languages = ["en", "de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]

    for lang in languages:
        all_translations[lang] = {}

    # Pour chaque clé HTML
    for html_key, en_text in html_en_trans.items():
        # Ajouter l'anglais directement
        all_translations["en"][html_key] = en_text

        # Trouver la correspondance Ada
        ada_key = find_best_ada_match(en_text, ada_translations)

        if ada_key:
            # Copier les traductions Ada adaptées
            for lang in ["de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]:
                if lang in ada_translations and ada_key in ada_translations[lang]:
                    ada_text = ada_translations[lang][ada_key]
                    adapted_text = adapt_for_sales(ada_text, tool_display)
                    all_translations[lang][html_key] = adapted_text

    return all_translations

def rebuild_i18n_file(tool, translations):
    """Reconstruit le fichier i18n.js"""
    camel_name = tool_to_camel(tool)
    title_name = tool_to_title(tool)

    js_content = f"// {title_name.upper()} I18N\n"
    js_content += f"const {camel_name}Translations = {{\n"

    languages = ["en", "de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]

    for idx, lang in enumerate(languages):
        if lang in translations and translations[lang]:
            js_content += f'  "{lang}": {json.dumps(translations[lang], indent=4, ensure_ascii=False)}'
            if idx < len(languages) - 1:
                js_content += ","
            js_content += "\n"

    js_content += "};\n\n"

    js_content += f"""function get{title_name.replace(' ', '').replace('.', '')}Translation(key, lang) {{
  if ({camel_name}Translations[lang] && {camel_name}Translations[lang][key]) {{
    return {camel_name}Translations[lang][key];
  }}
  if ({camel_name}Translations.en && {camel_name}Translations[lang][key]) {{
    return {camel_name}Translations.en[key];
  }}
  return null;
}}

function apply{title_name.replace(' ', '').replace('.', '')}Translations(lang) {{
  console.log(`Applying {tool} translations for: ${{lang}}`);
  let count = 0;
  document.querySelectorAll('[data-i18n]').forEach(element => {{
    const key = element.getAttribute('data-i18n');
    if (key && (key.startsWith('review.{tool}.') || key.startsWith('review.common.'))) {{
      const translation = get{title_name.replace(' ', '').replace('.', '')}Translation(key, lang);
      if (translation) {{
        element.textContent = translation;
        count++;
      }}
    }}
  }});
  console.log(`Applied ${{count}} {tool} translations`);
}}

window.addEventListener('languageChanged', (e) => {{
  const lang = e.detail.language;
  setTimeout(() => apply{title_name.replace(' ', '').replace('.', '')}Translations(lang), 200);
}});

if (document.readyState === 'loading') {{
  document.addEventListener('DOMContentLoaded', () => {{
    const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
    apply{title_name.replace(' ', '').replace('.', '')}Translations(currentLang);
  }});
}} else {{
  const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
  apply{title_name.replace(' ', '').replace('.', '')}Translations(currentLang);
}}

console.log('{tool} i18n loaded');
"""

    js_file = os.path.join(js_dir, f"{tool}-i18n.js")
    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(js_content)

    en_count = len(translations.get("en", {}))
    de_count = len(translations.get("de", {}))
    return en_count, de_count

# MAIN EXECUTION
print("=" * 70)
print("AI SALES & CRM I18N SETUP")
print("=" * 70)

print(f"\nTotal tools to process: {len(tools)}")

print("\n[1/2] Loading Ada i18n.js...")
ada_trans = load_ada_i18n()
print(f"  [OK] {sum(len(v) for v in ada_trans.values())} total Ada translations")

print("\n[2/2] Processing Sales tools...")
completed = []
skipped = []

for tool in tools:
    print(f"\n{tool}:")
    translations = create_complete_translations(tool)

    if translations:
        en_count, de_count = rebuild_i18n_file(tool, translations)
        print(f"  [OK] {tool}-i18n.js (EN: {en_count} keys, DE: {de_count} translations)")
        completed.append(tool)
    else:
        skipped.append(tool)

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"Completed: {len(completed)} tools")
print(f"Skipped: {len(skipped)} tools")
if skipped:
    print(f"Skipped tools: {', '.join(skipped)}")
print("=" * 70)
