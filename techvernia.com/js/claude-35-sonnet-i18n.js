// Claude 3.5 Sonnet Update Article - Multilingual Translations
// 10 Languages: EN, ES, FR, DE, PT, ZH, JA, KO, AR, HI

console.log('📦 claude-35-sonnet-i18n.js loaded');

const articleTranslations = {
    en: {
        pageTitle: "Claude 3.5 Sonnet Update: What's New and Why It Matters | TechVernia",
        metaDescription: "Breaking down the massive improvements in coding and reasoning capabilities.",
        heroTitle: "Claude 3.5 Sonnet Update: What's New and Why It Matters",
        heroExcerpt: "Anthropic's latest model brings impressive improvements to coding and analysis.",
        footerDesc: "Your trusted source for AI tool reviews, comparisons, and guides.",
        footerCategories: "Categories",
        footerResources: "Resources",
        footerCopyright: "© 2026 TechVernia. All rights reserved."
    },
    es: {
        pageTitle: "Actualización de Claude 3.5 Sonnet: Qué Hay de Nuevo y Por Qué Importa | TechVernia",
        metaDescription: "Desglosando las mejoras masivas en capacidades de codificación y razonamiento.",
        heroTitle: "Actualización de Claude 3.5 Sonnet: Qué Hay de Nuevo y Por Qué Importa",
        heroExcerpt: "El último modelo de Anthropic trae mejoras impresionantes en codificación y análisis.",
        footerDesc: "Tu fuente confiable de reseñas, comparaciones y guías de herramientas IA.",
        footerCategories: "Categorías",
        footerResources: "Recursos",
        footerCopyright: "© 2026 TechVernia. Todos los derechos reservados."
    },
    fr: {
        pageTitle: "Mise à Jour de Claude 3.5 Sonnet : Quoi de Neuf et Pourquoi C'est Important | TechVernia",
        metaDescription: "Décomposition des améliorations massives en capacités de codage et de raisonnement.",
        heroTitle: "Mise à Jour de Claude 3.5 Sonnet : Quoi de Neuf et Pourquoi C'est Important",
        heroExcerpt: "Le dernier modèle d'Anthropic apporte des améliorations impressionnantes au codage et à l'analyse.",
        footerDesc: "Votre source de confiance pour les avis, comparaisons et guides d'outils IA.",
        footerCategories: "Catégories",
        footerResources: "Ressources",
        footerCopyright: "© 2026 TechVernia. Tous droits réservés."
    },
    de: {
        pageTitle: "Claude 3.5 Sonnet Update: Was ist Neu und Warum es Wichtig ist | TechVernia",
        metaDescription: "Analyse der massiven Verbesserungen bei Codierungs- und Reasoning-Fähigkeiten.",
        heroTitle: "Claude 3.5 Sonnet Update: Was ist Neu und Warum es Wichtig ist",
        heroExcerpt: "Das neueste Modell von Anthropic bringt beeindruckende Verbesserungen bei Codierung und Analyse.",
        footerDesc: "Ihre vertrauenswürdige Quelle für KI-Tool-Bewertungen, Vergleiche und Leitfäden.",
        footerCategories: "Kategorien",
        footerResources: "Ressourcen",
        footerCopyright: "© 2026 TechVernia. Alle Rechte vorbehalten."
    },
    pt: {
        pageTitle: "Atualização Claude 3.5 Sonnet: O Que Há de Novo e Por Que Importa | TechVernia",
        metaDescription: "Detalhando as melhorias massivas em capacidades de codificação e raciocínio.",
        heroTitle: "Atualização Claude 3.5 Sonnet: O Que Há de Novo e Por Que Importa",
        heroExcerpt: "O modelo mais recente da Anthropic traz melhorias impressionantes em codificação e análise.",
        footerDesc: "Sua fonte confiável para avaliações, comparações e guias de ferramentas IA.",
        footerCategories: "Categorias",
        footerResources: "Recursos",
        footerCopyright: "© 2026 TechVernia. Todos os direitos reservados."
    },
    zh: { pageTitle: "Claude 3.5 Sonnet更新：新功能及其重要性 | TechVernia", heroTitle: "Claude 3.5 Sonnet更新：新功能及其重要性", heroExcerpt: "Anthropic的最新模型在编码和分析方面带来了令人印象深刻的改进。", footerDesc: "您值得信赖的 AI 工具评论、比较和指南来源。", footerCategories: "类别", footerResources: "资源", footerCopyright: "© 2026 TechVernia. 保留所有权利。" },
    ja: { pageTitle: "Claude 3.5 Sonnetアップデート：新機能とその重要性 | TechVernia", heroTitle: "Claude 3.5 Sonnetアップデート：新機能とその重要性", heroExcerpt: "Anthropicの最新モデルは、コーディングと分析に印象的な改善をもたらします。", footerDesc: "AIツールのレビュー、比較、ガイドの信頼できる情報源。", footerCategories: "カテゴリー", footerResources: "リソース", footerCopyright: "© 2026 TechVernia. 全著作権所有。" },
    ko: { pageTitle: "Claude 3.5 Sonnet 업데이트: 새로운 기능과 중요성 | TechVernia", heroTitle: "Claude 3.5 Sonnet 업데이트: 새로운 기능과 중요성", heroExcerpt: "Anthropic의 최신 모델은 코딩 및 분석에 인상적인 개선을 가져옵니다.", footerDesc: "AI 도구 리뷰, 비교 및 가이드의 신뢰할 수 있는 출처.", footerCategories: "카테고리", footerResources: "리소스", footerCopyright: "© 2026 TechVernia. 모든 권리 보유." },
    ar: { pageTitle: "تحديث Claude 3.5 Sonnet: ما الجديد ولماذا هو مهم | TechVernia", heroTitle: "تحديث Claude 3.5 Sonnet: ما الجديد ولماذا هو مهم", heroExcerpt: "أحدث نموذج من Anthropic يجلب تحسينات مذهلة للبرمجة والتحليل.", footerDesc: "مصدرك الموثوق لمراجعات ومقارنات وأدلة أدوات الذكاء الاصطناعي.", footerCategories: "الفئات", footerResources: "الموارد", footerCopyright: "© 2026 TechVernia. جميع الحقوق محفوظة." },
    hi: { pageTitle: "Claude 3.5 Sonnet अपडेट: क्या नया है और यह क्यों महत्वपूर्ण है | TechVernia", heroTitle: "Claude 3.5 Sonnet अपडेट: क्या नया है और यह क्यों महत्वपूर्ण है", heroExcerpt: "Anthropic का नवीनतम मॉडल कोडिंग और विश्लेषण में प्रभावशाली सुधार लाता है।", footerDesc: "AI टूल समीक्षाओं, तुलनाओं और गाइड के लिए आपका विश्वसनीय स्रोत।", footerCategories: "श्रेणियाँ", footerResources: "संसाधन", footerCopyright: "© 2026 TechVernia. सर्वाधिकार सुरक्षित।" }
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
