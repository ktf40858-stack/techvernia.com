#!/usr/bin/env python3
"""
Script d'extraction des clés i18n de la page Claude
"""
from bs4 import BeautifulSoup
import json
import re

print("🔍 Extraction des clés i18n de claude.html...")

# Lire le fichier HTML
with open('GenuisNet.ai/pages/reviews/chatbots/claude.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Parser avec BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Trouver tous les éléments avec data-i18n
elements = soup.find_all(attrs={'data-i18n': True})

print(f"📊 {len(elements)} éléments avec data-i18n trouvés")

# Extraire les clés et le contenu en anglais
translations = {}
keys_found = set()

for element in elements:
    key = element.get('data-i18n')
    text = element.get_text(strip=True)

    # Nettoyer le texte (enlever les espaces multiples)
    text = re.sub(r'\s+', ' ', text)

    if key and text:
        keys_found.add(key)
        translations[key] = text

print(f"✅ {len(keys_found)} clés uniques extraites")

# Sauvegarder dans un fichier JSON
output_file = 'claude_content_to_translate.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(translations, f, indent=2, ensure_ascii=False)

print(f"💾 Sauvegardé dans: {output_file}")

# Afficher quelques exemples
print("\n📌 Exemples de clés extraites:")
for i, (key, value) in enumerate(list(translations.items())[:5]):
    preview = value[:80] + '...' if len(value) > 80 else value
    print(f"  {key}: {preview}")

print("\n" + "="*60)
print(f"✅ EXTRACTION TERMINÉE - {len(translations)} clés prêtes pour traduction")
print("="*60)
