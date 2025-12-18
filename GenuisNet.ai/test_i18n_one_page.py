#!/usr/bin/env python3
"""
TEST: Ajouter data-i18n sur UNE SEULE page pour tester
"""

import os
import re
from bs4 import BeautifulSoup, NavigableString
import json

# Page de test
TEST_PAGE = 'pages/categories/ai-chatbots.html'

# Noms à préserver
PRESERVE_NAMES = [
    'ChatGPT', 'Claude', 'Gemini', 'GPT-4', 'Midjourney', 'DALL-E',
    'Copilot', 'Perplexity', 'Stable Diffusion'
]

# Traductions communes
COMMON_TRANSLATIONS = {
    'Try': 'common.try',
    'Try Free': 'common.try_free',
    'Try for free': 'common.try_for_free',
    'Features': 'common.features',
    'Pricing': 'common.pricing',
    'for free': 'common.for_free',
}

translation_counter = 0
all_translations = {}

def should_preserve(text):
    """Vérifier si le texte contient un nom à préserver"""
    text_clean = text.strip()
    for name in PRESERVE_NAMES:
        if name in text_clean:
            return True
    return False

def generate_key(text):
    """Générer une clé de traduction"""
    global translation_counter

    clean = re.sub(r'\s+', ' ', text.strip())

    # Utiliser clé commune si existe
    if clean in COMMON_TRANSLATIONS:
        return COMMON_TRANSLATIONS[clean]

    # Sinon générer une nouvelle clé
    translation_counter += 1
    words = clean.split()[:3]
    if words:
        key_base = '_'.join([w.lower() for w in words if w.isalnum()])[:25]
        return f"auto.{key_base}_{translation_counter}"

    return f"auto.text_{translation_counter}"

def process_element(element):
    """Traiter un élément"""
    # Ignorer si déjà traduit
    if element.has_attr('data-i18n'):
        return False

    # Ignorer certains tags
    if element.name in ['script', 'style', 'svg', 'code', 'pre', 'img', 'br', 'hr']:
        return False

    # Obtenir le texte direct uniquement
    direct_text = ''
    for child in element.children:
        if isinstance(child, NavigableString):
            direct_text += str(child)

    direct_text = direct_text.strip()

    # Ignorer si vide, trop court, ou juste des chiffres
    if not direct_text or len(direct_text) < 2:
        return False

    if re.match(r'^[\d\s\.\,\★\-]+$', direct_text):
        return False

    # Ignorer si contient un nom à préserver
    if should_preserve(direct_text):
        print(f"    ⏭️  Préservé: {direct_text}")
        return False

    # Ajouter data-i18n
    key = generate_key(direct_text)
    element['data-i18n'] = key
    all_translations[key] = direct_text

    print(f"    ✅ Ajouté: '{direct_text}' -> {key}")
    return True

def main():
    print("="*70)
    print("🧪 TEST: Ajout data-i18n sur une page")
    print("="*70)
    print()

    if not os.path.exists(TEST_PAGE):
        print(f"❌ Fichier non trouvé: {TEST_PAGE}")
        return

    # Faire une sauvegarde
    backup_file = TEST_PAGE + '.backup'
    with open(TEST_PAGE, 'r', encoding='utf-8') as f:
        content = f.read()
    with open(backup_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"💾 Sauvegarde créée: {backup_file}")
    print()

    # Traiter le fichier
    print(f"📄 Traitement de: {TEST_PAGE}")
    print()

    soup = BeautifulSoup(content, 'html.parser')
    changes = 0

    # Traiter tous les éléments de texte potentiels
    for element in soup.find_all(['span', 'p', 'h1', 'h2', 'h3', 'h4', 'a', 'button', 'li', 'div']):
        if process_element(element):
            changes += 1

    print()
    print(f"✅ Total: {changes} attributs data-i18n ajoutés")
    print()

    # Sauvegarder le HTML modifié
    with open(TEST_PAGE, 'w', encoding='utf-8') as f:
        f.write(str(soup))

    print(f"💾 Fichier mis à jour: {TEST_PAGE}")
    print()

    # Sauvegarder les traductions
    with open('test_translations.json', 'w', encoding='utf-8') as f:
        json.dump(all_translations, f, ensure_ascii=False, indent=2)

    print(f"📝 {len(all_translations)} traductions à ajouter")
    print(f"💾 Liste sauvegardée dans: test_translations.json")
    print()
    print("🧪 TESTEZ MAINTENANT:")
    print(f"   1. Ouvrez: http://localhost:8000/{TEST_PAGE}")
    print("   2. Changez la langue")
    print("   3. Vérifiez si TOUT change (sauf noms d'outils)")
    print()
    print("⚠️  Si ça ne marche pas, restaurez avec:")
    print(f"   cp {backup_file} {TEST_PAGE}")

if __name__ == '__main__':
    main()
