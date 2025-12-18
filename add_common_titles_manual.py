#!/usr/bin/env python3
"""
Ajouter les titres communs corrects manuellement
"""
import json
import re

print("=" * 80)
print("📋 AJOUT DES TITRES COMMUNS (VERSION MANUELLE)")
print("=" * 80)
print()

# Titres communs avec traductions correctes
common_titles = {
    "en": {
        "review.common.try.it.now": "Try It Now",
        "review.common.overview": "Overview",
        "review.common.key.features": "Key Features",
        "review.common.pricing.plans": "Pricing Plans",
        "review.common.best.use.cases": "Best Use Cases",
        "review.common.comparison.with.competitors": "Comparison with Competitors",
        "review.common.screenshots.interface": "Screenshots & Interface",
        "review.common.final.verdict": "Final Verdict",
        "review.common.frequently.asked.questions": "Frequently Asked Questions",
        "review.common.pros.cons": "Pros & Cons",
        "review.common.additional": "Additional Features"
    },
    "es": {
        "review.common.try.it.now": "Pruébalo Ahora",
        "review.common.overview": "Sinopsis",
        "review.common.key.features": "Características Clave",
        "review.common.pricing.plans": "Planes de Precios",
        "review.common.best.use.cases": "Mejores Casos de Uso",
        "review.common.comparison.with.competitors": "Comparación con Competidores",
        "review.common.screenshots.interface": "Capturas de Pantalla e Interfaz",
        "review.common.final.verdict": "Veredicto Final",
        "review.common.frequently.asked.questions": "Preguntas Frecuentes",
        "review.common.pros.cons": "Pros y Contras",
        "review.common.additional": "Características Adicionales"
    },
    "fr": {
        "review.common.try.it.now": "Essayez Maintenant",
        "review.common.overview": "Aperçu",
        "review.common.key.features": "Fonctionnalités Clés",
        "review.common.pricing.plans": "Plans Tarifaires",
        "review.common.best.use.cases": "Meilleurs Cas d'Usage",
        "review.common.comparison.with.competitors": "Comparaison avec Concurrents",
        "review.common.screenshots.interface": "Captures d'Écran et Interface",
        "review.common.final.verdict": "Verdict Final",
        "review.common.frequently.asked.questions": "Questions Fréquemment Posées",
        "review.common.pros.cons": "Avantages et Inconvénients",
        "review.common.additional": "Fonctionnalités Supplémentaires"
    },
    "de": {
        "review.common.try.it.now": "Jetzt Ausprobieren",
        "review.common.overview": "Überblick",
        "review.common.key.features": "Hauptfunktionen",
        "review.common.pricing.plans": "Preispläne",
        "review.common.best.use.cases": "Beste Anwendungsfälle",
        "review.common.comparison.with.competitors": "Vergleich mit Konkurrenten",
        "review.common.screenshots.interface": "Screenshots und Benutzeroberfläche",
        "review.common.final.verdict": "Endgültiges Urteil",
        "review.common.frequently.asked.questions": "Häufig Gestellte Fragen",
        "review.common.pros.cons": "Vor- und Nachteile",
        "review.common.additional": "Zusätzliche Funktionen"
    },
    "pt": {
        "review.common.try.it.now": "Experimente Agora",
        "review.common.overview": "Visão Geral",
        "review.common.key.features": "Recursos Principais",
        "review.common.pricing.plans": "Planos de Preços",
        "review.common.best.use.cases": "Melhores Casos de Uso",
        "review.common.comparison.with.competitors": "Comparação com Concorrentes",
        "review.common.screenshots.interface": "Capturas de Tela e Interface",
        "review.common.final.verdict": "Veredicto Final",
        "review.common.frequently.asked.questions": "Perguntas Frequentes",
        "review.common.pros.cons": "Prós e Contras",
        "review.common.additional": "Recursos Adicionais"
    },
    "zh": {
        "review.common.try.it.now": "立即试用",
        "review.common.overview": "概述",
        "review.common.key.features": "主要功能",
        "review.common.pricing.plans": "价格计划",
        "review.common.best.use.cases": "最佳使用案例",
        "review.common.comparison.with.competitors": "与竞争对手比较",
        "review.common.screenshots.interface": "截图和界面",
        "review.common.final.verdict": "最终评价",
        "review.common.frequently.asked.questions": "常见问题",
        "review.common.pros.cons": "优缺点",
        "review.common.additional": "附加功能"
    },
    "ja": {
        "review.common.try.it.now": "今すぐ試す",
        "review.common.overview": "概要",
        "review.common.key.features": "主な機能",
        "review.common.pricing.plans": "料金プラン",
        "review.common.best.use.cases": "最適なユースケース",
        "review.common.comparison.with.competitors": "競合他社との比較",
        "review.common.screenshots.interface": "スクリーンショットとインターフェース",
        "review.common.final.verdict": "最終評価",
        "review.common.frequently.asked.questions": "よくある質問",
        "review.common.pros.cons": "長所と短所",
        "review.common.additional": "追加機能"
    },
    "ko": {
        "review.common.try.it.now": "지금 시도하기",
        "review.common.overview": "개요",
        "review.common.key.features": "주요 기능",
        "review.common.pricing.plans": "가격 계획",
        "review.common.best.use.cases": "최적 사용 사례",
        "review.common.comparison.with.competitors": "경쟁사와 비교",
        "review.common.screenshots.interface": "스크린샷 및 인터페이스",
        "review.common.final.verdict": "최종 평가",
        "review.common.frequently.asked.questions": "자주 묻는 질문",
        "review.common.pros.cons": "장단점",
        "review.common.additional": "추가 기능"
    },
    "ar": {
        "review.common.try.it.now": "جربه الآن",
        "review.common.overview": "نظرة عامة",
        "review.common.key.features": "الميزات الرئيسية",
        "review.common.pricing.plans": "خطط الأسعار",
        "review.common.best.use.cases": "أفضل حالات الاستخدام",
        "review.common.comparison.with.competitors": "مقارنة مع المنافسين",
        "review.common.screenshots.interface": "لقطات الشاشة والواجهة",
        "review.common.final.verdict": "الحكم النهائي",
        "review.common.frequently.asked.questions": "الأسئلة الشائعة",
        "review.common.pros.cons": "الإيجابيات والسلبيات",
        "review.common.additional": "ميزات إضافية"
    },
    "hi": {
        "review.common.try.it.now": "अभी आज़माएं",
        "review.common.overview": "अवलोकन",
        "review.common.key.features": "मुख्य विशेषताएं",
        "review.common.pricing.plans": "मूल्य निर्धारण योजनाएं",
        "review.common.best.use.cases": "सर्वोत्तम उपयोग के मामले",
        "review.common.comparison.with.competitors": "प्रतियोगियों के साथ तुलना",
        "review.common.screenshots.interface": "स्क्रीनशॉट और इंटरफ़ेस",
        "review.common.final.verdict": "अंतिम निर्णय",
        "review.common.frequently.asked.questions": "अक्सर पूछे जाने वाले प्रश्न",
        "review.common.pros.cons": "फायदे और नुकसान",
        "review.common.additional": "अतिरिक्त सुविधाएँ"
    }
}

# Outils image
image_tools = [
    'adobe-firefly',
    'canva-ai',
    'clipdrop',
    'dall-e-3',
    'ideogram',
    'leonardo-ai',
    'midjourney',
    'stable-diffusion'
]

for tool in image_tools:
    i18n_file = f'GenuisNet.ai/js/{tool}-i18n.js'

    print(f"🔧 Traitement: {tool}-i18n.js")

    # Lire le fichier
    with open(i18n_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pour chaque langue, remplacer les clés communes incorrectes
    for lang in common_titles.keys():
        # Trouver et remplacer chaque clé commune dans cette section de langue
        for key, value in common_titles[lang].items():
            # Échapper les caractères spéciaux pour la valeur
            escaped_value = value.replace('"', '\\"')

            # Pattern pour trouver cette clé dans la section de langue
            # Chercher: "review.common.xxx": "n'importe quoi"
            pattern = rf'("{key}":\s*)"[^"]*"'
            replacement = rf'\1"{escaped_value}"'

            content = re.sub(pattern, replacement, content)

    # Sauvegarder
    with open(i18n_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  ✅ Titres communs corrigés")

print()
print("=" * 80)
print("✅ TOUS LES TITRES COMMUNS ONT ÉTÉ CORRIGÉS!")
print("=" * 80)
