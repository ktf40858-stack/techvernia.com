#!/usr/bin/env python3
"""
Complete Quantum Computing translations:
1. Add FAQ question translations
2. Add sidebar translations
"""

import re
import os

# Quantum tools mapping
QUANTUM_TOOLS = {
    "amazon-braket.html": ("amazon-braket-i18n.js", "Amazon Braket", "amazon-braket"),
    "azure-quantum.html": ("azure-quantum-i18n.js", "Azure Quantum", "azure-quantum"),
    "d-wave-leap.html": ("d-wave-leap-i18n.js", "D-Wave Leap", "d-wave-leap"),
    "google-cirq.html": ("google-cirq-i18n.js", "Google Cirq", "google-cirq"),
    "ibm-quantum.html": ("ibm-quantum-i18n.js", "IBM Quantum", "ibm-quantum"),
    "ionq.html": ("ionq-i18n.js", "IonQ", "ionq"),
    "rigetti-qcs.html": ("rigetti-qcs-i18n.js", "Rigetti QCS", "rigetti-qcs"),
    "xanadu-pennylane.html": ("xanadu-pennylane-i18n.js", "Xanadu PennyLane", "xanadu-pennylane")
}

# FAQ questions translations
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

# Sidebar translations
SIDEBAR_TRANSLATIONS = {
    "Rating Breakdown": {
        "key": "sidebar.rating-breakdown",
        "translations": {
            "de": "Bewertungsaufschlüsselung",
            "fr": "Répartition des Notes",
            "es": "Desglose de Calificación",
            "pt": "Detalhamento da Avaliação",
            "zh": "评分详情",
            "ja": "評価の内訳",
            "ko": "평가 세부사항",
            "ar": "تفصيل التقييم",
            "hi": "रेटिंग विवरण"
        }
    },
    "Features": {
        "key": "sidebar.features",
        "translations": {
            "de": "Funktionen",
            "fr": "Fonctionnalités",
            "es": "Características",
            "pt": "Recursos",
            "zh": "功能",
            "ja": "機能",
            "ko": "기능",
            "ar": "الميزات",
            "hi": "विशेषताएं"
        }
    },
    "Ease of Use": {
        "key": "sidebar.ease-of-use",
        "translations": {
            "de": "Benutzerfreundlichkeit",
            "fr": "Facilité d'utilisation",
            "es": "Facilidad de uso",
            "pt": "Facilidade de uso",
            "zh": "易用性",
            "ja": "使いやすさ",
            "ko": "사용 편의성",
            "ar": "سهولة الاستخدام",
            "hi": "उपयोग में आसानी"
        }
    },
    "Value": {
        "key": "sidebar.value",
        "translations": {
            "de": "Wert",
            "fr": "Valeur",
            "es": "Valor",
            "pt": "Valor",
            "zh": "价值",
            "ja": "価値",
            "ko": "가치",
            "ar": "القيمة",
            "hi": "मूल्य"
        }
    },
    "Support": {
        "key": "sidebar.support",
        "translations": {
            "de": "Support",
            "fr": "Support",
            "es": "Soporte",
            "pt": "Suporte",
            "zh": "支持",
            "ja": "サポート",
            "ko": "지원",
            "ar": "الدعم",
            "hi": "सहायता"
        }
    },
    "Performance": {
        "key": "sidebar.performance",
        "translations": {
            "de": "Leistung",
            "fr": "Performance",
            "es": "Rendimiento",
            "pt": "Desempenho",
            "zh": "性能",
            "ja": "パフォーマンス",
            "ko": "성능",
            "ar": "الأداء",
            "hi": "प्रदर्शन"
        }
    },
    "Quick Info": {
        "key": "sidebar.quick-info",
        "translations": {
            "de": "Schnellinfo",
            "fr": "Infos Rapides",
            "es": "Información Rápida",
            "pt": "Informações Rápidas",
            "zh": "快速信息",
            "ja": "クイック情報",
            "ko": "빠른 정보",
            "ar": "معلومات سريعة",
            "hi": "त्वरित जानकारी"
        }
    },
    "Category": {
        "key": "sidebar.category",
        "translations": {
            "de": "Kategorie",
            "fr": "Catégorie",
            "es": "Categoría",
            "pt": "Categoria",
            "zh": "类别",
            "ja": "カテゴリー",
            "ko": "카테고리",
            "ar": "الفئة",
            "hi": "श्रेणी"
        }
    },
    "Quantum": {
        "key": "sidebar.category-quantum",
        "translations": {
            "de": "Quantum",
            "fr": "Quantum",
            "es": "Quantum",
            "pt": "Quantum",
            "zh": "量子",
            "ja": "量子",
            "ko": "양자",
            "ar": "الكمومية",
            "hi": "क्वांटम"
        }
    },
    "Pricing": {
        "key": "sidebar.pricing",
        "translations": {
            "de": "Preise",
            "fr": "Tarifs",
            "es": "Precios",
            "pt": "Preços",
            "zh": "定价",
            "ja": "料金",
            "ko": "가격",
            "ar": "التسعير",
            "hi": "मूल्य निर्धारण"
        }
    },
    "From Free": {
        "key": "sidebar.pricing-from-free",
        "translations": {
            "de": "Ab Kostenlos",
            "fr": "Dès Gratuit",
            "es": "Desde Gratis",
            "pt": "A partir de Grátis",
            "zh": "从免费开始",
            "ja": "無料から",
            "ko": "무료부터",
            "ar": "من مجاني",
            "hi": "मुफ़्त से"
        }
    },
    "Free Trial": {
        "key": "sidebar.free-trial",
        "translations": {
            "de": "Kostenlose Testversion",
            "fr": "Essai Gratuit",
            "es": "Prueba Gratuita",
            "pt": "Teste Gratuito",
            "zh": "免费试用",
            "ja": "無料トライアル",
            "ko": "무료 체험",
            "ar": "تجربة مجانية",
            "hi": "निःशुल्क परीक्षण"
        }
    },
    "14 days": {
        "key": "sidebar.trial-14-days",
        "translations": {
            "de": "14 Tage",
            "fr": "14 jours",
            "es": "14 días",
            "pt": "14 dias",
            "zh": "14天",
            "ja": "14日間",
            "ko": "14일",
            "ar": "14 يومًا",
            "hi": "14 दिन"
        }
    },
    "Platform": {
        "key": "sidebar.platform",
        "translations": {
            "de": "Plattform",
            "fr": "Plateforme",
            "es": "Plataforma",
            "pt": "Plataforma",
            "zh": "平台",
            "ja": "プラットフォーム",
            "ko": "플랫폼",
            "ar": "المنصة",
            "hi": "प्लेटफ़ॉर्म"
        }
    },
    "Web, Mobile": {
        "key": "sidebar.platform-web-mobile",
        "translations": {
            "de": "Web, Mobil",
            "fr": "Web, Mobile",
            "es": "Web, Móvil",
            "pt": "Web, Móvel",
            "zh": "网页，移动",
            "ja": "ウェブ、モバイル",
            "ko": "웹, 모바일",
            "ar": "ويب، موبايل",
            "hi": "वेब, मोबाइल"
        }
    },
    "Table of Contents": {
        "key": "sidebar.table-of-contents",
        "translations": {
            "de": "Inhaltsverzeichnis",
            "fr": "Table des Matières",
            "es": "Tabla de Contenidos",
            "pt": "Índice",
            "zh": "目录",
            "ja": "目次",
            "ko": "목차",
            "ar": "جدول المحتويات",
            "hi": "विषय-सूची"
        }
    },
    "Overview": {
        "key": "toc.overview",
        "translations": {
            "de": "Überblick",
            "fr": "Aperçu",
            "es": "Resumen",
            "pt": "Visão Geral",
            "zh": "概览",
            "ja": "概要",
            "ko": "개요",
            "ar": "نظرة عامة",
            "hi": "अवलोकन"
        }
    },
    "Key Features": {
        "key": "toc.key-features",
        "translations": {
            "de": "Hauptmerkmale",
            "fr": "Fonctionnalités Clés",
            "es": "Características Clave",
            "pt": "Recursos Principais",
            "zh": "主要功能",
            "ja": "主な機能",
            "ko": "주요 기능",
            "ar": "الميزات الرئيسية",
            "hi": "मुख्य विशेषताएं"
        }
    },
    "Pros & Cons": {
        "key": "toc.pros-cons",
        "translations": {
            "de": "Vor- & Nachteile",
            "fr": "Avantages & Inconvénients",
            "es": "Pros & Contras",
            "pt": "Prós & Contras",
            "zh": "优缺点",
            "ja": "長所と短所",
            "ko": "장단점",
            "ar": "الإيجابيات والسلبيات",
            "hi": "फायदे और नुकसान"
        }
    },
    "Use Cases": {
        "key": "toc.use-cases",
        "translations": {
            "de": "Anwendungsfälle",
            "fr": "Cas d'Usage",
            "es": "Casos de Uso",
            "pt": "Casos de Uso",
            "zh": "使用场景",
            "ja": "使用例",
            "ko": "사용 사례",
            "ar": "حالات الاستخدام",
            "hi": "उपयोग के मामले"
        }
    },
    "Comparison": {
        "key": "toc.comparison",
        "translations": {
            "de": "Vergleich",
            "fr": "Comparaison",
            "es": "Comparación",
            "pt": "Comparação",
            "zh": "对比",
            "ja": "比較",
            "ko": "비교",
            "ar": "المقارنة",
            "hi": "तुलना"
        }
    },
    "FAQ": {
        "key": "toc.faq",
        "translations": {
            "de": "FAQ",
            "fr": "FAQ",
            "es": "FAQ",
            "pt": "FAQ",
            "zh": "常见问题",
            "ja": "よくある質問",
            "ko": "FAQ",
            "ar": "الأسئلة الشائعة",
            "hi": "सामान्य प्रश्न"
        }
    },
    "Final Verdict": {
        "key": "toc.final-verdict",
        "translations": {
            "de": "Endgültiges Urteil",
            "fr": "Verdict Final",
            "es": "Veredicto Final",
            "pt": "Veredicto Final",
            "zh": "最终评价",
            "ja": "最終評価",
            "ko": "최종 평가",
            "ar": "الحكم النهائي",
            "hi": "अंतिम निर्णय"
        }
    }
}

def add_faq_data_i18n_to_html(html_path, tool_name, tool_key):
    """Add data-i18n attributes to FAQ questions in HTML"""

    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    updates = 0

    for question_template, data in FAQ_QUESTIONS.items():
        question = question_template.replace("{TOOL}", tool_name)
        i18n_key = f"review.{tool_key}.faq.{data['key']}"

        if f'data-i18n="{i18n_key}"' in content:
            continue

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

def add_sidebar_data_i18n_to_html(html_path):
    """Add data-i18n attributes to sidebar elements in HTML"""

    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    updates = 0

    for text, data in SIDEBAR_TRANSLATIONS.items():
        i18n_key = data['key']

        if f'data-i18n="{i18n_key}"' in content:
            continue

        # Multiple patterns for different HTML structures
        patterns = [
            (f'(<h3[^>]*>(?:[^<]*?))({re.escape(text)})(</h3>)', f'\\1<span data-i18n="{i18n_key}">\\2</span>\\3'),
            (f'(<span class="(?:stat-)?label">)({re.escape(text)})(</span>)', f'\\1<span data-i18n="{i18n_key}">\\2</span>\\3'),
            (f'(<span class="stat-value">)({re.escape(text)})(</span>)', f'\\1<span data-i18n="{i18n_key}">\\2</span>\\3'),
            (f'(<a [^>]*>)({re.escape(text)})(</a>)', f'\\1<span data-i18n="{i18n_key}">\\2</span>\\3')
        ]

        for pattern, replacement in patterns:
            new_content = re.sub(pattern, replacement, content)
            if new_content != content:
                content = new_content
                updates += 1
                break

    if content != original_content:
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(content)

    return updates

def add_translations_to_i18n(i18n_path, tool_name, tool_key):
    """Add FAQ and sidebar translations to i18n file"""

    with open(i18n_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    additions = 0

    # Add FAQ translations
    for question_template, data in FAQ_QUESTIONS.items():
        question = question_template.replace("{TOOL}", tool_name)
        base_key = f"review.{tool_key}.faq.{data['key']}"

        # Add English
        if f'"{base_key}"' not in content:
            en_pattern = r'("en":\s*\{)([\s\S]*?)(\s*\})'
            match = re.search(en_pattern, content)
            if match:
                insert_pos = match.end(2)
                new_entry = f',\n      "{base_key}": "{question}"'
                content = content[:insert_pos] + new_entry + content[insert_pos:]
                additions += 1

        # Add translations
        for lang_code, translation_template in data['translations'].items():
            translation = translation_template.replace("{TOOL}", tool_name)

            lang_pattern = f'"{lang_code}":[\\s\\S]*?"{base_key}"'
            if re.search(lang_pattern, content):
                continue

            lang_section_pattern = f'("{lang_code}":\\s*{{)([\\s\\S]*?)(\\s*}})'
            match = re.search(lang_section_pattern, content)
            if match:
                insert_pos = match.end(2)
                new_entry = f',\n      "{base_key}": "{translation}"'
                content = content[:insert_pos] + new_entry + content[insert_pos:]
                additions += 1

    # Add sidebar translations
    for text, data in SIDEBAR_TRANSLATIONS.items():
        key = data['key']

        # Add English
        if f'"{key}"' not in content:
            en_pattern = r'("en":\s*\{)([\s\S]*?)(\s*\})'
            match = re.search(en_pattern, content)
            if match:
                insert_pos = match.end(2)
                new_entry = f',\n      "{key}": "{text}"'
                content = content[:insert_pos] + new_entry + content[insert_pos:]
                additions += 1

        # Add translations
        for lang_code, translation in data['translations'].items():
            lang_pattern = f'"{lang_code}":[\\s\\S]*?"{key}"'
            if re.search(lang_pattern, content):
                continue

            lang_section_pattern = f'("{lang_code}":\\s*{{)([\\s\\S]*?)(\\s*}})'
            match = re.search(lang_section_pattern, content)
            if match:
                insert_pos = match.end(2)
                new_entry = f',\n      "{key}": "{translation}"'
                content = content[:insert_pos] + new_entry + content[insert_pos:]
                additions += 1

    if content != original_content:
        with open(i18n_path, 'w', encoding='utf-8') as f:
            f.write(content)

    return additions

def main():
    html_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\pages\reviews\quantum"
    js_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\js"

    print("="*60)
    print("COMPLETING QUANTUM COMPUTING TRANSLATIONS")
    print("="*60)
    print()

    total_html_faq = 0
    total_html_sidebar = 0
    total_i18n = 0

    for html_file, (i18n_file, tool_name, tool_key) in QUANTUM_TOOLS.items():
        html_path = os.path.join(html_dir, html_file)
        i18n_path = os.path.join(js_dir, i18n_file)

        if not os.path.exists(html_path) or not os.path.exists(i18n_path):
            print(f"[SKIP] Files not found for {html_file}")
            continue

        print(f"Processing {html_file}...")

        # Update HTML - FAQ
        faq_updates = add_faq_data_i18n_to_html(html_path, tool_name, tool_key)

        # Update HTML - Sidebar
        sidebar_updates = add_sidebar_data_i18n_to_html(html_path)

        # Update i18n
        i18n_additions = add_translations_to_i18n(i18n_path, tool_name, tool_key)

        print(f"  FAQ HTML: {faq_updates} data-i18n added")
        print(f"  Sidebar HTML: {sidebar_updates} data-i18n added")
        print(f"  i18n: {i18n_additions} translations added")

        total_html_faq += faq_updates
        total_html_sidebar += sidebar_updates
        total_i18n += i18n_additions

    print()
    print("="*60)
    print("SUMMARY")
    print("="*60)
    print(f"FAQ HTML updates: {total_html_faq}")
    print(f"Sidebar HTML updates: {total_html_sidebar}")
    print(f"i18n additions: {total_i18n}")
    print()
    print("Quantum Computing translations complete!")

if __name__ == "__main__":
    main()
