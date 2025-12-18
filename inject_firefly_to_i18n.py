#!/usr/bin/env python3
"""
Script pour injecter les traductions Adobe Firefly dans i18n.js
"""
import json
import re

print("🚀 Injection des traductions Adobe Firefly dans i18n.js...")
print()

# Charger les traductions pour chaque langue
languages_map = {
    'es': 'SPANISH',
    'fr': 'FRENCH',
    'de': 'GERMAN',
    'pt': 'PORTUGUESE',
    'zh': 'CHINESE',
    'ja': 'JAPANESE',
    'ko': 'KOREAN',
    'ar': 'ARABIC',
    'hi': 'HINDI'
}

# Charger les clés à traduire
with open('image_content_keys_to_translate.json', 'r', encoding='utf-8') as f:
    en_keys = json.load(f)

# Charger toutes les traductions
all_translations = {}
for lang_code in languages_map.keys():
    with open(f'all_full_translations_{lang_code}.json', 'r', encoding='utf-8') as f:
        translations = json.load(f)

    # Filtrer pour ne garder que les clés Adobe Firefly
    firefly_translations = {}
    for key in en_keys.keys():
        if key in translations:
            firefly_translations[key] = translations[key]

    all_translations[lang_code] = firefly_translations
    print(f"✓ {lang_code.upper()}: {len(firefly_translations)} traductions chargées")

print()

# Charger i18n.js
with open('GenuisNet.ai/js/i18n.js', 'r', encoding='utf-8') as f:
    i18n_content = f.read()

def escape_js_string(s):
    """Échapper les caractères spéciaux pour JavaScript"""
    s = s.replace('\\', '\\\\')
    s = s.replace('"', '\\"')
    s = s.replace("'", "\\'")
    s = s.replace('\n', '\\n')
    s = s.replace('\r', '\\r')
    s = s.replace('\t', '\\t')
    return s

# Pour chaque langue, injecter les traductions
modifications_count = 0

for lang_code, lang_name in languages_map.items():
    # Trouver la section de la langue dans i18n.js
    pattern = rf'(// ====================\s*{lang_name}\s*====================\s*\n\s*{lang_code}:\s*\{{)'
    match = re.search(pattern, i18n_content)

    if not match:
        print(f"  ⚠️  Section {lang_name} non trouvée")
        continue

    insert_pos = match.end()

    # Vérifier si les traductions Adobe Firefly existent déjà
    firefly_marker = f"// ===== Adobe Firefly Review Translations ====="
    if firefly_marker in i18n_content:
        # Supprimer l'ancien bloc
        start_marker = f"// ===== Adobe Firefly Review Translations ====="
        end_marker = f"// ===== End Adobe Firefly Review Translations ====="

        # Trouver tous les blocs Adobe Firefly
        pattern_old = rf'\n\s*{re.escape(start_marker)}.*?{re.escape(end_marker)}\n'
        i18n_content = re.sub(pattern_old, '', i18n_content, flags=re.DOTALL)

        # Re-trouver la position d'insertion après suppression
        match = re.search(rf'(// ====================\s*{lang_name}\s*====================\s*\n\s*{lang_code}:\s*\{{)', i18n_content)
        if match:
            insert_pos = match.end()

    # Créer le bloc de traductions
    translation_lines = []
    translation_lines.append(f"\n        // ===== Adobe Firefly Review Translations =====")

    for key, value in all_translations[lang_code].items():
        escaped_value = escape_js_string(value)
        translation_lines.append(f'        "{key}": "{escaped_value}",')

    translation_lines.append(f"        // ===== End Adobe Firefly Review Translations =====\n")

    translations_block = '\n'.join(translation_lines)
    i18n_content = i18n_content[:insert_pos] + translations_block + i18n_content[insert_pos:]
    modifications_count += len(all_translations[lang_code])

    print(f"✓ {lang_name}: {len(all_translations[lang_code])} traductions injectées")

# Sauvegarder i18n.js
with open('GenuisNet.ai/js/i18n.js', 'w', encoding='utf-8') as f:
    f.write(i18n_content)

print()
print("=" * 80)
print(f"✅ INJECTION TERMINÉE!")
print(f"📊 {modifications_count} traductions injectées dans i18n.js")
print("=" * 80)
print()
print("Les traductions Adobe Firefly sont maintenant disponibles sur la page web!")
