#!/usr/bin/env python3
"""
Script d'injection des traductions Copilot dans i18n.js
"""
import json
import re

print("🚀 Injection des traductions Copilot dans i18n.js...")

# 1. Charger les traductions Copilot
print("\n📖 Chargement des traductions Copilot...")
with open('copilot_translations_all_langs.json', 'r', encoding='utf-8') as f:
    copilot_translations = json.load(f)

# 2. Lire le fichier i18n.js
print("📖 Lecture de i18n.js...")
with open('GenuisNet.ai/js/i18n.js', 'r', encoding='utf-8') as f:
    i18n_content = f.read()

# 3. Fonction pour échapper les caractères spéciaux dans les valeurs JSON pour JavaScript
def escape_js_string(s):
    """Échappe les caractères spéciaux pour JavaScript"""
    s = s.replace('\\', '\\\\')  # Backslash
    s = s.replace('"', '\\"')     # Guillemets doubles
    s = s.replace("'", "\\'")     # Guillemets simples
    s = s.replace('\n', '\\n')    # Retour à la ligne
    s = s.replace('\r', '\\r')    # Retour chariot
    s = s.replace('\t', '\\t')    # Tabulation
    return s

# 4. Pour chaque langue, ajouter les traductions Copilot
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

modifications_count = 0

for lang_code, lang_name in languages_map.items():
    print(f"\n🌍 Injection {lang_name} ({lang_code})...")

    if lang_code not in copilot_translations:
        print(f"  ⚠️  Langue {lang_code} non trouvée dans les traductions")
        continue

    # Trouver la section de la langue dans i18n.js
    pattern = rf'(// ====================\s*{lang_name}\s*====================\s*\n\s*{lang_code}:\s*\{{)'

    match = re.search(pattern, i18n_content)

    if not match:
        print(f"  ⚠️  Section {lang_name} non trouvée dans i18n.js")
        continue

    # Position d'insertion (juste après "es: {")
    insert_pos = match.end()

    # Générer les lignes de traduction Copilot
    translation_lines = []
    translation_lines.append("\n        // ===== Copilot Review Translations =====")

    for key, value in copilot_translations[lang_code].items():
        escaped_value = escape_js_string(value)
        translation_lines.append(f'        "{key}": "{escaped_value}",')

    translation_lines.append("        // ===== End Copilot Review Translations =====\n")

    translations_block = '\n'.join(translation_lines)

    # Insérer les traductions
    i18n_content = i18n_content[:insert_pos] + translations_block + i18n_content[insert_pos:]
    modifications_count += len(copilot_translations[lang_code])

    print(f"  ✅ {len(copilot_translations[lang_code])} clés injectées")

# 5. Sauvegarder le fichier i18n.js modifié
print(f"\n💾 Sauvegarde de i18n.js avec {modifications_count} nouvelles traductions...")
with open('GenuisNet.ai/js/i18n.js', 'w', encoding='utf-8') as f:
    f.write(i18n_content)

print("\n" + "="*60)
print("✅ INJECTION COPILOT TERMINÉE!")
print(f"📊 {modifications_count} traductions Copilot ajoutées dans i18n.js")
print("="*60)
