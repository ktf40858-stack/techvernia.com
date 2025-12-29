import os
import re
import json as json_module

# Configuration
tools = [
    "aleks", "carnegie-learning", "century-tech", "cognii",
    "coursera-coach", "duolingo-max", "gradescope", "khan-academy-ai",
    "knewton-alta", "querium", "quizlet-ai", "socratic-by-google",
    "squirrel-ai", "thinkster-math"
]

base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
html_dir = os.path.join(base_dir, "pages", "reviews", "education")
js_dir = os.path.join(base_dir, "js")
batch_dir = html_dir

def extract_faq_questions(html_file):
    """Extrait toutes les questions FAQ d'un fichier HTML"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Trouver toutes les questions FAQ (maintenant avec data-i18n)
    pattern = r'<span data-i18n="([^"]+)">([^<]+)</span></h4>'
    matches = re.findall(pattern, content)

    # Retourner un dict {key: question_text}
    return {key: text for key, text in matches}

def update_i18n_with_faq(tool):
    """Met à jour le fichier i18n.js avec les traductions FAQ"""
    js_file = os.path.join(js_dir, f"{tool}-i18n.js")
    faq_batch_file = os.path.join(batch_dir, f"{tool}-faq-batch.json")
    html_file = os.path.join(html_dir, f"{tool}.html")

    if not os.path.exists(faq_batch_file):
        print(f"  [SKIP] No FAQ batch file for {tool}")
        return

    # Charger le fichier i18n.js existant
    with open(js_file, 'r', encoding='utf-8') as f:
        js_content = f.read()

    # Charger les traductions FAQ
    with open(faq_batch_file, 'r', encoding='utf-8') as f:
        faq_data = json_module.load(f)

    # Extraire les questions EN depuis le HTML
    en_faq = extract_faq_questions(html_file)

    # Pour chaque langue, ajouter les traductions FAQ
    languages = ["de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]

    for lang in ["en"] + languages:
        # Trouver le bloc de langue dans le JS
        pattern = rf'"{lang}":\s*(\{{)'
        match = re.search(pattern, js_content)

        if match:
            # Position de fin du bloc (juste avant la virgule ou accolade fermante)
            start_pos = match.end()

            # Trouver la fin du bloc JSON
            brace_count = 1
            pos = start_pos
            in_string = False
            escape = False

            while pos < len(js_content) and brace_count > 0:
                char = js_content[pos]

                if escape:
                    escape = False
                elif char == '\\':
                    escape = True
                elif char == '"':
                    in_string = not in_string
                elif not in_string:
                    if char == '{':
                        brace_count += 1
                    elif char == '}':
                        brace_count -= 1

                pos += 1

            if brace_count == 0:
                # Extraire le bloc JSON
                json_block = js_content[start_pos:pos-1]

                try:
                    # Parser le JSON existant
                    current_data = json_module.loads('{' + json_block + '}')

                    # Ajouter les FAQ
                    if lang == "en":
                        current_data.update(en_faq)
                    elif lang in faq_data:
                        current_data.update(faq_data[lang])

                    # Recréer le bloc JSON
                    new_json_block = json_module.dumps(current_data, indent=4, ensure_ascii=False)
                    # Enlever les accolades extérieures
                    new_json_block = new_json_block[1:-1].strip()

                    # Remplacer dans le contenu
                    js_content = js_content[:start_pos] + new_json_block + js_content[pos-1:]

                except Exception as e:
                    print(f"    [ERROR] Failed to parse {lang} block: {e}")

    # Sauvegarder le fichier i18n.js mis à jour
    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(js_content)

    faq_count = len(en_faq)
    print(f"  [OK] {tool}-i18n.js updated with {faq_count} FAQ translations")

# MAIN EXECUTION
print("=" * 70)
print("UPDATING I18N FILES WITH FAQ TRANSLATIONS")
print("=" * 70)

for tool in tools:
    print(f"\n{tool}:")
    update_i18n_with_faq(tool)

print("\n" + "=" * 70)
print("[COMPLETE] All i18n files updated with FAQ translations!")
print("=" * 70)
