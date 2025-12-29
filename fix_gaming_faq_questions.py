#!/usr/bin/env python3
"""
Fix FAQ questions in Gaming category
1. Add data-i18n attributes to FAQ question titles in HTML files
2. Add translations for FAQ questions in i18n files
"""

import re
import os

# FAQ questions and their translations
FAQ_QUESTIONS = {
    "Is {TOOL} worth the investment?": {
        "key": "is.tool.worth.the.investment",
        "translations": {
            "de": "Lohnt sich die Investition in {TOOL}?",
            "fr": "{TOOL} vaut-il l'investissement ?",
            "es": "¿Vale la pena invertir en {TOOL}?",
            "pt": "{TOOL} vale o investimento?",
            "zh": "{TOOL} 值得投资吗？",
            "ja": "{TOOL} は投資に値しますか？",
            "ko": "{TOOL}는 투자할 가치가 있나요?",
            "ar": "هل يستحق {TOOL} الاستثمار؟",
            "hi": "क्या {TOOL} निवेश के लायक है？"
        }
    },
    "How long does implementation take?": {
        "key": "how.long.does.implementation.take",
        "translations": {
            "de": "Wie lange dauert die Implementierung?",
            "fr": "Combien de temps prend la mise en œuvre ?",
            "es": "¿Cuánto tiempo lleva la implementación?",
            "pt": "Quanto tempo leva a implementação?",
            "zh": "实施需要多长时间？",
            "ja": "実装にはどのくらいの時間がかかりますか？",
            "ko": "구현에는 얼마나 걸리나요?",
            "ar": "كم من الوقت يستغرق التنفيذ؟",
            "hi": "कार्यान्वयन में कितना समय लगता है？"
        }
    },
    "What integrations are available?": {
        "key": "what.integrations.are.available",
        "translations": {
            "de": "Welche Integrationen sind verfügbar?",
            "fr": "Quelles intégrations sont disponibles ?",
            "es": "¿Qué integraciones están disponibles?",
            "pt": "Quais integrações estão disponíveis?",
            "zh": "有哪些集成可用？",
            "ja": "どのような統合が利用できますか？",
            "ko": "어떤 통합이 가능한가요?",
            "ar": "ما هي التكاملات المتاحة؟",
            "hi": "कौन से एकीकरण उपलब्ध हैं？"
        }
    },
    "Is my data secure?": {
        "key": "is.my.data.secure",
        "translations": {
            "de": "Sind meine Daten sicher?",
            "fr": "Mes données sont-elles sécurisées ?",
            "es": "¿Están seguros mis datos?",
            "pt": "Meus dados estão seguros?",
            "zh": "我的数据安全吗？",
            "ja": "私のデータは安全ですか？",
            "ko": "내 데이터는 안전한가요?",
            "ar": "هل بياناتي آمنة؟",
            "hi": "क्या मेरा डेटा सुरक्षित है？"
        }
    },
    "Can I migrate from another platform?": {
        "key": "can.i.migrate.from.another.platform",
        "translations": {
            "de": "Kann ich von einer anderen Plattform migrieren?",
            "fr": "Puis-je migrer depuis une autre plateforme ?",
            "es": "¿Puedo migrar desde otra plataforma?",
            "pt": "Posso migrar de outra plataforma?",
            "zh": "我可以从其他平台迁移吗？",
            "ja": "他のプラットフォームから移行できますか？",
            "ko": "다른 플랫폼에서 마이그레이션할 수 있나요?",
            "ar": "هل يمكنني الانتقال من منصة أخرى؟",
            "hi": "क्या मैं दूसरे प्लेटफ़ॉर्म से माइग्रेट कर सकता हूँ？"
        }
    },
    "What kind of support is available?": {
        "key": "what.kind.of.support.is.available",
        "translations": {
            "de": "Welche Art von Support ist verfügbar?",
            "fr": "Quel type de support est disponible ?",
            "es": "¿Qué tipo de soporte está disponible?",
            "pt": "Que tipo de suporte está disponível?",
            "zh": "提供哪些类型的支持？",
            "ja": "どのようなサポートが利用できますか？",
            "ko": "어떤 종류의 지원이 가능한가요?",
            "ar": "ما نوع الدعم المتاح؟",
            "hi": "किस प्रकार का समर्थन उपलब्ध है？"
        }
    },
    "Does {TOOL} offer a free trial?": {
        "key": "does.tool.offer.a.free.trial",
        "translations": {
            "de": "Bietet {TOOL} eine kostenlose Testversion an?",
            "fr": "{TOOL} propose-t-il un essai gratuit ?",
            "es": "¿{TOOL} ofrece una prueba gratuita?",
            "pt": "{TOOL} oferece um teste gratuito?",
            "zh": "{TOOL} 提供免费试用吗？",
            "ja": "{TOOL} は無料トライアルを提供していますか？",
            "ko": "{TOOL}는 무료 체험을 제공하나요?",
            "ar": "هل يقدم {TOOL} تجربة مجانية؟",
            "hi": "क्या {TOOL} निःशुल्क परीक्षण प्रदान करता है？"
        }
    },
    "How does AI enhance the platform?": {
        "key": "how.does.ai.enhance.the.platform",
        "translations": {
            "de": "Wie verbessert KI die Plattform?",
            "fr": "Comment l'IA améliore-t-elle la plateforme ?",
            "es": "¿Cómo mejora la IA la plataforma?",
            "pt": "Como a IA aprimora a plataforma?",
            "zh": "AI 如何增强平台？",
            "ja": "AI はプラットフォームをどのように強化しますか？",
            "ko": "AI가 플랫폼을 어떻게 향상시키나요?",
            "ar": "كيف يعزز الذكاء الاصطناعي المنصة؟",
            "hi": "AI प्लेटफ़ॉर्म को कैसे बेहतर बनाता है？"
        }
    }
}

GAMING_FILES = {
    "artomatix.html": ("artomatix-i18n.js", "Artomatix", "artomatix"),
    "charismaai.html": ("charismaai-i18n.js", "Charisma.ai", "charismaai"),
    "hidden-door.html": ("hidden-door-i18n.js", "Hidden Door", "hidden-door"),
    "inworld-ai.html": ("inworld-ai-i18n.js", "Inworld AI", "inworld-ai"),
    "latitude-ai-dungeon.html": ("latitude-ai-dungeon-i18n.js", "AI Dungeon", "latitude-ai-dungeon"),
    "ludoai.html": ("ludoai-i18n.js", "Ludo.ai", "ludoai"),
    "promethean-ai.html": ("promethean-ai-i18n.js", "Promethean AI", "promethean-ai"),
    "rct-ai.html": ("rct-ai-i18n.js", "RCT AI", "rct-ai"),
    "replika.html": ("replika-i18n.js", "Replika", "replika"),
    "rosebud-ai.html": ("rosebud-ai-i18n.js", "Rosebud AI", "rosebud-ai"),
    "scenario.html": ("scenario-i18n.js", "Scenario", "scenario")
}

def add_data_i18n_to_html(html_path, tool_name, tool_key):
    """Add data-i18n attributes to FAQ questions in HTML"""

    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    updates = 0

    for question_template, data in FAQ_QUESTIONS.items():
        question = question_template.replace("{TOOL}", tool_name)
        i18n_key = f"review.{tool_key}.faq.{data['key']}"

        # Pattern: <h4>Question text</h4>
        # Replace with: <h4><span data-i18n="key">Question text</span></h4>

        # First, check if already has data-i18n
        if f'data-i18n="{i18n_key}"' in content:
            continue

        # Pattern to match h4 with the question
        pattern = f'(<h4>){re.escape(question)}(</h4>)'
        replacement = f'\\1<span data-i18n="{i18n_key}">{question}</span>\\2'

        new_content = re.sub(pattern, replacement, content)
        if new_content != content:
            content = new_content
            updates += 1

    if content != original_content:
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(content)

    return updates

def add_translations_to_i18n(i18n_path, tool_name, tool_key):
    """Add FAQ question translations to i18n file"""

    with open(i18n_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    additions = 0

    for question_template, data in FAQ_QUESTIONS.items():
        question = question_template.replace("{TOOL}", tool_name)
        base_key = f"review.{tool_key}.faq.{data['key']}"

        # Add to English section first
        if f'"{base_key}"' not in content:
            # Find the FAQ section or end of English section
            en_pattern = r'("en":\s*\{[^}]*"review\.' + re.escape(tool_key) + r'\.frequently\.asked\.questions"[^}]*)'
            match = re.search(en_pattern, content, re.DOTALL)
            if match:
                insert_pos = match.end()
                # Add the new key
                new_entry = f',\n      "{base_key}": "{question}"'
                content = content[:insert_pos] + new_entry + content[insert_pos:]
                additions += 1

        # Add translations for each language
        for lang_code, translation_template in data['translations'].items():
            translation = translation_template.replace("{TOOL}", tool_name)

            # Check if translation already exists
            lang_pattern = f'"{lang_code}":[\\s\\S]*?"{base_key}"'
            if re.search(lang_pattern, content):
                continue

            # Find the language section
            lang_section_pattern = f'("{lang_code}":\\s*{{[^}}]*"review\\.{re.escape(tool_key)}\\.frequently\\.asked\\.questions"[^}}]*)'
            match = re.search(lang_section_pattern, content, re.DOTALL)
            if match:
                insert_pos = match.end()
                new_entry = f',\n      "{base_key}": "{translation}"'
                content = content[:insert_pos] + new_entry + content[insert_pos:]
                additions += 1

    if content != original_content:
        with open(i18n_path, 'w', encoding='utf-8') as f:
            f.write(content)

    return additions

def main():
    html_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\pages\reviews\gaming"
    js_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\js"

    print("="*60)
    print("FIXING FAQ QUESTIONS IN GAMING CATEGORY")
    print("="*60)
    print()

    total_html_updates = 0
    total_i18n_additions = 0

    for html_file, (i18n_file, tool_name, tool_key) in GAMING_FILES.items():
        html_path = os.path.join(html_dir, html_file)
        i18n_path = os.path.join(js_dir, i18n_file)

        if not os.path.exists(html_path):
            print(f"[SKIP] HTML not found: {html_file}")
            continue
        if not os.path.exists(i18n_path):
            print(f"[SKIP] i18n not found: {i18n_file}")
            continue

        print(f"Processing {html_file}...")

        # Update HTML
        html_updates = add_data_i18n_to_html(html_path, tool_name, tool_key)

        # Update i18n
        i18n_additions = add_translations_to_i18n(i18n_path, tool_name, tool_key)

        print(f"  HTML: {html_updates} data-i18n attributes added")
        print(f"  i18n: {i18n_additions} translations added")

        total_html_updates += html_updates
        total_i18n_additions += i18n_additions

    print()
    print("="*60)
    print(f"TOTAL HTML UPDATES: {total_html_updates}")
    print(f"TOTAL i18n ADDITIONS: {total_i18n_additions}")
    print("="*60)

if __name__ == "__main__":
    main()
