"""
Final script to merge translations and generate i18n files for AI Business tools
Run this AFTER all 48 translation agents have completed
"""
import json
import os
import re

TOOLS = ['chorusai', 'conversica', 'drift', 'gong', 'hubspot-ai', 'looker', 'salesforce-einstein', 'tableau']

def merge_translations_for_tool(tool_name):
    """Merge content and FAQ translations into a single i18n file"""
    print(f"\n{'='*60}")
    print(f"Merging translations for {tool_name.upper()}")
    print(f"{'='*60}")

    merged = {}

    # Merge content translations from 3 batches
    for batch_num in range(1, 4):
        batch_file = f"GenuisNet.ai/pages/reviews/business/{tool_name}-batch{batch_num}.json"
        if os.path.exists(batch_file):
            with open(batch_file, 'r', encoding='utf-8') as f:
                batch_data = json.load(f)
                for lang, translations in batch_data.items():
                    if lang not in merged:
                        merged[lang] = {}
                    merged[lang].update(translations)
            print(f"  Merged {tool_name}-batch{batch_num}.json")

    # Merge FAQ translations from 3 batches
    for batch_num in range(1, 4):
        faq_batch_file = f"GenuisNet.ai/pages/reviews/business/{tool_name}-faqs-batch{batch_num}.json"
        if os.path.exists(faq_batch_file):
            with open(faq_batch_file, 'r', encoding='utf-8') as f:
                faq_batch_data = json.load(f)
                for lang, translations in faq_batch_data.items():
                    if lang not in merged:
                        merged[lang] = {}
                    merged[lang].update(translations)
            print(f"  Merged {tool_name}-faqs-batch{batch_num}.json")

    # Add English from source files
    en_content_file = f"GenuisNet.ai/pages/reviews/business/{tool_name}-en.json"
    en_faq_file = f"GenuisNet.ai/pages/reviews/business/{tool_name}-faqs-en.json"

    merged['en'] = {}
    if os.path.exists(en_content_file):
        with open(en_content_file, 'r', encoding='utf-8') as f:
            merged['en'].update(json.load(f))
    if os.path.exists(en_faq_file):
        with open(en_faq_file, 'r', encoding='utf-8') as f:
            merged['en'].update(json.load(f))

    # Count keys
    total_keys = len(merged.get('en', {}))
    total_langs = len(merged)

    print(f"\n  Total languages: {total_langs}")
    print(f"  Keys per language: {total_keys}")
    print(f"  Total translations: {total_keys * total_langs}")

    return merged, total_keys, total_langs

def generate_i18n_js(tool_name, translations, total_keys, total_langs):
    """Generate JavaScript i18n file"""
    # Convert tool-name to camelCase for JavaScript
    tool_camel = tool_name.replace('-', '')
    tool_title = tool_name.replace('-', ' ').title().replace(' ', '')

    js_content = f"const {tool_camel}Translations = {{\n"

    # Add each language
    for lang in ['es', 'fr', 'de', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']:
        if lang in translations:
            js_content += f"    {lang}: {{"

            # Add translations
            for key, value in translations[lang].items():
                # Escape special characters
                escaped_value = value.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n').replace('\r', '')
                js_content += f'"{key}":"{escaped_value}",'

            # Remove last comma and close
            js_content = js_content.rstrip(',')
            js_content += "},\n"

    # Close object
    js_content = js_content.rstrip(',\n')
    js_content += f"""
}};

function get{tool_title}Translation(key, lang) {{
    if ({tool_camel}Translations[lang] && {tool_camel}Translations[lang][key]) {{
        return {tool_camel}Translations[lang][key];
    }}
    if ({tool_camel}Translations.en && {tool_camel}Translations.en[key]) {{
        return {tool_camel}Translations.en[key];
    }}
    return null;
}}

function apply{tool_title}Translations(lang) {{
    console.log('Applying {tool_name} translations for:', lang);
    let count = 0;
    document.querySelectorAll('[data-i18n]').forEach(element => {{
        const key = element.getAttribute('data-i18n');
        if (key && key.startsWith('review.{tool_name}.')) {{
            const translation = get{tool_title}Translation(key, lang);
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
    setTimeout(() => apply{tool_title}Translations(lang), 200);
}});

if (document.readyState === 'loading') {{
    document.addEventListener('DOMContentLoaded', () => {{
        const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
        apply{tool_title}Translations(currentLang);
    }});
}} else {{
    const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
    apply{tool_title}Translations(currentLang);
}}

console.log('{tool_name} i18n loaded');
"""

    # Save JavaScript file
    output_file = f"GenuisNet.ai/js/{tool_name}-i18n.js"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(js_content)

    print(f"\n  Created: {output_file}")
    print(f"  File size: {len(js_content)} characters")

# Process all tools
print("\n" + "="*60)
print("FINALIZING AI BUSINESS I18N FILES")
print("="*60)

for tool in TOOLS:
    try:
        translations, total_keys, total_langs = merge_translations_for_tool(tool)
        generate_i18n_js(tool, translations, total_keys, total_langs)
        print(f"\n  [OK] {tool} completed successfully!")
    except Exception as e:
        print(f"\n  [ERROR] processing {tool}: {str(e)}")

print("\n" + "="*60)
print("ALL I18N FILES GENERATED!")
print("="*60)
print("\nNext step: Integrate i18n scripts into HTML files")
