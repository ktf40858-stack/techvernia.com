#!/usr/bin/env python3
"""
Ajouter les data-i18n manquants - Correction rapide
"""

import re

def fix_missing_i18n():
    print("\n" + "="*80)
    print("🔧 AJOUT DES data-i18n MANQUANTS")
    print("="*80 + "\n")
    
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    modifications = 0
    
    # CTA Section - Ready to Discover
    old = r'<h2>Ready to Discover Your Perfect AI Tool\?</h2>'
    new = r'<h2><span data-i18n="btn.ready-to-discover-your-perfect">Ready to Discover Your Perfect AI Tool?</span></h2>'
    content, count = re.subn(old, new, content)
    if count > 0:
        print(f"✅ Added: btn.ready-to-discover-your-perfect ({count}x)")
        modifications += count
    
    # CTA Section - Explore 116+
    old = r'<p>Explore 116\+ carefully curated tools across 22 categories</p>'
    new = r'<p><span data-i18n="btn.explore-116-carefully-curated-">Explore 116+ carefully curated tools across 22 categories</span></p>'
    content, count = re.subn(old, new, content)
    if count > 0:
        print(f"✅ Added: btn.explore-116-carefully-curated- ({count}x)")
        modifications += count
    
    # Fix data-text for glitch effect
    old = r'data-text="Discover the Future of AI"'
    new = r'data-text="Discover the Future of AI Tools" data-i18n-text="hero.discover-the-future-of-ai"'
    content, count = re.subn(old, new, content)
    if count > 0:
        print(f"✅ Added: data-i18n-text for glitch effect ({count}x)")
        modifications += count
    
    # Save
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n✅ {modifications} modifications appliquées")
    print(f"✅ index.html mis à jour\n")
    print("="*80)
    print("✅ CORRECTION TERMINÉE")
    print("="*80 + "\n")
    
    return modifications

if __name__ == "__main__":
    fix_missing_i18n()
