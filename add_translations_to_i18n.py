#!/usr/bin/env python3
"""
Script pour ajouter toutes les traductions ChatGPT dans i18n.js
"""

import json

def add_translations_to_i18n():
    """Ajoute les traductions EN et ES dans i18n.js"""

    i18n_path = "GenuisNet.ai/js/i18n.js"

    # Load translations
    with open('chatgpt_translations_en.json', 'r', encoding='utf-8') as f:
        translations_en = json.load(f)

    with open('chatgpt_translations_es.json', 'r', encoding='utf-8') as f:
        translations_es = json.load(f)

    # Read i18n.js
    with open(i18n_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    print(f"📊 Chargé: {len(translations_en)} traductions EN, {len(translations_es)} traductions ES")

    # === ENGLISH SECTION ===
    # Find where to insert (after existing review translations or after common.tools)
    en_marker = '"common.tools": "tools",'

    if en_marker in content:
        # Generate EN translation strings
        en_lines = []
        for key in sorted(translations_en.keys()):
            value = translations_en[key].replace('"', '\\"').replace('\n', '\\n')
            en_lines.append(f'        "{key}": "{value}",')

        en_block = '\n' + '\n'.join(en_lines)

        # Insert after marker
        content = content.replace(en_marker, en_marker + en_block)
        print(f"✅ Ajouté {len(en_lines)} clés EN")
    else:
        print("❌ Marker EN non trouvé")

    # === SPANISH SECTION ===
    # Find ES section marker
    es_marker = '"common.tools": "herramientas",'

    if es_marker in content:
        # Generate ES translation strings
        es_lines = []
        for key in sorted(translations_es.keys()):
            value = translations_es[key].replace('"', '\\"').replace('\n', '\\n')
            es_lines.append(f'        "{key}": "{value}",')

        es_block = '\n' + '\n'.join(es_lines)

        # Insert after marker
        content = content.replace(es_marker, es_marker + es_block)
        print(f"✅ Ajouté {len(es_lines)} clés ES")
    else:
        print("❌ Marker ES non trouvé")

    # Save modified i18n.js
    if content != original_content:
        # Backup
        backup_path = i18n_path + '.chatgpt_backup'
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(original_content)

        with open(i18n_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"\n🎉 Traductions ajoutées à i18n.js!")
        print(f"📝 Backup: {backup_path}")
        print(f"📊 Total: {len(translations_en)} clés ajoutées pour EN et ES")
    else:
        print("\n⚠️  Aucune modification")

if __name__ == "__main__":
    add_translations_to_i18n()
