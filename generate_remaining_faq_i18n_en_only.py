import json

def generate_faq_i18n_js_en_only(tool_name):
    """Génère le fichier JS i18n pour les FAQs avec seulement EN"""
    en_file = f"GenuisNet.ai/pages/reviews/seo/{tool_name}-faqs-en.json"

    try:
        with open(en_file, 'r', encoding='utf-8') as f:
            en_data = json.load(f)
    except FileNotFoundError:
        print(f"Fichier {en_file} non trouve")
        return

    if not en_data:
        print(f"Aucune donnee dans {en_file}")
        return

    # Compter les FAQs
    num_faqs = len([k for k in en_data.keys() if k.endswith('.q1')]) or len(en_data) // 2

    print(f"\nGeneration de {tool_name}-faqs-i18n.js avec {num_faqs} FAQs...")

    # Structure du fichier JS - Placeholder pour les autres langues
    js_content = f"""const {tool_name.replace('-', '')}FaqTranslations = {{
    // Traductions EN disponibles, autres langues a venir
    en: {json.dumps(en_data, ensure_ascii=False, indent=8)[1:-1]},
    de: {{}},
    pt: {{}},
    zh: {{}},
    ja: {{}},
    ko: {{}},
    ar: {{}},
    hi: {{}},
    es: {{}},
    fr: {{}}
}};

function get{tool_name.replace('-', '').title()}FaqTranslation(key, lang) {{
    if ({tool_name.replace('-', '')}FaqTranslations[lang] && {tool_name.replace('-', '')}FaqTranslations[lang][key]) {{
        return {tool_name.replace('-', '')}FaqTranslations[lang][key];
    }}
    // Fallback to EN
    if ({tool_name.replace('-', '')}FaqTranslations.en && {tool_name.replace('-', '')}FaqTranslations.en[key]) {{
        return {tool_name.replace('-', '')}FaqTranslations.en[key];
    }}
    return null;
}}

function apply{tool_name.replace('-', '').title()}FaqTranslations(lang) {{
    console.log('Applying {tool_name} FAQ translations for:', lang);
    let count = 0;
    document.querySelectorAll('[data-i18n^="review.{tool_name}.faq"]').forEach(element => {{
        const key = element.getAttribute('data-i18n');
        if (key) {{
            const translation = get{tool_name.replace('-', '').title()}FaqTranslation(key, lang);
            if (translation) {{
                element.textContent = translation;
                count++;
            }}
        }}
    }});
    console.log(`Applied ${{count}} {tool_name} FAQ translations`);
}}

window.addEventListener('languageChanged', (e) => {{
    const lang = e.detail.language;
    setTimeout(() => apply{tool_name.replace('-', '').title()}FaqTranslations(lang), 200);
}});

if (document.readyState === 'loading') {{
    document.addEventListener('DOMContentLoaded', () => {{
        const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
        apply{tool_name.replace('-', '').title()}FaqTranslations(currentLang);
    }});
}} else {{
    const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
    apply{tool_name.replace('-', '').title()}FaqTranslations(currentLang);
}}

console.log('{tool_name} FAQs i18n loaded');
"""

    # Écrire le fichier
    output_file = f"GenuisNet.ai/js/{tool_name}-faqs-i18n.js"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(js_content)

    print(f"Genere: {output_file}")

# Générer les fichiers pour les 3 outils restants
tools = ['neuronwriter', 'scalenut', 'surfer-seo']

for tool in tools:
    generate_faq_i18n_js_en_only(tool)

print("\nTous les fichiers FAQs i18n (EN only) ont ete generes!")
print("\nNote: Les traductions dans les autres langues seront ajoutees via l'API de traduction.")
