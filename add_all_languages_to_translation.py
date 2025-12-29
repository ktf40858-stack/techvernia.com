#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Add all 8 missing languages to Translation tools i18n files
ES, FR, PT, ZH, JA, KO, AR, HI
"""

import os
import json
import re

# Base directory
base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
js_dir = os.path.join(base_dir, "js")

# All 10 Translation tools
tools = {
    "deepl-pro": "DeepL Pro",
    "google-translate-ai": "Google Translate AI",
    "lilt": "Lilt",
    "lokalise": "Lokalise",
    "microsoft-translator": "Microsoft Translator",
    "modernmt": "ModernMT",
    "phrase": "Phrase",
    "smartling": "Smartling",
    "systran": "SYSTRAN",
    "unbabel": "Unbabel"
}

# Common translation mapping for all languages
# Key: English phrase -> {lang: translation}
common_translations = {
    "Overview": {
        "es": "Descripción general",
        "fr": "Aperçu",
        "pt": "Visão geral",
        "zh": "概述",
        "ja": "概要",
        "ko": "개요",
        "ar": "نظرة عامة",
        "hi": "अवलोकन"
    },
    "Key Features": {
        "es": "Características principales",
        "fr": "Fonctionnalités principales",
        "pt": "Recursos principais",
        "zh": "主要功能",
        "ja": "主要機能",
        "ko": "주요 기능",
        "ar": "الميزات الرئيسية",
        "hi": "मुख्य विशेषताएं"
    },
    "AI-Powered Automation": {
        "es": "Automatización impulsada por IA",
        "fr": "Automatisation alimentée par l'IA",
        "pt": "Automação alimentada por IA",
        "zh": "AI驱动的自动化",
        "ja": "AI搭載の自動化",
        "ko": "AI 기반 자동화",
        "ar": "الأتمتة المدعومة بالذكاء الاصطناعي",
        "hi": "एआई-संचालित स्वचालन"
    },
    "Advanced Analytics": {
        "es": "Análisis avanzado",
        "fr": "Analytique avancée",
        "pt": "Análise avançada",
        "zh": "高级分析",
        "ja": "高度な分析",
        "ko": "고급 분석",
        "ar": "التحليلات المتقدمة",
        "hi": "उन्नत विश्लेषण"
    },
    "Seamless Integrations": {
        "es": "Integraciones perfectas",
        "fr": "Intégrations transparentes",
        "pt": "Integrações perfeitas",
        "zh": "无缝集成",
        "ja": "シームレスな統合",
        "ko": "원활한 통합",
        "ar": "التكاملات السلسة",
        "hi": "सहज एकीकरण"
    },
    "Enterprise Security": {
        "es": "Seguridad empresarial",
        "fr": "Sécurité d'entreprise",
        "pt": "Segurança empresarial",
        "zh": "企业安全",
        "ja": "エンタープライズセキュリティ",
        "ko": "엔터프라이즈 보안",
        "ar": "أمن المؤسسات",
        "hi": "एंटरप्राइज़ सुरक्षा"
    },
    "Real-Time Collaboration": {
        "es": "Colaboración en tiempo real",
        "fr": "Collaboration en temps réel",
        "pt": "Colaboração em tempo real",
        "zh": "实时协作",
        "ja": "リアルタイムコラボレーション",
        "ko": "실시간 협업",
        "ar": "التعاون في الوقت الفعلي",
        "hi": "रीयल-टाइम सहयोग"
    },
    "Customizable Workflows": {
        "es": "Flujos de trabajo personalizables",
        "fr": "Flux de travail personnalisables",
        "pt": "Fluxos de trabalho personalizáveis",
        "zh": "可自定义工作流程",
        "ja": "カスタマイズ可能なワークフロー",
        "ko": "맞춤형 워크플로우",
        "ar": "سير عمل قابل للتخصيص",
        "hi": "अनुकूलन योग्य वर्कफ़्लो"
    },
    "Pros & Cons": {
        "es": "Ventajas y desventajas",
        "fr": "Avantages et inconvénients",
        "pt": "Prós e contras",
        "zh": "优缺点",
        "ja": "長所と短所",
        "ko": "장단점",
        "ar": "الإيجابيات والسلبيات",
        "hi": "फायदे और नुकसान"
    },
    "Advantages": {
        "es": "Ventajas",
        "fr": "Avantages",
        "pt": "Vantagens",
        "zh": "优势",
        "ja": "利点",
        "ko": "장점",
        "ar": "المزايا",
        "hi": "लाभ"
    },
    "Disadvantages": {
        "es": "Desventajas",
        "fr": "Inconvénients",
        "pt": "Desvantagens",
        "zh": "缺点",
        "ja": "欠点",
        "ko": "단점",
        "ar": "العيوب",
        "hi": "नुकसान"
    },
    "Pricing": {
        "es": "Precios",
        "fr": "Tarification",
        "pt": "Preços",
        "zh": "定价",
        "ja": "価格",
        "ko": "가격",
        "ar": "التسعير",
        "hi": "मूल्य निर्धारण"
    },
    "Free Plan": {
        "es": "Plan gratuito",
        "fr": "Plan gratuit",
        "pt": "Plano gratuito",
        "zh": "免费计划",
        "ja": "無料プラン",
        "ko": "무료 플랜",
        "ar": "خطة مجانية",
        "hi": "मुफ्त योजना"
    },
    "Professional Plan": {
        "es": "Plan profesional",
        "fr": "Plan professionnel",
        "pt": "Plano profissional",
        "zh": "专业计划",
        "ja": "プロフェッショナルプラン",
        "ko": "프로페셔널 플랜",
        "ar": "خطة احترافية",
        "hi": "व्यावसायिक योजना"
    },
    "Enterprise Plan": {
        "es": "Plan empresarial",
        "fr": "Plan entreprise",
        "pt": "Plano empresarial",
        "zh": "企业计划",
        "ja": "エンタープライズプラン",
        "ko": "엔터프라이즈 플랜",
        "ar": "خطة المؤسسات",
        "hi": "एंटरप्राइज़ योजना"
    },
    "Custom Pricing": {
        "es": "Precios personalizados",
        "fr": "Tarification personnalisée",
        "pt": "Preços personalizados",
        "zh": "定制定价",
        "ja": "カスタム価格",
        "ko": "맞춤 가격",
        "ar": "تسعير مخصص",
        "hi": "कस्टम मूल्य निर्धारण"
    },
    "Best Use Cases": {
        "es": "Mejores casos de uso",
        "fr": "Meilleurs cas d'utilisation",
        "pt": "Melhores casos de uso",
        "zh": "最佳用例",
        "ja": "最適な使用例",
        "ko": "최적의 사용 사례",
        "ar": "أفضل حالات الاستخدام",
        "hi": "सर्वोत्तम उपयोग के मामले"
    },
    "Comparison": {
        "es": "Comparación",
        "fr": "Comparaison",
        "pt": "Comparação",
        "zh": "比较",
        "ja": "比較",
        "ko": "비교",
        "ar": "المقارنة",
        "hi": "तुलना"
    },
    "Key Advantages": {
        "es": "Ventajas clave",
        "fr": "Avantages clés",
        "pt": "Vantagens principais",
        "zh": "主要优势",
        "ja": "主な利点",
        "ko": "주요 장점",
        "ar": "المزايا الرئيسية",
        "hi": "मुख्य लाभ"
    },
    "Frequently Asked Questions": {
        "es": "Preguntas frecuentes",
        "fr": "Questions fréquemment posées",
        "pt": "Perguntas frequentes",
        "zh": "常见问题",
        "ja": "よくある質問",
        "ko": "자주 묻는 질문",
        "ar": "الأسئلة الشائعة",
        "hi": "अक्सर पूछे जाने वाले प्रश्न"
    },
    "Final Verdict": {
        "es": "Veredicto final",
        "fr": "Verdict final",
        "pt": "Veredicto final",
        "zh": "最终判决",
        "ja": "最終評価",
        "ko": "최종 평가",
        "ar": "الحكم النهائي",
        "hi": "अंतिम फैसला"
    },
    "Excellent Choice": {
        "es": "Excelente elección",
        "fr": "Excellent choix",
        "pt": "Excelente escolha",
        "zh": "绝佳选择",
        "ja": "優れた選択",
        "ko": "훌륭한 선택",
        "ar": "اختيار ممتاز",
        "hi": "उत्कृष्ट विकल्प"
    },
    "Try Free": {
        "es": "Prueba gratis",
        "fr": "Essai gratuit",
        "pt": "Experimente grátis",
        "zh": "免费试用",
        "ja": "無料で試す",
        "ko": "무료 체험",
        "ar": "جرب مجانا",
        "hi": "मुफ्त में आज़माएं"
    },
    "View Pricing": {
        "es": "Ver precios",
        "fr": "Voir les tarifs",
        "pt": "Ver preços",
        "zh": "查看定价",
        "ja": "価格を見る",
        "ko": "가격 보기",
        "ar": "عرض الأسعار",
        "hi": "मूल्य निर्धारण देखें"
    }
}

def translate_value(english_value, target_lang, tool_name):
    """Translate an English value to target language"""

    # Direct match
    if english_value in common_translations:
        return common_translations[english_value].get(target_lang, english_value)

    # Check for partial matches and translate phrases
    result = english_value
    for en_phrase, translations in common_translations.items():
        if en_phrase in result:
            result = result.replace(en_phrase, translations.get(target_lang, en_phrase))

    return result

def add_languages_to_file(tool_key, tool_name):
    """Add all missing languages to an i18n file"""

    filepath = os.path.join(js_dir, f"{tool_key}-i18n.js")

    if not os.path.exists(filepath):
        return None

    # Read existing file
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract variable name
    var_match = re.search(r'const\s+(\w+)\s*=', content)
    if not var_match:
        return None
    var_name = var_match.group(1)

    # Extract existing translations object
    json_match = re.search(r'const\s+\w+\s*=\s*(\{.+?\});', content, re.DOTALL)
    if not json_match:
        return None

    json_str = json_match.group(1)
    translations = json.loads(json_str)

    # Check if we already have all languages
    existing_langs = set(translations.keys())
    all_langs = {'en', 'de', 'es', 'fr', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi'}
    missing_langs = all_langs - existing_langs

    if not missing_langs:
        return 0  # Already has all languages

    # Get English translations as base
    en_translations = translations.get('en', {})

    # Generate translations for missing languages
    for lang in missing_langs:
        translations[lang] = {}
        for key, en_value in en_translations.items():
            translations[lang][key] = translate_value(en_value, lang, tool_name)

    # Rebuild file content
    new_content = f"// Translation data\nconst {var_name} = "
    new_content += json.dumps(translations, ensure_ascii=False, indent=2)
    new_content += ";\n\n"

    # Add event listener
    new_content += "// Listen for language changes\n"
    new_content += "window.addEventListener('languageChanged', (e) => {\n"
    new_content += "  const lang = e.detail.language;\n"
    new_content += f"  const translations = {var_name}[lang] || {var_name}['en'];\n"
    new_content += "  \n"
    new_content += "  // Update all elements with data-i18n attributes\n"
    new_content += "  document.querySelectorAll('[data-i18n]').forEach(element => {\n"
    new_content += "    const key = element.getAttribute('data-i18n');\n"
    new_content += "    if (translations[key]) {\n"
    new_content += "      element.textContent = translations[key];\n"
    new_content += "    }\n"
    new_content += "  });\n"
    new_content += "});\n"

    # Write file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return len(missing_langs)

# Main execution
print("=" * 70)
print("ADDING ALL LANGUAGES TO TRANSLATION TOOLS")
print("=" * 70)
print()

results = []

for tool_key, tool_name in tools.items():
    print(f"Processing {tool_name}...")

    try:
        langs_added = add_languages_to_file(tool_key, tool_name)

        if langs_added is None:
            results.append({"tool": tool_name, "status": "ERROR", "error": "File error"})
            print(f"  [ERROR] Could not process file")
        elif langs_added == 0:
            results.append({"tool": tool_name, "status": "SKIP", "langs": 0})
            print(f"  [SKIP] Already has all languages")
        else:
            results.append({"tool": tool_name, "status": "SUCCESS", "langs": langs_added})
            print(f"  [OK] Added {langs_added} languages")
    except Exception as e:
        results.append({"tool": tool_name, "status": "ERROR", "error": str(e)})
        print(f"  [ERROR] {str(e)}")

    print()

# Summary
print("=" * 70)
print("SUMMARY")
print("=" * 70)
print()

success_count = sum(1 for r in results if r["status"] == "SUCCESS")
total_langs = sum(r.get("langs", 0) for r in results if r["status"] == "SUCCESS")

print(f"Tools processed: {len(results)}")
print(f"Successfully updated: {success_count}")
print(f"Total languages added: {total_langs}")
print()

if success_count > 0:
    print("[SUCCESS] Languages added to tools!")
else:
    print("[INFO] No changes needed")

print()
print("=" * 70)
