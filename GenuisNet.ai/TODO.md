# 📝 TODO - GenuisNet.ai

## 🔴 PRIORITÉ HAUTE (À faire en premier)

### 1. Ajouter Full Reviews pour les 81 AI simples

**Catégories concernées:**
- ai-chatbots: 4 AI simples (Character.AI, Pi, YouChat, Mistral Chat)
- ai-writing: 4 AI simples
- ai-coding: 5 AI simples
- ai-image: 4 AI simples
- ai-video: 4 AI simples
- ai-audio: 4 AI simples
- ai-productivity: 4 AI simples
- ai-seo: 4 AI simples (+ Surfer SEO, LongShot AI, SEO.ai sans full review)
- ai-business: 4 AI simples
- ai-networking: 6 AI simples
- ai-cybersecurity: 12 AI (TOUTES simples)
- ai-medical: 12 AI (TOUTES simples)
- ai-architecture: 12 AI (TOUTES simples)

**Template de full review à suivre:**
```html
<article class="tool-card-full">
    <div class="tool-card-header">
        <div class="tool-logo-large [class-name]"></div>
        <div class="tool-header-info">
            <h3>[AI Name]</h3>
            <span class="company">by [Company]</span>
            <div style="display: flex; gap: var(--space-sm); margin-top: var(--space-sm); align-items: center;">
                <span class="badge badge-[type]">[Badge]</span>
                <span class="badge badge-rating">[Rating] ★</span>
                <span class="country-flag">[Flag]</span>
            </div>
        </div>
    </div>
    <div class="tool-card-body">
        <p class="tool-description">[Description détaillée]</p>
        <div class="tool-features-list">
            <span class="feature-tag">Feature 1</span>
            <!-- Plus de features -->
        </div>
        <div class="tool-stats">
            <div class="stat-item">
                <div class="stat-value">[Value]</div>
                <div class="stat-label">[Label]</div>
            </div>
            <!-- Plus de stats -->
        </div>
        <div class="pros-cons">
            <div class="pros">
                <h4>Pros</h4>
                <ul>
                    <li>[Pro 1]</li>
                    <!-- Plus de pros -->
                </ul>
            </div>
            <div class="cons">
                <h4>Cons</h4>
                <ul>
                    <li>[Con 1]</li>
                    <!-- Plus de cons -->
                </ul>
            </div>
        </div>
        <div class="tool-pricing-row">
            <div class="pricing-info">
                <span class="price">[Price]</span>
                <span class="period">[Period]</span>
            </div>
            <div class="tool-actions">
                <a href="[review-link]" class="btn btn-outline">Full Review</a>
                <a href="[website]" class="btn btn-primary" target="_blank" rel="nofollow sponsored">Try Free →</a>
            </div>
        </div>
    </div>
</article>
```

**Étapes:**
1. Créer un script Python pour transformer cartes simples en full reviews
2. Rechercher infos pour chaque AI (pricing, features, stats, pros/cons)
3. Utiliser ChatGPT/Claude pour générer contenu si besoin
4. Vérifier cohérence et qualité

---

### 2. Télécharger les 61 logos manquants

**AI sans logo (avec emoji):**

**Chatbots (4):**
- Microsoft Copilot 🤖
- Pi 🥧
- YouChat 💬
- Mistral Chat 🌬️

**Writing (7):**
- Jasper ✨
- Copy.ai 📝
- Writesonic 🎵
- Wordtune 🎯
- Sudowrite ✍️
- Grammarly ✅
- Scalenut 📈

**Coding (6):**
- GitHub Copilot 👨‍✈️
- Replit AI 🔄
- Blackbox AI ⬛
- Phind 🔍
- Bito AI 🤖
- AlphaCode 🅰️

**Image (4):**
- Midjourney 🎨
- DALL-E 3 🖼️
- Ideogram 💡
- Runway ML 🎬

**Video (5):**
- Runway Gen-2 🎬
- Synthesia 🎥
- Descript 🎙️
- Lumen5 💡
- OpusClip ✂️

**Audio (5):**
- Murf AI 🎤
- Descript Overdub 🎙️
- WellSaid Labs 🗣️
- LOVO 🔊
- Krisp 🔇

**Productivity (6):**
- Reclaim AI 📅
- Mem 🧠
- Tactiq 📝
- Clockwise 🕐
- Sunsama ☀️
- Superhuman ⚡

**SEO (3):**
- Surfer SEO 🏄
- LongShot AI 🎯
- SEO.ai 🔍

**Business (2):**
- UiPath 🤖
- Workday AI 💼

**Networking (3):**
- Juniper Mist AI 🌫️
- Aruba AI 🏝️
- Auvik 🌐

**Cybersecurity (4):**
- CrowdStrike Falcon 🦅
- Darktrace 🕷️
- Vectra AI 🔎
- Cylance 🛡️

**Medical (4):**
- Zebra Medical Vision 🦓
- Viz.ai 🧠
- Tempus ⏱️
- Babylon Health 🏥

**Architecture (5):**
- TestFit 📐
- Finch3D 🐦
- Archistar 🏗️
- Augmenta 🔧
- Doxel 📊

**Sources alternatives à essayer:**
1. Sites officiels (section press/media)
2. GitHub repositories
3. Crunchbase
4. LinkedIn company pages
5. ProductHunt
6. Logo.dev API
7. Clearbit Logo API
8. Brandfetch
9. Créer logos SVG simples avec initiales

---

### 3. Créer pages de review détaillées

**Structure des dossiers:**
```
pages/reviews/
├── chatbots/
│   ├── chatgpt.html
│   ├── claude.html
│   ├── gemini.html
│   └── [autres...]
├── writing/
├── coding/
├── image/
├── video/
├── audio/
├── productivity/
├── seo/
├── business/
├── networking/
├── cybersecurity/
├── medical/
└── architecture/
```

**Template de page review:**
- Hero section avec logo et CTA
- Overview (description complète)
- Key Features (liste détaillée)
- Pricing Plans (tableau comparatif)
- Use Cases (exemples concrets)
- Pros & Cons (détaillés)
- Alternatives (comparaison avec concurrents)
- FAQ
- User Reviews/Ratings
- Footer avec CTA

**Créer un template HTML réutilisable:**
`/pages/reviews/template.html`

---

## 🟡 PRIORITÉ MOYENNE

### 4. Optimisation des performances

- [ ] Compresser tous les logos PNG (TinyPNG, ImageOptim)
- [ ] Convertir logos en WebP avec fallback PNG
- [ ] Minifier CSS et JavaScript
- [ ] Lazy loading pour les images
- [ ] Preload des ressources critiques
- [ ] CDN pour assets statiques
- [ ] Cache headers appropriés

### 5. SEO et Métadonnées

**Pour chaque page:**
- [ ] Meta title unique (50-60 caractères)
- [ ] Meta description unique (150-160 caractères)
- [ ] Open Graph tags (og:title, og:description, og:image)
- [ ] Twitter Card tags
- [ ] Canonical URLs
- [ ] Alt text pour toutes les images
- [ ] Schema.org markup (Organization, WebSite, Review)
- [ ] Sitemap.xml
- [ ] Robots.txt

### 6. Amélioration de la navigation

- [ ] Barre de recherche fonctionnelle
- [ ] Filtres par catégorie/pricing/features
- [ ] Breadcrumbs
- [ ] Pagination pour les catégories avec 20+ AI
- [ ] "Related Tools" sur chaque page
- [ ] "Recently Viewed" tracking

### 7. Fonctionnalités interactives

- [ ] Comparaison côte-à-côte (comparer 2-3 AI)
- [ ] Système de rating/reviews utilisateurs
- [ ] Bookmark/Favorites
- [ ] Filtres avancés (price range, features, etc.)
- [ ] Dark mode toggle
- [ ] Langue switcher (préparer i18n)

---

## 🟢 PRIORITÉ BASSE

### 8. Blog et contenu

- [ ] Section blog (/blog/)
- [ ] Articles "Best AI for [use case]"
- [ ] Guides "How to use [AI tool]"
- [ ] Comparaisons détaillées
- [ ] News section (nouveautés AI)
- [ ] Case studies

### 9. Analytics et tracking

- [ ] Google Analytics 4
- [ ] Hotjar ou alternative (heatmaps)
- [ ] Event tracking (clics CTA, navigation)
- [ ] Conversion funnel analysis
- [ ] A/B testing setup

### 10. Newsletter et engagement

- [ ] Formulaire newsletter (Mailchimp/Sendinblue)
- [ ] Lead magnet (ebook, guide gratuit)
- [ ] Email sequences (welcome, tips, etc.)
- [ ] RSS feed

### 11. Monétisation

- [ ] Programme d'affiliation structuré
- [ ] Disclosure pages
- [ ] Tracking links pour analytics
- [ ] Sponsored listings (si applicable)

### 12. Infrastructure

- [ ] Initialiser repo Git
- [ ] `.gitignore` approprié
- [ ] Branches (dev, staging, production)
- [ ] CI/CD pipeline
- [ ] Backups automatiques
- [ ] Monitoring uptime
- [ ] SSL certificate

---

## 📊 MÉTRIQUES DE SUCCÈS

**Court terme (1 mois):**
- [ ] 200+ AI tools listés
- [ ] 100+ full reviews complétées
- [ ] 90%+ logos réels (non-emoji)
- [ ] Toutes les pages review créées
- [ ] SEO optimisé (score 90+ sur PageSpeed)

**Moyen terme (3 mois):**
- [ ] 500+ AI tools
- [ ] 10 articles de blog
- [ ] 1000+ visiteurs/mois
- [ ] Newsletter 100+ subscribers
- [ ] Mobile responsive parfait

**Long terme (6 mois):**
- [ ] 1000+ AI tools
- [ ] 50+ articles de blog
- [ ] 10,000+ visiteurs/mois
- [ ] Top 3 Google pour keywords clés
- [ ] Multilingue (FR, EN, ES)

---

## 🛠️ OUTILS RECOMMANDÉS

**Design:**
- Figma (wireframes, mockups)
- Canva (graphics, social media)

**Développement:**
- VS Code
- Git + GitHub
- Chrome DevTools

**SEO:**
- Google Search Console
- Google Analytics
- Ahrefs/SEMrush
- Screaming Frog

**Performance:**
- GTmetrix
- PageSpeed Insights
- WebPageTest

**Testing:**
- BrowserStack (cross-browser)
- Lighthouse (audits)

---

## 📅 PLANNING SUGGÉRÉ

**Semaine 1:**
- Full reviews prioritaires (cybersecurity, medical, architecture)
- Télécharger 30 logos manquants

**Semaine 2:**
- Compléter full reviews restantes
- Créer template pages review
- Optimisation images

**Semaine 3:**
- Créer pages review individuelles
- SEO optimization
- Testing mobile

**Semaine 4:**
- Blog setup
- Analytics
- Lancement v1.0

---

*TODO créé le 2 Décembre 2025*
*À mettre à jour régulièrement! 📝*
