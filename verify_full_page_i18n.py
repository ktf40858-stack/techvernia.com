#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Verify full page i18n coverage
Find all text elements that should be translated but don't have data-i18n
"""

import os
import re
from bs4 import BeautifulSoup

# Base directory
base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
pages_dir = os.path.join(base_dir, "pages", "reviews", "translation")

def verify_page_i18n(tool_key):
    """Verify i18n coverage for a page"""

    html_file = os.path.join(pages_dir, f"{tool_key}.html")

    if not os.path.exists(html_file):
        return None

    with open(html_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Find all elements with text content (excluding script, style, etc.)
    issues = []

    # Check main content sections
    main_sections = soup.find_all(['h1', 'h2', 'h3', 'h4', 'p', 'li', 'span', 'a', 'button'])

    for elem in main_sections:
        # Skip elements that are inside script or style tags
        if elem.find_parent(['script', 'style']):
            continue

        # Skip if element is empty
        text = elem.get_text(strip=True)
        if not text or len(text) < 2:
            continue

        # Skip if it's just a number or special character
        if re.match(r'^[\d\s\.,\-\+\*\/\(\)]+$', text):
            continue

        # Skip URLs
        if text.startswith('http'):
            continue

        # Check if element or parent has data-i18n
        has_i18n = elem.has_attr('data-i18n') or any(parent.has_attr('data-i18n') for parent in elem.parents if parent.name != '[document]')

        # Skip nav items (handled by nav-i18n.js)
        if elem.find_parent(class_='nav-menu') or elem.find_parent(id='nav-menu'):
            continue

        # Skip meta, already i18n'd elements
        if has_i18n:
            continue

        # This element doesn't have i18n
        issues.append({
            'tag': elem.name,
            'class': elem.get('class', []),
            'text': text[:50] + ('...' if len(text) > 50 else ''),
            'parent': elem.parent.name if elem.parent else 'None'
        })

    return issues

# Check deepl-pro as example
print("=" * 70)
print("CHECKING DEEPL PRO PAGE FOR MISSING I18N")
print("=" * 70)
print()

issues = verify_page_i18n('deepl-pro')

if issues:
    print(f"Found {len(issues)} potential elements without i18n:")
    print()

    # Group by tag
    by_tag = {}
    for issue in issues:
        tag = issue['tag']
        if tag not in by_tag:
            by_tag[tag] = []
        by_tag[tag].append(issue)

    for tag, items in by_tag.items():
        print(f"{tag.upper()} ({len(items)} items):")
        for item in items[:5]:  # Show first 5
            classes = ', '.join(item['class']) if item['class'] else 'no-class'
            try:
                print(f"  [{classes}] {item['text']}")
            except UnicodeEncodeError:
                print(f"  [{classes}] [Unicode text]")
        if len(items) > 5:
            print(f"  ... and {len(items) - 5} more")
        print()
else:
    print("[SUCCESS] All text elements have i18n coverage!")

print("=" * 70)
