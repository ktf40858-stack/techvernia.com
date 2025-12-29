import os
import json
import re

base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
edu_dir = os.path.join(base_dir, "pages", "reviews", "education")
js_dir = os.path.join(base_dir, "js")

tools = [
    "aleks", "carnegie-learning", "century-tech", "cognii",
    "coursera-coach", "duolingo-max", "gradescope", "khan-academy-ai",
    "knewton-alta", "querium", "quizlet-ai", "socratic-by-google",
    "squirrel-ai", "thinkster-math"
]

def tool_to_camel(tool):
    parts = tool.split('-')
    return parts[0] + ''.join(p.capitalize() for p in parts[1:])

def tool_to_title(tool):
    return ' '.join(p.capitalize() for p in tool.split('-'))

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

            en_text_comp = en_text_normalized.replace("education", "")

            # Si les textes sont similaires
            if ada_normalized in en_text_comp or en_text_comp in ada_normalized:
                return ada_key

            # Vérifier les premiers 50 caractères
            if len(ada_normalized) > 50 and len(en_text_comp) > 50:
                if ada_normalized[:50] in en_text_comp or en_text_comp[:50] in ada_normalized:
                    return ada_key

    return None

def adapt_for_education(text, tool_display):
    """Adapte le texte pour Education"""
    adapted = text.replace("Ada", tool_display)
    adapted = adapted.replace("ada", tool_display.lower())

    replacements = {
        "customer service": "education",
        "customer-service": "education",
        "modern businesses": "modern educational institutions",
        "organizations": "educational institutions",

        "Kundenservice": "Bildung",
        "Kundendienst": "Bildung",
        "moderne Unternehmen": "moderne Bildungseinrichtungen",
        "Organisationen": "Bildungseinrichtungen",

        "servicio al cliente": "educación",
        "atención al cliente": "educación",
        "empresas modernas": "instituciones educativas modernas",
        "organizaciones": "instituciones educativas",

        "service client": "éducation",
        "entreprises modernes": "établissements éducatifs modernes",
        "organisations": "établissements éducatifs",

        "atendimento ao cliente": "educação",
        "empresas modernas": "instituições educacionais modernas",
        "organizações": "instituições educacionais",

        "客户服务": "教育",
        "现代企业": "现代教育机构",
        "组织": "教育机构",

        "カスタマーサービス": "教育",
        "現代の企業": "現代の教育機関",
        "組織": "教育機関",

        "고객 서비스": "교육",
        "현대 기업": "현대 교육 기관",
        "조직": "교육 기관",

        "خدمة العملاء": "التعليم",
        "الشركات الحديثة": "المؤسسات التعليمية الحديثة",
        "المنظمات": "المؤسسات التعليمية",

        "ग्राहक सेवा": "शिक्षा",
        "आधुनिक व्यवसाय": "आधुनिक शैक्षणिक संस्थान",
        "संगठन": "शैक्षणिक संस्थान"
    }

    for old, new in replacements.items():
        adapted = adapted.replace(old, new)

    return adapted

def create_complete_translations(tool):
    """Crée les traductions complètes basées sur le HTML et Ada"""
    html_file = os.path.join(edu_dir, f"{tool}.html")
    tool_display = tool_to_title(tool)

    # Extraire les clés et textes du HTML
    html_en_trans = extract_html_translations(html_file)

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
                    adapted_text = adapt_for_education(ada_text, tool_display)
                    all_translations[lang][html_key] = adapted_text

    # Charger les FAQ
    faq_batch = os.path.join(edu_dir, f"{tool}-faq-batch.json")
    if os.path.exists(faq_batch):
        with open(faq_batch, 'r', encoding='utf-8') as f:
            faq_data = json.load(f)
            for lang in languages:
                if lang in faq_data:
                    all_translations[lang].update(faq_data[lang])

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

    js_content += f"""function get{title_name.replace(' ', '')}Translation(key, lang) {{
  if ({camel_name}Translations[lang] && {camel_name}Translations[lang][key]) {{
    return {camel_name}Translations[lang][key];
  }}
  if ({camel_name}Translations.en && {camel_name}Translations[lang][key]) {{
    return {camel_name}Translations.en[key];
  }}
  return null;
}}

function apply{title_name.replace(' ', '')}Translations(lang) {{
  console.log(`Applying {tool} translations for: ${{lang}}`);
  let count = 0;
  document.querySelectorAll('[data-i18n]').forEach(element => {{
    const key = element.getAttribute('data-i18n');
    if (key && (key.startsWith('review.{tool}.') || key.startsWith('review.common.'))) {{
      const translation = get{title_name.replace(' ', '')}Translation(key, lang);
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
  setTimeout(() => apply{title_name.replace(' ', '')}Translations(lang), 200);
}});

if (document.readyState === 'loading') {{
  document.addEventListener('DOMContentLoaded', () => {{
    const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
    apply{title_name.replace(' ', '')}Translations(currentLang);
  }});
}} else {{
  const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
  apply{title_name.replace(' ', '')}Translations(currentLang);
}}

console.log('{tool} i18n loaded');
"""

    js_file = os.path.join(js_dir, f"{tool}-i18n.js")
    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(js_content)

    en_count = len(translations.get("en", {}))
    de_count = len(translations.get("de", {}))
    print(f"  [OK] {tool}-i18n.js (EN: {en_count} keys, DE: {de_count} translations)")

# MAIN EXECUTION
print("=" * 70)
print("EXTRACT HTML KEYS & CREATE EXACT TRANSLATIONS")
print("=" * 70)

print("\n[1/2] Loading Ada i18n.js...")
ada_trans = load_ada_i18n()
print(f"  [OK] {sum(len(v) for v in ada_trans.values())} total Ada translations")

print("\n[2/2] Processing Education tools...")
for tool in tools:
    print(f"\n{tool}:")
    translations = create_complete_translations(tool)
    rebuild_i18n_file(tool, translations)

print("\n" + "=" * 70)
print("[COMPLETE] All Education i18n files rebuilt with exact HTML keys!")
print("=" * 70)
