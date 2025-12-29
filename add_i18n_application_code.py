#!/usr/bin/env python3
import sys, io

if sys.platform=='win32':
    sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

tools = [
    'beamery', 'eightfold-ai', 'fetcher', 'findem', 'harver', 'hirevue',
    'humanly', 'paradox-olivia', 'phenom', 'pymetrics', 'seekout', 'sense',
    'textio', 'workable-ai'
]

for tool in tools:
    tool_var = tool.replace('-', '')
    tool_name = tool.replace('-', ' ').title()
    i18n_path = f'GenuisNet.ai/js/{tool}-i18n.js'

    print(f"🔧 {tool_name}...")

    # Lire le fichier existant
    with open(i18n_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Vérifier s'il a déjà le code d'application
    if f'function get{tool_var.capitalize()}Translation' in content:
        print(f"  ⏭️  Déjà complet")
        continue

    # Ajouter le code d'application après l'objet
    application_code = f'''

function get{tool_var.capitalize()}Translation(key, lang) {{
  if ({tool_var}Translations[lang] && {tool_var}Translations[lang][key]) {{
    return {tool_var}Translations[lang][key];
  }}
  if ({tool_var}Translations.en && {tool_var}Translations.en[key]) {{
    return {tool_var}Translations.en[key];
  }}
  return null;
}}

function apply{tool_var.capitalize()}Translations(lang) {{
  console.log(`🔥 Applying {tool} translations for: ${{lang}}`);
  let count = 0;
  document.querySelectorAll('[data-i18n]').forEach(element => {{
    const key = element.getAttribute('data-i18n');
    if (key && (key.startsWith('review.{tool}.') || key.startsWith('review.common.'))) {{
      const translation = get{tool_var.capitalize()}Translation(key, lang);
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
  setTimeout(() => apply{tool_var.capitalize()}Translations(lang), 200);
}});

if (document.readyState === 'loading') {{
  document.addEventListener('DOMContentLoaded', () => {{
    const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
    apply{tool_var.capitalize()}Translations(currentLang);
  }});
}} else {{
  const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
  apply{tool_var.capitalize()}Translations(currentLang);
}}

console.log('✅ {tool} i18n loaded');
'''

    # Ajouter le code à la fin
    content = content + application_code

    # Sauvegarder
    with open(i18n_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  ✅ Code d'application ajouté")

print("\n✅ Tous les fichiers i18n complétés!")
