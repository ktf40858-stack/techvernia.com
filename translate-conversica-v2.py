#!/usr/bin/env python3
"""
Translate Conversica batch3 content to Korean, Arabic, and Hindi.
Uses Claude API for high-quality translations via HTTP requests.
"""

import json
import os
import requests
import time

def load_json_file(filepath):
    """Load JSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json_file(filepath, data):
    """Save JSON file with proper formatting."""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def translate_batch(texts, target_language, language_name):
    """Translate a batch of texts to target language using Claude API."""

    # Get API key from environment
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY environment variable not set")

    # Create a mapping of keys to texts
    items = list(texts.items())

    # Split into chunks for API calls
    chunk_size = 15
    all_translations = {}

    for i in range(0, len(items), chunk_size):
        chunk = items[i:i + chunk_size]
        chunk_num = i // chunk_size + 1
        total_chunks = (len(items) + chunk_size - 1) // chunk_size

        # Create the prompt
        text_pairs = "\n".join([f"{key}: {text}" for key, text in chunk])

        prompt = f"""Translate the following English content keys and values to {language_name} ({target_language}).
Keep the JSON key format exactly the same. Provide only the translations without any additional commentary.
Format your response as key: translation pairs (one per line).

{text_pairs}"""

        print(f"Translating batch {chunk_num}/{total_chunks} to {language_name}...")

        # Call Claude API
        headers = {
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        }

        body = {
            "model": "claude-opus-4-5-20251101",
            "max_tokens": 2000,
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers=headers,
            json=body,
            timeout=30
        )

        if response.status_code != 200:
            print(f"API Error: {response.status_code}")
            print(response.text)
            raise Exception(f"Translation API failed: {response.text}")

        # Parse the response
        response_data = response.json()
        response_text = response_data['content'][0]['text']
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

        # Rate limiting
        if chunk_num < total_chunks:
            time.sleep(1)

    return all_translations

def main():
    # File path
    file_path = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\pages\reviews\business\conversica-batch3.json"

    # Load the current data
    print("Loading JSON file...")
    data = load_json_file(file_path)

    # Get English content (from 'ko' section which currently has English)
    english_content = data.get('ko', {})
    print(f"Found {len(english_content)} content keys to translate")

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
