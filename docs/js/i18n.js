/* ============================================
   TechVernia - Internationalization (i18n)
   Multi-language support for 10 languages.
   The HTML is written in English, so English needs no dictionary.
   Each other language lives in js/i18n/<lang>.js (~2.3 MB) and is
   only downloaded when a visitor picks that language.
   ============================================ */

const translations = window.TV_I18N = window.TV_I18N || {};

// Folder of this script, used to locate js/i18n/<lang>.js from any page depth
const i18nBaseUrl = (function () {
    const script = document.currentScript;
    if (script && script.src) {
        return script.src.replace(/i18n\.js(\?.*)?$/, 'i18n/');
    }
    return '/js/i18n/';
})();

// Typing words for hero section in different languages
const typingWords = {
    en: ["Best AI Tools", "Perfect Solution", "Smart Automation", "AI Innovation"],
    es: ["Mejores Herramientas IA", "Solución Perfecta", "Automatización Inteligente"],
    fr: ["Meilleurs Outils IA", "Solution Parfaite", "Automatisation Intelligente"],
    de: ["Beste KI-Tools", "Perfekte Lösung", "Intelligente Automatisierung"],
    pt: ["Melhores Ferramentas IA", "Solução Perfeita", "Automação Inteligente"],
    zh: ["最佳AI工具", "完美解决方案", "智能自动化"],
    ja: ["最高のAIツール", "完璧なソリューション", "スマート自動化"],
    ko: ["최고의 AI 도구", "완벽한 솔루션", "스마트 자동화"],
    ar: ["أفضل أدوات الذكاء الاصطناعي", "الحل المثالي", "الأتمتة الذكية"],
    hi: ["सर्वश्रेष्ठ AI टूल्स", "परफेक्ट समाधान", "स्मार्ट ऑटोमेशन"]
};

// Language configuration
const languages = {
    en: { name: "English", flag: "🇺🇸", dir: "ltr" },
    es: { name: "Español", flag: "🇪🇸", dir: "ltr" },
    fr: { name: "Français", flag: "🇫🇷", dir: "ltr" },
    de: { name: "Deutsch", flag: "🇩🇪", dir: "ltr" },
    pt: { name: "Português", flag: "🇧🇷", dir: "ltr" },
    zh: { name: "中文", flag: "🇨🇳", dir: "ltr" },
    ja: { name: "日本語", flag: "🇯🇵", dir: "ltr" },
    ko: { name: "한국어", flag: "🇰🇷", dir: "ltr" },
    ar: { name: "العربية", flag: "🇸🇦", dir: "rtl" },
    hi: { name: "हिन्दी", flag: "🇮🇳", dir: "ltr" }
};

// Current language - URL parameter first, then saved choice, then English
function getStoredLanguage() {
    const urlLang = new URLSearchParams(window.location.search).get('lang');
    if (urlLang && languages[urlLang]) {
        return urlLang;
    }

    for (const storage of ['localStorage', 'sessionStorage']) {
        try {
            const stored = window[storage].getItem('language');
            if (stored && languages[stored]) {
                return stored;
            }
        } catch (e) {
            // Storage blocked (private mode, file://)
        }
    }

    return 'en';
}

let currentLanguage = getStoredLanguage();
let pageTranslated = false;
const pendingLoads = {};

// Download a language dictionary once
function loadLanguage(lang) {
    if (lang === 'en' || translations[lang]) {
        return Promise.resolve();
    }
    if (!pendingLoads[lang]) {
        pendingLoads[lang] = new Promise((resolve, reject) => {
            const script = document.createElement('script');
            script.src = i18nBaseUrl + lang + '.js';
            script.async = true;
            script.onload = resolve;
            script.onerror = () => {
                delete pendingLoads[lang];
                reject(new Error('Could not load ' + lang));
            };
            document.head.appendChild(script);
        });
    }
    return pendingLoads[lang];
}

// Initialize i18n
function initI18n() {
    setupLanguageSelector();
    setLanguage(currentLanguage);
}

function saveLanguage(lang) {
    for (const storage of ['localStorage', 'sessionStorage']) {
        try {
            window[storage].setItem('language', lang);
        } catch (e) {
            // Storage blocked
        }
    }
}

// Set language - translates the ENTIRE page
function setLanguage(lang) {
    if (!languages[lang]) {
        lang = 'en';
    }

    // Back to English after a translation: the original text is gone, reload it
    if (lang === 'en' && pageTranslated) {
        saveLanguage('en');
        const url = new URL(window.location.href);
        url.searchParams.delete('lang');
        window.location.replace(url.pathname + url.search + url.hash);
        return;
    }

    // Pages without translatable text only need to remember the choice
    if (!document.querySelector('[data-i18n], [data-i18n-html], [data-i18n-placeholder], [data-i18n-aria], [data-i18n-title], [data-i18n-alt], [data-i18n-text]')) {
        applyLanguage(lang);
        return;
    }

    loadLanguage(lang).then(() => applyLanguage(lang), () => applyLanguage('en'));
}

function applyLanguage(lang) {
    currentLanguage = lang;
    saveLanguage(lang);

    // Update all internal links to include lang parameter
    updateLinksWithLanguage(lang);

    // Update document direction for RTL languages
    document.documentElement.dir = languages[lang].dir;
    document.documentElement.lang = lang;

    if (lang !== 'en' && translations[lang]) {
        translatePage();
        pageTranslated = true;
    }

    // Update language selector display
    updateLanguageSelector(lang);

    // Update typing words for hero
    if (window.typingEffect) {
        window.typingEffect.words = typingWords[lang] || typingWords.en;
    }

    // Dispatch event for other scripts
    window.dispatchEvent(new CustomEvent('languageChanged', { detail: { language: lang } }));
}

// Translate entire page - ALL elements with data-i18n
function translatePage() {
    document.querySelectorAll('[data-i18n]').forEach(element => {
        const translation = getTranslation(element.getAttribute('data-i18n'));
        if (translation) {
            element.textContent = translation;
        }
    });

    document.querySelectorAll('[data-i18n-html]').forEach(element => {
        const translation = getTranslation(element.getAttribute('data-i18n-html'));
        if (translation) {
            element.innerHTML = translation;
        }
    });

    const attributeMap = {
        'data-i18n-placeholder': 'placeholder',
        'data-i18n-aria': 'aria-label',
        'data-i18n-title': 'title',
        'data-i18n-alt': 'alt',
        'data-i18n-text': 'data-text'
    };
    for (const [source, target] of Object.entries(attributeMap)) {
        document.querySelectorAll('[' + source + ']').forEach(element => {
            const translation = getTranslation(element.getAttribute(source));
            if (translation) {
                element.setAttribute(target, translation);
            }
        });
    }

    const pageTitle = document.querySelector('title[data-i18n]');
    if (pageTitle) {
        const translation = getTranslation(pageTitle.getAttribute('data-i18n'));
        if (translation) {
            document.title = translation;
        }
    }
}

// Get text nodes from element
function getTextNodes(element) {
    const textNodes = [];
    const walker = document.createTreeWalker(element, NodeFilter.SHOW_TEXT, null, false);
    let node;
    while (node = walker.nextNode()) {
        if (node.textContent.trim()) {
            textNodes.push(node);
        }
    }
    return textNodes;
}

// Tool-specific and certification translations defined by page scripts
const translationObjects = [
    'comparisonsTranslations',
    'chatbotsComparisonTranslations',
    'cursorTranslations',
    'githubCopilotVsCursorTranslations',
    'cursorVsWindsurfTranslations',
    'githubCopilotVsCodeiumTranslations',
    'githubCopilotVsTabnineTranslations',
    'ccnaTranslations',
    'devnetAssociateTranslations',
    'ccnpEnterpriseTranslations',
    'ciscoWirelessSpecialistTranslations',
    'ciscoInfrastructureSpecialistTranslations',
    'ccieEnterpriseTranslations',
    'jnciaMistaiTranslations',
    'jncipMistaiTranslations',
    'jncisMistaiWirelessTranslations',
    'ansibleAutomationTranslations',
    'ansibleAdvancedTranslations',
    'terraformAssociateTranslations',
    'terraformProfessionalTranslations',
    'zabbixSpecialistTranslations',
    'zabbixProfessionalTranslations',
    'zabbixExpertTranslations',
    'rhceTranslations'
];

// Get translation for a key. Returns null when missing, so the English HTML stays.
function getTranslation(key) {
    if (translations[currentLanguage] && translations[currentLanguage][key]) {
        return translations[currentLanguage][key];
    }

    for (const objName of translationObjects) {
        const obj = window[objName];
        if (obj && obj[currentLanguage] && obj[currentLanguage][key]) {
            return obj[currentLanguage][key];
        }
    }

    for (const objName of translationObjects) {
        const obj = window[objName];
        if (obj && obj.en && obj.en[key]) {
            return obj.en[key];
        }
    }

    return null;
}

// Update all internal links with language parameter
function updateLinksWithLanguage(lang) {
    if (lang === 'en') return; // Don't add parameter for default language

    document.querySelectorAll('a[href]').forEach(link => {
        const href = link.getAttribute('href');

        // Skip external links, anchors, and javascript links
        if (!href || href.startsWith('#') || href.startsWith('http') || href.startsWith('javascript:')) {
            return;
        }

        if (href.endsWith('.html') || href.includes('/pages/') || href.includes('../')) {
            const url = new URL(href, window.location.href);
            url.searchParams.set('lang', lang);
            link.setAttribute('href', url.pathname + url.search);
        }
    });
}

// Setup language selector
function setupLanguageSelector() {
    const langBtn = document.getElementById('lang-btn');
    const langDropdown = document.getElementById('lang-dropdown');
    const langSelector = document.querySelector('.language-selector');

    if (!langBtn || !langDropdown) return;

    langBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        langSelector.classList.toggle('active');
    });

    document.addEventListener('click', () => {
        langSelector.classList.remove('active');
    });

    langDropdown.querySelectorAll('.lang-option').forEach(option => {
        option.addEventListener('click', () => {
            setLanguage(option.getAttribute('data-lang'));
            langSelector.classList.remove('active');
        });
    });
}

// Update language selector display
function updateLanguageSelector(lang) {
    const langCurrent = document.querySelector('.lang-current');
    if (langCurrent) {
        langCurrent.textContent = lang.toUpperCase();
    }

    document.querySelectorAll('.lang-option').forEach(option => {
        option.classList.toggle('active', option.getAttribute('data-lang') === lang);
    });
}

// Translate single element
function translateElement(element) {
    const key = element.getAttribute('data-i18n');
    if (key) {
        const translation = getTranslation(key);
        if (translation) {
            element.textContent = translation;
        }
    }
}

// Get current language
function getCurrentLanguage() {
    return currentLanguage;
}

// Get all available languages
function getAvailableLanguages() {
    return Object.keys(languages);
}

// Translate a specific key (for dynamic content)
function t(key) {
    return getTranslation(key) || key;
}

// Export functions
window.i18n = {
    init: initI18n,
    setLanguage,
    loadLanguage,
    getTranslation,
    translatePage,
    translateElement,
    getCurrentLanguage,
    getAvailableLanguages,
    t,
    languages,
    typingWords
};

// Auto-initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initI18n);
} else {
    initI18n();
}
