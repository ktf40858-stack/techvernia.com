#!/usr/bin/env python3
"""
Ajoute les icônes néon SVG dans les sections "Related Categories"
de toutes les pages de catégories
"""

import re
from pathlib import Path

# Mapping emoji -> catégorie -> SVG néon
EMOJI_TO_CATEGORY = {
    '💬': 'chatbots',
    '✍️': 'writing',
    '🎨': 'image',
    '🎬': 'video',
    '🎵': 'audio',
    '💻': 'coding',
    '⚡': 'productivity',
    '📈': 'seo',
    '💼': 'business',
    '🌐': 'networking',
    '🔒': 'cybersecurity',
}

SVG_ICONS = {
    'chatbots': '''<svg viewBox="0 0 24 24" fill="none" stroke="url(#gradient-chatbots)" stroke-width="1.5">
                            <path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>
                            <path d="M8 12h.01M12 12h.01M16 12h.01" stroke-linecap="round"/>
                        </svg>''',
    'writing': '''<svg viewBox="0 0 24 24" fill="none" stroke="url(#gradient-writing)" stroke-width="1.5">
                            <path d="M12 19l7-7 3 3-7 7-3-3z"/>
                            <path d="M18 13l-1.5-7.5L2 2l3.5 14.5L13 18l5-5z"/>
                            <path d="M2 2l7.586 7.586"/>
                            <circle cx="11" cy="11" r="2"/>
                        </svg>''',
    'image': '''<svg viewBox="0 0 24 24" fill="none" stroke="url(#gradient-image)" stroke-width="1.5">
                            <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
                            <circle cx="8.5" cy="8.5" r="1.5"/>
                            <polyline points="21 15 16 10 5 21"/>
                        </svg>''',
    'video': '''<svg viewBox="0 0 24 24" fill="none" stroke="url(#gradient-video)" stroke-width="1.5">
                            <polygon points="23 7 16 12 23 17 23 7"/>
                            <rect x="1" y="5" width="15" height="14" rx="2" ry="2"/>
                        </svg>''',
    'audio': '''<svg viewBox="0 0 24 24" fill="none" stroke="url(#gradient-audio)" stroke-width="1.5">
                            <path d="M9 18V5l12-2v13"/>
                            <circle cx="6" cy="18" r="3"/>
                            <circle cx="18" cy="16" r="3"/>
                        </svg>''',
    'coding': '''<svg viewBox="0 0 24 24" fill="none" stroke="url(#gradient-coding)" stroke-width="1.5">
                            <polyline points="16 18 22 12 16 6"/>
                            <polyline points="8 6 2 12 8 18"/>
                        </svg>''',
    'productivity': '''<svg viewBox="0 0 24 24" fill="none" stroke="url(#gradient-productivity)" stroke-width="1.5">
                            <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>
                        </svg>''',
    'seo': '''<svg viewBox="0 0 24 24" fill="none" stroke="url(#gradient-seo)" stroke-width="1.5">
                            <line x1="18" y1="20" x2="18" y2="10"/>
                            <line x1="12" y1="20" x2="12" y2="4"/>
                            <line x1="6" y1="20" x2="6" y2="14"/>
                            <path d="M3 20h18"/>
                        </svg>''',
    'business': '''<svg viewBox="0 0 24 24" fill="none" stroke="url(#gradient-business)" stroke-width="1.5">
                            <rect x="2" y="7" width="20" height="14" rx="2" ry="2"/>
                            <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>
                        </svg>''',
    'networking': '''<svg viewBox="0 0 24 24" fill="none" stroke="url(#gradient-networking)" stroke-width="1.5">
                            <rect x="9" y="9" width="6" height="6" rx="1"/>
                            <path d="M5 9a2 2 0 0 1 2-2h1"/>
                            <path d="M5 15a2 2 0 0 0 2 2h1"/>
                            <path d="M19 9a2 2 0 0 0-2-2h-1"/>
                            <path d="M19 15a2 2 0 0 1-2 2h-1"/>
                            <path d="M5 12H3"/>
                            <path d="M21 12h-2"/>
                            <path d="M12 5V3"/>
                            <path d="M12 21v-2"/>
                        </svg>''',
    'cybersecurity': '''<svg viewBox="0 0 24 24" fill="none" stroke="url(#gradient-cybersecurity)" stroke-width="1.5">
                            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                            <path d="M9 12l2 2 4-4"/>
                        </svg>''',
}

GRADIENTS_SVG = '''<!-- SVG Gradients for Neon Icons -->
            <svg width="0" height="0" style="position:absolute">
                <defs>
                    <linearGradient id="gradient-chatbots" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:#00D9FF"/>
                        <stop offset="100%" style="stop-color:#0066FF"/>
                    </linearGradient>
                    <linearGradient id="gradient-writing" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:#A855F7"/>
                        <stop offset="100%" style="stop-color:#6366F1"/>
                    </linearGradient>
                    <linearGradient id="gradient-image" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:#F472B6"/>
                        <stop offset="100%" style="stop-color:#EC4899"/>
                    </linearGradient>
                    <linearGradient id="gradient-video" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:#FB923C"/>
                        <stop offset="100%" style="stop-color:#F97316"/>
                    </linearGradient>
                    <linearGradient id="gradient-audio" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:#4ADE80"/>
                        <stop offset="100%" style="stop-color:#22C55E"/>
                    </linearGradient>
                    <linearGradient id="gradient-coding" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:#38BDF8"/>
                        <stop offset="100%" style="stop-color:#0EA5E9"/>
                    </linearGradient>
                    <linearGradient id="gradient-productivity" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:#FACC15"/>
                        <stop offset="100%" style="stop-color:#EAB308"/>
                    </linearGradient>
                    <linearGradient id="gradient-seo" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:#34D399"/>
                        <stop offset="100%" style="stop-color:#10B981"/>
                    </linearGradient>
                    <linearGradient id="gradient-business" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:#818CF8"/>
                        <stop offset="100%" style="stop-color:#6366F1"/>
                    </linearGradient>
                    <linearGradient id="gradient-networking" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:#2DD4BF"/>
                        <stop offset="100%" style="stop-color:#14B8A6"/>
                    </linearGradient>
                    <linearGradient id="gradient-cybersecurity" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:#F87171"/>
                        <stop offset="100%" style="stop-color:#EF4444"/>
                    </linearGradient>
                </defs>
            </svg>

'''

def replace_emoji_with_neon(content, emoji, category):
    """Remplace un emoji par une icône SVG néon"""
    if category not in SVG_ICONS:
        return content, False

    svg = SVG_ICONS[category]

    # Pattern pour trouver: <div class="category-icon"><span>EMOJI</span></div>
    pattern = rf'<div class="category-icon"><span>{re.escape(emoji)}</span></div>'
    replacement = f'<div class="category-icon neon-icon icon-{category}">\n                        {svg}\n                    </div>'

    new_content = content.replace(pattern, replacement)

    return new_content, (new_content != content)

def add_gradients_if_missing(content):
    """Ajoute les définitions de gradients SVG si elles ne sont pas présentes"""
    if 'SVG Gradients for Neon Icons' in content:
        return content, False

    # Chercher la section "Related Categories"
    pattern = r'(<!-- Related Categories -->.*?<div class="container">)'
    match = re.search(pattern, content, re.DOTALL)

    if match:
        replacement = match.group(1) + '\n            ' + GRADIENTS_SVG
        new_content = content.replace(match.group(1), replacement)
        return new_content, True

    return content, False

def process_file(filepath):
    """Traite un fichier HTML"""
    print(f"\n📄 Processing: {filepath.name}")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    changes = []

    # Ajouter les gradients SVG
    content, changed = add_gradients_if_missing(content)
    if changed:
        changes.append("Added SVG gradients")

    # Remplacer chaque emoji par son SVG néon
    for emoji, category in EMOJI_TO_CATEGORY.items():
        if emoji in content:
            content, changed = replace_emoji_with_neon(content, emoji, category)
            if changed:
                changes.append(f"Replaced {emoji} with neon {category} icon")

    # Sauvegarder si modifié
    if content != original_content:
        # Backup
        backup_path = str(filepath) + '.bak_neon'
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(original_content)

        # Save
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✅ Updated!")
        for change in changes:
            print(f"   - {change}")
        return True
    else:
        print("⚠️  No emoji icons found")
        return False

def main():
    """Traite toutes les pages de catégories"""
    categories_dir = Path('pages/categories')

    if not categories_dir.exists():
        print("❌ Directory not found")
        return

    html_files = list(categories_dir.glob('ai-*.html'))

    print("=" * 70)
    print("🎨 CONVERSION EMOJI → ICÔNES NÉON SVG")
    print("=" * 70)
    print(f"\nTrouvé {len(html_files)} fichiers\n")

    updated = 0
    for filepath in sorted(html_files):
        if process_file(filepath):
            updated += 1

    print("\n" + "=" * 70)
    print(f"✅ TERMINÉ! {updated}/{len(html_files)} fichiers mis à jour")
    print("=" * 70)

if __name__ == '__main__':
    main()
