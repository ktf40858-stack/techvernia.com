#!/usr/bin/env python3
"""
BATCH TRANSLATOR - ALL 23 CATEGORIES
Extracts content from ALL 255 review pages
"""

import os
import json
import re
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
            all_items.append({
                'tool': tool_name,
                'file': html_path,
                'items': items
            })
            print(f"  {tool_name}: {len(items)} items")

    return all_items

def main():
    """Extract all content from ALL categories"""

    print("="*70)
    print("  BATCH TRANSLATOR - ALL 23 CATEGORIES")
    print("  Processing 255 Review Pages")
    print("="*70)

    # ALL categories (23 total)
    all_categories = [
        ('Chatbots', 'chatbots'),
        ('Writing', 'writing'),
        ('Image Generation', 'image'),
        ('Video', 'video'),
        ('Audio', 'audio'),
        ('Coding', 'coding'),
        ('Productivity', 'productivity'),
        ('SEO & Marketing', 'seo'),
        ('Business', 'business'),
        ('Networking', 'networking'),
        ('Cybersecurity', 'cybersecurity'),
        ('Architecture', 'architecture'),
        ('Medical', 'medical'),
        ('Analytics', 'analytics'),
        ('Legal', 'legal'),
        ('Customer Service', 'customer-service'),
        ('Education', 'education'),
        ('Sales', 'sales'),
        ('Research', 'research'),
        ('HR', 'hr'),
        ('Translation', 'translation'),
        ('Gaming', 'gaming'),
        ('Quantum', 'quantum'),
    ]

    all_content = []
    total_items = 0
    total_tools = 0

    for cat_name, cat_dir in all_categories:
        cat_items = create_translation_batch_files(cat_dir, cat_name)
        if cat_items:
            all_content.extend(cat_items)
            for tool_data in cat_items:
                total_items += len(tool_data['items'])
                total_tools += 1

    # Flatten all items for translation
    flat_items = []
    for tool_data in all_content:
        flat_items.extend(tool_data['items'])

    # Create master file with all content
    master_file = {
        'total_tools': total_tools,
        'total_items': total_items,
        'items': flat_items
    }

    output_file = 'translation_batch_all.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(master_file, f, indent=2, ensure_ascii=False)

    print(f"\n{'='*70}")
    print(f"📦 EXTRACTION COMPLETE")
    print(f"{'='*70}")
    print(f"   Total tools: {total_tools}")
    print(f"   Total items: {total_items:,}")
    print(f"   Output file: {output_file}")
    print(f"{'='*70}")

    # Also save tool mapping for later
    tool_mapping = {}
    for tool_data in all_content:
        tool_mapping[tool_data['tool']] = {
            'file': tool_data['file'],
            'item_count': len(tool_data['items'])
        }

    with open('tool_mapping.json', 'w', encoding='utf-8') as f:
        json.dump(tool_mapping, f, indent=2, ensure_ascii=False)

    print(f"\n📝 Also created: tool_mapping.json")
    print(f"\n{'='*70}")

if __name__ == "__main__":
    main()
