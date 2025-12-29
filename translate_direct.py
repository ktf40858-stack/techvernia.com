#!/usr/bin/env python3
import json
import requests
import os

# Read the English file
with open('GenuisNet.ai/pages/reviews/analytics/mode-analytics-en.json', 'r', encoding='utf-8') as f:
    en_data = json.load(f)

# Define batches with language info
batches = {
    "batch1": {
        "es": "Spanish",
        "fr": "French",
        "de": "German"
    },
    "batch2": {
        "pt": "Portuguese",
        "ja": "Japanese",
        "zh": "Chinese (Simplified)"
    },
    "batch3": {
        "zh-tw": "Chinese (Traditional)",
        "it": "Italian",
        "nl": "Dutch"
    }
}

def translate_batch(batch_name, languages_dict):
    """Translate content to specified languages"""
    json_str = json.dumps(en_data, ensure_ascii=False, indent=2)
    lang_names = list(languages_dict.values())
    language_list = ", ".join(lang_names)

    prompt = f"""You are a professional translator. Translate the following JSON values to {language_list}.

CRITICAL INSTRUCTIONS:
1. Translate ONLY the values, NEVER the keys
2. Keep ALL JSON structure identical
3. Keep same indentation and formatting
4. Do NOT add or remove any fields
5. Return ONLY valid JSON

Return output in this exact format with JUST the JSON (no markdown, no explanation):

---SPANISH---
{{"key1": "spanish translation", ...}}

---FRENCH---
{{"key1": "french translation", ...}}

---GERMAN---
{{"key1": "german translation", ...}}

English JSON:
{json_str}

Translate now:"""

    print(f"Translating {batch_name}: {', '.join(lang_names)}")

    try:
        response = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "x-api-key": os.environ.get("ANTHROPIC_API_KEY", ""),
                "anthropic-version": "2023-06-01",
                "content-type": "application/json"
            },
            json={
                "model": "claude-opus-4-5-20251101",
                "max_tokens": 15000,
                "messages": [{"role": "user", "content": prompt}]
            },
            timeout=60
        )

        if response.status_code == 200:
            response_json = response.json()
            return response_json['content'][0]['text'], languages_dict
        else:
            print(f"API Error: {response.status_code} - {response.text}")
            return None, None
    except Exception as e:
        print(f"Error: {e}")
        return None, None

def parse_translations(response_text, languages_dict):
    """Parse response text to extract JSON for each language"""
    translations = {}
    lines = response_text.split('\n')

    current_lang = None
    current_json = []

    lang_code_to_name = {v: k for k, v in languages_dict.items()}

    for line in lines:
        line = line.strip()

        # Check for language markers
        if "---SPANISH---" in line or "---Spanish---" in line:
            if current_json and current_lang:
                try:
                    translations[current_lang] = json.loads('\n'.join(current_json))
                except:
                    pass
            current_lang = "es"
            current_json = []
        elif "---FRENCH---" in line or "---French---" in line:
            if current_json and current_lang:
                try:
                    translations[current_lang] = json.loads('\n'.join(current_json))
                except:
                    pass
            current_lang = "fr"
            current_json = []
        elif "---GERMAN---" in line or "---German---" in line:
            if current_json and current_lang:
                try:
                    translations[current_lang] = json.loads('\n'.join(current_json))
                except:
                    pass
            current_lang = "de"
            current_json = []
        elif "---PORTUGUESE---" in line or "---Portuguese---" in line:
            if current_json and current_lang:
                try:
                    translations[current_lang] = json.loads('\n'.join(current_json))
                except:
                    pass
            current_lang = "pt"
            current_json = []
        elif "---JAPANESE---" in line or "---Japanese---" in line:
            if current_json and current_lang:
                try:
                    translations[current_lang] = json.loads('\n'.join(current_json))
                except:
                    pass
            current_lang = "ja"
            current_json = []
        elif "---CHINESE" in line or "---Chinese" in line:
            if "SIMPLIFIED" in line or "SIMP" in line:
                if current_json and current_lang:
                    try:
                        translations[current_lang] = json.loads('\n'.join(current_json))
                    except:
                        pass
                current_lang = "zh"
                current_json = []
            elif "TRADITIONAL" in line or "TRAD" in line:
                if current_json and current_lang:
                    try:
                        translations[current_lang] = json.loads('\n'.join(current_json))
                    except:
                        pass
                current_lang = "zh-tw"
                current_json = []
        elif "---ITALIAN---" in line or "---Italian---" in line:
            if current_json and current_lang:
                try:
                    translations[current_lang] = json.loads('\n'.join(current_json))
                except:
                    pass
            current_lang = "it"
            current_json = []
        elif "---DUTCH---" in line or "---Dutch---" in line:
            if current_json and current_lang:
                try:
                    translations[current_lang] = json.loads('\n'.join(current_json))
                except:
                    pass
            current_lang = "nl"
            current_json = []
        elif line and current_lang:
            current_json.append(line)

    # Don't forget the last one
    if current_json and current_lang:
        try:
            translations[current_lang] = json.loads('\n'.join(current_json))
        except Exception as e:
            print(f"Error parsing last section for {current_lang}: {e}")

    return translations

def save_batch_files(batch_name, translations):
    """Save translations to batch files"""
    for code, data in translations.items():
        if isinstance(data, dict):
            filename = f"GenuisNet.ai/pages/reviews/analytics/mode-analytics-{batch_name}-{code}.json"
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"Saved: {filename}")

# Process all batches
for batch_name, languages_dict in batches.items():
    response_text, langs = translate_batch(batch_name, languages_dict)
    if response_text:
        translations = parse_translations(response_text, langs)
        print(f"Parsed {len(translations)} languages from response")
        save_batch_files(batch_name, translations)
        print(f"Completed {batch_name}\n")
    else:
        print(f"Failed to translate {batch_name}\n")

print("All translations complete!")
