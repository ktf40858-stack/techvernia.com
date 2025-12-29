#!/usr/bin/env python3
"""
Complete ALL missing translations in Translation category i18n files
This script translates ALL remaining English text in non-English language sections
"""

import re
import os

# Generic translations that work for any tool (use {TOOL} as placeholder)
GENERIC_TRANSLATIONS = {
    # Main descriptions
    "{TOOL} is a powerful, feature-rich translation platform that delivers exceptional value for teams of all sizes. Highly recommended.": {
        "de": "{TOOL} ist eine leistungsstarke, funktionsreiche Übersetzungsplattform, die außergewöhnlichen Wert für Teams jeder Größe bietet. Sehr empfehlenswert.",
        "fr": "{TOOL} est une plateforme de traduction puissante et riche en fonctionnalités qui offre une valeur exceptionnelle pour les équipes de toutes tailles. Hautement recommandé.",
        "es": "{TOOL} es una plataforma de traducción potente y rica en funciones que ofrece un valor excepcional para equipos de todos los tamaños. Muy recomendado.",
        "pt": "{TOOL} é uma plataforma de tradução poderosa e rica em recursos que oferece valor excepcional para equipes de todos os tamanhos. Altamente recomendado.",
        "zh": "{TOOL} 是一个功能强大、功能丰富的翻译平台，为各种规模的团队提供卓越的价值。强烈推荐。",
        "ja": "{TOOL}は、あらゆる規模のチームに卓越した価値を提供する、強力で機能豊富な翻訳プラットフォームです。強くお勧めします。",
        "ko": "{TOOL}는 모든 규모의 팀에 뛰어난 가치를 제공하는 강력하고 기능이 풍부한 번역 플랫폼입니다. 적극 권장합니다.",
        "ar": "{TOOL} هي منصة ترجمة قوية وغنية بالميزات تقدم قيمة استثنائية للفرق من جميع الأحجام. موصى بها بشدة.",
        "hi": "{TOOL} एक शक्तिशाली, सुविधा संपन्न अनुवाद प्लेटफ़ॉर्म है जो सभी आकारों की टीमों के लिए असाधारण मूल्य प्रदान करता है। अत्यधिक अनुशंसित।"
    },

    # Section titles
    "{TOOL} Excels For:": {
        "de": "{TOOL} Überzeugt Für:",
        "fr": "{TOOL} Excelle Pour :",
        "es": "{TOOL} Sobresale Para:",
        "pt": "{TOOL} Destaca-se Para:",
        "zh": "{TOOL} 的优势场景：",
        "ja": "{TOOL}が優れている用途：",
        "ko": "{TOOL}가 뛰어난 분야:",
        "ar": "{TOOL} يتفوق في:",
        "hi": "{TOOL} इसमें उत्कृष्ट है:"
    },

    "{TOOL} vs Competitors": {
        "de": "{TOOL} vs. Konkurrenten",
        "fr": "{TOOL} vs. Concurrents",
        "es": "{TOOL} vs. Competidores",
        "pt": "{TOOL} vs. Concorrentes",
        "zh": "{TOOL} 与竞争对手",
        "ja": "{TOOL} vs. 競合他社",
        "ko": "{TOOL} vs. 경쟁사",
        "ar": "{TOOL} مقابل المنافسين",
        "hi": "{TOOL} बनाम प्रतिस्पर्धी"
    },

    "Explore {TOOL}'s interface:": {
        "de": "Erkunden Sie die Benutzeroberfläche von {TOOL}:",
        "fr": "Explorez l'interface de {TOOL} :",
        "es": "Explora la interfaz de {TOOL}:",
        "pt": "Explore a interface do {TOOL}:",
        "zh": "探索 {TOOL} 的界面：",
        "ja": "{TOOL}のインターフェースを探索：",
        "ko": "{TOOL}의 인터페이스 살펴보기:",
        "ar": "استكشف واجهة {TOOL}:",
        "hi": "{TOOL} के इंटरफ़ेस का अन्वेषण करें:"
    },

    # Common sections
    "Final Verdict": {
        "de": "Abschließendes Urteil",
        "fr": "Verdict Final",
        "es": "Veredicto Final",
        "pt": "Veredicto Final",
        "zh": "最终评价",
        "ja": "最終評価",
        "ko": "최종 평가",
        "ar": "الحكم النهائي",
        "hi": "अंतिम निर्णय"
    },

    "Frequently Asked Questions": {
        "de": "Häufig Gestellte Fragen",
        "fr": "Questions Fréquemment Posées",
        "es": "Preguntas Frecuentes",
        "pt": "Perguntas Frequentes",
        "zh": "常见问题",
        "ja": "よくある質問",
        "ko": "자주 묻는 질문",
        "ar": "الأسئلة الشائعة",
        "hi": "अक्सर पूछे जाने वाले प्रश्न"
    },

    # CTAs
    "Try {TOOL} Free": {
        "de": "{TOOL} Kostenlos Testen",
        "fr": "Essayer {TOOL} Gratuitement",
        "es": "Probar {TOOL} Gratis",
        "pt": "Experimentar {TOOL} Grátis",
        "zh": "免费试用 {TOOL}",
        "ja": "{TOOL}を無料で試す",
        "ko": "{TOOL} 무료 체험",
        "ar": "جرب {TOOL} مجانًا",
        "hi": "{TOOL} मुफ्त में आज़माएं"
    },

    "Try {TOOL} today and experience the power of AI-driven automation.": {
        "de": "Testen Sie {TOOL} heute und erleben Sie die Kraft der KI-gesteuerten Automatisierung.",
        "fr": "Essayez {TOOL} aujourd'hui et découvrez la puissance de l'automatisation pilotée par l'IA.",
        "es": "Pruebe {TOOL} hoy y experimente el poder de la automatización impulsada por IA.",
        "pt": "Experimente {TOOL} hoje e descubra o poder da automação impulsionada por IA.",
        "zh": "立即试用 {TOOL}，体验 AI 驱动自动化的强大功能。",
        "ja": "今すぐ{TOOL}を試して、AI駆動の自動化の力を体験してください。",
        "ko": "오늘 {TOOL}를 사용해보고 AI 기반 자동화의 힘을 경험하세요.",
        "ar": "جرب {TOOL} اليوم واختبر قوة الأتمتة المدعومة بالذكاء الاصطناعي.",
        "hi": "आज ही {TOOL} आज़माएं और AI-संचालित स्वचालन की शक्ति का अनुभव करें।"
    },

    # Integrations
    "{TOOL} integrates with 100+ popular platforms including Slack, Microsoft Teams, Salesforce, Google Workspace, and many more. A robust API enables custom integrations.": {
        "de": "{TOOL} integriert sich mit über 100 beliebten Plattformen, darunter Slack, Microsoft Teams, Salesforce, Google Workspace und viele mehr. Eine robuste API ermöglicht kundenspezifische Integrationen.",
        "fr": "{TOOL} s'intègre avec plus de 100 plateformes populaires, notamment Slack, Microsoft Teams, Salesforce, Google Workspace et bien d'autres. Une API robuste permet des intégrations personnalisées.",
        "es": "{TOOL} se integra con más de 100 plataformas populares, incluidas Slack, Microsoft Teams, Salesforce, Google Workspace y muchas más. Una API robusta permite integraciones personalizadas.",
        "pt": "{TOOL} integra-se com mais de 100 plataformas populares, incluindo Slack, Microsoft Teams, Salesforce, Google Workspace e muito mais. Uma API robusta permite integrações personalizadas.",
        "zh": "{TOOL} 与 100 多个流行平台集成，包括 Slack、Microsoft Teams、Salesforce、Google Workspace 等。强大的 API 支持自定义集成。",
        "ja": "{TOOL}は、Slack、Microsoft Teams、Salesforce、Google Workspaceなど、100以上の人気プラットフォームと統合します。堅牢なAPIによりカスタム統合が可能です。",
        "ko": "{TOOL}는 Slack, Microsoft Teams, Salesforce, Google Workspace 등 100개 이상의 인기 플랫폼과 통합됩니다. 강력한 API를 통해 맞춤형 통합이 가능합니다.",
        "ar": "يتكامل {TOOL} مع أكثر من 100 منصة شائعة بما في ذلك Slack وMicrosoft Teams وSalesforce وGoogle Workspace والعديد غيرها. تمكن واجهة برمجة تطبيقات قوية من التكاملات المخصصة.",
        "hi": "{TOOL} Slack, Microsoft Teams, Salesforce, Google Workspace और कई अन्य सहित 100+ लोकप्रिय प्लेटफ़ॉर्म के साथ एकीकृत होता है। एक मजबूत API कस्टम एकीकरण को सक्षम बनाता है।"
    },

    # Pricing
    "{TOOL} offers flexible pricing plans to suit different organization sizes and needs:": {
        "de": "{TOOL} bietet flexible Preispläne für verschiedene Unternehmensgrößen und Bedürfnisse:",
        "fr": "{TOOL} propose des plans tarifaires flexibles adaptés à différentes tailles d'organisation et besoins :",
        "es": "{TOOL} ofrece planes de precios flexibles para adaptarse a diferentes tamaños de organización y necesidades:",
        "pt": "{TOOL} oferece planos de preços flexíveis para atender a diferentes tamanhos e necessidades de organização:",
        "zh": "{TOOL} 提供灵活的定价计划，以适应不同的组织规模和需求：",
        "ja": "{TOOL}は、さまざまな組織規模とニーズに合わせた柔軟な料金プランを提供しています：",
        "ko": "{TOOL}는 다양한 조직 규모와 요구 사항에 맞는 유연한 요금제를 제공합니다:",
        "ar": "يقدم {TOOL} خطط تسعير مرنة لتناسب أحجام واحتياجات المنظمات المختلفة:",
        "hi": "{TOOL} विभिन्न संगठन आकारों और जरूरतों के अनुरूप लचीली मूल्य निर्धारण योजनाएं प्रदान करता है:"
    },

    # Migration
    "Absolutely. {TOOL} provides migration tools and dedicated support to help you seamlessly transition from competing platforms with minimal downtime.": {
        "de": "Absolut. {TOOL} bietet Migrationswerkzeuge und dedizierten Support, um Ihnen einen nahtlosen Übergang von konkurrierenden Plattformen mit minimaler Ausfallzeit zu ermöglichen.",
        "fr": "Absolument. {TOOL} fournit des outils de migration et un support dédié pour vous aider à effectuer une transition transparente depuis des plateformes concurrentes avec un temps d'arrêt minimal.",
        "es": "Por supuesto. {TOOL} proporciona herramientas de migración y soporte dedicado para ayudarlo a realizar una transición sin problemas desde plataformas competidoras con un tiempo de inactividad mínimo.",
        "pt": "Absolutamente. {TOOL} fornece ferramentas de migração e suporte dedicado para ajudá-lo a fazer uma transição perfeita de plataformas concorrentes com tempo de inatividade mínimo.",
        "zh": "当然可以。{TOOL} 提供迁移工具和专门支持，帮助您从竞争平台无缝过渡，停机时间最短。",
        "ja": "もちろんです。{TOOL}は、競合プラットフォームからのシームレスな移行をサポートし、ダウンタイムを最小限に抑えるための移行ツールと専用サポートを提供します。",
        "ko": "물론입니다. {TOOL}는 경쟁 플랫폼에서 최소한의 다운타임으로 원활하게 전환할 수 있도록 마이그레이션 도구와 전담 지원을 제공합니다.",
        "ar": "بالتأكيد. يوفر {TOOL} أدوات الترحيل والدعم المخصص لمساعدتك على الانتقال بسلاسة من المنصات المنافسة مع الحد الأدنى من وقت التوقف.",
        "hi": "बिल्कुल। {TOOL} न्यूनतम डाउनटाइम के साथ प्रतिस्पर्धी प्लेटफ़ॉर्म से निर्बाध रूप से संक्रमण में मदद करने के लिए माइग्रेशन उपकरण और समर्पित सहायता प्रदान करता है।"
    },
}

# Files to update
FILES = [
    "deepl-pro-i18n.js",
    "google-translate-ai-i18n.js",
    "lilt-i18n.js",
    "lokalise-i18n.js",
    "microsoft-translator-i18n.js",
    "modernmt-i18n.js",
    "phrase-i18n.js",
    "smartling-i18n.js",
    "systran-i18n.js",
    "unbabel-i18n.js"
]

# Tool name mappings
TOOL_NAMES = {
    "deepl-pro": "DeepL Pro",
    "google-translate-ai": "Google Translate AI",
    "lilt": "Lilt",
    "lokalise": "Lokalise",
    "microsoft-translator": "Microsoft Translator",
    "modernmt": "ModernMT",
    "phrase": "Phrase",
    "smartling": "Smartling",
    "systran": "Systran",
    "unbabel": "Unbabel"
}

def get_tool_name(filename):
    """Extract tool name from filename"""
    for key in TOOL_NAMES:
        if filename.startswith(key):
            return TOOL_NAMES[key]
    return "Tool"

def update_file_complete(filepath):
    """Update a file with ALL missing translations"""
    filename = os.path.basename(filepath)
    tool_name = get_tool_name(filename)

    print(f"Processing {filename}...")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    updates_count = 0

    # For each English phrase template
    for english_template, translations in GENERIC_TRANSLATIONS.items():
        # Replace {TOOL} with actual tool name
        english_text = english_template.replace("{TOOL}", tool_name)

        # For each language
        for lang_code, translation_template in translations.items():
            # Replace {TOOL} in translation
            translated_text = translation_template.replace("{TOOL}", tool_name)

            # Escape special regex characters
            english_escaped = re.escape(english_text)

            # Find and replace in the specific language section
            # Pattern: find text in specific language section
            pattern = f'("{lang_code}":[\\s\\S]*?)(".*?":\\s*")({english_escaped})(")'

            def replacer(match):
                nonlocal updates_count
                updates_count += 1
                return match.group(1) + match.group(2) + translated_text + match.group(4)

            content = re.sub(pattern, replacer, content)

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  [OK] Updated {updates_count} translations in {filename}")
    return updates_count

def main():
    base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\js"

    total_updates = 0
    for filename in FILES:
        filepath = os.path.join(base_dir, filename)
        if os.path.exists(filepath):
            count = update_file_complete(filepath)
            total_updates += count
        else:
            print(f"  [ERROR] File not found: {filename}")

    print(f"\n{'='*60}")
    print(f"TOTAL TRANSLATIONS UPDATED: {total_updates}")
    print(f"FILES PROCESSED: {len(FILES)}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
