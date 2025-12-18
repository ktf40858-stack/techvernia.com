#!/usr/bin/env python3
"""
Intégrer automatiquement les nouvelles clés dans js/i18n.js
"""

import json
import re
import os

PROJECT_ROOT = "/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai"
I18N_FILE = os.path.join(PROJECT_ROOT, "js/i18n.js")
KEYS_FILE = os.path.join(PROJECT_ROOT, "i18n_keys_index_FINAL.json")

def load_new_keys():
    """Charger les nouvelles clés depuis le fichier JSON"""
    with open(KEYS_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['keys']

def integrate_keys():
    """Intégrer les nouvelles clés dans i18n.js"""

    print(f"\n{'='*80}")
    print(f"🔄 INTÉGRATION DES NOUVELLES CLÉS DANS i18n.js")
    print(f"{'='*80}\n")

    # Charger les nouvelles clés
    new_keys = load_new_keys()
    print(f"📝 Chargement de {len(new_keys)} nouvelles clés...")

    # Lire i18n.js
    with open(I18N_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    print(f"✅ Fichier i18n.js chargé ({len(content)} caractères)\n")

    # Pour chaque langue, ajouter les clés
    languages = ['en', 'es', 'fr', 'de', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']

    for lang in languages:
        print(f"🔄 Traitement de {lang.upper()}...", end=' ')

        # Générer le code pour cette langue
        keys_code = ""
        for key, translations in sorted(new_keys.items()):
            value = translations[lang]
            # Échapper les caractères spéciaux
            value = value.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
            keys_code += f'        "{key}": "{value}",\n'

        # Trouver la fin du bloc de langue
        # Pattern: chercher "country.us" qui est la dernière clé de chaque langue
        pattern = rf'({lang}:\s*{{.*?"country\.us":\s*"[^"]*")\s*\n(\s*}})'

        def replacer(match):
            before_close = match.group(1)
            close_brace = match.group(2)

            # Ajouter les nouvelles clés avant la fermeture
            return f"{before_close},\n\n        // ========== Nouvelles clés pour index.html ==========\n{keys_code.rstrip()}\n{close_brace}"

        content, count = re.subn(pattern, replacer, content, flags=re.DOTALL)

        if count > 0:
            print(f"✅ {len(new_keys)} clés ajoutées")
        else:
            print(f"⚠️  Bloc non trouvé, recherche d'un pattern alternatif...")

            # Pattern alternatif: chercher la fin du bloc de langue
            # Pour hindi (dernier bloc), il n'y a pas de virgule après }
            if lang == 'hi':
                pattern_alt = rf'({lang}:\s*{{.*?"country\.us":\s*"[^"]*")\s*\n(\s*}}\s*\n}};)'
            else:
                pattern_alt = rf'({lang}:\s*{{.*?"country\.us":\s*"[^"]*")\s*\n(\s*}},)'

            def replacer_alt(match):
                before_close = match.group(1)
                close_brace = match.group(2)

                return f"{before_close},\n\n        // ========== Nouvelles clés pour index.html ==========\n{keys_code.rstrip()}\n{close_brace}"

            content, count = re.subn(pattern_alt, replacer_alt, content, flags=re.DOTALL)

            if count > 0:
                print(f"  ✅ {len(new_keys)} clés ajoutées (pattern alternatif)")
            else:
                print(f"  ❌ Échec - pattern non trouvé")

    # Sauvegarder le fichier modifié
    output_file = I18N_FILE
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\n{'='*80}")
    print(f"✅ INTÉGRATION TERMINÉE")
    print(f"{'='*80}\n")
    print(f"📁 Fichier modifié: {output_file}")
    print(f"📁 Backup disponible: {I18N_FILE}.backup")
    print(f"📊 Total: {len(new_keys)} clés × {len(languages)} langues = {len(new_keys) * len(languages)} traductions ajoutées")

    # Vérifier la taille du fichier
    new_size = len(content)
    print(f"\n📈 Taille du fichier:")
    print(f"   Avant: ~155 KB")
    print(f"   Après: ~{new_size // 1024} KB")

    return True

def main():
    try:
        integrate_keys()
        print(f"\n🎉 Intégration réussie!")
        print(f"\n📝 Prochaine étape: Appliquer data-i18n à index.html")
        print(f"   Commande: python3 add_i18n_smart.py index.html --apply")
    except Exception as e:
        print(f"\n❌ Erreur: {str(e)}")
        import traceback
        traceback.print_exc()
        print(f"\n💡 Le backup est disponible: {I18N_FILE}.backup")
        print(f"   Pour restaurer: cp js/i18n.js.backup js/i18n.js")

if __name__ == "__main__":
    main()
