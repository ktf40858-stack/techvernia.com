#!/usr/bin/env python3
"""
Remplacer proprement les traductions Adobe Firefly dans i18n.js
"""
import json
import re

print("🚀 Remplacement propre des traductions Adobe Firefly...")
print()

# Langues
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

# Charger toutes les traductions
all_translations = {}
for lang_code in languages_map.keys():
    try:
        with open(f'all_full_translations_{lang_code}.json', 'r', encoding='utf-8') as f:
            translations = json.load(f)

        # Filtrer seulement les clés Adobe Firefly
        firefly_translations = {k: v for k, v in translations.items() if k.startswith('review.adobe-firefly.')}
        all_translations[lang_code] = firefly_translations
        print(f"✓ {lang_code.upper()}: {len(firefly_translations)} traductions chargées")
    except FileNotFoundError:
        print(f"❌ Fichier all_full_translations_{lang_code}.json non trouvé")
        continue

print()

# Charger i18n.js
with open('GenuisNet.ai/js/i18n.js', 'r', encoding='utf-8') as f:
    content = f.read()

def escape_for_js(text):
    """Échapper une chaîne pour JavaScript - VERSION SÉCURISÉE"""
    # Remplacer backslash en premier
    text = text.replace('\\', '\\\\')
    # Remplacer les guillemets doubles
    text = text.replace('"', '\\"')
    # Remplacer newlines
    text = text.replace('\n', '\\n')
    text = text.replace('\r', '\\r')
    text = text.replace('\t', '\\t')
    return text

# Pour chaque langue, remplacer les traductions
total_replacements = 0

for lang_code, lang_name in languages_map.items():
    if lang_code not in all_translations:
        continue

    print(f"Traitement {lang_name}...")

    # Trouver la section de la langue
    # Format: es: { ... },
    section_pattern = rf'(// ====================\s+{lang_name}\s+====================\s+{lang_code}:\s+{{)(.*?)(^\s+}},)'

    section_match = re.search(section_pattern, content, re.MULTILINE | re.DOTALL)

    if not section_match:
        print(f"  ⚠️  Section {lang_name} non trouvée")
        continue

    section_content = section_match.group(2)
    replacements = 0

    # Pour chaque clé Adobe Firefly
    for key, new_value in all_translations[lang_code].items():
        # Échapper la clé pour regex
        escaped_key = re.escape(key)

        # Échapper la nouvelle valeur pour JavaScript
        escaped_value = escape_for_js(new_value)

        # Pattern pour trouver la clé avec sa valeur actuelle
        # Gère les valeurs multi-lignes et les caractères échappés
        key_pattern = rf'("{escaped_key}":\s*")([^"\\]*(\\.[^"\\]*)*)"'

        # Vérifier si la clé existe dans cette section
        if re.search(key_pattern, section_content):
            # Remplacer
            section_content = re.sub(
                key_pattern,
                rf'\1{escaped_value}"',
                section_content
            )
            replacements += 1

    # Remplacer la section dans le contenu complet
    if replacements > 0:
        new_section = section_match.group(1) + section_content + section_match.group(3)
        content = content[:section_match.start()] + new_section + content[section_match.end():]
        print(f"  ✓ {lang_name}: {replacements} traductions remplacées")
        total_replacements += replacements
    else:
        print(f"  ⚠️  {lang_name}: Aucune traduction remplacée")

# Sauvegarder
with open('GenuisNet.ai/js/i18n.js', 'w', encoding='utf-8') as f:
    f.write(content)

print()
print("=" * 80)
print(f"✅ REMPLACEMENT TERMINÉ!")
print(f"📊 {total_replacements} traductions remplacées")
print("=" * 80)
