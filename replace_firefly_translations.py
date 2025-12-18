#!/usr/bin/env python3
"""
Script pour remplacer les traductions Adobe Firefly existantes dans i18n.js
"""
import json
import re

print("🚀 Remplacement des traductions Adobe Firefly dans i18n.js...")
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

# Charger les clés traduites
all_translations = {}
for lang_code in languages_map.keys():
    with open(f'all_full_translations_{lang_code}.json', 'r', encoding='utf-8') as f:
        translations = json.load(f)

    # Filtrer pour ne garder que les clés Adobe Firefly
    firefly_translations = {k: v for k, v in translations.items() if k.startswith('review.adobe-firefly.')}
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
    s = s.replace('\n', '\\n')
    s = s.replace('\r', '\\r')
    s = s.replace('\t', '\\t')
    return s

def unescape_js_string(s):
    """Dés-échapper une chaîne JavaScript"""
    s = s.replace('\\n', '\n')
    s = s.replace('\\r', '\r')
    s = s.replace('\\t', '\t')
    s = s.replace('\\"', '"')
    s = s.replace('\\\\', '\\')
    return s

# Pour chaque langue, remplacer les traductions
replacements_count = 0

for lang_code, lang_name in languages_map.items():
    print(f"Traitement {lang_name}...")

    # Pour chaque clé Adobe Firefly, chercher et remplacer
    for key, new_value in all_translations[lang_code].items():
        # Échapper les caractères spéciaux pour la regex
        escaped_key = re.escape(key)

        # Pattern pour trouver la clé avec n'importe quelle valeur
        # Format: "key": "valeur",
        pattern = rf'("{escaped_key}":\s*")([^"]*(?:\\.[^"]*)*)"'

        # Échapper la nouvelle valeur pour JavaScript
        escaped_value = escape_js_string(new_value)

        # Fonction de remplacement qui garde la clé et remplace seulement la valeur
        def replacer(match):
            return f'{match.group(1)}{escaped_value}"'

        # Remplacer dans tout le fichier
        new_content = re.sub(pattern, replacer, i18n_content)

        if new_content != i18n_content:
            replacements_count += 1
            i18n_content = new_content

    print(f"  ✓ {lang_name}: traductions remplacées")

# Sauvegarder i18n.js
with open('GenuisNet.ai/js/i18n.js', 'w', encoding='utf-8') as f:
    f.write(i18n_content)

print()
print("=" * 80)
print(f"✅ REMPLACEMENT TERMINÉ!")
print(f"📊 {replacements_count} traductions remplacées dans i18n.js")
print("=" * 80)
print()
print("Les traductions Adobe Firefly sont maintenant actives!")
