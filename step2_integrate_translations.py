#!/usr/bin/env python3
"""
ÉTAPE 2: Intégration des traductions dans i18n.js
Usage: python3 step2_integrate_translations.py <category>
Exemple: python3 step2_integrate_translations.py image

Ce script va:
1. Charger le fichier {category}_translations.json
2. Créer une sauvegarde de i18n.js
3. Intégrer les traductions dans i18n.js
4. Vérifier la syntaxe JavaScript

PRÉREQUIS: Avoir exécuté step1_generate_translations.py d'abord
"""

import sys
import os
import json
import re
import subprocess
from datetime import datetime

def log(message):
    """Afficher un message avec formatage"""
    print(f"[STEP 2] {message}")

def create_backup():
    """Créer une sauvegarde de i18n.js"""
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_file = f"GenuisNet.ai/js/i18n.js.backup-{timestamp}"

    with open('GenuisNet.ai/js/i18n.js', 'r', encoding='utf-8') as f:
        content = f.read()

    with open(backup_file, 'w', encoding='utf-8') as f:
        f.write(content)

    log(f"✓ Sauvegarde créée: {backup_file}")
    return backup_file

def inject_translations_into_i18n(category):
    """Injecter les traductions dans i18n.js"""

    # Charger les traductions
    translations_file = f'{category}_translations.json'
    if not os.path.exists(translations_file):
        log(f"❌ Fichier {translations_file} non trouvé")
        log(f"   Veuillez d'abord exécuter: python3 step1_generate_translations.py {category}")
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

    total_injected = 0

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
            # Échappement sécurisé avec json.dumps
            escaped_value = json.dumps(translated_value, ensure_ascii=False)[1:-1]  # Enlever les guillemets de json.dumps

            # Regex améliorée pour capturer correctement les guillemets échappés
            key_pattern = rf'"{re.escape(key)}":\s*"((?:[^"\\]|\\.)*)"'

            if re.search(key_pattern, section_body):
                section_body = re.sub(key_pattern, f'"{key}": "{escaped_value}"', section_body)
                updated_count += 1
            else:
                # Si la clé n'existe pas, l'ajouter à la fin de la section
                section_body += f'\n        "{key}": "{escaped_value}",'
                updated_count += 1

        content = content.replace(match.group(0), opening + section_body + closing)
        log(f"  {lang_code.upper()}: {updated_count} clés mises à jour/ajoutées")
        total_injected += updated_count

    # Hindi (dernière section)
    if 'hi' in translations:
        hi_pattern = r'(hi:\s*\{)(.*?)(\n\s*\}\n\};)'
        hi_match = re.search(hi_pattern, content, re.DOTALL)

        if hi_match:
            opening = hi_match.group(1)
            section_body = hi_match.group(2)
            closing = hi_match.group(3)

            updated_count = 0
            for key, translated_value in translations['hi'].items():
                # Échappement sécurisé avec json.dumps
                escaped_value = json.dumps(translated_value, ensure_ascii=False)[1:-1]  # Enlever les guillemets de json.dumps

                # Regex améliorée pour capturer correctement les guillemets échappés
                key_pattern = rf'"{re.escape(key)}":\s*"((?:[^"\\]|\\.)*)"'

                if re.search(key_pattern, section_body):
                    section_body = re.sub(key_pattern, f'"{key}": "{escaped_value}"', section_body)
                    updated_count += 1
                else:
                    section_body += f'\n        "{key}": "{escaped_value}",'
                    updated_count += 1

            content = content.replace(hi_match.group(0), opening + section_body + closing)
            log(f"  HI: {updated_count} clés mises à jour/ajoutées")
            total_injected += updated_count

    # Sauvegarder
    with open('GenuisNet.ai/js/i18n.js', 'w', encoding='utf-8') as f:
        f.write(content)

    log(f"✓ i18n.js mis à jour ({total_injected} clés au total)")
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
        print("Usage: python3 step2_integrate_translations.py <category>")
        print("Exemple: python3 step2_integrate_translations.py image")
        sys.exit(1)

    category = sys.argv[1]

    print("╔══════════════════════════════════════════════════════════╗")
    print(f"║  ÉTAPE 2: INTÉGRATION DANS i18n.js - {category.upper():15s} ║")
    print("╚══════════════════════════════════════════════════════════╝\n")

    # Vérifier que le fichier de traduction existe
    if not os.path.exists(f'{category}_translations.json'):
        log(f"❌ Le fichier {category}_translations.json n'existe pas")
        log(f"   Veuillez d'abord exécuter:")
        log(f"   python3 step1_generate_translations.py {category}")
        sys.exit(1)

    # Créer une sauvegarde
    log("[1/3] Création d'une sauvegarde de sécurité...")
    backup_file = create_backup()

    # Intégrer les traductions
    log("\n[2/3] Intégration des traductions dans i18n.js...")
    if not inject_translations_into_i18n(category):
        log("❌ Échec de l'intégration")
        sys.exit(1)

    # Vérifier la syntaxe
    log("\n[3/3] Vérification de la syntaxe JavaScript...")
    if not verify_syntax():
        log("❌ Syntaxe invalide!")
        log(f"   Restauration de la sauvegarde...")
        with open(backup_file, 'r', encoding='utf-8') as f:
            content = f.read()
        with open('GenuisNet.ai/js/i18n.js', 'w', encoding='utf-8') as f:
            f.write(content)
        log("   i18n.js restauré à l'état précédent")
        sys.exit(1)

    print("\n" + "="*60)
    print(f"✅ ÉTAPE 2 TERMINÉE POUR {category.upper()}!")
    print("="*60)
    print(f"\n✓ Les traductions ont été intégrées dans i18n.js")
    print(f"✓ La syntaxe JavaScript est valide")
    print(f"✓ Sauvegarde disponible: {backup_file}")
    print(f"\n🧪 POUR TESTER:")
    print(f"   1. Ouvrir GenuisNet.ai/pages/reviews/{category}/<fichier>.html")
    print(f"   2. Vider le cache (Ctrl+Shift+Del)")
    print(f"   3. Recharger (Ctrl+F5)")
    print(f"   4. Changer de langue et vérifier les traductions")
    print()

if __name__ == "__main__":
    main()
