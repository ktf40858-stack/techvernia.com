import os
import json
import re

base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
batch_dir = os.path.join(base_dir, "pages", "reviews", "education")
js_dir = os.path.join(base_dir, "js")

tools = [
    "aleks", "carnegie-learning", "century-tech", "cognii",
    "coursera-coach", "duolingo-max", "gradescope", "khan-academy-ai",
    "knewton-alta", "querium", "quizlet-ai", "socratic-by-google",
    "squirrel-ai", "thinkster-math"
]

def get_tool_display_name(tool):
    """Convertit le nom du tool en format d'affichage"""
    return ' '.join(p.capitalize() for p in tool.split('-'))

def fix_tool_specific_faq(tool):
    """Corrige les traductions pour les questions spécifiques aux outils"""
    batch_file = os.path.join(batch_dir, f"{tool}-faq-batch.json")
    js_file = os.path.join(js_dir, f"{tool}-i18n.js")

    if not os.path.exists(batch_file):
        return

    tool_display = get_tool_display_name(tool)

    # Patterns de traduction
    worth_pattern = {
        "de": f"Lohnt sich die Investition in {tool_display}?",
        "es": f"¿Vale la pena la inversión en {tool_display}?",
        "fr": f"{tool_display} vaut-il l'investissement ?",
        "pt": f"{tool_display} vale o investimento?",
        "zh": f"{tool_display}值得投资吗？",
        "ja": f"{tool_display}は投資する価値がありますか？",
        "ko": f"{tool_display}는 투자 가치가 있나요?",
        "ar": f"هل يستحق {tool_display} الاستثمار؟",
        "hi": f"क्या {tool_display} में निवेश करना उचित है?"
    }

    trial_pattern = {
        "de": f"Bietet {tool_display} eine kostenlose Testversion an?",
        "es": f"¿{tool_display} ofrece una prueba gratuita?",
        "fr": f"{tool_display} propose-t-il un essai gratuit ?",
        "pt": f"{tool_display} oferece um teste gratuito?",
        "zh": f"{tool_display}提供免费试用吗？",
        "ja": f"{tool_display}は無料トライアルを提供していますか？",
        "ko": f"{tool_display}는 무료 평가판을 제공하나요?",
        "ar": f"هل يقدم {tool_display} تجربة مجانية؟",
        "hi": f"क्या {tool_display} निःशुल्क परीक्षण प्रदान करता है?"
    }

    # Charger le fichier batch
    with open(batch_file, 'r', encoding='utf-8') as f:
        faq_data = json.load(f)

    # Mettre à jour les traductions
    for lang in ["de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]:
        if lang not in faq_data:
            continue

        for key, value in faq_data[lang].items():
            # Chercher les questions non traduites
            if f"Is {tool_display} worth the investment?" in value:
                faq_data[lang][key] = worth_pattern[lang]
            elif f"Does {tool_display} offer a free trial?" in value:
                faq_data[lang][key] = trial_pattern[lang]

    # Sauvegarder le fichier batch
    with open(batch_file, 'w', encoding='utf-8') as f:
        json.dump(faq_data, f, indent=2, ensure_ascii=False)

    # Mettre à jour le fichier i18n.js
    with open(js_file, 'r', encoding='utf-8') as f:
        js_content = f.read()

    for lang in ["de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]:
        if lang not in faq_data:
            continue

        for key, value in faq_data[lang].items():
            # Échapper les caractères spéciaux pour regex
            escaped_key = re.escape(key)
            # Chercher et remplacer
            pattern = rf'("{escaped_key}":\s*)"[^"]*"'
            replacement = rf'\1"{value}"'
            js_content = re.sub(pattern, replacement, js_content)

    # Sauvegarder le fichier i18n.js
    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(js_content)

    print(f"  [OK] {tool} FAQ translations fixed")

# MAIN EXECUTION
print("=" * 70)
print("FIXING TOOL-SPECIFIC FAQ TRANSLATIONS")
print("=" * 70)

for tool in tools:
    fix_tool_specific_faq(tool)

print("\n" + "=" * 70)
print("[COMPLETE] All tool-specific FAQ translations fixed!")
print("=" * 70)
