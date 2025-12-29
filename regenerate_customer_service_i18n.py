#!/usr/bin/env python3
"""Regenerate i18n JavaScript files for Customer Service & Support tools"""

import os
import json
import sys

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

CUSTOMER_SERVICE_DIR = 'GenuisNet.ai/pages/reviews/customer-service'
JS_DIR = 'GenuisNet.ai/js'

# Exclude drift (already has i18n from business category)
TOOLS = [
    'ada', 'certainly', 'cognigy', 'forethought', 'freshdesk-ai',
    'helpshift', 'intercom-fin', 'kustomer', 'liveperson', 'netomi',
    'polyai', 'ultimateai', 'yellowai', 'zendesk-ai'
]

def merge_all_translations(tool_name):
    """Merge all translation files (en.json + batch1-3) into single object"""

    all_translations = {'en': {}}

    # Load English base
    en_file = os.path.join(CUSTOMER_SERVICE_DIR, f'{tool_name}-en.json')
    if os.path.exists(en_file):
        with open(en_file, 'r', encoding='utf-8') as f:
            en_data = json.load(f)
            if 'en' in en_data:
                all_translations['en'] = en_data['en']

    # Load batch files
    for batch_num in [1, 2, 3]:
        batch_file = os.path.join(CUSTOMER_SERVICE_DIR, f'{tool_name}-batch{batch_num}.json')
        if os.path.exists(batch_file):
            with open(batch_file, 'r', encoding='utf-8') as f:
                batch_data = json.load(f)
                for lang, translations in batch_data.items():
                    if translations:  # Only add non-empty language objects
                        all_translations[lang] = translations

    return all_translations

def generate_i18n_js(tool_name, translations):
    """Generate JavaScript i18n file"""

    # Convert tool name to camelCase for function names
    tool_camel = tool_name.replace('-', ' ').title().replace(' ', '')
    tool_camel = tool_camel[0].lower() + tool_camel[1:]

    # Format translations as JavaScript object
    js_translations = "const " + tool_name.replace('-', '') + "Translations = {\n"

    for lang in sorted(translations.keys()):
        js_translations += f'    "{lang}": {{\n'
        for key, value in sorted(translations[lang].items()):
            # Escape special characters
            value_escaped = value.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
            js_translations += f'        "{key}": "{value_escaped}",\n'
        js_translations = js_translations.rstrip(',\n') + '\n    },\n'

    js_translations = js_translations.rstrip(',\n') + '\n};\n\n'

    # Add helper functions
    func_name_get = f'get{tool_name.replace("-", "").title()}Translation'
    func_name_apply = f'apply{tool_name.replace("-", "").title()}Translations'

    js_code = js_translations + f'''function {func_name_get}(key, lang) {{
    const translations = {tool_name.replace('-', '')}Translations;
    if (translations[lang] && translations[lang][key]) {{
        return translations[lang][key];
    }}
    if (translations.en && translations.en[key]) {{
        return translations.en[key];
    }}
    return null;
}}

function {func_name_apply}(lang) {{
    document.querySelectorAll('[data-i18n]').forEach(element => {{
        const key = element.getAttribute('data-i18n');
        const translation = {func_name_get}(key, lang);
        if (translation) {{
            element.textContent = translation;
        }}
    }});
}}

window.addEventListener('languageChanged', (e) => {{
    {func_name_apply}(e.detail.language);
}});

if (document.readyState === 'loading') {{
    document.addEventListener('DOMContentLoaded', () => {{
        const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
        {func_name_apply}(currentLang);
    }});
}} else {{
    const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
    {func_name_apply}(currentLang);
}}
'''

    return js_code

print("=" * 70)
print("CUSTOMER SERVICE & SUPPORT - I18N REGENERATION")
print("=" * 70)

for tool in TOOLS:
    try:
        # Merge all translations
        translations = merge_all_translations(tool)

        if not translations or len(translations) == 0:
            print(f"\n⚠️  {tool}: No translations found")
            continue

        # Generate JavaScript file
        js_code = generate_i18n_js(tool, translations)

        # Write to file
        output_file = os.path.join(JS_DIR, f'{tool}-i18n.js')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(js_code)

        # Get file size
        file_size = os.path.getsize(output_file)

        print(f"\n✅ {tool}:")
        print(f"  Merged {len(translations)} languages")
        print(f"  [CREATED] {file_size:,} bytes")

    except Exception as e:
        print(f"\n❌ {tool}: Error - {str(e)}")

print("\n" + "=" * 70)
print("Regeneration Complete!")
print("=" * 70)
