#!/usr/bin/env python3
"""
Extraction des clés de traduction de gemini.html
"""
from bs4 import BeautifulSoup
import json
import re

print("🔍 Extraction des clés de Gemini...")

# Lire le fichier HTML
with open('GenuisNet.ai/pages/reviews/chatbots/gemini.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Parser avec BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Trouver tous les éléments avec data-i18n
elements = soup.find_all(attrs={'data-i18n': True})

print(f"📊 {len(elements)} éléments trouvés avec data-i18n")

# Extraire les clés et le contenu en anglais
translations = {}
for element in elements:
    key = element.get('data-i18n')
    text = element.get_text(strip=True)
    # Nettoyer les espaces multiples
    text = re.sub(r'\s+', ' ', text)

    if key and text:
        translations[key] = text

print(f"✅ {len(translations)} clés uniques extraites")

# Sauvegarder dans un fichier JSON
with open('gemini_content_to_translate.json', 'w', encoding='utf-8') as f:
    json.dump(translations, f, indent=2, ensure_ascii=False)

print(f"💾 Sauvegardé dans gemini_content_to_translate.json")

# Afficher quelques exemples
print("\n🔍 Exemples de clés extraites:")
for i, (key, value) in enumerate(list(translations.items())[:5]):
    print(f"  {key}: {value[:60]}...")
