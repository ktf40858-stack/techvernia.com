#!/usr/bin/env python3
"""
FULL CONTENT TRANSLATOR
Extracts and translates ALL content from review pages (not just titles)
Uses MyMemory Translation API (free, no API key needed)
"""

import os
import re
import json
import time
import requests
from pathlib import Path
from bs4 import BeautifulSoup

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
    """Translate text using MyMemory API (free)"""

    if not text or len(text.strip()) == 0:
        return text

    # Skip if already in target language or is a number/symbol
    if text.isdigit() or len(text) < 2:
        return text

    # MyMemory API endpoint
    url = "https://api.mymemory.translated.net/get"

    params = {
        'q': text,
        'langpair': f'en|{target_lang}'
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 200:
            data = response.json()

            if data.get('responseStatus') == 200:
                translated = data['responseData']['translatedText']

                # Quality check - if translation is same as original, might be error
                if translated != text:
                    return translated

    except Exception as e:
        print(f"    ⚠️  Translation error: {e}")

    # Return original if translation fails
    return text

def clean_text(text):
    """Clean text for translation"""
    if not text:
        return ""

    # Remove extra whitespace
    text = ' '.join(text.split())
    return text.strip()

def text_to_key(text, prefix="", max_words=5):
    """Convert text to i18n key"""

    cleaned = clean_text(text)

    # Take first N words
    words = cleaned.split()[:max_words]
    key_text = ' '.join(words).lower()

    # Remove special characters
    key_text = re.sub(r'[^a-z0-9\s-]', '', key_text)

    # Replace spaces with dots
    key_text = re.sub(r'\s+', '.', key_text).strip('.')

    if prefix:
        return f"{prefix}.{key_text}"
    return key_text

def extract_full_content(html_path, tool_name):
    """Extract ALL translatable content from HTML"""

    print(f"\n📄 Extracting content from: {tool_name}")

    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')

    # Find the main article/content area
    article = soup.find('article') or soup.find('main') or soup.find('body')

    if not article:
        print(f"  ⚠️  No article content found")
        return None

    extractions = []

    # 1. Extract H1 (title)
    h1 = article.find('h1')
    if h1:
        text = clean_text(h1.get_text())
        if text and 'data-i18n' not in str(h1):
            extractions.append({
                'type': 'h1',
                'text': text,
                'element': h1
            })

    # 2. Extract H2 section titles
    for h2 in article.find_all('h2'):
        text = clean_text(h2.get_text())
        if text and 'data-i18n' not in str(h2):
            extractions.append({
                'type': 'h2',
                'text': text,
                'element': h2
            })

    # 3. Extract H3 subsection titles
    for h3 in article.find_all('h3'):
        text = clean_text(h3.get_text())
        if text and 'data-i18n' not in str(h3):
            extractions.append({
                'type': 'h3',
                'text': text,
                'element': h3
            })

    # 4. Extract paragraphs
    for p in article.find_all('p'):
        text = clean_text(p.get_text())
        if text and len(text) > 10 and 'data-i18n' not in str(p):
            # Skip if inside a data-i18n element
            parent_has_i18n = False
            for parent in p.parents:
                if 'data-i18n' in str(parent):
                    parent_has_i18n = True
                    break

            if not parent_has_i18n:
                extractions.append({
                    'type': 'p',
                    'text': text,
                    'element': p
                })

    # 5. Extract list items (pros, cons, features)
    for li in article.find_all('li'):
        text = clean_text(li.get_text())
        if text and 'data-i18n' not in str(li):
            # Get only direct text, not nested
            direct_text = clean_text(li.find(text=True, recursive=False) or '')
            if not direct_text:
                direct_text = text

            if direct_text and len(direct_text) > 2:
                extractions.append({
                    'type': 'li',
                    'text': direct_text,
                    'element': li
                })

    # 6. Extract badges/labels
    for badge in article.find_all(class_=re.compile('badge|label|tag')):
        text = clean_text(badge.get_text())
        if text and 'data-i18n' not in str(badge):
            extractions.append({
                'type': 'badge',
                'text': text,
                'element': badge
            })

    # 7. Extract button text
    for btn in article.find_all(['a', 'button'], class_=re.compile('btn|button')):
        text = clean_text(btn.get_text())
        if text and 'data-i18n' not in str(btn):
            extractions.append({
                'type': 'button',
                'text': text,
                'element': btn
            })

    # 8. Extract table headers and cells
    for th in article.find_all('th'):
        text = clean_text(th.get_text())
        if text and 'data-i18n' not in str(th):
            extractions.append({
                'type': 'th',
                'text': text,
                'element': th
            })

    for td in article.find_all('td'):
        text = clean_text(td.get_text())
        if text and len(text) > 2 and 'data-i18n' not in str(td):
            # Skip cells with only numbers
            if not text.replace('$', '').replace(',', '').replace('.', '').isdigit():
                extractions.append({
                    'type': 'td',
                    'text': text,
                    'element': td
                })

    print(f"  📊 Found {len(extractions)} elements to translate")
    return extractions

def translate_content(extractions, tool_name):
    """Translate all extracted content to all languages"""

    print(f"\n🌐 Translating {len(extractions)} elements to 9 languages...")

    translations = {lang: {} for lang in ['en'] + list(LANGUAGES.keys())}

    for i, item in enumerate(extractions):
        text = item['text']

        # Generate i18n key
        key = f"review.{tool_name}.{text_to_key(text, max_words=5)}"

        # Add English (original)
        translations['en'][key] = text

        # Translate to other languages
        print(f"  [{i+1}/{len(extractions)}] Translating: {text[:50]}...")

        for lang_code, api_lang in LANGUAGES.items():
            translated = translate_text(text, api_lang)
            translations[lang_code][key] = translated

            # Rate limiting - be nice to free API
            time.sleep(0.3)

        item['key'] = key

    return translations

def apply_i18n_to_html(html_path, extractions):
    """Apply data-i18n attributes to HTML"""

    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')

    modified_count = 0

    for item in extractions:
        element = item['element']
        key = item['key']
        text = item['text']
        elem_type = item['type']

        # Wrap text in span with data-i18n
        if elem_type in ['h1', 'h2', 'h3', 'p', 'li', 'badge', 'button', 'th', 'td']:
            # Clear element and add span
            element.clear()
            span = soup.new_tag('span')
            span['data-i18n'] = key
            span.string = text
            element.append(span)
            modified_count += 1

    # Save modified HTML
    backup_path = html_path + '.fullcontent_backup'
    if not os.path.exists(backup_path):
        with open(html_path + '.fullcontent_backup', 'w', encoding='utf-8') as f:
            with open(html_path, 'r', encoding='utf-8') as orig:
                f.write(orig.read())

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))

    print(f"  ✅ Applied {modified_count} data-i18n attributes")
    return modified_count

def process_single_tool(html_path, tool_name):
    """Process a single tool page"""

    # Extract all content
    extractions = extract_full_content(html_path, tool_name)

    if not extractions or len(extractions) == 0:
        print(f"  ⚠️  No content to translate")
        return None

    # Translate content
    translations = translate_content(extractions, tool_name)

    # Apply to HTML
    apply_i18n_to_html(html_path, extractions)

    return translations

def main():
    """Main execution - process ChatGPT as test first"""

    print("="*70)
    print("  FULL CONTENT TRANSLATOR - TEST WITH CHATGPT")
    print("="*70)

    # Test with ChatGPT first
    test_file = "GenuisNet.ai/pages/reviews/chatbots/chatgpt.html"

    if not os.path.exists(test_file):
        print(f"❌ Test file not found: {test_file}")
        return

    print(f"\n🧪 Testing with ChatGPT review...")

    translations = process_single_tool(test_file, 'chatgpt')

    if translations:
        # Save translations
        for lang in translations:
            filename = f'full_translations_{lang}_chatgpt.json'
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(translations[lang], f, indent=2, ensure_ascii=False)

            print(f"  ✅ Saved {lang}: {len(translations[lang])} keys → {filename}")

        print("\n" + "="*70)
        print("🎉 TEST COMPLETE!")
        print("="*70)
        print(f"📊 Generated {len(translations['en'])} translation keys")
        print("📌 Review the results before processing all 255 pages")
        print("="*70)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
