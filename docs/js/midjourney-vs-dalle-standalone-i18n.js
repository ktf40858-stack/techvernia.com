/**
 * MIDJOURNEY VS DALL-E 3 - STANDALONE i18n SYSTEM
 * Self-contained translation system for this comparison page
 */



// Load translations
const translations = window.midjourneyVsDalleTranslations || {};

.length,
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




function getTranslation(key) {
    if (translations[currentLanguage] && translations[currentLanguage][key]) {
        return translations[currentLanguage][key];
    }
    if (translations.en && translations.en[key]) {
        
        return translations.en[key];
    }
    
    return key;
}

function translatePage() {
    
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

    
}

function setLanguage(lang) {
    

    if (!translations[lang] || Object.keys(translations[lang]).length === 0) {
        
        lang = 'en';
    }

    currentLanguage = lang;

    try {
        localStorage.setItem('language', lang);
        sessionStorage.setItem('language', lang);
        
    } catch (e) {
        
    }

    document.documentElement.dir = languages[lang].dir;
    document.documentElement.lang = lang;

    translatePage();
    updateLanguageSelector(lang);

    window.dispatchEvent(new CustomEvent('languageChanged', {
        detail: { language: lang }
    }));

    
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
        
        return;
    }

    

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

    
}

function getCurrentLanguage() {
    return currentLanguage;
}

function initI18n() {
    
    .length);
    

    if (Object.keys(translations).length === 0) {
        
        return;
    }

    setupLanguageSelector();
    setLanguage(currentLanguage);

    
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

        
    }, 100);
});

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initI18n);
} else {
    initI18n();
}


