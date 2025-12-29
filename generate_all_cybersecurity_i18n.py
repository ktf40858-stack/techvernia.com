#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Génération complète des fichiers i18n pour cybersecurity
Format des batches : { "lang": { "key": "value" } }
"""

import os
import json

# Configuration
CYBER_DIR = "GenuisNet.ai/pages/reviews/cybersecurity"
JS_DIR = "GenuisNet.ai/js"

# Langues attendues (9 langues sans italien)
EXPECTED_LANGS = ['de', 'es', 'fr', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']

# Tous les outils cybersecurity
ALL_TOOLS = [
    'abnormal-security', 'carbon-black', 'cisco-securex', 'cortex-xdr',
    'crowdstrike', 'cyberark', 'cybereason', 'cylance', 'darktrace',
    'exabeam', 'fortinet', 'ibm-qradar', 'lacework', 'mcafee-mvision',
    'microsoft-sentinel', 'okta', 'palo-alto-ngfw', 'qualys', 'rapid7',
    'recorded-future', 'sentinelone', 'snyk', 'sophos-interceptx',
    'splunk-security', 'symantec-endpoint', 'tenable',
    'trend-micro-vision-one', 'vectra-ai', 'wiz', 'zerofox'
]

# Outils sans FAQs
NO_FAQ_TOOLS = ['cybereason', 'snyk']

def merge_batches(tool, include_faqs=True):
    """Fusionne les batches de traduction pour un outil"""
    # Structure finale : { "lang": { "key": "value" } }
    merged = {}

    # Initialiser avec les langues attendues
    for lang in EXPECTED_LANGS:
        merged[lang] = {}

    # Fusionner les 3 batches de contenu
    for batch_num in [1, 2, 3]:
        batch_file = os.path.join(CYBER_DIR, f'{tool}-batch{batch_num}.json')
        if os.path.exists(batch_file):
            try:
                with open(batch_file, 'r', encoding='utf-8') as f:
                    batch_data = json.load(f)
                    # batch_data = { "lang": { "key": "value" } }
                    for lang, translations in batch_data.items():
                        if lang in EXPECTED_LANGS:
                            merged[lang].update(translations)
            except Exception as e:
                print(f"    [WARN] Erreur lecture {batch_file}: {e}")

    # Fusionner les 3 batches de FAQs (si applicable)
    if include_faqs and tool not in NO_FAQ_TOOLS:
        for batch_num in [1, 2, 3]:
            faq_file = os.path.join(CYBER_DIR, f'{tool}-faqs-batch{batch_num}.json')
            if os.path.exists(faq_file):
                try:
                    with open(faq_file, 'r', encoding='utf-8') as f:
                        faq_data = json.load(f)
                        for lang, translations in faq_data.items():
                            if lang in EXPECTED_LANGS:
                                merged[lang].update(translations)
                except Exception as e:
                    print(f"    [WARN] Erreur lecture {faq_file}: {e}")

    # Retirer les langues vides
    merged = {lang: trans for lang, trans in merged.items() if trans}

    return merged

def generate_i18n_file(tool, translations):
    """Génère le fichier i18n JavaScript"""
    var_name = tool.replace('-', '_')

    js_content = f"""// {tool} i18n translations
// Auto-generated from batch translation files

const {var_name}_translations = {{
"""

    # Générer le contenu par langue
    for lang in sorted(translations.keys()):
        js_content += f"    {lang}: {{\n"
        for key in sorted(translations[lang].keys()):
            value = translations[lang][key].replace('"', '\\"').replace('\n', '\\n')
            js_content += f'        "{key}": "{value}",\n'
        js_content = js_content.rstrip(',\n') + '\n'
        js_content += "    },\n"

    js_content = js_content.rstrip(',\n') + '\n'
    js_content += f"""
}};

// Helper functions
function get{var_name}Translation(key, lang) {{
    if ({var_name}_translations[lang] && {var_name}_translations[lang][key]) {{
        return {var_name}_translations[lang][key];
    }}
    return null;
}}

function apply{var_name}Translations(lang) {{
    console.log('Applying {tool} translations for:', lang);
    let count = 0;
    document.querySelectorAll('[data-i18n]').forEach(element => {{
        const key = element.getAttribute('data-i18n');
        if (key) {{
            const translation = get{var_name}Translation(key, lang);
            if (translation) {{
                element.textContent = translation;
                count++;
            }}
        }}
    }});
    console.log(`Applied ${{count}} {tool} translations`);
}}

// Event listeners
window.addEventListener('languageChanged', (e) => {{
    const lang = e.detail.language;
    setTimeout(() => apply{var_name}Translations(lang), 200);
}});

if (document.readyState === 'loading') {{
    document.addEventListener('DOMContentLoaded', () => {{
        const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
        apply{var_name}Translations(currentLang);
    }});
}} else {{
    const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
    apply{var_name}Translations(currentLang);
}}

console.log('{tool} i18n loaded');
"""

    # Sauvegarder
    output_file = os.path.join(JS_DIR, f'{tool}-i18n.js')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(js_content)

    return output_file

def check_tool_completeness(tool):
    """Vérifie si un outil a toutes ses traductions"""
    # Vérifier les 3 batches de contenu
    content_langs = set()
    for batch_num in [1, 2, 3]:
        batch_file = os.path.join(CYBER_DIR, f'{tool}-batch{batch_num}.json')
        if os.path.exists(batch_file):
            try:
                with open(batch_file, 'r', encoding='utf-8') as f:
                    batch_data = json.load(f)
                    content_langs.update(lang for lang in batch_data.keys() if lang in EXPECTED_LANGS)
            except:
                pass

    content_complete = len(content_langs) >= 9  # 9 langues minimum

    # Vérifier les FAQs si applicable
    if tool in NO_FAQ_TOOLS:
        faq_complete = True
        faq_langs = set()
    else:
        faq_langs = set()
        for batch_num in [1, 2, 3]:
            faq_file = os.path.join(CYBER_DIR, f'{tool}-faqs-batch{batch_num}.json')
            if os.path.exists(faq_file):
                try:
                    with open(faq_file, 'r', encoding='utf-8') as f:
                        faq_data = json.load(f)
                        faq_langs.update(lang for lang in faq_data.keys() if lang in EXPECTED_LANGS)
                except:
                    pass
        faq_complete = len(faq_langs) >= 9

    return content_complete, faq_complete, content_langs, faq_langs

def main():
    print("=" * 80)
    print("GENERATION I18N - CYBERSECURITY TOOLS")
    print("=" * 80)

    complete_tools = []
    content_only = []
    incomplete = []

    # Analyser tous les outils
    for tool in ALL_TOOLS:
        content_ok, faq_ok, content_langs, faq_langs = check_tool_completeness(tool)

        if content_ok and faq_ok:
            complete_tools.append({'tool': tool, 'content': len(content_langs), 'faq': len(faq_langs)})
        elif content_ok:
            content_only.append({'tool': tool, 'content': len(content_langs), 'faq': len(faq_langs)})
        else:
            incomplete.append({'tool': tool, 'content': len(content_langs), 'faq': len(faq_langs)})

    # Afficher le résumé
    print(f"\n[COMPLET] Contenu + FAQs ({len(complete_tools)}):")
    for item in complete_tools:
        print(f"  - {item['tool']:30s} ({item['content']} langs contenu, {item['faq']} langs FAQs)")

    print(f"\n[PARTIEL] Contenu OK, FAQs en cours ({len(content_only)}):")
    for item in content_only:
        print(f"  - {item['tool']:30s} ({item['content']} langs contenu, {item['faq']} langs FAQs)")

    print(f"\n[INCOMPLET] Contenu incomplet ({len(incomplete)}):")
    for item in incomplete:
        print(f"  - {item['tool']:30s} ({item['content']} langs contenu, {item['faq']} langs FAQs)")

    # Générer les fichiers i18n pour les outils avec contenu complet
    tools_to_generate = complete_tools + content_only

    if not tools_to_generate:
        print("\n[INFO] Aucun outil prêt pour génération i18n")
        return

    print(f"\n{'=' * 80}")
    print(f"GENERATION DE {len(tools_to_generate)} FICHIERS I18N")
    print("=" * 80)

    generated = 0
    for item in tools_to_generate:
        tool = item['tool']
        include_faqs = tool not in NO_FAQ_TOOLS and item['faq'] >= 9

        print(f"\n{tool}:")
        translations = merge_batches(tool, include_faqs)

        if translations:
            output_file = generate_i18n_file(tool, translations)

            # Calculer les stats
            num_keys = sum(len(trans) for trans in translations.values()) // len(translations)
            num_langs = len(translations)
            total_trans = sum(len(trans) for trans in translations.values())

            print(f"  [OK] {output_file}")
            print(f"       ~{num_keys} clés × {num_langs} langues = {total_trans} traductions")
            generated += 1
        else:
            print(f"  [ERREUR] Aucune traduction trouvée")

    print(f"\n{'=' * 80}")
    print(f"TERMINE: {generated}/{len(tools_to_generate)} fichiers i18n générés")
    print("=" * 80)

if __name__ == "__main__":
    main()
