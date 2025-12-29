import os
import json
import re

base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
cs_dir = os.path.join(base_dir, "pages", "reviews", "customer-service")
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

def load_ada_translations():
    """Charge TOUTES les traductions d'Ada (Customer Service) comme référence"""
    all_trans = {}
    languages = ["en", "de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]

    for lang in languages:
        all_trans[lang] = {}

    # Charger les 3 batch files d'Ada
    for batch_num in range(1, 4):
        batch_file = os.path.join(cs_dir, f"ada-batch{batch_num}.json")
        if os.path.exists(batch_file):
            with open(batch_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for lang in languages:
                    if lang in data:
                        all_trans[lang].update(data[lang])

    return all_trans

def adapt_for_education(text, tool_display):
    """Adapte un texte de Customer Service pour Education"""
    # Remplacer Ada par le nom de l'outil
    adapted = text.replace("Ada", tool_display)
    adapted = adapted.replace("ada", tool_display.lower())

    # Remplacements spécifiques pour Education
    replacements = {
        # English
        "customer service": "education",
        "customer-service": "education",
        "modern businesses": "modern educational institutions",

        # Spanish
        "servicio al cliente": "educación",
        "atención al cliente": "educación",
        "empresas modernas": "instituciones educativas modernas",

        # German
        "Kundenservice": "Bildung",
        "Kundendienst": "Bildung",
        "moderne Unternehmen": "moderne Bildungseinrichtungen",

        # French
        "service client": "éducation",
        "entreprises modernes": "établissements éducatifs modernes",

        # Portuguese
        "atendimento ao cliente": "educação",
        "empresas modernas": "instituições educacionais modernas",

        # Chinese
        "客户服务": "教育",
        "现代企业": "现代教育机构",

        # Japanese
        "カスタマーサービス": "教育",
        "現代の企業": "現代の教育機関",

        # Korean
        "고객 서비스": "교육",
        "현대 기업": "현대 교육 기관",

        # Arabic
        "خدمة العملاء": "التعليم",
        "الشركات الحديثة": "المؤسسات التعليمية الحديثة",

        # Hindi
        "ग्राहक सेवा": "शिक्षा",
        "आधुनिक व्यवसाय": "आधुनिक शैक्षणिक संस्थान"
    }

    for old, new in replacements.items():
        adapted = adapted.replace(old, new)

    return adapted

def create_education_translations(tool, ada_translations):
    """Crée les traductions pour un outil Education basées sur Ada"""
    edu_translations = {}
    tool_display = tool_to_title(tool)

    languages = ["en", "de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]

    for lang in languages:
        edu_translations[lang] = {}

        if lang in ada_translations:
            for ada_key, ada_value in ada_translations[lang].items():
                # Convertir la clé
                edu_key = ada_key.replace("review.ada.", f"review.{tool}.")

                # Adapter le texte
                edu_value = adapt_for_education(ada_value, tool_display)

                edu_translations[lang][edu_key] = edu_value

    # Charger les batch files Education s'ils existent (pour FAQ, etc.)
    for batch_num in range(1, 4):
        batch_file = os.path.join(edu_dir, f"{tool}-batch{batch_num}.json")
        if os.path.exists(batch_file):
            with open(batch_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for lang in languages:
                    if lang in data:
                        edu_translations[lang].update(data[lang])

    # Charger FAQ batch
    faq_batch = os.path.join(edu_dir, f"{tool}-faq-batch.json")
    if os.path.exists(faq_batch):
        with open(faq_batch, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for lang in languages:
                if lang in data:
                    edu_translations[lang].update(data[lang])

    # Charger EN depuis l'ancien fichier si existe
    old_js = os.path.join(js_dir, f"{tool}-i18n.js")
    if os.path.exists(old_js):
        with open(old_js, 'r', encoding='utf-8') as f:
            content = f.read()
            pattern = r'"en":\s*\{([^}]+(?:\{[^}]*\}[^}]*)*)\}'
            match = re.search(pattern, content, re.DOTALL)
            if match:
                en_dict = {}
                key_pattern = r'"([^"]+)":\s*"([^"]*(?:\\.[^"]*)*)"'
                matches = re.findall(key_pattern, match.group(1))
                for key, value in matches:
                    clean_value = value.replace('\\"', '"')
                    en_dict[key] = clean_value
                edu_translations["en"].update(en_dict)

    return edu_translations

def rebuild_i18n_file(tool, translations):
    """Reconstruit complètement le fichier i18n.js avec les bonnes traductions"""
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
    print(f"  [OK] {tool}-i18n.js ({en_count} keys × 10 languages)")

# MAIN EXECUTION
print("=" * 70)
print("COMPLETE REBUILD OF EDUCATION I18N FILES")
print("=" * 70)

print("\n[1/2] Loading Ada translations as reference...")
ada_translations = load_ada_translations()
print(f"  [OK] Loaded {sum(len(v) for v in ada_translations.values())} translations")

print("\n[2/2] Rebuilding Education tools...")
for tool in tools:
    translations = create_education_translations(tool, ada_translations)
    rebuild_i18n_file(tool, translations)

print("\n" + "=" * 70)
print("[COMPLETE] All Education i18n files rebuilt correctly!")
print("=" * 70)
