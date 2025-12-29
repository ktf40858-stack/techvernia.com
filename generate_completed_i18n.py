"""
Generate i18n files for completed Cybersecurity tools only
"""
import json
import os

# Tools that are fully completed (all 3 batches done, no FAQs pending)
COMPLETED_TOOLS = [
    'abnormal-security',
    'carbon-black',
    'cylance',
    'exabeam',
    'lacework',
    'mcafee-mvision',
    'recorded-future',
    'symantec-endpoint',
    'vectra-ai',
    'wiz',
    'zerofox'
]

def merge_batches(tool_name):
    """Merge all 3 batch files into a single translations object"""
    merged = {}

    for batch_num in range(1, 4):
        batch_file = f"GenuisNet.ai/pages/reviews/cybersecurity/{tool_name}-batch{batch_num}.json"

        if os.path.exists(batch_file):
            with open(batch_file, 'r', encoding='utf-8') as f:
                batch_data = json.load(f)

            # Merge all languages from this batch
            for lang, translations in batch_data.items():
                if lang not in merged:
                    merged[lang] = {}
                merged[lang].update(translations)

    return merged

def generate_i18n_js(tool_name, translations):
    """Generate JavaScript i18n file for a tool"""

    # Build JavaScript content
    var_name = tool_name.replace('-', '_')
    func_name = tool_name.replace('-', '_').title().replace('_', '')

    js_content = f"""const {var_name}_translations = {{\n"""

    # Add all languages (skip English as it's the base)
    for lang in ['es', 'fr', 'de', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']:
        if lang in translations and translations[lang]:
            js_content += f"    {lang}: {json.dumps(translations[lang], ensure_ascii=False, indent=8)},\n"

    js_content += "};\n\n"

    # Add translation function
    js_content += f"""function get{func_name}Translation(key, lang) {{
    if ({var_name}_translations[lang] && {var_name}_translations[lang][key]) {{
        return {var_name}_translations[lang][key];
    }}
    return null;
}}

function apply{func_name}Translations(lang) {{
    console.log('Applying {tool_name} translations for:', lang);
    let count = 0;
    document.querySelectorAll('[data-i18n]').forEach(element => {{
        const key = element.getAttribute('data-i18n');
        if (key && key.startsWith('review.{tool_name}.')) {{
            const translation = get{func_name}Translation(key, lang);
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
    setTimeout(() => apply{func_name}Translations(lang), 200);
}});

if (document.readyState === 'loading') {{
    document.addEventListener('DOMContentLoaded', () => {{
        const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
        apply{func_name}Translations(currentLang);
    }});
}} else {{
    const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
    apply{func_name}Translations(currentLang);
}}

console.log('{tool_name} i18n loaded');
"""

    return js_content

# Main processing
print("\n" + "=" * 70)
print("GENERATING I18N FILES FOR COMPLETED TOOLS")
print("=" * 70)

generated = 0
failed = 0

for tool in COMPLETED_TOOLS:
    print(f"\n{tool}:")

    try:
        # Merge all batches
        merged_translations = merge_batches(tool)

        # Count keys
        en_keys = len(merged_translations.get('en', {}))
        lang_count = sum(len(merged_translations.get(lang, {})) for lang in ['es', 'fr', 'de', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi'])

        print(f"  English keys: {en_keys}")
        print(f"  Translations: {lang_count} ({lang_count // en_keys if en_keys > 0 else 0} languages)")

        # Generate JavaScript file
        js_content = generate_i18n_js(tool, merged_translations)
        js_file = f"GenuisNet.ai/js/{tool}-i18n.js"

        with open(js_file, 'w', encoding='utf-8') as f:
            f.write(js_content)

        print(f"  [OK] Generated {js_file}")
        generated += 1

    except Exception as e:
        print(f"  [FAIL] Error: {e}")
        failed += 1

print("\n" + "=" * 70)
print("GENERATION SUMMARY")
print("=" * 70)
print(f"Successfully generated: {generated}/{len(COMPLETED_TOOLS)}")
print(f"Failed: {failed}")

if generated > 0:
    print(f"\nYou can now test these {generated} tools with live translations!")
    print("The language selector should work on these pages:")
    for tool in COMPLETED_TOOLS[:generated]:
        print(f"  - {tool}.html")

print("\n" + "=" * 70)
