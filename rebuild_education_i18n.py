import os
import re
import json

tools = [
    "aleks", "carnegie-learning", "century-tech", "cognii",
    "coursera-coach", "duolingo-max", "gradescope", "khan-academy-ai",
    "knewton-alta", "querium", "quizlet-ai", "socratic-by-google",
    "squirrel-ai", "thinkster-math"
]

base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
js_dir = os.path.join(base_dir, "js")
batch_dir = os.path.join(base_dir, "pages", "reviews", "education")

def tool_to_camel(tool):
    """khan-academy-ai -> khanAcademyAi"""
    parts = tool.split('-')
    return parts[0] + ''.join(p.capitalize() for p in parts[1:])

def tool_to_title(tool):
    """khan-academy-ai -> Khan Academy Ai"""
    return ' '.join(p.capitalize() for p in tool.split('-'))

def load_all_translations(tool):
    """Charge toutes les traductions d'un outil (batch1, batch2, batch3 + FAQ)"""
    all_translations = {}
    languages = ["en", "de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]

    for lang in languages:
        all_translations[lang] = {}

    # Charger les batch 1, 2, 3
    for batch_num in range(1, 4):
        batch_file = os.path.join(batch_dir, f"{tool}-batch{batch_num}.json")
        if os.path.exists(batch_file):
            with open(batch_file, 'r', encoding='utf-8') as f:
                batch_data = json.load(f)
                for lang in languages:
                    if lang == "en":
                        continue  # EN sera extrait du HTML
                    if lang in batch_data:
                        all_translations[lang].update(batch_data[lang])

    # Charger les FAQ
    faq_batch_file = os.path.join(batch_dir, f"{tool}-faq-batch.json")
    if os.path.exists(faq_batch_file):
        with open(faq_batch_file, 'r', encoding='utf-8') as f:
            faq_data = json.load(f)
            for lang in languages:
                if lang in faq_data:
                    all_translations[lang].update(faq_data[lang])

    # Charger les EN depuis l'ancien fichier i18n.js
    old_js_file = os.path.join(js_dir, f"{tool}-i18n.js")
    if os.path.exists(old_js_file):
        with open(old_js_file, 'r', encoding='utf-8') as f:
            content = f.read()

        pattern = r'"en":\s*\{([^}]+(?:\{[^}]*\}[^}]*)*)\}'
        match = re.search(pattern, content, re.DOTALL)

        if match:
            en_dict = {}
            key_pattern = r'"([^"]+)":\s*"([^"]*(?:\\.[^"]*)*)"'
            matches = re.findall(key_pattern, match.group(1))
            for key, value in matches:
                clean_value = value.replace('\\"', '"').replace('\\n', '\n')
                en_dict[key] = clean_value
            all_translations["en"] = en_dict

    return all_translations

def rebuild_i18n_file(tool):
    """Reconstruit complètement le fichier i18n.js"""
    all_translations = load_all_translations(tool)

    if not all_translations.get("en"):
        print(f"  [ERROR] No English translations for {tool}")
        return

    camel_name = tool_to_camel(tool)
    title_name = tool_to_title(tool)

    # Générer le fichier JS
    js_content = f"// {title_name.upper()} I18N\n"
    js_content += f"const {camel_name}Translations = {{\n"

    languages = ["en", "de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]

    for idx, lang in enumerate(languages):
        if lang in all_translations and all_translations[lang]:
            js_content += f'  "{lang}": {json.dumps(all_translations[lang], indent=4, ensure_ascii=False)}'
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

    # Sauvegarder
    js_file = os.path.join(js_dir, f"{tool}-i18n.js")
    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(js_content)

    en_count = len(all_translations.get("en", {}))
    print(f"  [OK] {tool}-i18n.js rebuilt ({en_count} keys × 10 languages)")

# MAIN EXECUTION
print("=" * 70)
print("REBUILDING ALL EDUCATION I18N FILES")
print("=" * 70)

for tool in tools:
    print(f"\n{tool}:")
    rebuild_i18n_file(tool)

print("\n" + "=" * 70)
print("[COMPLETE] All Education i18n files rebuilt with complete translations!")
print("=" * 70)
