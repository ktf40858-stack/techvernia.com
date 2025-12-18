#!/usr/bin/env python3
"""
Implémente les logos téléchargés dans le HTML (version optimisée)
"""

from pathlib import Path
import re

def scan_downloaded_logos():
    """Scanne le dossier logos et retourne un dictionnaire."""
    logos_dir = Path('/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/assets/images/logos')
    logo_map = {}

    if not logos_dir.exists():
        print("❌ Dossier logos non trouvé!")
        return logo_map

    for logo_file in logos_dir.glob('*'):
        if logo_file.is_file() and logo_file.suffix in ['.svg', '.png', '.jpg', '.ico']:
            logo_map[logo_file.stem] = logo_file.name

    print(f"✅ {len(logo_map)} logos trouvés\n")
    return logo_map

def update_logos_in_file(file_path, logo_map):
    """Met à jour les logos dans un fichier HTML."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        updated_count = 0

        # Déterminer le chemin relatif
        logo_path_prefix = '../../assets/images/logos/'

        # Pattern simple: remplacer le span emoji par img logo
        # Format: <div class="tool-logo">\n<span style="font-size: 32px;">🤖</span>\n</div>
        # Nouveau: <div class="tool-logo">\n<img src="..." alt="..." style="...">\n</div>

        # Chercher tous les blocs de tool-card
        card_pattern = r'<(article|a[^>]*) class="tool-card">(.*?)</\1>'

        def replace_logo(match):
            card_tag = match.group(1)
            card_content = match.group(2)

            # Extraire le nom de l'AI
            h3_match = re.search(r'<h3>([^<]+)</h3>', card_content)
            if not h3_match:
                return match.group(0)

            ai_name = h3_match.group(1).strip()

            # Créer le slug
            slug = ai_name.lower()
            slug = re.sub(r'[^\w\s-]', '', slug)
            slug = re.sub(r'[-\s]+', '-', slug)

            # Chercher le logo correspondant
            logo_filename = None
            if slug in logo_map:
                logo_filename = logo_map[slug]

            if logo_filename:
                # Remplacer le span emoji par img
                emoji_pattern = r'(<div class="tool-logo">\s*)<span style="font-size: 32px;">.*?</span>(\s*</div>)'
                replacement = rf'\1<img src="{logo_path_prefix}{logo_filename}" alt="{ai_name}" style="width: 48px; height: 48px; object-fit: contain;">\2'

                new_content = re.sub(emoji_pattern, replacement, card_content, count=1)

                if new_content != card_content:
                    nonlocal updated_count
                    updated_count += 1
                    print(f"   ✅ {ai_name} -> {logo_filename}")
                    return f'<{card_tag} class="tool-card">{new_content}</{card_tag.split()[0]}>'

            return match.group(0)

        content = re.sub(card_pattern, replace_logo, content, flags=re.DOTALL)

        # Sauvegarder si modifié
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, updated_count

        return False, 0

    except Exception as e:
        print(f"   ❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        return False, 0

def main():
    """Programme principal."""
    print("🎨 IMPLÉMENTATION DES LOGOS (version optimisée)\n")

    # Scanner les logos
    logo_map = scan_downloaded_logos()

    if not logo_map:
        print("Aucun logo à implémenter!")
        return

    base_dir = Path('/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/categories')

    categories = ['ai-chatbots', 'ai-writing', 'ai-coding', 'ai-image', 'ai-video',
                  'ai-audio', 'ai-productivity', 'ai-seo', 'ai-business', 'ai-networking',
                  'ai-cybersecurity', 'ai-medical', 'ai-architecture']

    total_updated = 0

    for category in categories:
        file_path = base_dir / f'{category}.html'
        if file_path.exists():
            print(f"📁 {category}")
            success, count = update_logos_in_file(file_path, logo_map)
            if success:
                total_updated += count
            print()

    print(f"{'='*60}")
    print(f"🎉 Terminé!")
    print(f"🖼️  {total_updated} logos implémentés")

if __name__ == '__main__':
    main()
