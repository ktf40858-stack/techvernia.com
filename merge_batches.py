#!/usr/bin/env python3
import json
import sys
import os

def merge_batches_to_i18n(tool_name, category='customer-service'):
    """Merge batch files and create i18n.js file"""

    base_path = f'GenuisNet.ai/pages/reviews/{category}'

    # Read all batch files
    translations = {}
    for batch_num in [1, 2, 3]:
        batch_file = f'{base_path}/{tool_name}-batch{batch_num}.json'
        if os.path.exists(batch_file):
            with open(batch_file, 'r', encoding='utf-8') as f:
                batch_data = json.load(f)
                for lang, content in batch_data.items():
                    if lang not in translations:
                        translations[lang] = {}
                    if content and isinstance(content, dict):  # Only add if not empty and is dict
                        translations[lang].update(content)

    # Read en.json
    en_file = f'{base_path}/{tool_name}-en.json'
    if os.path.exists(en_file):
        with open(en_file, 'r', encoding='utf-8') as f:
            translations['en'] = json.load(f)

    # Create function names
    func_name = tool_name.replace('-', '')
    capitalized = ''.join(word.capitalize() for word in tool_name.split('-'))

    # Generate i18n.js content
    js_content = f"// {tool_name.upper()} I18N\n"
    js_content += f"const {func_name}Translations = {{\n"

    # Add all languages
    for lang in ['en', 'de', 'es', 'fr', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']:
        js_content += f'  "{lang}": '
        if lang in translations and translations[lang]:
            js_content += json.dumps(translations[lang], ensure_ascii=False, indent=4).replace('\n', '\n  ')
        else:
            js_content += '{}'
        js_content += ',\n'

    js_content = js_content.rstrip(',\n') + '\n};\n\n'

    # Add helper functions
    js_content += f"""function get{capitalized}Translation(key, lang) {{
  if ({func_name}Translations[lang] && {func_name}Translations[lang][key]) {{
    return {func_name}Translations[lang][key];
  }}
  if ({func_name}Translations.en && {func_name}Translations.en[key]) {{
    return {func_name}Translations.en[key];
  }}
  return null;
}}

function apply{capitalized}Translations(lang) {{
  console.log(`🔥 Applying {tool_name} translations for: ${{lang}}`);
  let count = 0;
  document.querySelectorAll('[data-i18n]').forEach(element => {{
    const key = element.getAttribute('data-i18n');
    if (key && (key.startsWith('review.{tool_name}.') || key.startsWith('review.common.'))) {{
      const translation = get{capitalized}Translation(key, lang);
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
  setTimeout(() => apply{capitalized}Translations(lang), 200);
}});

if (document.readyState === 'loading') {{
  document.addEventListener('DOMContentLoaded', () => {{
    const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
    apply{capitalized}Translations(currentLang);
  }});
}} else {{
  const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
  apply{capitalized}Translations(currentLang);
}}

console.log('✅ {tool_name} i18n loaded');
"""

    # Write to file
    output_file = f'GenuisNet.ai/js/{tool_name}-i18n.js'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(js_content)

    print(f'Created {output_file}')
    return True

if __name__ == '__main__':
    if len(sys.argv) > 1:
        tool_name = sys.argv[1]
        category = sys.argv[2] if len(sys.argv) > 2 else 'customer-service'
        merge_batches_to_i18n(tool_name, category)
    else:
        print('Usage: python merge_batches.py <tool-name> [category]')
