/**
 * MIDJOURNEY VS DALL-E 3 - STANDALONE i18n SYSTEM
 * Self-contained translation system for this comparison page
 */

console.log('[2/2] midjourney-vs-dalle-standalone-i18n.js loading...');

// Load translations
const translations = window.midjourneyVsDalleTranslations || {};

console.log('[2/2] Checking translations:', {
    available: !!window.midjourneyVsDalleTranslations,
    languages: Object.keys(translations).length,
    keys: translations.en ? Object.keys(translations.en).length : 0
});

// Language configuration
const languages = {
    en: { name: 'English', flag: '🇺🇸', dir: 'ltr' },
    es: { name: 'Español', flag: '🇪🇸', dir: 'ltr' },
    fr: { name: 'Français', flag: '🇫🇷', dir: 'ltr' },
    de: { name: 'Deutsch', flag: '🇩🇪', dir: 'ltr' },
    pt: { name: 'Português', flag: '🇧🇷', dir: 'ltr' },
    zh: { name: '中文', flag: '🇨🇳', dir: 'ltr' },
    ja: { name: '日本語', flag: '🇯🇵', dir: 'ltr' },
    ko: { name: '한국어', flag: '🇰🇷', dir: 'ltr' },
    ar: { name: 'العربية', flag: '🇸🇦', dir: 'rtl' },
    hi: { name: 'हिन्दी', flag: '🇮🇳', dir: 'ltr' }
};

let currentLanguage = localStorage.getItem('language') || sessionStorage.getItem('language') || 'en';

console.log('[Midjourney vs DALL-E i18n] Initializing...');
console.log('Current language:', currentLanguage);

function getTranslation(key) {
    if (translations[currentLanguage] && translations[currentLanguage][key]) {
        return translations[currentLanguage][key];
    }
    if (translations.en && translations.en[key]) {
        console.warn(`Translation missing for "${key}" in ${currentLanguage}, using English`);
        return translations.en[key];
    }
    console.warn(`Translation not found for key: "${key}"`);
    return key;
}

function translatePage() {
    console.log('[translatePage] Starting translation to:', currentLanguage);
    let count = 0;

    document.querySelectorAll('[data-i18n]').forEach(element => {
        const key = element.getAttribute('data-i18n');
        const translation = getTranslation(key);
        if (translation && translation !== key) {
            element.textContent = translation;
            count++;
        }
    });

    document.querySelectorAll('[data-i18n-html]').forEach(element => {
        const key = element.getAttribute('data-i18n-html');
        const translation = getTranslation(key);
        if (translation && translation !== key) {
            element.innerHTML = translation;
            count++;
        }
    });

    document.querySelectorAll('[data-i18n-placeholder]').forEach(element => {
        const key = element.getAttribute('data-i18n-placeholder');
        const translation = getTranslation(key);
        if (translation && translation !== key) {
            element.placeholder = translation;
            count++;
        }
    });

    document.querySelectorAll('[data-i18n-aria]').forEach(element => {
        const key = element.getAttribute('data-i18n-aria');
        const translation = getTranslation(key);
        if (translation && translation !== key) {
            element.setAttribute('aria-label', translation);
            count++;
        }
    });

    document.querySelectorAll('[data-i18n-title]').forEach(element => {
        const key = element.getAttribute('data-i18n-title');
        const translation = getTranslation(key);
        if (translation && translation !== key) {
            element.setAttribute('title', translation);
            count++;
        }
    });

    const pageTitle = document.querySelector('title[data-i18n]');
    if (pageTitle) {
        const key = pageTitle.getAttribute('data-i18n');
        const translation = getTranslation(key);
        if (translation && translation !== key) {
            document.title = translation;
            count++;
        }
    }

    console.log(`[translatePage] Translated ${count} elements`);
}

function setLanguage(lang) {
    console.log('[setLanguage] Switching to:', lang);

    if (!translations[lang] || Object.keys(translations[lang]).length === 0) {
        console.warn(`Language '${lang}' not available, falling back to English`);
        lang = 'en';
    }

    currentLanguage = lang;

    try {
        localStorage.setItem('language', lang);
        sessionStorage.setItem('language', lang);
        console.log('Language saved to storage:', lang);
    } catch (e) {
        console.warn('Could not save to storage');
    }

    document.documentElement.dir = languages[lang].dir;
    document.documentElement.lang = lang;

    translatePage();
    updateLanguageSelector(lang);

    window.dispatchEvent(new CustomEvent('languageChanged', {
        detail: { language: lang }
    }));

    console.log('[setLanguage] Language switched to:', lang);
}

function updateLanguageSelector(lang) {
    const langCurrent = document.querySelector('.lang-current');
    if (langCurrent) {
        langCurrent.textContent = lang.toUpperCase();
    }

    document.querySelectorAll('.lang-option').forEach(option => {
        option.classList.toggle('active', option.getAttribute('data-lang') === lang);
    });
}

function setupLanguageSelector() {
    const langBtn = document.getElementById('lang-btn');
    const langDropdown = document.getElementById('lang-dropdown');
    const langSelector = document.querySelector('.language-selector');

    if (!langBtn || !langDropdown || !langSelector) {
        console.warn('Language selector elements not found');
        return;
    }

    console.log('Setting up language selector');

    langBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        langSelector.classList.toggle('active');
    });

    document.addEventListener('click', () => {
        langSelector.classList.remove('active');
    });

    langDropdown.querySelectorAll('.lang-option').forEach(option => {
        option.addEventListener('click', (e) => {
            e.stopPropagation();
            const lang = option.getAttribute('data-lang');
            setLanguage(lang);
            langSelector.classList.remove('active');
        });
    });

    console.log('Language selector setup complete');
}

function getCurrentLanguage() {
    return currentLanguage;
}

function initI18n() {
    console.log('[initI18n] Initializing Midjourney vs DALL-E i18n');
    console.log('Available languages:', Object.keys(translations).length);
    console.log('Current language:', currentLanguage);

    if (Object.keys(translations).length === 0) {
        console.error('No translations loaded! Make sure midjourney-vs-dalle-i18n.js is loaded first.');
        return;
    }

    setupLanguageSelector();
    setLanguage(currentLanguage);

    console.log('[initI18n] Initialization complete');
}

window.midjourneyVsDalleI18n = {
    setLanguage,
    getTranslation,
    translatePage,
    getCurrentLanguage,
    languages,
    init: initI18n
};

// Override main.js LanguageSelector
window.addEventListener('DOMContentLoaded', () => {
    setTimeout(() => {
        console.log('Overriding main.js language selector with standalone i18n');

        document.querySelectorAll('.lang-option').forEach(option => {
            const newOption = option.cloneNode(true);
            option.parentNode.replaceChild(newOption, option);

            newOption.addEventListener('click', (e) => {
                e.stopPropagation();
                const lang = newOption.getAttribute('data-lang');
                setLanguage(lang);

                const selector = document.querySelector('.language-selector');
                if (selector) {
                    selector.classList.remove('active');
                }
            });
        });

        console.log('Language selector override complete');
    }, 100);
});

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initI18n);
} else {
    initI18n();
}

console.log('[2/2] Midjourney vs DALL-E standalone i18n loaded');
