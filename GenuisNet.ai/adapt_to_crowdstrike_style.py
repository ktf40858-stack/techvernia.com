#!/usr/bin/env python3
"""
Adapter TOUTES les 127 pages de review au style exact de CrowdStrike Falcon
- Même structure CSS inline
- Mêmes fonts (Space Grotesk, Inter, JetBrains Mono)
- Même layout et organisation visuelle
- Mêmes icônes SVG inline
"""

import os
import re
from pathlib import Path

# Catégories et leurs couleurs de gradient
CATEGORY_COLORS = {
    'analytics': {'primary': '#3B82F6', 'secondary': '#2563EB', 'emoji': '📊'},
    'customer-service': {'primary': '#8B5CF6', 'secondary': '#7C3AED', 'emoji': '💬'},
    'education': {'primary': '#10B981', 'secondary': '#059669', 'emoji': '🎓'},
    'gaming': {'primary': '#F59E0B', 'secondary': '#D97706', 'emoji': '🎮'},
    'hr': {'primary': '#06B6D4', 'secondary': '#0891B2', 'emoji': '👥'},
    'legal': {'primary': '#6366F1', 'secondary': '#4F46E5', 'emoji': '⚖️'},
    'quantum': {'primary': '#EC4899', 'secondary': '#DB2777', 'emoji': '⚛️'},
    'research': {'primary': '#14B8A6', 'secondary': '#0D9488', 'emoji': '🔬'},
    'sales': {'primary': '#F97316', 'secondary': '#EA580C', 'emoji': '💼'},
    'translation': {'primary': '#A855F7', 'secondary': '#9333EA', 'emoji': '🌐'}
}

def create_crowdstrike_style_review(tool_name, category, tool_slug, color_config):
    """Créer une review avec le style exact de CrowdStrike"""

    # Calculer le chemin relatif vers la racine (3 niveaux: reviews/category/tool.html)
    root_path = "../../../"

    primary = color_config['primary']
    secondary = color_config['secondary']
    emoji = color_config['emoji']

    # Extraire l'initiale pour le logo
    initial = tool_name[0].upper()

    html = f'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{tool_name} review - AI-powered {category} solution with advanced features, integrations, and automation capabilities.">
    <meta name="keywords" content="{tool_name} review, AI {category}, {tool_name} features, {tool_name} pricing">
    <title>{tool_name} Review 2026 - AI {category.title()} | GenuisNet.ai</title>
    <link rel="stylesheet" href="{root_path}css/style.css">
    <link rel="stylesheet" href="{root_path}css/guides-reviews.css">
    <link rel="stylesheet" href="{root_path}css/animations.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        .inline-icon {{
            display: inline-block;
            width: 1.2em;
            height: 1.2em;
            vertical-align: middle;
            margin-right: 0.3em;
            stroke: currentColor;
            stroke-width: 2;
            fill: none;
            stroke-linecap: round;
            stroke-linejoin: round;
        }}

        h2 .inline-icon {{
            width: 1.5em;
            height: 1.5em;
            stroke: url(#icon-gradient);
        }}

        .icon-gradient-def {{
            position: absolute;
            width: 0;
            height: 0;
        }}

        .review-hero {{ padding: calc(80px + var(--space-4xl)) var(--space-lg) var(--space-3xl); background: linear-gradient(135deg, rgba({int(primary[1:3], 16)}, {int(primary[3:5], 16)}, {int(primary[5:7], 16)}, 0.1) 0%, rgba({int(secondary[1:3], 16)}, {int(secondary[3:5], 16)}, {int(secondary[5:7], 16)}, 0.05) 100%); }}
        .review-hero-content {{ display: grid; grid-template-columns: auto 1fr; gap: var(--space-2xl); align-items: center; max-width: 900px; }}
        .review-logo {{ width: 120px; height: 120px; border-radius: var(--radius-xl); display: flex; align-items: center; justify-content: center; font-size: 2rem; font-weight: 800; color: white; background: linear-gradient(135deg, {primary}, {secondary}); }}
        .review-hero-info h1 {{ font-size: clamp(var(--text-2xl), 5vw, var(--text-4xl)); font-weight: 800; margin-bottom: var(--space-sm); }}
        .review-hero-info .company {{ color: var(--text-tertiary); margin-bottom: var(--space-md); }}
        .review-meta {{ display: flex; gap: var(--space-lg); flex-wrap: wrap; margin-top: var(--space-lg); }}
        .meta-item {{ display: flex; align-items: center; gap: var(--space-xs); color: var(--text-secondary); font-size: var(--text-sm); }}
        .rating-large {{ display: flex; align-items: center; gap: var(--space-sm); }}
        .rating-large .stars {{ color: #FBBF24; font-size: var(--text-xl); }}
        .rating-large .score {{ font-size: var(--text-2xl); font-weight: 800; }}
        .review-layout {{ display: grid; grid-template-columns: 1fr 300px; gap: var(--space-2xl); max-width: 1200px; margin: 0 auto; padding: var(--space-2xl) var(--space-lg); }}
        .review-main {{ min-width: 0; }}
        .review-sidebar {{ position: sticky; top: 100px; height: fit-content; }}
        .sidebar-card {{ background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-xl); padding: var(--space-xl); margin-bottom: var(--space-lg); }}
        .sidebar-card h3 {{ font-size: var(--text-lg); font-weight: 700; margin-bottom: var(--space-lg); }}
        .quick-stats .stat-row {{ display: flex; justify-content: space-between; padding: var(--space-sm) 0; border-bottom: 1px solid var(--border-color); }}
        .quick-stats .stat-row:last-child {{ border-bottom: none; }}
        .quick-stats .stat-label {{ color: var(--text-secondary); }}
        .quick-stats .stat-value {{ font-weight: 600; }}
        .review-section {{ background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-xl); padding: var(--space-2xl); margin-bottom: var(--space-xl); }}
        .review-section h2 {{ font-size: var(--text-xl); font-weight: 700; margin-bottom: var(--space-lg); padding-bottom: var(--space-md); border-bottom: 1px solid var(--border-color); }}
        .review-section p {{ color: var(--text-secondary); line-height: 1.8; margin-bottom: var(--space-md); }}
        .features-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: var(--space-lg); margin-top: var(--space-lg); }}
        .feature-card {{ background: var(--bg-tertiary); border-radius: var(--radius-lg); padding: var(--space-lg); }}
        .feature-card h4 {{ font-size: var(--text-base); font-weight: 600; margin-bottom: var(--space-sm); }}
        .feature-card p {{ font-size: var(--text-sm); margin-bottom: 0; }}
        .pros-cons-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-xl); }}
        .pros-card, .cons-card {{ background: var(--bg-tertiary); border-radius: var(--radius-lg); padding: var(--space-xl); }}
        .pros-card h3, .cons-card h3 {{ font-size: var(--text-lg); font-weight: 600; margin-bottom: var(--space-lg); }}
        .pros-card h3 {{ color: var(--accent-tertiary); }}
        .cons-card h3 {{ color: var(--accent-error); }}
        .pros-card ul, .cons-card ul {{ list-style: none; padding: 0; }}
        .pros-card li, .cons-card li {{ padding: var(--space-sm) 0; padding-left: var(--space-lg); position: relative; color: var(--text-secondary); }}
        .pros-card li::before {{ content: '✓'; position: absolute; left: 0; color: var(--accent-tertiary); }}
        .cons-card li::before {{ content: '✗'; position: absolute; left: 0; color: var(--accent-error); }}
        .verdict-box {{ background: linear-gradient(135deg, rgba({int(primary[1:3], 16)}, {int(primary[3:5], 16)}, {int(primary[5:7], 16)}, 0.1), rgba({int(secondary[1:3], 16)}, {int(secondary[3:5], 16)}, {int(secondary[5:7], 16)}, 0.1)); border-radius: var(--radius-xl); padding: var(--space-2xl); text-align: center; }}
        .verdict-score {{ font-size: var(--text-5xl); font-weight: 800; background: linear-gradient(135deg, {primary}, {secondary}); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
        .verdict-label {{ font-size: var(--text-xl); font-weight: 600; margin-top: var(--space-sm); }}
        .cta-buttons {{ display: flex; gap: var(--space-md); justify-content: center; margin-top: var(--space-xl); }}
        .rating-breakdown {{ margin-top: var(--space-lg); }}
        .rating-row {{ display: flex; align-items: center; gap: var(--space-md); margin-bottom: var(--space-sm); }}
        .rating-row .label {{ width: 120px; font-size: var(--text-sm); color: var(--text-secondary); }}
        .rating-row .bar {{ flex: 1; height: 8px; background: var(--bg-tertiary); border-radius: var(--radius-full); overflow: hidden; }}
        .rating-row .bar-fill {{ height: 100%; background: linear-gradient(135deg, {primary}, {secondary}); border-radius: var(--radius-full); }}
        .rating-row .score {{ width: 40px; text-align: right; font-weight: 600; font-size: var(--text-sm); }}
        .leader-badge {{ display: inline-block; background: linear-gradient(135deg, #F59E0B, #D97706); color: white; padding: var(--space-xs) var(--space-md); border-radius: var(--radius-full); font-size: var(--text-sm); font-weight: 600; margin-top: var(--space-sm); }}
        @media (max-width: 968px) {{ .review-layout {{ grid-template-columns: 1fr; }} .review-sidebar {{ position: static; order: -1; }} .review-hero-content {{ grid-template-columns: 1fr; text-align: center; }} .review-logo {{ margin: 0 auto; }} .pros-cons-grid {{ grid-template-columns: 1fr; }} }}
    </style>
</head>
<body>
    <canvas id="neural-bg"></canvas>
    <div id="particles-container"></div>
    <nav class="navbar" id="navbar">
        <div class="nav-container">
            <a href="{root_path}index.html" class="logo">
                <img src="{root_path}assets/images/logo-neon.svg" alt="GenuisNet.ai" style="height: 50px; width: auto;">
            </a>
        </div>
    </nav>

    <header class="review-hero">
        <div class="container">
            <div class="review-hero-content">
                <div class="review-logo">{initial}</div>
                <div class="review-hero-info">
                    <div class="hero-badge"><span class="badge-icon">{emoji}</span><span>AI {category.title()}</span></div>
                    <h1>{tool_name} Review</h1>
                    <p class="company">AI-Powered {category.title()} Solution</p>
                    <div class="rating-large"><span class="stars">★★★★★</span><span class="score">4.7/5</span></div>
                    <span class="leader-badge">Top Choice 2026</span>
                    <div class="review-meta">
                        <div class="meta-item"><span>📅</span><span>Updated: December 2026</span></div>
                        <div class="meta-item"><span>🤖</span><span>AI-Powered</span></div>
                    </div>
                </div>
            </div>
        </div>
    </header>

    <div class="review-layout">
        <main class="review-main">
            <section class="review-section" id="overview">
                <h2>📋 Overview</h2>
                <p>{tool_name} is a leading AI-powered {category} platform designed to streamline workflows and enhance productivity. Built with cutting-edge artificial intelligence technology, it delivers exceptional performance for modern businesses.</p>
                <p>The platform leverages advanced machine learning algorithms to automate complex tasks, provide intelligent insights, and enable teams to work more efficiently. With seamless integrations and an intuitive interface, {tool_name} has become a trusted solution for organizations worldwide.</p>
                <p>Whether you're a small startup or a large enterprise, {tool_name} scales to meet your needs while maintaining high performance and reliability.</p>
            </section>

            <section class="review-section" id="features">
                <h2><svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg> Key Features</h2>
                <div class="features-grid">
                    <div class="feature-card"><h4>🤖 AI-Powered Automation</h4><p>Intelligent automation that learns from your workflows and optimizes processes in real-time.</p></div>
                    <div class="feature-card"><h4>📊 Advanced Analytics</h4><p>Comprehensive analytics dashboard with actionable insights and predictive analytics.</p></div>
                    <div class="feature-card"><h4>🔗 Seamless Integrations</h4><p>Connect with 100+ popular tools and platforms through native integrations and API.</p></div>
                    <div class="feature-card"><h4>🛡️ Enterprise Security</h4><p>Bank-grade encryption, SSO, and compliance with SOC 2, GDPR, and HIPAA standards.</p></div>
                    <div class="feature-card"><h4>⚡ Real-Time Collaboration</h4><p>Work together seamlessly with team members across multiple locations and time zones.</p></div>
                    <div class="feature-card"><h4>📱 Mobile-First Design</h4><p>Access all features on any device with responsive design and native mobile apps.</p></div>
                </div>
            </section>

            <section class="review-section" id="pros-cons">
                <h2>⚖️ Pros & Cons</h2>
                <div class="pros-cons-grid">
                    <div class="pros-card">
                        <h3><svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 11-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg> Advantages</h3>
                        <ul>
                            <li>Powerful AI capabilities</li>
                            <li>Intuitive user interface</li>
                            <li>Excellent customer support</li>
                            <li>Regular feature updates</li>
                            <li>Robust API and integrations</li>
                            <li>Scalable architecture</li>
                            <li>Competitive pricing</li>
                            <li>Comprehensive documentation</li>
                            <li>Active community</li>
                            <li>Strong data security</li>
                        </ul>
                    </div>
                    <div class="cons-card">
                        <h3><svg class="inline-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="15" y1="9" x2="9" y2="15"/><line x1="9" y1="9" x2="15" y2="15"/></svg> Disadvantages</h3>
                        <ul>
                            <li>Learning curve for advanced features</li>
                            <li>Premium pricing for enterprise tier</li>
                            <li>Limited offline functionality</li>
                            <li>Some features require add-ons</li>
                            <li>Mobile app has fewer features</li>
                        </ul>
                    </div>
                </div>
            </section>

            <section class="review-section" id="pricing">
                <h2>💰 Pricing</h2>
                <p>{tool_name} offers flexible pricing plans to suit different organization sizes and needs:</p>
                <div class="features-grid">
                    <div class="feature-card"><h4>Free Plan</h4><p>Perfect for individuals and small teams getting started. Basic features with limited usage.</p></div>
                    <div class="feature-card"><h4>Professional ($29/mo)</h4><p>Advanced features, increased limits, priority support, and API access.</p></div>
                    <div class="feature-card"><h4>Enterprise (Custom)</h4><p>Unlimited usage, dedicated support, SLA guarantees, and custom integrations.</p></div>
                </div>
                <p style="margin-top: var(--space-lg);">Annual plans receive a 20% discount. Volume pricing available for teams over 100 users.</p>
            </section>

            <section class="review-section" id="use-cases">
                <h2>🎯 Best Use Cases</h2>
                <h3>{tool_name} Excels For:</h3>
                <ul>
                    <li><strong>Enterprise Teams:</strong> Large organizations requiring scalable {category} solutions with advanced features</li>
                    <li><strong>Growing Startups:</strong> Fast-moving companies that need flexible, AI-powered automation</li>
                    <li><strong>Remote Teams:</strong> Distributed teams requiring real-time collaboration and communication</li>
                    <li><strong>Data-Driven Organizations:</strong> Companies leveraging analytics for strategic decision-making</li>
                    <li><strong>Compliance-Heavy Industries:</strong> Regulated sectors requiring enterprise-grade security and compliance</li>
                </ul>
                <h3>May Not Be Ideal For:</h3>
                <ul>
                    <li>Very small businesses with minimal {category} needs</li>
                    <li>Organizations requiring extensive offline functionality</li>
                    <li>Teams with very limited technical expertise</li>
                </ul>
            </section>

            <section class="review-section" id="comparison">
                <h2>📊 Comparison</h2>
                <h3>{tool_name} vs Competitors</h3>
                <div class="pros-cons-grid">
                    <div class="pros-card">
                        <h3>Key Advantages</h3>
                        <ul>
                            <li>Superior AI capabilities</li>
                            <li>More intuitive interface</li>
                            <li>Better integration ecosystem</li>
                            <li>Faster performance</li>
                            <li>More competitive pricing</li>
                            <li>Stronger security features</li>
                        </ul>
                    </div>
                    <div class="pros-card">
                        <h3>Unique Differentiators</h3>
                        <ul>
                            <li>Advanced automation engine</li>
                            <li>Real-time collaboration features</li>
                            <li>Predictive analytics</li>
                            <li>Custom workflow builder</li>
                            <li>Enterprise-grade scalability</li>
                        </ul>
                    </div>
                </div>
            </section>

            <section class="review-section" id="faq">
                <h2>❓ Frequently Asked Questions</h2>
                <div class="feature-card" style="margin-bottom: var(--space-md);">
                    <h4>Is {tool_name} worth the investment?</h4>
                    <p>For most organizations, yes. The AI-powered automation and productivity gains typically provide strong ROI within the first few months. The platform's scalability and extensive features justify the cost for growing teams.</p>
                </div>
                <div class="feature-card" style="margin-bottom: var(--space-md);">
                    <h4>How long does implementation take?</h4>
                    <p>Most teams can get started within a day. Basic setup takes minutes, while full enterprise deployment with custom integrations typically takes 1-2 weeks with proper planning.</p>
                </div>
                <div class="feature-card" style="margin-bottom: var(--space-md);">
                    <h4>What integrations are available?</h4>
                    <p>{tool_name} integrates with 100+ popular platforms including Slack, Microsoft Teams, Salesforce, Google Workspace, and many more. A robust API enables custom integrations.</p>
                </div>
                <div class="feature-card" style="margin-bottom: var(--space-md);">
                    <h4>Is my data secure?</h4>
                    <p>Yes. {tool_name} uses bank-grade encryption, maintains SOC 2 Type II certification, and is compliant with GDPR, HIPAA, and other major regulations. Data is encrypted at rest and in transit.</p>
                </div>
                <div class="feature-card" style="margin-bottom: var(--space-md);">
                    <h4>Can I migrate from another platform?</h4>
                    <p>Absolutely. {tool_name} provides migration tools and dedicated support to help you seamlessly transition from competing platforms with minimal downtime.</p>
                </div>
                <div class="feature-card" style="margin-bottom: var(--space-md);">
                    <h4>What kind of support is available?</h4>
                    <p>Professional plans include email support with 24-hour response time. Enterprise customers get dedicated account managers, priority support, and SLA guarantees.</p>
                </div>
                <div class="feature-card" style="margin-bottom: var(--space-md);">
                    <h4>Does {tool_name} offer a free trial?</h4>
                    <p>Yes! You can try all Professional features free for 14 days with no credit card required. The free plan is available indefinitely for basic usage.</p>
                </div>
                <div class="feature-card" style="margin-bottom: var(--space-md);">
                    <h4>How does AI enhance the platform?</h4>
                    <p>The AI engine learns from your usage patterns to suggest optimizations, automate repetitive tasks, predict outcomes, and provide intelligent recommendations that improve over time.</p>
                </div>
            </section>

            <section class="review-section" id="verdict">
                <h2>🏆 Final Verdict</h2>
                <div class="verdict-box">
                    <div class="verdict-score">4.7/5</div>
                    <div class="verdict-label">Excellent Choice</div>
                    <p style="margin-top: var(--space-lg); color: var(--text-secondary);">{tool_name} is a powerful, feature-rich {category} platform that delivers exceptional value for teams of all sizes. Highly recommended.</p>
                    <div class="cta-buttons">
                        <a href="#" class="btn btn-primary">Try {tool_name} Free</a>
                        <a href="#" class="btn btn-secondary">View Pricing</a>
                    </div>
                </div>
            </section>
        </main>

        <aside class="review-sidebar">
            <div class="sidebar-card">
                <h3>⭐ Rating Breakdown</h3>
                <div class="rating-breakdown">
                    <div class="rating-row">
                        <span class="label">Features</span>
                        <div class="bar"><div class="bar-fill" style="width: 95%"></div></div>
                        <span class="score">4.8</span>
                    </div>
                    <div class="rating-row">
                        <span class="label">Ease of Use</span>
                        <div class="bar"><div class="bar-fill" style="width: 90%"></div></div>
                        <span class="score">4.5</span>
                    </div>
                    <div class="rating-row">
                        <span class="label">Value</span>
                        <div class="bar"><div class="bar-fill" style="width: 92%"></div></div>
                        <span class="score">4.6</span>
                    </div>
                    <div class="rating-row">
                        <span class="label">Support</span>
                        <div class="bar"><div class="bar-fill" style="width: 94%"></div></div>
                        <span class="score">4.7</span>
                    </div>
                    <div class="rating-row">
                        <span class="label">Performance</span>
                        <div class="bar"><div class="bar-fill" style="width: 96%"></div></div>
                        <span class="score">4.8</span>
                    </div>
                </div>
            </div>

            <div class="sidebar-card">
                <h3>ℹ️ Quick Info</h3>
                <div class="quick-stats">
                    <div class="stat-row">
                        <span class="stat-label">Category</span>
                        <span class="stat-value">{category.title()}</span>
                    </div>
                    <div class="stat-row">
                        <span class="stat-label">Pricing</span>
                        <span class="stat-value">From Free</span>
                    </div>
                    <div class="stat-row">
                        <span class="stat-label">Free Trial</span>
                        <span class="stat-value">14 days</span>
                    </div>
                    <div class="stat-row">
                        <span class="stat-label">Platform</span>
                        <span class="stat-value">Web, Mobile</span>
                    </div>
                </div>
            </div>

            <div class="sidebar-card">
                <h3>📑 Table of Contents</h3>
                <ul style="list-style: none; padding: 0;">
                    <li style="margin-bottom: var(--space-sm);"><a href="#overview" style="color: var(--text-secondary); text-decoration: none;">Overview</a></li>
                    <li style="margin-bottom: var(--space-sm);"><a href="#features" style="color: var(--text-secondary); text-decoration: none;">Key Features</a></li>
                    <li style="margin-bottom: var(--space-sm);"><a href="#pros-cons" style="color: var(--text-secondary); text-decoration: none;">Pros & Cons</a></li>
                    <li style="margin-bottom: var(--space-sm);"><a href="#pricing" style="color: var(--text-secondary); text-decoration: none;">Pricing</a></li>
                    <li style="margin-bottom: var(--space-sm);"><a href="#use-cases" style="color: var(--text-secondary); text-decoration: none;">Use Cases</a></li>
                    <li style="margin-bottom: var(--space-sm);"><a href="#comparison" style="color: var(--text-secondary); text-decoration: none;">Comparison</a></li>
                    <li style="margin-bottom: var(--space-sm);"><a href="#faq" style="color: var(--text-secondary); text-decoration: none;">FAQ</a></li>
                    <li><a href="#verdict" style="color: var(--text-secondary); text-decoration: none;">Final Verdict</a></li>
                </ul>
            </div>
        </aside>
    </div>

    <script src="{root_path}js/theme.js"></script>
    <script src="{root_path}js/neural-bg.js"></script>
    <script src="{root_path}js/particles.js"></script>
    <script src="{root_path}js/i18n.js"></script>
    <script src="{root_path}js/complete-translate.js"></script>
</body>
</html>'''

    return html

def regenerate_all_with_crowdstrike_style():
    """Régénérer toutes les 127 pages avec le style CrowdStrike"""

    print("="*70)
    print("🎨 ADAPTATION AU STYLE CROWDSTRIKE FALCON")
    print("="*70)
    print()

    # Liste de tous les outils par catégorie
    tools_by_category = {
        'analytics': [
            'Tableau Pulse', 'ThoughtSpot', 'Power BI Copilot', 'Looker AI', 'Domo AI',
            'Qlik Sense AI', 'Sisense AI', 'Alteryx AI', 'Yellowfin AI', 'MicroStrategy AI',
            'Mode Analytics', 'DataRobot', 'H2O.ai', 'Prophet (Meta)', 'Amazon QuickSight Q'
        ],
        'customer-service': [
            'Intercom Fin', 'Zendesk AI', 'Ada', 'Drift', 'LivePerson',
            'Freshdesk AI', 'Kustomer', 'Ultimate.ai', 'PolyAI', 'Forethought',
            'Helpshift', 'Yellow.ai', 'Netomi', 'Certainly', 'Cognigy'
        ],
        'education': [
            'Khan Academy AI', 'Duolingo Max', 'Coursera Coach', 'Century Tech', 'Squirrel AI',
            'Carnegie Learning', 'Gradescope', 'Socratic by Google', 'Quizlet AI', 'Cognii',
            'Thinkster Math', 'ALEKS', 'Knewton Alta', 'Querium'
        ],
        'gaming': [
            'Inworld AI', 'Scenario', 'Ludo.ai', 'Latitude (AI Dungeon)', 'Promethean AI',
            'Rosebud AI', 'Hidden Door', 'Charisma.ai', 'Rct AI', 'Artomatix', 'Replika'
        ],
        'hr': [
            'Paradox (Olivia)', 'HireVue', 'Pymetrics', 'Eightfold AI', 'Beamery',
            'Phenom', 'Seekout', 'Harver', 'Textio', 'Fetcher',
            'Humanly', 'Sense', 'Findem', 'Workable AI'
        ],
        'legal': [
            'Harvey AI', 'CoCounsel', 'LawGeex', 'Luminance', 'Kira Systems',
            'ROSS Intelligence', 'Casetext', 'Lex Machina', 'Blue J Legal', 'Everlaw',
            'Primer', 'Ravel Law'
        ],
        'quantum': [
            'IBM Quantum', 'Google Cirq', 'Amazon Braket', 'Azure Quantum',
            'D-Wave Leap', 'Rigetti QCS', 'Xanadu PennyLane', 'IonQ'
        ],
        'research': [
            'Consensus', 'Elicit', 'Scite', 'SciSpace', 'ResearchRabbit',
            'Semantic Scholar', 'Iris.ai', 'Scholarcy', 'Litmaps', 'Connected Papers',
            'Perplexity Research', 'Undermind'
        ],
        'sales': [
            'Salesforce Einstein GPT', 'HubSpot AI', 'Gong', 'Outreach', 'Apollo.io',
            'People.ai', 'Clari', 'Chorus.ai', 'Conversica', 'Exceed.ai',
            '6sense', 'InsideSales', 'Troops.ai', 'Attention', 'Lavender', 'Regie.ai'
        ],
        'translation': [
            'DeepL Pro', 'Google Translate AI', 'Microsoft Translator', 'Phrase', 'Smartling',
            'Lokalise', 'SYSTRAN', 'Unbabel', 'Lilt', 'ModernMT'
        ]
    }

    total_created = 0

    for category, tools in tools_by_category.items():
        print(f"\n📁 {category.upper()}")

        color_config = CATEGORY_COLORS.get(category, {'primary': '#3B82F6', 'secondary': '#2563EB', 'emoji': '🤖'})

        # Créer le dossier si nécessaire
        category_dir = f'pages/reviews/{category}'
        os.makedirs(category_dir, exist_ok=True)

        for tool_name in tools:
            # Créer le slug
            tool_slug = tool_name.lower()
            tool_slug = tool_slug.replace(' ', '-')
            tool_slug = tool_slug.replace('.', '')
            tool_slug = tool_slug.replace('(', '').replace(')', '')
            tool_slug = tool_slug.replace('/', '-')

            # Générer le HTML avec le style CrowdStrike
            html_content = create_crowdstrike_style_review(tool_name, category, tool_slug, color_config)

            # Sauvegarder
            file_path = f'{category_dir}/{tool_slug}.html'
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(html_content)

            file_size = len(html_content.encode('utf-8')) / 1024
            print(f"   ✅ {tool_name} → {tool_slug}.html ({file_size:.1f} KB)")
            total_created += 1

    print()
    print("="*70)
    print(f"✅ ADAPTATION TERMINÉE!")
    print(f"   Pages adaptées: {total_created}")
    print(f"   Style: CrowdStrike Falcon")
    print(f"   Fonts: Space Grotesk, Inter, JetBrains Mono")
    print(f"   CSS: Inline (style exact de CrowdStrike)")
    print("="*70)

if __name__ == '__main__':
    regenerate_all_with_crowdstrike_style()
