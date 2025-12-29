import os
import re

base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
hr_dir = os.path.join(base_dir, "pages", "reviews", "hr")
js_dir = os.path.join(base_dir, "js")

hr_tools = [
    "beamery", "eightfold-ai", "fetcher", "findem", "harver",
    "hirevue", "humanly", "paradox-olivia", "phenom", "pymetrics",
    "seekout", "sense", "textio", "workable-ai"
]

# FAQ question translations
faq_questions = {
    "en": {
        "faq.is.worth.the.investment": "Is {tool} worth the investment?",
        "faq.how.long.does.implementation.take": "How long does implementation take?",
        "faq.what.integrations.are.available": "What integrations are available?",
        "faq.is.my.data.secure": "Is my data secure?",
        "faq.can.i.migrate.from.another.platform": "Can I migrate from another platform?",
        "faq.what.kind.of.support.is.available": "What kind of support is available?",
        "faq.does.offer.a.free.trial": "Does {tool} offer a free trial?",
        "faq.how.does.ai.enhance.the.platform": "How does AI enhance the platform?"
    },
    "de": {
        "faq.is.worth.the.investment": "Lohnt sich die Investition in {tool}?",
        "faq.how.long.does.implementation.take": "Wie lange dauert die Implementierung?",
        "faq.what.integrations.are.available": "Welche Integrationen sind verfügbar?",
        "faq.is.my.data.secure": "Sind meine Daten sicher?",
        "faq.can.i.migrate.from.another.platform": "Kann ich von einer anderen Plattform migrieren?",
        "faq.what.kind.of.support.is.available": "Welche Art von Support ist verfügbar?",
        "faq.does.offer.a.free.trial": "Bietet {tool} eine kostenlose Testversion an?",
        "faq.how.does.ai.enhance.the.platform": "Wie verbessert KI die Plattform?"
    },
    "es": {
        "faq.is.worth.the.investment": "¿Vale la pena la inversión en {tool}?",
        "faq.how.long.does.implementation.take": "¿Cuánto tiempo tarda la implementación?",
        "faq.what.integrations.are.available": "¿Qué integraciones están disponibles?",
        "faq.is.my.data.secure": "¿Están seguros mis datos?",
        "faq.can.i.migrate.from.another.platform": "¿Puedo migrar desde otra plataforma?",
        "faq.what.kind.of.support.is.available": "¿Qué tipo de soporte está disponible?",
        "faq.does.offer.a.free.trial": "¿Ofrece {tool} una prueba gratuita?",
        "faq.how.does.ai.enhance.the.platform": "¿Cómo mejora la IA la plataforma?"
    },
    "fr": {
        "faq.is.worth.the.investment": "Est-ce que {tool} vaut l'investissement ?",
        "faq.how.long.does.implementation.take": "Combien de temps prend la mise en œuvre ?",
        "faq.what.integrations.are.available": "Quelles intégrations sont disponibles ?",
        "faq.is.my.data.secure": "Mes données sont-elles sécurisées ?",
        "faq.can.i.migrate.from.another.platform": "Puis-je migrer depuis une autre plateforme ?",
        "faq.what.kind.of.support.is.available": "Quel type de support est disponible ?",
        "faq.does.offer.a.free.trial": "Est-ce que {tool} propose un essai gratuit ?",
        "faq.how.does.ai.enhance.the.platform": "Comment l'IA améliore-t-elle la plateforme ?"
    },
    "pt": {
        "faq.is.worth.the.investment": "Vale a pena o investimento em {tool}?",
        "faq.how.long.does.implementation.take": "Quanto tempo leva a implementação?",
        "faq.what.integrations.are.available": "Quais integrações estão disponíveis?",
        "faq.is.my.data.secure": "Meus dados estão seguros?",
        "faq.can.i.migrate.from.another.platform": "Posso migrar de outra plataforma?",
        "faq.what.kind.of.support.is.available": "Que tipo de suporte está disponível?",
        "faq.does.offer.a.free.trial": "{tool} oferece um teste gratuito?",
        "faq.how.does.ai.enhance.the.platform": "Como a IA melhora a plataforma?"
    },
    "zh": {
        "faq.is.worth.the.investment": "{tool}值得投资吗？",
        "faq.how.long.does.implementation.take": "实施需要多长时间？",
        "faq.what.integrations.are.available": "有哪些集成可用？",
        "faq.is.my.data.secure": "我的数据安全吗？",
        "faq.can.i.migrate.from.another.platform": "我可以从另一个平台迁移吗？",
        "faq.what.kind.of.support.is.available": "提供什么样的支持？",
        "faq.does.offer.a.free.trial": "{tool}提供免费试用吗？",
        "faq.how.does.ai.enhance.the.platform": "人工智能如何增强平台？"
    },
    "ja": {
        "faq.is.worth.the.investment": "{tool}は投資する価値がありますか？",
        "faq.how.long.does.implementation.take": "実装にはどのくらい時間がかかりますか？",
        "faq.what.integrations.are.available": "どのような統合が利用できますか？",
        "faq.is.my.data.secure": "私のデータは安全ですか？",
        "faq.can.i.migrate.from.another.platform": "別のプラットフォームから移行できますか？",
        "faq.what.kind.of.support.is.available": "どのようなサポートが利用できますか？",
        "faq.does.offer.a.free.trial": "{tool}は無料トライアルを提供していますか？",
        "faq.how.does.ai.enhance.the.platform": "AIはどのようにプラットフォームを強化しますか？"
    },
    "ko": {
        "faq.is.worth.the.investment": "{tool}는 투자할 가치가 있나요?",
        "faq.how.long.does.implementation.take": "구현에 얼마나 걸리나요?",
        "faq.what.integrations.are.available": "어떤 통합을 사용할 수 있나요?",
        "faq.is.my.data.secure": "내 데이터는 안전한가요?",
        "faq.can.i.migrate.from.another.platform": "다른 플랫폼에서 마이그레이션할 수 있나요?",
        "faq.what.kind.of.support.is.available": "어떤 종류의 지원을 사용할 수 있나요?",
        "faq.does.offer.a.free.trial": "{tool}는 무료 평가판을 제공하나요?",
        "faq.how.does.ai.enhance.the.platform": "AI는 플랫폼을 어떻게 향상시키나요?"
    },
    "ar": {
        "faq.is.worth.the.investment": "هل يستحق {tool} الاستثمار؟",
        "faq.how.long.does.implementation.take": "كم من الوقت يستغرق التنفيذ؟",
        "faq.what.integrations.are.available": "ما هي عمليات التكامل المتاحة؟",
        "faq.is.my.data.secure": "هل بياناتي آمنة؟",
        "faq.can.i.migrate.from.another.platform": "هل يمكنني الانتقال من منصة أخرى؟",
        "faq.what.kind.of.support.is.available": "ما نوع الدعم المتاح؟",
        "faq.does.offer.a.free.trial": "هل يقدم {tool} نسخة تجريبية مجانية؟",
        "faq.how.does.ai.enhance.the.platform": "كيف يعزز الذكاء الاصطناعي المنصة؟"
    },
    "hi": {
        "faq.is.worth.the.investment": "क्या {tool} निवेश के लायक है?",
        "faq.how.long.does.implementation.take": "कार्यान्वयन में कितना समय लगता है?",
        "faq.what.integrations.are.available": "कौन से एकीकरण उपलब्ध हैं?",
        "faq.is.my.data.secure": "क्या मेरा डेटा सुरक्षित है?",
        "faq.can.i.migrate.from.another.platform": "क्या मैं किसी अन्य प्लेटफ़ॉर्म से माइग्रेट कर सकता हूं?",
        "faq.what.kind.of.support.is.available": "किस प्रकार का समर्थन उपलब्ध है?",
        "faq.does.offer.a.free.trial": "क्या {tool} निःशुल्क परीक्षण प्रदान करता है?",
        "faq.how.does.ai.enhance.the.platform": "AI प्लेटफ़ॉर्म को कैसे बेहतर बनाता है?"
    }
}

def add_faq_translations(tool_key):
    """Add FAQ question translations to tool i18n file"""

    js_file = os.path.join(js_dir, f"{tool_key}-i18n.js")

    if not os.path.exists(js_file):
        return False

    with open(js_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # For each language
    for lang, questions in faq_questions.items():
        # Find language section
        lang_pattern = rf'"{lang}":\s*\{{'
        lang_match = re.search(lang_pattern, content)

        if not lang_match:
            continue

        # Add each FAQ question
        for key_suffix, question_template in questions.items():
            full_key = f"review.{tool_key}.{key_suffix}"

            # Skip if already exists
            if f'"{full_key}"' in content:
                continue

            # Replace {tool} placeholder (for questions that have it)
            question = question_template.replace("{tool}", tool_key.replace("-", " ").title())

            # Add the translation
            insert_pos = lang_match.end()
            escaped_value = question.replace('"', '\\"')
            new_line = f'\n    "{full_key}": "{escaped_value}",'
            content = content[:insert_pos] + new_line + content[insert_pos:]

    # Write updated content
    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(content)

    return True

print("=" * 70)
print("ADDING FAQ QUESTION SUPPORT TO ALL HR TOOLS")
print("=" * 70)

count = 0

for tool_key in hr_tools:
    if add_faq_translations(tool_key):
        print(f"  [+] {tool_key}: FAQ questions added")
        count += 1
    else:
        print(f"  [!] {tool_key}: Failed")

print("\n" + "=" * 70)
print(f"COMPLETE: {count}/{len(hr_tools)} tools")
print("=" * 70)
