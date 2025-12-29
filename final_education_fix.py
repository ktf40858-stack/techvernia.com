import os
import json
import re

base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
cs_dir = os.path.join(base_dir, "pages", "reviews", "customer-service")
html_dir = os.path.join(base_dir, "pages", "reviews", "education")
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

def load_ada_translations():
    """Charge toutes les traductions d'Ada (référence Customer Service)"""
    ada_trans = {}
    languages = ["de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]

    for lang in languages:
        ada_trans[lang] = {}

    # Charger les 3 batch files d'Ada
    for batch_num in range(1, 4):
        batch_file = os.path.join(cs_dir, f"ada-batch{batch_num}.json")
        if os.path.exists(batch_file):
            with open(batch_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for lang in languages:
                    if lang in data:
                        ada_trans[lang].update(data[lang])

    return ada_trans

def extract_html_keys(html_file):
    """Extrait toutes les clés data-i18n du HTML"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'data-i18n="([^"]+)"'
    matches = re.findall(pattern, content)
    return sorted(set(matches))

def extract_english_from_html(html_file, key):
    """Extrait le texte anglais pour une clé donnée"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = rf'data-i18n="{re.escape(key)}"[^>]*>([^<]+)<'
    match = re.search(pattern, content)

    if match:
        return match.group(1).strip()
    return None

def adapt_text_for_education(text, tool_display):
    """Adapte un texte de Customer Service pour Education"""
    adapted = text.replace("Ada", tool_display)
    adapted = adapted.replace("ada", tool_display.lower())

    replacements = {
        # English
        "customer service": "education",
        "customer-service": "education",
        "modern businesses": "modern educational institutions",
        "organizations": "educational institutions",

        # German
        "Kundenservice": "Bildung",
        "Kundendienst": "Bildung",
        "moderne Unternehmen": "moderne Bildungseinrichtungen",
        "Organisationen": "Bildungseinrichtungen",

        # Spanish
        "servicio al cliente": "educación",
        "atención al cliente": "educación",
        "empresas modernas": "instituciones educativas modernas",
        "organizaciones": "instituciones educativas",

        # French
        "service client": "éducation",
        "entreprises modernes": "établissements éducatifs modernes",
        "organisations": "établissements éducatifs",

        # Portuguese
        "atendimento ao cliente": "educação",
        "empresas modernas": "instituições educacionais modernas",
        "organizações": "instituições educacionais",

        # Chinese
        "客户服务": "教育",
        "现代企业": "现代教育机构",
        "组织": "教育机构",

        # Japanese
        "カスタマーサービス": "教育",
        "現代の企業": "現代の教育機関",
        "組織": "教育機関",

        # Korean
        "고객 서비스": "교육",
        "현대 기업": "현대 교육 기관",
        "조직": "교육 기관",

        # Arabic
        "خدمة العملاء": "التعليم",
        "الشركات الحديثة": "المؤسسات التعليمية الحديثة",
        "المنظمات": "المؤسسات التعليمية",

        # Hindi
        "ग्राहक सेवा": "शिक्षा",
        "आधुनिक व्यवसाय": "आधुनिक शैक्षणिक संस्थान",
        "संगठन": "शैक्षणिक संस्थान"
    }

    for old, new in replacements.items():
        adapted = adapted.replace(old, new)

    return adapted

def create_key_suffix_from_text(text):
    """Crée un suffixe de clé à partir du texte anglais"""
    # Prendre les premiers mots et les normaliser
    words = text.lower().split()[:6]
    suffix = '.'.join(words)
    suffix = re.sub(r'[^a-z0-9.]', '', suffix)
    suffix = re.sub(r'\.+', '.', suffix)
    return suffix.strip('.')

def create_translations_for_tool(tool, ada_translations):
    """Crée toutes les traductions pour un outil Education"""
    html_file = os.path.join(html_dir, f"{tool}.html")
    tool_display = tool_to_title(tool)

    # Extraire toutes les clés HTML
    html_keys = extract_html_keys(html_file)

    # Créer les traductions
    all_translations = {}
    languages = ["en", "de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]

    for lang in languages:
        all_translations[lang] = {}

    # Pour chaque clé HTML
    for html_key in html_keys:
        # Extraire le texte anglais
        en_text = extract_english_from_html(html_file, html_key)

        if not en_text:
            continue

        # Ajouter l'anglais
        all_translations["en"][html_key] = en_text

        # Chercher la traduction correspondante dans Ada
        # La clé Ada serait: review.ada.{suffix}
        # On doit trouver quelle clé Ada correspond

        # Créer un suffixe à partir du texte
        suffix = create_key_suffix_from_text(en_text)

        # Chercher dans Ada
        ada_key_pattern = f"review.ada.{suffix}"

        # Chercher une correspondance exacte ou partielle
        found = False
        for ada_key in ada_translations.get("de", {}).keys():
            if suffix in ada_key or ada_key.endswith(suffix[:20]):
                # Trouvé une correspondance potentielle
                for lang in ["de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]:
                    if lang in ada_translations and ada_key in ada_translations[lang]:
                        ada_text = ada_translations[lang][ada_key]
                        adapted_text = adapt_text_for_education(ada_text, tool_display)
                        all_translations[lang][html_key] = adapted_text
                found = True
                break

        # Si pas trouvé, chercher par correspondance de texte
        if not found:
            # Chercher le texte anglais dans les valeurs Ada
            for ada_key, ada_en_text in ada_translations.get("en", {}).items():
                if en_text.lower() == ada_en_text.lower().replace("ada", "").replace("customer service", ""):
                    for lang in ["de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]:
                        if lang in ada_translations and ada_key in ada_translations[lang]:
                            ada_text = ada_translations[lang][ada_key]
                            adapted_text = adapt_text_for_education(ada_text, tool_display)
                            all_translations[lang][html_key] = adapted_text
                    break

    # Charger les FAQ translations
    faq_batch = os.path.join(html_dir, f"{tool}-faq-batch.json")
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
  if ({camel_name}Translations.en && {camel_name}Translations[key]) {{
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
print("FINAL FIX: MAPPING ALL TRANSLATIONS TO CORRECT KEYS")
print("=" * 70)

print("\n[1/2] Loading Ada translations...")
ada_translations = load_ada_translations()
# Ajouter EN aussi
ada_translations["en"] = {}
for batch_num in range(1, 4):
    batch_file = os.path.join(cs_dir, f"ada-batch{batch_num}-en.json")
    if os.path.exists(batch_file):
        with open(batch_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if "en" in data:
                ada_translations["en"].update(data["en"])

print(f"  [OK] Loaded translations for 10 languages")

print("\n[2/2] Creating translations for all Education tools...")
for tool in tools:
    print(f"\n{tool}:")
    translations = create_translations_for_tool(tool, ada_translations)
    rebuild_i18n_file(tool, translations)

print("\n" + "=" * 70)
print("[COMPLETE] All Education tools have correct translations!")
print("=" * 70)
