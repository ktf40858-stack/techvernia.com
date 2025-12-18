#!/usr/bin/env python3
"""
Trouver tous les textes visibles qui n'ont PAS de data-i18n
"""

from bs4 import BeautifulSoup
import re

def find_untranslated():
    with open('index.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    print("\n" + "="*80)
    print("🔍 TEXTES VISIBLES SANS data-i18n")
    print("="*80 + "\n")
    
    # Chercher les éléments de texte communs sans data-i18n
    selectors = [
        ('h1', 'Titres H1'),
        ('h2', 'Titres H2'),
        ('h3', 'Titres H3'),
        ('p', 'Paragraphes'),
        ('button', 'Boutons'),
        ('a.btn', 'Liens boutons'),
        ('.spotlight-badge', 'Badges'),
    ]
    
    for selector, name in selectors:
        elements = soup.select(selector)
        untranslated = []
        
        for elem in elements:
            # Ignorer si a déjà data-i18n (ou data-i18n dans un parent/enfant)
            has_i18n = (elem.get('data-i18n') or 
                       elem.find(attrs={'data-i18n': True}) or
                       any(child.get('data-i18n') for child in elem.find_all()))
            
            text = elem.get_text(strip=True)
            
            # Ignorer les vides, scripts, nombres purs
            if not has_i18n and text and len(text) > 3 and not text.isdigit():
                untranslated.append((elem.name, text[:60]))
        
        if untranslated:
            print(f"\n📌 {name} ({len(untranslated)}):")
            for tag, text in untranslated[:5]:  # Montrer les 5 premiers
                print(f"   - <{tag}>: {text}")
            if len(untranslated) > 5:
                print(f"   ... et {len(untranslated) - 5} autres")
    
    print("\n" + "="*80 + "\n")

if __name__ == "__main__":
    find_untranslated()
