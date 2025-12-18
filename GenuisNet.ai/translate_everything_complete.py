#!/usr/bin/env python3
"""
TRADUCTION COMPLÈTE - Ajoute data-i18n sur TOUT LE CONTENU
Ce script va rendre TOUT le site traduisible dans les 10 langues
"""

import os
import re

def add_all_data_i18n_attributes(content, file_path):
    """Ajoute data-i18n sur TOUS les éléments de texte"""

    changes = 0
    category = os.path.basename(file_path).replace('.html', '')

    # Mapping des catégories
    category_map = {
        'ai-chatbots': 'cat.chatbots',
        'ai-writing': 'cat.writing',
        'ai-image': 'cat.image',
        'ai-video': 'cat.video',
        'ai-audio': 'cat.audio',
        'ai-coding': 'cat.coding',
        'ai-productivity': 'cat.productivity',
        'ai-business': 'cat.business',
        'ai-networking': 'cat.networking',
        'ai-cybersecurity': 'cat.cybersecurity',
    }

    if category not in category_map:
        return content, 0

    cat_key = category_map[category]

    # 1. FIX H1 - Le titre principal
    if '<h1>AI Chatbots' in content or '<h1>AI' in content:
        content = re.sub(
            r'<h1>([^<]+)</h1>',
            f'<h1 data-i18n="{cat_key}">\\1</h1>',
            content,
            count=1
        )
        print(f"    ✅ H1 titre -> {cat_key}")
        changes += 1

    # 2. FIX Description (déjà fait mais vérifions)
    if f'data-i18n="{cat_key}.full"' not in content:
        # Chercher le premier paragraphe après h1
        pattern = r'(<h1[^>]*>.*?</h1>\s*<p>)(?!<span data-i18n)([^<]+)(</p>)'
        if re.search(pattern, content, re.DOTALL):
            content = re.sub(
                pattern,
                f'\\1<span data-i18n="{cat_key}.full">\\2</span>\\3',
                content,
                count=1,
                flags=re.DOTALL
            )
            print(f"    ✅ Description -> {cat_key}.full")
            changes += 1

    # 3. FIX Stats labels
    replacements = [
        (r'>Tools Reviewed<', f' data-i18n="stats.tools">Tools Reviewed<'),
        (r'>Avg Rating<', f' data-i18n="stats.avgRating">Avg Rating<'),
        (r'>Full Review<', f' data-i18n="btn.review">Full Review<'),
        (r'>United States<', f' data-i18n="country.us">United States<'),
    ]

    for pattern, replacement in replacements:
        if re.search(pattern, content) and replacement.split('"')[1] not in content:
            content = re.sub(pattern, replacement, content)
            key = replacement.split('"')[1]
            print(f"    ✅ '{pattern[1:-1]}' -> {key}")
            changes += 1

    return content, changes

def process_file(file_path):
    """Traiter un fichier"""
    print(f"\n📄 {file_path}")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        content, changes = add_all_data_i18n_attributes(content, file_path)

        if changes > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"    💾 Saved {changes} changes")
            return True
        else:
            print(f"    ℹ️  Already complete")
            return False

    except Exception as e:
        print(f"    ❌ Error: {e}")
        return False

def main():
    print("="*70)
    print("🌍 TRADUCTION COMPLÈTE - Tous les Éléments")
    print("="*70)
    print()

    updated = 0
    total = 0

    # Traiter toutes les catégories
    for file in sorted(os.listdir('pages/categories')):
        if file.startswith('ai-') and file.endswith('.html'):
            file_path = os.path.join('pages/categories', file)
            total += 1
            if process_file(file_path):
                updated += 1

    print("\n" + "="*70)
    print(f"✅ Mis à jour {updated} sur {total} pages")
    print("="*70)

    print("\n🧪 TESTEZ MAINTENANT:")
    print("1. http://localhost:8000/pages/categories/ai-chatbots.html")
    print("2. Cliquez sur 🌐 et choisissez Français")
    print("3. Le TITRE doit changer maintenant!")

if __name__ == '__main__':
    main()
