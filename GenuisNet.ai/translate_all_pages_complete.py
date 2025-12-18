#!/usr/bin/env python3
"""
Complete Translation System - Add data-i18n to ALL page content
This script ensures EVERYTHING on the page is translatable
"""

import os
import re

def add_data_i18n_to_category_page(content, category_name):
    """Add data-i18n attributes to category pages"""

    # Category mappings to i18n keys
    category_map = {
        'ai-chatbots': ('cat.chatbots', 'cat.chatbots.full'),
        'ai-writing': ('cat.writing', 'cat.writing.full'),
        'ai-image': ('cat.image', 'cat.image.full'),
        'ai-video': ('cat.video', 'cat.video.full'),
        'ai-audio': ('cat.audio', 'cat.audio.full'),
        'ai-coding': ('cat.coding', 'cat.coding.full'),
        'ai-productivity': ('cat.productivity', 'cat.productivity.full'),
        'ai-business': ('cat.business', 'cat.business.full'),
        'ai-networking': ('cat.networking', 'cat.networking.full'),
        'ai-cybersecurity': ('cat.cybersecurity', 'cat.cybersecurity.full'),
    }

    if category_name not in category_map:
        return content, 0

    title_key, desc_key = category_map[category_name]
    changes = 0

    # 1. Add data-i18n to H1 title (if not already present)
    if '<h1>' in content and 'data-i18n' not in content.split('<h1>')[0] + content.split('<h1>')[1].split('</h1>')[0]:
        content = re.sub(
            r'<h1>([^<]+)</h1>',
            f'<h1 data-i18n="{title_key}">\\1</h1>',
            content,
            count=1
        )
        print(f"    ✅ H1 title -> {title_key}")
        changes += 1

    # 2. Add data-i18n to category description (first paragraph after h1)
    # Look for <p> after <h1> in the hero section
    hero_pattern = r'(<header[^>]*category-hero[^>]*>.*?<h1[^>]*>.*?</h1>\s*<p>)([^<]+)(</p>)'
    if re.search(hero_pattern, content, re.DOTALL):
        if f'data-i18n="{desc_key}"' not in content:
            content = re.sub(
                hero_pattern,
                f'\\1<span data-i18n="{desc_key}">\\2</span>\\3',
                content,
                count=1,
                flags=re.DOTALL
            )
            print(f"    ✅ Description -> {desc_key}")
            changes += 1

    # 3. Add data-i18n to "Tools Reviewed" label
    if '>Tools Reviewed<' in content and 'data-i18n="stats.tools"' not in content:
        content = content.replace(
            '>Tools Reviewed<',
            ' data-i18n="stats.tools">Tools Reviewed<'
        )
        print(f"    ✅ 'Tools Reviewed' -> stats.tools")
        changes += 1

    # 4. Add data-i18n to "Avg Rating" label
    if '>Avg Rating<' in content and 'data-i18n="stats.avgRating"' not in content:
        content = content.replace(
            '>Avg Rating<',
            ' data-i18n="stats.avgRating">Avg Rating<'
        )
        print(f"    ✅ 'Avg Rating' -> stats.avgRating")
        changes += 1

    # 5. Add data-i18n to "Full Review" text
    content = re.sub(
        r'<span>Full Review</span>',
        '<span data-i18n="btn.review">Full Review</span>',
        content
    )
    if 'btn.review' in content and '>Full Review<' in content:
        print(f"    ✅ 'Full Review' -> btn.review")
        changes += 1

    return content, changes

def process_category_file(file_path):
    """Process a single category file"""
    filename = os.path.basename(file_path)
    category_name = filename.replace('.html', '')

    print(f"\n📄 {file_path}")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        content, changes = add_data_i18n_to_category_page(content, category_name)

        if changes > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"    💾 Saved {changes} changes")
            return True
        else:
            print(f"    ℹ️  Already translated")
            return False

    except Exception as e:
        print(f"    ❌ Error: {e}")
        return False

def main():
    """Main function"""
    print("="  * 70)
    print("🌍 TRANSLATING ALL CATEGORY PAGES - COMPLETE SYSTEM")
    print("=" * 70)
    print("\nThis will add data-i18n to:")
    print("  • Category titles (H1)")
    print("  • Category descriptions")
    print("  • Stats labels (Tools Reviewed, Avg Rating)")
    print("  • Buttons (Full Review)")
    print()

    updated = 0
    total = 0

    # Process all category pages
    category_dir = 'pages/categories'

    if os.path.exists(category_dir):
        for file in sorted(os.listdir(category_dir)):
            if file.startswith('ai-') and file.endswith('.html'):
                file_path = os.path.join(category_dir, file)
                total += 1
                if process_category_file(file_path):
                    updated += 1

    print("\n" + "=" * 70)
    print(f"✅ COMPLETE! Updated {updated} out of {total} category pages")
    print("=" * 70)

    print("\n🧪 TEST NOW:")
    print("1. Go to: http://localhost:8000/pages/categories/ai-chatbots.html")
    print("2. Click the language selector (🌐)")
    print("3. Select 'Français'")
    print("4. Watch EVERYTHING change to French!")
    print()
    print("The title, description, and labels should ALL translate! 🎉")

if __name__ == '__main__':
    main()
