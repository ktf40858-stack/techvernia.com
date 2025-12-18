#!/usr/bin/env python3
"""
Met à jour toutes les pages de certification avec:
- Le background exact de la page d'accueil
- La font Space Grotesk du website
- Les vrais couleurs et gradients
"""

from pathlib import Path

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return f"{int(hex_color[0:2], 16)}, {int(hex_color[2:4], 16)}, {int(hex_color[4:6], 16)}"

def create_homepage_style_page(cert_id, data):
    """Crée une page avec le style exact de la homepage"""
    
    brand_rgb = hex_to_rgb(data['c'])
    t = "\n".join([f"            <li>{x}</li>" for x in data['t']])
    r = "\n".join([f"            <li>{x}</li>" for x in data['r']])
    cr = "\n".join([f"            <li>{x}</li>" for x in data['cr']])
    o = "\n".join([f"        <p>{x}</p>" for x in data['o']])
    
    return f'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>{data['n']} - {data['v']} Certification | GenuisNet.ai</title>
    <meta name="description" content="{data['n']} certification guide from {data['v']}."/>
    <link href="../../assets/images/favicon.png" rel="icon" type="image/png"/>
    
    <!-- Google Fonts - Exact same as homepage -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    
    <style>
/* Exact colors from homepage */
:root {{
    /* Background - EXACT from style.css */
    --bg-primary: #0a0a0f;
    --bg-secondary: #12121a;
    --bg-tertiary: #1a1a25;
    --bg-card: #15151f;
    --bg-card-hover: #1c1c28;
    
    /* Text colors */
    --text-primary: #ffffff;
    --text-secondary: #a0a0b0;
    --text-tertiary: #6b6b7a;
    --text-muted: #4a4a58;
    
    /* Accent colors */
    --accent-primary: #00D9FF;
    --accent-secondary: #7C3AED;
    --accent-brand: {data['c']};
    
    /* Gradients - EXACT from homepage */
    --gradient-primary: linear-gradient(135deg, #00D9FF 0%, #7C3AED 100%);
    --gradient-bg: linear-gradient(180deg, #0a0a0f 0%, #12121a 50%, #0a0a0f 100%);
    --gradient-brand: linear-gradient(135deg, rgba({brand_rgb}, 0.2) 0%, rgba({brand_rgb}, 0.05) 100%);
    
    /* Shadows */
    --shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.3);
    --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.4);
    --shadow-lg: 0 8px 32px rgba(0, 0, 0, 0.5);
    --shadow-glow: 0 0 40px rgba(0, 217, 255, 0.15);
    
    /* Border */
    --border-color: rgba(255, 255, 255, 0.08);
    --border-color-hover: rgba(255, 255, 255, 0.15);
    
    /* Typography - EXACT from homepage */
    --font-sans: 'Space Grotesk', 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    --font-mono: 'JetBrains Mono', 'Fira Code', monospace;
    
    /* Spacing */
    --space-xs: 0.25rem;
    --space-sm: 0.5rem;
    --space-md: 1rem;
    --space-lg: 1.5rem;
    --space-xl: 2rem;
    --space-2xl: 3rem;
    --space-3xl: 4rem;
    --space-4xl: 6rem;
    
    /* Text sizes */
    --text-xs: 0.75rem;
    --text-sm: 0.875rem;
    --text-base: 1rem;
    --text-lg: 1.125rem;
    --text-xl: 1.25rem;
    --text-2xl: 1.5rem;
    --text-3xl: 2rem;
    --text-4xl: 2.5rem;
    --text-5xl: 3.5rem;
    
    /* Border radius */
    --radius-sm: 0.375rem;
    --radius-md: 0.5rem;
    --radius-lg: 0.75rem;
    --radius-xl: 1rem;
    --radius-2xl: 1.5rem;
}}

*, *::before, *::after {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}}

html {{
    scroll-behavior: smooth;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}}

body {{
    font-family: var(--font-sans);
    font-size: var(--text-base);
    line-height: 1.6;
    color: var(--text-primary);
    background-color: var(--bg-primary);
    background-image: var(--gradient-bg);
    min-height: 100vh;
    overflow-x: hidden;
}}

/* Force Space Grotesk everywhere - same as homepage */
h1, h2, h3, h4, h5, h6, p, span, a, button, div {{
    font-family: var(--font-sans);
}}

.container {{
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 var(--space-lg);
}}

/* Navbar - same style as homepage */
.navbar {{
    position: fixed;
    top: 0;
    width: 100%;
    background: rgba(10, 10, 15, 0.95);
    backdrop-filter: blur(10px);
    border-bottom: 1px solid var(--border-color);
    z-index: 1000;
    padding: var(--space-md) 0;
}}

.navbar a {{
    color: var(--accent-primary);
    text-decoration: none;
    font-weight: 600;
    font-size: var(--text-lg);
    transition: all 0.3s ease;
}}

.navbar a:hover {{
    color: var(--accent-secondary);
}}

/* Hero Section */
.cert-hero {{
    padding: calc(80px + var(--space-4xl)) var(--space-lg) var(--space-3xl);
    background: var(--gradient-brand);
    text-align: center;
    border-bottom: 1px solid var(--border-color);
}}

.cert-badge {{
    width: 200px;
    height: 200px;
    margin: 0 auto var(--space-xl);
    border-radius: var(--radius-xl);
    background: var(--bg-card);
    padding: var(--space-md);
    box-shadow: var(--shadow-glow);
    border: 1px solid var(--border-color);
}}

.cert-badge img {{
    width: 100%;
    height: 100%;
    object-fit: contain;
}}

.cert-hero h1 {{
    font-size: clamp(var(--text-3xl), 5vw, var(--text-5xl));
    font-weight: 700;
    margin-bottom: var(--space-md);
    background: var(--gradient-primary);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}}

.cert-level {{
    color: var(--accent-brand);
    font-size: var(--text-xl);
    font-weight: 600;
    margin-bottom: var(--space-lg);
}}

.cert-meta {{
    display: flex;
    gap: var(--space-xl);
    justify-content: center;
    flex-wrap: wrap;
    margin-top: var(--space-xl);
}}

.meta-item {{
    display: flex;
    align-items: center;
    gap: var(--space-sm);
    color: var(--text-secondary);
    font-size: var(--text-sm);
    background: var(--bg-card);
    padding: var(--space-sm) var(--space-lg);
    border-radius: var(--radius-full);
    border: 1px solid var(--border-color);
}}

/* Review Sections */
.review-section {{
    padding: var(--space-3xl) 0;
    border-bottom: 1px solid var(--border-color);
}}

.review-section h2 {{
    display: flex;
    align-items: center;
    gap: var(--space-md);
    font-size: var(--text-3xl);
    margin-bottom: var(--space-xl);
    color: var(--text-primary);
    font-weight: 600;
}}

.review-section h3 {{
    font-size: var(--text-xl);
    margin: var(--space-xl) 0 var(--space-md);
    color: var(--text-primary);
}}

.review-section p {{
    color: var(--text-secondary);
    line-height: 1.8;
    margin-bottom: var(--space-md);
    font-size: var(--text-lg);
}}

.review-section ul {{
    list-style: none;
    padding: 0;
}}

.review-section ul li {{
    padding: var(--space-md) 0;
    padding-left: var(--space-xl);
    color: var(--text-secondary);
    position: relative;
    font-size: var(--text-lg);
    line-height: 1.6;
}}

.review-section ul li:before {{
    content: "▹";
    position: absolute;
    left: 0;
    color: var(--accent-primary);
    font-weight: bold;
    font-size: var(--text-xl);
}}

/* Info Cards */
.info-box {{
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-lg);
    padding: var(--space-xl);
    margin: var(--space-xl) 0;
    box-shadow: var(--shadow-md);
}}

.info-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: var(--space-lg);
    margin: var(--space-xl) 0;
}}

.info-card {{
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-lg);
    padding: var(--space-xl);
    transition: all 0.3s ease;
}}

.info-card:hover {{
    background: var(--bg-card-hover);
    border-color: var(--border-color-hover);
    transform: translateY(-2px);
    box-shadow: var(--shadow-glow);
}}

.info-card h4 {{
    color: var(--accent-primary);
    font-size: var(--text-xs);
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: var(--space-sm);
    font-weight: 600;
}}

.info-card .value {{
    color: var(--text-primary);
    font-size: var(--text-2xl);
    font-weight: 700;
}}

/* Highlight Box */
.highlight-box {{
    background: var(--gradient-brand);
    border-radius: var(--radius-lg);
    border-left: 4px solid var(--accent-brand);
    padding: var(--space-xl);
    margin: var(--space-xl) 0;
    box-shadow: var(--shadow-md);
}}

.highlight-box p {{
    color: var(--text-primary);
    font-size: var(--text-lg);
}}

/* Icons */
.neon-icon {{
    width: 24px;
    height: 24px;
    stroke: var(--accent-primary);
    flex-shrink: 0;
}}

/* Footer */
footer {{
    background: var(--bg-secondary);
    border-top: 1px solid var(--border-color);
    padding: var(--space-2xl) 0;
    margin-top: var(--space-4xl);
    text-align: center;
}}

footer p {{
    color: var(--text-tertiary);
    font-size: var(--text-sm);
}}

/* Responsive */
@media (max-width: 768px) {{
    .cert-meta {{
        flex-direction: column;
        gap: var(--space-md);
    }}
    
    .info-grid {{
        grid-template-columns: 1fr;
    }}
    
    .cert-hero h1 {{
        font-size: var(--text-3xl);
    }}
}}
    </style>
</head>
<body>

<nav class="navbar">
    <div class="container">
        <a href="../../index.html">← Back to GenuisNet.ai</a>
    </div>
</nav>

<header class="cert-hero">
    <div class="container">
        <div class="cert-badge">
            <img src="../../assets/images/certifications/{data['b']}" alt="{data['n']} Badge"/>
        </div>
        <h1>{data['n']}</h1>
        <div class="cert-level">{data['l']} | {data['v']}</div>
        <p style="max-width: 800px; margin: 0 auto; color: var(--text-secondary); font-size: var(--text-xl);">{data['h']}</p>

        <div class="cert-meta">
            <div class="meta-item">
                <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                    <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                </svg>
                <span>Exam: {data['e']}</span>
            </div>
            <div class="meta-item">
                <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                    <circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>
                </svg>
                <span>{data['d']}</span>
            </div>
            <div class="meta-item">
                <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                    <line x1="12" x2="12" y1="1" y2="23"></line><path d="M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"></path>
                </svg>
                <span>{data['co']}</span>
            </div>
            <div class="meta-item">
                <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                    <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
                </svg>
                <span>Valid: {data['va']}</span>
            </div>
        </div>
    </div>
</header>

<main class="container">
    <section class="review-section">
        <h2>
            <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
                <rect height="4" rx="1" ry="1" width="8" x="8" y="2"></rect>
            </svg>
            Overview
        </h2>
{o}
    </section>

    <section class="review-section">
        <h2>
            <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
            </svg>
            Key Topics Covered
        </h2>
        <p>The {data['n']} certification covers the following key areas:</p>
        <ul>
{t}
        </ul>
    </section>

    <section class="review-section">
        <h2>
            <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
            </svg>
            Exam Information
        </h2>
        <div class="info-grid">
            <div class="info-card">
                <h4>Exam Code</h4>
                <div class="value">{data['e']}</div>
            </div>
            <div class="info-card">
                <h4>Duration</h4>
                <div class="value">{data['d']}</div>
            </div>
            <div class="info-card">
                <h4>Exam Cost</h4>
                <div class="value">{data['co']}</div>
            </div>
            <div class="info-card">
                <h4>Validity</h4>
                <div class="value">{data['va']}</div>
            </div>
        </div>
    </section>

    <section class="review-section">
        <h2>
            <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <path d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path>
            </svg>
            Study Resources
        </h2>
        <p>Recommended resources for preparing for this certification:</p>
        <ul>
{r}
        </ul>
    </section>

    <section class="review-section">
        <h2>
            <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <path d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
            </svg>
            Career Opportunities
        </h2>
        <p>This certification opens doors to the following career paths:</p>
        <ul>
{cr}
        </ul>
        <div class="info-box">
            <h3 style="color: var(--text-primary); margin-bottom: var(--space-md);">Expected Salary Range</h3>
            <p style="font-size: var(--text-3xl); color: var(--accent-primary); font-weight: 700; margin: var(--space-md) 0;">{data['s']}</p>
            <p style="color: var(--text-secondary);">Salary ranges vary by location, experience, and company size. Figures represent typical ranges in the United States market.</p>
        </div>
    </section>

    <section class="review-section">
        <h2>
            <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <path d="M9 5l7 7-7 7"></path>
            </svg>
            Next Steps
        </h2>
        <div class="highlight-box">
            <p>{data['nx']}</p>
        </div>
        <p style="margin-top: var(--space-xl);">Ready to get started? Visit the <a href="{data['u']}" style="color: var(--accent-primary); text-decoration: underline;" target="_blank" rel="noopener">{data['v']} Training Portal</a> for official training materials and exam registration.</p>
    </section>
</main>

<footer>
    <div class="container">
        <p>&copy; 2025 GenuisNet.ai. All rights reserved.</p>
        <p style="margin-top: var(--space-sm);">{data['v']} and related trademarks are property of {data['v']}.</p>
    </div>
</footer>

</body>
</html>'''

print("✅ Template créé avec le style exact de la homepage")

