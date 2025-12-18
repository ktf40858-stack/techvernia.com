#!/usr/bin/env python3
"""
Restaure la version précédente des fichiers de catégories
"""

from pathlib import Path
import shutil
from datetime import datetime

def restore_categories():
    """Restaure les fichiers de catégories depuis les backups."""
    base_dir = Path('/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/categories')

    # Liste des catégories
    categories = [
        'ai-chatbots',
        'ai-writing',
        'ai-coding',
        'ai-image',
        'ai-video',
        'ai-audio',
        'ai-productivity',
        'ai-seo',
        'ai-business',
        'ai-networking',
        'ai-cybersecurity',
        'ai-medical',
        'ai-architecture',
    ]

    print("🔄 Restauration de la version précédente...\n")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    restored_count = 0

    for category in categories:
        current_file = base_dir / f'{category}.html'
        backup_file = base_dir / f'{category}.html.backup_20ai_{timestamp}'

        if current_file.exists():
            # Sauvegarder la version actuelle (avec les 20 AI)
            shutil.copy2(current_file, backup_file)
            print(f"💾 Backup créé: {category}.html.backup_20ai_{timestamp}")

            # Vérifier si on a un backup précédent
            old_backup = base_dir / f'{category}.html.backup_complete'

            if old_backup.exists():
                # Restaurer depuis le backup
                shutil.copy2(old_backup, current_file)
                print(f"✅ Restauré: {category}.html")
                restored_count += 1
            else:
                print(f"⚠️  Pas de backup disponible pour {category}.html")
        else:
            print(f"❌ Fichier non trouvé: {category}.html")

        print()

    print(f"{'='*50}")
    print(f"🎉 Restauration terminée!")
    print(f"✅ {restored_count}/{len(categories)} catégories restaurées")
    print(f"💾 Backups des versions avec 20 AI sauvegardés")

if __name__ == '__main__':
    restore_categories()
