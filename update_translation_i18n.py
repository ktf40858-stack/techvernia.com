#!/usr/bin/env python3
"""
Script to complete missing translations in Translation category i18n files
"""

import re
import os

# Translation mappings for all untranslated keys
TRANSLATIONS = {
    "Advanced Analytics": {
        "de": "Erweiterte Analysen",
        "fr": "Analyses Avancées",
        "es": "Análisis Avanzados",
        "pt": "Análises Avançadas",
        "zh": "高级分析",
        "ja": "高度な分析",
        "ko": "고급 분석",
        "ar": "التحليلات المتقدمة",
        "hi": "उन्नत विश्लेषण"
    },
    "Advantages": {
        "de": "Vorteile",
        "fr": "Avantages",
        "es": "Ventajas",
        "pt": "Vantagens",
        "zh": "优势",
        "ja": "利点",
        "ko": "장점",
        "ar": "المزايا",
        "hi": "लाभ"
    },
    "AI-Powered Automation": {
        "de": "KI-gestützte Automatisierung",
        "fr": "Automatisation Alimentée par l'IA",
        "es": "Automatización Impulsada por IA",
        "pt": "Automação Alimentada por IA",
        "zh": "AI驱动的自动化",
        "ja": "AI駆動の自動化",
        "ko": "AI 기반 자동화",
        "ar": "الأتمتة المدعومة بالذكاء الاصطناعي",
        "hi": "AI-संचालित स्वचालन"
    },
    "Best Use Cases": {
        "de": "Beste Anwendungsfälle",
        "fr": "Meilleurs Cas d'Utilisation",
        "es": "Mejores Casos de Uso",
        "pt": "Melhores Casos de Uso",
        "zh": "最佳使用案例",
        "ja": "ベストユースケース",
        "ko": "최적 사용 사례",
        "ar": "أفضل حالات الاستخدام",
        "hi": "सर्वोत्तम उपयोग मामले"
    },
    "Comparison": {
        "de": "Vergleich",
        "fr": "Comparaison",
        "es": "Comparación",
        "pt": "Comparação",
        "zh": "比较",
        "ja": "比較",
        "ko": "비교",
        "ar": "المقارنة",
        "hi": "तुलना"
    },
    "Custom": {
        "de": "Benutzerdefiniert",
        "fr": "Personnalisé",
        "es": "Personalizado",
        "pt": "Personalizado",
        "zh": "定制",
        "ja": "カスタム",
        "ko": "맞춤형",
        "ar": "مخصص",
        "hi": "कस्टम"
    },
    "Disadvantages": {
        "de": "Nachteile",
        "fr": "Inconvénients",
        "es": "Desventajas",
        "pt": "Desvantagens",
        "zh": "缺点",
        "ja": "デメリット",
        "ko": "단점",
        "ar": "العيوب",
        "hi": "नुकसान"
    },
    "Enterprise": {
        "de": "Unternehmen",
        "fr": "Entreprise",
        "es": "Empresarial",
        "pt": "Empresarial",
        "zh": "企业版",
        "ja": "エンタープライズ",
        "ko": "엔터프라이즈",
        "ar": "المؤسسات",
        "hi": "एंटरप्राइज"
    },
    "Enterprise Security": {
        "de": "Unternehmenssicherheit",
        "fr": "Sécurité d'Entreprise",
        "es": "Seguridad Empresarial",
        "pt": "Segurança Empresarial",
        "zh": "企业安全",
        "ja": "エンタープライズセキュリティ",
        "ko": "엔터프라이즈 보안",
        "ar": "أمان المؤسسات",
        "hi": "एंटरप्राइज सुरक्षा"
    },
    "Free Plan": {
        "de": "Kostenloser Plan",
        "fr": "Plan Gratuit",
        "es": "Plan Gratuito",
        "pt": "Plano Gratuito",
        "zh": "免费计划",
        "ja": "無料プラン",
        "ko": "무료 플랜",
        "ar": "الخطة المجانية",
        "hi": "मुफ्त योजना"
    },
    "Key Features": {
        "de": "Hauptmerkmale",
        "fr": "Fonctionnalités Clés",
        "es": "Características Clave",
        "pt": "Recursos Principais",
        "zh": "主要功能",
        "ja": "主な機能",
        "ko": "주요 기능",
        "ar": "الميزات الرئيسية",
        "hi": "मुख्य विशेषताएं"
    },
    "Professional": {
        "de": "Professionell",
        "fr": "Professionnel",
        "es": "Profesional",
        "pt": "Profissional",
        "zh": "专业版",
        "ja": "プロフェッショナル",
        "ko": "프로페셔널",
        "ar": "احترافي",
        "hi": "प्रोफेशनल"
    },
    "Real-Time Collaboration": {
        "de": "Echtzeit-Zusammenarbeit",
        "fr": "Collaboration en Temps Réel",
        "es": "Colaboración en Tiempo Real",
        "pt": "Colaboração em Tempo Real",
        "zh": "实时协作",
        "ja": "リアルタイムコラボレーション",
        "ko": "실시간 협업",
        "ar": "التعاون في الوقت الفعلي",
        "hi": "रीयल-टाइम सहयोग"
    },
    "Seamless Integrations": {
        "de": "Nahtlose Integrationen",
        "fr": "Intégrations Transparentes",
        "es": "Integraciones Perfectas",
        "pt": "Integrações Perfeitas",
        "zh": "无缝集成",
        "ja": "シームレスな統合",
        "ko": "원활한 통합",
        "ar": "التكاملات السلسة",
        "hi": "सहज एकीकरण"
    }
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

def update_file(filepath):
    """Update a single i18n file with complete translations"""
    print(f"Processing {os.path.basename(filepath)}...")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    updates_count = 0

    # For each English phrase that needs translation
    for english, translations in TRANSLATIONS.items():
        # For each non-English language
        for lang_code, translated_text in translations.items():
            # Find and replace the untranslated English text
            # Pattern: "key": "English Text" in non-English language sections
            pattern = f'("{lang_code}":[\\s\\S]*?)(".*?":\\s*")({re.escape(english)})(")'

            def replacer(match):
                nonlocal updates_count
                # Check if this is already the correct translation
                if match.group(3) == english:
                    updates_count += 1
                    return match.group(1) + match.group(2) + translated_text + match.group(4)
                return match.group(0)

            content = re.sub(pattern, replacer, content)

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  [OK] Updated {updates_count} translations in {os.path.basename(filepath)}")
    return updates_count

def main():
    base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\js"

    total_updates = 0
    for filename in FILES:
        filepath = os.path.join(base_dir, filename)
        if os.path.exists(filepath):
            count = update_file(filepath)
            total_updates += count
        else:
            print(f"  [ERROR] File not found: {filename}")

    print(f"\n{'='*60}")
    print(f"TOTAL TRANSLATIONS UPDATED: {total_updates}")
    print(f"FILES PROCESSED: {len(FILES)}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
