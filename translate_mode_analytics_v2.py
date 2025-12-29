import json
import subprocess
import sys

# Read the English file
with open('GenuisNet.ai/pages/reviews/analytics/mode-analytics-en.json', 'r', encoding='utf-8') as f:
    en_data = json.load(f)

# Define the 9 languages in 3 batches
batches = {
    "batch1": {
        "es": ("Spanish", "Español"),
        "fr": ("French", "Français"),
        "de": ("German", "Deutsch")
    },
    "batch2": {
        "pt": ("Portuguese", "Português"),
        "ja": ("Japanese", "日本語"),
        "zh": ("Chinese (Simplified)", "简体中文")
    },
    "batch3": {
        "zh-tw": ("Chinese (Traditional)", "繁體中文"),
        "it": ("Italian", "Italiano"),
        "nl": ("Dutch", "Nederlands")
    }
}

def create_curl_command(json_str, languages):
    """Create a curl command for translation via Claude API"""
    lang_names = [lang[0] for lang in languages.values()]
    language_list = ", ".join(lang_names)

    prompt = f"""You are a professional translator. Translate the following JSON file containing English text to {language_list}.

IMPORTANT INSTRUCTIONS:
1. Translate ONLY the values, NOT the keys
2. Keep all JSON structure exactly the same
3. Keep the same indentation and formatting
4. Do NOT add or remove any fields
5. Preserve all special characters and formatting in the values
6. Return valid JSON objects

For each language, create a complete JSON object with the same keys but translated values.

English JSON to translate:
{json_str}

Provide translations in this exact format - return ONLY valid JSON for each language with no other text:

OUTPUT_SEPARATOR_START_SPANISH
{{...complete JSON translation...}}
OUTPUT_SEPARATOR_END_SPANISH

OUTPUT_SEPARATOR_START_FRENCH
{{...complete JSON translation...}}
OUTPUT_SEPARATOR_END_FRENCH

OUTPUT_SEPARATOR_START_GERMAN
{{...complete JSON translation...}}
OUTPUT_SEPARATOR_END_GERMAN
"""

    return prompt

def translate_batch(batch_name, languages_dict):
    """Translate content using subprocess call to curl"""
    json_str = json.dumps(en_data, ensure_ascii=False, indent=2)
    prompt = create_curl_command(json_str, languages_dict)

    print(f"Translating {batch_name}...")

    # Prepare the API request
    import os
    api_key = os.environ.get('ANTHROPIC_API_KEY')

    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)

    # Create curl command for Claude API
    curl_cmd = [
        'curl', '-X', 'POST',
        'https://api.anthropic.com/v1/messages',
        '-H', f'x-api-key: {api_key}',
        '-H', 'anthropic-version: 2023-06-01',
        '-H', 'content-type: application/json',
        '-d', json.dumps({
            "model": "claude-opus-4-5-20251101",
            "max_tokens": 12000,
            "messages": [
                {"role": "user", "content": prompt}
            ]
        })
    ]

    try:
        result = subprocess.run(curl_cmd, capture_output=True, text=True, timeout=60)
        if result.returncode == 0:
            response_json = json.loads(result.stdout)
            response_text = response_json['content'][0]['text']
            return response_text, languages_dict
        else:
            print(f"Error: {result.stderr}")
            return None, None
    except Exception as e:
        print(f"Error during translation: {e}")
        return None, None

def parse_translations(response_text, languages_dict):
    """Parse the API response and extract translations for each language"""
    translations = {}

    # Map language names to file codes
    lang_name_to_code = {
        "Spanish": "es",
        "French": "fr",
        "German": "de",
        "Portuguese": "pt",
        "Japanese": "ja",
        "Chinese (Simplified)": "zh",
        "Chinese (Traditional)": "zh-tw",
        "Italian": "it",
        "Dutch": "nl"
    }

    for code, (lang_name, lang_native) in languages_dict.items():
        marker_start = f"OUTPUT_SEPARATOR_START_{lang_name.upper().replace(' ', '_')}"
        marker_end = f"OUTPUT_SEPARATOR_END_{lang_name.upper().replace(' ', '_')}"

        if marker_start in response_text and marker_end in response_text:
            start = response_text.find(marker_start) + len(marker_start)
            end = response_text.find(marker_end)
            json_str = response_text[start:end].strip()

            try:
                translations[code] = (lang_name, json.loads(json_str))
            except json.JSONDecodeError as e:
                print(f"Error parsing JSON for {lang_name}: {e}")
        else:
            print(f"Warning: Could not find markers for {lang_name}")

    return translations

def save_batch_files(batch_name, translations):
    """Save translations to individual files for each language"""
    for code, (lang_name, data) in translations.items():
        filename = f"GenuisNet.ai/pages/reviews/analytics/mode-analytics-{batch_name}-{code}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Saved: {filename}")

# Process each batch
for batch_name, languages_dict in batches.items():
    response_text, langs = translate_batch(batch_name, languages_dict)
    if response_text:
        translations = parse_translations(response_text, langs)
        save_batch_files(batch_name, translations)
        print(f"Completed {batch_name}\n")
    else:
        print(f"Failed to translate {batch_name}")

print("All translations complete!")
