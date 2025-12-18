#!/usr/bin/env python3
"""
Créer un fichier i18n séparé pour CHAQUE outil image
"""
import json
import os
import re

print("=" * 80)
print("🚀 CRÉATION DES FICHIERS I18N POUR TOUS LES OUTILS IMAGE")
print("=" * 80)
print()

# Liste des outils image
image_tools = [
    'adobe-firefly',
    'canva-ai',
    'clipdrop',
    'dall-e-3',
    'ideogram',
    'leonardo-ai',
    'midjourney',
    'stable-diffusion'
]

# Langues
languages = ['es', 'fr', 'de', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']

# Charger toutes les traductions une seule fois
print("📥 Chargement des traductions...")
all_translations = {}
for lang in languages:
    try:
        with open(f'all_full_translations_{lang}.json', 'r', encoding='utf-8') as f:
            all_translations[lang] = json.load(f)
        print(f"  ✓ {lang.upper()}: {len(all_translations[lang])} clés")
    except FileNotFoundError:
        print(f"  ❌ {lang.upper()}: Fichier non trouvé")
        all_translations[lang] = {}

print()

# Pour chaque outil
for tool in image_tools:
    print(f"🔧 Traitement: {tool}")

    # Convertir tool-name en tool.name pour les clés
    tool_key = tool.replace('-', '.')

    # Créer l'objet translations pour cet outil
    tool_translations = {
        'en': {}
    }

    # Extraire les clés EN depuis le fichier JSON correspondant
    json_filename = f"{tool.replace('-', '_')}_content_to_translate.json"

    if os.path.exists(json_filename):
        with open(json_filename, 'r', encoding='utf-8') as f:
            en_keys = json.load(f)

        # Filtrer seulement les clés de CONTENU (pas les standards)
        # Les clés standards sont: overview, key.features, pros.cons, etc.
        standard_patterns = [
            'overview', 'key.features', 'pros.cons', 'pricing', 'getting.started',
            'verdict', 'comparison', 'use.cases', 'limitations', 'alternatives',
            'faq', 'badge', 'btn', 'case', 'step', 'plan', 'tier', 'level'
        ]

        content_keys = {}
        for key, value in en_keys.items():
            # Vérifier si c'est une clé standard
            is_standard = any(pattern in key for pattern in standard_patterns)
            if not is_standard:
                content_keys[key] = value

        tool_translations['en'] = content_keys
        print(f"  ✓ EN: {len(content_keys)} clés de contenu")
    else:
        print(f"  ⚠️  Fichier {json_filename} non trouvé, recherche dans all_full_translations...")

        # Fallback: extraire depuis all_full_translations_en.json
        if os.path.exists('all_full_translations_en.json'):
            with open('all_full_translations_en.json', 'r', encoding='utf-8') as f:
                all_en = json.load(f)

            # Filtrer les clés de cet outil
            prefix = f'review.{tool_key}.'
            tool_keys = {k: v for k, v in all_en.items() if k.startswith(prefix)}

            # Filtrer les standards
            standard_patterns = [
                'overview', 'key.features', 'pros.cons', 'pricing', 'getting.started',
                'verdict', 'comparison', 'use.cases', 'limitations', 'alternatives',
                'faq', 'badge', 'btn', 'case', 'step', 'plan', 'tier', 'level'
            ]

            content_keys = {}
            for key, value in tool_keys.items():
                is_standard = any(pattern in key for pattern in standard_patterns)
                if not is_standard:
                    content_keys[key] = value

            tool_translations['en'] = content_keys
            print(f"  ✓ EN: {len(content_keys)} clés de contenu")

    # Extraire les traductions pour les autres langues
    prefix = f'review.{tool_key}.'
    for lang in languages:
        if lang not in all_translations:
            continue

        # Filtrer les clés de cet outil
        tool_keys = {k: v for k, v in all_translations[lang].items() if k.startswith(prefix)}

        # Filtrer les standards
        content_keys = {}
        for key, value in tool_keys.items():
            is_standard = any(pattern in key for pattern in standard_patterns)
            if not is_standard:
                content_keys[key] = value

        tool_translations[lang] = content_keys
        print(f"  ✓ {lang.upper()}: {len(content_keys)} clés")

    # Créer le fichier JavaScript
    # Convertir tool-name en camelCase pour les noms de variables
    var_name = ''.join(word.capitalize() for word in tool.split('-'))

    js_content = f"""/* {tool.upper()} Translations */
const {var_name.lower()}Translations = {json.dumps(tool_translations, ensure_ascii=False, indent=2)};

// Fonction pour obtenir une traduction
function get{var_name}Translation(key, lang) {{
    if ({var_name.lower()}Translations[lang] && {var_name.lower()}Translations[lang][key]) {{
        return {var_name.lower()}Translations[lang][key];
    }}
    // Fallback à l'anglais
    if ({var_name.lower()}Translations.en && {var_name.lower()}Translations.en[key]) {{
        return {var_name.lower()}Translations.en[key];
    }}
    return null;
}}

// Appliquer les traductions {tool}
function apply{var_name}Translations(lang) {{
    console.log('🔥 Applying {tool} translations for:', lang);

    let count = 0;
    document.querySelectorAll('[data-i18n]').forEach(element => {{
        const key = element.getAttribute('data-i18n');

        // Seulement pour les clés {tool}
        if (key && key.startsWith('review.{tool_key}.')) {{
            const translation = get{var_name}Translation(key, lang);
            if (translation) {{
                element.textContent = translation;
                count++;
            }}
        }}
    }});

    console.log(`✅ Applied ${{count}} {tool} translations`);
}}

// Auto-appliquer quand la langue change
window.addEventListener('languageChanged', (e) => {{
    const lang = e.detail.language;
    setTimeout(() => apply{var_name}Translations(lang), 200);
}});

// Appliquer au chargement
if (document.readyState === 'loading') {{
    document.addEventListener('DOMContentLoaded', () => {{
        const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
        apply{var_name}Translations(currentLang);
    }});
}} else {{
    const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
    apply{var_name}Translations(currentLang);
}}

console.log('✅ {tool} i18n loaded');
"""

    # Sauvegarder le fichier
    output_file = f'GenuisNet.ai/js/{tool}-i18n.js'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(js_content)

    print(f"  ✅ Fichier créé: {output_file}")
    print()

print()
print("=" * 80)
print("✅ TOUS LES FICHIERS I18N ONT ÉTÉ CRÉÉS!")
print("=" * 80)
print()
print("Prochaine étape: Ajouter les scripts dans chaque fichier HTML")
