#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de vérification et génération i18n pour outils cybersecurity
Vérifie que titres + contenus sont traduits et génère les fichiers i18n
"""

import os
import json
import re

# Configuration
CYBER_DIR = "GenuisNet.ai/pages/reviews/cybersecurity"
JS_DIR = "GenuisNet.ai/js"

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

def check_batch_files(tool):
    """Vérifie l'état des fichiers batch pour un outil"""
    content_batches = {}
    faq_batches = {}

    # Vérifier les batches de contenu
    for batch in ['batch1', 'batch2', 'batch3']:
        fname = os.path.join(CYBER_DIR, f'{tool}-{batch}.json')
        if os.path.exists(fname):
            size = os.path.getsize(fname) / 1024
            # Considéré complet si > 25 KB
            content_batches[batch] = {'size': size, 'complete': size > 25}
        else:
            content_batches[batch] = {'size': 0, 'complete': False}

    # Vérifier les batches de FAQs (si applicable)
    if tool not in NO_FAQ_TOOLS:
        for batch in ['batch1', 'batch2', 'batch3']:
            fname = os.path.join(CYBER_DIR, f'{tool}-faqs-{batch}.json')
            if os.path.exists(fname):
                size = os.path.getsize(fname) / 1024
                faq_batches[batch] = {'size': size, 'complete': size > 25}
            else:
                faq_batches[batch] = {'size': 0, 'complete': False}

    return content_batches, faq_batches

def merge_translations(tool, has_faqs=True):
    """Merge les traductions des batches"""
    all_translations = {}

    # Charger le fichier EN
    en_file = os.path.join(CYBER_DIR, f'{tool}-en.json')
    if not os.path.exists(en_file):
        return None

    with open(en_file, 'r', encoding='utf-8') as f:
        en_data = json.load(f)

    # Initialiser avec les clés EN
    for key in en_data.keys():
        all_translations[key] = {'en': en_data[key]}

    # Merger les batches 1, 2, 3
    for batch in ['batch1', 'batch2', 'batch3']:
        batch_file = os.path.join(CYBER_DIR, f'{tool}-{batch}.json')
        if os.path.exists(batch_file):
            try:
                with open(batch_file, 'r', encoding='utf-8') as f:
                    batch_data = json.load(f)
                    for key, translations in batch_data.items():
                        if key in all_translations:
                            all_translations[key].update(translations)
            except:
                pass

    # Merger les FAQs si applicable
    if has_faqs:
        for batch in ['batch1', 'batch2', 'batch3']:
            faq_file = os.path.join(CYBER_DIR, f'{tool}-faqs-{batch}.json')
            if os.path.exists(faq_file):
                try:
                    with open(faq_file, 'r', encoding='utf-8') as f:
                        faq_data = json.load(f)
                        for key, translations in faq_data.items():
                            if key in all_translations:
                                all_translations[key].update(translations)
                except:
                    pass

    return all_translations

def generate_i18n_file(tool, translations):
    """Génère le fichier i18n JavaScript"""
    js_content = f"""// {tool} i18n translations
// Auto-generated from batch translation files

const {tool.replace('-', '_')}_translations = {{
"""

    # Organiser par langue
    languages = {}
    for key, trans in translations.items():
        for lang, text in trans.items():
            if lang != 'en':
                if lang not in languages:
                    languages[lang] = {}
                languages[lang][key] = text

    # Générer le contenu
    for lang in sorted(languages.keys()):
        js_content += f"    {lang}: {{\n"
        for key in sorted(languages[lang].keys()):
            value = languages[lang][key].replace('"', '\\"').replace('\n', '\\n')
            js_content += f'        "{key}": "{value}",\n'
        js_content = js_content.rstrip(',\n') + '\n'
        js_content += "    },\n"

    js_content = js_content.rstrip(',\n') + '\n'
    js_content += """};

// Helper functions
function get_translation(key, lang) {
    if (""" + tool.replace('-', '_') + """_translations[lang] && """ + tool.replace('-', '_') + """_translations[lang][key]) {
        return """ + tool.replace('-', '_') + """_translations[lang][key];
    }
    return null;
}

function apply_translations(lang) {
    console.log('Applying """ + tool + """ translations for:', lang);
    let count = 0;
    document.querySelectorAll('[data-i18n]').forEach(element => {
        const key = element.getAttribute('data-i18n');
        if (key) {
            const translation = get_translation(key, lang);
            if (translation) {
                element.textContent = translation;
                count++;
            }
        }
    });
    console.log(`Applied ${count} """ + tool + """ translations`);
}

// Event listeners
window.addEventListener('languageChanged', (e) => {
    const lang = e.detail.language;
    setTimeout(() => apply_translations(lang), 200);
});

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
        apply_translations(currentLang);
    });
} else {
    const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
    apply_translations(currentLang);
}

console.log('""" + tool + """ i18n loaded');
"""

    # Sauvegarder
    output_file = os.path.join(JS_DIR, f'{tool}-i18n.js')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(js_content)

    return output_file

def main():
    print("=" * 80)
    print("VERIFICATION ET GENERATION I18N - CYBERSECURITY TOOLS")
    print("=" * 80)

    ready_for_i18n = []
    partial_content = []
    partial_faqs = []

    for tool in ALL_TOOLS:
        content_batches, faq_batches = check_batch_files(tool)

        # Vérifier si le contenu est complet
        content_complete = all(b['complete'] for b in content_batches.values())

        # Vérifier si les FAQs sont complètes (si applicable)
        if tool not in NO_FAQ_TOOLS:
            faqs_complete = all(b['complete'] for b in faq_batches.values()) if faq_batches else False
        else:
            faqs_complete = True  # Pas de FAQs = considéré complet

        status = {
            'tool': tool,
            'content_complete': content_complete,
            'faqs_complete': faqs_complete,
            'content_batches': content_batches,
            'faq_batches': faq_batches
        }

        if content_complete and faqs_complete:
            ready_for_i18n.append(status)
        elif content_complete and not faqs_complete:
            partial_faqs.append(status)
        else:
            partial_content.append(status)

    # Afficher les résultats
    print(f"\n[OK] PRETS POUR I18N ({len(ready_for_i18n)}):")
    for s in ready_for_i18n:
        print(f"  - {s['tool']}")

    print(f"\n[FAQS] CONTENU OK, FAQS EN COURS ({len(partial_faqs)}):")
    for s in partial_faqs:
        print(f"  - {s['tool']}")

    print(f"\n[PARTIAL] CONTENU INCOMPLET ({len(partial_content)}):")
    for s in partial_content:
        tool = s['tool']
        cb = s['content_batches']
        print(f"  - {tool}:")
        for batch, info in cb.items():
            status = "OK" if info['complete'] else "PARTIEL"
            print(f"      {batch}: {info['size']:.1f} KB [{status}]")

    # Générer les fichiers i18n pour les outils prêts
    print(f"\n{'=' * 80}")
    print("GENERATION DES FICHIERS I18N")
    print("=" * 80)

    generated = 0
    for status in ready_for_i18n:
        tool = status['tool']
        has_faqs = tool not in NO_FAQ_TOOLS

        print(f"\nTraitement de {tool}...")
        translations = merge_translations(tool, has_faqs)

        if translations:
            output_file = generate_i18n_file(tool, translations)
            num_keys = len(translations)
            num_langs = len(set(lang for trans in translations.values() for lang in trans.keys())) - 1
            print(f"  [OK] {output_file}")
            print(f"       {num_keys} clés x {num_langs} langues = {num_keys * num_langs} traductions")
            generated += 1
        else:
            print(f"  [ERREUR] Impossible de charger les traductions")

    print(f"\n{'=' * 80}")
    print(f"RESUME: {generated} fichiers i18n générés")
    print("=" * 80)

if __name__ == "__main__":
    main()
