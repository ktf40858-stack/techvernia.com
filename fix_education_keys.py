import os
import json
import re

base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
html_dir = os.path.join(base_dir, "pages", "reviews", "education")
js_dir = os.path.join(base_dir, "js")

tools = [
    "aleks", "carnegie-learning", "century-tech", "cognii",
    "coursera-coach", "duolingo-max", "gradescope", "khan-academy-ai",
    "knewton-alta", "querium", "quizlet-ai", "socratic-by-google",
    "squirrel-ai", "thinkster-math"
]

def extract_html_keys(html_file):
    """Extrait toutes les clés data-i18n du fichier HTML"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'data-i18n="([^"]+)"'
    matches = re.findall(pattern, content)
    return set(matches)

def load_i18n_file(js_file):
    """Charge le fichier i18n.js et extrait toutes les traductions"""
    with open(js_file, 'r', encoding='utf-8') as f:
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

def create_key_mapping(tool):
    """Crée un mapping entre les clés Ada et les clés de l'outil"""
    # Mapping des clés communes
    key_mappings = {
        f"review.{tool}.ada.is.a.leading.ai-powered": f"review.{tool}.{tool.replace('-', '.')}.is.a",
        f"review.{tool}.ada.is.a.powerful.feature-rich": f"review.{tool}.{tool.replace('-', '.')}.is.a",
        f"review.{tool}.ada.offers.flexible.pricing.plans": f"review.{tool}.{tool.replace('-', '.')}.offers.flexible",
        f"review.{tool}.ada.excels.for": f"review.{tool}.{tool.replace('-', '.')}.excels.for",
        f"review.{tool}.ada.integrates.with.100.popular": f"review.{tool}.{tool.replace('-', '.')}.integrates.with",
        f"review.{tool}.try.ada.today.and.experience": f"review.{tool}.try.{tool.replace('-', '.')}.today",
        f"review.{tool}.try.ada.free": f"review.{tool}.try.{tool.replace('-', '.')}.free",
        f"review.{tool}.ada.vs.competitors": f"review.{tool}.{tool.replace('-', '.')}.vs.competitors"
    }

    return key_mappings

def fix_i18n_keys(tool):
    """Corrige les clés dans le fichier i18n.js"""
    html_file = os.path.join(html_dir, f"{tool}.html")
    js_file = os.path.join(js_dir, f"{tool}-i18n.js")

    # Extraire les clés HTML
    html_keys = extract_html_keys(html_file)

    # Charger les traductions actuelles
    current_translations = load_i18n_file(js_file)

    # Créer le mapping de clés
    key_mapping = create_key_mapping(tool)

    # Nouvelles traductions corrigées
    fixed_translations = {}
    languages = ["en", "de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]

    for lang in languages:
        fixed_translations[lang] = {}

        if lang in current_translations:
            for old_key, value in current_translations[lang].items():
                # Vérifier si la clé doit être mappée
                new_key = key_mapping.get(old_key, old_key)

                # Utiliser la nouvelle clé
                fixed_translations[lang][new_key] = value

    # Régénérer le fichier i18n.js
    tool_camel = ''.join(p.capitalize() if i > 0 else p for i, p in enumerate(tool.split('-')))
    tool_title = ' '.join(p.capitalize() for p in tool.split('-'))

    js_content = f"// {tool_title.upper()} I18N\n"
    js_content += f"const {tool_camel}Translations = {{\n"

    for idx, lang in enumerate(languages):
        if lang in fixed_translations and fixed_translations[lang]:
            js_content += f'  "{lang}": {json.dumps(fixed_translations[lang], indent=4, ensure_ascii=False)}'
            if idx < len(languages) - 1:
                js_content += ","
            js_content += "\n"

    js_content += "};\n\n"

    js_content += f"""function get{tool_title.replace(' ', '')}Translation(key, lang) {{
  if ({tool_camel}Translations[lang] && {tool_camel}Translations[lang][key]) {{
    return {tool_camel}Translations[lang][key];
  }}
  if ({tool_camel}Translations.en && {tool_camel}Translations[lang][key]) {{
    return {tool_camel}Translations.en[key];
  }}
  return null;
}}

function apply{tool_title.replace(' ', '')}Translations(lang) {{
  console.log(`Applying {tool} translations for: ${{lang}}`);
  let count = 0;
  document.querySelectorAll('[data-i18n]').forEach(element => {{
    const key = element.getAttribute('data-i18n');
    if (key && (key.startsWith('review.{tool}.') || key.startsWith('review.common.'))) {{
      const translation = get{tool_title.replace(' ', '')}Translation(key, lang);
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
  setTimeout(() => apply{tool_title.replace(' ', '')}Translations(lang), 200);
}});

if (document.readyState === 'loading') {{
  document.addEventListener('DOMContentLoaded', () => {{
    const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
    apply{tool_title.replace(' ', '')}Translations(currentLang);
  }});
}} else {{
  const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
  apply{tool_title.replace(' ', '')}Translations(currentLang);
}}

console.log('{tool} i18n loaded');
"""

    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(js_content)

    print(f"  [OK] {tool}-i18n.js keys fixed")

# MAIN EXECUTION
print("=" * 70)
print("FIXING EDUCATION I18N KEYS TO MATCH HTML")
print("=" * 70)

for tool in tools:
    fix_i18n_keys(tool)

print("\n" + "=" * 70)
print("[COMPLETE] All i18n keys fixed!")
print("=" * 70)
