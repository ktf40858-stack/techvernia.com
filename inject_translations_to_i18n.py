#!/usr/bin/env python3
"""
Script to inject all review translations into i18n.js
Adds translations for all 10 languages
"""

import os
import json
import re

LANGUAGES = ['en', 'fr', 'es', 'de', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']
I18N_FILE = "GenuisNet.ai/js/i18n.js"

def load_translations():
    """Load all translation JSON files"""

    all_translations = {}

    for lang in LANGUAGES:
        filename = f'all_reviews_translations_{lang}.json'

        if not os.path.exists(filename):
            print(f"⚠️  Missing: {filename}")
            continue

        with open(filename, 'r', encoding='utf-8') as f:
            all_translations[lang] = json.load(f)

        print(f"✅ Loaded {lang}: {len(all_translations[lang])} keys")

    return all_translations

def format_translations_for_js(translations_dict):
    """Format translations as JavaScript object properties"""

    lines = []
    for key, value in sorted(translations_dict.items()):
        # Escape quotes in value
        escaped_value = value.replace('"', '\\"')
        lines.append(f'        "{key}": "{escaped_value}",')

    return lines

def inject_into_i18n(all_translations):
    """Inject translations into i18n.js"""

    if not os.path.exists(I18N_FILE):
        print(f"❌ i18n.js not found at {I18N_FILE}")
        return False

    # Read current i18n.js
    with open(I18N_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Backup
    backup_path = I18N_FILE + '.injection_backup'
    with open(backup_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"📦 Backup created: {backup_path}")

    # For each language, find the language section and add translations
    for lang in LANGUAGES:
        if lang not in all_translations:
            continue

        translations = all_translations[lang]

        # Find the language section
        # Pattern: lang: { ... },
        lang_pattern = rf'({lang}:\s*\{{)'
        match = re.search(lang_pattern, content)

        if not match:
            print(f"⚠️  Could not find {lang} section in i18n.js")
            continue

        # Find the end of the language section (next language or end of translations)
        start_pos = match.end()

        # Find the position before the closing brace of this language section
        # We'll look for the pattern },\n or }\n at the same indentation level

        # Count braces to find the matching closing brace
        brace_count = 1
        pos = start_pos
        while pos < len(content) and brace_count > 0:
            if content[pos] == '{':
                brace_count += 1
            elif content[pos] == '}':
                brace_count -= 1
            pos += 1

        # pos is now at the position after the closing brace
        # We want to insert before the closing brace
        insert_pos = pos - 1

        # Go back to find the last comma before the closing brace
        # We'll insert our new translations right before the closing brace

        # Format the new translations
        new_lines = format_translations_for_js(translations)

        # Check if keys already exist
        existing_keys = []
        for key in translations.keys():
            if f'"{key}"' in content[match.start():insert_pos]:
                existing_keys.append(key)

        if existing_keys:
            print(f"  ℹ️  {lang}: {len(existing_keys)} keys already exist, skipping duplicates")
            # Remove existing keys
            new_lines = [line for line in new_lines if not any(f'"{key}"' in line for key in existing_keys)]

        if not new_lines:
            print(f"  ✅ {lang}: All keys already exist")
            continue

        # Insert the new translations
        new_content = '\n'.join(new_lines)

        # Add a comment before the new section
        comment = f"\n        // Review Common Sections (Auto-injected)\n"

        content = content[:insert_pos] + comment + new_content + '\n' + content[insert_pos:]

        print(f"  ✅ {lang}: Added {len(new_lines)} new keys")

    # Write the modified content
    with open(I18N_FILE, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\n✅ Translations injected into {I18N_FILE}")
    return True

def main():
    """Main execution"""

    print("="*70)
    print("  INJECTING TRANSLATIONS INTO i18n.js")
    print("="*70)

    # Load all translation files
    print("\n📂 Loading translation files...")
    all_translations = load_translations()

    if not all_translations:
        print("\n❌ No translation files found!")
        return

    # Inject into i18n.js
    print("\n💉 Injecting translations...")
    success = inject_into_i18n(all_translations)

    if success:
        print("\n" + "="*70)
        print("🎉 INJECTION COMPLETE!")
        print("="*70)
        print("\n📊 Summary:")
        for lang in LANGUAGES:
            if lang in all_translations:
                print(f"   {lang.upper()}: {len(all_translations[lang])} keys")
        print("\n✅ All review pages now support 10 languages!")
        print("="*70)
    else:
        print("\n❌ Injection failed!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
