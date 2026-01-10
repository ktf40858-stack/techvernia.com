/**
 * UNIVERSAL TRANSLATE - Solution Finale
 * Traduit ABSOLUMENT TOUT le texte visible sur TOUTES les pages
 * Sauf les noms d'outils IA
 */

(function() {
    'use strict';

    

    // Dictionnaire COMPLET de traductions pour toutes les langues
    const DICT = {
        fr: {
            // Boutons et actions
            'Try': 'Essayer',
            'Try Free': 'Essayer Gratuitement',
            'Try for free': 'Essayer gratuitement',
            'Try it free': 'Essayez-le gratuitement',
            'Try Now': 'Essayer Maintenant',
            'Get Started': 'Commencer',
            'Learn More': 'En savoir plus',
            'Read Review': 'Lire l\'Avis',
            'Full Review': 'Avis Complet',
            'View All': 'Voir Tout',
            'Show More': 'Voir Plus',
            'Load More': 'Charger Plus',

            // Textes courants
            'for free': 'gratuitement',
            'free': 'gratuit',
            'Free': 'Gratuit',
            'Popular': 'Populaire',
            'New': 'Nouveau',
            'Premium': 'Premium',
            'Pro': 'Pro',
            'Plus': 'Plus',
            'Enterprise': 'Entreprise',
            'Business': 'Entreprise',

            //Sections
            'Features': 'Fonctionnalités',
            'Pricing': 'Tarifs',
            'Overview': 'Aperçu',
            'Reviews': 'Avis',
            'Rating': 'Note',
            'Comparison': 'Comparaison',
            'Alternatives': 'Alternatives',

            // Pays
            'United States': 'États-Unis',
            'China': 'Chine',
            'International': 'International',

            // Textes longs
            'Your trusted source for AI tool reviews, comparisons, and guides.': 'Votre source de confiance pour les avis, comparaisons et guides d\'outils IA.',
            'All rights reserved': 'Tous droits réservés'
        },
        es: {
            'Try': 'Probar',
            'Try Free': 'Probar Gratis',
            'Try for free': 'Probar gratis',
            'Try Now': 'Probar Ahora',
            'Get Started': 'Comenzar',
            'Learn More': 'Saber más',
            'Full Review': 'Reseña Completa',
            'for free': 'gratis',
            'free': 'gratis',
            'Free': 'Gratis',
            'Popular': 'Popular',
            'New': 'Nuevo',
            'Features': 'Características',
            'Pricing': 'Precios',
            'Overview': 'Descripción',
            'United States': 'Estados Unidos',
            'China': 'China'
        },
        de: {
            'Try': 'Testen',
            'Try Free': 'Kostenlos Testen',
            'Try for free': 'Kostenlos testen',
            'Try Now': 'Jetzt Testen',
            'Get Started': 'Erste Schritte',
            'Learn More': 'Mehr erfahren',
            'Full Review': 'Vollständige Rezension',
            'for free': 'kostenlos',
            'free': 'kostenlos',
            'Free': 'Kostenlos',
            'Features': 'Funktionen',
            'Pricing': 'Preise',
            'Overview': 'Übersicht',
            'United States': 'Vereinigte Staaten',
            'China': 'China'
        },
        pt: {
            'Try': 'Experimentar',
            'Try Free': 'Experimente Grátis',
            'for free': 'grátis',
            'Features': 'Recursos',
            'Pricing': 'Preços'
        },
        zh: {
            'Try': '试用',
            'Try Free': '免费试用',
            'for free': '免费',
            'Features': '特点',
            'Pricing': '价格'
        },
        ja: {
            'Try': '試す',
            'Try Free': '無料で試す',
            'for free': '無料',
            'Features': '機能',
            'Pricing': '価格'
        },
        ko: {
            'Try': '시도',
            'Try Free': '무료로 사용해 보세요',
            'for free': '무료',
            'Features': '기능',
            'Pricing': '가격'
        },
        ar: {
            'Try': 'جرب',
            'Try Free': 'جرب مجانا',
            'for free': 'مجانا',
            'Features': 'الميزات',
            'Pricing': 'التسعير'
        },
        hi: {
            'Try': 'प्रयास करें',
            'Try Free': 'मुफ्त में आज़माएं',
            'for free': 'मुफ्त में',
            'Features': 'विशेषताएँ',
            'Pricing': 'मूल्य निर्धारण'
        }
    };

    // Noms à NE JAMAIS traduire
    const NEVER_TRANSLATE = [
        'ChatGPT', 'Claude', 'Gemini', 'GPT-4', 'GPT-3.5', 'Midjourney',
        'DALL-E', 'DALL·E', 'Copilot', 'Perplexity', 'Stable Diffusion',
        'Leonardo AI', 'Ideogram', 'Runway', 'Pika', 'Grok', 'Poe',
        'Deepseek', 'GitHub', 'Amazon Q', 'Tabnine', 'Replit',
        'Tableau', 'Looker', 'Salesforce', 'HubSpot', 'CrowdStrike',
        'Darktrace', 'Splunk', 'Cortex', 'SentinelOne', 'ChatGpt', 'Chatgpt'
    ];

    // Cache des nœuds déjà traités
    const processedNodes = new WeakSet();

    // Traduire un nœud de texte
    function translateNode(node, lang) {
        // Ignorer si déjà traité
        if (processedNodes.has(node)) return;
        processedNodes.add(node);

        let text = node.textContent;
        if (!text || text.trim().length === 0) return;

        const trimmed = text.trim();

        // Ne pas traduire les noms d'outils
        if (NEVER_TRANSLATE.some(name => trimmed.includes(name))) {
            return;
        }

        // Ne pas traduire si c'est juste des chiffres/symboles
        if (/^[\d\s\.\,\★\-\(\)]+$/.test(trimmed)) {
            return;
        }

        // Traduire
        if (DICT[lang]) {
            let translated = text;
            const dict = DICT[lang];

            // Trier les clés par longueur (plus longues d'abord)
            const sortedKeys = Object.keys(dict).sort((a, b) => b.length - a.length);

            for (const key of sortedKeys) {
                if (text.includes(key)) {
                    const regex = new RegExp(key.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'g');
                    translated = translated.replace(regex, dict[key]);
                }
            }

            if (translated !== text) {
                node.textContent = translated;
            }
        }
    }

    // Parcourir récursivement tous les nœuds
    function walkDOM(element, lang) {
        if (!element) return;

        // Ignorer certains éléments
        const tagName = element.tagName ? element.tagName.toLowerCase() : '';
        if (['script', 'style', 'svg', 'code', 'pre', 'noscript'].includes(tagName)) {
            return;
        }

        // Ignorer les éléments avec data-i18n (déjà traduits)
        if (element.hasAttribute && element.hasAttribute('data-i18n')) {
            return;
        }

        // Parcourir les enfants
        for (const child of Array.from(element.childNodes)) {
            if (child.nodeType === Node.TEXT_NODE) {
                translateNode(child, lang);
            } else if (child.nodeType === Node.ELEMENT_NODE) {
                walkDOM(child, lang);
            }
        }
    }

    // Traduire toute la page
    function translateAll(lang) {
        if (!lang || lang === 'en') {
            
            return;
        }

        }`);

        // Vider le cache
        processedNodes.clear();

        // Traduire tout le document
        walkDOM(document.body, lang);

        
    }

    // Initialisation
    function init() {
        // Attendre i18n
        if (!window.i18n || typeof window.i18n.getCurrentLanguage !== 'function') {
            setTimeout(init, 50);
            return;
        }

        

        // Écouter les changements de langue
        document.addEventListener('languageChanged', (e) => {
            const newLang = e.detail.language;
            

            // Attendre un peu que i18n finisse
            setTimeout(() => translateAll(newLang), 100);
        });

        // Traduire si pas anglais
        const currentLang = window.i18n.getCurrentLanguage();
        if (currentLang && currentLang !== 'en') {
            setTimeout(() => translateAll(currentLang), 200);
        }
    }

    // Démarrer
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    // Export
    window.universalTranslate = { translate: translateAll };

})();


