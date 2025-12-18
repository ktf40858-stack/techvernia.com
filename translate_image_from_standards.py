#!/usr/bin/env python3
"""
Script pour traduire les clés IMAGE en utilisant les traductions existantes des patterns standards
"""
import json
import os

# Langues disponibles
LANGUAGES = ['ar', 'de', 'es', 'fr', 'hi', 'ja', 'ko', 'pt', 'zh', 'en']

# Image tools
IMAGE_TOOLS = ['adobe-firefly', 'canva-ai', 'clipdrop', 'dall-e-3',
               'ideogram', 'leonardo-ai', 'midjourney', 'stable-diffusion']

# Chatbot tools
CHATBOT_TOOLS = ['chatgpt', 'claude', 'copilot', 'deepseek', 'gemini', 'grok', 'perplexity', 'poe']

def get_pattern(key):
    """Extract pattern without tool name"""
    parts = key.split('.')
    if len(parts) >= 3 and parts[0] == 'review':
        return '.'.join(parts[2:])
    return None

print("="*80)
print(" TRADUCTION DES CLÉS IMAGE DEPUIS LES PATTERNS STANDARDS")
print("="*80)

# Load review content (source en anglais)
with open('review_content_to_translate.json', 'r', encoding='utf-8') as f:
    review_en = json.load(f)

# Load standard patterns
with open('standard_patterns.json', 'r', encoding='utf-8') as f:
    standard_patterns = json.load(f)

print(f"\n📝 Patterns standards: {len(standard_patterns)}")

# Build pattern translation database from all chatbot tools
pattern_translations = {}  # {lang: {pattern: translation}}

for lang in LANGUAGES:
    pattern_translations[lang] = {}

    # Load from chatbot translation files
    for tool in CHATBOT_TOOLS:
        filename = f'{tool}_translations_all_langs.json'
        if not os.path.exists(filename):
            continue

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)

            if lang not in data:
                continue

            # Extract patterns and their translations
            for key, translation in data[lang].items():
                pattern = get_pattern(key)
                if pattern and pattern in standard_patterns:
                    # Store translation if not already stored
                    if pattern not in pattern_translations[lang]:
                        pattern_translations[lang][pattern] = translation

        except Exception as e:
            print(f"   ⚠️  Erreur lecture {filename}: {e}")

    # Also load from writing_content_translations.json
    if os.path.exists('writing_content_translations.json'):
        try:
            with open('writing_content_translations.json', 'r', encoding='utf-8') as f:
                writing_data = json.load(f)

            if lang in writing_data:
                for key, translation in writing_data[lang].items():
                    pattern = get_pattern(key)
                    if pattern and pattern in standard_patterns:
                        if pattern not in pattern_translations[lang]:
                            pattern_translations[lang][pattern] = translation
        except:
            pass

    print(f"   {lang.upper()}: {len(pattern_translations[lang])} patterns traduits")

print(f"\n{'='*80}")
print(" APPLICATION DES TRADUCTIONS AUX OUTILS IMAGE")
print(f"{'='*80}")

# Now translate image keys
stats = {}

for lang in LANGUAGES:
    print(f"\n🌍 Langue: {lang.upper()}")

    # Load existing translations
    all_trans_file = f'all_full_translations_{lang}.json'
    if os.path.exists(all_trans_file):
        with open(all_trans_file, 'r', encoding='utf-8') as f:
            all_translations = json.load(f)
    else:
        all_translations = {}

    added = 0
    already_exists = 0
    no_translation = 0

    # Process each image tool
    for tool in IMAGE_TOOLS:
        prefix = f'review.{tool}.'

        for key, en_value in review_en.items():
            if not key.startswith(prefix):
                continue

            # Skip if already translated
            if key in all_translations:
                already_exists += 1
                continue

            # Get pattern
            pattern = get_pattern(key)

            # Find translation
            if pattern and pattern in pattern_translations[lang]:
                all_translations[key] = pattern_translations[lang][pattern]
                added += 1
            elif lang == 'en':
                # For English, use original
                all_translations[key] = en_value
                added += 1
            else:
                # No translation found, use English
                all_translations[key] = en_value
                no_translation += 1

    # Save updated translations
    with open(all_trans_file, 'w', encoding='utf-8') as f:
        json.dump(all_translations, f, indent=2, ensure_ascii=False)

    stats[lang] = {
        'added': added,
        'exists': already_exists,
        'no_trans': no_translation
    }

    print(f"   ✅ Ajouté: {added}")
    print(f"   ℹ️  Déjà existantes: {already_exists}")
    if no_translation > 0:
        print(f"   ⚠️  Sans traduction (EN utilisé): {no_translation}")

print(f"\n{'='*80}")
print(" RÉSUMÉ FINAL")
print(f"{'='*80}\n")

for lang in LANGUAGES:
    s = stats[lang]
    total = s['added'] + s['no_trans']
    if total > 0:
        coverage = (s['added'] / total * 100) if total > 0 else 0
        status = "✅" if coverage >= 90 else "⚠️"
        print(f"{status} {lang.upper()}: {s['added']}/{total} traduits ({coverage:.1f}%)")

print(f"\n{'='*80}")
print("✅ TRADUCTION TERMINÉE!")
print(f"{'='*80}")
