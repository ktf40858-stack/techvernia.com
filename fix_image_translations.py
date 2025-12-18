#!/usr/bin/env python3
"""
Script pour corriger les traductions IMAGE en copiant les vraies traductions (non anglais)
"""
import json
import os

# Langues disponibles
LANGUAGES = ['ar', 'de', 'es', 'fr', 'hi', 'ja', 'ko', 'pt', 'zh']

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
print(" CORRECTION DES TRADUCTIONS IMAGE")
print("="*80)

# Load review content (source en anglais)
with open('review_content_to_translate.json', 'r', encoding='utf-8') as f:
    review_en = json.load(f)

# For each language, build pattern database from chatbot/writing translations
for lang in LANGUAGES:
    print(f"\n🌍 Langue: {lang.upper()}")

    # Build pattern translation map from all sources
    pattern_map = {}  # {pattern: translated_value}

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
                if pattern and pattern not in pattern_map:
                    # Only store if it's actually translated (not same as English)
                    pattern_map[pattern] = translation

        except Exception as e:
            print(f"   ⚠️  Erreur: {e}")

    # Also load from writing_content_translations.json
    if os.path.exists('writing_content_translations.json'):
        try:
            with open('writing_content_translations.json', 'r', encoding='utf-8') as f:
                writing_data = json.load(f)

            if lang in writing_data:
                for key, translation in writing_data[lang].items():
                    pattern = get_pattern(key)
                    if pattern and pattern not in pattern_map:
                        pattern_map[pattern] = translation
        except:
            pass

    print(f"   📚 Patterns avec traductions: {len(pattern_map)}")

    # Load existing all_full_translations file
    all_trans_file = f'all_full_translations_{lang}.json'
    if not os.path.exists(all_trans_file):
        print(f"   ❌ Fichier {all_trans_file} n'existe pas!")
        continue

    with open(all_trans_file, 'r', encoding='utf-8') as f:
        all_translations = json.load(f)

    # Fix image translations
    fixed = 0
    for tool in IMAGE_TOOLS:
        prefix = f'review.{tool}.'

        for key in all_translations.keys():
            if not key.startswith(prefix):
                continue

            # Get pattern
            pattern = get_pattern(key)
            if not pattern:
                continue

            # Get current value
            current_value = all_translations[key]

            # Get English value for comparison
            en_value = review_en.get(key, "")

            # If current value is same as English, it needs translation
            if pattern in pattern_map:
                new_value = pattern_map[pattern]

                # Only update if different from current
                if new_value != current_value:
                    all_translations[key] = new_value
                    fixed += 1

    # Save updated translations
    with open(all_trans_file, 'w', encoding='utf-8') as f:
        json.dump(all_translations, f, indent=2, ensure_ascii=False)

    print(f"   ✅ Corrigé: {fixed} traductions")

print(f"\n{'='*80}")
print("✅ CORRECTION TERMINÉE!")
print(f"{'='*80}")
