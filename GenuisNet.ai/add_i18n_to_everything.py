#!/usr/bin/env python3
"""
Ajouter data-i18n sur TOUS les éléments de texte du site
Et générer automatiquement les traductions
"""

import os
import re
from bs4 import BeautifulSoup, NavigableString
import json
import hashlib

# Noms d'outils à ne JAMAIS traduire
PRESERVE_NAMES = [
    'ChatGPT', 'Claude', 'Gemini', 'GPT-4', 'GPT-3.5', 'Midjourney',
    'DALL-E', 'Copilot', 'Perplexity', 'Stable Diffusion', 'Leonardo AI',
    'Ideogram', 'Runway', 'Pika', 'Tableau', 'Looker', 'Salesforce Einstein',
    'HubSpot AI', 'GitHub Copilot', 'Amazon Q', 'Tabnine', 'Replit',
    'CrowdStrike', 'Darktrace', 'Splunk', 'Cortex', 'SentinelOne'
]

# Traductions communes pré-définies
COMMON_TRANSLATIONS = {
    'Try': {'fr': 'Essayer', 'es': 'Probar', 'de': 'Testen', 'pt': 'Experimentar'},
    'Try Free': {'fr': 'Essayer Gratuitement', 'es': 'Probar Gratis', 'de': 'Kostenlos Testen'},
    'Try for free': {'fr': 'Essayer gratuitement', 'es': 'Probar gratis', 'de': 'Kostenlos testen'},
    'Try Now': {'fr': 'Essayer Maintenant', 'es': 'Probar Ahora', 'de': 'Jetzt Testen'},
    'Get Started': {'fr': 'Commencer', 'es': 'Comenzar', 'de': 'Erste Schritte'},
    'Learn More': {'fr': 'En savoir plus', 'es': 'Saber más', 'de': 'Mehr erfahren'},
    'Read Review': {'fr': 'Lire l\'Avis', 'es': 'Leer Reseña', 'de': 'Rezension lesen'},
    'Full Review': {'fr': 'Avis Complet', 'es': 'Reseña Completa', 'de': 'Vollständige Rezension'},
    'Features': {'fr': 'Fonctionnalités', 'es': 'Características', 'de': 'Funktionen'},
    'Pricing': {'fr': 'Tarifs', 'es': 'Precios', 'de': 'Preise'},
    'Overview': {'fr': 'Aperçu', 'es': 'Descripción', 'de': 'Übersicht'},
    'Popular': {'fr': 'Populaire', 'es': 'Popular', 'de': 'Beliebt'},
    'New': {'fr': 'Nouveau', 'es': 'Nuevo', 'de': 'Neu'},
    'Free': {'fr': 'Gratuit', 'es': 'Gratis', 'de': 'Kostenlos'},
    'Premium': {'fr': 'Premium', 'es': 'Premium', 'de': 'Premium'},
    'for free': {'fr': 'gratuitement', 'es': 'gratis', 'de': 'kostenlos'},
}

# Dictionnaire pour stocker toutes les traductions à générer
all_translations = {}
translation_counter = 0

def should_preserve(text):
    """Vérifier si le texte doit être préservé (noms d'outils)"""
    text_clean = text.strip()
    for name in PRESERVE_NAMES:
        if name.lower() in text_clean.lower():
            return True
    return False

def generate_translation_key(text):
    """Générer une clé de traduction unique"""
    global translation_counter

    # Nettoyer le texte
    clean = re.sub(r'\s+', ' ', text.strip())

    # Si traduction commune existe, utiliser cette clé
    if clean in COMMON_TRANSLATIONS:
        return f"common.{clean.lower().replace(' ', '_')}"

    # Créer une clé basée sur les premiers mots
    words = clean.split()[:3]
    if words:
        key_base = '_'.join([w.lower() for w in words if w.isalnum()])[:30]
        translation_counter += 1
        return f"auto.{key_base}_{translation_counter}"

    translation_counter += 1
    return f"auto.text_{translation_counter}"

def add_i18n_to_element(element, soup):
    """Ajouter data-i18n à un élément si nécessaire"""

    # Ignorer si déjà a data-i18n
    if element.has_attr('data-i18n'):
        return False

    # Ignorer certains éléments
    if element.name in ['script', 'style', 'svg', 'path', 'code', 'pre']:
        return False

    # Ignorer si contient des enfants avec data-i18n
    if element.find(attrs={'data-i18n': True}):
        return False

    # Obtenir le texte direct (sans enfants)
    direct_text = ''
    for child in element.children:
        if isinstance(child, NavigableString):
            direct_text += str(child)

    direct_text = direct_text.strip()

    # Ignorer si vide ou trop court
    if not direct_text or len(direct_text) < 2:
        return False

    # Ignorer si c'est juste des nombres ou symboles
    if re.match(r'^[\d\s\.\,\★\-]+$', direct_text):
        return False

    # Ignorer si doit être préservé
    if should_preserve(direct_text):
        return False

    # Générer une clé et ajouter data-i18n
    key = generate_translation_key(direct_text)
    element['data-i18n'] = key

    # Stocker la traduction
    all_translations[key] = direct_text

    return True

def process_html_file(file_path):
    """Traiter un fichier HTML"""
    print(f"\n📄 {file_path}")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        soup = BeautifulSoup(content, 'html.parser')
        changes = 0

        # Éléments à traiter
        elements_to_process = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'li', 'span', 'a', 'button', 'div'])

        for element in elements_to_process:
            if add_i18n_to_element(element, soup):
                changes += 1

        if changes > 0:
            # Sauvegarder
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))

            print(f"    ✅ {changes} attributs data-i18n ajoutés")
            return changes
        else:
            print(f"    ℹ️  Aucun changement")
            return 0

    except Exception as e:
        print(f"    ❌ Erreur: {e}")
        return 0

def main():
    print("="*70)
    print("🌍 AJOUT DE data-i18n SUR TOUT LE SITE")
    print("="*70)
    print()

    total_files = 0
    total_changes = 0

    # Traiter index.html
    if os.path.exists('index.html'):
        total_files += 1
        total_changes += process_html_file('index.html')

    # Traiter toutes les pages
    for root, dirs, files in os.walk('pages'):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                total_files += 1
                total_changes += process_html_file(file_path)

    print("\n" + "="*70)
    print(f"✅ {total_changes} attributs ajoutés sur {total_files} fichiers")
    print(f"📝 {len(all_translations)} traductions uniques à ajouter")
    print("="*70)

    # Sauvegarder les traductions à ajouter
    output_file = 'translations_to_add.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_translations, f, ensure_ascii=False, indent=2)

    print(f"\n💾 Traductions sauvegardées dans: {output_file}")
    print("\n📋 PROCHAINE ÉTAPE:")
    print("   Utiliser ce fichier pour générer les traductions dans toutes les langues")

if __name__ == '__main__':
    main()
