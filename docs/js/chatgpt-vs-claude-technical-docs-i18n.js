// i18n translations for ChatGPT vs Claude Technical Documentation 2026
const translations = {
    en: {
        title: "ChatGPT vs Claude for Technical Documentation 2026 | TechVernia",
        metaDescription: "ChatGPT vs Claude for technical documentation: comprehensive comparison with real tests, pricing analysis, and use case recommendations. Discover which AI tool is best for your technical writing needs in 2026.",
        h1: "ChatGPT vs Claude for Technical Documentation: Which is Better?",
        subtitle: "In-depth comparison with real-world tests, pricing analysis, and recommendations for IT professionals"
    },
    fr: {
        title: "ChatGPT vs Claude pour Documentation Technique 2026 | TechVernia",
        metaDescription: "ChatGPT vs Claude pour la documentation technique : comparaison complète avec tests réels, analyse tarifaire et recommandations. Découvrez quel outil IA est le meilleur pour vos besoins en rédaction technique.",
        h1: "ChatGPT vs Claude pour la Documentation Technique : Lequel Choisir ?",
        subtitle: "Comparaison approfondie avec tests réels, analyse tarifaire et recommandations pour professionnels IT"
    },
    es: {
        title: "ChatGPT vs Claude para Documentación Técnica 2026 | TechVernia",
        metaDescription: "ChatGPT vs Claude para documentación técnica: comparación completa con pruebas reales, análisis de precios y recomendaciones. Descubre qué herramienta de IA es mejor para tus necesidades de redacción técnica.",
        h1: "ChatGPT vs Claude para Documentación Técnica: ¿Cuál es Mejor?",
        subtitle: "Comparación en profundidad con pruebas reales, análisis de precios y recomendaciones para profesionales de TI"
    },
    de: {
        title: "ChatGPT vs Claude für Technische Dokumentation 2026 | TechVernia",
        metaDescription: "ChatGPT vs Claude für technische Dokumentation: umfassender Vergleich mit echten Tests, Preisanalyse und Empfehlungen. Entdecken Sie, welches KI-Tool für Ihre technischen Schreibanforderungen am besten geeignet ist.",
        h1: "ChatGPT vs Claude für Technische Dokumentation: Welches ist Besser?",
        subtitle: "Ausführlicher Vergleich mit realen Tests, Preisanalyse und Empfehlungen für IT-Profis"
    },
    pt: {
        title: "ChatGPT vs Claude para Documentação Técnica 2026 | TechVernia",
        metaDescription: "ChatGPT vs Claude para documentação técnica: comparação abrangente com testes reais, análise de preços e recomendações. Descubra qual ferramenta de IA é melhor para suas necessidades de redação técnica.",
        h1: "ChatGPT vs Claude para Documentação Técnica: Qual é Melhor?",
        subtitle: "Comparação aprofundada com testes reais, análise de preços e recomendações para profissionais de TI"
    },
    zh: {
        title: "ChatGPT vs Claude 技术文档对比 2026 | TechVernia",
        metaDescription: "ChatGPT vs Claude 技术文档：包含真实测试、价格分析和用例推荐的全面对比。发现哪个AI工具最适合您的技术写作需求。",
        h1: "ChatGPT vs Claude 技术文档对比：哪个更好？",
        subtitle: "包含真实测试、价格分析和IT专业人士推荐的深入对比"
    },
    ja: {
        title: "ChatGPT vs Claude 技術ドキュメント比較 2026 | TechVernia",
        metaDescription: "技術ドキュメントのためのChatGPT vs Claude：実テスト、価格分析、ユースケース推奨を含む包括的な比較。2026年の技術ライティングニーズに最適なAIツールを発見してください。",
        h1: "ChatGPT vs Claude 技術ドキュメント：どちらが優れているか？",
        subtitle: "実世界テスト、価格分析、ITプロフェッショナル向け推奨を含む詳細比較"
    },
    ko: {
        title: "ChatGPT vs Claude 기술 문서 비교 2026 | TechVernia",
        metaDescription: "기술 문서를 위한 ChatGPT vs Claude: 실제 테스트, 가격 분석 및 사용 사례 권장사항이 포함된 포괄적인 비교. 2026년 기술 작성 요구사항에 가장 적합한 AI 도구를 찾아보세요.",
        h1: "ChatGPT vs Claude 기술 문서: 어느 것이 더 나은가?",
        subtitle: "실제 테스트, 가격 분석 및 IT 전문가를 위한 권장사항이 포함된 심층 비교"
    },
    ar: {
        title: "ChatGPT مقابل Claude للتوثيق التقني 2026 | TechVernia",
        metaDescription: "ChatGPT مقابل Claude للتوثيق التقني: مقارنة شاملة مع اختبارات حقيقية، تحليل الأسعار، وتوصيات حالات الاستخدام. اكتشف أي أداة ذكاء اصطناعي هي الأفضل لاحتياجات الكتابة التقنية الخاصة بك.",
        h1: "ChatGPT مقابل Claude للتوثيق التقني: أيهما أفضل؟",
        subtitle: "مقارنة متعمقة مع اختبارات واقعية، تحليل الأسعار، وتوصيات لمحترفي تكنولوجيا المعلومات"
    },
    hi: {
        title: "ChatGPT vs Claude तकनीकी दस्तावेज़ीकरण 2026 | TechVernia",
        metaDescription: "तकनीकी दस्तावेज़ीकरण के लिए ChatGPT vs Claude: वास्तविक परीक्षण, मूल्य विश्लेषण और उपयोग केस सिफारिशों के साथ व्यापक तुलना। 2026 में अपनी तकनीकी लेखन आवश्यकताओं के लिए सर्वश्रेष्ठ AI टूल खोजें।",
        h1: "ChatGPT vs Claude तकनीकी दस्तावेज़ीकरण: कौन बेहतर है?",
        subtitle: "वास्तविक परीक्षण, मूल्य विश्लेषण और IT पेशेवरों के लिए सिफारिशों के साथ गहन तुलना"
    }
};

// Apply translations based on current language
function applyTranslations() {
    const currentLang = document.documentElement.lang || 'en';
    const trans = translations[currentLang] || translations.en;

    // Update document title
    document.title = trans.title;

    // Update meta description
    const metaDesc = document.querySelector('meta[name="description"]');
    if (metaDesc) metaDesc.content = trans.metaDescription;

    // Update h1
    const h1 = document.querySelector('.review-hero-info h1');
    if (h1) h1.textContent = trans.h1;

    // Update subtitle
    const subtitle = document.querySelector('.review-hero-info .subtitle');
    if (subtitle) subtitle.textContent = trans.subtitle;
}

// Run on page load
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', applyTranslations);
} else {
    applyTranslations();
}
