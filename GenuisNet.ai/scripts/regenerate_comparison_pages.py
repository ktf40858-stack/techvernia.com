#!/usr/bin/env python3
"""
Regénère les pages de comparaison avec le style des reviews
"""

import os

# Template basé sur la structure des reviews
COMPARISON_TEMPLATE = '''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | GenuisNet.ai</title>
    <meta name="description" content="{description}">
    <meta name="keywords" content="{keywords}">

    <link rel="stylesheet" href="../../css/style.css">
    <link rel="stylesheet" href="../../css/guides-reviews.css">
    <link rel="stylesheet" href="../../css/animations.css">
    <link rel="stylesheet" href="../../css/neon-icons.css">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">

    <style>
        /* Comparison-specific styles based on review template */
        .comparison-hero {{
            padding: calc(80px + var(--space-4xl)) 0 var(--space-3xl);
            background: linear-gradient(135deg, {hero_gradient});
            border-bottom: 1px solid var(--border-color);
        }}

        .comparison-hero-content {{
            text-align: center;
            max-width: 900px;
            margin: 0 auto;
        }}

        .comparison-badge {{
            display: inline-block;
            padding: var(--space-xs) var(--space-lg);
            background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
            border-radius: var(--radius-full);
            font-size: var(--text-sm);
            font-weight: 600;
            margin-bottom: var(--space-lg);
        }}

        .comparison-hero-content h1 {{
            font-size: clamp(2rem, 5vw, 3.5rem);
            font-weight: 800;
            margin-bottom: var(--space-md);
            line-height: 1.2;
        }}

        .comparison-hero-content .subtitle {{
            font-size: var(--text-lg);
            color: var(--text-secondary);
            margin-bottom: var(--space-2xl);
        }}

        .tools-showcase {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
            gap: var(--space-lg);
            max-width: 700px;
            margin: var(--space-2xl) auto 0;
        }}

        .tool-badge {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: var(--space-lg);
            text-align: center;
            transition: all 0.3s ease;
        }}

        .tool-badge:hover {{
            border-color: var(--accent-primary);
            transform: translateY(-2px);
            box-shadow: 0 8px 24px rgba(0, 217, 255, 0.2);
        }}

        .tool-badge-name {{
            font-weight: 600;
            font-size: var(--text-sm);
            color: var(--text-primary);
        }}

        /* Content Layout */
        .comparison-content {{
            display: grid;
            grid-template-columns: 250px 1fr;
            gap: var(--space-3xl);
            padding: var(--space-4xl) 0;
            max-width: 1400px;
            margin: 0 auto;
        }}

        .comparison-sidebar {{
            position: sticky;
            top: 100px;
            height: fit-content;
        }}

        .toc-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-xl);
            padding: var(--space-xl);
        }}

        .toc-card h3 {{
            font-size: var(--text-lg);
            font-weight: 600;
            margin-bottom: var(--space-lg);
            padding-bottom: var(--space-sm);
            border-bottom: 1px solid var(--border-color);
        }}

        .toc {{
            display: flex;
            flex-direction: column;
            gap: var(--space-sm);
        }}

        .toc-link {{
            display: block;
            padding: var(--space-sm) var(--space-md);
            color: var(--text-secondary);
            text-decoration: none;
            border-radius: var(--radius-md);
            transition: all 0.2s ease;
            font-size: var(--text-sm);
        }}

        .toc-link:hover {{
            background: var(--bg-tertiary);
            color: var(--accent-primary);
        }}

        .comparison-main {{
            min-width: 0;
        }}

        .comparison-section {{
            margin-bottom: var(--space-4xl);
        }}

        .comparison-section h2 {{
            font-size: var(--text-2xl);
            font-weight: 700;
            margin-bottom: var(--space-xl);
            padding-bottom: var(--space-md);
            border-bottom: 2px solid var(--border-color);
        }}

        .comparison-section h3 {{
            font-size: var(--text-xl);
            font-weight: 600;
            margin: var(--space-2xl) 0 var(--space-lg);
            color: var(--text-primary);
        }}

        .comparison-section h4 {{
            font-size: var(--text-lg);
            font-weight: 600;
            margin: var(--space-xl) 0 var(--space-md);
            color: var(--accent-primary);
        }}

        .comparison-section p {{
            color: var(--text-secondary);
            line-height: 1.8;
            margin-bottom: var(--space-lg);
        }}

        .comparison-section ul,
        .comparison-section ol {{
            margin-bottom: var(--space-lg);
            padding-left: var(--space-xl);
        }}

        .comparison-section li {{
            color: var(--text-secondary);
            line-height: 1.7;
            margin-bottom: var(--space-sm);
        }}

        /* Tables */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: var(--space-xl) 0;
            background: var(--bg-card);
            border-radius: var(--radius-lg);
            overflow: hidden;
            border: 1px solid var(--border-color);
        }}

        th, td {{
            padding: var(--space-lg);
            text-align: left;
            border-bottom: 1px solid var(--border-color);
        }}

        th {{
            background: var(--bg-tertiary);
            font-weight: 600;
            color: var(--text-primary);
            font-size: var(--text-sm);
        }}

        td {{
            color: var(--text-secondary);
            font-size: var(--text-sm);
        }}

        tr:last-child td {{
            border-bottom: none;
        }}

        /* Callouts */
        .callout {{
            padding: var(--space-xl);
            border-radius: var(--radius-lg);
            margin: var(--space-xl) 0;
            border-left: 4px solid;
        }}

        .callout-success {{
            background: rgba(16, 185, 129, 0.1);
            border-color: #10B981;
        }}

        .callout-info {{
            background: rgba(0, 217, 255, 0.1);
            border-color: var(--accent-primary);
        }}

        .callout-warning {{
            background: rgba(245, 158, 11, 0.1);
            border-color: #F59E0B;
        }}

        .callout h4 {{
            margin: 0 0 var(--space-md) 0;
            font-size: var(--text-lg);
            font-weight: 600;
        }}

        .callout p {{
            margin: 0 0 var(--space-sm) 0;
        }}

        .callout ul {{
            margin: var(--space-md) 0 0 0;
        }}

        /* Code blocks */
        pre {{
            background: var(--bg-tertiary);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: var(--space-lg);
            overflow-x: auto;
            margin: var(--space-lg) 0;
        }}

        code {{
            font-family: var(--font-mono);
            font-size: var(--text-sm);
            color: var(--accent-primary);
        }}

        pre code {{
            color: var(--text-secondary);
        }}

        /* Responsive */
        @media (max-width: 1024px) {{
            .comparison-content {{
                grid-template-columns: 1fr;
            }}

            .comparison-sidebar {{
                position: static;
            }}
        }}
    </style>
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar">
        <div class="container nav-container">
            <a href="../../index.html" class="logo">
                <img src="../../assets/images/logo-neon.svg" alt="GenuisNet.ai Logo" style="height: 40px; width: auto;">
            </a>
            <ul class="nav-menu">
                <li><a href="../../index.html" class="nav-link">Home</a></li>
                <li><a href="../../pages/guides.html" class="nav-link">Guides</a></li>
                <li><a href="../../pages/compare.html" class="nav-link active">Compare</a></li>
                <li><a href="../../pages/about.html" class="nav-link">About</a></li>
            </ul>
        </div>
    </nav>

    <!-- Comparison Hero -->
    <section class="comparison-hero">
        <div class="container">
            <div class="comparison-hero-content">
                <div class="comparison-badge">Comparison 2025</div>
                <h1>{h1_title}</h1>
                <p class="subtitle">{subtitle}</p>

                <div class="tools-showcase">
{tools_badges}
                </div>
            </div>
        </div>
    </section>

    <!-- Comparison Content -->
    <div class="container">
        <div class="comparison-content">
            <aside class="comparison-sidebar">
                <div class="toc-card">
                    <h3>Quick Navigation</h3>
                    <nav class="toc">
                        <a href="#overview" class="toc-link">Overview</a>
                        <a href="#comparison-table" class="toc-link">Comparison Table</a>
                        <a href="#detailed-reviews" class="toc-link">Detailed Reviews</a>
                        <a href="#verdict" class="toc-link">Final Verdict</a>
                    </nav>
                </div>
            </aside>

            <main class="comparison-main">
{content}
            </main>
        </div>
    </div>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <p>&copy; 2025 GenuisNet.ai. All rights reserved.</p>
        </div>
    </footer>

    <script src="../../js/i18n.js"></script>
    <script src="../../js/main.js"></script>
</body>
</html>
'''

print("Template créé! Utilisez ce template pour régénérer les pages de comparaison.")
print("Le style est maintenant basé sur les pages de review avec le même background et organisation.")
