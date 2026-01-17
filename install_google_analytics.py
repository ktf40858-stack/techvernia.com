#!/usr/bin/env python3
"""
Script d'installation automatique de Google Analytics 4 sur TechVernia
Measurement ID: G-S2YLSEB9VR
"""

import os
import re
from pathlib import Path

# Configuration
MEASUREMENT_ID = "G-S2YLSEB9VR"
DOCS_DIR = "docs"

# Code Google Analytics a inserer
GA_CODE = f'''
<!-- Google Analytics 4 - TechVernia -->
<script async src="https://www.googletagmanager.com/gtag/js?id={MEASUREMENT_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{MEASUREMENT_ID}');
</script>
<!-- End Google Analytics -->
'''

def has_google_analytics(content):
    """Verifie si Google Analytics est deja installe"""
    return 'gtag' in content or MEASUREMENT_ID in content or 'googletagmanager.com/gtag/js' in content

def add_google_analytics(file_path):
    """Ajoute Google Analytics a un fichier HTML"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Verifier si GA est deja installe
        if has_google_analytics(content):
            return 'skipped', 'Already has Google Analytics'

        # Verifier que c'est un fichier HTML valide avec <head>
        if '<head>' not in content.lower():
            return 'skipped', 'No <head> tag found'

        # Chercher la position apres Google AdSense ou apres <head>
        # Pattern 1: Apres AdSense (ideal)
        adsense_pattern = r'(<script[^>]*googlesyndication\.com[^>]*>.*?</script>)'
        adsense_match = re.search(adsense_pattern, content, re.DOTALL | re.IGNORECASE)

        if adsense_match:
            # Inserer apres AdSense
            insert_pos = adsense_match.end()
            new_content = content[:insert_pos] + GA_CODE + content[insert_pos:]
        else:
            # Pattern 2: Apres la balise <head> si pas d'AdSense
            head_pattern = r'(<head[^>]*>)'
            head_match = re.search(head_pattern, content, re.IGNORECASE)

            if head_match:
                insert_pos = head_match.end()
                new_content = content[:insert_pos] + GA_CODE + content[insert_pos:]
            else:
                return 'skipped', 'Could not find insertion point'

        # Sauvegarder le fichier modifie
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        return 'success', 'Google Analytics installed'

    except Exception as e:
        return 'error', str(e)

def main():
    """Fonction principale"""
    print("=" * 70)
    print("Installation de Google Analytics 4 sur TechVernia")
    print(f"Measurement ID: {MEASUREMENT_ID}")
    print("=" * 70)
    print()

    # Statistiques
    stats = {
        'success': 0,
        'skipped': 0,
        'error': 0,
        'total': 0
    }

    # Parcourir tous les fichiers HTML
    docs_path = Path(DOCS_DIR)

    if not docs_path.exists():
        print(f"ERREUR: Le dossier '{DOCS_DIR}' n'existe pas!")
        print("   Assurez-vous d'executer ce script depuis le dossier techvernia.com")
        return

    print("Recherche des fichiers HTML...")
    html_files = list(docs_path.rglob('*.html'))

    print(f"Trouve {len(html_files)} fichiers HTML")
    print()

    # Traiter chaque fichier
    for html_file in html_files:
        stats['total'] += 1
        try:
            relative_path = html_file.relative_to(Path.cwd())
        except ValueError:
            relative_path = html_file

        status, message = add_google_analytics(html_file)
        stats[status] += 1

        # Symboles de statut
        symbol = {
            'success': '[OK]',
            'skipped': '[SKIP]',
            'error': '[ERROR]'
        }[status]

        if stats['total'] % 100 == 0 or status != 'success':
            print(f"{symbol} [{stats['total']:4d}/{len(html_files)}] {relative_path}")
            if message and status != 'success':
                print(f"    -> {message}")

    # Resume
    print()
    print("=" * 70)
    print("RESUME DE L'INSTALLATION")
    print("=" * 70)
    print(f"[OK]    Installe avec succes : {stats['success']} fichiers")
    print(f"[SKIP]  Ignore (deja installe): {stats['skipped']} fichiers")
    print(f"[ERROR] Erreurs              : {stats['error']} fichiers")
    print(f"        Total traite         : {stats['total']} fichiers")
    print()

    if stats['success'] > 0:
        print("SUCCESS! Google Analytics 4 installe avec succes!")
        print()
        print("PROCHAINES ETAPES:")
        print("1. Ouvrez https://techvernia.com dans votre navigateur")
        print("2. Allez dans Google Analytics -> Reports -> Realtime")
        print("3. Vous devriez voir votre visite en temps reel (1 user active)")
        print()
        print("Si vous ne voyez rien apres 2-3 minutes:")
        print("   - Videz le cache de votre navigateur (Ctrl+F5)")
        print("   - Verifiez que vous n'avez pas de bloqueur de pub actif")
        print("   - Attendez 10-15 minutes (delai de propagation)")
    else:
        print("ATTENTION: Aucun fichier n'a ete modifie.")
        print("   Tous les fichiers ont deja Google Analytics ou ne sont pas compatibles.")

    print()
    print("=" * 70)

if __name__ == "__main__":
    main()
