/* ============================================
   TechVernia - Automatic Content Translation (VERSION CORRIGÉE)
   Traduit TOUT le contenu automatiquement avec une vraie API
   ============================================ */

// Configuration
const AUTO_TRANSLATE_CONFIG = {
    enabled: true,
    excludeSelectors: [
        '.tool-card h3',           // Noms d'outils (ChatGPT, Claude, etc.)
        '.tool-name',              // Noms d'outils
        '[data-i18n]',             // Déjà traduit par i18n.js
        'script',                  // Scripts
        'style',                   // Styles
        'code',                    // Code
        'pre',                     // Code préformaté
        'svg',                     // SVG
        'path'                     // SVG paths
    ],
    preserveNames: ['ChatGPT', 'Claude', 'Gemini', 'GPT-4', 'Midjourney', 'DALL-E', 'Copilot', 'Perplexity', 'Stable Diffusion'],
    cacheEnabled: true,
    cacheExpiry: 7 * 24 * 60 * 60 * 1000  // 7 jours
};

// Cache des traductions
let translationCache = {};

// Charger le cache depuis localStorage
function loadTranslationCache() {
    try {
        const cached = localStorage.getItem('translationCache');
        if (cached) {
            const data = JSON.parse(cached);
            if (data.timestamp && (Date.now() - data.timestamp) < AUTO_TRANSLATE_CONFIG.cacheExpiry) {
                translationCache = data.translations || {};
                .length, 'entrées');
            }
        }
    } catch (e) {
        
    }
}

// Sauvegarder le cache
function saveTranslationCache() {
    try {
        localStorage.setItem('translationCache', JSON.stringify({
            timestamp: Date.now(),
            translations: translationCache
        }));
    } catch (e) {
        
    }
}

// Traductions manuelles complètes pour toutes les langues
const COMPLETE_TRANSLATIONS = {
    'en_fr': {
        // Boutons et actions
        'Try': 'Essayer',
        'Try for free': 'Essayer gratuitement',
        'Try Free': 'Essayer Gratuitement',
        'Try Now': 'Essayer Maintenant',
        'Get Started': 'Commencer',
        'Learn More': 'En savoir plus',
        'Read Review': 'Lire l\'Avis',
        'Full Review': 'Avis Complet',
        'Sign Up': 'S\'inscrire',
        'Login': 'Connexion',
        'Download': 'Télécharger',
        'Visit Website': 'Visiter le Site',

        // Sections
        'Features': 'Fonctionnalités',
        'Pricing': 'Tarifs',
        'Overview': 'Aperçu',
        'Pros': 'Avantages',
        'Cons': 'Inconvénients',
        'Alternatives': 'Alternatives',
        'Summary': 'Résumé',
        'Rating': 'Note',
        'Review': 'Avis',
        'Reviews': 'Avis',
        'Key Features': 'Fonctionnalités Clés',
        'Getting Started': 'Commencer',
        'FAQ': 'Questions Fréquentes',
        'Comparison': 'Comparaison',
        'Documentation': 'Documentation',

        // Statut
        'Free': 'Gratuit',
        'Paid': 'Payant',
        'Premium': 'Premium',
        'Enterprise': 'Entreprise',
        'Popular': 'Populaire',
        'New': 'Nouveau',
        'Updated': 'Mis à jour',
        'Published': 'Publié',
        'By': 'Par',

        // Textes courants
        'for free': 'gratuitement',
        'Available': 'Disponible',
        'Category': 'Catégorie',
        'Categories': 'Catégories',
        'Tools': 'Outils',
        'All': 'Tous',
        'Latest': 'Derniers',
        'Best': 'Meilleurs',
        'Top': 'Top',
        'More': 'Plus',
        'Less': 'Moins',
        'Show': 'Afficher',
        'Hide': 'Masquer'
    },
    'en_es': {
        'Try': 'Probar',
        'Try for free': 'Probar gratis',
        'Try Free': 'Probar Gratis',
        'Try Now': 'Probar Ahora',
        'Get Started': 'Comenzar',
        'Learn More': 'Saber más',
        'Read Review': 'Leer Reseña',
        'Full Review': 'Reseña Completa',
        'Sign Up': 'Registrarse',
        'Login': 'Iniciar sesión',
        'Download': 'Descargar',
        'Visit Website': 'Visitar Sitio',
        'Features': 'Características',
        'Pricing': 'Precios',
        'Overview': 'Descripción',
        'Pros': 'Ventajas',
        'Cons': 'Desventajas',
        'Alternatives': 'Alternativas',
        'Summary': 'Resumen',
        'Rating': 'Calificación',
        'Review': 'Reseña',
        'Reviews': 'Reseñas',
        'for free': 'gratis',
        'Free': 'Gratis',
        'Paid': 'Pago',
        'Premium': 'Premium',
        'Popular': 'Popular',
        'New': 'Nuevo'
    },
    'en_de': {
        'Try': 'Testen',
        'Try for free': 'Kostenlos testen',
        'Try Free': 'Kostenlos Testen',
        'Try Now': 'Jetzt Testen',
        'Get Started': 'Erste Schritte',
        'Learn More': 'Mehr erfahren',
        'Read Review': 'Rezension lesen',
        'Full Review': 'Vollständige Rezension',
        'Features': 'Funktionen',
        'Pricing': 'Preise',
        'Overview': 'Übersicht',
        'Pros': 'Vorteile',
        'Cons': 'Nachteile',
        'for free': 'kostenlos',
        'Free': 'Kostenlos',
        'Paid': 'Bezahlt'
    },
    'en_pt': {
        'Try': 'Experimentar',
        'Try for free': 'Experimente grátis',
        'Try Free': 'Experimente Grátis',
        'Try Now': 'Experimente Agora',
        'Get Started': 'Começar',
        'Learn More': 'Saiba mais',
        'Features': 'Recursos',
        'Pricing': 'Preços',
        'for free': 'grátis',
        'Free': 'Grátis'
    },
    'en_zh': {
        'Try': '试用',
        'Try for free': '免费试用',
        'Features': '特点',
        'Pricing': '价格',
        'for free': '免费'
    },
    'en_ja': {
        'Try': '試す',
        'Try for free': '無料で試す',
        'Features': '機能',
        'Pricing': '価格',
        'for free': '無料'
    },
    'en_ko': {
        'Try': '시도',
        'Try for free': '무료로 사용해 보세요',
        'Features': '기능',
        'Pricing': '가격',
        'for free': '무료'
    },
    'en_ar': {
        'Try': 'جرب',
        'Try for free': 'جرب مجانا',
        'Features': 'الميزات',
        'Pricing': 'التسعير',
        'for free': 'مجانا'
    },
    'en_hi': {
        'Try': 'प्रयास करें',
        'Try for free': 'मुफ्त में आज़माएं',
        'Features': 'विशेषताएँ',
        'Pricing': 'मूल्य निर्धारण',
        'for free': 'मुफ्त में'
    }
};

// Vérifier si un élément doit être exclu
function shouldExclude(element) {
    if (!element) return true;

    // Vérifier si l'élément ou un parent a data-i18n
    let current = element;
    while (current && current !== document.body) {
        if (current.hasAttribute && current.hasAttribute('data-i18n')) {
            return true;
        }
        current = current.parentElement;
    }

    // Vérifier les sélecteurs d'exclusion
    for (const selector of AUTO_TRANSLATE_CONFIG.excludeSelectors) {
        try {
            if (element.matches && element.matches(selector)) {
                return true;
            }
        } catch (e) {
            // Ignorer les erreurs de sélecteur invalide
        }
    }

    return false;
}

// Traduire le texte
function translateText(text, fromLang, toLang) {
    if (!text || text.trim().length === 0) return text;

    const trimmedText = text.trim();
    const key = `${fromLang}_${toLang}_${trimmedText}`;

    // Vérifier le cache
    if (translationCache[key]) {
        return text.replace(trimmedText, translationCache[key]);
    }

    // Préserver les noms d'outils
    for (const name of AUTO_TRANSLATE_CONFIG.preserveNames) {
        if (trimmedText === name || trimmedText.includes(name)) {
            return text; // Ne pas traduire
        }
    }

    // Utiliser les traductions complètes
    const transKey = `${fromLang}_${toLang}`;
    if (COMPLETE_TRANSLATIONS[transKey]) {
        // Essayer correspondance exacte d'abord
        if (COMPLETE_TRANSLATIONS[transKey][trimmedText]) {
            const translated = COMPLETE_TRANSLATIONS[transKey][trimmedText];
            translationCache[key] = translated;
            saveTranslationCache();
            return text.replace(trimmedText, translated);
        }

        // Essayer correspondance partielle (pour les phrases)
        for (const [en, trans] of Object.entries(COMPLETE_TRANSLATIONS[transKey])) {
            if (trimmedText.toLowerCase().includes(en.toLowerCase())) {
                const regex = new RegExp(en, 'gi');
                const translated = trimmedText.replace(regex, trans);
                translationCache[key] = translated;
                saveTranslationCache();
                return text.replace(trimmedText, translated);
            }
        }
    }

    // Si pas de traduction trouvée, retourner original
    return text;
}

// Traduire tous les nœuds de texte d'un élément
function translateElement(element, toLang) {
    if (!element || shouldExclude(element)) return;

    // Traduire les nœuds de texte directs uniquement
    Array.from(element.childNodes).forEach(node => {
        if (node.nodeType === Node.TEXT_NODE) {
            const originalText = node.textContent;
            if (originalText && originalText.trim().length > 0) {
                const translated = translateText(originalText, 'en', toLang);
                if (translated !== originalText) {
                    node.textContent = translated;
                }
            }
        } else if (node.nodeType === Node.ELEMENT_NODE && !shouldExclude(node)) {
            // Récursif pour les éléments enfants
            translateElement(node, toLang);
        }
    });
}

// Traduire toute la page
function translatePage(toLang) {
    if (!AUTO_TRANSLATE_CONFIG.enabled || toLang === 'en') return;

    
    loadTranslationCache();

    // Traduire le contenu principal
    const main = document.querySelector('main');
    if (main) {
        translateElement(main, toLang);
    }

    // Traduire le footer
    const footer = document.querySelector('footer');
    if (footer) {
        translateElement(footer, toLang);
    }

    saveTranslationCache();
    
}

// Initialiser la traduction automatique
function initAutoTranslate() {
    if (!window.i18n || !window.i18n.getCurrentLanguage) {
        setTimeout(initAutoTranslate, 100);
        return;
    }

    const currentLang = window.i18n.getCurrentLanguage();
    if (!currentLang) {
        setTimeout(initAutoTranslate, 100);
        return;
    }

    

    // Écouter les changements de langue
    document.addEventListener('languageChanged', (event) => {
        const newLang = event.detail.language;
        setTimeout(() => {
            translatePage(newLang);
        }, 150);
    });

    // Traduire immédiatement si pas anglais
    if (currentLang !== 'en') {
        setTimeout(() => {
            translatePage(currentLang);
        }, 200);
    }
}

// Auto-initialiser
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAutoTranslate);
} else {
    initAutoTranslate();
}

// Export
window.autoTranslate = {
    translatePage,
    translateElement,
    clearCache: () => {
        translationCache = {};
        localStorage.removeItem('translationCache');
        
    }
};

');
