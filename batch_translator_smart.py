#!/usr/bin/env python3
"""
SMART BATCH TRANSLATOR
Uses intelligent batching and caching to translate content efficiently
Prepares content for batch translation via LLM or translation service
"""

import os
import re
import json
from pathlib import Path
from bs4 import BeautifulSoup

def clean_text(text):
    """Clean text"""
    if not text:
        return ""
    return ' '.join(text.split()).strip()

def text_to_key(text, prefix="", max_words=5):
    """Convert text to i18n key"""
    cleaned = clean_text(text)
    words = cleaned.split()[:max_words]
    key_text = ' '.join(words).lower()
    key_text = re.sub(r'[^a-z0-9\s-]', '', key_text)
    key_text = re.sub(r'\s+', '.', key_text).strip('.')

    if prefix:
        return f"{prefix}.{key_text}"
    return key_text

def extract_content_for_translation(html_path, tool_name):
    """Extract all content that needs translation"""

    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')
    article = soup.find('article') or soup.find('main') or soup.find('body')

    if not article:
        return []

    items = []

    # Extract all text elements
    for h1 in article.find_all('h1'):
        text = clean_text(h1.get_text())
        if text and 'data-i18n' not in str(h1):
            items.append({'type': 'h1', 'text': text})

    for h2 in article.find_all('h2'):
        text = clean_text(h2.get_text())
        if text and 'data-i18n' not in str(h2):
            items.append({'type': 'h2', 'text': text})

    for h3 in article.find_all('h3'):
        text = clean_text(h3.get_text())
        if text and 'data-i18n' not in str(h3):
            items.append({'type': 'h3', 'text': text})

    for p in article.find_all('p'):
        text = clean_text(p.get_text())
        if text and len(text) > 10 and 'data-i18n' not in str(p):
            items.append({'type': 'p', 'text': text})

    for li in article.find_all('li'):
        text = clean_text(li.get_text())
        if text and len(text) > 2 and 'data-i18n' not in str(li):
            items.append({'type': 'li', 'text': text})

    for badge in article.find_all(class_=re.compile('badge|label|tag')):
        text = clean_text(badge.get_text())
        if text and 'data-i18n' not in str(badge):
            items.append({'type': 'badge', 'text': text})

    for btn in article.find_all(['a', 'button'], class_=re.compile('btn|button')):
        text = clean_text(btn.get_text())
        if text and 'data-i18n' not in str(btn):
            items.append({'type': 'button', 'text': text})

    for th in article.find_all('th'):
        text = clean_text(th.get_text())
        if text and 'data-i18n' not in str(th):
            items.append({'type': 'th', 'text': text})

    for td in article.find_all('td'):
        text = clean_text(td.get_text())
        if text and len(text) > 2 and 'data-i18n' not in str(td):
            if not text.replace('$', '').replace(',', '').replace('.', '').isdigit():
                items.append({'type': 'td', 'text': text})

    # Add keys and tool name
    for item in items:
        item['tool'] = tool_name
        item['key'] = f"review.{tool_name}.{text_to_key(item['text'])}"

    return items

def create_translation_batch_files(category_dir, category_name):
    """Create batch files for a category"""

    review_path = f"GenuisNet.ai/pages/reviews/{category_dir}"

    if not os.path.exists(review_path):
        return None

    print(f"\n📁 Processing {category_name}...")

    all_items = []

    for filename in sorted(os.listdir(review_path)):
        if not filename.endswith('.html') or 'backup' in filename:
            continue

        tool_name = Path(filename).stem
        html_path = os.path.join(review_path, filename)

        items = extract_content_for_translation(html_path, tool_name)

        if items:
            all_items.extend(items)
            print(f"  {tool_name}: {len(items)} items")

    return all_items

def main():
    """Extract all content and create batch translation files"""

    print("="*70)
    print("  SMART BATCH TRANSLATOR - Content Extraction")
    print("="*70)

    # Test with a few categories first
    test_categories = [
        ('Chatbots', 'chatbots'),
        ('Writing', 'writing'),
        ('Video', 'video'),
    ]

    all_content = []

    for cat_name, cat_dir in test_categories:
        items = create_translation_batch_files(cat_dir, cat_name)
        if items:
            all_content.extend(items)

    # Create master file with all English text
    master_file = {
        'total_items': len(all_content),
        'items': all_content
    }

    output_file = 'translation_batch_input.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(master_file, f, indent=2, ensure_ascii=False)

    print(f"\n{'='*70}")
    print(f"📦 EXTRACTION COMPLETE")
    print(f"{'='*70}")
    print(f"   Total items: {len(all_content)}")
    print(f"   Output file: {output_file}")
    print(f"{'='*70}")

    # Create a simplified version for LLM translation
    simple_texts = [item['text'] for item in all_content]

    with open('texts_to_translate.txt', 'w', encoding='utf-8') as f:
        for i, text in enumerate(simple_texts, 1):
            f.write(f"{i}. {text}\n")

    print(f"\n📝 Also created: texts_to_translate.txt")
    print(f"   → Use this with Claude/ChatGPT/DeepL for batch translation")

    # Create template for translations
    template = {
        'fr': {},
        'es': {},
        'de': {},
        'pt': {},
        'zh': {},
        'ja': {},
        'ko': {},
        'ar': {},
        'hi': {}
    }

    for item in all_content:
        key = item['key']
        text = item['text']
        for lang in template:
            template[lang][key] = f"[TO_TRANSLATE: {text}]"

    with open('translation_template.json', 'w', encoding='utf-8') as f:
        json.dump(template, f, indent=2, ensure_ascii=False)

    print(f"   → Created: translation_template.json")
    print(f"\n{'='*70}")

if __name__ == "__main__":
    main()
