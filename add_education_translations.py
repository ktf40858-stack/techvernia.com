import os
import re
import json

# Liste des 14 outils Education
tools = [
    "aleks", "carnegie-learning", "century-tech", "cognii",
    "coursera-coach", "duolingo-max", "gradescope", "khan-academy-ai",
    "knewton-alta", "querium", "quizlet-ai", "socratic-by-google",
    "squirrel-ai", "thinkster-math"
]

base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
js_dir = os.path.join(base_dir, "js")
batch_dir = os.path.join(base_dir, "pages", "reviews", "education")

# Langues cibles
languages = ["de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]

def extract_en_translations(js_file):
    """Extrait les traductions EN du fichier i18n.js"""
    with open(js_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Trouver le bloc "en": { ... }
    pattern = r'"en":\s*({[^}]+(?:{[^}]*}[^}]*)*})'
    match = re.search(pattern, content, re.DOTALL)

    if match:
        try:
            en_block = match.group(1)
            en_dict = json.loads(en_block)
            return en_dict
        except:
            # Fallback: extraire manuellement
            en_dict = {}
            key_pattern = r'"([^"]+)":\s*"([^"]*(?:\\.[^"]*)*)"'
            matches = re.findall(key_pattern, match.group(1))
            for key, value in matches:
                en_dict[key] = value.replace('\\"', '"')
            return en_dict

    return {}

def load_batch_translations(tool):
    """Charge les traductions depuis les fichiers batch JSON s'ils existent"""
    all_translations = {}

    for i in range(1, 4):
        batch_file = os.path.join(batch_dir, f"{tool}-batch{i}.json")
        if os.path.exists(batch_file):
            try:
                with open(batch_file, 'r', encoding='utf-8') as f:
                    batch_data = json.load(f)
                    for lang, translations in batch_data.items():
                        if lang not in all_translations:
                            all_translations[lang] = {}
                        all_translations[lang].update(translations)
            except Exception as e:
                print(f"[WARN] Error loading {batch_file}: {e}")

    return all_translations

def tool_to_camel(tool):
    """Convertit khan-academy-ai en khanAcademyAi"""
    parts = tool.split('-')
    return parts[0] + ''.join(p.capitalize() for p in parts[1:])

def tool_to_title(tool):
    """Convertit khan-academy-ai en Khan Academy Ai"""
    return ' '.join(p.capitalize() for p in tool.split('-'))

def generate_complete_i18n(tool):
    """Génère le fichier i18n.js complet avec toutes les langues"""
    js_file = os.path.join(js_dir, f"{tool}-i18n.js")

    if not os.path.exists(js_file):
        print(f"[SKIP] {tool}-i18n.js not found")
        return

    # Extraire les traductions EN existantes
    en_translations = extract_en_translations(js_file)

    if not en_translations:
        print(f"[ERROR] No English translations found in {tool}-i18n.js")
        return

    # Charger les traductions depuis les batch JSON
    batch_translations = load_batch_translations(tool)

    # Fusionner: EN + batch translations
    all_translations = {"en": en_translations}

    for lang in languages:
        if lang in batch_translations:
            all_translations[lang] = batch_translations[lang]
        else:
            # Si pas de batch, on laisse vide pour l'instant
            all_translations[lang] = {}

    # Générer le nouveau fichier i18n.js
    camel_name = tool_to_camel(tool)
    title_name = tool_to_title(tool)

    # Construire le JavaScript
    js_content = f"// {title_name.upper()} I18N\n"
    js_content += f"const {camel_name}Translations = {{\n"

    for lang in ["en"] + languages:
        if lang in all_translations and all_translations[lang]:
            js_content += f'  "{lang}": {json.dumps(all_translations[lang], indent=4, ensure_ascii=False)}'
            if lang != languages[-1]:
                js_content += ","
            js_content += "\n"

    js_content += "};\n\n"

    # Fonctions JavaScript
    js_content += f"""function get{title_name.replace(' ', '')}Translation(key, lang) {{
  if ({camel_name}Translations[lang] && {camel_name}Translations[lang][key]) {{
    return {camel_name}Translations[lang][key];
  }}
  if ({camel_name}Translations.en && {camel_name}Translations.en[key]) {{
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
    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(js_content)

    lang_count = sum(1 for lang in all_translations if all_translations[lang])
    print(f"[OK] {tool}-i18n.js updated ({len(en_translations)} keys, {lang_count} languages)")

# Traiter tous les outils
print("Adding translations to Education i18n files...")
print("=" * 60)

for tool in tools:
    generate_complete_i18n(tool)

print("=" * 60)
print("[DONE] All Education i18n files updated!")
