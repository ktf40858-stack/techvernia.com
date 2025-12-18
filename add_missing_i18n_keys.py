#!/usr/bin/env python3
"""
Script pour ajouter les clés i18n manquantes dans toutes les langues
"""

def add_missing_i18n_keys():
    """Ajoute les clés i18n manquantes"""

    file_path = "GenuisNet.ai/js/i18n.js"

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Définir les nouvelles clés avec traductions
    new_keys = {
        'en': {
            '"stats.tools": "AI Tools",': '"stats.tools": "AI Tools",\n        "stats.reviews": "Expert Reviews",\n        "hero.featuring-tools-from": "Featuring tools from",',
            '"card.curated-selection": "Curated Selection",': '"card.curated-selection": "Curated Selection",\n        "card.curated-selection-desc": "Handpicked AI tools across 22 categories, tested and reviewed by experts",',
            '"card.always-updated": "Always Updated",': '"card.always-updated": "Always Updated",\n        "card.always-updated-desc": "Fresh reviews and comparisons to keep you ahead in the AI revolution",',
            '"card.expert-insights": "Expert Insights",': '"card.expert-insights": "Expert Insights",\n        "card.expert-insights-desc": "In-depth analysis from beginners to enterprise solutions",',
        },
        'fr': {
            '"stats.tools": "Outils IA",': '"stats.tools": "Outils IA",\n        "stats.reviews": "Avis d\'Experts",\n        "hero.featuring-tools-from": "Avec des outils de",',
            '"card.curated-selection": "Sélection Curatée",': '"card.curated-selection": "Sélection Curatée",\n        "card.curated-selection-desc": "Outils IA triés sur le volet dans 22 catégories, testés et évalués par des experts",',
            '"card.always-updated": "Toujours à Jour",': '"card.always-updated": "Toujours à Jour",\n        "card.always-updated-desc": "Critiques et comparaisons fraîches pour vous garder en avance dans la révolution IA",',
            '"card.expert-insights": "Analyses d\'Experts",': '"card.expert-insights": "Analyses d\'Experts",\n        "card.expert-insights-desc": "Analyses approfondies des débutants aux solutions d\'entreprise",',
        },
        'es': {
            '"stats.tools": "Herramientas IA",': '"stats.tools": "Herramientas IA",\n        "stats.reviews": "Reseñas de Expertos",\n        "hero.featuring-tools-from": "Con herramientas de",',
            '"card.curated-selection": "Selección Curada",': '"card.curated-selection": "Selección Curada",\n        "card.curated-selection-desc": "Herramientas IA seleccionadas a mano en 22 categorías, probadas y revisadas por expertos",',
            '"card.always-updated": "Siempre Actualizado",': '"card.always-updated": "Siempre Actualizado",\n        "card.always-updated-desc": "Reseñas y comparaciones frescas para mantenerte a la vanguardia de la revolución IA",',
            '"card.expert-insights": "Análisis de Expertos",': '"card.expert-insights": "Análisis de Expertos",\n        "card.expert-insights-desc": "Análisis en profundidad desde principiantes hasta soluciones empresariales",',
        },
        'de': {
            '"stats.tools": "KI-Tools",': '"stats.tools": "KI-Tools",\n        "stats.reviews": "Experten-Bewertungen",\n        "hero.featuring-tools-from": "Mit Tools von",',
            '"card.curated-selection": "Kuratierte Auswahl",': '"card.curated-selection": "Kuratierte Auswahl",\n        "card.curated-selection-desc": "Handverlesene KI-Tools in 22 Kategorien, getestet und bewertet von Experten",',
            '"card.always-updated": "Immer Aktuell",': '"card.always-updated": "Immer Aktuell",\n        "card.always-updated-desc": "Frische Bewertungen und Vergleiche, um Sie in der KI-Revolution voraus zu halten",',
            '"card.expert-insights": "Experten-Einblicke",': '"card.expert-insights": "Experten-Einblicke",\n        "card.expert-insights-desc": "Tiefgehende Analysen von Anfängern bis zu Unternehmenslösungen",',
        },
        'pt': {
            '"stats.tools": "Ferramentas IA",': '"stats.tools": "Ferramentas IA",\n        "stats.reviews": "Avaliações de Especialistas",\n        "hero.featuring-tools-from": "Com ferramentas de",',
            '"card.curated-selection": "Seleção Curada",': '"card.curated-selection": "Seleção Curada",\n        "card.curated-selection-desc": "Ferramentas IA selecionadas a dedo em 22 categorias, testadas e avaliadas por especialistas",',
            '"card.always-updated": "Sempre Atualizado",': '"card.always-updated": "Sempre Atualizado",\n        "card.always-updated-desc": "Avaliações e comparações frescas para mantê-lo à frente na revolução IA",',
            '"card.expert-insights": "Insights de Especialistas",': '"card.expert-insights": "Insights de Especialistas",\n        "card.expert-insights-desc": "Análise aprofundada desde iniciantes até soluções empresariais",',
        },
        'zh': {
            '"stats.tools": "AI工具",': '"stats.tools": "AI工具",\n        "stats.reviews": "专家评论",\n        "hero.featuring-tools-from": "精选工具来自",',
            '"card.curated-selection": "精选收藏",': '"card.curated-selection": "精选收藏",\n        "card.curated-selection-desc": "22个类别的精选AI工具，由专家测试和审查",',
            '"card.always-updated": "持续更新",': '"card.always-updated": "持续更新",\n        "card.always-updated-desc": "新鲜的评论和比较，让您在AI革命中保持领先",',
            '"card.expert-insights": "专家洞察",': '"card.expert-insights": "专家洞察",\n        "card.expert-insights-desc": "从初学者到企业解决方案的深入分析",',
        },
        'ja': {
            '"stats.tools": "AIツール",': '"stats.tools": "AIツール",\n        "stats.reviews": "専門家レビュー",\n        "hero.featuring-tools-from": "ツール提供元",',
            '"card.curated-selection": "厳選されたセレクション",': '"card.curated-selection": "厳選されたセレクション",\n        "card.curated-selection-desc": "22カテゴリーの厳選されたAIツール、専門家によってテストおよびレビュー済み",',
            '"card.always-updated": "常に最新",': '"card.always-updated": "常に最新",\n        "card.always-updated-desc": "AI革命で先を行くための新鮮なレビューと比較",',
            '"card.expert-insights": "専門家の洞察",': '"card.expert-insights": "専門家の洞察",\n        "card.expert-insights-desc": "初心者からエンタープライズソリューションまでの詳細な分析",',
        },
        'ko': {
            '"stats.tools": "AI 도구",': '"stats.tools": "AI 도구",\n        "stats.reviews": "전문가 리뷰",\n        "hero.featuring-tools-from": "도구 제공",',
            '"card.curated-selection": "선별된 선택",': '"card.curated-selection": "선별된 선택",\n        "card.curated-selection-desc": "22개 카테고리의 엄선된 AI 도구, 전문가가 테스트하고 검토함",',
            '"card.always-updated": "항상 최신",': '"card.always-updated": "항상 최신",\n        "card.always-updated-desc": "AI 혁명에서 앞서 나가기 위한 신선한 리뷰와 비교",',
            '"card.expert-insights": "전문가 통찰",': '"card.expert-insights": "전문가 통찰",\n        "card.expert-insights-desc": "초보자부터 기업 솔루션까지 심층 분석",',
        },
        'ar': {
            '"stats.tools": "أدوات الذكاء الاصطناعي",': '"stats.tools": "أدوات الذكاء الاصطناعي",\n        "stats.reviews": "مراجعات الخبراء",\n        "hero.featuring-tools-from": "يضم أدوات من",',
            '"card.curated-selection": "تشكيلة منسقة",': '"card.curated-selection": "تشكيلة منسقة",\n        "card.curated-selection-desc": "أدوات ذكاء اصطناعي منتقاة عبر 22 فئة، تم اختبارها ومراجعتها من قبل الخبراء",',
            '"card.always-updated": "محدّث دائمًا",': '"card.always-updated": "محدّث دائمًا",\n        "card.always-updated-desc": "مراجعات ومقارنات جديدة لتبقيك في صدارة ثورة الذكاء الاصطناعي",',
            '"card.expert-insights": "رؤى الخبراء",': '"card.expert-insights": "رؤى الخبراء",\n        "card.expert-insights-desc": "تحليل متعمق من المبتدئين إلى حلول المؤسسات",',
        },
        'hi': {
            '"stats.tools": "AI टूल्स",': '"stats.tools": "AI टूल्स",\n        "stats.reviews": "विशेषज्ञ समीक्षाएं",\n        "hero.featuring-tools-from": "उपकरण प्रदर्शित करता है",',
            '"card.curated-selection": "क्यूरेटेड चयन",': '"card.curated-selection": "क्यूरेटेड चयन",\n        "card.curated-selection-desc": "22 श्रेणियों में हाथ से चुने गए AI टूल्स, विशेषज्ञों द्वारा परीक्षित और समीक्षित",',
            '"card.always-updated": "हमेशा अपडेटेड",': '"card.always-updated": "हमेशा अपडेटेड",\n        "card.always-updated-desc": "ताजा समीक्षाएं और तुलनाएं जो आपको AI क्रांति में आगे रखती हैं",',
            '"card.expert-insights": "विशेषज्ञ अंतर्दृष्टि",': '"card.expert-insights": "विशेषज्ञ अंतर्दृष्टि",\n        "card.expert-insights-desc": "शुरुआती से लेकर उद्यम समाधान तक गहन विश्लेषण",',
        },
    }

    # Appliquer les remplacements pour chaque langue
    for lang, replacements in new_keys.items():
        for old, new in replacements.items():
            if old in content:
                content = content.replace(old, new, 1)
                print(f"✅ {lang}: Clés ajoutées")

    # Écrire les modifications
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print("\n✅ Toutes les clés i18n ont été ajoutées!")
    else:
        print("\nℹ️  Aucune modification nécessaire")

if __name__ == "__main__":
    add_missing_i18n_keys()
