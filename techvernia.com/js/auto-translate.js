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

    // Ratings & Labels
    'Coding': 'Codage',
    'Reasoning': 'Raisonnement',
    'Context': 'Contexte',
    'Value': 'Valeur',
    'Get': 'Obtenir',

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
    // Page d'accueil - Hero
    'Discover the Best AI Tools': 'Descubre las Mejores Herramientas IA',
    'Your Ultimate Guide to AI Tools': 'Tu Guía Definitiva de Herramientas IA',
    'Expert reviews and guides for': 'Reseñas expertas y guías para',
    'AI tools': 'herramientas IA',
    'From': 'Desde',
    'to enterprise solutions': 'hasta soluciones empresariales',
    'Explore Tools': 'Explorar Herramientas',
    'View Categories': 'Ver Categorías',

    // Sections principales
    'Categories': 'Categorías',
    'Featured Tools': 'Herramientas Destacadas',
    'Latest Reviews': 'Últimas Reseñas',
    'Popular Categories': 'Categorías Populares',
    'Trending Now': 'Tendencias Ahora',
    'New Arrivals': 'Novedades',
    'Editor\'s Choice': 'Elección del Editor',

    // Catégories
    'AI Chatbots & Assistants': 'Chatbots y Asistentes IA',
    'AI Writing Tools': 'Herramientas de Escritura IA',
    'AI Image Generation': 'Generación de Imágenes IA',
    'AI Video Tools': 'Herramientas de Video IA',
    'AI Audio & Music': 'Audio y Música IA',
    'AI Coding Tools': 'Herramientas de Codificación IA',
    'AI Productivity': 'Productividad IA',
    'AI for SEO': 'IA para SEO',
    'AI for Business': 'IA para Negocios',
    'AI for Networking': 'IA para Redes',
    'AI for Cybersecurity': 'IA para Ciberseguridad',

    // Boutons et actions
    'Try': 'Probar',
    'Try Free': 'Probar Gratis',
    'Try for free': 'Probar gratis',
    'Try it free': 'Pruébalo gratis',
    'Try Now': 'Probar Ahora',
    'Get Started': 'Comenzar',
    'Get Started Free': 'Comenzar Gratis',
    'Start Free': 'Empezar Gratis',
    'Learn More': 'Saber más',
    'Read Review': 'Leer Reseña',
    'Full Review': 'Reseña Completa',
    'View All': 'Ver Todo',
    'View All Tools': 'Ver Todas las Herramientas',
    'Show More': 'Ver Más',
    'Show Less': 'Ver Menos',
    'Load More': 'Cargar Más',
    'Explore': 'Explorar',
    'Discover': 'Descubrir',
    'Compare': 'Comparar',
    'Sign Up': 'Registrarse',
    'Sign In': 'Iniciar Sesión',
    'Login': 'Iniciar Sesión',
    'Register': 'Registrarse',
    'Download': 'Descargar',
    'Visit Website': 'Visitar Sitio Web',
    'Official Website': 'Sitio Oficial',
    'Go to': 'Ir a',

    // Statut et badges
    'for free': 'gratis',
    'free': 'gratis',
    'Free': 'Gratis',
    'Free Plan': 'Plan Gratuito',
    'Free Trial': 'Prueba Gratuita',
    'Popular': 'Popular',
    'New': 'Nuevo',
    'Updated': 'Actualizado',
    'Premium': 'Premium',
    'Pro': 'Pro',
    'Plus': 'Plus',
    'Enterprise': 'Empresarial',
    'Business': 'Negocios',
    'Starter': 'Inicial',
    'Basic': 'Básico',
    'Advanced': 'Avanzado',
    'Professional': 'Profesional',
    'Verified': 'Verificado',
    'Recommended': 'Recomendado',
    'Featured': 'Destacado',
    'Trending': 'Tendencia',
    'Hot': 'Popular',
    'Best': 'Mejor',
    'Top Rated': 'Mejor Calificado',

    // Ratings & Labels
    'Coding': 'Codificación',
    'Reasoning': 'Razonamiento',
    'Context': 'Contexto',
    'Value': 'Valor',
    'Get': 'Obtener',

    // Sections et titres
    'Features': 'Características',
    'Key Features': 'Características Clave',
    'Main Features': 'Características Principales',
    'Pricing': 'Precios',
    'Plans': 'Planes',
    'Pricing Plans': 'Planes de Precios',
    'Overview': 'Resumen',
    'Description': 'Descripción',
    'About': 'Acerca de',
    'Pros': 'Ventajas',
    'Cons': 'Desventajas',
    'Advantages': 'Ventajas',
    'Disadvantages': 'Desventajas',
    'Alternatives': 'Alternativas',
    'Similar Tools': 'Herramientas Similares',
    'Summary': 'Resumen',
    'Rating': 'Calificación',
    'Ratings': 'Calificaciones',
    'Review': 'Reseña',
    'Reviews': 'Reseñas',
    'User Reviews': 'Reseñas de Usuarios',
    'Comparison': 'Comparación',
    'Getting Started': 'Comenzar',
    'How to Use': 'Cómo Usar',
    'Tutorial': 'Tutorial',
    'Guide': 'Guía',
    'Guides': 'Guías',
    'FAQ': 'Preguntas Frecuentes',
    'Help': 'Ayuda',
    'Support': 'Soporte',
    'Documentation': 'Documentación',
    'Docs': 'Docs',
    'API': 'API',
    'Blog': 'Blog',
    'News': 'Noticias',
    'Updates': 'Actualizaciones',
    'Changelog': 'Registro de cambios',

    // Stats et métriques
    'Tools': 'Herramientas',
    'Tools Reviewed': 'Herramientas Revisadas',
    'AI Tools': 'Herramientas IA',
    'Avg Rating': 'Calificación Promedio',
    'Average Rating': 'Calificación Promedio',
    'Users': 'Usuarios',
    'Active Users': 'Usuarios Activos',
    'Downloads': 'Descargas',
    'Views': 'Vistas',
    'Likes': 'Me gusta',
    'Shares': 'Compartidos',
    'Comments': 'Comentarios',

    // Pays et régions
    'United States': 'Estados Unidos',
    'China': 'China',
    'International': 'Internacional',
    'Global': 'Global',
    'Worldwide': 'Mundial',
    'Europe': 'Europa',
    'Asia': 'Asia',
    'America': 'América',

    // Navigation
    'Home': 'Inicio',
    'Back': 'Atrás',
    'Next': 'Siguiente',
    'Previous': 'Anterior',
    'Close': 'Cerrar',
    'Open': 'Abrir',
    'Menu': 'Menú',
    'Search': 'Buscar',
    'Filter': 'Filtrar',
    'Sort': 'Ordenar',
    'All': 'Todos',
    'Latest': 'Últimos',
    'Oldest': 'Más antiguos',

    // Footer
    'Resources': 'Recursos',
    'Company': 'Empresa',
    'Legal': 'Legal',
    'Contact': 'Contacto',
    'Contact Us': 'Contáctanos',
    'About Us': 'Acerca de Nosotros',
    'Terms': 'Términos',
    'Terms of Service': 'Términos de Servicio',
    'Privacy': 'Privacidad',
    'Privacy Policy': 'Política de Privacidad',
    'Cookie Policy': 'Política de Cookies',
    'All rights reserved': 'Todos los derechos reservados',
    'Your trusted source for AI tool reviews, comparisons, and guides.': 'Tu fuente confiable para reseñas, comparaciones y guías de herramientas IA.',

    // Messages communs
    'Loading': 'Cargando',
    'Loading...': 'Cargando...',
    'Please wait': 'Por favor espera',
    'Error': 'Error',
    'Success': 'Éxito',
    'Warning': 'Advertencia',
    'Info': 'Información',
    'Coming Soon': 'Próximamente',
    'Under Construction': 'En construcción',
    'No results found': 'No se encontraron resultados',
    'Try again': 'Intentar de nuevo',
    'Refresh': 'Actualizar',
    'Share': 'Compartir',
    'Copy': 'Copiar',
    'Copied': 'Copiado',
    'Save': 'Guardar',
    'Saved': 'Guardado',
    'Delete': 'Eliminar',
    'Edit': 'Editar',
    'Cancel': 'Cancelar',
    'Confirm': 'Confirmar',
    'Yes': 'Sí',
    'No': 'No',
    'OK': 'OK',
    'Got it': 'Entendido',
    'Understand': 'Entendido'
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
    'TechVernia', 'TechVernia', 'Cursor', 'cursor', 'VS Code', 'Codeium', 'CodeWhisperer', 'Windsurf'
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

        // Ignorer les cellules de tableau (sauf si elles ont data-i18n)
        // Les tableaux contiennent souvent des données techniques qui ne doivent pas être traduites
        if (['td', 'th'].includes(tag) && !el.hasAttribute('data-i18n')) return;

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

// Observer pour détecter les changements DOM
let observer = null;
let currentLang = 'en';

function observeDOM() {
    if (observer) observer.disconnect();

    observer = new MutationObserver((mutations) => {
        if (currentLang === 'en') return;

        let shouldTranslate = false;
        for (const mutation of mutations) {
            if (mutation.type === 'childList' && mutation.addedNodes.length > 0) {
                shouldTranslate = true;
                break;
            }
        }

        if (shouldTranslate) {
            console.log('🔄 Nouveau contenu détecté - Re-traduction...');
            setTimeout(() => translateAll(currentLang), 100);
        }
    });

    observer.observe(document.body, {
        childList: true,
        subtree: true
    });

    console.log('👁️ Observer DOM activé');
}

// Init
function init() {
    if (!window.i18n || !window.i18n.getCurrentLanguage) {
        console.log('⏳ En attente de i18n...');
        setTimeout(init, 50);
        return;
    }

    console.log('✅ COMPLETE TRANSLATE: Prêt');

    // Activer l'observer DOM
    observeDOM();

    window.addEventListener('languageChanged', (e) => {
        currentLang = e.detail.language;
        console.log('📡 Langue changée → ' + currentLang);
        setTimeout(() => translateAll(currentLang), 100);
    });

    const lang = window.i18n.getCurrentLanguage();
    currentLang = lang;
    console.log('🌍 Langue détectée au chargement: ' + lang);

    if (lang && lang !== 'en') {
        console.log('🔄 Déclenchement de la traduction en ' + lang);
        // Traduire immédiatement après que le DOM soit prêt
        setTimeout(() => {
            console.log('🚀 Exécution de translateAll(' + lang + ')');
            translateAll(lang);
        }, 100);
    } else {
        console.log('ℹ️  Langue = EN ou non définie, pas de traduction');
    }
}

if (document.readyState === 'loading') {
    console.log('📄 DOM en cours de chargement...');
    document.addEventListener('DOMContentLoaded', init);
} else {
    console.log('📄 DOM déjà chargé, initialisation immédiate');
    init();
}

window.completeTranslate = translateAll;
console.log('✅ COMPLETE TRANSLATE: Chargé');
