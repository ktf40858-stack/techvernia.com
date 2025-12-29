#!/usr/bin/env python3
import json
import urllib.request
import urllib.parse
import time

# Load the JSON file
file_path = r'C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\pages\reviews\business\tableau-batch3.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Extract English translations
english_texts = dict(data['ko'])

def translate_text(text, target_lang):
    """Translate using MyMemory API"""
    try:
        lang_map = {'ko': 'ko', 'ar': 'ar', 'hi': 'hi'}
        url = f"https://api.mymemory.translated.net/get?q={urllib.parse.quote(text)}&langpair=en|{lang_map[target_lang]}"

        with urllib.request.urlopen(url, timeout=10) as response:
            result = json.loads(response.read().decode('utf-8'))
            if result.get('responseStatus') == 200:
                return result['responseData']['translatedText']
    except:
        pass
    return text

# Translate
print("Translating Tableau batch3 to Korean, Arabic, and Hindi...")

for lang, lang_name in [('ko', 'Korean'), ('ar', 'Arabic'), ('hi', 'Hindi')]:
    print(f"\nProcessing {lang_name}...")
    data[lang] = {}
    for i, (key, english_text) in enumerate(english_texts.items(), 1):
        translated = translate_text(english_text, lang)
        data[lang][key] = translated
        if i % 10 == 0:
            print(f"  Completed {i}/73")
        time.sleep(0.1)  # Rate limiting

# Save
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\nComplete!")
