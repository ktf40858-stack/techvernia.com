#!/usr/bin/env python3
"""
Analyze content extraction - see how much needs translation
"""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup

def clean_text(text):
    """Clean text"""
    if not text:
        return ""
    return ' '.join(text.split()).strip()

def analyze_page(html_path):
    """Analyze a single page"""

    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')
    article = soup.find('article') or soup.find('main') or soup.find('body')

    if not article:
        return None

    counts = {
        'h1': 0, 'h2': 0, 'h3': 0,
        'p': 0, 'li': 0,
        'badge': 0, 'button': 0,
        'th': 0, 'td': 0
    }

    total_chars = 0

    # Count H1
    for h1 in article.find_all('h1'):
        text = clean_text(h1.get_text())
        if text and 'data-i18n' not in str(h1):
            counts['h1'] += 1
            total_chars += len(text)

    # Count H2
    for h2 in article.find_all('h2'):
        text = clean_text(h2.get_text())
        if text and 'data-i18n' not in str(h2):
            counts['h2'] += 1
            total_chars += len(text)

    # Count H3
    for h3 in article.find_all('h3'):
        text = clean_text(h3.get_text())
        if text and 'data-i18n' not in str(h3):
            counts['h3'] += 1
            total_chars += len(text)

    # Count paragraphs
    for p in article.find_all('p'):
        text = clean_text(p.get_text())
        if text and len(text) > 10 and 'data-i18n' not in str(p):
            counts['p'] += 1
            total_chars += len(text)

    # Count list items
    for li in article.find_all('li'):
        text = clean_text(li.get_text())
        if text and 'data-i18n' not in str(li):
            counts['li'] += 1
            total_chars += len(text)

    # Count badges
    for badge in article.find_all(class_=re.compile('badge|label|tag')):
        text = clean_text(badge.get_text())
        if text and 'data-i18n' not in str(badge):
            counts['badge'] += 1
            total_chars += len(text)

    # Count buttons
    for btn in article.find_all(['a', 'button'], class_=re.compile('btn|button')):
        text = clean_text(btn.get_text())
        if text and 'data-i18n' not in str(btn):
            counts['button'] += 1
            total_chars += len(text)

    # Count table headers
    for th in article.find_all('th'):
        text = clean_text(th.get_text())
        if text and 'data-i18n' not in str(th):
            counts['th'] += 1
            total_chars += len(text)

    # Count table cells
    for td in article.find_all('td'):
        text = clean_text(td.get_text())
        if text and len(text) > 2 and 'data-i18n' not in str(td):
            if not text.replace('$', '').replace(',', '').replace('.', '').isdigit():
                counts['td'] += 1
                total_chars += len(text)

    total_elements = sum(counts.values())

    return {
        'counts': counts,
        'total_elements': total_elements,
        'total_chars': total_chars
    }

def main():
    """Analyze ChatGPT and Claude pages"""

    print("="*70)
    print("  CONTENT ANALYSIS - Translation Scope")
    print("="*70)

    pages = [
        ("ChatGPT", "GenuisNet.ai/pages/reviews/chatbots/chatgpt.html"),
        ("Claude", "GenuisNet.ai/pages/reviews/chatbots/claude.html"),
    ]

    for name, path in pages:
        if not os.path.exists(path):
            print(f"\n❌ {name}: File not found")
            continue

        result = analyze_page(path)

        if result:
            print(f"\n📄 {name}")
            print(f"   Total elements: {result['total_elements']}")
            print(f"   Total characters: {result['total_chars']:,}")
            print(f"   Breakdown:")
            for elem_type, count in result['counts'].items():
                if count > 0:
                    print(f"      {elem_type}: {count}")

    # Estimate for all 255 pages
    print(f"\n{'='*70}")
    print("📊 ESTIMATED TOTALS FOR ALL 255 PAGES")
    print(f"{'='*70}")
    print(f"   If average = 150 elements per page:")
    print(f"   Total elements: {150 * 255:,}")
    print(f"   × 9 languages = {150 * 255 * 9:,} translations needed")
    print(f"{'='*70}")

if __name__ == "__main__":
    main()
