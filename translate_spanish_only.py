#!/usr/bin/env python3
"""
SPANISH ONLY TRANSLATOR
Translates all 18,425 keys to SPANISH only
Fast test to measure translation time per language
"""

import json
import time
import requests
import os
from datetime import datetime

CACHE_FILE = 'translation_cache_es.json'
PROGRESS_FILE = 'translation_progress_es.json'

def load_cache():
    """Load cache"""
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
    return {'completed_keys': [], 'start_time': None}

def save_progress(progress):
    """Save progress"""
    with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
        json.dump(progress, f, indent=2, ensure_ascii=False)

def translate_text(text, cache):
    """Translate to Spanish using MyMemory API"""

    # Check cache
    if text in cache:
        return cache[text]

    # Skip very short, numeric, or code-like text
    if len(text) < 3:
        cache[text] = text
        return text

    if text.replace('$', '').replace(',', '').replace('.', '').isdigit():
        cache[text] = text
        return text

    if any(marker in text for marker in ['()', '{}', '[]', 'GPT-', 'API', 'http://', 'https://']):
        cache[text] = text
        return text

    # Call API
    url = "https://api.mymemory.translated.net/get"
    params = {
        'q': text[:500],
        'langpair': 'en|es-ES'
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data.get('responseStatus') == 200:
                translated = data['responseData']['translatedText']
                cache[text] = translated
                return translated
        time.sleep(0.5)
    except Exception as e:
        time.sleep(1)

    # Fallback
    cache[text] = text
    return text

def main():
    """Main translation process"""

    print("="*70)
    print("  SPANISH TRANSLATION - TEST MODE")
    print("  Translating 18,425 keys to SPANISH")
    print("="*70)

    # Load English source
    with open('all_full_translations_en.json', 'r', encoding='utf-8') as f:
        en_translations = json.load(f)

    total_keys = len(en_translations)
    print(f"\n📊 Total keys: {total_keys:,}")
    print(f"   Target: Spanish (ES)")
    print(f"   Estimated time: ~3-4 hours")
    print(f"\n🚀 Starting in 3 seconds...")
    time.sleep(3)

    # Load cache and progress
    cache = load_cache()
    progress = load_progress()
    completed = set(progress['completed_keys'])

    if not progress['start_time']:
        progress['start_time'] = datetime.now().isoformat()

    print(f"\n💾 Cache: {len(cache)} entries")
    print(f"   Progress: {len(completed)}/{total_keys} keys\n")

    # Initialize Spanish translations
    es_translations = {}

    # Process each key
    start_time = time.time()
    keys_list = list(en_translations.items())

    for i, (key, en_text) in enumerate(keys_list):
        # Skip if already completed
        if key in completed:
            if en_text in cache:
                es_translations[key] = cache[en_text]
            continue

        # Progress info
        elapsed = time.time() - start_time
        rate = (i - len(completed) + 1) / elapsed if elapsed > 0 else 0
        remaining = total_keys - i
        eta_seconds = remaining / rate if rate > 0 else 0
        eta_hours = eta_seconds / 3600
        eta_minutes = eta_seconds / 60

        if (i + 1) % 10 == 0:
            print(f"[{i+1}/{total_keys}] {(i+1)/total_keys*100:.1f}% | "
                  f"ETA: {eta_hours:.1f}h ({eta_minutes:.0f}min) | "
                  f"Rate: {rate*60:.1f}/min | {key[:45]}")

        # Translate
        translated = translate_text(en_text, cache)
        es_translations[key] = translated

        time.sleep(0.4)  # Rate limiting

        # Mark as completed
        completed.add(key)
        progress['completed_keys'] = list(completed)

        # Save every 50 keys
        if (i + 1) % 50 == 0:
            save_cache(cache)
            save_progress(progress)

            # Save partial
            with open('real_translations_es_partial.json', 'w', encoding='utf-8') as f:
                json.dump(es_translations, f, indent=2, ensure_ascii=False)

            print(f"  💾 Saved ({len(completed)}/{total_keys}) - Cache: {len(cache)}")

    # Save final
    print(f"\n{'='*70}")
    print("💾 SAVING FINAL SPANISH TRANSLATIONS")
    print(f"{'='*70}")

    with open('real_translations_es.json', 'w', encoding='utf-8') as f:
        json.dump(es_translations, f, indent=2, ensure_ascii=False)

    save_cache(cache)
    save_progress(progress)

    total_time = time.time() - start_time
    print(f"\n✅ ES: {len(es_translations):,} keys → real_translations_es.json")

    print(f"\n{'='*70}")
    print("🎉 SPANISH TRANSLATION COMPLETE!")
    print(f"{'='*70}")
    print(f"   Keys translated: {total_keys:,}")
    print(f"   Cache entries: {len(cache):,}")
    print(f"   Time taken: {total_time/3600:.2f} hours ({total_time/60:.0f} minutes)")
    print(f"   Rate: {total_keys/(total_time/60):.1f} keys/minute")
    print(f"\n   Estimated time for all 9 languages: {(total_time * 9)/3600:.1f} hours")
    print(f"{'='*70}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted! Progress and cache saved.")
        print("   Run script again to continue.")
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
