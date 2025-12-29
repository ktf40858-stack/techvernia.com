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

def load_ada_complete():
    """Charge le fichier i18n.js complet d'Ada"""
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

def adapt_for_education(text, tool_display):
    """Adapte le texte pour Education"""
    adapted = text

    # Remplacer Ada par le nom de l'outil
    adapted = adapted.replace("Ada", tool_display)

    # Adaptations Education
    replacements = [
        ("customer service", "education"),
        ("servicio al cliente", "educación"),
        ("service client", "éducation"),
        ("Kundenservice", "Bildung"),
        ("atendimento ao cliente", "educação"),
        ("客户服务", "教育"),
        ("カスタマーサービス", "教育"),
        ("고객 서비스", "교육"),
        ("خدمة العملاء", "التعليم"),
        ("ग्राहक सेवा", "शिक्षा"),

        ("modern businesses", "modern educational institutions"),
        ("empresas modernas", "instituciones educativas modernas"),
        ("entreprises modernes", "établissements éducatifs modernes"),
        ("moderne Unternehmen", "moderne Bildungseinrichtungen"),
        ("empresas modernas", "instituições educacionais modernas"),
        ("现代企业", "现代教育机构"),
        ("現代の企業", "現代の教育機関"),
        ("현대 기업", "현대 교육 기관"),
        ("الشركات الحديثة", "المؤسسات التعليمية الحديثة"),
        ("आधुनिक व्यवसाय", "आधुनिक शैक्षणिक संस्थान"),

        ("organizations", "educational institutions"),
        ("organizaciones", "instituciones educativas"),
        ("organisations", "établissements éducatifs"),
        ("Organisationen", "Bildungseinrichtungen"),
        ("organizações", "instituições educacionais"),
        ("组织", "教育机构"),
        ("組織", "教育機関"),
        ("조직", "교육 기관"),
        ("المنظمات", "المؤسسات التعليمية"),
        ("संगठन", "शैक्षणिक संस्थान")
    ]

    for old, new in replacements:
        adapted = adapted.replace(old, new)

    return adapted

def create_tool_translations(tool, ada_translations):
    """Crée les traductions pour un outil"""
    tool_display = tool_to_title(tool)
    tool_key = tool.replace("-", ".")

    all_trans = {}
    languages = ["en", "de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]

    for lang in languages:
        all_trans[lang] = {}

        if lang in ada_translations:
            for ada_key, ada_value in ada_translations[lang].items():
                # Convertir la clé: review.ada.xxx -> review.tool.xxx
                # review.ada.ada.is.a -> review.tool.tool-normalized.is.a
                new_key = ada_key.replace("review.ada.", f"review.{tool}.")
                # Remplacer aussi "ada" par le nom normalisé de l'outil dans le reste de la clé
                new_key = new_key.replace(".ada.", f".{tool_key}.")
                # Remplacer les occurrences de "ada" au début d'un segment de clé
                import re
                new_key = re.sub(r'\.ada\.', f'.{tool_key}.', new_key)
                new_key = re.sub(r'\.ada$', f'.{tool_key}', new_key)

                # Adapter le texte
                new_value = adapt_for_education(ada_value, tool_display)

                all_trans[lang][new_key] = new_value

    # Ajouter les FAQ
    faq_batch = os.path.join(edu_dir, f"{tool}-faq-batch.json")
    if os.path.exists(faq_batch):
        with open(faq_batch, 'r', encoding='utf-8') as f:
            faq_data = json.load(f)
            for lang in languages:
                if lang in faq_data:
                    all_trans[lang].update(faq_data[lang])

    return all_trans

def rebuild_i18n(tool, translations):
    """Reconstruit le fichier i18n.js"""
    camel = tool_to_camel(tool)
    title = tool_to_title(tool)

    js_content = f"// {title.upper()} I18N\n"
    js_content += f"const {camel}Translations = {{\n"

    langs = ["en", "de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]

    for idx, lang in enumerate(langs):
        if lang in translations:
            js_content += f'  "{lang}": {json.dumps(translations[lang], indent=4, ensure_ascii=False)}'
            if idx < len(langs) - 1:
                js_content += ","
            js_content += "\n"

    js_content += "};\n\n"

    js_content += f"""function get{title.replace(' ', '')}Translation(key, lang) {{
  if ({camel}Translations[lang] && {camel}Translations[lang][key]) {{
    return {camel}Translations[lang][key];
  }}
  if ({camel}Translations.en && {camel}Translations[key]) {{
    return {camel}Translations.en[key];
  }}
  return null;
}}

function apply{title.replace(' ', '')}Translations(lang) {{
  console.log(`Applying {tool} translations for: ${{lang}}`);
  let count = 0;
  document.querySelectorAll('[data-i18n]').forEach(element => {{
    const key = element.getAttribute('data-i18n');
    if (key && (key.startsWith('review.{tool}.') || key.startsWith('review.common.'))) {{
      const translation = get{title.replace(' ', '')}Translation(key, lang);
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
  setTimeout(() => apply{title.replace(' ', '')}Translations(lang), 200);
}});

if (document.readyState === 'loading') {{
  document.addEventListener('DOMContentLoaded', () => {{
    const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
    apply{title.replace(' ', '')}Translations(currentLang);
  }});
}} else {{
  const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
  apply{title.replace(' ', '')}Translations(currentLang);
}}

console.log('{tool} i18n loaded');
"""

    js_file = os.path.join(js_dir, f"{tool}-i18n.js")
    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(js_content)

    print(f"  [OK] {tool} ({len(translations['en'])} keys × 10 languages)")

# MAIN
print("=" * 70)
print("SIMPLE & DIRECT: COPYING ADA TRANSLATIONS TO EDUCATION")
print("=" * 70)

print("\n[1/2] Loading Ada i18n.js...")
ada_trans = load_ada_complete()
print(f"  [OK] {sum(len(v) for v in ada_trans.values())} total translations")

print("\n[2/2] Creating Education tools...")
for tool in tools:
    translations = create_tool_translations(tool, ada_trans)
    rebuild_i18n(tool, translations)

print("\n" + "=" * 70)
print("[COMPLETE!] All Education tools ready with full translations!")
print("=" * 70)
