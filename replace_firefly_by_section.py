#!/usr/bin/env python3
"""
Script pour remplacer les traductions Adobe Firefly par section de langue
"""
import json
import re

print("🚀 Remplacement des traductions Adobe Firefly par section...")
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

# Charger les traductions
all_translations = {}
for lang_code in languages_map.keys():
    with open(f'all_full_translations_{lang_code}.json', 'r', encoding='utf-8') as f:
        translations = json.load(f)
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

# Diviser le fichier par sections de langue
# Format: // ==================== LANGUAGE_NAME ====================
sections = {}
current_lang = None
current_content = []

for line in i18n_content.split('\n'):
    # Détecter le début d'une nouvelle section de langue
    lang_match = re.search(r'// ====================\s+(\w+)\s+====================', line)

    if lang_match:
        # Sauvegarder la section précédente
        if current_lang:
            sections[current_lang] = '\n'.join(current_content)

        # Commencer une nouvelle section
        current_lang = lang_match.group(1)
        current_content = [line]
    else:
        current_content.append(line)

# Sauvegarder la dernière section
if current_lang:
    sections[current_lang] = '\n'.join(current_content)

print("Sections trouvées:", list(sections.keys()))
print()

# Pour chaque langue, remplacer dans SA section seulement
total_replacements = 0

for lang_code, lang_name in languages_map.items():
    if lang_name not in sections:
        print(f"⚠️  Section {lang_name} non trouvée")
        continue

    section_content = sections[lang_name]
    replacements = 0

    # Remplacer chaque clé dans cette section
    for key, new_value in all_translations[lang_code].items():
        escaped_key = re.escape(key)
        escaped_value = escape_js_string(new_value)

        # Pattern pour trouver la clé
        pattern = rf'("{escaped_key}":\s*")([^"]*(?:\\.[^"]*)*)"'

        # Compter et remplacer
        matches = re.findall(pattern, section_content)
        if matches:
            section_content = re.sub(pattern, lambda m: f'{m.group(1)}{escaped_value}"', section_content)
            replacements += len(matches)

    # Mettre à jour la section
    sections[lang_name] = section_content
    total_replacements += replacements
    print(f"✓ {lang_name}: {replacements} traductions remplacées")

# Reconstruire le fichier
reconstructed = []
for lang_name in sections.keys():
    reconstructed.append(sections[lang_name])

final_content = '\n'.join(reconstructed)

# Sauvegarder
with open('GenuisNet.ai/js/i18n.js', 'w', encoding='utf-8') as f:
    f.write(final_content)

print()
print("=" * 80)
print(f"✅ REMPLACEMENT TERMINÉ!")
print(f"📊 {total_replacements} traductions remplacées")
print("=" * 80)
