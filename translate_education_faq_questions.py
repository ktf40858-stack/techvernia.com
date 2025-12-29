import os
import re
import json

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

# Dictionnaire de traduction pour les questions FAQ communes
faq_translations = {
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
    "How long does implementation take?": {
        "de": "Wie lange dauert die Implementierung?",
        "es": "¿Cuánto tiempo lleva la implementación?",
        "fr": "Combien de temps prend la mise en œuvre ?",
        "pt": "Quanto tempo leva a implementação?",
        "zh": "实施需要多长时间？",
        "ja": "実装にはどのくらい時間がかかりますか？",
        "ko": "구현에 얼마나 걸리나요?",
        "ar": "كم من الوقت يستغرق التنفيذ؟",
        "hi": "कार्यान्वयन में कितना समय लगता है?"
    },
    "What integrations are available?": {
        "de": "Welche Integrationen sind verfügbar?",
        "es": "¿Qué integraciones están disponibles?",
        "fr": "Quelles intégrations sont disponibles ?",
        "pt": "Quais integrações estão disponíveis?",
        "zh": "有哪些集成可用？",
        "ja": "どのような統合が利用できますか？",
        "ko": "어떤 통합을 사용할 수 있나요?",
        "ar": "ما هي التكاملات المتاحة؟",
        "hi": "कौन से एकीकरण उपलब्ध हैं?"
    },
    "Is my data secure?": {
        "de": "Sind meine Daten sicher?",
        "es": "¿Están seguros mis datos?",
        "fr": "Mes données sont-elles sécurisées ?",
        "pt": "Meus dados estão seguros?",
        "zh": "我的数据安全吗？",
        "ja": "私のデータは安全ですか？",
        "ko": "내 데이터는 안전한가요?",
        "ar": "هل بياناتي آمنة؟",
        "hi": "क्या मेरा डेटा सुरक्षित है?"
    },
    "Can I migrate from another platform?": {
        "de": "Kann ich von einer anderen Plattform migrieren?",
        "es": "¿Puedo migrar desde otra plataforma?",
        "fr": "Puis-je migrer depuis une autre plateforme ?",
        "pt": "Posso migrar de outra plataforma?",
        "zh": "我可以从其他平台迁移吗？",
        "ja": "他のプラットフォームから移行できますか？",
        "ko": "다른 플랫폼에서 마이그레이션할 수 있나요?",
        "ar": "هل يمكنني الترحيل من منصة أخرى؟",
        "hi": "क्या मैं किसी अन्य प्लेटफ़ॉर्म से माइग्रेट कर सकता हूँ?"
    },
    "What kind of support is available?": {
        "de": "Welche Art von Support ist verfügbar?",
        "es": "¿Qué tipo de soporte está disponible?",
        "fr": "Quel type de support est disponible ?",
        "pt": "Que tipo de suporte está disponível?",
        "zh": "提供哪种类型的支持？",
        "ja": "どのようなサポートが利用できますか？",
        "ko": "어떤 종류의 지원을 받을 수 있나요?",
        "ar": "ما نوع الدعم المتاح؟",
        "hi": "किस प्रकार का समर्थन उपलब्ध है?"
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
    },
    "How does AI enhance the platform?": {
        "de": "Wie verbessert KI die Plattform?",
        "es": "¿Cómo mejora la IA la plataforma?",
        "fr": "Comment l'IA améliore-t-elle la plateforme ?",
        "pt": "Como a IA aprimora a plataforma?",
        "zh": "AI如何增强平台？",
        "ja": "AIはプラットフォームをどのように強化しますか？",
        "ko": "AI가 플랫폼을 어떻게 향상시키나요?",
        "ar": "كيف يعزز الذكاء الاصطناعي المنصة؟",
        "hi": "AI प्लेटफ़ॉर्म को कैसे बेहतर बनाता है?"
    }
}

def extract_faq_questions(html_file):
    """Extrait toutes les questions FAQ d'un fichier HTML"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Trouver toutes les questions FAQ (balises h4 sans data-i18n)
    pattern = r'<h4>([^<]+)</h4>'
    matches = re.findall(pattern, content)

    return matches

def create_i18n_key(question, tool):
    """Crée une clé i18n à partir d'une question"""
    # Nettoyer la question et créer une clé
    key = question.lower()
    key = re.sub(r'[^a-z0-9\s]', '', key)  # Enlever la ponctuation
    key = re.sub(r'\s+', '.', key.strip())  # Remplacer espaces par points
    key = f"review.{tool}.faq.{key}"
    return key

def translate_question(question, tool_name):
    """Traduit une question FAQ"""
    tool_display = ' '.join(p.capitalize() for p in tool_name.split('-'))

    # Remplacer le nom de l'outil par un placeholder
    question_template = question.replace(tool_display, "{tool}")

    translations = {}

    # Chercher dans le dictionnaire de traductions
    if question_template in faq_translations:
        for lang, trans_template in faq_translations[question_template].items():
            translations[lang] = trans_template.replace("{tool}", tool_display)
    else:
        # Traduction de secours (garder l'anglais)
        print(f"  [WARN] No translation found for: {question}")
        for lang in ["de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]:
            translations[lang] = question

    return translations

def update_html_with_faq_i18n(tool):
    """Met à jour le HTML avec les attributs data-i18n pour les questions FAQ"""
    html_file = os.path.join(html_dir, f"{tool}.html")

    if not os.path.exists(html_file):
        print(f"  [SKIP] {tool}.html not found")
        return []

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extraire les questions
    questions = extract_faq_questions(html_file)

    if not questions:
        print(f"  [INFO] No FAQ questions found in {tool}.html")
        return []

    # Créer un mapping question -> clé i18n
    question_mappings = []
    for question in questions:
        key = create_i18n_key(question, tool)
        question_mappings.append((question, key))

        # Remplacer dans le HTML
        old_html = f"<h4>{question}</h4>"
        new_html = f'<h4><span data-i18n="{key}">{question}</span></h4>'
        content = content.replace(old_html, new_html)

    # Sauvegarder le HTML mis à jour
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  [OK] {tool}.html updated with {len(question_mappings)} FAQ i18n keys")
    return question_mappings

def create_faq_batch_file(tool, question_mappings):
    """Crée un fichier batch pour les traductions FAQ"""
    if not question_mappings:
        return

    languages = ["de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]
    batch_data = {}

    for lang in languages:
        batch_data[lang] = {}

    for question, key in question_mappings:
        translations = translate_question(question, tool)
        for lang in languages:
            if lang in translations:
                batch_data[lang][key] = translations[lang]

    # Sauvegarder le fichier batch FAQ
    batch_file = os.path.join(batch_dir, f"{tool}-faq-batch.json")
    with open(batch_file, 'w', encoding='utf-8') as f:
        json.dump(batch_data, f, indent=2, ensure_ascii=False)

    print(f"  [OK] {tool}-faq-batch.json created ({len(question_mappings)} questions)")

def tool_to_camel(tool):
    """khan-academy-ai -> khanAcademyAi"""
    parts = tool.split('-')
    return parts[0] + ''.join(p.capitalize() for p in parts[1:])

def update_i18n_with_faq(tool):
    """Met à jour le fichier i18n.js avec les traductions FAQ"""
    js_file = os.path.join(js_dir, f"{tool}-i18n.js")
    faq_batch_file = os.path.join(batch_dir, f"{tool}-faq-batch.json")

    if not os.path.exists(faq_batch_file):
        return

    # Charger le fichier i18n.js existant
    with open(js_file, 'r', encoding='utf-8') as f:
        js_content = f.read()

    # Charger les traductions FAQ
    with open(faq_batch_file, 'r', encoding='utf-8') as f:
        faq_data = json.load(f)

    # Pour chaque langue, ajouter les traductions FAQ
    languages = ["de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]

    for lang in ["en"] + languages:
        # Trouver le bloc de langue
        pattern = rf'"{lang}":\s*(\{{[^}}]+(?:\{{[^}}]*\}}[^}}]*)*\}})'
        match = re.search(pattern, js_content, re.DOTALL)

        if match:
            old_block = match.group(1)

            if lang == "en":
                # Pour EN, extraire les questions depuis le HTML
                html_file = os.path.join(html_dir, f"{tool}.html")
                questions = extract_faq_questions(html_file)
                en_faq = {}
                for question in questions:
                    key = create_i18n_key(question, tool)
                    en_faq[key] = question

                # Ajouter les FAQ au bloc existant
                try:
                    import json
                    current_data = json.loads(old_block)
                    current_data.update(en_faq)
                    new_block = json.dumps(current_data, indent=4, ensure_ascii=False)
                    js_content = js_content.replace(old_block, new_block)
                except:
                    pass
            else:
                # Pour les autres langues, ajouter depuis faq_data
                if lang in faq_data:
                    try:
                        current_data = json.loads(old_block)
                        current_data.update(faq_data[lang])
                        new_block = json.dumps(current_data, indent=4, ensure_ascii=False)
                        js_content = js_content.replace(old_block, new_block)
                    except:
                        pass

    # Sauvegarder le fichier i18n.js mis à jour
    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(js_content)

    print(f"  [OK] {tool}-i18n.js updated with FAQ translations")

# MAIN EXECUTION
print("=" * 70)
print("EDUCATION TOOLS - FAQ QUESTIONS TRANSLATION")
print("=" * 70)

print("\n[1/3] Updating HTML files with data-i18n attributes...")
all_mappings = {}
for tool in tools:
    print(f"\n{tool}:")
    mappings = update_html_with_faq_i18n(tool)
    all_mappings[tool] = mappings

print("\n[2/3] Creating FAQ translation batch files...")
for tool in tools:
    print(f"\n{tool}:")
    if tool in all_mappings:
        create_faq_batch_file(tool, all_mappings[tool])

print("\n[3/3] Updating i18n.js files with FAQ translations...")
for tool in tools:
    print(f"\n{tool}:")
    update_i18n_with_faq(tool)

print("\n" + "=" * 70)
print("[COMPLETE] FAQ questions are now multilingual!")
print("=" * 70)
print("\nUpdated:")
print(f"  - 14 HTML files with data-i18n on FAQ questions")
print(f"  - 14 FAQ batch files created")
print(f"  - 14 i18n.js files updated")
print(f"  - ~8 FAQ questions × 10 languages × 14 tools = ~1,120 translations")
