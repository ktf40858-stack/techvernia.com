// Jasper AI vs Copy.ai Article - Multilingual Translations
// 10 Languages: EN, ES, FR, DE, PT, ZH, JA, KO, AR, HI

console.log('📦 jasper-vs-copyai-i18n.js loaded');

const articleTranslations = {
    en: {
        pageTitle: "Jasper AI vs Copy.ai: Which AI Writing Tool is Best for Marketing? | GenuisNet.ai",
        metaDescription: "Side-by-side comparison of features, pricing, and content quality.",
        heroTitle: "Jasper AI vs Copy.ai: Which AI Writing Tool is Best for Marketing?",
        heroExcerpt: "Head-to-head comparison for content creators and marketing teams.",
        footerDesc: "Your trusted source for AI tool reviews, comparisons, and guides.",
        footerCategories: "Categories",
        footerResources: "Resources",
        footerCopyright: "© 2026 GenuisNet.ai. All rights reserved."
    },
    es: {
        pageTitle: "Jasper AI vs Copy.ai: ¿Qué Herramienta de Escritura IA es Mejor para Marketing? | GenuisNet.ai",
        metaDescription: "Comparación lado a lado de características, precios y calidad de contenido.",
        heroTitle: "Jasper AI vs Copy.ai: ¿Qué Herramienta de Escritura IA es Mejor para Marketing?",
        heroExcerpt: "Comparación directa para creadores de contenido y equipos de marketing.",
        footerDesc: "Tu fuente confiable de reseñas, comparaciones y guías de herramientas IA.",
        footerCategories: "Categorías",
        footerResources: "Recursos",
        footerCopyright: "© 2026 GenuisNet.ai. Todos los derechos reservados."
    },
    fr: {
        pageTitle: "Jasper AI vs Copy.ai : Quel Outil d'Écriture IA est le Meilleur pour le Marketing ? | GenuisNet.ai",
        metaDescription: "Comparaison côte à côte des fonctionnalités, tarifs et qualité du contenu.",
        heroTitle: "Jasper AI vs Copy.ai : Quel Outil d'Écriture IA est le Meilleur pour le Marketing ?",
        heroExcerpt: "Comparaison directe pour les créateurs de contenu et les équipes marketing.",
        footerDesc: "Votre source de confiance pour les avis, comparaisons et guides d'outils IA.",
        footerCategories: "Catégories",
        footerResources: "Ressources",
        footerCopyright: "© 2026 GenuisNet.ai. Tous droits réservés."
    },
    de: {
        pageTitle: "Jasper AI vs Copy.ai: Welches KI-Schreibwerkzeug ist Besser für Marketing? | GenuisNet.ai",
        metaDescription: "Side-by-Side-Vergleich von Features, Preisen und Inhaltsqualität.",
        heroTitle: "Jasper AI vs Copy.ai: Welches KI-Schreibwerkzeug ist Besser für Marketing?",
        heroExcerpt: "Direkter Vergleich für Content-Ersteller und Marketing-Teams.",
        footerDesc: "Ihre vertrauenswürdige Quelle für KI-Tool-Bewertungen, Vergleiche und Leitfäden.",
        footerCategories: "Kategorien",
        footerResources: "Ressourcen",
        footerCopyright: "© 2026 GenuisNet.ai. Alle Rechte vorbehalten."
    },
    pt: {
        pageTitle: "Jasper AI vs Copy.ai: Qual Ferramenta de Escrita IA é Melhor para Marketing? | GenuisNet.ai",
        metaDescription: "Comparação lado a lado de recursos, preços e qualidade do conteúdo.",
        heroTitle: "Jasper AI vs Copy.ai: Qual Ferramenta de Escrita IA é Melhor para Marketing?",
        heroExcerpt: "Comparação direta para criadores de conteúdo e equipes de marketing.",
        footerDesc: "Sua fonte confiável para avaliações, comparações e guias de ferramentas IA.",
        footerCategories: "Categorias",
        footerResources: "Recursos",
        footerCopyright: "© 2026 GenuisNet.ai. Todos os direitos reservados."
    },
    zh: { pageTitle: "Jasper AI vs Copy.ai：哪个AI写作工具更适合营销？ | GenuisNet.ai", heroTitle: "Jasper AI vs Copy.ai：哪个AI写作工具更适合营销？", heroExcerpt: "为内容创作者和营销团队提供的直接比较。", footerDesc: "您值得信赖的 AI 工具评论、比较和指南来源。", footerCategories: "类别", footerResources: "资源", footerCopyright: "© 2026 GenuisNet.ai. 保留所有权利。" },
    ja: { pageTitle: "Jasper AI vs Copy.ai：マーケティングに最適なAIライティングツールは？ | GenuisNet.ai", heroTitle: "Jasper AI vs Copy.ai：マーケティングに最適なAIライティングツールは？", heroExcerpt: "コンテンツクリエイターとマーケティングチーム向けの直接比較。", footerDesc: "AIツールのレビュー、比較、ガイドの信頼できる情報源。", footerCategories: "カテゴリー", footerResources: "リソース", footerCopyright: "© 2026 GenuisNet.ai. 全著作権所有。" },
    ko: { pageTitle: "Jasper AI vs Copy.ai: 마케팅에 가장 적합한 AI 작성 도구는? | GenuisNet.ai", heroTitle: "Jasper AI vs Copy.ai: 마케팅에 가장 적합한 AI 작성 도구는?", heroExcerpt: "콘텐츠 제작자 및 마케팅 팀을 위한 직접 비교.", footerDesc: "AI 도구 리뷰, 비교 및 가이드의 신뢰할 수 있는 출처.", footerCategories: "카테고리", footerResources: "리소스", footerCopyright: "© 2026 GenuisNet.ai. 모든 권리 보유." },
    ar: { pageTitle: "Jasper AI مقابل Copy.ai: أي أداة كتابة بالذكاء الاصطناعي هي الأفضل للتسويق؟ | GenuisNet.ai", heroTitle: "Jasper AI مقابل Copy.ai: أي أداة كتابة بالذكاء الاصطناعي هي الأفضل للتسويق؟", heroExcerpt: "مقارنة مباشرة لمنشئي المحتوى وفرق التسويق.", footerDesc: "مصدرك الموثوق لمراجعات ومقارنات وأدلة أدوات الذكاء الاصطناعي.", footerCategories: "الفئات", footerResources: "الموارد", footerCopyright: "© 2026 GenuisNet.ai. جميع الحقوق محفوظة." },
    hi: { pageTitle: "Jasper AI बनाम Copy.ai: मार्केटिंग के लिए कौन सा AI लेखन उपकरण सर्वोत्तम है? | GenuisNet.ai", heroTitle: "Jasper AI बनाम Copy.ai: मार्केटिंग के लिए कौन सा AI लेखन उपकरण सर्वोत्तम है?", heroExcerpt: "सामग्री निर्माताओं और मार्केटिंग टीमों के लिए सीधी तुलना।", footerDesc: "AI टूल समीक्षाओं, तुलनाओं और गाइड के लिए आपका विश्वसनीय स्रोत।", footerCategories: "श्रेणियाँ", footerResources: "संसाधन", footerCopyright: "© 2026 GenuisNet.ai. सर्वाधिकार सुरक्षित।" }
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
