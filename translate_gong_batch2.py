#!/usr/bin/env python3
"""
Translate Gong batch2 content to Portuguese (PT), Chinese (ZH), and Japanese (JA)
"""

import json
import anthropic

# Read the original file
with open('GenuisNet.ai/pages/reviews/business/gong-batch2.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Extract English content from 'pt' section (which currently contains English)
english_content = data['pt']

# Initialize the Anthropic client
client = anthropic.Anthropic()

def translate_batch(texts, target_language):
    """Translate a batch of texts to the target language using Claude"""

    # Create a prompt for translation
    language_names = {
        'PT': 'Portuguese (PT)',
        'ZH': 'Chinese Simplified (ZH)',
        'JA': 'Japanese (JA)'
    }

    language_name = language_names.get(target_language, target_language)

    # Format texts as a JSON object for translation
    texts_json = json.dumps(texts, ensure_ascii=False, indent=2)

    prompt = f"""Translate the following JSON object to {language_name}.
Keep the same structure and keys. Only translate the values, not the keys.
Maintain technical terms, product names (like Gong, Salesforce, etc.), and acronyms as they are.
Ensure translations are professional and suitable for B2B software review content.

JSON to translate:
{texts_json}

Return ONLY the translated JSON object with the same structure."""

    response = client.messages.create(
        model="claude-opus-4-5-20251101",
        max_tokens=4000,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    # Parse the response
    translated_text = response.content[0].text

    # Extract JSON from response
    try:
        # Try to find JSON in the response
        start_idx = translated_text.find('{')
        end_idx = translated_text.rfind('}') + 1
        if start_idx != -1 and end_idx > start_idx:
            json_str = translated_text[start_idx:end_idx]
            translated = json.loads(json_str)
            return translated
    except json.JSONDecodeError:
        print(f"Error parsing JSON response for {target_language}")
        print("Response:", translated_text[:500])
        return None

    return None

def main():
    print("Starting translation of Gong batch2...")

    # Split into batches of 20 items to avoid token limits
    keys = list(english_content.keys())
    batch_size = 20

    translations = {
        'pt': {},
        'zh': {},
        'ja': {}
    }

    for i in range(0, len(keys), batch_size):
        batch_keys = keys[i:i+batch_size]
        batch_texts = {k: english_content[k] for k in batch_keys}

        print(f"\nProcessing batch {i//batch_size + 1}/{(len(keys)-1)//batch_size + 1}")
        print(f"Keys: {batch_keys[0]} to {batch_keys[-1]}")

        # Translate to Portuguese
        print("  Translating to Portuguese (PT)...")
        pt_result = translate_batch(batch_texts, 'PT')
        if pt_result:
            translations['pt'].update(pt_result)
            print(f"    Translated {len(pt_result)} items")

        # Translate to Chinese
        print("  Translating to Chinese (ZH)...")
        zh_result = translate_batch(batch_texts, 'ZH')
        if zh_result:
            translations['zh'].update(zh_result)
            print(f"    Translated {len(zh_result)} items")

        # Translate to Japanese
        print("  Translating to Japanese (JA)...")
        ja_result = translate_batch(batch_texts, 'JA')
        if ja_result:
            translations['ja'].update(ja_result)
            print(f"    Translated {len(ja_result)} items")

    # Update the data structure
    data['pt'] = translations['pt']
    data['zh'] = translations['zh']
    data['ja'] = translations['ja']

    # Write back to file
    with open('GenuisNet.ai/pages/reviews/business/gong-batch2.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("\nTranslation complete! File updated.")
    print(f"PT: {len(translations['pt'])} translations")
    print(f"ZH: {len(translations['zh'])} translations")
    print(f"JA: {len(translations['ja'])} translations")

if __name__ == "__main__":
    main()
