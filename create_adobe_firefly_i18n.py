#!/usr/bin/env python3
"""
Créer un fichier i18n séparé pour Adobe Firefly
"""
import json

print("🚀 Création de adobe-firefly-i18n.js...")

# Langues
languages = ['es', 'fr', 'de', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']

# Créer l'objet translations
translations_obj = {
    'en': {}
}

# Charger l'anglais depuis image_content_keys_to_translate.json
with open('image_content_keys_to_translate.json', 'r', encoding='utf-8') as f:
    en_keys = json.load(f)
    translations_obj['en'] = en_keys
    print(f"✓ EN: {len(en_keys)} clés chargées")

# Charger les autres langues
for lang in languages:
    try:
        with open(f'all_full_translations_{lang}.json', 'r', encoding='utf-8') as f:
            all_trans = json.load(f)

        # Filtrer seulement les clés Adobe Firefly
        firefly_trans = {k: v for k, v in all_trans.items() if k.startswith('review.adobe-firefly.')}
        translations_obj[lang] = firefly_trans
        print(f"✓ {lang.upper()}: {len(firefly_trans)} clés chargées")
    except FileNotFoundError:
        print(f"❌ Fichier pour {lang} non trouvé")

# Créer le fichier JavaScript
js_content = f"""/* Adobe Firefly Translations */
const adobeFireflyTranslations = {json.dumps(translations_obj, ensure_ascii=False, indent=2)};

// Fonction pour obtenir une traduction
function getFireflyTranslation(key, lang) {{
    if (adobeFireflyTranslations[lang] && adobeFireflyTranslations[lang][key]) {{
        return adobeFireflyTranslations[lang][key];
    }}
    // Fallback à l'anglais
    if (adobeFireflyTranslations.en && adobeFireflyTranslations.en[key]) {{
        return adobeFireflyTranslations.en[key];
    }}
    return null;
}}

// Appliquer les traductions Adobe Firefly
function applyFireflyTranslations(lang) {{
    console.log('🔥 Applying Adobe Firefly translations for:', lang);

    let count = 0;
    document.querySelectorAll('[data-i18n]').forEach(element => {{
        const key = element.getAttribute('data-i18n');

        // Seulement pour les clés Adobe Firefly
        if (key && key.startsWith('review.adobe-firefly.')) {{
            const translation = getFireflyTranslation(key, lang);
            if (translation) {{
                element.textContent = translation;
                count++;
            }}
        }}
    }});

    console.log(`✅ Applied ${{count}} Adobe Firefly translations`);
}}

// Auto-appliquer quand la langue change
window.addEventListener('languageChanged', (e) => {{
    const lang = e.detail.language;
    setTimeout(() => applyFireflyTranslations(lang), 200);
}});

// Appliquer au chargement
if (document.readyState === 'loading') {{
    document.addEventListener('DOMContentLoaded', () => {{
        const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
        applyFireflyTranslations(currentLang);
    }});
}} else {{
    const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
    applyFireflyTranslations(currentLang);
}}

console.log('✅ Adobe Firefly i18n loaded');
"""

# Sauvegarder
with open('GenuisNet.ai/js/adobe-firefly-i18n.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print()
print("=" * 80)
print("✅ Fichier créé: GenuisNet.ai/js/adobe-firefly-i18n.js")
print("=" * 80)
print()
print("Maintenant, ajoutez cette ligne dans adobe-firefly.html APRÈS i18n.js:")
print('<script src="../../../js/adobe-firefly-i18n.js"></script>')
