#!/usr/bin/env python3
"""
Translate Conversica batch3 content to Korean, Arabic, and Hindi.
Uses Claude API for high-quality translations.
"""

import json
import os
from anthropic import Anthropic

# Initialize Anthropic client
client = Anthropic()

def load_json_file(filepath):
    """Load JSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json_file(filepath, data):
    """Save JSON file with proper formatting."""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def translate_batch(texts, target_language, language_name):
    """Translate a batch of texts to target language using Claude."""

    # Create a mapping of keys to texts for easy reference
    items = list(texts.items())

    # Split into chunks for API calls (to avoid token limits)
    chunk_size = 20
    all_translations = {}

    for i in range(0, len(items), chunk_size):
        chunk = items[i:i + chunk_size]

        # Create the prompt
        text_pairs = "\n".join([f"{key}: {text}" for key, text in chunk])

        prompt = f"""Translate the following English content keys and values to {language_name} ({target_language}).
Keep the JSON key format exactly the same. Provide only the translations without any additional commentary.
Format your response as key: translation pairs (one per line).

{text_pairs}"""

        print(f"Translating batch {i//chunk_size + 1} of {(len(items) + chunk_size - 1)//chunk_size} to {language_name}...")

        # Call Claude API
        message = client.messages.create(
            model="claude-opus-4-5-20251101",
            max_tokens=2000,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        # Parse the response
        response_text = message.content[0].text
        lines = response_text.strip().split('\n')

        for line in lines:
            if ': ' in line:
                key, translation = line.split(': ', 1)
                key = key.strip()
                translation = translation.strip()
                # Remove quotes if present
                if translation.startswith('"') and translation.endswith('"'):
                    translation = translation[1:-1]
                if translation.startswith("'") and translation.endswith("'"):
                    translation = translation[1:-1]
                all_translations[key] = translation

    return all_translations

def main():
    # File path
    file_path = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\pages\reviews\business\conversica-batch3.json"

    # Load the current data
    print("Loading JSON file...")
    data = load_json_file(file_path)

    # Get English content (from 'ko' section which currently has English)
    english_content = data.get('ko', {})

    # Prepare to store translations
    translations = {
        'ko': {},  # Korean
        'ar': {},  # Arabic
        'hi': {}   # Hindi
    }

    # Translate to each language
    languages = [
        ('ko', 'Korean'),
        ('ar', 'Arabic'),
        ('hi', 'Hindi')
    ]

    for lang_code, lang_name in languages:
        print(f"\n{'='*60}")
        print(f"Starting translation to {lang_name}...")
        print(f"{'='*60}")

        translations[lang_code] = translate_batch(english_content, lang_code, lang_name)

        print(f"Completed {lang_name} translation: {len(translations[lang_code])} items")

    # Update the data with translations
    data['ko'] = translations['ko']
    data['ar'] = translations['ar']
    data['hi'] = translations['hi']

    # Save the updated file
    print(f"\n{'='*60}")
    print("Saving translated file...")
    save_json_file(file_path, data)
    print(f"Successfully saved to {file_path}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
