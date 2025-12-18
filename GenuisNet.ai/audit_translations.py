#!/usr/bin/env python3
"""
Script d'audit des traductions i18n
Étape 1: Vérifier que toutes les clés existent dans toutes les langues
"""

import re
import json
from collections import defaultdict

I18N_FILE = "/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/js/i18n.js"
LANGUAGES = ['en', 'es', 'fr', 'de', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']

def extract_translation_keys(file_path):
    """
    Extraire toutes les clés de traduction par langue
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    translations = {}

    for lang in LANGUAGES:
        translations[lang] = []

        # Trouver le bloc de la langue (avec ou sans virgule finale)
        # Hindi est la dernière langue donc pas de virgule après }
        pattern = rf'{lang}:\s*\{{(.*?)\n    \}}[,;]?'
        match = re.search(pattern, content, re.DOTALL)

        if match:
            lang_block = match.group(1)

            # Extraire toutes les clés (format: "key": "value")
            key_pattern = r'"([^"]+)":\s*"'
            keys = re.findall(key_pattern, lang_block)
            translations[lang] = set(keys) if keys else set()
        else:
            print(f"⚠️ Warning: Could not find language block for {lang}")

    return translations

def analyze_translations(translations):
    """
    Analyser les traductions et identifier les problèmes
    """
    # Obtenir toutes les clés uniques
    all_keys = set()
    for keys in translations.values():
        all_keys.update(keys)

    print(f"\n{'='*70}")
    print("📊 RAPPORT D'AUDIT DES TRADUCTIONS")
    print(f"{'='*70}\n")

    print(f"Nombre total de clés uniques: {len(all_keys)}\n")

    # Analyser par langue
    missing_by_lang = {}

    for lang in LANGUAGES:
        keys_in_lang = translations.get(lang, set())
        missing = all_keys - keys_in_lang
        missing_by_lang[lang] = missing

        completion = (len(keys_in_lang) / len(all_keys) * 100) if all_keys else 0

        status = "✅" if completion == 100 else "⚠️" if completion >= 80 else "❌"

        print(f"{status} {lang.upper():5} | {len(keys_in_lang):4} clés | {completion:5.1f}% complet | {len(missing):3} manquantes")

    print(f"\n{'='*70}")
    print("📋 DÉTAILS DES CLÉS MANQUANTES PAR LANGUE")
    print(f"{'='*70}\n")

    for lang in LANGUAGES:
        if missing_by_lang[lang]:
            print(f"\n🔴 {lang.upper()} - {len(missing_by_lang[lang])} clés manquantes:")
            for key in sorted(missing_by_lang[lang])[:10]:  # Afficher les 10 premières
                print(f"   - {key}")
            if len(missing_by_lang[lang]) > 10:
                print(f"   ... et {len(missing_by_lang[lang]) - 10} autres")
        else:
            print(f"\n✅ {lang.upper()} - Toutes les clés présentes!")

    # Statistiques globales
    print(f"\n{'='*70}")
    print("📈 STATISTIQUES GLOBALES")
    print(f"{'='*70}\n")

    total_possible = len(all_keys) * len(LANGUAGES)
    total_present = sum(len(translations.get(lang, set())) for lang in LANGUAGES)
    total_missing = sum(len(missing_by_lang[lang]) for lang in LANGUAGES)

    global_completion = (total_present / total_possible * 100) if total_possible > 0 else 0

    print(f"Total de traductions possibles: {total_possible}")
    print(f"Total de traductions présentes: {total_present}")
    print(f"Total de traductions manquantes: {total_missing}")
    print(f"Taux de complétion global: {global_completion:.1f}%")

    # Sauvegarder le rapport JSON
    report = {
        "total_keys": len(all_keys),
        "languages": {},
        "global_stats": {
            "total_possible": total_possible,
            "total_present": total_present,
            "total_missing": total_missing,
            "completion_rate": round(global_completion, 2)
        }
    }

    for lang in LANGUAGES:
        keys_in_lang = translations.get(lang, set())
        missing = missing_by_lang[lang]
        completion = (len(keys_in_lang) / len(all_keys) * 100) if all_keys else 0

        report["languages"][lang] = {
            "keys_count": len(keys_in_lang),
            "missing_count": len(missing),
            "completion_rate": round(completion, 2),
            "missing_keys": sorted(list(missing))
        }

    report_file = "/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/translation_audit_report.json"
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Rapport détaillé sauvegardé: translation_audit_report.json")

    # Créer fichier des clés manquantes
    missing_file = "/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/missing_translations.txt"
    with open(missing_file, 'w', encoding='utf-8') as f:
        f.write("CLÉS MANQUANTES PAR LANGUE\n")
        f.write("="*70 + "\n\n")

        for lang in LANGUAGES:
            if missing_by_lang[lang]:
                f.write(f"\n{lang.upper()} - {len(missing_by_lang[lang])} clés manquantes:\n")
                f.write("-" * 50 + "\n")
                for key in sorted(missing_by_lang[lang]):
                    f.write(f"{key}\n")

    print(f"✅ Clés manquantes sauvegardées: missing_translations.txt\n")

    return report

def main():
    """Fonction principale"""
    print("\n🔍 Démarrage de l'audit des traductions...")

    try:
        translations = extract_translation_keys(I18N_FILE)
        report = analyze_translations(translations)

        print(f"\n{'='*70}")
        print("✅ AUDIT TERMINÉ")
        print(f"{'='*70}\n")

    except Exception as e:
        print(f"\n❌ Erreur: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
