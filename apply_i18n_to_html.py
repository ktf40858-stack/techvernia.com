#!/usr/bin/env python3
"""
APPLY I18N TO HTML
Wraps translated content in data-i18n spans in the HTML files
"""

import os
import json
import re
from pathlib import Path
from bs4 import BeautifulSoup

def apply_i18n_to_page(html_path, tool_items):
    """Apply data-i18n attributes to a single page"""

    if not os.path.exists(html_path):
        print(f"  ⚠️  File not found: {html_path}")
        return 0

    # Read HTML
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')
    article = soup.find('article') or soup.find('main') or soup.find('body')

    if not article:
        print(f"  ⚠️  No article content found")
        return 0

    modifications = 0

    # Group items by type for efficient processing
    items_by_type = {}
    for item in tool_items:
        elem_type = item['type']
        if elem_type not in items_by_type:
            items_by_type[elem_type] = []
        items_by_type[elem_type].append(item)

    # Process H2
    if 'h2' in items_by_type:
        for h2 in article.find_all('h2'):
            text = ' '.join(h2.get_text().split()).strip()

            # Find matching item
            for item in items_by_type['h2']:
                if item['text'] == text and 'data-i18n' not in str(h2):
                    # Wrap in span
                    h2.clear()
                    span = soup.new_tag('span')
                    span['data-i18n'] = item['key']
                    span.string = text
                    h2.append(span)
                    modifications += 1
                    break

    # Process H3
    if 'h3' in items_by_type:
        for h3 in article.find_all('h3'):
            text = ' '.join(h3.get_text().split()).strip()

            for item in items_by_type['h3']:
                if item['text'] == text and 'data-i18n' not in str(h3):
                    h3.clear()
                    span = soup.new_tag('span')
                    span['data-i18n'] = item['key']
                    span.string = text
                    h3.append(span)
                    modifications += 1
                    break

    # Process paragraphs
    if 'p' in items_by_type:
        for p in article.find_all('p'):
            text = ' '.join(p.get_text().split()).strip()

            for item in items_by_type['p']:
                if item['text'] == text and 'data-i18n' not in str(p):
                    p.clear()
                    span = soup.new_tag('span')
                    span['data-i18n'] = item['key']
                    span.string = text
                    p.append(span)
                    modifications += 1
                    break

    # Process list items
    if 'li' in items_by_type:
        for li in article.find_all('li'):
            text = ' '.join(li.get_text().split()).strip()

            for item in items_by_type['li']:
                if item['text'] == text and 'data-i18n' not in str(li):
                    li.clear()
                    span = soup.new_tag('span')
                    span['data-i18n'] = item['key']
                    span.string = text
                    li.append(span)
                    modifications += 1
                    break

    # Process buttons
    if 'button' in items_by_type:
        for btn in article.find_all(['a', 'button'], class_=re.compile('btn|button')):
            text = ' '.join(btn.get_text().split()).strip()

            for item in items_by_type['button']:
                if item['text'] == text and 'data-i18n' not in str(btn):
                    btn.clear()
                    span = soup.new_tag('span')
                    span['data-i18n'] = item['key']
                    span.string = text
                    btn.append(span)
                    modifications += 1
                    break

    # Process table headers
    if 'th' in items_by_type:
        for th in article.find_all('th'):
            text = ' '.join(th.get_text().split()).strip()

            for item in items_by_type['th']:
                if item['text'] == text and 'data-i18n' not in str(th):
                    th.clear()
                    span = soup.new_tag('span')
                    span['data-i18n'] = item['key']
                    span.string = text
                    th.append(span)
                    modifications += 1
                    break

    # Process table cells
    if 'td' in items_by_type:
        for td in article.find_all('td'):
            text = ' '.join(td.get_text().split()).strip()

            for item in items_by_type['td']:
                if item['text'] == text and 'data-i18n' not in str(td):
                    td.clear()
                    span = soup.new_tag('span')
                    span['data-i18n'] = item['key']
                    span.string = text
                    td.append(span)
                    modifications += 1
                    break

    # Process badges
    if 'badge' in items_by_type:
        for badge in article.find_all(class_=re.compile('badge|label|tag')):
            text = ' '.join(badge.get_text().split()).strip()

            for item in items_by_type['badge']:
                if item['text'] == text and 'data-i18n' not in str(badge):
                    badge.clear()
                    span = soup.new_tag('span')
                    span['data-i18n'] = item['key']
                    span.string = text
                    badge.append(span)
                    modifications += 1
                    break

    # Save modified HTML
    if modifications > 0:
        # Backup
        backup_path = html_path + '.fullcontent_backup'
        if not os.path.exists(backup_path):
            with open(backup_path, 'w', encoding='utf-8') as f:
                with open(html_path, 'r', encoding='utf-8') as orig:
                    f.write(orig.read())

        # Write modified
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))

    return modifications

def main():
    """Apply i18n to all processed pages"""

    print("="*70)
    print("  APPLYING DATA-I18N TO HTML FILES")
    print("="*70)

    # Load the batch input to get mappings
    with open('translation_batch_input.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    items = data['items']

    # Group items by tool
    items_by_tool = {}
    for item in items:
        tool = item['tool']
        if tool not in items_by_tool:
            items_by_tool[tool] = []
        items_by_tool[tool].append(item)

    print(f"\n📊 Processing {len(items_by_tool)} tools...")

    # Map tool names to their file paths
    tool_paths = {}

    # Search in all category directories
    categories = [
        ('chatbots', 'GenuisNet.ai/pages/reviews/chatbots'),
        ('writing', 'GenuisNet.ai/pages/reviews/writing'),
        ('video', 'GenuisNet.ai/pages/reviews/video'),
    ]

    for cat_name, cat_path in categories:
        if os.path.exists(cat_path):
            for filename in os.listdir(cat_path):
                if filename.endswith('.html') and 'backup' not in filename:
                    tool_name = Path(filename).stem
                    tool_paths[tool_name] = os.path.join(cat_path, filename)

    # Process each tool
    total_modifications = 0

    for tool_name, tool_items in items_by_tool.items():
        if tool_name not in tool_paths:
            print(f"\n⚠️  {tool_name}: File not found")
            continue

        html_path = tool_paths[tool_name]

        print(f"\n📄 {tool_name}: Applying {len(tool_items)} attributes...")

        mods = apply_i18n_to_page(html_path, tool_items)

        if mods > 0:
            print(f"  ✅ Added {mods} data-i18n attributes")
            total_modifications += mods
        else:
            print(f"  ℹ️  No modifications made")

    print(f"\n{'='*70}")
    print(f"🎉 I18N APPLICATION COMPLETE!")
    print(f"{'='*70}")
    print(f"📊 Total data-i18n attributes added: {total_modifications}")
    print(f"{'='*70}")

if __name__ == "__main__":
    main()
