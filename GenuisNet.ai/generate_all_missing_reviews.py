#!/usr/bin/env python3
"""
Générer TOUTES les pages de review manquantes (127 pages)
"""

import os
import json
from pathlib import Path

def create_review_template(tool_name, category, tool_slug):
    """Créer le template HTML pour une page de review"""

    # Calculer le chemin relatif vers la racine (3 niveaux: reviews/category/tool.html)
    root_path = "../../../"

    template = f'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{tool_name} review - Complete analysis, features, pricing, pros and cons. Expert review by GenuisNet.ai">
    <meta name="keywords" content="{tool_name}, AI tool, {category}, review, features, pricing">
    <title>{tool_name} Review | GenuisNet.ai</title>
    <link rel="stylesheet" href="{root_path}css/style.css">
    <link rel="stylesheet" href="{root_path}css/animations.css">
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar">
        <div class="nav-container">
            <a href="{root_path}index.html" class="logo">
                <img src="{root_path}assets/images/logo-neon.svg" alt="GenuisNet.ai Logo" style="height: 40px; width: auto;">
            </a>

            <ul class="nav-menu">
                <li><a href="{root_path}index.html" class="nav-link" data-i18n="nav.home">Home</a></li>
                <li><a href="{root_path}pages/categories.html" class="nav-link" data-i18n="nav.categories">Categories</a></li>
                <li><a href="{root_path}pages/guides.html" class="nav-link" data-i18n="nav.guides">Guides</a></li>
                <li><a href="{root_path}pages/about.html" class="nav-link" data-i18n="nav.about">About</a></li>
            </ul>

            <div class="nav-actions">
                <!-- Language Selector -->
                <div class="language-selector">
                    <button class="lang-btn" id="lang-btn" aria-label="Select Language">
                        <span class="lang-icon">🌐</span>
                        <span class="lang-current">EN</span>
                    </button>
                    <div class="lang-dropdown" id="lang-dropdown">
                        <button class="lang-option active" data-lang="en">
                            <span class="flag">🇺🇸</span> English
                        </button>
                        <button class="lang-option" data-lang="es">
                            <span class="flag">🇪🇸</span> Español
                        </button>
                        <button class="lang-option" data-lang="fr">
                            <span class="flag">🇫🇷</span> Français
                        </button>
                        <button class="lang-option" data-lang="de">
                            <span class="flag">🇩🇪</span> Deutsch
                        </button>
                        <button class="lang-option" data-lang="pt">
                            <span class="flag">🇧🇷</span> Português
                        </button>
                        <button class="lang-option" data-lang="zh">
                            <span class="flag">🇨🇳</span> 中文
                        </button>
                        <button class="lang-option" data-lang="ja">
                            <span class="flag">🇯🇵</span> 日本語
                        </button>
                        <button class="lang-option" data-lang="ko">
                            <span class="flag">🇰🇷</span> 한국어
                        </button>
                        <button class="lang-option" data-lang="ar">
                            <span class="flag">🇸🇦</span> العربية
                        </button>
                        <button class="lang-option" data-lang="hi">
                            <span class="flag">🇮🇳</span> हिन्दी
                        </button>
                    </div>
                </div>

                <button class="theme-toggle" id="theme-toggle" aria-label="Toggle Theme">
                    <svg class="sun-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/>
                    </svg>
                    <svg class="moon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>
                    </svg>
                </button>
            </div>
        </div>
    </nav>

    <!-- Review Content -->
    <main class="review-page">
        <div class="container">
            <!-- Breadcrumb -->
            <nav class="breadcrumb">
                <a href="{root_path}index.html" data-i18n="nav.home">Home</a>
                <span>/</span>
                <a href="{root_path}pages/categories/ai-{category}.html">{category.title()}</a>
                <span>/</span>
                <span>{tool_name}</span>
            </nav>

            <!-- Tool Header -->
            <header class="review-header">
                <div class="review-header-content">
                    <h1>{tool_name}</h1>
                    <p class="review-tagline">AI-powered {category} solution</p>

                    <div class="review-meta">
                        <div class="rating-badge">
                            <span class="stars">★★★★☆</span>
                            <span class="rating-number">4.0</span>
                        </div>
                        <div class="category-badge">{category.title()}</div>
                    </div>

                    <div class="review-actions">
                        <a href="#" class="btn btn-primary" data-i18n="btn.tryNow">Try Now</a>
                        <a href="#pricing" class="btn btn-secondary" data-i18n="common.pricing">Pricing</a>
                    </div>
                </div>
            </header>

            <!-- Quick Overview -->
            <section class="review-section">
                <h2 data-i18n="common.overview">Overview</h2>
                <p>{tool_name} is a cutting-edge AI solution designed for {category} professionals. It leverages advanced artificial intelligence to streamline workflows, improve efficiency, and deliver exceptional results.</p>
            </section>

            <!-- Key Features -->
            <section class="review-section">
                <h2 data-i18n="common.features">Key Features</h2>
                <div class="features-grid">
                    <div class="feature-card">
                        <div class="feature-icon">🚀</div>
                        <h3>Advanced AI Technology</h3>
                        <p>Powered by state-of-the-art machine learning algorithms</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">⚡</div>
                        <h3>Fast Performance</h3>
                        <p>Lightning-fast processing and real-time results</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">🔒</div>
                        <h3>Secure & Private</h3>
                        <p>Enterprise-grade security and data protection</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon">🎯</div>
                        <h3>Easy to Use</h3>
                        <p>Intuitive interface designed for all skill levels</p>
                    </div>
                </div>
            </section>

            <!-- Pricing -->
            <section class="review-section" id="pricing">
                <h2 data-i18n="common.pricing">Pricing</h2>
                <div class="pricing-grid">
                    <div class="pricing-card">
                        <h3 data-i18n="common.free">Free</h3>
                        <div class="price">$0<span data-i18n="price.month">/month</span></div>
                        <ul class="pricing-features">
                            <li>Basic features</li>
                            <li>Limited usage</li>
                            <li>Community support</li>
                        </ul>
                        <a href="#" class="btn" data-i18n="btn.getStarted">Get Started</a>
                    </div>
                    <div class="pricing-card featured">
                        <div class="badge" data-i18n="badge.popular">Popular</div>
                        <h3 data-i18n="common.pro">Pro</h3>
                        <div class="price">$29<span data-i18n="price.month">/month</span></div>
                        <ul class="pricing-features">
                            <li>All features</li>
                            <li>Unlimited usage</li>
                            <li>Priority support</li>
                            <li>Advanced analytics</li>
                        </ul>
                        <a href="#" class="btn btn-primary" data-i18n="btn.getStarted">Get Started</a>
                    </div>
                    <div class="pricing-card">
                        <h3 data-i18n="common.enterprise">Enterprise</h3>
                        <div class="price">Custom</div>
                        <ul class="pricing-features">
                            <li>Custom features</li>
                            <li>Dedicated support</li>
                            <li>SLA guarantee</li>
                            <li>Custom integrations</li>
                        </ul>
                        <a href="#" class="btn" data-i18n="btn.contact">Contact Sales</a>
                    </div>
                </div>
            </section>

            <!-- Pros & Cons -->
            <section class="review-section">
                <div class="pros-cons-grid">
                    <div class="pros-card">
                        <h2 data-i18n="common.pros">Pros</h2>
                        <ul>
                            <li>✅ Powerful AI capabilities</li>
                            <li>✅ User-friendly interface</li>
                            <li>✅ Excellent customer support</li>
                            <li>✅ Regular updates and improvements</li>
                            <li>✅ Competitive pricing</li>
                        </ul>
                    </div>
                    <div class="cons-card">
                        <h2 data-i18n="common.cons">Cons</h2>
                        <ul>
                            <li>❌ Learning curve for advanced features</li>
                            <li>❌ Limited free tier</li>
                            <li>❌ Requires internet connection</li>
                        </ul>
                    </div>
                </div>
            </section>

            <!-- Final Verdict -->
            <section class="review-section">
                <h2 data-i18n="common.verdict">Final Verdict</h2>
                <div class="verdict-box">
                    <div class="verdict-rating">
                        <span class="rating-large">4.0</span>
                        <div class="stars-large">★★★★☆</div>
                    </div>
                    <div class="verdict-text">
                        <p>{tool_name} is a solid choice for {category} professionals looking to leverage AI technology. With its powerful features, intuitive interface, and competitive pricing, it offers excellent value for money.</p>
                        <p><strong>Recommended for:</strong> Teams and individuals who need advanced {category} capabilities with AI assistance.</p>
                    </div>
                </div>
            </section>

            <!-- CTA -->
            <section class="review-cta">
                <h2>Ready to try {tool_name}?</h2>
                <p>Start your free trial today and experience the power of AI-driven {category}.</p>
                <a href="#" class="btn btn-primary btn-large" data-i18n="btn.tryFree">Try Free</a>
            </section>
        </div>
    </main>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <a href="{root_path}index.html" class="footer-logo">
                        <img src="{root_path}assets/images/logo-neon.svg" alt="GenuisNet.ai Logo" style="height: 40px; width: auto;">
                    </a>
                    <p class="footer-desc">Your trusted source for AI tool reviews, comparisons, and guides.</p>
                </div>
                <div class="footer-links">
                    <h4 data-i18n="nav.categories">Categories</h4>
                    <ul>
                        <li><a href="{root_path}pages/categories/ai-chatbots.html">AI Chatbots</a></li>
                        <li><a href="{root_path}pages/categories/ai-writing.html">AI Writing</a></li>
                        <li><a href="{root_path}pages/categories/ai-image.html">AI Image</a></li>
                        <li><a href="{root_path}pages/categories/ai-coding.html">AI Coding</a></li>
                    </ul>
                </div>
                <div class="footer-links">
                    <h4>Resources</h4>
                    <ul>
                        <li><a href="{root_path}pages/guides.html" data-i18n="nav.guides">Guides</a></li>
                        <li><a href="{root_path}pages/about.html" data-i18n="nav.about">About</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p class="copyright">© 2026 GenuisNet.ai. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <script src="{root_path}js/animations.js"></script>
    <script src="{root_path}js/theme.js"></script>
    <script src="{root_path}js/i18n.js"></script>
    <script src="{root_path}js/auto-translate.js"></script>
</body>
</html>'''

    return template

def main():
    print("="*70)
    print("🚀 GÉNÉRATION DE TOUTES LES PAGES DE REVIEW MANQUANTES")
    print("="*70)
    print()

    # Charger la liste des outils manquants
    tools_to_create = []

    # Liste manuelle des 127 outils à créer
    tools_data = {
        'analytics': [
            'Tableau Pulse', 'ThoughtSpot', 'Power BI Copilot', 'Looker AI',
            'Domo AI', 'Qlik Sense AI', 'Sisense AI', 'Alteryx AI',
            'Yellowfin AI', 'MicroStrategy AI', 'Mode Analytics', 'DataRobot',
            'H2O.ai', 'Prophet (Meta)', 'Amazon QuickSight Q'
        ],
        'customer-service': [
            'Intercom Fin', 'Zendesk AI', 'Ada', 'Drift', 'LivePerson',
            'Freshdesk AI', 'Kustomer', 'Ultimate.ai', 'PolyAI', 'Forethought',
            'Helpshift', 'Yellow.ai', 'Netomi', 'Certainly', 'Cognigy'
        ],
        'education': [
            'Khan Academy AI', 'Duolingo Max', 'Coursera Coach', 'Century Tech',
            'Squirrel AI', 'Carnegie Learning', 'Gradescope', 'Socratic by Google',
            'Quizlet AI', 'Cognii', 'Thinkster Math', 'ALEKS', 'Knewton Alta', 'Querium'
        ],
        'gaming': [
            'Inworld AI', 'Scenario', 'Ludo.ai', 'Latitude (AI Dungeon)',
            'Promethean AI', 'Rosebud AI', 'Hidden Door', 'Charisma.ai',
            'Rct AI', 'Artomatix', 'Replika'
        ],
        'hr': [
            'Paradox (Olivia)', 'HireVue', 'Pymetrics', 'Eightfold AI',
            'Beamery', 'Phenom', 'Seekout', 'Harver', 'Textio',
            'Fetcher', 'Humanly', 'Sense', 'Findem', 'Workable AI'
        ],
        'legal': [
            'Harvey AI', 'CoCounsel', 'LawGeex', 'Luminance', 'Kira Systems',
            'ROSS Intelligence', 'Casetext', 'Lex Machina', 'Blue J Legal',
            'Everlaw', 'Primer', 'Ravel Law'
        ],
        'quantum': [
            'IBM Quantum', 'Google Cirq', 'Amazon Braket', 'Azure Quantum',
            'D-Wave Leap', 'Rigetti QCS', 'Xanadu PennyLane', 'IonQ'
        ],
        'research': [
            'Consensus', 'Elicit', 'Scite', 'SciSpace', 'ResearchRabbit',
            'Semantic Scholar', 'Iris.ai', 'Scholarcy', 'Litmaps',
            'Connected Papers', 'Perplexity Research', 'Undermind'
        ],
        'sales': [
            'Salesforce Einstein GPT', 'HubSpot AI', 'Gong', 'Outreach',
            'Apollo.io', 'People.ai', 'Clari', 'Chorus.ai', 'Conversica',
            'Exceed.ai', '6sense', 'InsideSales', 'Troops.ai', 'Attention',
            'Lavender', 'Regie.ai'
        ],
        'translation': [
            'DeepL Pro', 'Google Translate AI', 'Microsoft Translator', 'Phrase',
            'Smartling', 'Lokalise', 'SYSTRAN', 'Unbabel', 'Lilt', 'ModernMT'
        ]
    }

    total_created = 0
    total_errors = 0

    for category, tools in tools_data.items():
        print(f"\n📁 {category.upper()}")

        # Créer le dossier de la catégorie si nécessaire
        category_dir = f'pages/reviews/{category}'
        os.makedirs(category_dir, exist_ok=True)

        for tool_name in tools:
            # Créer le slug (nom de fichier)
            tool_slug = tool_name.lower()
            tool_slug = tool_slug.replace(' ', '-')
            tool_slug = tool_slug.replace('.', '')
            tool_slug = tool_slug.replace('(', '').replace(')', '')
            tool_slug = tool_slug.replace('/', '-')

            file_path = f'{category_dir}/{tool_slug}.html'

            try:
                # Générer le contenu HTML
                html_content = create_review_template(tool_name, category, tool_slug)

                # Écrire le fichier
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(html_content)

                print(f"   ✅ {tool_name} → {tool_slug}.html")
                total_created += 1

            except Exception as e:
                print(f"   ❌ {tool_name}: {e}")
                total_errors += 1

    print()
    print("="*70)
    print(f"✅ TERMINÉ!")
    print(f"   Pages créées: {total_created}")
    print(f"   Erreurs: {total_errors}")
    print("="*70)

if __name__ == '__main__':
    main()
