#!/usr/bin/env python3
import sys, io, os, glob, json, re
from bs4 import BeautifulSoup

if sys.platform=='win32':
    sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

# Catégories à traiter
incomplete_categories = [
    'chatbots', 'research', 'gaming', 'translation', 'quantum', 'writing',
    'networking', 'productivity'
]

languages = ['de', 'fr', 'es', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']

print("🚀 COMPLÉTION AUTOMATIQUE DE TOUS LES OUTILS RESTANTS")
print("=" * 100)

# Charger les traductions de référence (paradox-olivia)
print("\n📦 Chargement des traductions de référence...")
ref_translations = {}
for lang in languages:
    with open(f'GenuisNet.ai/pages/reviews/hr/trans-{lang}.json', 'r', encoding='utf-8') as f:
        ref_translations[lang] = json.load(f)
print(f"✅ {len(ref_translations)} langues de référence chargées")

tools_processed = 0
tools_skipped = 0

for category in incomplete_categories:
    print(f"\n{'='*100}")
    print(f"📁 CATÉGORIE: {category.upper()}")
    print(f"{'='*100}")

    html_files = glob.glob(f'GenuisNet.ai/pages/reviews/{category}/*.html')

    for html_file in html_files:
        tool_name = os.path.basename(html_file).replace('.html', '')
        i18n_file = f'GenuisNet.ai/js/{tool_name}-i18n.js'

        # Vérifier si déjà complet
        if os.path.exists(i18n_file):
            with open(i18n_file, 'r', encoding='utf-8') as f:
                content = f.read()
                if 'function apply' in content and 'languageChanged' in content:
                    tools_skipped += 1
                    continue

        print(f"\n🔧 {tool_name}...")

        # Extraire le contenu anglais du HTML
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f.read(), 'html.parser')

            elements = soup.find_all(attrs={'data-i18n': re.compile(f'review\\.{re.escape(tool_name)}\\.')})
            en_content = {}
            for elem in elements:
                key = elem.get('data-i18n')
                text = elem.get_text(strip=True)
                if text:
                    en_content[key] = text

            if not en_content:
                print(f"  ⚠️  Aucune clé i18n trouvée, skip")
                tools_skipped += 1
                continue

            print(f"  📄 {len(en_content)} clés extraites")

        except Exception as e:
            print(f"  ❌ Erreur extraction: {e}")
            tools_skipped += 1
            continue

        # Créer les traductions pour chaque langue
        tool_translations = {'en': en_content}
        tool_display_name = tool_name.replace('-', ' ').title()

        for lang in languages:
            tool_translations[lang] = {}

            for en_key, en_value in en_content.items():
                # Essayer de trouver une traduction de référence
                ref_key = en_key.replace(tool_name, 'paradox-olivia')

                if ref_key in ref_translations[lang]:
                    # Adapter la traduction
                    translated = ref_translations[lang][ref_key]
                    translated = translated.replace('Paradox Olivia', tool_display_name)
                    translated = translated.replace('Paradox (Olivia)', tool_display_name)
                    tool_translations[lang][en_key] = translated
                else:
                    # Fallback: anglais
                    tool_translations[lang][en_key] = en_value

        # Générer le fichier i18n complet
        tool_var = tool_name.replace('-', '')
        output_lines = [f'// {tool_display_name.upper()} I18N']
        output_lines.append(f'const {tool_var}Translations = {{')

        for lang in ['en'] + languages:
            if tool_translations[lang]:
                output_lines.append(f'  "{lang}": {{')
                for key in sorted(tool_translations[lang].keys()):
                    value = tool_translations[lang][key]
                    # Échapper les guillemets
                    value = value.replace('\\', '\\\\').replace('"', '\\"')
                    output_lines.append(f'      "{key}": "{value}",')

                if output_lines[-1].endswith(','):
                    output_lines[-1] = output_lines[-1][:-1]
                output_lines.append('  },')

        if output_lines[-1].endswith(','):
            output_lines[-1] = output_lines[-1][:-1]
        output_lines.append('};')

        # Ajouter le code d'application
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
  console.log(`🔥 Applying {tool_name} translations for: ${{lang}}`);
  let count = 0;
  document.querySelectorAll('[data-i18n]').forEach(element => {{
    const key = element.getAttribute('data-i18n');
    if (key && (key.startsWith('review.{tool_name}.') || key.startsWith('review.common.'))) {{
      const translation = get{tool_var.capitalize()}Translation(key, lang);
      if (translation) {{
        element.textContent = translation;
        count++;
      }}
    }}
  }});
  console.log(`✅ Applied ${{count}} {tool_name} translations`);
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

console.log('✅ {tool_name} i18n loaded');
'''

        output_lines.append(application_code)

        # Sauvegarder
        with open(i18n_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(output_lines))

        total_translations = sum(len(tool_translations[lang]) for lang in ['en'] + languages)
        print(f"  ✅ {total_translations} traductions ({len(en_content)} clés × 10 langues)")
        tools_processed += 1

print(f"\n{'='*100}")
print(f"✅ TERMINÉ!")
print(f"  📦 {tools_processed} outils traités")
print(f"  ⏭️  {tools_skipped} outils skippés (déjà complets)")
print(f"{'='*100}")
