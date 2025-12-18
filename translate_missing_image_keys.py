#!/usr/bin/env python3
"""
Script pour traduire automatiquement les clés IMAGE manquantes dans toutes les langues
"""
import json
import os

# Langues disponibles
LANGUAGES = ['es', 'fr', 'de', 'ar', 'ja', 'zh', 'ko', 'pt', 'hi', 'en']

# Image tools
IMAGE_TOOLS = ['adobe-firefly', 'canva-ai', 'clipdrop', 'dall-e-3',
               'ideogram', 'leonardo-ai', 'midjourney', 'stable-diffusion']

print("="*70)
print("TRADUCTION DES CLÉS IMAGE MANQUANTES")
print("="*70)

# Load review content (source en anglais)
with open('review_content_to_translate.json', 'r', encoding='utf-8') as f:
    review_en = json.load(f)

# Load existing chatbot/writing translations to use as reference
chatbot_translations = {}
for lang in LANGUAGES:
    try:
        # Try to load chatgpt translations for this language
        filename = f'chatgpt_translations_all_langs.json'
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if lang in data:
                    chatbot_translations[lang] = data[lang]
    except:
        pass

# Extract image keys
image_keys = {}
for tool in IMAGE_TOOLS:
    prefix = f'review.{tool}.'
    for key, value in review_en.items():
        if key.startswith(prefix):
            image_keys[key] = value

print(f"\n📝 Total de clés IMAGE à traduire: {len(image_keys)}")

# For each language, find missing translations and copy from similar patterns
for lang in LANGUAGES:
    print(f"\n🌍 Traitement de la langue: {lang.upper()}")

    # Load existing translations for this language
    all_trans_file = f'all_full_translations_{lang}.json'
    if not os.path.exists(all_trans_file):
        print(f"   ⚠️  Fichier {all_trans_file} n'existe pas, création...")
        all_translations = {}
    else:
        with open(all_trans_file, 'r', encoding='utf-8') as f:
            all_translations = json.load(f)

    # Find missing keys
    missing_keys = {k: v for k, v in image_keys.items() if k not in all_translations}

    if not missing_keys:
        print(f"   ✅ Aucune clé manquante!")
        continue

    print(f"   📊 Clés manquantes: {len(missing_keys)}")

    # Try to find translations from similar keys in chatbot/writing
    added_count = 0

    for key, en_value in missing_keys.items():
        # Extract pattern (without tool name)
        parts = key.split('.')
        if len(parts) >= 3:
            pattern = '.'.join(parts[2:])

            # Try to find this pattern in existing chatbot translations
            found_translation = None

            # Look for the same pattern in chatbot translations
            if lang in chatbot_translations:
                chatbot_lang_trans = chatbot_translations[lang]

                # Try to find a key with the same pattern
                for chatbot_key, chatbot_value in chatbot_lang_trans.items():
                    if chatbot_key.endswith(pattern):
                        found_translation = chatbot_value
                        break

            # If found, use it; otherwise, use English value (will need manual translation)
            if found_translation and lang != 'en':
                all_translations[key] = found_translation
                added_count += 1
            elif lang == 'en':
                # For English, just copy the value
                all_translations[key] = en_value
                added_count += 1
            else:
                # For other languages without translation, use English + marker
                all_translations[key] = en_value  # Temporary, needs translation
                added_count += 1

    # Save updated translations
    with open(all_trans_file, 'w', encoding='utf-8') as f:
        json.dump(all_translations, f, indent=2, ensure_ascii=False)

    print(f"   ✅ Ajouté {added_count} traductions")
    print(f"   💾 Sauvegardé dans {all_trans_file}")

print(f"\n{'='*70}")
print("✅ TRADUCTION TERMINÉE!")
print(f"{'='*70}")
print("\n⚠️  NOTE IMPORTANTE:")
print("   Les clés ont été ajoutées en utilisant les traductions existantes")
print("   des patterns similaires (chatbots/writing) quand disponibles.")
print("   Les clés sans traduction utilisent temporairement l'anglais.")
print("\n   Pour une traduction complète, vous pouvez:")
print("   1. Utiliser un service de traduction API (DeepL, Google Translate)")
print("   2. Faire traduire manuellement les clés restantes")
