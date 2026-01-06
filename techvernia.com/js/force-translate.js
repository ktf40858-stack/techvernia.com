/**
 * FORCE TRANSLATE - Solution Ultra Simple
 * Traduit TOUT le texte visible sur la page
 */

(function() {
    'use strict';

    console.log('🚀 Force Translate chargé');

    // Dictionnaire de traductions COMPLET
    const TRANSLATIONS = {
        fr: {
            // Exact matches (case-sensitive)
            'Try': 'Essayer',
            'Try Free': 'Essayer Gratuitement',
            'Try for free': 'Essayer gratuitement',
            'Try Now': 'Essayer Maintenant',
            'Get Started': 'Commencer',
            'Learn More': 'En savoir plus',
            'Read Review': 'Lire l\'Avis',
            'Full Review': 'Avis Complet',
            'Features': 'Fonctionnalités',
            'Pricing': 'Tarifs',
            'Overview': 'Aperçu',
            'Popular': 'Populaire',
            'New': 'Nouveau',
            'Free': 'Gratuit',
            'Premium': 'Premium',
            'Rating': 'Note',
            'Review': 'Avis',
            'Reviews': 'Avis',

            // Partial matches (case-insensitive)
            'for free': 'gratuitement',
            'free': 'gratuit'
        },
        es: {
            'Try': 'Probar',
            'Try Free': 'Probar Gratis',
            'Try for free': 'Probar gratis',
            'Features': 'Características',
            'Pricing': 'Precios',
            'for free': 'gratis'
        },
        de: {
            'Try': 'Testen',
            'Try Free': 'Kostenlos Testen',
            'Try for free': 'Kostenlos testen',
            'Features': 'Funktionen',
            'Pricing': 'Preise',
            'for free': 'kostenlos'
        }
    };

    // Noms à ne JAMAIS traduire
    const PRESERVE = ['ChatGPT', 'Claude', 'Gemini', 'GPT-4', 'Midjourney', 'DALL-E', 'Copilot', 'Perplexity'];

    // Traduire un nœud de texte
    function translateTextNode(node, lang) {
        if (!node || !node.textContent) return;

        let text = node.textContent;
        const originalText = text;

        // Ne pas traduire si c'est un nom préservé
        for (const name of PRESERVE) {
            if (text.trim() === name) return;
        }

        // Ne pas traduire si vide ou juste des espaces/nombres
        if (text.trim().length === 0 || /^\d+$/.test(text.trim())) return;

        // Appliquer les traductions
        if (TRANSLATIONS[lang]) {
            const dict = TRANSLATIONS[lang];

            // Essayer correspondance exacte
            const trimmed = text.trim();
            if (dict[trimmed]) {
                text = text.replace(trimmed, dict[trimmed]);
            } else {
                // Essayer correspondance partielle
                for (const [en, trans] of Object.entries(dict)) {
                    if (text.includes(en)) {
                        const regex = new RegExp(en, 'gi');
                        text = text.replace(regex, trans);
                    }
                }
            }
        }

        // Appliquer si changé
        if (text !== originalText) {
            node.textContent = text;
            console.log(`Traduit: "${originalText.trim()}" -> "${text.trim()}"`);
        }
    }

    // Parcourir tous les nœuds de texte
    function translateAllText(lang) {
        console.log(`🌍 Force translation vers: ${lang}`);
        let count = 0;

        // Fonction récursive pour parcourir l'arbre DOM
        function walkNode(node) {
            // Ignorer les éléments exclus
            if (node.nodeType === Node.ELEMENT_NODE) {
                const tagName = node.tagName ? node.tagName.toLowerCase() : '';

                // Ignorer certains éléments
                if (['script', 'style', 'svg', 'code', 'pre'].includes(tagName)) {
                    return;
                }

                // Ignorer les éléments avec data-i18n (déjà traduits)
                if (node.hasAttribute && node.hasAttribute('data-i18n')) {
                    return;
                }
            }

            // Si c'est un nœud de texte, le traduire
            if (node.nodeType === Node.TEXT_NODE) {
                translateTextNode(node, lang);
                count++;
            }

            // Parcourir les enfants
            if (node.childNodes) {
                node.childNodes.forEach(child => walkNode(child));
            }
        }

        // Traduire le main
        const main = document.querySelector('main');
        if (main) {
            walkNode(main);
        }

        // Traduire le footer
        const footer = document.querySelector('footer');
        if (footer) {
            walkNode(footer);
        }

        console.log(`✅ Force translation terminée (${count} nœuds parcourus)`);
    }

    // Écouter les changements de langue
    function init() {
        // Attendre i18n
        if (!window.i18n || !window.i18n.getCurrentLanguage) {
            setTimeout(init, 100);
            return;
        }

        console.log('🔧 Force Translate initialisé');

        // Écouter l'événement de changement de langue
        document.addEventListener('languageChanged', (event) => {
            const newLang = event.detail.language;
            console.log(`📡 Changement de langue détecté: ${newLang}`);

            // Attendre que i18n ait fini
            setTimeout(() => {
                if (newLang !== 'en') {
                    translateAllText(newLang);
                }
            }, 200);
        });

        // Traduire immédiatement si pas anglais
        const currentLang = window.i18n.getCurrentLanguage();
        if (currentLang && currentLang !== 'en') {
            setTimeout(() => {
                translateAllText(currentLang);
            }, 300);
        }
    }

    // Lancer l'initialisation
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    // Export pour test manuel
    window.forceTranslate = {
        translate: translateAllText
    };

})();
