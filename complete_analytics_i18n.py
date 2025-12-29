#!/usr/bin/env python3
"""
Complete Analytics i18n Translation Script
Processes batch JSON files and creates complete multilingual i18n JavaScript files
"""

import json
import os
import sys

# Tools that need multilingual support
TOOLS_TO_PROCESS = [
    'datarobot',
    'domo-ai',
    'h2oai',
    'microstrategy-ai',
    'power-bi-copilot',
    'qlik-sense-ai',
    'sisense-ai',
    'yellowfin-ai'
]

ANALYTICS_DIR = 'GenuisNet.ai/pages/reviews/analytics'
JS_DIR = 'GenuisNet.ai/js'

def load_json_file(filepath):
    """Load JSON file safely"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return None

def merge_translations(tool_name):
    """Merge all batch files for a tool"""
    print(f"\n=== Processing {tool_name} ===")

    # Load English base
    en_file = os.path.join(ANALYTICS_DIR, f"{tool_name}-en.json")
    en_data = load_json_file(en_file)
    if not en_data:
        print(f"  [X] No English file found: {en_file}")
        return None

    print(f"  [OK] Loaded {len(en_data)} English keys")

    # Initialize result with English
    result = {
        "en": en_data
    }

    # Load batch files
    for batch_num in [1, 2, 3]:
        batch_file = os.path.join(ANALYTICS_DIR, f"{tool_name}-batch{batch_num}.json")
        batch_data = load_json_file(batch_file)

        if batch_data:
            # Count non-empty languages
            non_empty = 0
            for lang, translations in batch_data.items():
                if translations and len(translations) > 0:
                    result[lang] = translations
                    non_empty += 1

            if non_empty > 0:
                print(f"  [OK] Batch {batch_num}: {non_empty} languages loaded")
            else:
                print(f"  [!] Batch {batch_num}: All languages empty (needs translation)")
        else:
            print(f"  [!] Batch {batch_num}: File not found or invalid")

    return result

def generate_i18n_js(tool_name, translations):
    """Generate JavaScript i18n file"""
    if not translations:
        return None

    # Convert tool name to variable name (replace hyphens with underscores)
    var_name = tool_name.replace('-', '')

    # Build JavaScript file
    js_content = f"// {tool_name.upper()} I18N\n"
    js_content += f"const {var_name}Translations = {{\n"

    # Add each language
    language_order = ['en', 'es', 'fr', 'de', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']

    first_lang = True
    for lang in language_order:
        if lang in translations and translations[lang]:
            if not first_lang:
                js_content += ",\n"
            first_lang = False

            js_content += f'  "{lang}": {{\n'

            # Add all translations for this language
            keys = sorted(translations[lang].keys())
            for i, key in enumerate(keys):
                value = translations[lang][key]
                # Escape quotes and special characters
                value_escaped = value.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')

                comma = "," if i < len(keys) - 1 else ""
                js_content += f'    "{key}": "{value_escaped}"{comma}\n'

            js_content += '  }'

    js_content += "\n};\n\n"

    # Add translation function
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
    console.log('🔥 Applying {tool_name} translations for:', lang);
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
    console.log(`✅ Applied ${{count}} {tool_name} translations`);
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

console.log('✅ {tool_name} i18n loaded');
"""

    return js_content

def main():
    print("=" * 60)
    print("Analytics Tools i18n Completion Script")
    print("=" * 60)

    for tool_name in TOOLS_TO_PROCESS:
        # Merge all translations
        translations = merge_translations(tool_name)

        if not translations:
            print(f"  [SKIP] {tool_name} - no data")
            continue

        # Check how many languages we have
        lang_count = len([lang for lang in translations if translations[lang]])
        print(f"  [STATS] Total languages: {lang_count}")

        # Generate JavaScript
        js_content = generate_i18n_js(tool_name, translations)

        if js_content:
            output_file = os.path.join(JS_DIR, f"{tool_name}-i18n.js")

            try:
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(js_content)

                # Get file size
                file_size = os.path.getsize(output_file)
                print(f"  [CREATED] {output_file} ({file_size:,} bytes)")
            except Exception as e:
                print(f"  [ERROR] Error writing file: {e}")

    print("\n" + "=" * 60)
    print("[DONE] Processing complete!")
    print("=" * 60)

if __name__ == '__main__':
    main()
