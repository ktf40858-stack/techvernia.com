#!/usr/bin/env python3
"""
Script automatisé pour traduire une catégorie complète (contenu + FAQ)
Usage: python3 process_category.py <nom_categorie>
Exemple: python3 process_category.py image
"""

import sys
import os
import json
import re
from bs4 import BeautifulSoup, NavigableString
import subprocess

def log(message):
    """Afficher un message avec formatage"""
    print(f"[PROCESS] {message}")

def get_tools_in_category(category):
    """Obtenir la liste des outils HTML dans une catégorie"""
    category_path = f"GenuisNet.ai/pages/reviews/{category}"
    if not os.path.exists(category_path):
        log(f"❌ Catégorie {category} non trouvée dans {category_path}")
        return []
    
    html_files = [f.replace('.html', '') for f in os.listdir(category_path) 
                  if f.endswith('.html') and not f.startswith('.')]
    
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
        tool_key = tool.replace('-', '')
        
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
    pattern = r'"(review\.[^"]+)":\s*"([^"]*(?:\\.[^"]*)*)"'
    
    content_dict = {}
    
    for match in re.finditer(pattern, en_section):
        key = match.group(1)
        value = match.group(2)
        
        # Vérifier si c'est une clé pour un des outils (et pas FAQ)
        for tool in tools:
            tool_key = tool.replace('-', '')
            if key.startswith(f'review.{tool}') and '.faq' not in key:
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

def inject_translations_into_i18n(category):
    """Injecter les traductions dans i18n.js"""
    
    # Charger les traductions
    translations_file = f'{category}_translations.json'
    if not os.path.exists(translations_file):
        log(f"❌ Fichier {translations_file} non trouvé")
        return False
    
    with open(translations_file, 'r', encoding='utf-8') as f:
        translations = json.load(f)
    
    # Charger i18n.js
    with open('GenuisNet.ai/js/i18n.js', 'r', encoding='utf-8') as f:
        content = f.read()
    
    log("Injection des traductions dans i18n.js...")
    
    languages = [
        ('fr', 'FRENCH', 'SPANISH'),
        ('es', 'SPANISH', 'GERMAN'),
        ('de', 'GERMAN', 'PORTUGUESE'),
        ('pt', 'PORTUGUESE', 'CHINESE'),
        ('zh', 'CHINESE', 'JAPANESE'),
        ('ja', 'JAPANESE', 'KOREAN'),
        ('ko', 'KOREAN', 'ARABIC'),
        ('ar', 'ARABIC', 'HINDI'),
    ]
    
    for lang_code, current_lang, next_lang in languages:
        if lang_code not in translations:
            continue
        
        pattern = rf'({lang_code}:\s*\{{)(.*?)(\n\s*\}},\s*\n\s*// ==+ {next_lang})'
        match = re.search(pattern, content, re.DOTALL)
        
        if not match:
            log(f"⚠️  {lang_code.upper()}: Section non trouvée")
            continue
        
        opening = match.group(1)
        section_body = match.group(2)
        closing = match.group(3)
        
        updated_count = 0
        for key, translated_value in translations[lang_code].items():
            escaped_value = translated_value.replace('\\', '\\\\')
            escaped_value = escaped_value.replace('"', '\\"')
            escaped_value = escaped_value.replace("'", "\\'")
            
            key_pattern = rf'"{re.escape(key)}":\s*"([^"]*(?:\\.[^"]*)*)"'
            
            if re.search(key_pattern, section_body):
                section_body = re.sub(key_pattern, f'"{key}": "{escaped_value}"', section_body)
                updated_count += 1
            else:
                # Si la clé n'existe pas, l'ajouter à la fin de la section
                section_body += f'\n        "{key}": "{escaped_value}",'
                updated_count += 1
        
        content = content.replace(match.group(0), opening + section_body + closing)
        log(f"  {lang_code.upper()}: {updated_count} clés mises à jour/ajoutées")
    
    # HI
    if 'hi' in translations:
        hi_pattern = r'(hi:\s*\{)(.*?)(\n\s*\}\n\};)'
        hi_match = re.search(hi_pattern, content, re.DOTALL)
        
        if hi_match:
            opening = hi_match.group(1)
            section_body = hi_match.group(2)
            closing = hi_match.group(3)
            
            updated_count = 0
            for key, translated_value in translations['hi'].items():
                escaped_value = translated_value.replace('\\', '\\\\')
                escaped_value = escaped_value.replace('"', '\\"')
                escaped_value = escaped_value.replace("'", "\\'")
                
                key_pattern = rf'"{re.escape(key)}":\s*"([^"]*(?:\\.[^"]*)*)"'
                
                if re.search(key_pattern, section_body):
                    section_body = re.sub(key_pattern, f'"{key}": "{escaped_value}"', section_body)
                    updated_count += 1
                else:
                    section_body += f'\n        "{key}": "{escaped_value}",'
                    updated_count += 1
            
            content = content.replace(hi_match.group(0), opening + section_body + closing)
            log(f"  HI: {updated_count} clés mises à jour/ajoutées")
    
    # Sauvegarder
    with open('GenuisNet.ai/js/i18n.js', 'w', encoding='utf-8') as f:
        f.write(content)
    
    log("✓ i18n.js mis à jour")
    return True

def verify_syntax():
    """Vérifier la syntaxe JavaScript"""
    result = subprocess.run(
        ['node', '-c', 'GenuisNet.ai/js/i18n.js'],
        capture_output=True,
        text=True,
        cwd='/home/komet/Desktop/Projekt/AI Tools'
    )
    
    if result.returncode == 0:
        log("✓✓✓ Syntaxe JavaScript valide!")
        return True
    else:
        log(f"❌ Erreur de syntaxe JavaScript:\n{result.stderr}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 process_category.py <category>")
        print("Exemple: python3 process_category.py image")
        sys.exit(1)
    
    category = sys.argv[1]
    
    print("╔══════════════════════════════════════════════════════════╗")
    print(f"║  TRAITEMENT AUTOMATIQUE DE LA CATÉGORIE: {category.upper():15s} ║")
    print("╚══════════════════════════════════════════════════════════╝\n")
    
    # Étape 1: Obtenir les outils
    tools = get_tools_in_category(category)
    if not tools:
        log("❌ Aucun outil trouvé. Abandon.")
        sys.exit(1)
    
    # Étape 2: Extraire les FAQ
    log("\n[1/6] Extraction des FAQ...")
    all_faqs = extract_faqs_from_html(category, tools)
    total_faqs = sum(len(faqs) for faqs in all_faqs.values())
    log(f"✓ Total: {total_faqs} FAQ extraites")
    
    # Étape 3: Ajouter data-i18n aux FAQ
    log("\n[2/6] Ajout de data-i18n aux FAQ...")
    add_data_i18n_to_faqs(category, tools, all_faqs)
    log(f"✓ data-i18n ajouté aux FAQ de {len(all_faqs)} outils")
    
    # Étape 4: Extraire le contenu existant
    log("\n[3/6] Extraction du contenu existant...")
    existing_content = extract_content_from_i18n(tools)
    
    # Étape 5: Créer les données FAQ pour traduction
    log("\n[4/6] Préparation des données pour traduction...")
    all_data = dict(existing_content)  # Copier le contenu
    
    # Ajouter les FAQ
    for tool, faqs in all_faqs.items():
        tool_key = tool.replace('-', '')
        for faq in faqs:
            num = faq['number']
            all_data[f'review.{tool_key}.faq{num}.question'] = faq['question']
            all_data[f'review.{tool_key}.faq{num}.answer'] = faq['answer']
    
    log(f"✓ Total de clés à traduire: {len(all_data)}")
    log(f"  Contenu: {len(existing_content)}")
    log(f"  FAQ: {len(all_data) - len(existing_content)}")
    
    # Étape 6: Générer les traductions
    log("\n[5/6] Génération des traductions...")
    if not generate_translations(all_data, category):
        log("❌ Échec de la génération des traductions")
        sys.exit(1)
    
    # Étape 7: Injecter dans i18n.js
    log("\n[6/6] Injection dans i18n.js...")
    if not inject_translations_into_i18n(category):
        log("❌ Échec de l'injection")
        sys.exit(1)
    
    # Vérifier la syntaxe
    log("\n[VÉRIFICATION] Validation de la syntaxe...")
    if not verify_syntax():
        log("❌ Syntaxe invalide. Veuillez corriger les erreurs.")
        sys.exit(1)
    
    print("\n" + "="*60)
    print(f"✅ CATÉGORIE {category.upper()} TRAITÉE AVEC SUCCÈS!")
    print("="*60)
    print(f"\nTotal de clés traduites: {len(all_data)}")
    print(f"Total de traductions générées: {len(all_data) * 9}")
    print(f"\nN'oubliez pas de vider le cache du navigateur et tester!")

if __name__ == "__main__":
    main()
