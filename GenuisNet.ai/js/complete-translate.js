/**
 * COMPLETE TRANSLATE - Traduction TOTALE du site
 * Traduit ABSOLUMENT TOUT sauf les noms d'outils IA
 */

console.log('🌍 COMPLETE TRANSLATE - Chargement...');

// DICTIONNAIRE MASSIF - Français
const FR = {
    // Page d'accueil - Hero
    'Discover the Best AI Tools': 'Découvrez les Meilleurs Outils IA',
    'Your Ultimate Guide to AI Tools': 'Votre Guide Ultime des Outils IA',
    'Expert reviews and guides for': 'Avis d\'experts et guides pour',
    'AI tools': 'outils IA',
    'From': 'De',
    'to enterprise solutions': 'aux solutions d\'entreprise',
    'Explore Tools': 'Explorer les Outils',
    'View Categories': 'Voir les Catégories',

    // Sections principales
    'Categories': 'Catégories',
    'Featured Tools': 'Outils en Vedette',
    'Latest Reviews': 'Derniers Avis',
    'Popular Categories': 'Catégories Populaires',
    'Trending Now': 'Tendances Actuelles',
    'New Arrivals': 'Nouveautés',
    'Editor\'s Choice': 'Choix de l\'Éditeur',

    // Catégories
    'AI Chatbots & Assistants': 'Chatbots et Assistants IA',
    'AI Writing Tools': 'Outils d\'Écriture IA',
    'AI Image Generation': 'Génération d\'Images IA',
    'AI Video Tools': 'Outils Vidéo IA',
    'AI Audio & Music': 'Audio et Musique IA',
    'AI Coding Tools': 'Outils de Codage IA',
    'AI Productivity': 'Productivité IA',
    'AI for SEO': 'IA pour le SEO',
    'AI for Business': 'IA pour les Entreprises',
    'AI for Networking': 'IA pour le Réseautage',
    'AI for Cybersecurity': 'IA pour la Cybersécurité',
    'AI for Architecture': 'IA pour l\'Architecture',
    'AI for Medical': 'IA pour la Médecine',
    'AI for Analytics': 'IA pour l\'Analytique',

    // Descriptions
    'Discover the most powerful AI chatbots and virtual assistants': 'Découvrez les chatbots IA et assistants virtuels les plus puissants',
    'From general-purpose tools like': 'Des outils polyvalents comme',
    'to specialized assistants': 'aux assistants spécialisés',
    'find the perfect AI companion for your needs': 'trouvez le compagnon IA parfait pour vos besoins',
    'Professional writing assistants': 'Assistants d\'écriture professionnels',
    'Create stunning AI-generated images': 'Créez des images époustouflantes générées par IA',
    'Advanced video creation and editing': 'Création et montage vidéo avancés',
    'AI-powered development tools': 'Outils de développement alimentés par IA',

    // Boutons et actions
    'Try': 'Essayer',
    'Try Free': 'Essayer Gratuitement',
    'Try for free': 'Essayer gratuitement',
    'Try it free': 'Essayez-le gratuitement',
    'Try Now': 'Essayer Maintenant',
    'Get Started': 'Commencer',
    'Get Started Free': 'Commencer Gratuitement',
    'Start Free': 'Démarrer Gratuitement',
    'Learn More': 'En savoir plus',
    'Read Review': 'Lire l\'Avis',
    'Full Review': 'Avis Complet',
    'View All': 'Voir Tout',
    'View All Tools': 'Voir Tous les Outils',
    'Show More': 'Voir Plus',
    'Show Less': 'Voir Moins',
    'Load More': 'Charger Plus',
    'Explore': 'Explorer',
    'Discover': 'Découvrir',
    'Compare': 'Comparer',
    'Sign Up': 'S\'inscrire',
    'Sign In': 'Se Connecter',
    'Login': 'Connexion',
    'Register': 'S\'inscrire',
    'Download': 'Télécharger',
    'Visit Website': 'Visiter le Site',
    'Official Website': 'Site Officiel',
    'Go to': 'Aller à',

    // Statut et badges
    'for free': 'gratuitement',
    'free': 'gratuit',
    'Free': 'Gratuit',
    'Free Plan': 'Plan Gratuit',
    'Free Trial': 'Essai Gratuit',
    'Popular': 'Populaire',
    'New': 'Nouveau',
    'Updated': 'Mis à jour',
    'Premium': 'Premium',
    'Pro': 'Pro',
    'Plus': 'Plus',
    'Enterprise': 'Entreprise',
    'Business': 'Entreprise',
    'Starter': 'Débutant',
    'Basic': 'Basique',
    'Advanced': 'Avancé',
    'Professional': 'Professionnel',
    'Verified': 'Vérifié',
    'Recommended': 'Recommandé',
    'Featured': 'En Vedette',
    'Trending': 'Tendance',
    'Hot': 'Populaire',
    'Best': 'Meilleur',
    'Top Rated': 'Mieux Noté',

    // Sections et titres
    'Features': 'Fonctionnalités',
    'Key Features': 'Fonctionnalités Clés',
    'Main Features': 'Fonctionnalités Principales',
    'Pricing': 'Tarifs',
    'Plans': 'Plans',
    'Pricing Plans': 'Plans Tarifaires',
    'Overview': 'Aperçu',
    'Description': 'Description',
    'About': 'À propos',
    'Pros': 'Avantages',
    'Cons': 'Inconvénients',
    'Advantages': 'Avantages',
    'Disadvantages': 'Inconvénients',
    'Alternatives': 'Alternatives',
    'Similar Tools': 'Outils Similaires',
    'Summary': 'Résumé',
    'Rating': 'Note',
    'Ratings': 'Notes',
    'Review': 'Avis',
    'Reviews': 'Avis',
    'User Reviews': 'Avis des Utilisateurs',
    'Comparison': 'Comparaison',
    'Getting Started': 'Commencer',
    'How to Use': 'Comment Utiliser',
    'Tutorial': 'Tutoriel',
    'Guide': 'Guide',
    'Guides': 'Guides',
    'FAQ': 'Questions Fréquentes',
    'Help': 'Aide',
    'Support': 'Support',
    'Documentation': 'Documentation',
    'Docs': 'Docs',
    'API': 'API',
    'Blog': 'Blog',
    'News': 'Actualités',
    'Updates': 'Mises à jour',
    'Changelog': 'Journal des modifications',

    // Stats et métriques
    'Tools': 'Outils',
    'Tools Reviewed': 'Outils Analysés',
    'AI Tools': 'Outils IA',
    'Avg Rating': 'Note Moyenne',
    'Average Rating': 'Note Moyenne',
    'Users': 'Utilisateurs',
    'Active Users': 'Utilisateurs Actifs',
    'Downloads': 'Téléchargements',
    'Views': 'Vues',
    'Likes': 'J\'aime',
    'Shares': 'Partages',
    'Comments': 'Commentaires',

    // Pays et régions
    'United States': 'États-Unis',
    'China': 'Chine',
    'International': 'International',
    'Global': 'Mondial',
    'Worldwide': 'Mondial',
    'Europe': 'Europe',
    'Asia': 'Asie',
    'America': 'Amérique',

    // Temps et dates
    'Published': 'Publié',
    'Last Updated': 'Dernière Mise à jour',
    'By': 'Par',
    'on': 'le',
    'ago': 'il y a',
    'minute': 'minute',
    'minutes': 'minutes',
    'hour': 'heure',
    'hours': 'heures',
    'day': 'jour',
    'days': 'jours',
    'week': 'semaine',
    'weeks': 'semaines',
    'month': 'mois',
    'months': 'mois',
    'year': 'an',
    'years': 'ans',

    // Prix
    'month': 'mois',
    'per month': 'par mois',
    '/month': '/mois',
    'year': 'an',
    'per year': 'par an',
    '/year': '/an',
    'one-time': 'paiement unique',
    'Starting at': 'À partir de',
    'From': 'Dès',

    // Navigation
    'Home': 'Accueil',
    'Back': 'Retour',
    'Next': 'Suivant',
    'Previous': 'Précédent',
    'Close': 'Fermer',
    'Open': 'Ouvrir',
    'Menu': 'Menu',
    'Search': 'Rechercher',
    'Filter': 'Filtrer',
    'Sort': 'Trier',
    'All': 'Tous',
    'Latest': 'Derniers',
    'Oldest': 'Plus anciens',

    // Footer
    'Resources': 'Ressources',
    'Company': 'Entreprise',
    'Legal': 'Légal',
    'Contact': 'Contact',
    'Contact Us': 'Nous Contacter',
    'About Us': 'À propos de nous',
    'Terms': 'Conditions',
    'Terms of Service': 'Conditions d\'utilisation',
    'Privacy': 'Confidentialité',
    'Privacy Policy': 'Politique de confidentialité',
    'Cookie Policy': 'Politique de cookies',
    'All rights reserved': 'Tous droits réservés',
    'Your trusted source for AI tool reviews, comparisons, and guides.': 'Votre source de confiance pour les avis, comparaisons et guides d\'outils IA.',

    // Messages communs
    'Loading': 'Chargement',
    'Loading...': 'Chargement...',
    'Please wait': 'Veuillez patienter',
    'Error': 'Erreur',
    'Success': 'Succès',
    'Warning': 'Attention',
    'Info': 'Information',
    'Coming Soon': 'Bientôt disponible',
    'Under Construction': 'En construction',
    'No results found': 'Aucun résultat trouvé',
    'Try again': 'Réessayer',
    'Refresh': 'Actualiser',
    'Share': 'Partager',
    'Copy': 'Copier',
    'Copied': 'Copié',
    'Save': 'Enregistrer',
    'Saved': 'Enregistré',
    'Delete': 'Supprimer',
    'Edit': 'Modifier',
    'Cancel': 'Annuler',
    'Confirm': 'Confirmer',
    'Yes': 'Oui',
    'No': 'Non',
    'OK': 'OK',
    'Got it': 'Compris',
    'Understand': 'Compris',

    // Mots courts/fréquents
    'and': 'et',
    'or': 'ou',
    'with': 'avec',
    'without': 'sans',
    'more': 'plus',
    'less': 'moins',
    'other': 'autre',
    'others': 'autres',
    'see': 'voir',
    'view': 'voir'
};

// Autres langues (Espagnol, Allemand, etc.) - versions simplifiées
const ES = {
    'Try Free': 'Probar Gratis',
    'Try for free': 'Probar gratis',
    'Get Started': 'Comenzar',
    'Learn More': 'Saber más',
    'Features': 'Características',
    'Pricing': 'Precios',
    'for free': 'gratis',
    'Free': 'Gratis',
    'Categories': 'Categorías',
    'Tools': 'Herramientas',
    'United States': 'Estados Unidos',
    'China': 'China'
};

const DE = {
    'Try Free': 'Kostenlos Testen',
    'Try for free': 'Kostenlos testen',
    'Get Started': 'Erste Schritte',
    'Learn More': 'Mehr erfahren',
    'Features': 'Funktionen',
    'Pricing': 'Preise',
    'for free': 'kostenlos',
    'Free': 'Kostenlos',
    'Categories': 'Kategorien',
    'Tools': 'Werkzeuge',
    'United States': 'Vereinigte Staaten'
};

// Dictionnaire complet
const DICT = { fr: FR, es: ES, de: DE };

// Noms à JAMAIS traduire
const NEVER = [
    'ChatGPT', 'Claude', 'Gemini', 'GPT-4', 'GPT-3.5', 'Midjourney',
    'DALL-E', 'DALL·E', 'Copilot', 'Perplexity', 'Stable Diffusion',
    'Leonardo AI', 'Ideogram', 'Runway', 'Pika', 'Grok', 'Poe',
    'Deepseek', 'GitHub', 'Amazon Q', 'Tabnine', 'Replit',
    'Tableau', 'Looker', 'Salesforce', 'HubSpot', 'CrowdStrike',
    'Darktrace', 'Splunk', 'Cortex', 'SentinelOne', 'Chatgpt',
    'GenuisNet', 'GenuisNet.ai'
];

// Traduire tout
function translateAll(lang) {
    console.log('🌍 COMPLETE TRANSLATE → ' + lang.toUpperCase());

    if (!lang || lang === 'en' || !DICT[lang]) {
        console.log('⏭️  Pas de traduction nécessaire');
        return;
    }

    const dict = DICT[lang];
    const sortedKeys = Object.keys(dict).sort((a, b) => b.length - a.length);
    let count = 0;

    // Parcourir TOUS les éléments
    document.querySelectorAll('*').forEach(el => {
        const tag = el.tagName.toLowerCase();

        // Ignorer certains tags
        if (['script', 'style', 'svg', 'code', 'pre', 'noscript'].includes(tag)) return;

        // Ignorer si a data-i18n
        if (el.hasAttribute('data-i18n')) return;

        // Traduire les nœuds de texte directs
        Array.from(el.childNodes).forEach(node => {
            if (node.nodeType !== 3) return; // Seulement text nodes

            let text = node.textContent;
            if (!text || text.trim().length === 0) return;

            // Ne pas traduire les noms préservés
            if (NEVER.some(name => text.includes(name))) return;

            let translated = text;

            // Appliquer traductions (plus longues en premier)
            for (const key of sortedKeys) {
                if (translated.includes(key)) {
                    const escaped = key.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
                    const regex = new RegExp(escaped, 'g');
                    translated = translated.replace(regex, dict[key]);
                }
            }

            if (translated !== text) {
                node.textContent = translated;
                count++;
            }
        });
    });

    console.log('✅ COMPLETE TRANSLATE: ' + count + ' éléments traduits');
}

// Init
function init() {
    if (!window.i18n || !window.i18n.getCurrentLanguage) {
        setTimeout(init, 50);
        return;
    }

    console.log('✅ COMPLETE TRANSLATE: Prêt');

    window.addEventListener('languageChanged', (e) => {
        console.log('📡 Langue changée → ' + e.detail.language);
        setTimeout(() => translateAll(e.detail.language), 150);
    });

    const lang = window.i18n.getCurrentLanguage();
    if (lang && lang !== 'en') {
        setTimeout(() => translateAll(lang), 300);
    }
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
} else {
    init();
}

window.completeTranslate = translateAll;
console.log('✅ COMPLETE TRANSLATE: Chargé');
