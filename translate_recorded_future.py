import json
import os
import sys

# Add the parent directory to the path to import anthropic
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from anthropic import Anthropic

def translate_json_to_language(json_data, target_language_code, target_language_name):
    """Translate all English values in the JSON to the target language."""

    client = Anthropic()
    conversation_history = []

    # Extract all English key-value pairs
    en_data = json_data.get("en", {})
    translation_pairs = list(en_data.items())

    # Process in batches to avoid token limits
    batch_size = 30
    translated_data = {}

    print(f"\nTranslating to {target_language_name} ({target_language_code})...")

    for batch_start in range(0, len(translation_pairs), batch_size):
        batch_end = min(batch_start + batch_size, len(translation_pairs))
        batch_items = translation_pairs[batch_start:batch_end]

        # Create a prompt for this batch
        batch_dict = {key: value for key, value in batch_items}

        prompt = f"""You are a professional translator. Translate the following English text to {target_language_name} ({target_language_code}).

IMPORTANT RULES:
1. Keep the JSON key names exactly the same
2. Only translate the values (the English text)
3. Preserve HTML entities like &amp; as-is
4. Return ONLY valid JSON with no additional text or explanation
5. Maintain the same structure
6. Be consistent with terminology across all translations

English text to translate:
{json.dumps(batch_dict, ensure_ascii=False, indent=2)}

Provide the translation as a JSON object with the same keys but translated values."""

        conversation_history.append({
            "role": "user",
            "content": prompt
        })

        response = client.messages.create(
            model="claude-opus-4.5-20251101",
            max_tokens=4000,
            messages=conversation_history
        )

        assistant_message = response.content[0].text
        conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })

        # Parse the response
        try:
            # Clean up the response - remove markdown code blocks if present
            cleaned_response = assistant_message
            if "```json" in cleaned_response:
                cleaned_response = cleaned_response.split("```json")[1].split("```")[0]
            elif "```" in cleaned_response:
                cleaned_response = cleaned_response.split("```")[1].split("```")[0]

            batch_translation = json.loads(cleaned_response)
            translated_data.update(batch_translation)
            print(f"  Batch {batch_start//batch_size + 1} done ({len(translated_data)} items)")
        except json.JSONDecodeError as e:
            print(f"Error parsing translation batch {batch_start//batch_size + 1}: {e}")
            print(f"Response: {assistant_message[:500]}")
            return None

    return translated_data

def main():
    input_file = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\pages\reviews\cybersecurity\recorded-future-batch3.json"

    # Read the original JSON
    with open(input_file, 'r', encoding='utf-8') as f:
        original_data = json.load(f)

    # Create output structure
    output_data = original_data.copy()

    # Languages to translate to
    languages = [
        ("ko", "Korean"),
        ("ar", "Arabic"),
        ("hi", "Hindi")
    ]

    # Translate to each language
    for lang_code, lang_name in languages:
        translated_values = translate_json_to_language(original_data, lang_code, lang_name)

        if translated_values:
            output_data[lang_code] = translated_values
        else:
            print(f"Failed to translate to {lang_name}")
            return

    # Save the updated JSON
    with open(input_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"\nTranslation complete! Updated file saved to:")
    print(input_file)
    print(f"\nLanguages added: Korean (ko), Arabic (ar), Hindi (hi)")

if __name__ == "__main__":
    main()
