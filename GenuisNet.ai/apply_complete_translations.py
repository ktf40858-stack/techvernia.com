#!/usr/bin/env python3
"""
Appliquer les traductions complètes depuis complete_translations.json
"""

import json
import sys
import os

PROJECT_ROOT = "/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai"

def apply_translations(keys_file, translations_file):
    """Appliquer les traductions au fichier de clés"""

    # Charger les fichiers
    try:
        with open(keys_file, 'r', encoding='utf-8') as f:
            keys_data = json.load(f)

        with open(translations_file, 'r', encoding='utf-8') as f:
            trans_data = json.load(f)
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return None

    translations = trans_data.get('translations', {})
    keys = keys_data.get('keys', {})

    print(f"\n{'='*80}")
    print(f"🔄 APPLICATION DES TRADUCTIONS")
    print(f"{'='*80}\n")

    applied_count = 0
    remaining_count = 0

    for key, key_trans in keys.items():
        en_text = key_trans['en'].replace('[TO TRANSLATE] ', '')

        # Chercher la traduction
        if en_text in translations:
            trans = translations[en_text]

            # Appliquer pour chaque langue
            for lang in ['es', 'fr', 'de', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']:
                if lang in trans and trans[lang]:
                    key_trans[lang] = trans[lang]
                    applied_count += 1
                elif key_trans[lang].startswith('[TO TRANSLATE]'):
                    remaining_count += 1

    total_possible = len(keys) * 9
    completion_rate = (applied_count / total_possible * 100) if total_possible > 0 else 0

    print(f"📊 Résultats:")
    print(f"   - Traductions appliquées: {applied_count}")
    print(f"   - Encore à traduire: {remaining_count}")
    print(f"   - Taux de complétion: {completion_rate:.1f}%\n")

    # Sauvegarder
    output_file = keys_file.replace('.json', '_complete.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(keys_data, f, indent=2, ensure_ascii=False)

    print(f"✅ Fichier sauvegardé: {output_file}\n")

    # Lister ce qui reste à traduire
    print(f"{'='*80}")
    print(f"📝 PHRASES ENCORE À TRADUIRE")
    print(f"{'='*80}\n")

    still_needed = []
    for key, key_trans in keys.items():
        en_text = key_trans['en'].replace('[TO TRANSLATE] ', '')

        needs_translation = False
        for lang in ['es', 'fr', 'de', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']:
            if key_trans[lang].startswith('[TO TRANSLATE]'):
                needs_translation = True
                break

        if needs_translation and en_text not in still_needed:
            still_needed.append(en_text)

    if still_needed:
        print(f"Total: {len(still_needed)} phrases\n")
        for i, text in enumerate(still_needed[:20], 1):
            print(f"{i:3}. {text}")

        if len(still_needed) > 20:
            print(f"\n... et {len(still_needed) - 20} autres")
    else:
        print("🎉 Toutes les phrases ont été traduites!\n")

    return keys_data

def main():
    keys_file = os.path.join(PROJECT_ROOT, "i18n_keys_index_auto.json")
    translations_file = os.path.join(PROJECT_ROOT, "complete_translations.json")

    if not os.path.exists(keys_file):
        print(f"❌ Fichier non trouvé: {keys_file}")
        sys.exit(1)

    if not os.path.exists(translations_file):
        print(f"❌ Fichier non trouvé: {translations_file}")
        sys.exit(1)

    apply_translations(keys_file, translations_file)

if __name__ == "__main__":
    main()
