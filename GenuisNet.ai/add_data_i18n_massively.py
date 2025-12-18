#!/usr/bin/env python3
"""
Ajouter data-i18n MASSIVEMENT sur tous les éléments de texte
Ce script va rendre TOUT traduisible en ajoutant des attributs data-i18n partout
"""

import os
import re
from bs4 import BeautifulSoup
import hashlib

def generate_key(text):
    """Générer une clé unique pour un texte"""
    # Nettoyer le texte
    clean = re.sub(r'\s+', ' ', text.strip())
    # Créer une clé basée sur le contenu
    hash_part = hashlib.md5(clean.encode()).hexdigest()[:8]
    # Créer une clé lisible
    words = clean.split()[:3]
    if words:
        key_words = '_'.join([w.lower() for w in words if w.isalnum()])[:30]
        return f"auto.{key_words}_{hash_part}"
    return f"auto.text_{hash_part}"

def add_data_i18n_to_html(file_path):
    """Ajoute data-i18n à tous les éléments de texte significatifs"""

    print(f"\n📄 {file_path}")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        soup = BeautifulSoup(content, 'html.parser')
        changes = 0
        translations_needed = {}

        # Éléments à traiter
        text_elements = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'li', 'span', 'div'])

        for elem in text_elements:
            # Ignorer si déjà a data-i18n
            if elem.get('data-i18n'):
                continue

            # Ignorer si c'est un conteneur (a des enfants avec data-i18n)
            if elem.find(attrs={'data-i18n': True}):
                continue

            # Ignorer les éléments vides ou avec juste des espaces
            text = elem.get_text(strip=True)
            if not text or len(text) < 3:
                continue

            # Ignorer si c'est juste un nombre ou des symboles
            if text.replace('.', '').replace(',', '').replace('★', '').strip().isdigit():
                continue

            # Ignorer les noms d'outils connus (ChatGPT, Claude, etc.)
            tool_names = ['chatgpt', 'claude', 'gemini', 'copilot', 'midjourney', 'dall-e', 'perplexity']
            if text.lower() in tool_names:
                continue

            # Vérifier si c'est un élément de texte direct (pas juste un conteneur)
            direct_text = ''.join([str(c) for c in elem.contents if isinstance(c, str)]).strip()
            if not direct_text and len(text) > 50:
                continue  # C'est un conteneur

            # Générer une clé
            key = generate_key(text)

            # Ajouter data-i18n
            elem['data-i18n'] = key
            translations_needed[key] = text
            changes += 1

        if changes > 0:
            # Sauvegarder le HTML modifié
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))

            # Sauvegarder les traductions nécessaires
            trans_file = file_path.replace('.html', '_translations.txt')
            with open(trans_file, 'w', encoding='utf-8') as f:
                for key, text in translations_needed.items():
                    f.write(f'"{key}": "{text}",\n')

            print(f"    ✅ {changes} éléments avec data-i18n ajoutés")
            print(f"    📝 Traductions sauvegardées dans {trans_file}")
            return True
        else:
            print(f"    ℹ️  Aucun élément à ajouter")
            return False

    except Exception as e:
        print(f"    ❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    print("="*70)
    print("🌍 AJOUT MASSIF DE data-i18n")
    print("="*70)
    print()
    print("⚠️  ATTENTION: Cette approche va créer BEAUCOUP de clés")
    print("⚠️  Solution alternative recommandée ci-dessous")
    print()

    # Ne traiter qu'UNE page pour test
    test_file = 'pages/categories/ai-chatbots.html'

    if os.path.exists(test_file):
        add_data_i18n_to_html(test_file)

    print("\n" + "="*70)
    print("❌ PROBLÈME AVEC CETTE APPROCHE:")
    print("   - Crée des centaines de clés de traduction")
    print("   - Difficile à maintenir")
    print("   - Nécessite de traduire manuellement chaque clé")
    print()
    print("✅ MEILLEURE SOLUTION:")
    print("   Utiliser Google Translate Widget!")
    print("="*70)

if __name__ == '__main__':
    main()
