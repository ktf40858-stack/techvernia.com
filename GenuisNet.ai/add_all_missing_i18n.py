#!/usr/bin/env python3
"""
Ajouter TOUS les data-i18n manquants de manière complète
"""

import re

def add_all_missing_i18n():
    print("\n" + "="*80)
    print("🔧 AJOUT COMPLET DES data-i18n MANQUANTS")
    print("="*80 + "\n")
    
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    modifications = 0
    
    # 1. Badge "AI of the Moment"
    old = r'<div class="spotlight-badge">AI of the Moment</div>'
    new = r'<div class="spotlight-badge"><span data-i18n="section.ai-of-the-moment">AI of the Moment</span></div>'
    content, count = re.subn(old, new, content)
    if count > 0:
        print(f"✅ AI of the Moment badge ({count}x)")
        modifications += count
    
    # 2. Titre "Why GenuisNet.ai?"
    old = r'<h2>Why GenuisNet\.ai\?</h2>'
    new = r'<h2><span data-i18n="section.why-genuisnetai">Why GenuisNet.ai?</span></h2>'
    content, count = re.subn(old, new, content)
    if count > 0:
        print(f"✅ Why GenuisNet.ai title ({count}x)")
        modifications += count
    
    # 3. Boutons "Read Full Review" (tous)
    old = r'(<a[^>]*class="[^"]*btn-secondary[^"]*"[^>]*>)\s*Read Full Review\s*(</a>)'
    new = r'\1<span data-i18n="btn.read-full-review">Read Full Review</span>\2'
    content, count = re.subn(old, new, content)
    if count > 0:
        print(f"✅ Read Full Review buttons ({count}x)")
        modifications += count
    
    # 4. Descriptions des cards (3 paragraphes principaux)
    cards_desc = [
        ('Handpicked AI tools across 22 categories, tested and reviewed by experts', 
         'card.handpicked-ai-tools-across-22-'),
        ('Fresh reviews and comparisons to keep you ahead in the AI revolution', 
         'card.fresh-reviews-and-comparisons-to'),
        ('In-depth analysis from beginners to enterprise solutions', 
         'card.in-depth-analysis-from-beginner'),
    ]
    
    for text, key in cards_desc:
        old = f'<p>{re.escape(text)}</p>'
        new = f'<p><span data-i18n="{key}">{text}</span></p>'
        content, count = re.subn(old, new, content)
        if count > 0:
            print(f"✅ Card: {text[:40]}... ({count}x)")
            modifications += count
    
    # 5. Descriptions des outils spotlight (paragraphes longs)
    spotlight_desc = [
        ('Claude by Anthropic represents the cutting edge',
         'section.claude-by-anthropic-represents'),
        ('The AI assistant that thinks before it speaks',
         'section.the-ai-assistant-that-thinks-be'),
        ('Midjourney has revolutionized AI art creation',
         'section.midjourney-has-revolutionized-a'),
        ('Create breathtaking art from text',
         'section.create-breathtaking-art-from-t'),
        ('Generate Hollywood-quality videos',
         'section.generate-hollywood-quality-vide'),
        ('Hollywood-quality AI video generation',
         'section.hollywood-quality-ai-video-gen'),
    ]
    
    for text_start, key in spotlight_desc:
        # Chercher le pattern avec début de texte
        pattern = rf'(<p[^>]*>)\s*{re.escape(text_start)}[^<]*(</p>)'
        # Vérifier si existe d'abord
        if re.search(pattern, content):
            # Extraire le texte complet
            match = re.search(pattern, content)
            if match:
                full_text = match.group(0)
                # Extraire juste le texte entre >...</p>
                text_content = re.search(r'>(.*?)</p>', full_text).group(1).strip()
                new = f'<p><span data-i18n="{key}">{text_content}</span></p>'
                content, count = re.subn(re.escape(full_text), new, content, count=1)
                if count > 0:
                    print(f"✅ Description: {text_start[:35]}... ({count}x)")
                    modifications += count
    
    # Sauvegarder
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n{'='*80}")
    print(f"✅ TOTAL: {modifications} modifications appliquées")
    print(f"✅ index.html mis à jour")
    print(f"{'='*80}\n")
    
    return modifications

if __name__ == "__main__":
    add_all_missing_i18n()
