#!/usr/bin/env python3
"""
Ajouter les data-i18n restants (approche plus simple et sûre)
"""

import re

def add_remaining_i18n():
    print("\n" + "="*80)
    print("🔧 AJOUT DES data-i18n RESTANTS")
    print("="*80 + "\n")
    
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    modifications = 0
    
    # Simple replacements - textes exacts
    replacements = [
        # Titre
        ('<h2>Why GenuisNet.ai?</h2>',
         '<h2><span data-i18n="section.why-genuisnetai">Why GenuisNet.ai?</span></h2>'),
        
        # Descriptions spotlight (textes complets)
        ('<p>The AI assistant that thinks before it speaks</p>',
         '<p><span data-i18n="section.the-ai-assistant-that-thinks-be">The AI assistant that thinks before it speaks</span></p>'),
        
        # Boutons Try (si pas déjà faits)
        ('<a class="btn-primary" href="https://claude.ai" rel="nofollow" target="_blank">Try Claude Free</a>',
         '<a class="btn-primary" href="https://claude.ai" rel="nofollow" target="_blank"><span data-i18n="btn.try-claude-free">Try Claude Free</span></a>'),
        
        ('<a class="btn-primary" href="https://chat.openai.com" rel="nofollow" target="_blank">Try ChatGPT Free</a>',
         '<a class="btn-primary" href="https://chat.openai.com" rel="nofollow" target="_blank"><span data-i18n="btn.try-chatgpt-free">Try ChatGPT Free</span></a>'),
    ]
    
    for old, new in replacements:
        count = content.count(old)
        if count > 0:
            content = content.replace(old, new)
            print(f"✅ Remplacé: {old[:50]}... ({count}x)")
            modifications += count
    
    # Sauvegarder
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n{'='*80}")
    print(f"✅ TOTAL: {modifications} modifications")
    print(f"✅ index.html mis à jour")
    print(f"{'='*80}\n")
    
    return modifications

if __name__ == "__main__":
    add_remaining_i18n()
