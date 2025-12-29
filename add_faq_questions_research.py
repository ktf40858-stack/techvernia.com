import os
import re

base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
research_dir = os.path.join(base_dir, "pages", "reviews", "research")
js_dir = os.path.join(base_dir, "js")

tools = [
    "connected-papers", "consensus", "elicit", "irisai", "litmaps",
    "perplexity-research", "researchrabbit", "scholarcy", "scispace",
    "scite", "semantic-scholar", "undermind"
]

tool_names = {
    "connected-papers": "Connected Papers",
    "consensus": "Consensus",
    "elicit": "Elicit",
    "irisai": "Iris.ai",
    "litmaps": "Litmaps",
    "perplexity-research": "Perplexity Research",
    "researchrabbit": "ResearchRabbit",
    "scholarcy": "Scholarcy",
    "scispace": "SciSpace",
    "scite": "Scite",
    "semantic-scholar": "Semantic Scholar",
    "undermind": "Undermind"
}

# Questions FAQ communes
common_faq_questions = {
    "Is {tool} worth the investment?": "faq.is.{tool_key}.worth.the.investment",
    "How long does implementation take?": "faq.how.long.does.implementation.take",
    "What integrations are available?": "faq.what.integrations.are.available",
    "Is my data secure?": "faq.is.my.data.secure",
    "Can I migrate from another platform?": "faq.can.i.migrate.from.another.platform",
    "What kind of support is available?": "faq.what.kind.of.support.is.available",
    "Does {tool} offer a free trial?": "faq.does.{tool_key}.offer.a.free.trial",
    "How does AI enhance the platform?": "faq.how.does.ai.enhance.the.platform"
}

# Traductions des questions FAQ
faq_translations = {
    "faq.is.{tool_key}.worth.the.investment": {
        "en": "Is {tool} worth the investment?",
        "de": "Lohnt sich die Investition in {tool}?",
        "es": "¿Vale la pena la inversión en {tool}?",
        "fr": "Est-ce que {tool} vaut l'investissement ?",
        "pt": "Vale a pena investir em {tool}?",
        "zh": "{tool}值得投资吗？",
        "ja": "{tool}への投資は価値がありますか？",
        "ko": "{tool}에 투자할 가치가 있나요?",
        "ar": "هل يستحق الاستثمار في {tool}؟",
        "hi": "क्या {tool} में निवेश करना उचित है?"
    },
    "faq.how.long.does.implementation.take": {
        "en": "How long does implementation take?",
        "de": "Wie lange dauert die Implementierung?",
        "es": "¿Cuánto tiempo tarda la implementación?",
        "fr": "Combien de temps prend l'implémentation ?",
        "pt": "Quanto tempo leva a implementação?",
        "zh": "实施需要多长时间？",
        "ja": "実装にはどのくらい時間がかかりますか？",
        "ko": "구현에 얼마나 걸리나요?",
        "ar": "كم من الوقت يستغرق التنفيذ؟",
        "hi": "कार्यान्वयन में कितना समय लगता है?"
    },
    "faq.what.integrations.are.available": {
        "en": "What integrations are available?",
        "de": "Welche Integrationen sind verfügbar?",
        "es": "¿Qué integraciones están disponibles?",
        "fr": "Quelles intégrations sont disponibles ?",
        "pt": "Quais integrações estão disponíveis?",
        "zh": "有哪些集成可用？",
        "ja": "どのような統合が利用可能ですか？",
        "ko": "어떤 통합을 사용할 수 있나요?",
        "ar": "ما هي التكاملات المتاحة؟",
        "hi": "कौन से एकीकरण उपलब्ध हैं?"
    },
    "faq.is.my.data.secure": {
        "en": "Is my data secure?",
        "de": "Sind meine Daten sicher?",
        "es": "¿Están seguros mis datos?",
        "fr": "Mes données sont-elles sécurisées ?",
        "pt": "Meus dados estão seguros?",
        "zh": "我的数据安全吗？",
        "ja": "データは安全ですか？",
        "ko": "내 데이터는 안전한가요?",
        "ar": "هل بياناتي آمنة؟",
        "hi": "क्या मेरा डेटा सुरक्षित है?"
    },
    "faq.can.i.migrate.from.another.platform": {
        "en": "Can I migrate from another platform?",
        "de": "Kann ich von einer anderen Plattform migrieren?",
        "es": "¿Puedo migrar desde otra plataforma?",
        "fr": "Puis-je migrer depuis une autre plateforme ?",
        "pt": "Posso migrar de outra plataforma?",
        "zh": "我可以从其他平台迁移吗？",
        "ja": "他のプラットフォームから移行できますか？",
        "ko": "다른 플랫폼에서 마이그레이션할 수 있나요?",
        "ar": "هل يمكنني الترحيل من منصة أخرى؟",
        "hi": "क्या मैं किसी अन्य प्लेटफ़ॉर्म से माइग्रेट कर सकता हूं?"
    },
    "faq.what.kind.of.support.is.available": {
        "en": "What kind of support is available?",
        "de": "Welche Art von Support ist verfügbar?",
        "es": "¿Qué tipo de soporte está disponible?",
        "fr": "Quel type de support est disponible ?",
        "pt": "Que tipo de suporte está disponível?",
        "zh": "有哪些类型的支持可用？",
        "ja": "どのようなサポートが利用可能ですか？",
        "ko": "어떤 종류의 지원을 받을 수 있나요?",
        "ar": "ما نوع الدعم المتاح؟",
        "hi": "किस प्रकार का समर्थन उपलब्ध है?"
    },
    "faq.does.{tool_key}.offer.a.free.trial": {
        "en": "Does {tool} offer a free trial?",
        "de": "Bietet {tool} eine kostenlose Testversion an?",
        "es": "¿Ofrece {tool} una prueba gratuita?",
        "fr": "Est-ce que {tool} propose un essai gratuit ?",
        "pt": "{tool} oferece um teste gratuito?",
        "zh": "{tool}提供免费试用吗？",
        "ja": "{tool}は無料トライアルを提供していますか？",
        "ko": "{tool}은 무료 평가판을 제공하나요?",
        "ar": "هل يقدم {tool} تجربة مجانية؟",
        "hi": "क्या {tool} निःशुल्क परीक्षण प्रदान करता है?"
    },
    "faq.how.does.ai.enhance.the.platform": {
        "en": "How does AI enhance the platform?",
        "de": "Wie verbessert KI die Plattform?",
        "es": "¿Cómo mejora la IA la plataforma?",
        "fr": "Comment l'IA améliore-t-elle la plateforme ?",
        "pt": "Como a IA melhora a plataforma?",
        "zh": "AI如何增强平台？",
        "ja": "AIはプラットフォームをどのように強化しますか？",
        "ko": "AI는 플랫폼을 어떻게 향상시키나요?",
        "ar": "كيف يعزز الذكاء الاصطناعي المنصة؟",
        "hi": "AI प्लेटफ़ॉर्म को कैसे बेहतर बनाता है?"
    }
}

def add_faq_i18n_to_html(html_file, tool):
    """Ajoute les attributs data-i18n aux questions FAQ"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    tool_display = tool_names[tool]
    tool_key = tool.replace("-", ".")

    modified = False
    count = 0

    # Pour chaque question FAQ
    for question_pattern, key_template in common_faq_questions.items():
        # Remplacer {tool} par le nom de l'outil
        question = question_pattern.replace("{tool}", tool_display)
        key = key_template.replace("{tool_key}", tool_key)
        full_key = f"review.{tool}.{key}"

        # Pattern pour trouver le h4 sans data-i18n
        pattern = rf'<h4>({re.escape(question)})</h4>'
        replacement = rf'<h4><span data-i18n="{full_key}">\1</span></h4>'

        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content)
            modified = True
            count += 1

    if modified:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)

    return modified, count

def append_faq_to_i18n_file(tool):
    """Ajoute les traductions FAQ au fichier i18n.js"""
    js_file = os.path.join(js_dir, f"{tool}-i18n.js")

    if not os.path.exists(js_file):
        return False

    tool_display = tool_names[tool]
    tool_key = tool.replace("-", ".")

    with open(js_file, 'r', encoding='utf-8') as f:
        content = f.read()

    languages = ["en", "de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]

    for lang in languages:
        # Trouver la section de langue
        pattern = rf'"{lang}":\s*\{{([^}}]*)\}}'
        match = re.search(pattern, content, re.DOTALL)

        if match:
            lang_section = match.group(1)

            # Ajouter les traductions FAQ
            for key_template, translations in faq_translations.items():
                key = key_template.replace("{tool_key}", tool_key)
                full_key = f"review.{tool}.{key}"

                if lang in translations:
                    translation = translations[lang].replace("{tool}", tool_display)

                    # Vérifier si la clé n'existe pas déjà
                    if f'"{full_key}"' not in lang_section:
                        # Échapper les caractères spéciaux
                        escaped_value = translation.replace('"', '\\"')
                        new_item = f',\n    "{full_key}": "{escaped_value}"'

                        # Ajouter avant la fermeture de l'objet
                        if lang_section.strip():
                            lang_section = lang_section.rstrip() + new_item
                        else:
                            lang_section = f'\n    "{full_key}": "{escaped_value}"\n  '

            # Remplacer la section de langue
            new_lang_section = f'"{lang}": {{{lang_section}}}'
            content = content.replace(match.group(0), new_lang_section)

    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(content)

    return True

print("=" * 70)
print("ADDING FAQ QUESTIONS I18N TO RESEARCH TOOLS")
print("=" * 70)

total_html = 0
total_js = 0

for tool in tools:
    print(f"\n{tool}:")
    html_file = os.path.join(research_dir, f"{tool}.html")

    if os.path.exists(html_file):
        # 1. Ajouter data-i18n aux questions FAQ
        modified, count = add_faq_i18n_to_html(html_file, tool)
        if modified:
            print(f"  [+] HTML: Added data-i18n to {count} FAQ questions")
            total_html += 1
        else:
            print(f"  [OK] HTML: Questions already have data-i18n")

        # 2. Ajouter les traductions FAQ au fichier i18n.js
        if append_faq_to_i18n_file(tool):
            print(f"  [+] i18n.js: Added {len(faq_translations)} FAQ question translations")
            total_js += 1
        else:
            print(f"  [!] i18n.js: File not found")
    else:
        print(f"  [SKIP] HTML file not found")

print("\n" + "=" * 70)
print(f"[COMPLETE] Modified {total_html} HTML files and {total_js} i18n files")
print("=" * 70)
