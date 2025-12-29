import os
import re
import json

# Liste des 14 outils
tools = [
    "aleks", "carnegie-learning", "century-tech", "cognii",
    "coursera-coach", "duolingo-max", "gradescope", "khan-academy-ai",
    "knewton-alta", "querium", "quizlet-ai", "socratic-by-google",
    "squirrel-ai", "thinkster-math"
]

base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
html_dir = os.path.join(base_dir, "pages", "reviews", "education")
js_dir = os.path.join(base_dir, "js")

def tool_to_camel(tool):
    """Convertit khan-academy-ai en khanAcademyAi"""
    parts = tool.split('-')
    return parts[0] + ''.join(p.capitalize() for p in parts[1:])

def tool_to_title(tool):
    """Convertit khan-academy-ai en Khan Academy Ai"""
    return ' '.join(p.capitalize() for p in tool.split('-'))

def extract_i18n_keys(html_file):
    """Extrait toutes les clés data-i18n du HTML"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Trouver tous les data-i18n="..."
    pattern = r'data-i18n="([^"]+)"'
    matches = re.findall(pattern, content)

    # Filtrer pour ne garder que les clés de ce tool
    tool_name = os.path.basename(html_file).replace('.html', '')
    keys = [m for m in matches if m.startswith(f'review.{tool_name}.')]

    return sorted(set(keys))

def extract_english_text(html_file, key):
    """Extrait le texte anglais pour une clé donnée"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Chercher <span data-i18n="key">Text</span>
    pattern = rf'data-i18n="{re.escape(key)}"[^>]*>([^<]+)<'
    match = re.search(pattern, content)

    if match:
        return match.group(1).strip()
    return ""

def generate_i18n_js(tool):
    """Génère le fichier i18n.js pour un outil"""
    html_file = os.path.join(html_dir, f"{tool}.html")

    if not os.path.exists(html_file):
        print(f"[SKIP] {tool}.html not found")
        return

    # Extraire les clés
    keys = extract_i18n_keys(html_file)

    if not keys:
        print(f"[SKIP] No i18n keys found in {tool}.html")
        return

    # Créer le dictionnaire EN
    en_dict = {}
    for key in keys:
        text = extract_english_text(html_file, key)
        if text:
            en_dict[key] = text

    camel_name = tool_to_camel(tool)
    title_name = tool_to_title(tool)

    # Générer le fichier JS
    js_content = f"""// {title_name.upper()} I18N
const {camel_name}Translations = {{
  "en": {json.dumps(en_dict, indent=4, ensure_ascii=False)}
}};

function get{title_name.replace(' ', '')}Translation(key, lang) {{
  if ({camel_name}Translations[lang] && {camel_name}Translations[lang][key]) {{
    return {camel_name}Translations[lang][key];
  }}
  if ({camel_name}Translations.en && {camel_name}Translations.en[key]) {{
    return {camel_name}Translations.en[key];
  }}
  return null;
}}

function apply{title_name.replace(' ', '')}Translations(lang) {{
  console.log(`🔥 Applying {tool} translations for: ${{lang}}`);
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
  console.log(`✅ Applied ${{count}} {tool} translations`);
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

console.log('✅ {tool} i18n loaded');
"""

    # Sauvegarder
    js_file = os.path.join(js_dir, f"{tool}-i18n.js")
    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(js_content)

    print(f"[OK] Created {tool}-i18n.js ({len(keys)} keys)")

# Générer tous les fichiers
print("Creating i18n files for Education tools...")
for tool in tools:
    generate_i18n_js(tool)

print("\n[DONE] All i18n files created!")
