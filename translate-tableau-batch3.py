import json
import requests
from typing import Dict, List
import sys

# Set UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

# Load the JSON file
with open(r'C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\pages\reviews\business\tableau-batch3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Extract English translations (from ko section as reference)
english_texts = {}
for key, value in data['ko'].items():
    english_texts[key] = value

# Function to translate text using Google Translate API
def translate_text(text: str, target_lang: str) -> str:
    """
    Translate text using Google Translate (free API via MyMemory)
    target_lang: 'ko' for Korean, 'ar' for Arabic, 'hi' for Hindi
    """
    # Using MyMemory API (free, no key required)
    lang_map = {'ko': 'ko', 'ar': 'ar', 'hi': 'hi'}

    try:
        url = f"https://api.mymemory.translated.net/get?q={text}&langpair=en|{lang_map[target_lang]}"
        response = requests.get(url, timeout=10)
        result = response.json()

        if result['responseStatus'] == 200:
            return result['responseData']['translatedText']
        else:
            return text
    except Exception as e:
        return text

# Translate all keys to Korean, Arabic, and Hindi
print("Starting translations...")

# Korean translations
print("Translating to Korean (KO)...")
data['ko'] = {}
for i, (key, english_text) in enumerate(english_texts.items(), 1):
    translated = translate_text(english_text, 'ko')
    data['ko'][key] = translated
    print(f"  {i}. {key} translated")

# Arabic translations
print("\nTranslating to Arabic (AR)...")
data['ar'] = {}
for i, (key, english_text) in enumerate(english_texts.items(), 1):
    translated = translate_text(english_text, 'ar')
    data['ar'][key] = translated
    print(f"  {i}. {key} translated")

# Hindi translations
print("\nTranslating to Hindi (HI)...")
data['hi'] = {}
for i, (key, english_text) in enumerate(english_texts.items(), 1):
    translated = translate_text(english_text, 'hi')
    data['hi'][key] = translated
    print(f"  {i}. {key} translated")

# Save the translated JSON
with open(r'C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\pages\reviews\business\tableau-batch3.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\nTranslation complete! File saved.")
