#!/usr/bin/env python3
"""Regenerate ALL Legal i18n files"""

import json
import os
import sys

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

TOOLS = ['blue-j-legal', 'casetext', 'cocounsel', 'everlaw', 'harvey-ai', 'kira-systems', 'lawgeex', 'lex-machina', 'luminance', 'primer', 'ravel-law', 'ross-intelligence']
LEGAL_DIR = 'GenuisNet.ai/pages/reviews/legal'
JS_DIR = 'GenuisNet.ai/js'

def load_json_file(filepath):
    """Load JSON file safely"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return None

def merge_all_translations(tool_name):
    """Merge English base + all batch files"""
    print(f"\n{tool_name}:")

    # Load English base
    en_file = os.path.join(LEGAL_DIR, f"{tool_name}-en.json")
    en_data = load_json_file(en_file)

    if not en_data:
        print(f"  [ERROR] No English file")
        return None

    result = {"en": en_data}

    # Load standard batch files (batch1, batch2, batch3)
    for batch_num in [1, 2, 3]:
        batch_file = os.path.join(LEGAL_DIR, f"{tool_name}-batch{batch_num}.json")
        batch_data = load_json_file(batch_file)

        if batch_data:
            for lang, translations in batch_data.items():
                if translations and len(translations) > 0:
                    result[lang] = translations

    lang_count = len([l for l in result if result[l]])
    print(f"  Merged {lang_count} languages")

    return result

def generate_i18n_js(tool_name, translations):
    """Generate JavaScript i18n file"""
    if not translations:
        return None

    var_name = tool_name.replace('-', '')

    js_content = f"// {tool_name.upper()} I18N\n"
    js_content += f"const {var_name}Translations = {{\n"

    language_order = ['en', 'es', 'fr', 'de', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']

    first_lang = True
    for lang in language_order:
        if lang in translations and translations[lang]:
            if not first_lang:
                js_content += ",\n"
            first_lang = False

            js_content += f'  "{lang}": {{\n'

            keys = sorted(translations[lang].keys())
            for i, key in enumerate(keys):
                value = translations[lang][key]
                value_escaped = value.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
                comma = "," if i < len(keys) - 1 else ""
                js_content += f'    "{key}": "{value_escaped}"{comma}\n'

            js_content += '  }'

    js_content += "\n};\n\n"

    # Add functions
    js_content += f"""function get{var_name.capitalize()}Translation(key, lang) {{
    if ({var_name}Translations[lang] && {var_name}Translations[lang][key]) {{
        return {var_name}Translations[lang][key];
    }}
    if ({var_name}Translations.en && {var_name}Translations.en[key]) {{
        return {var_name}Translations.en[key];
    }}
    return null;
}}

function apply{var_name.capitalize()}Translations(lang) {{
    console.log('Applying {tool_name} translations for:', lang);
    let count = 0;
    document.querySelectorAll('[data-i18n]').forEach(element => {{
        const key = element.getAttribute('data-i18n');
        if (key && key.startsWith('review.{tool_name}.')) {{
            const translation = get{var_name.capitalize()}Translation(key, lang);
            if (translation) {{
                element.textContent = translation;
                count++;
            }}
        }}
    }});
    console.log(`Applied ${{count}} {tool_name} translations`);
}}

window.addEventListener('languageChanged', (e) => {{
    const lang = e.detail.language;
    setTimeout(() => apply{var_name.capitalize()}Translations(lang), 200);
}});

if (document.readyState === 'loading') {{
    document.addEventListener('DOMContentLoaded', () => {{
        const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
        apply{var_name.capitalize()}Translations(currentLang);
    }});
}} else {{
    const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
    apply{var_name.capitalize()}Translations(currentLang);
}}

console.log('{tool_name} i18n loaded');
"""

    return js_content

print("=" * 70)
print("LEGAL TOOLS - I18N REGENERATION")
print("=" * 70)

for tool_name in TOOLS:
    translations = merge_all_translations(tool_name)

    if not translations:
        print(f"  [SKIP] No data")
        continue

    js_content = generate_i18n_js(tool_name, translations)

    if js_content:
        output_file = os.path.join(JS_DIR, f"{tool_name}-i18n.js")

        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(js_content)

            file_size = os.path.getsize(output_file)
            print(f"  [CREATED] {file_size:,} bytes")
        except Exception as e:
            print(f"  [ERROR] {e}")

print("\n" + "=" * 70)
print("Regeneration Complete!")
print("=" * 70)
