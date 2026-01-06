/* ============================================
   TechVernia - Automatic Content Translation
   Translates ALL remaining content automatically
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
        'pre'                      // Code préformaté
    ],
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
            // Vérifier l'expiration
            if (data.timestamp && (Date.now() - data.timestamp) < AUTO_TRANSLATE_CONFIG.cacheExpiry) {
                translationCache = data.translations || {};
                console.log('📦 Cache de traduction chargé:', Object.keys(translationCache).length, 'entrées');
            }
        }
    } catch (e) {
        console.warn('Erreur chargement cache traduction:', e);
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
        console.warn('Erreur sauvegarde cache traduction:', e);
    }
}

// Traductions manuelles pour textes courts courants (plus rapide que l'API)
const COMMON_TRANSLATIONS = {
    // Anglais vers Français
    'en_fr': {
        'Features': 'Fonctionnalités',
        'Pricing': 'Tarifs',
        'Overview': 'Aperçu',
        'Pros': 'Avantages',
        'Cons': 'Inconvénients',
        'Alternatives': 'Alternatives',
        'Summary': 'Résumé',
        'Rating': 'Note',
        'Review': 'Avis',
        'Key Features': 'Fonctionnalités Clés',
        'Getting Started': 'Commencer',
        'FAQ': 'Questions Fréquentes',
        'Comparison': 'Comparaison',
        'Published': 'Publié',
        'Updated': 'Mis à jour',
        'By': 'Par',
        'Read more': 'Lire la suite',
        'Learn more': 'En savoir plus',
        'Get started': 'Commencer',
        'Sign up': 'S\'inscrire',
        'Login': 'Connexion',
        'Free': 'Gratuit',
        'Premium': 'Premium',
        'Enterprise': 'Entreprise',
        'Contact': 'Contact',
        'Support': 'Support',
        'Documentation': 'Documentation',
        'API': 'API',
        'Blog': 'Blog',
        'About': 'À propos',
        'Privacy': 'Confidentialité',
        'Terms': 'Conditions',
        'Cookie Policy': 'Politique de cookies'
    },
    // Anglais vers Espagnol
    'en_es': {
        'Features': 'Características',
        'Pricing': 'Precios',
        'Overview': 'Descripción',
        'Pros': 'Ventajas',
        'Cons': 'Desventajas',
        'Alternatives': 'Alternativas',
        'Summary': 'Resumen',
        'Rating': 'Calificación',
        'Review': 'Reseña',
        'Key Features': 'Características Clave',
        'Getting Started': 'Comenzar',
        'FAQ': 'Preguntas Frecuentes',
        'Comparison': 'Comparación',
        'Published': 'Publicado',
        'Updated': 'Actualizado',
        'By': 'Por',
        'Read more': 'Leer más',
        'Learn more': 'Saber más',
        'Get started': 'Comenzar',
        'Sign up': 'Registrarse',
        'Login': 'Iniciar sesión',
        'Free': 'Gratis',
        'Premium': 'Premium',
        'Enterprise': 'Empresa',
        'Contact': 'Contacto',
        'Support': 'Soporte',
        'Documentation': 'Documentación'
    },
    // Anglais vers Allemand
    'en_de': {
        'Features': 'Funktionen',
        'Pricing': 'Preise',
        'Overview': 'Übersicht',
        'Pros': 'Vorteile',
        'Cons': 'Nachteile',
        'Alternatives': 'Alternativen',
        'Summary': 'Zusammenfassung',
        'Rating': 'Bewertung',
        'Review': 'Rezension',
        'Key Features': 'Hauptmerkmale',
        'Getting Started': 'Erste Schritte',
        'FAQ': 'Häufig gestellte Fragen',
        'Comparison': 'Vergleich',
        'Published': 'Veröffentlicht',
        'Updated': 'Aktualisiert',
        'By': 'Von'
    }
};

// Vérifier si un élément doit être exclu
function shouldExclude(element) {
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
        if (element.matches && element.matches(selector)) {
            return true;
        }
    }

    return false;
}

// Obtenir la traduction depuis le cache ou les traductions communes
function getCachedTranslation(text, fromLang, toLang) {
    const key = `${fromLang}_${toLang}_${text}`;

    // Vérifier le cache
    if (translationCache[key]) {
        return translationCache[key];
    }

    // Vérifier les traductions communes
    const commonKey = `${fromLang}_${toLang}`;
    if (COMMON_TRANSLATIONS[commonKey] && COMMON_TRANSLATIONS[commonKey][text]) {
        const translation = COMMON_TRANSLATIONS[commonKey][text];
        translationCache[key] = translation;
        return translation;
    }

    return null;
}

// Traduire le texte via l'API Google Translate (client-side)
async function translateText(text, fromLang, toLang) {
    // Vérifier le cache d'abord
    const cached = getCachedTranslation(text, fromLang, toLang);
    if (cached) return cached;

    // Si pas dans le cache, utiliser une bibliothèque de traduction côté client
    // Pour l'instant, retourner le texte original (on peut implémenter une vraie API plus tard)
    const key = `${fromLang}_${toLang}_${text}`;

    // Utiliser les traductions communes si possible
    const commonKey = `${fromLang}_${toLang}`;
    if (COMMON_TRANSLATIONS[commonKey]) {
        for (const [en, trans] of Object.entries(COMMON_TRANSLATIONS[commonKey])) {
            if (text.includes(en)) {
                const translated = text.replace(new RegExp(en, 'g'), trans);
                translationCache[key] = translated;
                saveTranslationCache();
                return translated;
            }
        }
    }

    // Sauvegarder pour ne pas re-traduire
    translationCache[key] = text;
    return text;
}

// Traduire tous les nœuds de texte d'un élément
async function translateElement(element, toLang) {
    if (!element || shouldExclude(element)) return;

    // Traduire les nœuds de texte directs
    const walker = document.createTreeWalker(
        element,
        NodeFilter.SHOW_TEXT,
        {
            acceptNode: (node) => {
                // Ignorer les espaces vides
                if (!node.textContent.trim()) return NodeFilter.FILTER_REJECT;

                // Vérifier si le parent doit être exclu
                if (shouldExclude(node.parentElement)) return NodeFilter.FILTER_REJECT;

                return NodeFilter.FILTER_ACCEPT;
            }
        }
    );

    const textNodes = [];
    let node;
    while (node = walker.nextNode()) {
        textNodes.push(node);
    }

    // Traduire chaque nœud de texte
    for (const textNode of textNodes) {
        const originalText = textNode.textContent.trim();
        if (originalText) {
            const translated = await translateText(originalText, 'en', toLang);
            if (translated !== originalText) {
                textNode.textContent = textNode.textContent.replace(originalText, translated);
            }
        }
    }
}

// Traduire toute la page
async function translatePage(toLang) {
    if (!AUTO_TRANSLATE_CONFIG.enabled || toLang === 'en') return;

    console.log(`🌍 Traduction automatique vers: ${toLang}`);

    // Charger le cache
    loadTranslationCache();

    // Sélectionner les zones principales à traduire
    const mainContent = document.querySelector('main') || document.body;

    // Traduire le contenu principal
    await translateElement(mainContent, toLang);

    // Traduire aussi le footer si présent
    const footer = document.querySelector('footer');
    if (footer) {
        await translateElement(footer, toLang);
    }

    // Sauvegarder le cache
    saveTranslationCache();

    console.log('✅ Traduction automatique terminée');
}

// Initialiser la traduction automatique
function initAutoTranslate() {
    // Attendre que i18n soit chargé ET initialisé
    if (!window.i18n || !window.i18n.getCurrentLanguage) {
        setTimeout(initAutoTranslate, 100);
        return;
    }

    const currentLang = window.i18n.getCurrentLanguage();

    // Si getCurrentLanguage() retourne undefined, réessayer
    if (!currentLang) {
        setTimeout(initAutoTranslate, 100);
        return;
    }

    console.log(`🔧 Auto-translate initialisé avec langue: ${currentLang}`);

    // Écouter les changements de langue
    window.addEventListener('languageChanged', (event) => {
        const newLang = event.detail.language;

        // Attendre que i18n.js ait fini sa traduction
        setTimeout(() => {
            translatePage(newLang);
        }, 100);
    });

    // Traduire immédiatement si la langue n'est pas l'anglais
    if (currentLang !== 'en') {
        setTimeout(() => {
            translatePage(currentLang);
        }, 200);
    }
}

// Auto-initialiser quand le DOM est prêt
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAutoTranslate);
} else {
    initAutoTranslate();
}

// Export pour utilisation externe
window.autoTranslate = {
    translatePage,
    translateElement,
    getCachedTranslation,
    clearCache: () => {
        translationCache = {};
        localStorage.removeItem('translationCache');
        console.log('🗑️ Cache de traduction vidé');
    }
};

console.log('✅ Système de traduction automatique chargé');
