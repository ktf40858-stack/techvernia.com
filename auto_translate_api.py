#!/usr/bin/env python3
"""
TRADUCTEUR AUTOMATIQUE VIA API CLAUDE
Traduit tous les chunks automatiquement sans copier-coller manuel
"""
import json
import os
import time
from pathlib import Path
import anthropic
from tqdm import tqdm

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

# Utiliser Claude Haiku pour réduire les coûts (3x moins cher que Sonnet)
MODEL = "claude-3-5-haiku-20241022"  # Rapide et économique

def get_api_key():
    """Récupère la clé API depuis les variables d'environnement"""
    api_key = os.environ.get('ANTHROPIC_API_KEY')

    if not api_key:
        print("=" * 70)
        print("⚠️  CLÉ API ANTHROPIC NON TROUVÉE")
        print("=" * 70)
        print()
        print("Pour utiliser ce script, vous avez besoin d'une clé API Anthropic.")
        print()
        print("📋 ÉTAPES:")
        print("1. Allez sur: https://console.anthropic.com/")
        print("2. Créez un compte (gratuit)")
        print("3. Obtenez $5 de crédits gratuits")
        print("4. Créez une clé API")
        print()
        print("💰 COÛT ESTIMÉ:")
        print("   - Par chunk (500 clés): ~$0.02-0.05")
        print("   - 37 chunks espagnol: ~$1-2")
        print("   - 9 langues complètes: ~$10-15")
        print()
        print("5. Définissez la variable d'environnement:")
        print("   export ANTHROPIC_API_KEY='votre-clé-ici'")
        print()
        print("Ou bien, créez un fichier .env avec:")
        print("   ANTHROPIC_API_KEY=votre-clé-ici")
        print("=" * 70)
        return None

    return api_key

def create_translation_prompt(lang_name):
    """Crée le prompt de traduction"""
    return f"""You are a professional translator. Translate this JSON file from English to {lang_name}.

CRITICAL RULES:
1. Translate ONLY the VALUES, NEVER the keys
2. Preserve ALL special characters exactly: {{{{variable}}}}, %s, %d, \\n, etc.
3. Keep the exact same JSON structure
4. Maintain HTML tags if present: <b>, <i>, <a>, etc.
5. Preserve all spacing and formatting
6. Return ONLY valid JSON, nothing else - no explanations, no markdown

Example:
Input:  {{"welcome": "Hello {{{{name}}}}, welcome!"}}
Output: {{"welcome": "¡Hola {{{{name}}}}, bienvenido!"}}

Translate the following JSON to {lang_name}. Return ONLY the translated JSON:"""

def translate_chunk(client, chunk_data, lang_code, lang_name, chunk_num):
    """Traduit un chunk via l'API Claude"""

    prompt = create_translation_prompt(lang_name)

    try:
        # Envoyer à Claude API
        message = client.messages.create(
            model=MODEL,
            max_tokens=8000,
            temperature=0.3,  # Faible température pour cohérence
            messages=[
                {
                    "role": "user",
                    "content": f"{prompt}\n\n{json.dumps(chunk_data, ensure_ascii=False, indent=2)}"
                }
            ]
        )

        # Extraire le JSON de la réponse
        response_text = message.content[0].text.strip()

        # Nettoyer la réponse (enlever markdown si présent)
        if response_text.startswith('```'):
            lines = response_text.split('\n')
            response_text = '\n'.join(lines[1:-1])

        # Parser le JSON pour vérifier qu'il est valide
        translated_data = json.loads(response_text)

        return translated_data, None

    except json.JSONDecodeError as e:
        return None, f"Erreur JSON: {e}"
    except Exception as e:
        return None, f"Erreur API: {e}"

def translate_language(client, lang_code, lang_name):
    """Traduit tous les chunks d'une langue"""

    print()
    print("=" * 70)
    print(f"🌍 TRADUCTION: {lang_name} ({lang_code})")
    print("=" * 70)

    lang_dir = Path('batch_translation') / lang_code
    if not lang_dir.exists():
        print(f"❌ Dossier {lang_dir} introuvable")
        return False

    # Trouver tous les chunks
    chunk_files = sorted(lang_dir.glob('chunk_*.json'))

    if not chunk_files:
        print(f"❌ Aucun chunk trouvé dans {lang_dir}")
        return False

    print(f"📦 {len(chunk_files)} chunks à traduire")
    print()

    # Traduire chaque chunk avec barre de progression
    success_count = 0

    for chunk_file in tqdm(chunk_files, desc=f"Traduction {lang_code}", unit="chunk"):
        # Vérifier si déjà traduit
        chunk_num = chunk_file.stem.split('_')[1]
        output_file = lang_dir / f'translated_chunk_{chunk_num}.json'

        if output_file.exists():
            tqdm.write(f"   ⏭️  Chunk {chunk_num} déjà traduit, ignoré")
            success_count += 1
            continue

        # Charger le chunk
        try:
            with open(chunk_file, 'r', encoding='utf-8') as f:
                chunk_data = json.load(f)
        except Exception as e:
            tqdm.write(f"   ❌ Erreur lecture {chunk_file.name}: {e}")
            continue

        # Traduire
        translated_data, error = translate_chunk(
            client, chunk_data, lang_code, lang_name, chunk_num
        )

        if error:
            tqdm.write(f"   ❌ Chunk {chunk_num}: {error}")
            continue

        # Sauvegarder
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(translated_data, f, ensure_ascii=False, indent=2)
            success_count += 1
            tqdm.write(f"   ✅ Chunk {chunk_num}: {len(translated_data)} clés traduites")
        except Exception as e:
            tqdm.write(f"   ❌ Erreur sauvegarde {output_file.name}: {e}")

        # Petit délai pour éviter le rate limiting
        time.sleep(0.5)

    print()
    print(f"✅ {success_count}/{len(chunk_files)} chunks traduits avec succès")
    return success_count == len(chunk_files)

def merge_translations(lang_code):
    """Fusionne tous les chunks traduits d'une langue"""

    lang_dir = Path('batch_translation') / lang_code
    translated_files = sorted(lang_dir.glob('translated_chunk_*.json'))

    if not translated_files:
        print(f"⚠️  Aucun fichier traduit pour {lang_code}")
        return False

    merged_data = {}
    for chunk_file in translated_files:
        try:
            with open(chunk_file, 'r', encoding='utf-8') as f:
                chunk_data = json.load(f)
                merged_data.update(chunk_data)
        except Exception as e:
            print(f"❌ Erreur fusion {chunk_file.name}: {e}")
            return False

    # Sauvegarder
    output_file = Path(f'{lang_code}.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(merged_data, f, ensure_ascii=False, indent=2)

    print(f"✅ {lang_code}.json créé: {len(merged_data):,} clés")
    return True

def main():
    print("=" * 70)
    print("🤖 TRADUCTEUR AUTOMATIQUE VIA API CLAUDE")
    print("=" * 70)

    # Récupérer la clé API
    api_key = get_api_key()
    if not api_key:
        return

    # Initialiser le client Anthropic
    try:
        client = anthropic.Anthropic(api_key=api_key)
        print("✅ Client API initialisé")
    except Exception as e:
        print(f"❌ Erreur initialisation API: {e}")
        return

    # Demander quelle(s) langue(s) traduire
    print()
    print("📋 LANGUES DISPONIBLES:")
    for i, (code, name) in enumerate(LANGUAGES.items(), 1):
        print(f"   {i}. {name} ({code})")
    print(f"   0. Toutes les langues")
    print()

    choice = input("Quelle langue voulez-vous traduire? (numéro ou code): ").strip()

    # Déterminer les langues à traduire
    langs_to_translate = []

    if choice == '0' or choice.lower() == 'all':
        langs_to_translate = list(LANGUAGES.items())
    elif choice in LANGUAGES:
        langs_to_translate = [(choice, LANGUAGES[choice])]
    else:
        try:
            idx = int(choice) - 1
            lang_codes = list(LANGUAGES.items())
            if 0 <= idx < len(lang_codes):
                langs_to_translate = [lang_codes[idx]]
        except:
            pass

    if not langs_to_translate:
        print("❌ Choix invalide")
        return

    # Traduire chaque langue
    print()
    print(f"🚀 Début de la traduction de {len(langs_to_translate)} langue(s)")
    print()

    start_time = time.time()

    for lang_code, lang_name in langs_to_translate:
        success = translate_language(client, lang_code, lang_name)

        if success:
            print()
            print("🔄 Fusion des traductions...")
            merge_translations(lang_code)

    end_time = time.time()
    elapsed = end_time - start_time

    print()
    print("=" * 70)
    print("✅ TRADUCTION TERMINÉE!")
    print("=" * 70)
    print(f"⏱️  Temps total: {elapsed/60:.1f} minutes")
    print()

if __name__ == '__main__':
    main()
