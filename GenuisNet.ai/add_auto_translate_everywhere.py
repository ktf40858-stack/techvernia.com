#!/usr/bin/env python3
"""
Ajouter le script de traduction automatique à toutes les pages
"""

import os
import re

def add_auto_translate_script(file_path):
    """Ajoute le script auto-translate.js si pas déjà présent"""

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Vérifier si déjà présent
        if 'auto-translate.js' in content:
            return False

        # Calculer le chemin relatif vers js/
        depth = len(os.path.relpath(file_path, '.').split(os.sep)) - 1
        relative_path = '../' * depth if depth > 0 else './'

        script_tag = f'    <script src="{relative_path}js/auto-translate.js"></script>'

        # Ajouter après i18n.js si présent, sinon avant </body>
        if 'i18n.js' in content:
            content = content.replace(
                'i18n.js"></script>',
                f'i18n.js"></script>\n{script_tag}'
            )
        elif '</body>' in content:
            content = content.replace('</body>', f'{script_tag}\n</body>')
        else:
            return False

        # Sauvegarder
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        return True

    except Exception as e:
        print(f"    ❌ Erreur: {e}")
        return False

def main():
    print("="*70)
    print("🌍 Ajout du Système de Traduction Automatique")
    print("="*70)
    print()

    updated = 0
    total = 0

    # Traiter index.html
    if os.path.exists('index.html'):
        print("📄 index.html")
        total += 1
        if add_auto_translate_script('index.html'):
            print("    ✅ Script auto-translate.js ajouté")
            updated += 1
        else:
            print("    ℹ️  Déjà présent ou erreur")

    # Traiter toutes les pages
    for root, dirs, files in os.walk('pages'):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                print(f"📄 {file_path}")
                total += 1
                if add_auto_translate_script(file_path):
                    print("    ✅ Script auto-translate.js ajouté")
                    updated += 1
                else:
                    print("    ℹ️  Déjà présent")

    print("\n" + "="*70)
    print(f"✅ Script ajouté à {updated} sur {total} pages")
    print("="*70)

    print("\n🎉 TRADUCTION AUTOMATIQUE ACTIVÉE!")
    print("\n📝 Comment ça fonctionne:")
    print("  1. Le visiteur change de langue (ex: Français)")
    print("  2. i18n.js traduit les éléments avec data-i18n")
    print("  3. auto-translate.js traduit TOUT le reste automatiquement!")
    print("  4. Les traductions sont mises en cache pour être rapides")
    print()
    print("🧪 Testez maintenant:")
    print("  http://localhost:8000/pages/categories/ai-chatbots.html")
    print("  Changez la langue et voyez TOUT changer! 🚀")

if __name__ == '__main__':
    main()
