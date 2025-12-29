import json
import anthropic

# Read the English file
with open('GenuisNet.ai/pages/reviews/analytics/mode-analytics-en.json', 'r', encoding='utf-8') as f:
    en_data = json.load(f)

# Define the 9 languages in 3 batches
batches = {
    "batch1": ["Spanish", "French", "German"],
    "batch2": ["Portuguese", "Japanese", "Chinese (Simplified)"],
    "batch3": ["Chinese (Traditional)", "Italian", "Dutch"]
}

# Language codes for file naming
lang_codes = {
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

def translate_batch(batch_name, languages):
    """Translate content to multiple languages in one batch"""
    client = anthropic.Anthropic()

    # Create translation prompt
    json_str = json.dumps(en_data, ensure_ascii=False, indent=2)

    # Create a prompt that translates to all languages in the batch
    language_list = ", ".join(languages)

    prompt = f"""You are a professional translator. Translate the following JSON file containing English text to {language_list}.

IMPORTANT INSTRUCTIONS:
1. Translate ONLY the values, NOT the keys
2. Keep all JSON structure exactly the same
3. Keep the same indentation and formatting
4. Do NOT add or remove any fields
5. Preserve all special characters and formatting in the values
6. Return a valid JSON object

For each language, create a complete JSON object with the same keys but translated values.

Return the translations as follows:
- For each language, on a new line write: [LANGUAGE_NAME]
- Then provide the complete JSON translation for that language
- Repeat for each language in the batch

English JSON to translate:
{json_str}

Translate to: {language_list}

Format your response exactly as:
[Spanish]
{{...json...}}

[French]
{{...json...}}

[German]
{{...json...}}
"""

    print(f"Translating {batch_name}...")

    message = client.messages.create(
        model="claude-opus-4-5-20251101",
        max_tokens=12000,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    response_text = message.content[0].text
    return response_text, languages

def parse_translations(response_text, languages):
    """Parse the API response and extract translations for each language"""
    translations = {}

    for lang in languages:
        # Find the section for this language
        marker = f"[{lang}]"
        if marker in response_text:
            start = response_text.find(marker) + len(marker)
            # Find the next language marker or end of string
            next_marker_pos = len(response_text)
            for other_lang in languages:
                if other_lang != lang:
                    other_marker = f"[{other_lang}]"
                    pos = response_text.find(other_marker, start)
                    if pos != -1 and pos < next_marker_pos:
                        next_marker_pos = pos

            json_str = response_text[start:next_marker_pos].strip()
            # Remove markdown code blocks if present
            if json_str.startswith("```"):
                json_str = json_str[json_str.find('\n')+1:]
            if json_str.endswith("```"):
                json_str = json_str[:json_str.rfind('```')]

            try:
                translations[lang] = json.loads(json_str.strip())
            except json.JSONDecodeError as e:
                print(f"Error parsing JSON for {lang}: {e}")
                print(f"JSON string: {json_str[:200]}")

    return translations

def save_batch_files(batch_name, translations, lang_codes):
    """Save translations to individual files for each language"""
    for lang, data in translations.items():
        code = lang_codes[lang]
        filename = f"GenuisNet.ai/pages/reviews/analytics/mode-analytics-{batch_name}-{code}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Saved: {filename}")

# Process each batch
for batch_name, languages in batches.items():
    response_text, langs = translate_batch(batch_name, languages)
    translations = parse_translations(response_text, langs)
    save_batch_files(batch_name, translations, lang_codes)
    print(f"Completed {batch_name}\n")

print("All translations complete!")
