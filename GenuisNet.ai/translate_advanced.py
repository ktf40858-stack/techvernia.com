#!/usr/bin/env python3
"""
Script de Traduction Avancée - Version Améliorée
Utilise des patterns de traduction plus sophistiqués
"""

import json
import sys
import os
import re

PROJECT_ROOT = "/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai"

# Dictionnaire étendu de traductions par patterns
TRANSLATION_PATTERNS = {
    # Patterns pour "Try X"
    r"^Try (.+)$": {
        "es": lambda m: f"Probar {m.group(1)}",
        "fr": lambda m: f"Essayer {m.group(1)}",
        "de": lambda m: f"{m.group(1)} testen",
        "pt": lambda m: f"Experimentar {m.group(1)}",
        "zh": lambda m: f"试用{m.group(1)}",
        "ja": lambda m: f"{m.group(1)}を試す",
        "ko": lambda m: f"{m.group(1)} 시도",
        "ar": lambda m: f"جرب {m.group(1)}",
        "hi": lambda m: f"{m.group(1)} आज़माएं"
    },

    # Patterns pour "X vs Y"
    r"^(.+) vs (.+)$": {
        "es": lambda m: f"{m.group(1)} vs {m.group(2)}",
        "fr": lambda m: f"{m.group(1)} vs {m.group(2)}",
        "de": lambda m: f"{m.group(1)} vs {m.group(2)}",
        "pt": lambda m: f"{m.group(1)} vs {m.group(2)}",
        "zh": lambda m: f"{m.group(1)} vs {m.group(2)}",
        "ja": lambda m: f"{m.group(1)} vs {m.group(2)}",
        "ko": lambda m: f"{m.group(1)} vs {m.group(2)}",
        "ar": lambda m: f"{m.group(1)} مقابل {m.group(2)}",
        "hi": lambda m: f"{m.group(1)} बनाम {m.group(2)}"
    },

    # Patterns pour "Best X"
    r"^Best (.+)$": {
        "es": lambda m: f"Mejores {m.group(1)}",
        "fr": lambda m: f"Meilleurs {m.group(1)}",
        "de": lambda m: f"Beste {m.group(1)}",
        "pt": lambda m: f"Melhores {m.group(1)}",
        "zh": lambda m: f"最佳{m.group(1)}",
        "ja": lambda m: f"ベスト{m.group(1)}",
        "ko": lambda m: f"최고의 {m.group(1)}",
        "ar": lambda m: f"أفضل {m.group(1)}",
        "hi": lambda m: f"सर्वश्रेष्ठ {m.group(1)}"
    },

    # Patterns pour "AI X"
    r"^AI (.+)$": {
        "es": lambda m: f"IA {m.group(1)}",
        "fr": lambda m: f"IA {m.group(1)}",
        "de": lambda m: f"KI {m.group(1)}",
        "pt": lambda m: f"IA {m.group(1)}",
        "zh": lambda m: f"AI{m.group(1)}",
        "ja": lambda m: f"AI{m.group(1)}",
        "ko": lambda m: f"AI {m.group(1)}",
        "ar": lambda m: f"الذكاء الاصطناعي {m.group(1)}",
        "hi": lambda m: f"AI {m.group(1)}"
    },
}

# Dictionnaire de traductions complètes pour phrases communes
PHRASE_TRANSLATIONS = {
    "Ready to Discover Your Perfect AI Tool?": {
        "es": "¿Listo para Descubrir tu Herramienta IA Perfecta?",
        "fr": "Prêt à Découvrir Votre Outil IA Parfait?",
        "de": "Bereit, Ihr Perfektes KI-Tool zu Entdecken?",
        "pt": "Pronto para Descobrir sua Ferramenta IA Perfeita?",
        "zh": "准备好发现完美的AI工具了吗？",
        "ja": "完璧なAIツールを見つける準備はできましたか？",
        "ko": "완벽한 AI 도구를 찾을 준비가 되셨나요?",
        "ar": "هل أنت مستعد لاكتشاف أداة الذكاء الاصطناعي المثالية؟",
        "hi": "क्या आप अपने परफेक्ट AI टूल की खोज के लिए तैयार हैं?"
    },

    "Discover the Future of AI Tools": {
        "es": "Descubre el Futuro de las Herramientas IA",
        "fr": "Découvrez l'Avenir des Outils IA",
        "de": "Entdecken Sie die Zukunft der KI-Tools",
        "pt": "Descubra o Futuro das Ferramentas IA",
        "zh": "发现AI工具的未来",
        "ja": "AIツールの未来を発見",
        "ko": "AI 도구의 미래를 발견하세요",
        "ar": "اكتشف مستقبل أدوات الذكاء الاصطناعي",
        "hi": "AI टूल्स का भविष्य खोजें"
    },

    "Curated Selection": {
        "es": "Selección Curada",
        "fr": "Sélection Organisée",
        "de": "Kuratierte Auswahl",
        "pt": "Seleção Curada",
        "zh": "精心挑选",
        "ja": "厳選されたセレクション",
        "ko": "선별된 선택",
        "ar": "اختيار منسق",
        "hi": "चयनित संग्रह"
    },

    "Expert Insights": {
        "es": "Perspectivas de Expertos",
        "fr": "Analyses d'Experts",
        "de": "Expertenmeinungen",
        "pt": "Insights de Especialistas",
        "zh": "专家见解",
        "ja": "専門家の洞察",
        "ko": "전문가 통찰",
        "ar": "رؤى الخبراء",
        "hi": "विशेषज्ञ अंतर्दृष्टि"
    },

    "Always Updated": {
        "es": "Siempre Actualizado",
        "fr": "Toujours à Jour",
        "de": "Immer Aktuell",
        "pt": "Sempre Atualizado",
        "zh": "持续更新",
        "ja": "常に最新",
        "ko": "항상 업데이트됨",
        "ar": "محدث دائمًا",
        "hi": "हमेशा अपडेट"
    },

    "Read Full Review": {
        "es": "Leer Reseña Completa",
        "fr": "Lire la Revue Complète",
        "de": "Vollständige Bewertung Lesen",
        "pt": "Ler Avaliação Completa",
        "zh": "阅读完整评论",
        "ja": "レビュー全文を読む",
        "ko": "전체 리뷰 읽기",
        "ar": "اقرأ المراجعة الكاملة",
        "hi": "पूर्ण समीक्षा पढ़ें"
    },

    "Browse Categories": {
        "es": "Explorar Categorías",
        "fr": "Parcourir les Catégories",
        "de": "Kategorien Durchsuchen",
        "pt": "Navegar pelas Categorias",
        "zh": "浏览类别",
        "ja": "カテゴリーを閲覧",
        "ko": "카테고리 탐색",
        "ar": "تصفح الفئات",
        "hi": "श्रेणियाँ ब्राउज़ करें"
    },

    "Select Language": {
        "es": "Seleccionar Idioma",
        "fr": "Sélectionner la Langue",
        "de": "Sprache Wählen",
        "pt": "Selecionar Idioma",
        "zh": "选择语言",
        "ja": "言語を選択",
        "ko": "언어 선택",
        "ar": "اختر اللغة",
        "hi": "भाषा चुनें"
    },

    "Toggle Menu": {
        "es": "Alternar Menú",
        "fr": "Basculer le Menu",
        "de": "Menü Umschalten",
        "pt": "Alternar Menu",
        "zh": "切换菜单",
        "ja": "メニューを切り替え",
        "ko": "메뉴 전환",
        "ar": "تبديل القائمة",
        "hi": "मेन्यू टॉगल करें"
    },

    # Nouvelles traductions complètes ajoutées
    "Handpicked AI tools across 22 categories, tested and reviewed by experts": {
        "es": "Herramientas IA seleccionadas en 22 categorías, probadas y revisadas por expertos",
        "fr": "Outils IA sélectionnés dans 22 catégories, testés et évalués par des experts",
        "de": "Handverlesene KI-Tools in 22 Kategorien, getestet und bewertet von Experten",
        "pt": "Ferramentas IA selecionadas em 22 categorias, testadas e avaliadas por especialistas",
        "zh": "22个类别中的精选AI工具，由专家测试和评审",
        "ja": "22カテゴリーにわたる厳選AIツール、専門家によるテストとレビュー",
        "ko": "전문가가 테스트하고 검토한 22개 카테고리의 엄선된 AI 도구",
        "ar": "أدوات الذكاء الاصطناعي المختارة في 22 فئة، تم اختبارها ومراجعتها من قبل الخبراء",
        "hi": "22 श्रेणियों में चयनित AI टूल्स, विशेषज्ञों द्वारा परीक्षण और समीक्षा की गई"
    },

    "Fresh reviews and comparisons to keep you ahead in the AI revolution": {
        "es": "Reseñas y comparaciones actualizadas para mantenerte a la vanguardia de la revolución IA",
        "fr": "Critiques et comparaisons récentes pour vous garder en avance dans la révolution IA",
        "de": "Frische Bewertungen und Vergleiche, um Sie in der KI-Revolution vorne zu halten",
        "pt": "Avaliações e comparações atualizadas para mantê-lo à frente na revolução IA",
        "zh": "最新的评论和比较，让您在AI革命中保持领先",
        "ja": "AI革命で先を行くための最新レビューと比較",
        "ko": "AI 혁명에서 앞서 나가기 위한 최신 리뷰 및 비교",
        "ar": "مراجعات ومقارنات حديثة لإبقائك في الطليعة في ثورة الذكاء الاصطناعي",
        "hi": "AI क्रांति में आगे रहने के लिए ताज़ा समीक्षाएं और तुलनाएं"
    },

    "In-depth analysis from beginners to enterprise solutions": {
        "es": "Análisis en profundidad desde principiantes hasta soluciones empresariales",
        "fr": "Analyse approfondie pour débutants et solutions d'entreprise",
        "de": "Eingehende Analyse von Anfängern bis zu Unternehmenslösungen",
        "pt": "Análise aprofundada desde iniciantes até soluções empresariais",
        "zh": "从初学者到企业解决方案的深入分析",
        "ja": "初心者からエンタープライズソリューションまでの詳細分析",
        "ko": "초보자부터 엔터프라이즈 솔루션까지 심층 분석",
        "ar": "تحليل متعمق من المبتدئين إلى حلول المؤسسات",
        "hi": "शुरुआती से लेकर एंटरप्राइज़ सॉल्यूशंस तक गहन विश्लेषण"
    },

    "Explore 116+ carefully curated tools across 22 categories": {
        "es": "Explora más de 116 herramientas cuidadosamente seleccionadas en 22 categorías",
        "fr": "Explorez plus de 116 outils soigneusement sélectionnés dans 22 catégories",
        "de": "Entdecken Sie über 116 sorgfältig kuratierte Tools in 22 Kategorien",
        "pt": "Explore mais de 116 ferramentas cuidadosamente selecionadas em 22 categorias",
        "zh": "探索22个类别中精心策划的116+工具",
        "ja": "22カテゴリーにわたる厳選された116以上のツールを探索",
        "ko": "22개 카테고리에 걸쳐 신중하게 선별된 116개 이상의 도구 탐색",
        "ar": "استكشف أكثر من 116 أداة منسقة بعناية في 22 فئة",
        "hi": "22 श्रेणियों में सावधानीपूर्वक चयनित 116+ टूल्स एक्सप्लोर करें"
    },
}

def translate_with_patterns(text, lang):
    """Essayer de traduire en utilisant les patterns"""
    for pattern, translations in TRANSLATION_PATTERNS.items():
        match = re.match(pattern, text)
        if match and lang in translations:
            return translations[lang](match)
    return None

def translate_text_advanced(text, lang):
    """Traduction avancée avec patterns et dictionnaire étendu"""

    # 1. Vérifier les traductions complètes
    if text in PHRASE_TRANSLATIONS:
        return PHRASE_TRANSLATIONS[text].get(lang)

    # 2. Essayer les patterns
    pattern_translation = translate_with_patterns(text, lang)
    if pattern_translation:
        return pattern_translation

    # 3. Sinon, retourner None (à traduire manuellement)
    return None

def process_translations(input_file):
    """Traiter toutes les traductions"""

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ Erreur lecture: {e}")
        return None

    keys = data.get('keys', {})
    total_keys = len(keys)

    print(f"\n{'='*80}")
    print(f"🚀 TRADUCTION AVANCÉE")
    print(f"{'='*80}\n")
    print(f"Fichier: {input_file}")
    print(f"Clés à traduire: {total_keys}\n")

    translated_count = 0
    manual_count = 0

    for key, translations in keys.items():
        en_text = translations['en']

        # Ignorer si déjà marqué comme traduit
        if not en_text.startswith('[TO TRANSLATE]'):
            original_text = en_text
        else:
            original_text = en_text.replace('[TO TRANSLATE] ', '')

        for lang in ['es', 'fr', 'de', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']:
            current = translations[lang]

            # Si déjà traduit (pas de [TO TRANSLATE]), garder la traduction
            if current and not current.startswith('[TO TRANSLATE]'):
                translated_count += 1
                continue

            # Essayer de traduire
            translated = translate_text_advanced(original_text, lang)

            if translated:
                translations[lang] = translated
                translated_count += 1
            else:
                translations[lang] = f"[TO TRANSLATE] {original_text}"
                manual_count += 1

    total_translations = total_keys * 9
    auto_percentage = (translated_count / total_translations * 100) if total_translations > 0 else 0

    print(f"📊 Résultats:")
    print(f"   - Traductions automatiques: {translated_count}/{total_translations} ({auto_percentage:.1f}%)")
    print(f"   - À traduire manuellement: {manual_count}/{total_translations} ({100-auto_percentage:.1f}%)")
    print()

    # Sauvegarder
    output_file = input_file.replace('.json', '_auto.json').replace('_translated', '')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"✅ Fichier sauvegardé: {output_file}\n")

    return data

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 translate_advanced.py <fichier_keys.json>")
        sys.exit(1)

    input_file = sys.argv[1]
    if not os.path.isabs(input_file):
        input_file = os.path.join(PROJECT_ROOT, input_file)

    if not os.path.exists(input_file):
        print(f"❌ Fichier non trouvé: {input_file}")
        sys.exit(1)

    data = process_translations(input_file)

    if data:
        print(f"{'='*80}")
        print(f"✅ TRADUCTION TERMINÉE")
        print(f"{'='*80}\n")

if __name__ == "__main__":
    main()
