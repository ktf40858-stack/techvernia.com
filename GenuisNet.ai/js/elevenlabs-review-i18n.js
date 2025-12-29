// ElevenLabs Review Article - Multilingual Translations
// 10 Languages: EN, ES, FR, DE, PT, ZH, JA, KO, AR, HI

console.log('📦 elevenlabs-review-i18n.js loaded');

const articleTranslations = {
    en: {
        pageTitle: "ElevenLabs Review: Is It Worth the Hype? Honest Analysis & Pricing | GenuisNet.ai",
        metaDescription: "In-depth review of the most realistic AI voice generator on the market.",
        heroTitle: "ElevenLabs Review: Is It Worth the Hype? Honest Analysis & Pricing",
        heroExcerpt: "In-depth review of the most realistic AI voice generator on the market.",
        footerDesc: "Your trusted source for AI tool reviews, comparisons, and guides.",
        footerCategories: "Categories",
        footerResources: "Resources",
        footerCopyright: "© 2026 GenuisNet.ai. All rights reserved."
    },
    es: {
        pageTitle: "Reseña de ElevenLabs: ¿Vale la Pena el Hype? Análisis Honesto y Precios | GenuisNet.ai",
        metaDescription: "Revisión en profundidad del generador de voz IA más realista del mercado.",
        heroTitle: "Reseña de ElevenLabs: ¿Vale la Pena el Hype? Análisis Honesto y Precios",
        heroExcerpt: "Revisión en profundidad del generador de voz IA más realista del mercado.",
        footerDesc: "Tu fuente confiable de reseñas, comparaciones y guías de herramientas IA.",
        footerCategories: "Categorías",
        footerResources: "Recursos",
        footerCopyright: "© 2026 GenuisNet.ai. Todos los derechos reservados."
    },
    fr: {
        pageTitle: "Revue ElevenLabs : Est-ce que ça Vaut le Battage ? Analyse Honnête et Tarifs | GenuisNet.ai",
        metaDescription: "Revue approfondie du générateur de voix IA le plus réaliste du marché.",
        heroTitle: "Revue ElevenLabs : Est-ce que ça Vaut le Battage ? Analyse Honnête et Tarifs",
        heroExcerpt: "Revue approfondie du générateur de voix IA le plus réaliste du marché.",
        footerDesc: "Votre source de confiance pour les avis, comparaisons et guides d'outils IA.",
        footerCategories: "Catégories",
        footerResources: "Ressources",
        footerCopyright: "© 2026 GenuisNet.ai. Tous droits réservés."
    },
    de: {
        pageTitle: "ElevenLabs Review: Ist der Hype Gerechtfertigt? Ehrliche Analyse & Preise | GenuisNet.ai",
        metaDescription: "Ausführliche Bewertung des realistischsten KI-Sprachgenerators auf dem Markt.",
        heroTitle: "ElevenLabs Review: Ist der Hype Gerechtfertigt? Ehrliche Analyse & Preise",
        heroExcerpt: "Ausführliche Bewertung des realistischsten KI-Sprachgenerators auf dem Markt.",
        footerDesc: "Ihre vertrauenswürdige Quelle für KI-Tool-Bewertungen, Vergleiche und Leitfäden.",
        footerCategories: "Kategorien",
        footerResources: "Ressourcen",
        footerCopyright: "© 2026 GenuisNet.ai. Alle Rechte vorbehalten."
    },
    pt: {
        pageTitle: "Análise ElevenLabs: Vale o Hype? Análise Honesta e Preços | GenuisNet.ai",
        metaDescription: "Revisão aprofundada do gerador de voz IA mais realista do mercado.",
        heroTitle: "Análise ElevenLabs: Vale o Hype? Análise Honesta e Preços",
        heroExcerpt: "Revisão aprofundada do gerador de voz IA mais realista do mercado.",
        footerDesc: "Sua fonte confiável para avaliações, comparações e guias de ferramentas IA.",
        footerCategories: "Categorias",
        footerResources: "Recursos",
        footerCopyright: "© 2026 GenuisNet.ai. Todos os direitos reservados."
    },
    zh: { pageTitle: "ElevenLabs评测：是否名副其实？诚实分析与价格 | GenuisNet.ai", heroTitle: "ElevenLabs评测：是否名副其实？诚实分析与价格", heroExcerpt: "市场上最逼真的AI语音生成器深度评测。", footerDesc: "您值得信赖的 AI 工具评论、比较和指南来源。", footerCategories: "类别", footerResources: "资源", footerCopyright: "© 2026 GenuisNet.ai. 保留所有权利。" },
    ja: { pageTitle: "ElevenLabsレビュー：誇大広告に値する？正直な分析と価格 | GenuisNet.ai", heroTitle: "ElevenLabsレビュー：誇大広告に値する？正直な分析と価格", heroExcerpt: "市場で最もリアルなAI音声生成器の詳細レビュー。", footerDesc: "AIツールのレビュー、比較、ガイドの信頼できる情報源。", footerCategories: "カテゴリー", footerResources: "リソース", footerCopyright: "© 2026 GenuisNet.ai. 全著作権所有。" },
    ko: { pageTitle: "ElevenLabs 리뷰: 과대 광고에 값어치가 있을까? 정직한 분석 및 가격 | GenuisNet.ai", heroTitle: "ElevenLabs 리뷰: 과대 광고에 값어치가 있을까? 정직한 분석 및 가격", heroExcerpt: "시장에서 가장 사실적인 AI 음성 생성기의 심층 리뷰.", footerDesc: "AI 도구 리뷰, 비교 및 가이드의 신뢰할 수 있는 출처.", footerCategories: "카테고리", footerResources: "리소스", footerCopyright: "© 2026 GenuisNet.ai. 모든 권리 보유." },
    ar: { pageTitle: "مراجعة ElevenLabs: هل يستحق الضجة؟ تحليل صادق والأسعار | GenuisNet.ai", heroTitle: "مراجعة ElevenLabs: هل يستحق الضجة؟ تحليل صادق والأسعار", heroExcerpt: "مراجعة متعمقة لمولد الصوت بالذكاء الاصطناعي الأكثر واقعية في السوق.", footerDesc: "مصدرك الموثوق لمراجعات ومقارنات وأدلة أدوات الذكاء الاصطناعي.", footerCategories: "الفئات", footerResources: "الموارد", footerCopyright: "© 2026 GenuisNet.ai. جميع الحقوق محفوظة." },
    hi: { pageTitle: "ElevenLabs समीक्षा: क्या यह प्रचार के योग्य है? ईमानदार विश्लेषण और मूल्य निर्धारण | GenuisNet.ai", heroTitle: "ElevenLabs समीक्षा: क्या यह प्रचार के योग्य है? ईमानदार विश्लेषण और मूल्य निर्धारण", heroExcerpt: "बाजार में सबसे यथार्थवादी AI वॉयस जनरेटर की गहन समीक्षा।", footerDesc: "AI टूल समीक्षाओं, तुलनाओं और गाइड के लिए आपका विश्वसनीय स्रोत।", footerCategories: "श्रेणियाँ", footerResources: "संसाधन", footerCopyright: "© 2026 GenuisNet.ai. सर्वाधिकार सुरक्षित।" }
};

function initArticleI18n() {
    const currentLang = localStorage.getItem('selectedLanguage') || 'en';
    applyArticleTranslations(currentLang);
    document.addEventListener('languageChanged', (e) => applyArticleTranslations(e.detail.language));
}

function applyArticleTranslations(lang) {
    console.log('🔧 Applying article translations for language:', lang);
    const t = articleTranslations[lang] || articleTranslations.en;

    // If language is simplified (ZH, JA, KO, AR, HI), only translate basic elements
    const isSimplifiedLang = ['zh', 'ja', 'ko', 'ar', 'hi'].includes(lang);

    // Update page title and meta
    document.title = t.pageTitle || articleTranslations.en.pageTitle;
    const metaDesc = document.querySelector('meta[name="description"]');
    const metaKeywords = document.querySelector('meta[name="keywords"]');
    if (metaDesc && t.metaDescription) metaDesc.content = t.metaDescription;
    if (metaKeywords && t.metaKeywords) metaKeywords.content = t.metaKeywords;

    // Get all elements with data-i18n attributes
    const i18nElements = document.querySelectorAll('[data-i18n]');
    console.log(`📍 Found ${i18nElements.length} elements with data-i18n attributes`);

    let translatedCount = 0;
    let skippedCount = 0;

    i18nElements.forEach(element => {
        const key = element.getAttribute('data-i18n');

        // For simplified languages, only translate basic elements (headings, hero, footer)
        if (isSimplifiedLang) {
            const isBasicElement = key.startsWith('heading') ||
                                   key.startsWith('subheading') ||
                                   key.startsWith('hero') ||
                                   key.startsWith('footer');
            if (!isBasicElement) {
                skippedCount++;
                return;
            }
        }

        // Get translation for this key
        const translation = t[key];

        if (translation) {
            // Handle different element types
            const tagName = element.tagName.toLowerCase();

            if (tagName === 'li' && (element.querySelector('strong') || element.querySelector('span[data-i18n]'))) {
                // For list items with strong tags and spans, handle each part separately
                const strong = element.querySelector('strong');
                const span = element.querySelector('span[data-i18n]');

                if (strong && strong.hasAttribute('data-i18n')) {
                    const strongKey = strong.getAttribute('data-i18n');
                    if (t[strongKey]) {
                        strong.textContent = t[strongKey];
                    }
                }

                if (span) {
                    const spanKey = span.getAttribute('data-i18n');
                    if (t[spanKey]) {
                        span.textContent = t[spanKey];
                    }
                }
            } else if (tagName === 'p' && (element.querySelector('strong') || element.querySelector('span[data-i18n]'))) {
                // For paragraphs with strong/span elements, handle separately
                const strong = element.querySelector('strong');
                const span = element.querySelector('span[data-i18n]');

                if (strong && strong.hasAttribute('data-i18n')) {
                    const strongKey = strong.getAttribute('data-i18n');
                    if (t[strongKey]) {
                        strong.textContent = t[strongKey];
                    }
                }

                if (span) {
                    const spanKey = span.getAttribute('data-i18n');
                    if (t[spanKey]) {
                        span.textContent = t[spanKey];
                    }
                } else if (!span && !strong.hasAttribute('data-i18n')) {
                    // Paragraph with inline strong but no data-i18n on strong
                    element.innerHTML = translation;
                }
            } else {
                // For simple elements, just replace text content
                element.textContent = translation;
            }

            translatedCount++;
        } else {
            // Translation key not found, use English fallback
            const fallback = articleTranslations.en[key];
            if (fallback && lang !== 'en') {
                element.textContent = fallback;
                console.warn(`⚠️ Translation key "${key}" not found for language "${lang}", using English fallback`);
            }
        }
    });

    console.log(`✅ Article translations applied: ${translatedCount} translated, ${skippedCount} skipped (simplified language)`);
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initArticleI18n);
} else {
    initArticleI18n();
}
