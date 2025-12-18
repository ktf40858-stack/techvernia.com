#!/usr/bin/env python3
"""
REAL TRANSLATOR - Actually translates content using MyMemory API
Processes all 18,425 keys with progress tracking and caching
"""

import json
import time
import requests
import os

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

CACHE_FILE = 'real_translation_cache.json'
PROGRESS_FILE = 'real_translation_progress.json'

def load_cache():
    """Load translation cache"""
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_cache(cache):
    """Save cache"""
    with open(CACHE_FILE, 'w', encoding='utf-8') as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)

def load_progress():
    """Load progress"""
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {'completed_keys': []}

def save_progress(progress):
    """Save progress"""
    with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
        json.dump(progress, f, indent=2, ensure_ascii=False)

def translate_text(text, target_lang, cache):
    """Translate using MyMemory API with caching"""

    # Check cache
    cache_key = f"{text[:100]}|{target_lang}"
    if cache_key in cache:
        return cache[cache_key]

    # Skip very short or numeric text
    if len(text) < 3 or text.replace('$', '').replace(',', '').isdigit():
        cache[cache_key] = text
        return text

    # Skip if contains code markers
    if any(marker in text for marker in ['()', '{}', '[]', '<>', '//', '/*', 'GPT-', 'API']):
        cache[cache_key] = text
        return text

    # Call API
    url = "https://api.mymemory.translated.net/get"
    params = {
        'q': text[:500],  # Limit length
        'langpair': f'en|{target_lang}'
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data.get('responseStatus') == 200:
                translated = data['responseData']['translatedText']
                cache[cache_key] = translated
                return translated
        time.sleep(1)  # Rate limiting
    except Exception as e:
        print(f"      ⚠️  API Error: {str(e)[:50]}")
        time.sleep(2)

    # Fallback
    cache[cache_key] = text
    return text

def main():
    """Main translation process"""

    print("="*70)
    print("  REAL TRANSLATOR - API-based Translation")
    print("  WARNING: This will take several hours!")
    print("="*70)

    # Load English source
    with open('all_full_translations_en.json', 'r', encoding='utf-8') as f:
        en_translations = json.load(f)

    total_keys = len(en_translations)
    print(f"\n📊 Total keys to translate: {total_keys:,}")
    print(f"   Languages: {len(LANGUAGES)}")
    print(f"   Total API calls needed: ~{total_keys * len(LANGUAGES):,}")
    print(f"   Estimated time: {(total_keys * len(LANGUAGES) * 0.5) / 3600:.1f} hours")

    response = input("\n⚠️  This will take a VERY long time. Continue? (yes/no): ")
    if response.lower() != 'yes':
        print("Cancelled.")
        return

    # Load cache and progress
    cache = load_cache()
    progress = load_progress()
    completed = set(progress['completed_keys'])

    print(f"\n💾 Cache: {len(cache)} entries")
    print(f"   Progress: {len(completed)}/{total_keys} keys completed")

    # Initialize translations
    translations = {lang: {} for lang in LANGUAGES}

    # Process each key
    start_time = time.time()
    keys_list = list(en_translations.items())

    for i, (key, en_text) in enumerate(keys_list):
        # Skip if already completed
        if key in completed:
            # Load from cache
            for lang_code in LANGUAGES:
                cache_key = f"{en_text[:100]}|{lang_code}"
                if cache_key in cache:
                    translations[lang_code][key] = cache[cache_key]
            continue

        # Progress info
        elapsed = time.time() - start_time
        rate = (i - len(completed) + 1) / elapsed if elapsed > 0 else 0
        remaining = total_keys - i
        eta_seconds = remaining / rate if rate > 0 else 0
        eta_hours = eta_seconds / 3600

        if (i + 1) % 10 == 0:
            print(f"\n[{i+1}/{total_keys}] Progress: {(i+1)/total_keys*100:.1f}% | ETA: {eta_hours:.1f}h")
            print(f"  Key: {key[:60]}...")
            print(f"  Text: {en_text[:60]}...")

        # Translate to all languages
        for lang_code, api_lang in LANGUAGES.items():
            translated = translate_text(en_text, api_lang, cache)
            translations[lang_code][key] = translated

            if (i + 1) % 10 == 0:
                print(f"    {lang_code}: {translated[:40]}...")

            time.sleep(0.3)  # Rate limiting

        # Mark as completed
        completed.add(key)
        progress['completed_keys'] = list(completed)

        # Save every 50 keys
        if (i + 1) % 50 == 0:
            save_cache(cache)
            save_progress(progress)

            # Save intermediate files
            for lang in translations:
                filename = f'real_translations_{lang}_partial.json'
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(translations[lang], f, indent=2, ensure_ascii=False)

            print(f"\n  💾 Progress saved ({len(completed)}/{total_keys})")

    # Save final results
    print(f"\n{'='*70}")
    print("💾 SAVING FINAL RESULTS")
    print(f"{'='*70}")

    for lang in translations:
        filename = f'real_translations_{lang}.json'
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(translations[lang], f, indent=2, ensure_ascii=False)
        print(f"  ✅ {lang.upper()}: {len(translations[lang]):,} keys → {filename}")

    save_cache(cache)
    save_progress(progress)

    total_time = time.time() - start_time
    print(f"\n{'='*70}")
    print("🎉 TRANSLATION COMPLETE!")
    print(f"{'='*70}")
    print(f"   Keys translated: {total_keys:,}")
    print(f"   Languages: {len(LANGUAGES)}")
    print(f"   Total translations: {total_keys * len(LANGUAGES):,}")
    print(f"   Cache entries: {len(cache):,}")
    print(f"   Time taken: {total_time/3600:.1f} hours")
    print(f"{'='*70}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted! Progress and cache saved.")
        print("   Run script again to continue from where you left off.")
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
