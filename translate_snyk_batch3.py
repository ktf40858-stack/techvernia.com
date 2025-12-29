import json
import urllib.request
import urllib.parse

# Read the JSON file
input_file = r"GenuisNet.ai\pages\reviews\cybersecurity\snyk-batch3.json"

with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

en_content = data.get('en', {})

# Function to translate text using MyMemory API
def translate_text(text, target_lang):
    """Translate text to target language using MyMemory API"""
    try:
        # MyMemory doesn't need authentication and is free
        text_encoded = urllib.parse.quote(text)
        url = f"https://api.mymemory.translated.net/get?q={text_encoded}&langpair=en|{target_lang}"

        with urllib.request.urlopen(url, timeout=5) as response:
            result = json.loads(response.read().decode('utf-8'))
            if result['responseStatus'] == 200:
                return result['responseData']['translatedText']
            else:
                return text
    except Exception as e:
        print(f"Error translating: {e}")
        return text

# Languages to translate to
languages = {
    'ko': 'Korean',
    'ar': 'Arabic',
    'hi': 'Hindi'
}

# Translate all keys
for lang_code, lang_name in languages.items():
    print(f"Translating to {lang_name} ({lang_code})...")
    translated_content = {}

    for key, value in en_content.items():
        try:
            translated_value = translate_text(value, lang_code)
            translated_content[key] = translated_value
            print(f"  {key}: OK")
        except Exception as e:
            print(f"  Error translating {key}: {e}")
            translated_content[key] = value

    # Add to data
    data[lang_code] = translated_content
    print(f"Completed {lang_name}\n")

# Save the updated file
with open(input_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"File saved to {input_file}")
