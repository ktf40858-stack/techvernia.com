/**
 * SIMPLE TRANSLATE - Version Ultra Basique
 * Traduit le texte visible en utilisant des remplacements simples
 */



// Dictionnaire de traductions
const TRANSLATIONS = {
    fr: {
        'Try Free': 'Essayer Gratuitement',
        'Try for free': 'Essayer gratuitement',
        'Try': 'Essayer',
        'Try Now': 'Essayer Maintenant',
        'Get Started': 'Commencer',
        'Learn More': 'En savoir plus',
        'Full Review': 'Avis Complet',
        'Features': 'Fonctionnalités',
        'Pricing': 'Tarifs',
        'Overview': 'Aperçu',
        'Popular': 'Populaire',
        'New': 'Nouveau',
        'Free': 'Gratuit',
        'for free': 'gratuitement',
        'United States': 'États-Unis',
        'China': 'Chine',
        'International': 'International',
        'Your trusted source for AI tool reviews, comparisons, and guides.': 'Votre source de confiance pour les avis, comparaisons et guides d\'outils IA.',
        'All rights reserved': 'Tous droits réservés'
    },
    es: {
        'Try Free': 'Probar Gratis',
        'Try for free': 'Probar gratis',
        'Try': 'Probar',
        'Features': 'Características',
        'Pricing': 'Precios',
        'for free': 'gratis',
        'Free': 'Gratis'
    },
    de: {
        'Try Free': 'Kostenlos Testen',
        'Try for free': 'Kostenlos testen',
        'Try': 'Testen',
        'Features': 'Funktionen',
        'Pricing': 'Preise',
        'for free': 'kostenlos'
    }
};

// Noms à ne jamais traduire
const PRESERVE = ['ChatGPT', 'Claude', 'Gemini', 'GPT-4', 'Copilot', 'Perplexity', 'Midjourney', 'DALL-E'];

// Fonction de traduction SIMPLE
function simpleTranslate(lang) {
    

    if (!lang || lang === 'en') {
        
        return;
    }

    if (!TRANSLATIONS[lang]) {
        
        return;
    }

    const dict = TRANSLATIONS[lang];
    let count = 0;

    // Parcourir TOUS les éléments de texte
    const allElements = document.querySelectorAll('*');

    allElements.forEach(element => {
        // Ignorer certains éléments
        const tag = element.tagName.toLowerCase();
        if (['script', 'style', 'svg', 'code', 'pre'].includes(tag)) {
            return;
        }

        // Ignorer si a déjà data-i18n
        if (element.hasAttribute('data-i18n')) {
            return;
        }

        // Parcourir les nœuds enfants directs
        element.childNodes.forEach(node => {
            if (node.nodeType === 3) { // Text node
                let text = node.textContent;
                let originalText = text;

                // Ne pas traduire si contient un nom préservé
                let shouldSkip = false;
                for (let name of PRESERVE) {
                    if (text.includes(name)) {
                        shouldSkip = true;
                        break;
                    }
                }

                if (shouldSkip) return;

                // Appliquer toutes les traductions
                for (let [en, trans] of Object.entries(dict)) {
                    if (text.includes(en)) {
                        text = text.replace(new RegExp(en, 'g'), trans);
                    }
                }

                // Mettre à jour si changé
                if (text !== originalText) {
                    node.textContent = text;
                    count++;
                    + '" → "' + text.trim() + '"');
                }
            }
        });
    });

    
}

// Initialisation
function initSimpleTranslate() {
    

    // Attendre i18n
    if (!window.i18n || !window.i18n.getCurrentLanguage) {
        
        setTimeout(initSimpleTranslate, 100);
        return;
    }

    

    // Écouter les changements de langue
    document.addEventListener('languageChanged', function(event) {
        const newLang = event.detail.language;
        
        setTimeout(function() {
            simpleTranslate(newLang);
        }, 150);
    });

    // Traduire si pas anglais au démarrage
    const currentLang = window.i18n.getCurrentLanguage();
    if (currentLang && currentLang !== 'en') {
        
        setTimeout(function() {
            simpleTranslate(currentLang);
        }, 300);
    }

    
}

// Démarrer
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initSimpleTranslate);
} else {
    initSimpleTranslate();
}

// Export global
window.simpleTranslate = simpleTranslate;


