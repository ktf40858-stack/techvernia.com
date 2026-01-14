/* ============================================
   TechVernia - Affiliate Disclosure Page i18n
   Translation system for affiliate disclosure page
   ============================================ */

// Language configuration (matching main site)
const affiliateLanguages = {
    en: { name: "English", flag: "🇬🇧", dir: "ltr" },
    fr: { name: "Français", flag: "🇫🇷", dir: "ltr" },
    es: { name: "Español", flag: "🇪🇸", dir: "ltr" },
    de: { name: "Deutsch", flag: "🇩🇪", dir: "ltr" },
    pt: { name: "Português", flag: "🇵🇹", dir: "ltr" },
    zh: { name: "中文", flag: "🇨🇳", dir: "ltr" },
    ja: { name: "日本語", flag: "🇯🇵", dir: "ltr" },
    ko: { name: "한국어", flag: "🇰🇷", dir: "ltr" },
    ar: { name: "العربية", flag: "🇸🇦", dir: "rtl" },
    hi: { name: "हिंदी", flag: "🇮🇳", dir: "ltr" }
};

// Get stored language from localStorage or default to 'en'
function getStoredLanguage() {
    // Try URL parameter first
    const urlParams = new URLSearchParams(window.location.search);
    const urlLang = urlParams.get('lang');
    if (urlLang && affiliateTranslations[urlLang]) {
        return urlLang;
    }

    // Try localStorage
    try {
        const storedLang = localStorage.getItem('language');
        if (storedLang && affiliateTranslations[storedLang]) {
            return storedLang;
        }
    } catch (e) {
        // Error reading from localStorage
    }

    // Try sessionStorage
    try {
        const sessionLang = sessionStorage.getItem('language');
        if (sessionLang && affiliateTranslations[sessionLang]) {
            return sessionLang;
        }
    } catch (e) {
        // Error reading from sessionStorage
    }

    // Default to English
    return 'en';
}

let currentLanguage = getStoredLanguage();

// Initialize the translation system
function initAffiliateI18n() {
    setAffiliateLanguage(currentLanguage);
    setupAffiliateLanguageSelector();
}

// Set language and translate the page
function setAffiliateLanguage(lang) {
    if (!affiliateTranslations[lang] || Object.keys(affiliateTranslations[lang]).length === 0) {
        lang = 'en';
    }

    currentLanguage = lang;

    // Save in multiple storages
    try {
        localStorage.setItem('language', lang);
    } catch (e) {
        // Error saving to localStorage
    }

    try {
        sessionStorage.setItem('language', lang);
    } catch (e) {
        // Error saving to sessionStorage
    }

    // Update all internal links to include lang parameter
    updateLinksWithLanguage(lang);

    // Update document direction for RTL languages
    document.documentElement.dir = affiliateLanguages[lang].dir;
    document.documentElement.lang = lang;

    // Translate all elements on the page
    translateAffiliatePage();

    // Update language selector display
    updateAffiliateLanguageSelector(lang);

    // Dispatch event for other scripts
    window.dispatchEvent(new CustomEvent('languageChanged', { detail: { language: lang } }));
}

// Translate entire page - all elements with data-affiliate-i18n
function translateAffiliatePage() {
    let translatedCount = 0;

    // Translate text content
    document.querySelectorAll('[data-affiliate-i18n]').forEach(element => {
        const key = element.getAttribute('data-affiliate-i18n');
        const translation = getAffiliateTranslation(key);

        if (translation) {
            element.textContent = translation;
            translatedCount++;
        }
    });

    // Translate HTML content
    document.querySelectorAll('[data-affiliate-i18n-html]').forEach(element => {
        const key = element.getAttribute('data-affiliate-i18n-html');
        const translation = getAffiliateTranslation(key);
        if (translation) {
            element.innerHTML = translation;
        }
    });

    // Translate placeholders
    document.querySelectorAll('[data-affiliate-i18n-placeholder]').forEach(element => {
        const key = element.getAttribute('data-affiliate-i18n-placeholder');
        const translation = getAffiliateTranslation(key);
        if (translation) {
            element.placeholder = translation;
        }
    });

    // Translate aria-labels
    document.querySelectorAll('[data-affiliate-i18n-aria]').forEach(element => {
        const key = element.getAttribute('data-affiliate-i18n-aria');
        const translation = getAffiliateTranslation(key);
        if (translation) {
            element.setAttribute('aria-label', translation);
        }
    });

    // Translate title attributes
    document.querySelectorAll('[data-affiliate-i18n-title]').forEach(element => {
        const key = element.getAttribute('data-affiliate-i18n-title');
        const translation = getAffiliateTranslation(key);
        if (translation) {
            element.setAttribute('title', translation);
        }
    });

    // Update page title
    const pageTitle = document.querySelector('title');
    if (pageTitle) {
        const translation = getAffiliateTranslation('page.title');
        if (translation) {
            document.title = translation;
        }
    }

    // Update meta description
    const metaDesc = document.querySelector('meta[name="description"]');
    if (metaDesc) {
        const translation = getAffiliateTranslation('page.description');
        if (translation) {
            metaDesc.setAttribute('content', translation);
        }
    }
}

// Get translation for a key with fallback to English
function getAffiliateTranslation(key) {
    // Check current language
    if (affiliateTranslations[currentLanguage] && affiliateTranslations[currentLanguage][key]) {
        return affiliateTranslations[currentLanguage][key];
    }

    // Fallback to English
    if (affiliateTranslations.en && affiliateTranslations.en[key]) {
        return affiliateTranslations.en[key];
    }

    return null;
}

// Update all internal links with language parameter
function updateLinksWithLanguage(lang) {
    if (lang === 'en') return; // Don't add parameter for default language

    // Update all internal navigation links
    document.querySelectorAll('a[href]').forEach(link => {
        const href = link.getAttribute('href');

        // Skip external links, anchors, and javascript links
        if (!href || href.startsWith('#') || href.startsWith('http') || href.startsWith('javascript:')) {
            return;
        }

        // Check if it's a relative link to another page
        if (href.endsWith('.html') || href.includes('/pages/') || href.includes('../')) {
            const url = new URL(href, window.location.href);

            // Add or update lang parameter
            url.searchParams.set('lang', lang);

            // Update the link
            link.setAttribute('href', url.pathname + url.search);
        }
    });
}

// Setup language selector
function setupAffiliateLanguageSelector() {
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
            const lang = option.getAttribute('data-lang');
            setAffiliateLanguage(lang);
            langSelector.classList.remove('active');
        });
    });
}

// Update language selector display
function updateAffiliateLanguageSelector(lang) {
    const langCurrent = document.querySelector('.lang-current');
    if (langCurrent) {
        langCurrent.textContent = lang.toUpperCase();
    }

    document.querySelectorAll('.lang-option').forEach(option => {
        option.classList.toggle('active', option.getAttribute('data-lang') === lang);
    });
}

// Translate single element
function translateAffiliateElement(element) {
    const key = element.getAttribute('data-affiliate-i18n');
    if (key) {
        const translation = getAffiliateTranslation(key);
        if (translation) {
            element.textContent = translation;
        }
    }
}

// Get current language
function getCurrentAffiliateLanguage() {
    return currentLanguage;
}

// Get all available languages
function getAvailableAffiliateLanguages() {
    return Object.keys(affiliateLanguages);
}

// Translate a specific key (for dynamic content)
function affiliateT(key) {
    return getAffiliateTranslation(key) || key;
}

// Export functions
window.affiliateI18n = {
    init: initAffiliateI18n,
    setLanguage: setAffiliateLanguage,
    getTranslation: getAffiliateTranslation,
    translatePage: translateAffiliatePage,
    translateElement: translateAffiliateElement,
    getCurrentLanguage: getCurrentAffiliateLanguage,
    getAvailableLanguages: getAvailableAffiliateLanguages,
    t: affiliateT,
    languages: affiliateLanguages
};

// Auto-initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAffiliateI18n);
} else {
    initAffiliateI18n();
}
