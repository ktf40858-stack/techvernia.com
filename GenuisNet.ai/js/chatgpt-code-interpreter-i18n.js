// ChatGPT Code Interpreter Article - Multilingual Translations
// 10 Languages: EN, ES, FR, DE, PT, ZH, JA, KO, AR, HI

console.log('📦 chatgpt-code-interpreter-i18n.js loaded');

const articleTranslations = {
    en: {
        pageTitle: "ChatGPT Code Interpreter: The Ultimate Guide for Non-Programmers | GenuisNet.ai",
        metaDescription: "Turn natural language into working code, charts, and data analysis.",
        heroTitle: "ChatGPT Code Interpreter: The Ultimate Guide for Non-Programmers",
        heroExcerpt: "Step-by-step guide to analyzing spreadsheets and creating visualizations.",
        footerDesc: "Your trusted source for AI tool reviews, comparisons, and guides.",
        footerCategories: "Categories",
        footerResources: "Resources",
        footerCopyright: "© 2026 GenuisNet.ai. All rights reserved."
    },
    es: {
        pageTitle: "Intérprete de Código ChatGPT: La Guía Definitiva para No Programadores | GenuisNet.ai",
        metaDescription: "Convierte lenguaje natural en código funcional, gráficos y análisis de datos.",
        heroTitle: "Intérprete de Código ChatGPT: La Guía Definitiva para No Programadores",
        heroExcerpt: "Guía paso a paso para analizar hojas de cálculo y crear visualizaciones.",
        footerDesc: "Tu fuente confiable de reseñas, comparaciones y guías de herramientas IA.",
        footerCategories: "Categorías",
        footerResources: "Recursos",
        footerCopyright: "© 2026 GenuisNet.ai. Todos los derechos reservados."
    },
    fr: {
        pageTitle: "Interpréteur de Code ChatGPT : Le Guide Ultime pour Non-Programmeurs | GenuisNet.ai",
        metaDescription: "Transformez le langage naturel en code fonctionnel, graphiques et analyse de données.",
        heroTitle: "Interpréteur de Code ChatGPT : Le Guide Ultime pour Non-Programmeurs",
        heroExcerpt: "Guide étape par étape pour analyser les feuilles de calcul et créer des visualisations.",
        footerDesc: "Votre source de confiance pour les avis, comparaisons et guides d'outils IA.",
        footerCategories: "Catégories",
        footerResources: "Ressources",
        footerCopyright: "© 2026 GenuisNet.ai. Tous droits réservés."
    },
    de: {
        pageTitle: "ChatGPT Code Interpreter: Der Ultimative Leitfaden für Nicht-Programmierer | GenuisNet.ai",
        metaDescription: "Verwandeln Sie natürliche Sprache in funktionierenden Code, Diagramme und Datenanalyse.",
        heroTitle: "ChatGPT Code Interpreter: Der Ultimative Leitfaden für Nicht-Programmierer",
        heroExcerpt: "Schritt-für-Schritt-Anleitung zur Analyse von Tabellenkalkulationen und Erstellung von Visualisierungen.",
        footerDesc: "Ihre vertrauenswürdige Quelle für KI-Tool-Bewertungen, Vergleiche und Leitfäden.",
        footerCategories: "Kategorien",
        footerResources: "Ressourcen",
        footerCopyright: "© 2026 GenuisNet.ai. Alle Rechte vorbehalten."
    },
    pt: {
        pageTitle: "Interpretador de Código ChatGPT: O Guia Definitivo para Não-Programadores | GenuisNet.ai",
        metaDescription: "Transforme linguagem natural em código funcional, gráficos e análise de dados.",
        heroTitle: "Interpretador de Código ChatGPT: O Guia Definitivo para Não-Programadores",
        heroExcerpt: "Guia passo a passo para analisar planilhas e criar visualizações.",
        footerDesc: "Sua fonte confiável para avaliações, comparações e guias de ferramentas IA.",
        footerCategories: "Categorias",
        footerResources: "Recursos",
        footerCopyright: "© 2026 GenuisNet.ai. Todos os direitos reservados."
    },
    zh: { pageTitle: "ChatGPT代码解释器：非程序员终极指南 | GenuisNet.ai", heroTitle: "ChatGPT代码解释器：非程序员终极指南", heroExcerpt: "分析电子表格和创建可视化的分步指南。", footerDesc: "您值得信赖的 AI 工具评论、比较和指南来源。", footerCategories: "类别", footerResources: "资源", footerCopyright: "© 2026 GenuisNet.ai. 保留所有权利。" },
    ja: { pageTitle: "ChatGPTコードインタープリター：非プログラマー向け究極ガイド | GenuisNet.ai", heroTitle: "ChatGPTコードインタープリター：非プログラマー向け究極ガイド", heroExcerpt: "スプレッドシートの分析と視覚化作成のステップバイステップガイド。", footerDesc: "AIツールのレビュー、比較、ガイドの信頼できる情報源。", footerCategories: "カテゴリー", footerResources: "リソース", footerCopyright: "© 2026 GenuisNet.ai. 全著作権所有。" },
    ko: { pageTitle: "ChatGPT 코드 인터프리터: 비프로그래머를 위한 궁극의 가이드 | GenuisNet.ai", heroTitle: "ChatGPT 코드 인터프리터: 비프로그래머를 위한 궁극의 가이드", heroExcerpt: "스프레드시트 분석 및 시각화 생성을 위한 단계별 가이드.", footerDesc: "AI 도구 리뷰, 비교 및 가이드의 신뢰할 수 있는 출처.", footerCategories: "카테고리", footerResources: "리소스", footerCopyright: "© 2026 GenuisNet.ai. 모든 권리 보유." },
    ar: { pageTitle: "مترجم أكواد ChatGPT: الدليل النهائي لغير المبرمجين | GenuisNet.ai", heroTitle: "مترجم أكواد ChatGPT: الدليل النهائي لغير المبرمجين", heroExcerpt: "دليل خطوة بخطوة لتحليل جداول البيانات وإنشاء التصورات.", footerDesc: "مصدرك الموثوق لمراجعات ومقارنات وأدلة أدوات الذكاء الاصطناعي.", footerCategories: "الفئات", footerResources: "الموارد", footerCopyright: "© 2026 GenuisNet.ai. جميع الحقوق محفوظة." },
    hi: { pageTitle: "ChatGPT कोड इंटरप्रेटर: गैर-प्रोग्रामर के लिए अंतिम गाइड | GenuisNet.ai", heroTitle: "ChatGPT कोड इंटरप्रेटर: गैर-प्रोग्रामर के लिए अंतिम गाइड", heroExcerpt: "स्प्रेडशीट का विश्लेषण और विज़ुअलाइज़ेशन बनाने के लिए चरण-दर-चरण मार्गदर्शिका।", footerDesc: "AI टूल समीक्षाओं, तुलनाओं और गाइड के लिए आपका विश्वसनीय स्रोत।", footerCategories: "श्रेणियाँ", footerResources: "संसाधन", footerCopyright: "© 2026 GenuisNet.ai. सर्वाधिकार सुरक्षित।" }
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
