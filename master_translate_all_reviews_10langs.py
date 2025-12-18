#!/usr/bin/env python3
"""
MASTER SCRIPT: Traduction complète de 255 pages × 10 langues
Version optimisée avec dictionnaire de traduction
"""

import os
import re
import json
from pathlib import Path
from translation_dictionaries import get_all_translations_for_text, TRANSLATIONS

LANGUAGES = ['en', 'fr', 'es', 'de', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']

def clean_text(text):
    """Clean text"""
    return ' '.join(text.split()).strip()

def text_to_key(text, max_length=40):
    """Convert text to i18n key"""
    key = clean_text(text)[:max_length].lower()
    key = re.sub(r'[^a-z0-9\s-]', '', key)
    key = re.sub(r'\s+', '.', key).strip('.')
    return key

def process_common_sections(html_content, tool_name):
    """Process common sections that appear in all reviews"""

    translations = {lang: {} for lang in LANGUAGES}
    modifications = []
    count = 0

    # Find all H2 section titles
    h2_pattern = r'<h2[^>]*>([^<]+)</h2>'
    h2_matches = re.finditer(h2_pattern, html_content)

    for match in h2_matches:
        section_text = clean_text(match.group(1))

        # Skip if already has data-i18n
        if 'data-i18n' in html_content[max(0, match.start()-100):match.start()]:
            continue

        # Check if it's a common term
        if section_text in TRANSLATIONS:
            # Use common key
            key = f"review.common.{text_to_key(section_text)}"

            # Get all translations
            all_trans = get_all_translations_for_text(section_text)
            for lang in LANGUAGES:
                translations[lang][key] = all_trans[lang]

            modifications.append({
                'type': 'h2',
                'text': section_text,
                'key': key,
                'position': match.start()
            })
            count += 1

    print(f"  📊 Found {count} common sections")
    return translations, modifications

def apply_i18n_to_html(html_path, modifications):
    """Apply i18n modifications to HTML"""

    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    modified_count = 0

    # Sort by position (reverse) to maintain positions
    mods_sorted = sorted(modifications, key=lambda x: x['position'], reverse=True)

    for mod in mods_sorted:
        if mod['type'] == 'h2':
            # Find exact position
            pattern = f"<h2[^>]*>{re.escape(mod['text'])}</h2>"
            replacement = f'<h2><span data-i18n="{mod["key"]}">{mod["text"]}</span></h2>'

            if re.search(pattern, content):
                content = re.sub(pattern, replacement, content, count=1)
                modified_count += 1

    if content != original:
        # Backup
        backup = html_path + '.i18n10_backup'
        if not os.path.exists(backup):
            with open(backup, 'w', encoding='utf-8') as f:
                f.write(original)

        # Save modified
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(content)

        return modified_count
    return 0

def process_category(category_name, category_dir):
    """Process all pages in a category"""

    review_path = f"GenuisNet.ai/pages/reviews/{category_dir}"

    if not os.path.exists(review_path):
        print(f"⚠️  Directory not found: {review_path}")
        return None

    print(f"\n{'='*70}")
    print(f"📁 CATEGORY: {category_name.upper()}")
    print(f"{'='*70}")

    category_translations = {lang: {} for lang in LANGUAGES}
    total_files = 0
    total_modified = 0

    for filename in sorted(os.listdir(review_path)):
        if not filename.endswith('.html') or 'backup' in filename:
            continue

        tool_name = Path(filename).stem
        html_path = os.path.join(review_path, filename)

        print(f"\n📄 {tool_name}")

        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if already heavily translated
        existing_count = content.count('data-i18n=')
        if existing_count > 50:
            print(f"  ✅ Already translated ({existing_count} attributes)")
            total_files += 1
            continue

        # Process common sections
        translations, modifications = process_common_sections(content, tool_name)

        if modifications:
            # Merge translations
            for lang in LANGUAGES:
                category_translations[lang].update(translations[lang])

            # Apply modifications
            mod_count = apply_i18n_to_html(html_path, modifications)
            if mod_count > 0:
                print(f"  ✅ Added {mod_count} i18n attributes")
                total_modified += 1
        else:
            print(f"  ℹ️  No modifications needed")

        total_files += 1

    print(f"\n{'─'*70}")
    print(f"📊 Category Summary: {total_modified}/{total_files} files modified")
    print(f"{'─'*70}")

    return category_translations

def main():
    """Main execution"""

    print("🌐 " + "="*68)
    print("   MASTER TRANSLATION SCRIPT - 10 LANGUAGES")
    print("   Processing 255 review pages")
    print("="*70)

    categories = [
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

    # Global translations dictionary
    global_translations = {lang: {} for lang in LANGUAGES}
    total_categories = 0
    total_keys = 0

    for cat_name, cat_dir in categories:
        cat_trans = process_category(cat_name, cat_dir)

        if cat_trans:
            # Merge into global
            for lang in LANGUAGES:
                global_translations[lang].update(cat_trans[lang])
            total_categories += 1

    # Count unique keys
    total_keys = len(global_translations['en'])

    # Save translation files for each language
    print(f"\n{'='*70}")
    print("💾 SAVING TRANSLATION FILES")
    print(f"{'='*70}")

    for lang in LANGUAGES:
        filename = f'all_reviews_translations_{lang}.json'
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(global_translations[lang], f, indent=2, ensure_ascii=False)
        print(f"  ✅ {lang.upper()}: {len(global_translations[lang])} keys → {filename}")

    print(f"\n{'='*70}")
    print("🎉 TRANSLATION COMPLETE!")
    print(f"{'='*70}")
    print(f"📊 Statistics:")
    print(f"   - Categories processed: {total_categories}")
    print(f"   - Unique translation keys: {total_keys}")
    print(f"   - Languages: {len(LANGUAGES)}")
    print(f"   - Total translations: {total_keys * len(LANGUAGES):,}")
    print(f"{'='*70}")

    print(f"\n📌 Next Step:")
    print(f"   Run: python3 inject_translations_to_i18n.py")
    print(f"   This will add all translations to i18n.js")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
