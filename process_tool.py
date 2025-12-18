#!/usr/bin/env python3
"""
Script générique pour traiter un outil: extraction, traduction, injection
"""
import json
import re
import sys
import time
from bs4 import BeautifulSoup
import argostranslate.translate
from tqdm import tqdm

if len(sys.argv) != 2:
    print("Usage: python3 process_tool.py <tool_name>")
    print("Example: python3 process_tool.py deepseek")
    sys.exit(1)

tool_name = sys.argv[1].lower()

print(f"\n{'='*60}")
print(f"🚀 TRAITEMENT DE {tool_name.upper()}")
print(f"{'='*60}\n")

# ========== 1. EXTRACTION ==========
print(f"📝 ÉTAPE 1/3: Extraction des clés de {tool_name}.html...")

html_file = f'GenuisNet.ai/pages/reviews/chatbots/{tool_name}.html'

with open(html_file, 'r', encoding='utf-8') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')
elements = soup.find_all(attrs={'data-i18n': True})

translations = {}
for element in elements:
    key = element.get('data-i18n')
    text = element.get_text(strip=True)
    text = re.sub(r'\s+', ' ', text)
    if key and text:
        translations[key] = text

output_file = f'{tool_name}_content_to_translate.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(translations, f, indent=2, ensure_ascii=False)

num_keys = len(translations)
total_translations = num_keys * 9

print(f"✅ {num_keys} clés extraites → {total_translations} traductions à générer\n")

# ========== 2. TRADUCTION ==========
print(f"🌍 ÉTAPE 2/3: Traduction de {num_keys} clés en 9 langues...")

languages = {
    'es': 'Espagnol',
    'fr': 'Français',
    'de': 'Allemand',
    'pt': 'Portugais',
    'zh': 'Chinois',
    'ja': 'Japonais',
    'ko': 'Coréen',
    'ar': 'Arabe',
    'hi': 'Hindi'
}

all_results = {}
start_time = time.time()

for lang_code, lang_name in languages.items():
    print(f"\n  🌍 {lang_name} ({lang_code})...")
    translated = {}

    for key, text in tqdm(translations.items(), desc=lang_code.upper(), unit='clé'):
        try:
            translation = argostranslate.translate.translate(text, 'en', lang_code)
            translated[key] = translation
        except Exception as e:
            print(f"\n  ⚠️  Erreur pour {key}: {e}")
            translated[key] = text

    all_results[lang_code] = translated
    print(f"     ✅ {len(translated)} clés traduites")

elapsed_time = time.time() - start_time
minutes = int(elapsed_time // 60)
seconds = int(elapsed_time % 60)

translations_file = f'{tool_name}_translations_all_langs.json'
with open(translations_file, 'w', encoding='utf-8') as f:
    json.dump(all_results, f, indent=2, ensure_ascii=False)

print(f"\n✅ Traduction terminée en {minutes}.{seconds//6} minutes\n")

# ========== 3. INJECTION ==========
print(f"💉 ÉTAPE 3/3: Injection dans i18n.js...")

with open('GenuisNet.ai/js/i18n.js', 'r', encoding='utf-8') as f:
    i18n_content = f.read()

def escape_js_string(s):
    s = s.replace('\\', '\\\\')
    s = s.replace('"', '\\"')
    s = s.replace("'", "\\'")
    s = s.replace('\n', '\\n')
    s = s.replace('\r', '\\r')
    s = s.replace('\t', '\\t')
    return s

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
tool_name_capitalized = tool_name.capitalize()

for lang_code, lang_name in languages_map.items():
    pattern = rf'(// ====================\s*{lang_name}\s*====================\s*\n\s*{lang_code}:\s*\{{)'
    match = re.search(pattern, i18n_content)

    if not match:
        print(f"  ⚠️  Section {lang_name} non trouvée")
        continue

    insert_pos = match.end()

    translation_lines = []
    translation_lines.append(f"\n        // ===== {tool_name_capitalized} Review Translations =====")

    for key, value in all_results[lang_code].items():
        escaped_value = escape_js_string(value)
        translation_lines.append(f'        "{key}": "{escaped_value}",')

    translation_lines.append(f"        // ===== End {tool_name_capitalized} Review Translations =====\n")

    translations_block = '\n'.join(translation_lines)
    i18n_content = i18n_content[:insert_pos] + translations_block + i18n_content[insert_pos:]
    modifications_count += len(all_results[lang_code])

with open('GenuisNet.ai/js/i18n.js', 'w', encoding='utf-8') as f:
    f.write(i18n_content)

print(f"✅ {modifications_count} traductions injectées\n")

# ========== RÉSUMÉ ==========
print(f"{'='*60}")
print(f"✅ {tool_name.upper()} TERMINÉ!")
print(f"📊 {num_keys} clés → {total_translations} traductions")
print(f"⏱️  Temps total: {minutes}.{seconds//6} minutes")
print(f"{'='*60}\n")
