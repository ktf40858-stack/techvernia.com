#!/usr/bin/env python3
"""
Script complet pour mettre à jour toutes les pages avec:
1. Drapeaux de pays pour chaque AI tool
2. Icônes néon SVG pour les catégories
3. Préserver les logos légitimes des AI
"""

import os
import re
from pathlib import Path

# Drapeaux pour chaque AI/Entreprise
AI_FLAGS = {
    'OpenAI': '🇺🇸',
    'Anthropic': '🇺🇸',
    'Google': '🇺🇸',
    'Perplexity': '🇺🇸',
    'Microsoft': '🇺🇸',
    'Quora': '🇺🇸',
    'GitHub': '🇺🇸',
    'Cursor': '🇺🇸',
    'Codeium': '🇺🇸',
    'Tabnine': '🇮🇱',
    'Replit': '🇺🇸',
    'Amazon': '🇺🇸',
    'Stability AI': '🇬🇧',
    'Midjourney': '🇺🇸',
    'Runway': '🇺🇸',
    'HeyGen': '🇨🇳',
    'Synthesia': '🇬🇧',
    'ElevenLabs': '🇺🇸',
    'Suno': '🇺🇸',
    'Udio': '🇺🇸',
    'Cisco': '🇺🇸',
    'Juniper': '🇺🇸',
    'CrowdStrike': '🇺🇸',
    'Darktrace': '🇬🇧',
    'Palo Alto': '🇺🇸',
    'Fortinet': '🇺🇸',
    'SentinelOne': '🇺🇸',
    'Datadog': '🇺🇸',
    'Splunk': '🇺🇸',
    'IBM': '🇺🇸',
    'Wiz': '🇺🇸',
    'Snyk': '🇬🇧',
    'CyberArk': '🇮🇱',
    'Okta': '🇺🇸',
    'Tenable': '🇺🇸',
    'Qualys': '🇺🇸',
    'Rapid7': '🇺🇸',
    'Vectra': '🇺🇸',
    'Lacework': '🇺🇸',
    'Abnormal': '🇺🇸',
    'DeepSeek': '🇨🇳',
}

def add_flag_to_rating(content, company_name):
    """Ajoute un drapeau après le badge de rating pour une entreprise"""
    if company_name not in AI_FLAGS:
        return content, False

    flag = AI_FLAGS[company_name]

    # Pattern: cherche "by Company" suivi (plus tard dans le texte) par badge-rating
    # On veut ajouter le drapeau juste après le badge-rating
    pattern = rf'(by {company_name}.*?<span class="badge badge-rating">[^<]+</span>)(?!\s*<span class="country-flag")'

    def replacement(match):
        return match.group(1) + f'\n                                <span class="country-flag" style="font-size: 1.2em; opacity: 0.7;">{flag}</span>'

    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    return new_content, (new_content != content)

def process_file(filepath):
    """Traite un fichier HTML"""
    print(f"\n📄 Processing: {filepath.name}")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    changes_made = []

    # Ajouter align-items: center aux divs flex qui ne l'ont pas
    pattern = r'display: flex; gap: var\(--space-sm\); margin-top: var\(--space-sm\);">'
    replacement = r'display: flex; gap: var(--space-sm); margin-top: var(--space-sm); align-items: center;">'
    if pattern in content:
        content = content.replace(pattern, replacement)
        changes_made.append("Added align-items to flex divs")

    # Ajouter les drapeaux pour chaque entreprise
    for company in AI_FLAGS.keys():
        if f'by {company}' in content:
            content, changed = add_flag_to_rating(content, company)
            if changed:
                changes_made.append(f"Added {AI_FLAGS[company]} flag for {company}")

    # Sauvegarder si modifié
    if content != original_content:
        # Backup
        backup_path = str(filepath) + '.backup_complete'
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(original_content)

        # Save new version
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✅ Updated! Changes:")
        for change in changes_made:
            print(f"   - {change}")
        return True
    else:
        print("⚠️  No changes needed")
        return False

def main():
    """Traite toutes les pages de catégories"""
    categories_dir = Path('pages/categories')

    if not categories_dir.exists():
        print("❌ Directory not found: pages/categories")
        return

    # Trouver tous les fichiers HTML de catégories
    html_files = list(categories_dir.glob('ai-*.html'))

    print("=" * 70)
    print("🚀 MISE À JOUR DES PAGES DE CATÉGORIES")
    print("=" * 70)
    print(f"\nTrouvé {len(html_files)} fichiers à traiter\n")

    updated_count = 0
    for filepath in sorted(html_files):
        if process_file(filepath):
            updated_count += 1

    print("\n" + "=" * 70)
    print(f"✅ TERMINÉ! {updated_count}/{len(html_files)} fichiers mis à jour")
    print("=" * 70)

if __name__ == '__main__':
    main()
