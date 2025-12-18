#!/usr/bin/env python3
"""
Corriger la fonction apply pour inclure les clés communes
"""
import re

tools = [
    'adobe-firefly',
    'canva-ai',
    'clipdrop',
    'dall-e-3',
    'ideogram',
    'leonardo-ai',
    'midjourney',
    'stable-diffusion'
]

print("=" * 80)
print("🔧 CORRECTION DES FONCTIONS APPLY")
print("=" * 80)
print()

for tool in tools:
    i18n_file = f'GenuisNet.ai/js/{tool}-i18n.js'
    print(f"🔧 {tool}-i18n.js")

    with open(i18n_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to find the line that filters keys
    # Before: if (key && key.startsWith('review.adobe-firefly.')) {
    # After: if (key && (key.startsWith('review.adobe-firefly.') || key.startsWith('review.common.'))) {

    # Escape special regex characters, but tool name will be inserted as-is
    old_pattern = rf"if \(key && key\.startsWith\('review\.{re.escape(tool)}\.'\)\) \{{"
    new_pattern = f"if (key && (key.startsWith('review.{tool}.') || key.startsWith('review.common.'))) {{"

    new_content = re.sub(old_pattern, new_pattern, content)

    if new_content != content:
        with open(i18n_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  ✅ Fonction apply corrigée")
    else:
        print(f"  ℹ️  Déjà corrigé ou pattern non trouvé")

print()
print("=" * 80)
print("✅ TOUTES LES FONCTIONS APPLY ONT ÉTÉ CORRIGÉES!")
print("=" * 80)
