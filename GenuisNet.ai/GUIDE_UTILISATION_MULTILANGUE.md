# 🌍 Guide d'Utilisation - Système Multilingue

## 🎯 Comment Utiliser le Système

### Pour les Visiteurs du Site

#### Changer la Langue
1. Ouvrez n'importe quelle page du site
2. Cherchez l'icône 🌐 en haut à droite de la navigation
3. Cliquez sur l'icône
4. Sélectionnez votre langue préférée parmi 10 options
5. La page change instantanément!

#### Langues Disponibles
- 🇺🇸 **English** - Langue par défaut
- 🇪🇸 **Español** - Espagnol
- 🇫🇷 **Français** - Français
- 🇩🇪 **Deutsch** - Allemand
- 🇧🇷 **Português** - Portugais
- 🇨🇳 **中文** - Chinois
- 🇯🇵 **日本語** - Japonais
- 🇰🇷 **한국어** - Coréen
- 🇸🇦 **العربية** - Arabe (avec affichage RTL)
- 🇮🇳 **हिन्दी** - Hindi

#### Persistance
Votre choix de langue est **automatiquement sauvegardé** dans votre navigateur. Quand vous revenez sur le site, votre langue préférée sera restaurée.

---

## 👨‍💻 Pour les Développeurs

### Ajouter une Nouvelle Traduction

#### Étape 1: Ajouter la Clé dans `js/i18n.js`

```javascript
const translations = {
    en: {
        // ... autres traductions
        "section.new.title": "My New Section",
        "section.new.desc": "Description of my section"
    },

    fr: {
        // ... autres traductions
        "section.new.title": "Ma Nouvelle Section",
        "section.new.desc": "Description de ma section"
    },

    es: {
        // ... autres traductions
        "section.new.title": "Mi Nueva Sección",
        "section.new.desc": "Descripción de mi sección"
    },

    // ... Répéter pour toutes les langues
};
```

#### Étape 2: Utiliser dans le HTML

```html
<!-- Simple texte -->
<h2 data-i18n="section.new.title">My New Section</h2>
<p data-i18n="section.new.desc">Description of my section</p>

<!-- Avec HTML à l'intérieur -->
<div data-i18n-html="section.new.content">
    <strong>Bold text</strong> with <em>italic</em>
</div>

<!-- Placeholder d'input -->
<input type="text"
       placeholder="Search..."
       data-i18n-placeholder="search.placeholder">

<!-- Attributs alt/title/aria-label -->
<img src="..." alt="Image" data-i18n-alt="image.alt">
<button title="Click me" data-i18n-title="button.title">...</button>
<button aria-label="Close" data-i18n-aria="ui.close">X</button>
```

### Convention de Nommage des Clés

```javascript
// Navigation
"nav.home"
"nav.categories"
"nav.guides"

// Catégories
"cat.chatbots"
"cat.chatbots.desc"
"cat.chatbots.full"

// Sections
"section.featured.title"
"section.featured.subtitle"

// Boutons
"btn.review"
"btn.tryNow"
"btn.learnMore"

// UI Commune
"ui.loading"
"ui.error"
"ui.close"

// Stats
"stats.tools"
"stats.categories"
```

### API JavaScript

#### Changer la Langue par Code

```javascript
// Changer la langue
window.i18n.setLanguage('fr');

// Obtenir la langue actuelle
const currentLang = window.i18n.getCurrentLanguage();
console.log(currentLang); // 'en', 'fr', 'es', etc.

// Obtenir toutes les langues disponibles
const langs = window.i18n.getAvailableLanguages();
console.log(langs); // ['en', 'es', 'fr', 'de', ...]

// Traduire une clé spécifique
const translation = window.i18n.t('nav.home');
console.log(translation); // "Home" ou "Accueil" selon la langue
```

#### Écouter les Changements de Langue

```javascript
// Événement déclenché quand la langue change
window.addEventListener('languageChanged', (event) => {
    const newLang = event.detail.language;
    console.log('Language changed to:', newLang);

    // Faire quelque chose de spécifique
    // Ex: recharger du contenu dynamique
    loadDynamicContent(newLang);
});
```

#### Traduire Dynamiquement du Contenu

```javascript
// Pour du contenu chargé via AJAX/fetch
function loadAndTranslate() {
    fetch('/api/data')
        .then(response => response.json())
        .then(data => {
            // Créer les éléments
            const container = document.getElementById('content');
            const title = document.createElement('h2');
            title.setAttribute('data-i18n', 'dynamic.title');
            title.textContent = 'Default Title';
            container.appendChild(title);

            // Traduire l'élément
            window.i18n.translateElement(title);
        });
}
```

### Ajouter une Nouvelle Langue

#### 1. Ajouter les Traductions dans `js/i18n.js`

```javascript
const translations = {
    // ... langues existantes

    // Nouvelle langue: Italien
    it: {
        "nav.home": "Home",
        "nav.categories": "Categorie",
        "nav.guides": "Guide",
        "nav.compare": "Confronta",
        "nav.about": "Chi Siamo",
        // ... toutes les autres clés
    }
};

// Configuration de la langue
const languages = {
    // ... langues existantes

    it: {
        name: "Italiano",
        flag: "🇮🇹",
        dir: "ltr"
    }
};

// Mots pour l'effet typing
const typingWords = {
    // ... langues existantes

    it: [
        "Migliori Strumenti AI",
        "Soluzione Perfetta",
        "Automazione Intelligente"
    ]
};
```

#### 2. Ajouter l'Option dans le HTML

Ajouter dans tous les fichiers HTML ayant le sélecteur:

```html
<div class="lang-dropdown" id="lang-dropdown">
    <!-- ... options existantes -->

    <button class="lang-option" data-lang="it">
        <span class="flag">🇮🇹</span> Italiano
    </button>
</div>
```

### Structure du Fichier i18n.js

```
js/i18n.js
├── translations (Object)
│   ├── en: { ... }      // Traductions anglaises
│   ├── es: { ... }      // Traductions espagnoles
│   ├── fr: { ... }      // Traductions françaises
│   └── ...
├── typingWords (Object)
│   ├── en: [...]        // Mots animés en anglais
│   └── ...
├── languages (Object)
│   ├── en: { name, flag, dir }
│   └── ...
├── currentLanguage      // Variable globale
└── Functions:
    ├── initI18n()
    ├── setLanguage(lang)
    ├── translatePage()
    ├── getTranslation(key)
    ├── setupLanguageSelector()
    └── t(key)
```

## 🎨 Exemples Pratiques

### Exemple 1: Page de Catégorie Complète

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title data-i18n="cat.chatbots">AI Chatbots</title>
    <!-- ... autres head tags -->
</head>
<body>
    <nav>
        <a href="/" data-i18n="nav.home">Home</a>
        <a href="/categories" data-i18n="nav.categories">Categories</a>
        <!-- Sélecteur de langue (déjà présent) -->
    </nav>

    <section class="hero">
        <h1 data-i18n="cat.chatbots">AI Chatbots & Assistants</h1>
        <p data-i18n="cat.chatbots.full">
            ChatGPT, Claude, Gemini and more...
        </p>
    </section>

    <script src="js/i18n.js"></script>
</body>
</html>
```

### Exemple 2: Boutons d'Action

```html
<!-- Boutons de review -->
<a href="/review/chatgpt" class="btn" data-i18n="btn.review">
    Read Review
</a>

<!-- Boutons d'essai -->
<a href="/try/chatgpt" class="btn" data-i18n="btn.try">
    Try Free
</a>

<!-- Boutons de navigation -->
<button data-i18n="ui.close">Close</button>
<button data-i18n="ui.next">Next</button>
```

### Exemple 3: Formulaire de Newsletter

```html
<section class="newsletter">
    <h3 data-i18n="newsletter.title">Stay Ahead with AI</h3>
    <p data-i18n="newsletter.desc">
        Get weekly updates on the latest AI tools...
    </p>

    <form>
        <input type="email"
               placeholder="Enter your email"
               data-i18n-placeholder="newsletter.placeholder">

        <button type="submit" data-i18n="newsletter.btn">
            Subscribe
        </button>
    </form>

    <small data-i18n="newsletter.note">
        No spam. Unsubscribe anytime.
    </small>
</section>
```

## 🐛 Débogage

### Vérifier si i18n est Chargé

```javascript
// Dans la console du navigateur
console.log(window.i18n);

// Si undefined, le script n'est pas chargé
// Vérifier: <script src="js/i18n.js"></script>
```

### Vérifier la Langue Actuelle

```javascript
console.log(window.i18n.getCurrentLanguage());
console.log(localStorage.getItem('language'));
```

### Tester une Traduction

```javascript
// Tester si une clé existe
console.log(window.i18n.t('nav.home'));

// Devrait retourner "Home" ou "Accueil" etc.
// Si retourne la clé elle-même, la traduction n'existe pas
```

### Forcer une Langue

```javascript
// Forcer le français
window.i18n.setLanguage('fr');

// Forcer l'anglais
window.i18n.setLanguage('en');

// Supprimer la préférence sauvegardée
localStorage.removeItem('language');
location.reload();
```

## 📚 Ressources

### Fichiers Importants
- **`js/i18n.js`** - Système de traduction complet
- **`RAPPORT_MULTILANGUE_FINAL.md`** - Rapport détaillé
- **`TEST_LANGUAGE_SWITCHING.md`** - Guide de test
- **`add_language_selector_everywhere.py`** - Script d'installation
- **`add_i18n_attributes.py`** - Script d'ajout d'attributs

### Scripts Utiles
```bash
# Trouver tous les éléments sans data-i18n
grep -r ">" pages/*.html | grep -v "data-i18n" | grep -E "<(h1|h2|h3|button|a)"

# Compter les traductions
grep -c '"[a-z]' js/i18n.js

# Vérifier les pages avec i18n.js
grep -r "i18n.js" pages/ | wc -l
```

## ✅ Checklist pour Nouvelle Page

- [ ] Inclure `<script src="js/i18n.js"></script>` avant `</body>`
- [ ] Ajouter le sélecteur de langue dans la navigation
- [ ] Ajouter `data-i18n` sur les liens de navigation
- [ ] Ajouter `data-i18n` sur les titres principaux
- [ ] Ajouter `data-i18n` sur les boutons
- [ ] Tester dans le navigateur
- [ ] Vérifier que la langue persiste

---

*Guide créé le 3 décembre 2025*
*GenuisNet.ai - Système Multilingue*
