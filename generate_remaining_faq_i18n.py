import json
import os

# Outils avec fichiers batch existants mais sans fichier i18n JS
tools_with_batches = [
    {'name': 'ahrefs', 'faqs': 6},
    {'name': 'semrush', 'faqs': 7},
    {'name': 'surfer-seo', 'faqs': 6}
]

languages = {
    'de': 'Allemand',
    'pt': 'Portugais',
    'zh': 'Chinois',
    'ja': 'Japonais',
    'ko': 'Coréen',
    'ar': 'Arabe',
    'hi': 'Hindi',
    'es': 'Espagnol',
    'fr': 'Français'
}

def merge_batches(tool_name):
    """Fusionne les 3 fichiers batch en un seul dictionnaire"""
    translations = {}

    for i in range(1, 4):
        batch_file = f"GenuisNet.ai/pages/reviews/seo/{tool_name}-faqs-batch{i}.json"
        if os.path.exists(batch_file):
            with open(batch_file, 'r', encoding='utf-8') as f:
                batch = json.load(f)
                translations.update(batch)

    return translations

def generate_faq_i18n_js(tool_name, num_faqs):
    """Génère le fichier JS i18n pour les FAQs"""
    print(f"\nGeneration de {tool_name}-faqs-i18n.js...")

    # Fusionner les batches
    all_translations = merge_batches(tool_name)

    if not all_translations:
        print(f"Aucune traduction trouvee pour {tool_name}")
        return

    # Structure du fichier JS
    js_content = f"""const {tool_name.replace('-', '')}FaqTranslations = {{\n"""

    # Pour chaque langue
    for lang_code, lang_name in languages.items():
        js_content += f"    {lang_code}: {{\n"

        # Pour chaque FAQ (q et a)
        for faq_num in range(1, num_faqs + 1):
            q_key = f"review.{tool_name}.faq.q{faq_num}"
            a_key = f"review.{tool_name}.faq.a{faq_num}"

            # Récupérer les traductions
            q_translation = all_translations.get(lang_code, {}).get(q_key, "")
            a_translation = all_translations.get(lang_code, {}).get(a_key, "")

            if q_translation:
                # Échapper les guillemets et les retours à la ligne
                q_translation = q_translation.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
                js_content += f'        "{q_key}": "{q_translation}",\n'

            if a_translation:
                a_translation = a_translation.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
                js_content += f'        "{a_key}": "{a_translation}",\n'

        # Enlever la dernière virgule
        js_content = js_content.rstrip(',\n') + '\n'
        js_content += "    },\n"

    js_content = js_content.rstrip(',\n') + '\n'
    js_content += "};\n\n"

    # Ajouter les fonctions helper
    js_content += f"""
function get{tool_name.replace('-', '').title()}FaqTranslation(key, lang) {{
    if ({tool_name.replace('-', '')}FaqTranslations[lang] && {tool_name.replace('-', '')}FaqTranslations[lang][key]) {{
        return {tool_name.replace('-', '')}FaqTranslations[lang][key];
    }}
    return null;
}}

function apply{tool_name.replace('-', '').title()}FaqTranslations(lang) {{
    console.log('🔥 Applying {tool_name} FAQ translations for:', lang);
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
    console.log(`✅ Applied ${{count}} {tool_name} FAQ translations`);
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

console.log('✅ {tool_name} FAQs i18n loaded');
"""

    # Écrire le fichier
    output_file = f"GenuisNet.ai/js/{tool_name}-faqs-i18n.js"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(js_content)

    print(f"Genere: {output_file}")

# Générer tous les fichiers
for tool in tools_with_batches:
    generate_faq_i18n_js(tool['name'], tool['faqs'])

print("\nTous les fichiers FAQs i18n ont ete generes!")
