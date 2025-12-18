#!/usr/bin/env python3
"""
ÉTAPE 1: Génération des traductions (contenu + FAQ) - SANS INTÉGRATION
Usage: python3 step1_generate_translations.py <category>
Exemple: python3 step1_generate_translations.py image

Ce script va:
1. Extraire les FAQ des fichiers HTML
2. Ajouter data-i18n aux FAQ
3. Extraire le contenu existant de i18n.js
4. Générer les traductions en 9 langues
5. Sauvegarder dans {category}_translations.json

PUIS vous pourrez vérifier le fichier JSON avant l'étape 2 (intégration)
"""

import sys
import os
import json
import re
from bs4 import BeautifulSoup, NavigableString
import subprocess

def log(message):
    """Afficher un message avec formatage"""
    print(f"[STEP 1] {message}")

def get_tools_in_category(category):
    """Obtenir la liste des outils HTML dans une catégorie"""
    category_path = f"GenuisNet.ai/pages/reviews/{category}"
    if not os.path.exists(category_path):
        log(f"❌ Catégorie {category} non trouvée dans {category_path}")
        return []

    html_files = [f.replace('.html', '') for f in os.listdir(category_path)
                  if f.endswith('.html') and not f.startswith('.') and '.backup' not in f]

    log(f"✓ Trouvé {len(html_files)} outils dans {category}")
    return html_files

def extract_faqs_from_html(category, tools):
    """Extraire toutes les FAQ des fichiers HTML"""
    all_faqs = {}

    for tool in tools:
        html_file = f"GenuisNet.ai/pages/reviews/{category}/{tool}.html"

        if not os.path.exists(html_file):
            continue

        with open(html_file, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')

        faq_items = soup.find_all('div', class_='faq-item')
        faqs = []

        for i, item in enumerate(faq_items, 1):
            question_div = item.find('div', class_='faq-question')
            answer_div = item.find('div', class_='faq-answer')

            if question_div and answer_div:
                q_text = ""
                for content in question_div.contents:
                    if isinstance(content, NavigableString):
                        q_text += str(content).strip()

                a_text = answer_div.get_text().strip()

                if q_text and a_text:
                    faqs.append({
                        'number': i,
                        'question': q_text,
                        'answer': a_text
                    })

        if faqs:
            all_faqs[tool] = faqs
            log(f"  {tool}: {len(faqs)} FAQ extraites")

    return all_faqs

def add_data_i18n_to_faqs(category, tools, all_faqs):
    """Ajouter data-i18n aux FAQ dans les HTML"""

    for tool in tools:
        if tool not in all_faqs or not all_faqs[tool]:
            continue

        html_file = f"GenuisNet.ai/pages/reviews/{category}/{tool}.html"

        with open(html_file, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')

        faq_items = soup.find_all('div', class_='faq-item')
        # IMPORTANT: Garder les tirets dans le nom de l'outil!
        tool_key = tool  # Ne PAS enlever les tirets

        for i, item in enumerate(faq_items):
            if i >= len(all_faqs[tool]):
                break

            faq_num = i + 1
            question_div = item.find('div', class_='faq-question')
            answer_div = item.find('div', class_='faq-answer')

            if question_div and answer_div:
                # Question
                q_text = ""
                plus_span = None
                for content in list(question_div.contents):
                    if isinstance(content, NavigableString):
                        q_text += str(content).strip()
                    elif content.name == 'span':
                        plus_span = content

                new_q_span = soup.new_tag('span')
                new_q_span['data-i18n'] = f'review.{tool_key}.faq{faq_num}.question'
                new_q_span.string = q_text

                question_div.clear()
                question_div.append(new_q_span)
                if plus_span:
                    question_div.append(plus_span)
                else:
                    plus_span = soup.new_tag('span')
                    plus_span.string = '+'
                    question_div.append(plus_span)

                # Answer
                a_text = answer_div.get_text().strip()
                new_a_span = soup.new_tag('span')
                new_a_span['data-i18n'] = f'review.{tool_key}.faq{faq_num}.answer'
                new_a_span.string = a_text

                answer_div.clear()
                answer_div.append(new_a_span)

        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(str(soup))

        log(f"  {tool}: data-i18n ajouté aux FAQ")

def extract_content_from_i18n(tools):
    """Extraire le contenu existant dans i18n.js EN pour ces outils"""

    with open('GenuisNet.ai/js/i18n.js', 'r', encoding='utf-8') as f:
        content = f.read()

    en_match = re.search(r'en:\s*\{(.*?)\n\s*\},\s*\n\s*// ==+ FRENCH', content, re.DOTALL)

    if not en_match:
        log("❌ Section EN non trouvée")
        return {}

    en_section = en_match.group(1)
    # Regex améliorée pour gérer les guillemets échappés dans les valeurs
    pattern = r'"(review\.[^"]+)":\s*"((?:[^"\\]|\\.)*)"'

    content_dict = {}

    for match in re.finditer(pattern, en_section):
        key = match.group(1)
        value = match.group(2)

        # Vérifier si c'est une clé pour un des outils (et pas FAQ)
        for tool in tools:
            # IMPORTANT: Garder les tirets dans le nom de l'outil!
            tool_key = tool  # Ne PAS enlever les tirets
            if key.startswith(f'review.{tool_key}') and '.faq' not in key:
                value_decoded = value.replace('\\"', '"')
                value_decoded = value_decoded.replace("\\'", "'")
                value_decoded = value_decoded.replace('\\\\', '\\')
                content_dict[key] = value_decoded
                break

    log(f"✓ {len(content_dict)} clés de contenu extraites de i18n.js EN")
    return content_dict

def generate_translations(all_data, category):
    """Générer toutes les traductions avec argostranslate"""

    log("Génération des traductions (cela peut prendre plusieurs minutes)...")

    # Créer un fichier temporaire pour le script de traduction
    translate_script = f"""
import json
import argostranslate.package
import argostranslate.translate

with open('/tmp/{category}_all_data.json', 'r', encoding='utf-8') as f:
    all_data = json.load(f)

target_langs = ['es', 'fr', 'de', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']

def translate_text(text, target_lang):
    try:
        installed_languages = argostranslate.translate.get_installed_languages()
        from_lang = next((lang for lang in installed_languages if lang.code == 'en'), None)
        to_lang = next((lang for lang in installed_languages if lang.code == target_lang), None)

        if not from_lang or not to_lang:
            return text

        translation = from_lang.get_translation(to_lang)
        if not translation:
            return text

        return translation.translate(text)
    except Exception as e:
        return text

translations = {{'en': all_data}}

for lang in target_langs:
    print(f"Traduction vers {{lang.upper()}}...", end=' ', flush=True)
    translations[lang] = {{}}

    for key, value in all_data.items():
        translations[lang][key] = translate_text(value, lang)

    print(f"✓ {{len(translations[lang])}} clés traduites")

with open('{category}_translations.json', 'w', encoding='utf-8') as f:
    json.dump(translations, f, ensure_ascii=False, indent=2)

total = sum(len(v) for v in translations.values())
print(f"\\n✓ Total: {{total}} traductions générées")
"""

    # Sauvegarder les données
    with open(f'/tmp/{category}_all_data.json', 'w', encoding='utf-8') as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)

    # Exécuter avec le venv Python
    with open(f'/tmp/translate_{category}.py', 'w', encoding='utf-8') as f:
        f.write(translate_script)

    result = subprocess.run(
        ['/home/komet/Desktop/Projekt/AI Tools/venv/bin/python3',
         f'/tmp/translate_{category}.py'],
        capture_output=True,
        text=True,
        cwd='/home/komet/Desktop/Projekt/AI Tools'
    )

    print(result.stdout)
    if result.returncode != 0:
        log(f"❌ Erreur lors de la traduction: {result.stderr}")
        return False

    return True

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 step1_generate_translations.py <category>")
        print("Exemple: python3 step1_generate_translations.py image")
        sys.exit(1)

    category = sys.argv[1]

    print("╔══════════════════════════════════════════════════════════╗")
    print(f"║  ÉTAPE 1: GÉNÉRATION DES TRADUCTIONS - {category.upper():15s} ║")
    print("╚══════════════════════════════════════════════════════════╝\n")

    # Étape 1: Obtenir les outils
    tools = get_tools_in_category(category)
    if not tools:
        log("❌ Aucun outil trouvé. Abandon.")
        sys.exit(1)

    # Étape 2: Extraire les FAQ
    log("\n[1/5] Extraction des FAQ...")
    all_faqs = extract_faqs_from_html(category, tools)
    total_faqs = sum(len(faqs) for faqs in all_faqs.values())
    log(f"✓ Total: {total_faqs} FAQ extraites")

    # Étape 3: Ajouter data-i18n aux FAQ
    log("\n[2/5] Ajout de data-i18n aux FAQ...")
    add_data_i18n_to_faqs(category, tools, all_faqs)
    log(f"✓ data-i18n ajouté aux FAQ de {len(all_faqs)} outils")

    # Étape 4: Extraire le contenu existant
    log("\n[3/5] Extraction du contenu existant de i18n.js...")
    existing_content = extract_content_from_i18n(tools)

    # Étape 5: Créer les données FAQ pour traduction
    log("\n[4/5] Préparation des données pour traduction...")
    all_data = dict(existing_content)  # Copier le contenu

    # Ajouter les FAQ
    for tool, faqs in all_faqs.items():
        # IMPORTANT: Garder les tirets dans le nom de l'outil!
        tool_key = tool  # Ne PAS enlever les tirets
        for faq in faqs:
            num = faq['number']
            all_data[f'review.{tool_key}.faq{num}.question'] = faq['question']
            all_data[f'review.{tool_key}.faq{num}.answer'] = faq['answer']

    log(f"✓ Total de clés à traduire: {len(all_data)}")
    log(f"  Contenu existant: {len(existing_content)}")
    log(f"  FAQ nouvelles: {len(all_data) - len(existing_content)}")

    # Étape 6: Générer les traductions
    log("\n[5/5] Génération des traductions en 9 langues...")
    if not generate_translations(all_data, category):
        log("❌ Échec de la génération des traductions")
        sys.exit(1)

    print("\n" + "="*60)
    print(f"✅ ÉTAPE 1 TERMINÉE POUR {category.upper()}!")
    print("="*60)
    print(f"\n📁 Fichier généré: {category}_translations.json")
    print(f"📊 Statistiques:")
    print(f"   - Clés totales: {len(all_data)}")
    print(f"   - Langues: 10 (EN + 9 traductions)")
    print(f"   - Total traductions: {len(all_data) * 10}")
    print(f"\n🔍 PROCHAINE ÉTAPE:")
    print(f"   1. Vérifier le fichier {category}_translations.json")
    print(f"   2. Exécuter: python3 step2_integrate_translations.py {category}")
    print()

if __name__ == "__main__":
    main()
