/**
 * CURSOR VS WINDSURF - STANDALONE i18n SYSTEM
 * Self-contained translation system for this comparison page
 * No dependency on the massive global i18n.js file
 */



// ============================================
// TRANSLATIONS DATA
// ============================================

// Load translations from the separate file
// This will be loaded AFTER cursor-vs-windsurf-i18n.js
const translations = window.cursorVsWindsurfTranslations || {};

.length,
    keys: translations.en ? Object.keys(translations.en).length : 0
});

// ============================================
// LANGUAGE CONFIGURATION
// ============================================

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

// ============================================
// STATE
// ============================================

let currentLanguage = localStorage.getItem('language') ||
                      sessionStorage.getItem('language') ||
                      'en';



);

// ============================================
// CORE FUNCTIONS
// ============================================

/**
 * Get translation for a key
 */
function getTranslation(key) {
    if (translations[currentLanguage] && translations[currentLanguage][key]) {
        return translations[currentLanguage][key];
    }

    // Fallback to English
    if (translations.en && translations.en[key]) {
        
        return translations.en[key];
    }

    
    return key; // Return the key itself as last resort
}

/**
 * Translate all elements with data-i18n attributes
 */
function translatePage() {
    
    let count = 0;

    // Translate text content
    document.querySelectorAll('[data-i18n]').forEach(element => {
        const key = element.getAttribute('data-i18n');
        const translation = getTranslation(key);

        if (translation && translation !== key) {
            element.textContent = translation;
            count++;
        }
    });

    // Translate HTML content
    document.querySelectorAll('[data-i18n-html]').forEach(element => {
        const key = element.getAttribute('data-i18n-html');
        const translation = getTranslation(key);

        if (translation && translation !== key) {
            element.innerHTML = translation;
            count++;
        }
    });

    // Translate placeholders
    document.querySelectorAll('[data-i18n-placeholder]').forEach(element => {
        const key = element.getAttribute('data-i18n-placeholder');
        const translation = getTranslation(key);

        if (translation && translation !== key) {
            element.placeholder = translation;
            count++;
        }
    });

    // Translate aria-labels
    document.querySelectorAll('[data-i18n-aria]').forEach(element => {
        const key = element.getAttribute('data-i18n-aria');
        const translation = getTranslation(key);

        if (translation && translation !== key) {
            element.setAttribute('aria-label', translation);
            count++;
        }
    });

    // Translate title attributes
    document.querySelectorAll('[data-i18n-title]').forEach(element => {
        const key = element.getAttribute('data-i18n-title');
        const translation = getTranslation(key);

        if (translation && translation !== key) {
            element.setAttribute('title', translation);
            count++;
        }
    });

    // Update page title
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

/**
 * Set the current language and translate the page
 */
function setLanguage(lang) {
    

    // Validate language
    if (!translations[lang] || Object.keys(translations[lang]).length === 0) {
        
        lang = 'en';
    }

    currentLanguage = lang;

    // Save to storage
    try {
        localStorage.setItem('language', lang);
        sessionStorage.setItem('language', lang);
        
    } catch (e) {
        
    }

    // Update document direction for RTL languages
    document.documentElement.dir = languages[lang].dir;
    document.documentElement.lang = lang;

    // Translate the page
    translatePage();

    // Update language selector display
    updateLanguageSelector(lang);

    // Dispatch event for other scripts (like auto-translate.js)
    window.dispatchEvent(new CustomEvent('languageChanged', {
        detail: { language: lang }
    }));

    
}

/**
 * Update language selector UI
 */
function updateLanguageSelector(lang) {
    // Update current language display
    const langCurrent = document.querySelector('.lang-current');
    if (langCurrent) {
        langCurrent.textContent = lang.toUpperCase();
    }

    // Update active state on options
    document.querySelectorAll('.lang-option').forEach(option => {
        option.classList.toggle('active', option.getAttribute('data-lang') === lang);
    });
}

/**
 * Setup language selector event listeners
 */
function setupLanguageSelector() {
    const langBtn = document.getElementById('lang-btn');
    const langDropdown = document.getElementById('lang-dropdown');
    const langSelector = document.querySelector('.language-selector');

    if (!langBtn || !langDropdown || !langSelector) {
        
        return;
    }

    

    // Toggle dropdown
    langBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        langSelector.classList.toggle('active');
    });

    // Close dropdown when clicking outside
    document.addEventListener('click', () => {
        langSelector.classList.remove('active');
    });

    // Language option clicks
    langDropdown.querySelectorAll('.lang-option').forEach(option => {
        option.addEventListener('click', (e) => {
            e.stopPropagation();
            const lang = option.getAttribute('data-lang');
            setLanguage(lang);
            langSelector.classList.remove('active');
        });
    });

    
}

/**
 * Get current language
 */
function getCurrentLanguage() {
    return currentLanguage;
}

/**
 * Initialize the i18n system
 */
function initI18n() {
    
    .length);
    

    // Check if translations are loaded
    if (Object.keys(translations).length === 0) {
        
        return;
    }

    // Setup language selector
    setupLanguageSelector();

    // Set initial language (will translate the page)
    setLanguage(currentLanguage);

    
}

// ============================================
// EXPORT TO WINDOW
// ============================================

window.cursorVsWindsurfI18n = {
    setLanguage,
    getTranslation,
    translatePage,
    getCurrentLanguage,
    languages,
    init: initI18n
};

// Override main.js LanguageSelector to use this system
window.addEventListener('DOMContentLoaded', () => {
    // Wait a bit for other scripts to load
    setTimeout(() => {
        

        // Find language options and attach our handler
        document.querySelectorAll('.lang-option').forEach(option => {
            // Remove existing listeners by cloning
            const newOption = option.cloneNode(true);
            option.parentNode.replaceChild(newOption, option);

            // Add our listener
            newOption.addEventListener('click', (e) => {
                e.stopPropagation();
                const lang = newOption.getAttribute('data-lang');
                setLanguage(lang);

                // Close dropdown
                const selector = document.querySelector('.language-selector');
                if (selector) {
                    selector.classList.remove('active');
                }
            });
        });

        
    }, 100);
});

// ============================================
// AUTO-INITIALIZE
// ============================================

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initI18n);
} else {
    initI18n();
}


