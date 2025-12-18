#!/usr/bin/env python3
"""
MERGE TRANSLATIONS
Fusionne tous les chunks traduits en fichiers de langue finaux
"""
import json
from pathlib import Path

LANGUAGES = ['es', 'fr', 'de', 'it', 'pt', 'ru', 'ja', 'zh', 'ar']

def merge_language(lang_code):
    """Fusionne tous les chunks d'une langue"""
    lang_dir = Path('batch_translation') / lang_code

    if not lang_dir.exists():
        print(f"❌ Dossier {lang_code} introuvable")
        return False

    # Trouver tous les fichiers traduits
    translated_files = sorted(lang_dir.glob('translated_chunk_*.json'))

    if not translated_files:
        print(f"⚠️  Aucun fichier traduit trouvé pour {lang_code}")
        return False

    # Fusionner
    merged_data = {}
    for chunk_file in translated_files:
        try:
            with open(chunk_file, 'r', encoding='utf-8') as f:
                chunk_data = json.load(f)
                merged_data.update(chunk_data)
            print(f"   ✓ {chunk_file.name}: {len(chunk_data)} clés")
        except Exception as e:
            print(f"   ❌ Erreur avec {chunk_file.name}: {e}")
            return False

    # Sauvegarder
    output_file = Path(f'{lang_code}.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(merged_data, f, ensure_ascii=False, indent=2)

    print(f"   ✅ {lang_code}.json créé: {len(merged_data):,} clés")
    return True

def main():
    print("=" * 70)
    print("🔄 FUSION DES TRADUCTIONS")
    print("=" * 70)
    print()

    success_count = 0
    for lang_code in LANGUAGES:
        print(f"📦 Fusion {lang_code}:")
        if merge_language(lang_code):
            success_count += 1
        print()

    print("=" * 70)
    print(f"✅ {success_count}/{len(LANGUAGES)} langues fusionnées avec succès")
    print("=" * 70)

if __name__ == '__main__':
    main()
