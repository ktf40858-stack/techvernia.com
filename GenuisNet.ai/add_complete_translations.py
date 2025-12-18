#!/usr/bin/env python3
"""
Add Complete Translations to All Pages
This script adds data-i18n attributes to ALL text elements on pages
"""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup

# Common translations to add
COMMON_TRANSLATIONS = {
    "Tools Reviewed": "stats.toolsReviewed",
    "Avg Rating": "stats.avgRating",
    "Full Review": "btn.fullReview",
    "United States": "country.us",
    "Tools": "common.tools",
    "AI Tools": "common.aiTools",
    "Popular": "badge.popular",
    "Free": "badge.free",
    "Paid": "badge.paid",
    "From": "price.from",
    "per month": "price.perMonth",
}

# Category descriptions mapping
CATEGORY_DESCRIPTIONS = {
    "ai-chatbots": {
        "title": "cat.chatbots",
        "desc": "cat.chatbots.full"
    },
    "ai-writing": {
        "title": "cat.writing",
        "desc": "cat.writing.full"
    },
    "ai-image": {
        "title": "cat.image",
        "desc": "cat.image.full"
    },
    "ai-video": {
        "title": "cat.video",
        "desc": "cat.video.full"
    },
    "ai-audio": {
        "title": "cat.audio",
        "desc": "cat.audio.full"
    },
    "ai-coding": {
        "title": "cat.coding",
        "desc": "cat.coding.full"
    },
    "ai-productivity": {
        "title": "cat.productivity",
        "desc": "cat.productivity.full"
    },
    "ai-business": {
        "title": "cat.business",
        "desc": "cat.business.full"
    },
    "ai-networking": {
        "title": "cat.networking",
        "desc": "cat.networking.full"
    },
    "ai-cybersecurity": {
        "title": "cat.cybersecurity",
        "desc": "cat.cybersecurity.full"
    }
}

def add_translations_to_page(file_path):
    """Add data-i18n attributes to a page"""
    print(f"\n📄 Processing: {file_path}")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        changes = 0

        # Detect category from filename
        filename = os.path.basename(file_path)
        category_key = filename.replace('.html', '')

        # Add data-i18n to category title (h1)
        if category_key in CATEGORY_DESCRIPTIONS:
            i18n_key = CATEGORY_DESCRIPTIONS[category_key]["title"]
            desc_key = CATEGORY_DESCRIPTIONS[category_key]["desc"]

            # Fix h1 without data-i18n
            if '<h1>' in content and 'data-i18n' not in content.split('<h1>')[1].split('</h1>')[0]:
                content = re.sub(
                    r'<h1>([^<]+)</h1>',
                    f'<h1 data-i18n="{i18n_key}">\\1</h1>',
                    content,
                    count=1
                )
                changes += 1
                print(f"  ✅ Added data-i18n to h1: {i18n_key}")

            # Fix category description (first p after h1)
            pattern = r'(<h1[^>]*>.*?</h1>\s*<p>)([^<]+)(</p>)'
            if re.search(pattern, content, re.DOTALL):
                content = re.sub(
                    pattern,
                    f'\\1<span data-i18n="{desc_key}">\\2</span>\\3',
                    content,
                    count=1,
                    flags=re.DOTALL
                )
                changes += 1
                print(f"  ✅ Added data-i18n to description: {desc_key}")

        # Add data-i18n to common elements
        for text, i18n_key in COMMON_TRANSLATIONS.items():
            # Match exact text in elements
            pattern = f'>({re.escape(text)})<'
            if re.search(pattern, content) and f'data-i18n="{i18n_key}"' not in content:
                # Add data-i18n attribute before the text
                content = re.sub(
                    f'(<[^>]+)>({re.escape(text)})<',
                    f'\\1 data-i18n="{i18n_key}">\\2<',
                    content,
                    count=1
                )
                changes += 1
                print(f"  ✅ Added: '{text}' -> {i18n_key}")

        # Save if changes were made
        if changes > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  💾 Saved {changes} changes")
            return True
        else:
            print(f"  ℹ️  No changes needed")
            return False

    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False

def main():
    """Main function"""
    print("=" * 70)
    print("Adding Complete Translations to All Pages")
    print("=" * 70)

    updated = 0
    total = 0

    # Process category pages
    category_dir = 'pages/categories'
    if os.path.exists(category_dir):
        for file in os.listdir(category_dir):
            if file.endswith('.html') and file.startswith('ai-'):
                file_path = os.path.join(category_dir, file)
                total += 1
                if add_translations_to_page(file_path):
                    updated += 1

    print("\n" + "=" * 70)
    print(f"✅ Updated {updated} out of {total} category pages")
    print("=" * 70)

    print("\n📝 Next: We need to add translations to i18n.js")
    print("   Then all category pages will be fully translated!")

if __name__ == '__main__':
    main()
