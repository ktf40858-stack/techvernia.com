#!/usr/bin/env python3
"""
Script pour corriger l'ordre des scripts dans toutes les pages
"""

import os
import glob

def fix_script_order():
    """Corrige l'ordre des scripts dans toutes les pages HTML"""

    pages_dir = "GenuisNet.ai/pages"

    # Trouver tous les fichiers HTML
    html_files = glob.glob(f"{pages_dir}/*.html")

    count = 0
    for html_file in html_files:
        # Ignorer les fichiers de backup
        if 'backup' in html_file.lower() or 'old' in html_file.lower():
            continue

        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Chercher la section des scripts et corriger l'ordre
        old_pattern1 = '''<!-- Scripts -->
<script src="../js/animations.js"></script>
<script src="../js/main.js"></script>
<script src="../js/i18n.js"></script>
<script src="../js/auto-translate.js"></script>'''

        new_pattern = '''<!-- Scripts -->
<script src="../js/i18n.js"></script>
<script src="../js/auto-translate.js"></script>
<script src="../js/animations.js"></script>
<script src="../js/main.js"></script>'''

        # Autre variante possible
        old_pattern2 = '''<!-- Scripts -->
<script src="../js/main.js"></script>
<script src="../js/i18n.js"></script>
<script src="../js/auto-translate.js"></script>'''

        new_pattern2 = '''<!-- Scripts -->
<script src="../js/i18n.js"></script>
<script src="../js/auto-translate.js"></script>
<script src="../js/main.js"></script>'''

        # Remplacer
        if old_pattern1 in content:
            content = content.replace(old_pattern1, new_pattern)
            count += 1
            print(f"✅ {os.path.basename(html_file)}: Scripts réorganisés (pattern 1)")
        elif old_pattern2 in content:
            content = content.replace(old_pattern2, new_pattern2)
            count += 1
            print(f"✅ {os.path.basename(html_file)}: Scripts réorganisés (pattern 2)")
        else:
            # Vérifier si le fichier a déjà l'ordre correct
            if new_pattern in content or new_pattern2 in content:
                print(f"ℹ️  {os.path.basename(html_file)}: Déjà dans le bon ordre")
            else:
                print(f"⚠️  {os.path.basename(html_file)}: Pattern non reconnu")

        # Écrire si modifié
        if content != original_content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)

    print(f"\n✅ {count} fichiers modifiés!")

if __name__ == "__main__":
    fix_script_order()
