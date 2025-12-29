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

# Traductions manquantes à ajouter
additional_translations = {
    "Free Plan": {
        "de": "Kostenloser Plan",
        "es": "Plan gratuito",
        "fr": "Plan gratuit",
        "pt": "Plano gratuito",
        "zh": "免费计划",
        "ja": "無料プラン",
        "ko": "무료 플랜",
        "ar": "خطة مجانية",
        "hi": "मुफ्त योजना"
    },
    "Professional ($29/mo)": {
        "de": "Professional (29 $/Monat)",
        "es": "Profesional ($29/mes)",
        "fr": "Professionnel (29 $/mois)",
        "pt": "Profissional ($29/mês)",
        "zh": "专业版（29美元/月）",
        "ja": "プロフェッショナル（29ドル/月）",
        "ko": "프로페셔널 ($29/월)",
        "ar": "احترافي (29 دولار/شهر)",
        "hi": "प्रोफेशनल ($29/माह)"
    },
    "Enterprise (Custom)": {
        "de": "Enterprise (Individuell)",
        "es": "Empresarial (Personalizado)",
        "fr": "Entreprise (Personnalisé)",
        "pt": "Empresarial (Personalizado)",
        "zh": "企业版（定制）",
        "ja": "エンタープライズ（カスタム）",
        "ko": "엔터프라이즈 (맞춤형)",
        "ar": "مؤسسي (مخصص)",
        "hi": "एंटरप्राइज़ (कस्टम)"
    }
}

# Template pour les questions spécifiques aux outils
tool_specific_patterns = {
    "Is {tool} worth the investment?": {
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
    "Does {tool} offer a free trial?": {
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

def get_tool_display_name(tool):
    """Convertit le nom du tool en format d'affichage"""
    return ' '.join(p.capitalize() for p in tool.split('-'))

def update_faq_batch_file(tool):
    """Met à jour le fichier FAQ batch avec les traductions manquantes"""
    batch_file = os.path.join(batch_dir, f"{tool}-faq-batch.json")

    if not os.path.exists(batch_file):
        return

    with open(batch_file, 'r', encoding='utf-8') as f:
        faq_data = json.load(f)

    tool_display = get_tool_display_name(tool)

    # Pour chaque langue
    for lang in ["de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]:
        if lang not in faq_data:
            continue

        # Trouver les clés qui ont des valeurs en anglais (non traduites)
        for key, value in list(faq_data[lang].items()):
            # Si la valeur est en anglais, chercher une traduction
            if value in additional_translations:
                faq_data[lang][key] = additional_translations[value][lang]

            # Vérifier les patterns spécifiques aux outils
            for pattern, translations in tool_specific_patterns.items():
                pattern_with_tool = pattern.replace("{tool}", tool_display)
                if value == pattern_with_tool:
                    faq_data[lang][key] = translations[lang].replace("{tool}", tool_display)

    # Sauvegarder
    with open(batch_file, 'w', encoding='utf-8') as f:
        json.dump(faq_data, f, indent=2, ensure_ascii=False)

    print(f"  [OK] {tool}-faq-batch.json updated")

def extract_faq_from_batch(tool):
    """Extrait les traductions FAQ depuis le fichier batch"""
    batch_file = os.path.join(batch_dir, f"{tool}-faq-batch.json")

    if not os.path.exists(batch_file):
        return {}

    with open(batch_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def update_i18n_file(tool):
    """Met à jour le fichier i18n.js avec les traductions FAQ corrigées"""
    js_file = os.path.join(js_dir, f"{tool}-i18n.js")
    faq_data = extract_faq_from_batch(tool)

    if not faq_data:
        return

    with open(js_file, 'r', encoding='utf-8') as f:
        js_content = f.read()

    # Pour chaque langue, mettre à jour les valeurs FAQ
    for lang in ["de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]:
        if lang not in faq_data:
            continue

        # Trouver et remplacer chaque clé FAQ
        for key, value in faq_data[lang].items():
            if key.startswith("review.") and ".faq." in key:
                # Chercher et remplacer dans le bloc de langue
                pattern = rf'("{re.escape(key)}":\s*)"[^"]*"'
                replacement = rf'\1"{value}"'
                js_content = re.sub(pattern, replacement, js_content)

    # Sauvegarder
    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(js_content)

    print(f"  [OK] {tool}-i18n.js updated with complete FAQ translations")

# MAIN EXECUTION
print("=" * 70)
print("COMPLETING FAQ TRANSLATIONS")
print("=" * 70)

print("\n[1/2] Updating FAQ batch files...")
for tool in tools:
    update_faq_batch_file(tool)

print("\n[2/2] Updating i18n.js files...")
for tool in tools:
    update_i18n_file(tool)

print("\n" + "=" * 70)
print("[COMPLETE] All FAQ translations are now complete!")
print("=" * 70)
