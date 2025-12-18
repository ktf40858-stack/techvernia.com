#!/usr/bin/env python3
"""
Supprime TOUS les doublons dans toutes les catégories
Garde les full reviews, supprime les cartes simples en double
"""

from pathlib import Path
import re

def remove_all_simple_duplicates(file_path):
    """Supprime toutes les cartes simples qui sont en double avec des full reviews."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Étape 1: Trouver tous les noms dans les cartes full review
        full_review_names = set()
        full_review_pattern = r'<article class="tool-card-full">.*?<h3>([^<]+)</h3>'
        for match in re.finditer(full_review_pattern, content, re.DOTALL):
            full_review_names.add(match.group(1).strip())

        print(f"   📋 {len(full_review_names)} full reviews trouvées")

        # Étape 2: Supprimer TOUTES les cartes simples (<article class="tool-card"> ou <a class="tool-card">)
        # qui ont le même nom qu'une full review
        removed_count = 0
        for name in full_review_names:
            # Pattern pour cartes simples (article ou a tag)
            simple_card_pattern = rf'(\s*<(?:article|a[^>]*) class="tool-card">.*?<h3>{re.escape(name)}</h3>.*?</(?:article|a)>\s*)'

            # Compter combien il y en a
            matches = list(re.finditer(simple_card_pattern, content, re.DOTALL))

            if matches:
                print(f"   🗑️  Suppression {len(matches)} doublon(s) de: {name}")
                # Supprimer tous les doublons
                for match in matches:
                    content = content.replace(match.group(0), '\n', 1)
                    removed_count += 1

        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, removed_count

        return False, 0

    except Exception as e:
        print(f"   ❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        return False, 0

def main():
    """Programme principal."""
    base_dir = Path('/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/categories')

    print("🗑️  SUPPRESSION DE TOUS LES DOUBLONS\n")

    categories = ['ai-chatbots', 'ai-writing', 'ai-coding', 'ai-image', 'ai-video',
                  'ai-audio', 'ai-productivity', 'ai-seo', 'ai-business', 'ai-networking',
                  'ai-cybersecurity', 'ai-medical', 'ai-architecture']

    total_removed = 0

    for category in categories:
        file_path = base_dir / f'{category}.html'
        if file_path.exists():
            print(f"📁 {category}")
            success, count = remove_all_simple_duplicates(file_path)
            if success:
                total_removed += count
                print(f"   ✅ {count} doublon(s) supprimé(s)\n")
            else:
                print(f"   ✓ Aucun doublon\n")

    print(f"{'='*60}")
    print(f"🎉 Terminé!")
    print(f"🗑️  Total doublons supprimés: {total_removed}")

if __name__ == '__main__':
    main()
