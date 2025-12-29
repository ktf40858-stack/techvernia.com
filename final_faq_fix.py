import os
import json

base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
batch_dir = os.path.join(base_dir, "pages", "reviews", "education")
js_dir = os.path.join(base_dir, "js")

tools = {
    "aleks": "ALEKS",
    "carnegie-learning": "Carnegie Learning",
    "century-tech": "Century Tech",
    "cognii": "Cognii",
    "coursera-coach": "Coursera Coach",
    "duolingo-max": "Duolingo Max",
    "gradescope": "Gradescope",
    "khan-academy-ai": "Khan Academy Ai",
    "knewton-alta": "Knewton Alta",
    "querium": "Querium",
    "quizlet-ai": "Quizlet Ai",
    "socratic-by-google": "Socratic By Google",
    "squirrel-ai": "Squirrel Ai",
    "thinkster-math": "Thinkster Math"
}

translations = {
    "worth": {
        "de": "Lohnt sich die Investition in {tool}?",
        "es": "¿Vale la pena la inversión en {tool}?",
        "fr": "{tool} vaut-il l'investissement ?",
        "pt": "{tool} vale o investimento?",
        "zh": "{tool}值得投资吗？",
        "ja": "{tool}は投資する価値がありますか？",
        "ko": "{tool}는 투자 가치가 있나요?",
        "ar": "هل يستحق {tool} الاستثمار؟",
        "hi": "क्या {tool} में निवेश करना उचित है?"
    },
    "trial": {
        "de": "Bietet {tool} eine kostenlose Testversion an?",
        "es": "¿{tool} ofrece una prueba gratuita?",
        "fr": "{tool} propose-t-il un essai gratuit ?",
        "pt": "{tool} oferece um teste gratuito?",
        "zh": "{tool}提供免费试用吗？",
        "ja": "{tool}は無料トライアルを提供していますか？",
        "ko": "{tool}는 무료 평가판을 제공하나요?",
        "ar": "هل يقدم {tool} تجربة مجانية؟",
        "hi": "क्या {tool} निःशुल्क परीक्षण प्रदान करता है?"
    }
}

for tool_key, tool_display in tools.items():
    batch_file = os.path.join(batch_dir, f"{tool_key}-faq-batch.json")

    if not os.path.exists(batch_file):
        continue

    # Charger le fichier
    with open(batch_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Mettre à jour
    changed = False
    for lang in ["de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]:
        if lang in data:
            for key in data[lang].keys():
                # Question "worth the investment"
                if f"{tool_key}.faq.is.{tool_key.replace('-', '.')}.worth.the.investment" in key:
                    data[lang][key] = translations["worth"][lang].replace("{tool}", tool_display)
                    changed = True
                # Question "free trial"
                elif f"{tool_key}.faq.does.{tool_key.replace('-', '.')}.offer.a.free.trial" in key:
                    data[lang][key] = translations["trial"][lang].replace("{tool}", tool_display)
                    changed = True

    # Sauvegarder si modifié
    if changed:
        with open(batch_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"[OK] {tool_key}-faq-batch.json updated")

        # Mettre à jour le fichier i18n.js
        js_file = os.path.join(js_dir, f"{tool_key}-i18n.js")

        with open(js_file, 'r', encoding='utf-8') as f:
            js_content = f.read()

        # Remplacer directement les chaînes dans le JS
        for lang in ["de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]:
            if lang in data:
                for key, value in data[lang].items():
                    if ".faq." in key:
                        # Format: "key": "old_value" -> "key": "new_value"
                        old_pattern = f'"{key}": "Is {tool_display} worth the investment?"'
                        new_pattern = f'"{key}": "{value}"'
                        js_content = js_content.replace(old_pattern, new_pattern)

                        old_pattern = f'"{key}": "Does {tool_display} offer a free trial?"'
                        new_pattern = f'"{key}": "{value}"'
                        js_content = js_content.replace(old_pattern, new_pattern)

        with open(js_file, 'w', encoding='utf-8') as f:
            f.write(js_content)

        print(f"[OK] {tool_key}-i18n.js updated")

print("\n[COMPLETE] FAQ translations finalized!")
