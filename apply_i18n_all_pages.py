#!/usr/bin/env python3
"""
APPLY I18N TO ALL PAGES
Wraps all translated content in data-i18n spans for ALL 232 pages
"""

import os
import json
import re
from pathlib import Path
from bs4 import BeautifulSoup

def apply_i18n_to_page(html_path, tool_items):
    """Apply data-i18n attributes to a single page"""

    if not os.path.exists(html_path):
        return 0

    # Read HTML
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')
    article = soup.find('article') or soup.find('main') or soup.find('body')

    if not article:
        return 0

    modifications = 0

    # Group items by type
    items_by_type = {}
    for item in tool_items:
        elem_type = item['type']
        if elem_type not in items_by_type:
            items_by_type[elem_type] = []
        items_by_type[elem_type].append(item)

    # Process each element type
    element_tags = {
        'h1': 'h1', 'h2': 'h2', 'h3': 'h3',
        'p': 'p', 'li': 'li', 'th': 'th', 'td': 'td'
    }

    for elem_type, tag in element_tags.items():
        if elem_type not in items_by_type:
            continue

        for elem in article.find_all(tag):
            text = ' '.join(elem.get_text().split()).strip()

            for item in items_by_type[elem_type]:
                if item['text'] == text and 'data-i18n' not in str(elem):
                    elem.clear()
                    span = soup.new_tag('span')
                    span['data-i18n'] = item['key']
                    span.string = text
                    elem.append(span)
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
    """Apply i18n to all pages"""

    print("="*70)
    print("  APPLYING DATA-I18N TO ALL 232 PAGES")
    print("="*70)

    # Load the batch input
    with open('translation_batch_all.json', 'r', encoding='utf-8') as f:
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

    # Load tool mapping
    with open('tool_mapping.json', 'r', encoding='utf-8') as f:
        tool_paths = json.load(f)

    # Process each tool
    total_modifications = 0
    successful = 0
    failed = 0

    for i, (tool_name, tool_items) in enumerate(items_by_tool.items(), 1):
        if tool_name not in tool_paths:
            print(f"\n⚠️  [{i}/{len(items_by_tool)}] {tool_name}: File not found")
            failed += 1
            continue

        html_path = tool_paths[tool_name]['file']

        if (i % 20 == 0):
            print(f"\n  Progress: {i}/{len(items_by_tool)} tools processed...")

        mods = apply_i18n_to_page(html_path, tool_items)

        if mods > 0:
            total_modifications += mods
            successful += 1
        else:
            failed += 1

    print(f"\n{'='*70}")
    print(f"🎉 I18N APPLICATION COMPLETE!")
    print(f"{'='*70}")
    print(f"📊 Results:")
    print(f"   Tools processed: {len(items_by_tool)}")
    print(f"   Successful: {successful}")
    print(f"   Failed/Skipped: {failed}")
    print(f"   Total data-i18n attributes added: {total_modifications:,}")
    print(f"{'='*70}")

if __name__ == "__main__":
    main()
