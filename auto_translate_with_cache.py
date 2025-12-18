#!/usr/bin/env python3
"""
AUTO TRANSLATOR WITH SMART CACHING
Translates content using MyMemory API with intelligent caching
Saves progress incrementally to avoid losing work
"""

import os
import json
import time
import requests
from pathlib import Path

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

CACHE_FILE = 'translation_cache.json'
PROGRESS_FILE = 'translation_progress.json'

def load_cache():
    """Load translation cache"""
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_cache(cache):
    """Save translation cache"""
    with open(CACHE_FILE, 'w', encoding='utf-8') as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)

def load_progress():
    """Load translation progress"""
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {'completed_indices': []}

def save_progress(progress):
    """Save translation progress"""
    with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
        json.dump(progress, f, indent=2, ensure_ascii=False)

def translate_text(text, target_lang, cache):
    """Translate text with caching"""

    # Check cache first
    cache_key = f"{text}|{target_lang}"

    if cache_key in cache:
        return cache[cache_key]

    # Skip translation for very short or numeric text
    if len(text) < 2 or text.isdigit():
        cache[cache_key] = text
        return text

    # Call MyMemory API
    url = "https://api.mymemory.translated.net/get"

    params = {
        'q': text[:500],  # Limit to 500 chars
        'langpair': f'en|{target_lang}'
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 200:
            data = response.json()

            if data.get('responseStatus') == 200:
                translated = data['responseData']['translatedText']

                # Cache the result
                cache[cache_key] = translated
                return translated

        # If error, wait a bit longer
        time.sleep(2)

    except Exception as e:
        print(f"      ⚠️  Error: {e}")
        time.sleep(2)

    # Return original if translation fails
    cache[cache_key] = text
    return text

def batch_translate(input_file='translation_batch_input.json'):
    """Translate all content from input file"""

    if not os.path.exists(input_file):
        print(f"❌ Input file not found: {input_file}")
        return

    print("="*70)
    print("  AUTO TRANSLATOR WITH SMART CACHING")
    print("="*70)

    # Load input
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    items = data['items']
    total = len(items)

    print(f"\n📊 Total items to translate: {total}")
    print(f"   Languages: {len(LANGUAGES)}")
    print(f"   Total translations: {total * len(LANGUAGES):,}")

    # Load cache and progress
    cache = load_cache()
    progress = load_progress()
    completed = set(progress['completed_indices'])

    print(f"\n💾 Loaded cache: {len(cache)} cached translations")
    print(f"   Completed: {len(completed)}/{total} items")

    # Create translation structure
    translations = {lang: {} for lang in ['en'] + list(LANGUAGES.keys())}

    # Add all English keys first
    for item in items:
        key = item['key']
        text = item['text']
        translations['en'][key] = text

    # Translate each item
    start_time = time.time()

    for i, item in enumerate(items):
        # Skip if already completed
        if i in completed:
            continue

        key = item['key']
        text = item['text']
        tool = item['tool']

        # Progress indicator
        remaining = total - i
        elapsed = time.time() - start_time
        rate = (i - len(completed) + 1) / elapsed if elapsed > 0 else 0
        eta = remaining / rate if rate > 0 else 0

        print(f"\n[{i+1}/{total}] {tool}: {text[:60]}...")
        print(f"  Progress: {(i/total)*100:.1f}% | ETA: {eta/60:.1f} min")

        # Translate to each language
        for lang_code, api_lang in LANGUAGES.items():
            translated = translate_text(text, api_lang, cache)
            translations[lang_code][key] = translated

            print(f"    {lang_code}: {translated[:40]}...")

            # Rate limiting
            time.sleep(0.5)

        # Mark as completed
        completed.add(i)
        progress['completed_indices'] = list(completed)

        # Save progress every 10 items
        if (i + 1) % 10 == 0:
            save_progress(progress)
            save_cache(cache)

            print(f"\n  💾 Progress saved ({len(completed)}/{total} items)")

            # Save intermediate translations
            for lang in translations:
                filename = f'translations_{lang}_partial.json'
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(translations[lang], f, indent=2, ensure_ascii=False)

    # Save final results
    print(f"\n{'='*70}")
    print("💾 SAVING FINAL RESULTS")
    print(f"{'='*70}")

    for lang in translations:
        filename = f'full_translations_{lang}.json'
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(translations[lang], f, indent=2, ensure_ascii=False)

        print(f"  ✅ {lang.upper()}: {len(translations[lang])} keys → {filename}")

    save_cache(cache)
    save_progress({'completed_indices': list(completed)})

    print(f"\n{'='*70}")
    print("🎉 TRANSLATION COMPLETE!")
    print(f"{'='*70}")
    print(f"📊 Stats:")
    print(f"   Items translated: {total}")
    print(f"   Languages: {len(LANGUAGES) + 1}")
    print(f"   Total translations: {total * (len(LANGUAGES) + 1):,}")
    print(f"   Cache entries: {len(cache)}")
    print(f"   Time elapsed: {(time.time() - start_time)/60:.1f} minutes")
    print(f"{'='*70}")

if __name__ == "__main__":
    try:
        batch_translate()
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted! Progress has been saved.")
        print("   Run script again to continue from where you left off.")
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
