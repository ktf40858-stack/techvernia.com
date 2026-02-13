#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour corriger les problèmes d'indexation de TechVernia
- Corrige les canonicals et hreflang dans les fichiers index.html
- Nettoie les sitemaps des URLs 404
- Génère un rapport détaillé
"""

import os
import re
import sys
from pathlib import Path
from datetime import datetime

# Fix encoding for Windows
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# Configuration
BASE_DIR = Path(__file__).parent / "docs"
LANGUAGES = ["en", "fr", "es", "de", "pt", "zh", "ja", "ko", "ar", "hi"]
URLS_TO_REMOVE = [
    "guides-old.html",
    "guides_old_backup.html",
    "chatbots-comparison-old.html"
]

# Rapport
report = []
files_modified = []

def log(message):
    """Ajoute un message au rapport"""
    print(message)
    report.append(message)

def fix_index_html_files():
    """Corrige les canonicals et hreflang dans tous les index.html"""
    log("\n" + "="*80)
    log("ÉTAPE 1: Correction des fichiers index.html")
    log("="*80)

    # Fichier principal index.html (anglais)
    main_index = BASE_DIR / "index.html"
    fix_single_index(main_index, "en", is_main=True)

    # Fichiers index.html des autres langues
    for lang in LANGUAGES:
        if lang == "en":
            continue
        index_file = BASE_DIR / lang / "index.html"
        if index_file.exists():
            fix_single_index(index_file, lang, is_main=False)

def fix_single_index(file_path, lang, is_main=False):
    """Corrige un fichier index.html individuel"""
    log(f"\n📝 Traitement: {file_path.relative_to(BASE_DIR.parent)}")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    changes = []

    # 1. Corriger la balise canonical
    if is_main:
        # Pour la page principale anglaise
        old_canonical = r'<link rel="canonical" href="https://techvernia\.com/index\.html"\s*/>'
        new_canonical = '<link rel="canonical" href="https://techvernia.com/"/>'
        if re.search(old_canonical, content):
            content = re.sub(old_canonical, new_canonical, content)
            changes.append("  ✓ Canonical: https://techvernia.com/index.html → https://techvernia.com/")

        # Aussi corriger si c'est déjà sans index.html mais vérifier quand même
        old_canonical2 = r'<link rel="canonical" href="https://techvernia\.com/"\s*/>'
        if re.search(old_canonical2, content):
            log("  ℹ Canonical déjà correct: https://techvernia.com/")
    else:
        # Pour les autres langues
        old_canonical = f'<link rel="canonical" href="https://techvernia.com/{lang}/index.html"\\s*/>'
        new_canonical = f'<link rel="canonical" href="https://techvernia.com/{lang}/"/>'
        if re.search(old_canonical, content):
            content = re.sub(old_canonical, new_canonical, content)
            changes.append(f"  ✓ Canonical: /{lang}/index.html → /{lang}/")

        # Vérifier si déjà correct
        correct_canonical = f'<link rel="canonical" href="https://techvernia.com/{lang}/"\\s*/>'
        if re.search(correct_canonical, content):
            log(f"  ℹ Canonical déjà correct: /{lang}/")

    # 2. Corriger les balises hreflang
    hreflang_changes = 0

    # Pour x-default
    content = re.sub(
        r'<link rel="alternate" hreflang="x-default" href="https://techvernia\.com/index\.html"\s*/>',
        '<link rel="alternate" hreflang="x-default" href="https://techvernia.com/" />',
        content
    )

    # Pour chaque langue
    for hlang in LANGUAGES:
        if hlang == "en":
            # Anglais: techvernia.com/index.html → techvernia.com/
            old_pattern = r'<link rel="alternate" hreflang="en" href="https://techvernia\.com/index\.html"\s*/>'
            new_tag = '<link rel="alternate" hreflang="en" href="https://techvernia.com/" />'
            if re.search(old_pattern, content):
                content = re.sub(old_pattern, new_tag, content)
                hreflang_changes += 1
        else:
            # Autres langues: /lang/index.html → /lang/
            old_pattern = f'<link rel="alternate" hreflang="{hlang}" href="https://techvernia\\.com/{hlang}/index\\.html"\\s*/>'
            new_tag = f'<link rel="alternate" hreflang="{hlang}" href="https://techvernia.com/{hlang}/" />'
            if re.search(old_pattern, content):
                content = re.sub(old_pattern, new_tag, content)
                hreflang_changes += 1

    if hreflang_changes > 0:
        changes.append(f"  ✓ {hreflang_changes} balises hreflang corrigées")

    # Sauvegarder si des changements ont été effectués
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        files_modified.append(str(file_path.relative_to(BASE_DIR.parent)))
        log("  ✅ Fichier modifié:")
        for change in changes:
            log(change)
    else:
        log("  ⏭️  Aucun changement nécessaire")

def clean_sitemaps():
    """Nettoie les sitemaps des URLs 404"""
    log("\n" + "="*80)
    log("ÉTAPE 2: Nettoyage des sitemaps")
    log("="*80)

    sitemap_files = list(BASE_DIR.glob("sitemap-*.xml"))

    for sitemap_file in sitemap_files:
        clean_single_sitemap(sitemap_file)

def clean_single_sitemap(file_path):
    """Nettoie un fichier sitemap individuel"""
    log(f"\n📝 Traitement: {file_path.name}")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    urls_removed = []

    # Pour chaque URL à supprimer
    for bad_url in URLS_TO_REMOVE:
        # Pattern pour matcher un bloc <url>...</url> complet contenant l'URL
        pattern = rf'  <ns0:url>\s*<ns0:loc>https://techvernia\.com/[^<]*{re.escape(bad_url)}</ns0:loc>.*?</ns0:url>\s*'

        matches = re.findall(pattern, content, re.DOTALL)
        if matches:
            urls_removed.append(f"{bad_url} ({len(matches)} occurrences)")
            content = re.sub(pattern, '', content, flags=re.DOTALL)

    # Sauvegarder si des changements ont été effectués
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        files_modified.append(str(file_path.relative_to(BASE_DIR.parent)))
        log(f"  ✅ Sitemap nettoyé:")
        for url in urls_removed:
            log(f"    ✓ Supprimé: {url}")
    else:
        log("  ⏭️  Aucun changement nécessaire")

def generate_report():
    """Génère le rapport final"""
    log("\n" + "="*80)
    log("RAPPORT FINAL")
    log("="*80)

    log(f"\n📊 Résumé:")
    log(f"  • Fichiers modifiés: {len(files_modified)}")
    log(f"  • Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    log(f"\n📁 Liste des fichiers modifiés:")
    for file in files_modified:
        log(f"  • {file}")

    log("\n✅ CORRECTIONS TERMINÉES!")
    log("\n📌 PROCHAINES ÉTAPES:")
    log("  1. Vérifiez les changements avec: git diff")
    log("  2. Testez le site en local")
    log("  3. Committez les changements: git add . && git commit -m 'Fix: SEO indexation issues'")
    log("  4. Poussez vers le serveur: git push")
    log("  5. Soumettez le sitemap mis à jour à Google Search Console")
    log("  6. Attendez 2-4 semaines pour voir les résultats dans GSC")

    # Sauvegarder le rapport
    report_file = BASE_DIR.parent / f"indexation_fix_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report))

    log(f"\n📄 Rapport sauvegardé: {report_file.name}")

def main():
    """Fonction principale"""
    log("🚀 CORRECTION DES PROBLÈMES D'INDEXATION TECHVERNIA")
    log(f"📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    # Vérifier que le répertoire docs existe
    if not BASE_DIR.exists():
        log(f"❌ ERREUR: Le répertoire {BASE_DIR} n'existe pas!")
        return

    try:
        # Étape 1: Corriger les index.html
        fix_index_html_files()

        # Étape 2: Nettoyer les sitemaps
        clean_sitemaps()

        # Étape 3: Générer le rapport
        generate_report()

    except Exception as e:
        log(f"\n❌ ERREUR: {str(e)}")
        import traceback
        log(traceback.format_exc())

if __name__ == "__main__":
    main()
