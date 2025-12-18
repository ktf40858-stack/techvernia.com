#!/usr/bin/env python3
"""
TEST BATCH TRANSLATOR - 100 items
Quick test to show the translation system works
"""

import json
import time
import requests

LANGUAGES = {
    'fr': 'fr-FR',
    'es': 'es-ES',
    'de': 'de-DE',
    'pt': 'pt-PT',
    'zh': 'zh-CN',
    'ja': 'ja-JP',
    'ko': 'ko-KR',
    'ar': 'ar-SA',
    'hi': 'hi-IN'
}

def translate_text(text, target_lang):
    """Translate text using MyMemory API"""

    if len(text) < 2 or text.isdigit():
        return text

    url = "https://api.mymemory.translated.net/get"
    params = {
        'q': text[:500],
        'langpair': f'en|{target_lang}'
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data.get('responseStatus') == 200:
                return data['responseData']['translatedText']
    except:
        pass

    return text

def test_translate():
    """Translate first 100 items as test"""

    # Load input
    with open('translation_batch_input.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Take first 100 items
    items = data['items'][:100]

    print("="*70)
    print("  TEST BATCH TRANSLATION - 100 items")
    print("="*70)

    translations = {lang: {} for lang in ['en'] + list(LANGUAGES.keys())}

    # Add English
    for item in items:
        translations['en'][item['key']] = item['text']

    # Translate
    start = time.time()

    for i, item in enumerate(items):
        print(f"\n[{i+1}/100] {item['text'][:50]}...")

        for lang_code, api_lang in LANGUAGES.items():
            trans = translate_text(item['text'], api_lang)
            translations[lang_code][item['key']] = trans
            print(f"  {lang_code}: {trans[:40]}...")
            time.sleep(0.3)

    elapsed = time.time() - start

    # Save results
    for lang in translations:
        with open(f'test_translations_{lang}.json', 'w', encoding='utf-8') as f:
            json.dump(translations[lang], f, indent=2, ensure_ascii=False)

    print(f"\n{'='*70}")
    print(f"✅ TEST COMPLETE!")
    print(f"{'='*70}")
    print(f"  Time: {elapsed/60:.1f} minutes")
    print(f"  Rate: {100*9/elapsed:.1f} translations/minute")
    print(f"  Estimated for all 1565 items: {(1565*9*elapsed)/(100*9*60):.0f} minutes")
    print(f"{'='*70}")

if __name__ == "__main__":
    test_translate()
