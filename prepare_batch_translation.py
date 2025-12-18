#!/usr/bin/env python3
"""
BATCH TRANSLATION PREPARER
Prépare des fichiers JSON optimisés pour traduction manuelle via Claude/ChatGPT
Divise en chunks gérables pour éviter les limites de tokens
"""
import json
import os
from pathlib import Path

# Configuration
LANGUAGES = {
    'es': 'Spanish (Español)',
    'fr': 'French (Français)',
    'de': 'German (Deutsch)',
    'it': 'Italian (Italiano)',
    'pt': 'Portuguese (Português)',
    'ru': 'Russian (Русский)',
    'ja': 'Japanese (日本語)',
    'zh': 'Chinese Simplified (简体中文)',
    'ar': 'Arabic (العربية)'
}

CHUNK_SIZE = 500  # Nombre de clés par chunk (pour éviter limite tokens)

def load_english_keys():
    """Charge toutes les clés anglaises"""
    en_file = Path('all_full_translations_en.json')
    if not en_file.exists():
        print("❌ Fichier all_full_translations_en.json introuvable!")
        return None

    with open(en_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def create_batch_files():
    """Crée les fichiers batch pour chaque langue"""

    print("=" * 70)
    print("📦 PRÉPARATION DES FICHIERS BATCH POUR TRADUCTION MANUELLE")
    print("=" * 70)
    print()

    # Charger les clés anglaises
    en_data = load_english_keys()
    if not en_data:
        return

    total_keys = len(en_data)
    print(f"✅ {total_keys:,} clés chargées depuis en.json")
    print()

    # Créer dossier de sortie
    output_dir = Path('batch_translation')
    output_dir.mkdir(exist_ok=True)

    # Pour chaque langue
    for lang_code, lang_name in LANGUAGES.items():
        print(f"📝 Préparation: {lang_name} ({lang_code})")

        # Diviser en chunks
        keys_list = list(en_data.items())
        num_chunks = (total_keys + CHUNK_SIZE - 1) // CHUNK_SIZE

        lang_dir = output_dir / lang_code
        lang_dir.mkdir(exist_ok=True)

        for i in range(num_chunks):
            start_idx = i * CHUNK_SIZE
            end_idx = min((i + 1) * CHUNK_SIZE, total_keys)
            chunk_data = dict(keys_list[start_idx:end_idx])

            # Créer le fichier de chunk
            chunk_file = lang_dir / f'chunk_{i+1:02d}_of_{num_chunks:02d}.json'

            with open(chunk_file, 'w', encoding='utf-8') as f:
                json.dump(chunk_data, f, ensure_ascii=False, indent=2)

            print(f"   ✓ Chunk {i+1}/{num_chunks}: {len(chunk_data)} clés → {chunk_file.name}")

        # Créer le fichier d'instructions
        create_instructions_file(lang_dir, lang_code, lang_name, num_chunks)

        print(f"   ✅ {num_chunks} fichiers créés pour {lang_name}")
        print()

    # Créer script de fusion
    create_merge_script(output_dir)

    print("=" * 70)
    print("✅ PRÉPARATION TERMINÉE!")
    print("=" * 70)
    print()
    print(f"📂 Fichiers dans: {output_dir.absolute()}/")
    print()
    print("📋 PROCHAINES ÉTAPES:")
    print("   1. Ouvrez le dossier batch_translation/")
    print("   2. Pour chaque langue, suivez les INSTRUCTIONS.txt")
    print("   3. Collez les chunks dans Claude.ai ou ChatGPT")
    print("   4. Sauvegardez les résultats traduits")
    print("   5. Lancez merge_translations.py pour fusionner")
    print()

def create_instructions_file(lang_dir, lang_code, lang_name, num_chunks):
    """Crée le fichier d'instructions pour une langue"""

    instructions = f"""╔══════════════════════════════════════════════════════════════╗
║  INSTRUCTIONS - TRADUCTION {lang_name.upper()}
╚══════════════════════════════════════════════════════════════╝

📋 ÉTAPES À SUIVRE:

1. Ouvrez Claude.ai (https://claude.ai) ou ChatGPT

2. Pour CHAQUE fichier chunk_XX_of_{num_chunks:02d}.json:

   a) Copiez le PROMPT ci-dessous
   b) Attachez le fichier chunk_XX_of_{num_chunks:02d}.json
   c) Envoyez et attendez la traduction complète
   d) Téléchargez le résultat en JSON
   e) Renommez en: translated_chunk_XX.json

3. Une fois TOUS les chunks traduits, lancez:
   python3 merge_translations.py

═══════════════════════════════════════════════════════════════

📝 PROMPT À UTILISER (copiez tel quel):

═══════════════════════════════════════════════════════════════

You are a professional translator. I need you to translate a JSON file from English to {lang_name}.

IMPORTANT RULES:
1. Translate ONLY the VALUES, NEVER the keys
2. Preserve ALL special characters: {{{{variable}}}}, %s, %d, \\n, etc.
3. Keep the same JSON structure
4. Maintain HTML tags if present: <b>, <i>, <a>, etc.
5. Preserve spacing and formatting
6. Return ONLY valid JSON, nothing else

Example:
Input:  {{"welcome_message": "Hello {{{{name}}}}, welcome!"}}
Output: {{"welcome_message": "¡Hola {{{{name}}}}, bienvenido!"}}

Please translate the attached JSON file to {lang_name} following these rules strictly.
Return the complete translated JSON.

═══════════════════════════════════════════════════════════════

⏱️  TEMPS ESTIMÉ: ~5-10 minutes par chunk
📊 PROGRESSION: Vous avez {num_chunks} chunks à traiter

💡 ASTUCE:
   - Claude.ai est gratuit et très performant
   - Vous pouvez ouvrir plusieurs onglets pour paralléliser
   - Vérifiez que chaque résultat est du JSON valide

═══════════════════════════════════════════════════════════════
"""

    instructions_file = lang_dir / 'INSTRUCTIONS.txt'
    with open(instructions_file, 'w', encoding='utf-8') as f:
        f.write(instructions)

def create_merge_script(output_dir):
    """Crée le script de fusion des traductions"""

    merge_script = '''#!/usr/bin/env python3
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
'''

    merge_file = output_dir.parent / 'merge_translations.py'
    with open(merge_file, 'w', encoding='utf-8') as f:
        f.write(merge_script)

    os.chmod(merge_file, 0o755)
    print(f"✅ Script de fusion créé: {merge_file.name}")

if __name__ == '__main__':
    create_batch_files()
