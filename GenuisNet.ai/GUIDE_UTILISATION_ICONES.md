# 🎨 Guide d'Utilisation des Nouvelles Icônes SVG

## 📋 Table des Matières
1. [Icônes Disponibles](#icones-disponibles)
2. [Comment les Utiliser](#comment-les-utiliser)
3. [Exemples Pratiques](#exemples-pratiques)
4. [Personnalisation](#personnalisation)

---

## 🎯 Icônes Disponibles

### Documentation & Navigation
```html
<!-- Document -->
<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <path d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
</svg>
```

### Fonctionnalités & Performance
```html
<!-- Layers / Stack (Fonctionnalités) -->
<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <path d="M12 2L2 7l10 5 10-5-10-5z"/>
    <path d="M2 17l10 5 10-5M2 12l10 5 10-5"/>
</svg>

<!-- Lightning (Performance) -->
<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>
</svg>
```

### Validation & Status
```html
<!-- Check Circle (Avantages) -->
<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <path d="M22 11.08V12a10 10 0 11-5.93-9.14"/>
    <polyline points="22 4 12 14.01 9 11.01"/>
</svg>

<!-- X Circle (Inconvénients) -->
<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <circle cx="12" cy="12" r="10"/>
    <line x1="15" y1="9" x2="9" y2="15"/>
    <line x1="9" y1="9" x2="15" y2="15"/>
</svg>
```

### Business & Finance
```html
<!-- Dollar (Prix) -->
<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <line x1="12" y1="1" x2="12" y2="23"/>
    <path d="M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"/>
</svg>

<!-- Briefcase (Business) -->
<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <rect x="2" y="7" width="20" height="14" rx="2" ry="2"/>
    <path d="M16 21V5a2 2 0 00-2-2h-4a2 2 0 00-2 2v16"/>
</svg>
```

### Alerts & Messages
```html
<!-- Alert Triangle (Attention) -->
<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z"/>
    <line x1="12" y1="9" x2="12" y2="13"/>
    <line x1="12" y1="17" x2="12.01" y2="17"/>
</svg>

<!-- Lightbulb (Conseil) -->
<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <path d="M9 18h6"/><path d="M10 22h4"/>
    <path d="M15.09 14c.18-.98.65-1.74 1.41-2.5A4.65 4.65 0 0018 8a6 6 0 10-12 0c0 1.33.47 2.48 1.5 3.5.76.76 1.23 1.52 1.41 2.5"/>
</svg>
```

### Tech & Security
```html
<!-- Lock (Sécurité) -->
<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <rect x="3" y="11" width="18" height="11" rx="2" ry="2"/>
    <path d="M7 11V7a5 5 0 0110 0v4"/>
</svg>

<!-- Tool / Wrench (Configuration) -->
<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z"/>
</svg>
```

### Analytics & Data
```html
<!-- Bar Chart (Analytics) -->
<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <line x1="18" y1="20" x2="18" y2="10"/>
    <line x1="12" y1="20" x2="12" y2="4"/>
    <line x1="6" y1="20" x2="6" y2="14"/>
</svg>

<!-- Trending Up (Croissance) -->
<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/>
    <polyline points="17 6 23 6 23 12"/>
</svg>
```

### Targeting & Goals
```html
<!-- Target (Ciblage) -->
<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <circle cx="12" cy="12" r="10"/>
    <circle cx="12" cy="12" r="6"/>
    <circle cx="12" cy="12" r="2"/>
</svg>

<!-- Star (Excellence) -->
<svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>
</svg>
```

---

## 💡 Comment les Utiliser

### Dans les Titres H2
```html
<h2>
    <svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <!-- Votre icône ici -->
    </svg>
    Titre de la Section
</h2>
```

**Résultat**: Icône avec gradient cyan→violet et effet de glow

### Dans les Paragraphes
```html
<p>
    <svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <!-- Votre icône ici -->
    </svg>
    Texte avec icône au début
</p>
```

### Dans les Listes
```html
<ul style="list-style: none;">
    <li>
        <svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <!-- Icône check -->
        </svg>
        Premier point avec icône
    </li>
    <li>
        <svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <!-- Icône check -->
        </svg>
        Deuxième point avec icône
    </li>
</ul>
```

---

## 📝 Exemples Pratiques

### Section Avantages
```html
<div class="success-box">
    <h3>
        <svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M22 11.08V12a10 10 0 11-5.93-9.14"/>
            <polyline points="22 4 12 14.01 9 11.01"/>
        </svg>
        Avantages
    </h3>
    <ul style="list-style: none; padding-left: 0;">
        <li>
            <svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M22 11.08V12a10 10 0 11-5.93-9.14"/>
                <polyline points="22 4 12 14.01 9 11.01"/>
            </svg>
            Performances exceptionnelles
        </li>
        <li>
            <svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M22 11.08V12a10 10 0 11-5.93-9.14"/>
                <polyline points="22 4 12 14.01 9 11.01"/>
            </svg>
            Interface intuitive
        </li>
    </ul>
</div>
```

### Section Inconvénients
```html
<div class="warning-box">
    <h3>
        <svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="10"/>
            <line x1="15" y1="9" x2="9" y2="15"/>
            <line x1="9" y1="9" x2="15" y2="15"/>
        </svg>
        Inconvénients
    </h3>
    <ul style="list-style: none; padding-left: 0;">
        <li>
            <svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="12" cy="12" r="10"/>
                <line x1="15" y1="9" x2="9" y2="15"/>
                <line x1="9" y1="9" x2="15" y2="15"/>
            </svg>
            Prix élevé pour les petites entreprises
        </li>
    </ul>
</div>
```

### Section Prix
```html
<div class="tip-box">
    <h3>
        <svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <line x1="12" y1="1" x2="12" y2="23"/>
            <path d="M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"/>
        </svg>
        Tarification
    </h3>
    <p>À partir de $20/mois</p>
</div>
```

---

## 🎨 Personnalisation

### Taille des Icônes
```css
/* Taille par défaut */
.inline-icon {
    width: 1.2em;
    height: 1.2em;
}

/* Icône grande */
.inline-icon-lg {
    width: 2em;
    height: 2em;
}

/* Icône petite */
.inline-icon-sm {
    width: 1em;
    height: 1em;
}
```

### Couleurs Personnalisées
```html
<!-- Icône cyan -->
<svg class="inline-icon" style="stroke: #00D9FF;">...</svg>

<!-- Icône violette -->
<svg class="inline-icon" style="stroke: #A855F7;">...</svg>

<!-- Icône verte -->
<svg class="inline-icon" style="stroke: #22C55E;">...</svg>
```

### Animation Personnalisée
```css
.inline-icon-animated {
    transition: all 0.3s ease;
}

.inline-icon-animated:hover {
    transform: scale(1.2) rotate(10deg);
}
```

---

## 🌈 Palette de Couleurs Recommandées

### Pour les Boxes
- **Success**: `#22C55E` (vert)
- **Warning**: `#FB923C` (orange)
- **Info**: `#00D9FF` (cyan)
- **Tip**: `#8B5CF6` (violet)

### Pour les Gradients
- **Primary**: `#00D9FF → #A855F7`
- **Secondary**: `#A855F7 → #F472B6`
- **Accent**: `#00FFF0 → #A855F7`

---

## 🚀 Astuces Pro

### 1. Cohérence Visuelle
Utilisez toujours la même icône pour le même type de contenu:
- ✅ pour tous les avantages
- ❌ pour tous les inconvénients
- 💰 pour toutes les sections prix

### 2. Animation au Survol
Les icônes dans les H2 ont automatiquement une animation au survol. Profitez-en!

### 3. Accessibilité
Ajoutez toujours un attribut `aria-label` pour les icônes importantes:
```html
<svg class="inline-icon" aria-label="Avantage" viewBox="0 0 24 24">...</svg>
```

### 4. Performance
Les icônes SVG sont légères (< 1KB chacune). Pas de souci de performance!

---

## 📚 Ressources

- **Fichier CSS**: `css/guides-reviews.css`
- **Démo**: `exemple-icones-moderne.html`
- **Documentation**: `RAPPORT_MODERNISATION_ICONES_POLICE.md`

---

**Dernière mise à jour**: 1er Décembre 2025
