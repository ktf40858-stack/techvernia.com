import json
import os

def merge_and_generate_i18n(tool_name):
    """Fusionne les 3 fichiers batch et génère le fichier i18n JS final"""

    # Lire et fusionner les 3 fichiers batch
    all_translations = {}

    for batch_num in range(1, 4):
        batch_file = f"GenuisNet.ai/pages/reviews/seo/{tool_name}-faqs-batch{batch_num}.json"

        if os.path.exists(batch_file):
            with open(batch_file, 'r', encoding='utf-8') as f:
                batch_data = json.load(f)

                # Fusionner les langues
                for lang, translations in batch_data.items():
                    if lang not in all_translations:
                        all_translations[lang] = {}
                    all_translations[lang].update(translations)
        else:
            print(f"Attention: {batch_file} non trouvé")

    # Générer le fichier JS
    js_content = f"""const {tool_name.replace('-', '')}FaqTranslations = {{
"""

    # Ajouter chaque langue
    for lang in ['es', 'fr', 'de', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']:
        if lang in all_translations:
            js_content += f"    {lang}: {{"

            # Ajouter les traductions
            for key, value in all_translations[lang].items():
                # Échapper les caractères spéciaux
                escaped_value = value.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
                js_content += f'"{key}":"{escaped_value}",'

            # Retirer la dernière virgule et fermer
            js_content = js_content.rstrip(',')
            js_content += "},\n"

    # Fermer l'objet
    js_content = js_content.rstrip(',\n')
    js_content += """
};

function get""" + tool_name.replace('-', '').title().replace('Seo', 'SEO') + """FaqTranslation(key, lang) {
    if (""" + tool_name.replace('-', '') + """FaqTranslations[lang] && """ + tool_name.replace('-', '') + """FaqTranslations[lang][key]) {
        return """ + tool_name.replace('-', '') + """FaqTranslations[lang][key];
    }
    return null;
}

function apply""" + tool_name.replace('-', '').title().replace('Seo', 'SEO') + """FaqTranslations(lang) {
    console.log('Applying """ + tool_name + """ FAQ translations for:', lang);
    let count = 0;
    document.querySelectorAll('[data-i18n]').forEach(element => {
        const key = element.getAttribute('data-i18n');
        if (key && key.startsWith('review.""" + tool_name + """.faq.')) {
            const translation = get""" + tool_name.replace('-', '').title().replace('Seo', 'SEO') + """FaqTranslation(key, lang);
            if (translation) {
                element.textContent = translation;
                count++;
            }
        }
    });
    console.log(`Applied ${count} """ + tool_name + """ FAQ translations`);
}

window.addEventListener('languageChanged', (e) => {
    const lang = e.detail.language;
    setTimeout(() => apply""" + tool_name.replace('-', '').title().replace('Seo', 'SEO') + """FaqTranslations(lang), 200);
});

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
        apply""" + tool_name.replace('-', '').title().replace('Seo', 'SEO') + """FaqTranslations(currentLang);
    });
} else {
    const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
    apply""" + tool_name.replace('-', '').title().replace('Seo', 'SEO') + """FaqTranslations(currentLang);
}

console.log('""" + tool_name + """ FAQ i18n loaded');
"""

    # Sauvegarder le fichier JS
    output_file = f"GenuisNet.ai/js/{tool_name}-faqs-i18n.js"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(js_content)

    print(f"Genere: {output_file}")

    # Compter les traductions
    total_keys = len(all_translations.get('es', {}))
    total_langs = len(all_translations)
    print(f"  - {total_langs} langues")
    print(f"  - {total_keys} cles par langue")
    print(f"  - {total_keys * total_langs} traductions au total")

# Générer les fichiers pour les 3 outils
print("\n=== Generation des fichiers i18n JS finaux ===\n")

tools = ['neuronwriter', 'scalenut', 'surfer-seo']

for tool in tools:
    print(f"\n--- {tool.upper()} ---")
    merge_and_generate_i18n(tool)

print("\n\nTermine! Tous les fichiers i18n JS ont ete generes.")
