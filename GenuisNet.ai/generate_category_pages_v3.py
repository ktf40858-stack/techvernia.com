#!/usr/bin/env python3
"""
Generate modern category pages with country flags and neon SVG icons.
"""

import os
import sys

# Add the base path to import tool_countries
base_path = "/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai"
sys.path.insert(0, base_path)

from tool_countries import get_country_info

# Category configurations
categories = {
    'chatbots': {
        'title': 'AI Chatbots & Assistants',
        'description': 'Discover the most powerful AI chatbots and virtual assistants. From general-purpose tools like ChatGPT and Claude to specialized assistants - find the perfect AI companion for your needs.',
        'icon_svg': 'chatbots-neon.svg',
        'gradient': 'rgba(0, 217, 255, 0.1), rgba(102, 102, 255, 0.1)',
        'gradient_css': '#00D9FF, #6666FF',
        'keywords': 'AI chatbots, ChatGPT, Claude, Gemini, AI assistants, conversational AI',
    },
    'writing': {
        'title': 'AI Writing Tools',
        'description': 'Professional AI writing assistants for content creation, copywriting, and editing. Transform your writing with advanced AI-powered tools.',
        'icon_svg': 'writing-neon.svg',
        'gradient': 'rgba(168, 85, 247, 0.1), rgba(99, 102, 241, 0.1)',
        'gradient_css': '#A855F7, #6366F1',
        'keywords': 'AI writing, content creation, copywriting, Jasper, Copy.ai, writing assistant',
    },
    'image': {
        'title': 'AI Image Generation',
        'description': 'Create stunning visuals with AI image generators. From photorealistic art to creative designs - explore the best AI image creation tools.',
        'icon_svg': 'image-neon.svg',
        'gradient': 'rgba(244, 114, 182, 0.1), rgba(236, 72, 153, 0.1)',
        'gradient_css': '#F472B6, #EC4899',
        'keywords': 'AI image generation, Midjourney, DALL-E, Stable Diffusion, AI art, image creation',
    },
    'video': {
        'title': 'AI Video Generation & Editing',
        'description': 'Revolutionary AI video tools for creation, editing, and enhancement. Transform your video production workflow with cutting-edge AI technology.',
        'icon_svg': 'video-neon.svg',
        'gradient': 'rgba(251, 146, 60, 0.1), rgba(249, 115, 22, 0.1)',
        'gradient_css': '#FB923C, #F97316',
        'keywords': 'AI video, video generation, Runway, Synthesia, video editing, AI video creation',
    },
    'audio': {
        'title': 'AI Audio & Voice Generation',
        'description': 'Natural AI voices, music generation, and audio enhancement tools. Create professional audio content with advanced AI technology.',
        'icon_svg': 'audio-neon.svg',
        'gradient': 'rgba(74, 222, 128, 0.1), rgba(34, 197, 94, 0.1)',
        'gradient_css': '#4ADE80, #22C55E',
        'keywords': 'AI voice, text to speech, ElevenLabs, AI music, voice generation, audio AI',
    },
    'coding': {
        'title': 'AI Coding Assistants',
        'description': 'Supercharge your development with AI coding tools. From code completion to full project generation - code faster and smarter.',
        'icon_svg': 'coding-neon.svg',
        'gradient': 'rgba(56, 189, 248, 0.1), rgba(14, 165, 233, 0.1)',
        'gradient_css': '#38BDF8, #0EA5E9',
        'keywords': 'AI coding, GitHub Copilot, Cursor, code assistant, programming AI, developer tools',
    },
    'productivity': {
        'title': 'AI Productivity Tools',
        'description': 'Boost your productivity with AI automation and workflow tools. Smart assistants that help you work faster and more efficiently.',
        'icon_svg': 'productivity-neon.svg',
        'gradient': 'rgba(250, 204, 21, 0.1), rgba(234, 179, 8, 0.1)',
        'gradient_css': '#FACC15, #EAB308',
        'keywords': 'AI productivity, automation, workflow tools, AI assistant, productivity AI',
    },
    'seo': {
        'title': 'AI SEO & Marketing Tools',
        'description': 'Optimize your content and boost rankings with AI-powered SEO tools. Advanced keyword research, content optimization, and analytics.',
        'icon_svg': 'seo-neon.svg',
        'gradient': 'rgba(52, 211, 153, 0.1), rgba(16, 185, 129, 0.1)',
        'gradient_css': '#34D399, #10B981',
        'keywords': 'AI SEO, SEO tools, content optimization, keyword research, marketing AI',
    },
    'business': {
        'title': 'AI Business & Analytics',
        'description': 'Enterprise AI solutions for business intelligence, analytics, and automation. Data-driven insights for smarter business decisions.',
        'icon_svg': 'business-neon.svg',
        'gradient': 'rgba(129, 140, 248, 0.1), rgba(99, 102, 241, 0.1)',
        'gradient_css': '#818CF8, #6366F1',
        'keywords': 'AI business, business intelligence, analytics, enterprise AI, business automation',
    },
    'architecture': {
        'title': 'AI Architecture & Design',
        'description': 'Revolutionary AI tools for architects and designers. From conceptual design to 3D modeling - transform your creative workflow.',
        'icon_svg': 'architecture-neon.svg',
        'gradient': 'rgba(14, 165, 233, 0.1), rgba(56, 189, 248, 0.1)',
        'gradient_css': '#0EA5E9, #38BDF8',
        'keywords': 'AI architecture, design AI, 3D modeling, architectural design, AI CAD',
    },
    'medical': {
        'title': 'AI Medical & Healthcare',
        'description': 'Advanced AI solutions for healthcare and medical diagnostics. Cutting-edge technology improving patient care and medical research.',
        'icon_svg': 'medical-neon.svg',
        'gradient': 'rgba(59, 130, 246, 0.1), rgba(96, 165, 250, 0.1)',
        'gradient_css': '#3B82F6, #60A5FA',
        'keywords': 'AI medical, healthcare AI, medical diagnostics, AI health, medical technology',
    },
}

def get_reviews_for_category(category_name):
    """Get list of review files for a category."""
    review_path = os.path.join(base_path, f"pages/reviews/{category_name}")
    if not os.path.exists(review_path):
        return []

    reviews = []
    for filename in sorted(os.listdir(review_path)):
        if filename.endswith('.html'):
            tool_slug = filename.replace('.html', '')
            # Convert slug to title (e.g., "github-copilot" -> "GitHub Copilot")
            tool_name = tool_slug.replace('-', ' ').title()

            # Get country info
            country_info = get_country_info(tool_slug)

            reviews.append({
                'slug': tool_slug,
                'name': tool_name,
                'filename': filename,
                'country': country_info['country'],
                'flag': country_info['flag']
            })
    return reviews

def generate_category_page(category_slug, config):
    """Generate a category page HTML with country flags and neon SVG icon."""

    reviews = get_reviews_for_category(category_slug)
    tool_count = len(reviews)

    # Generate tool cards HTML
    tool_cards_html = ""
    for review in reviews:
        logo_path = f"../../assets/images/tools/{category_slug}/{review['slug']}.svg"

        tool_cards_html += f'''
                <a href="../reviews/{category_slug}/{review['filename']}" class="tool-card">
                    <div class="tool-logo">
                        <img src="{logo_path}" alt="{review['name']}" style="width: 64px; height: 64px; object-fit: contain;">
                    </div>
                    <h3>{review['name']}</h3>
                    <div class="tool-country">
                        <span class="country-flag">{review['flag']}</span>
                        <span class="country-name">{review['country']}</span>
                    </div>
                    <div class="tool-meta">
                        <span class="meta-item">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width: 14px; height: 14px;">
                                <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                            </svg>
                            <span>Full Review</span>
                        </span>
                    </div>
                </a>'''

    html_content = f'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{config['description']}">
    <meta name="keywords" content="{config['keywords']}">
    <meta name="author" content="GenuisNet.ai">
    <title>{config['title']} | GenuisNet.ai</title>
    <link rel="stylesheet" href="../../css/style.css">
    <link rel="stylesheet" href="../../css/animations.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        .category-hero {{
            padding: calc(80px + var(--space-4xl)) 0 var(--space-3xl);
            background: linear-gradient(135deg, {config['gradient']});
            border-bottom: 1px solid var(--border-color);
        }}
        .category-hero-content {{
            display: grid;
            grid-template-columns: 1fr auto;
            gap: var(--space-3xl);
            align-items: center;
        }}
        .category-icon-large {{
            width: 120px;
            height: 120px;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .category-icon-large img {{
            width: 100%;
            height: 100%;
            object-fit: contain;
        }}
        .category-hero h1 {{
            font-size: clamp(2.5rem, 5vw, 3.5rem);
            font-weight: 800;
            margin-bottom: var(--space-md);
        }}
        .category-hero p {{
            font-size: var(--text-lg);
            color: var(--text-secondary);
            max-width: 600px;
            line-height: 1.7;
        }}
        .category-stats {{
            display: flex;
            gap: var(--space-2xl);
            margin-top: var(--space-xl);
        }}
        .category-stat {{
            text-align: center;
        }}
        .category-stat-number {{
            font-size: var(--text-3xl);
            font-weight: 800;
            background: linear-gradient(135deg, {config['gradient_css']});
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .category-stat-label {{
            font-size: var(--text-sm);
            color: var(--text-tertiary);
        }}

        /* Tools Section */
        .tools-section {{
            padding: var(--space-4xl) 0;
        }}
        .tools-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: var(--space-xl);
        }}
        .tool-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-xl);
            padding: var(--space-xl);
            text-align: center;
            transition: all var(--transition-normal);
            text-decoration: none;
            color: inherit;
            display: flex;
            flex-direction: column;
            align-items: center;
        }}
        .tool-card:hover {{
            transform: translateY(-5px);
            border-color: var(--border-color-hover);
            box-shadow: var(--shadow-glow);
        }}
        .tool-logo {{
            width: 80px;
            height: 80px;
            margin-bottom: var(--space-md);
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .tool-card h3 {{
            font-size: var(--text-lg);
            font-weight: 700;
            margin-bottom: var(--space-sm);
        }}
        .tool-country {{
            display: flex;
            align-items: center;
            gap: var(--space-xs);
            margin-bottom: var(--space-sm);
            font-size: var(--text-sm);
            color: var(--text-secondary);
        }}
        .country-flag {{
            font-size: 1.2em;
        }}
        .country-name {{
            font-weight: 500;
        }}
        .tool-meta {{
            display: flex;
            gap: var(--space-sm);
            font-size: var(--text-xs);
            color: var(--text-tertiary);
            margin-top: auto;
        }}
        .meta-item {{
            display: flex;
            align-items: center;
            gap: 4px;
        }}

        @media (max-width: 768px) {{
            .category-hero-content {{
                grid-template-columns: 1fr;
                text-align: center;
            }}
            .category-icon-large {{
                margin: 0 auto;
            }}
            .tools-grid {{
                grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            }}
        }}
    </style>
</head>
<body>
    <canvas id="neural-bg"></canvas>
    <div id="particles-container"></div>

    <!-- Navigation -->
    <nav class="navbar" id="navbar">
        <div class="nav-container">
            <a href="../../index.html" class="logo">
                <img src="../../assets/images/logo-neon.svg" alt="GenuisNet.ai Logo" style="height: 40px; width: auto;">
            </a>

            <ul class="nav-menu" id="nav-menu">
                <li class="nav-item"><a href="../../index.html" class="nav-link">Home</a></li>
                <li class="nav-item"><a href="#" class="nav-link active">Categories</a></li>
                <li class="nav-item"><a href="../guides.html" class="nav-link">Guides</a></li>
                <li class="nav-item"><a href="../about.html" class="nav-link">About</a></li>
            </ul>

            <div class="nav-actions">
                <button class="theme-toggle" id="theme-toggle" aria-label="Toggle Theme">
                    <svg class="sun-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/>
                    </svg>
                    <svg class="moon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>
                    </svg>
                </button>
                <button class="menu-toggle" id="menu-toggle" aria-label="Toggle Menu">
                    <span></span>
                    <span></span>
                    <span></span>
                </button>
            </div>
        </div>
    </nav>

    <!-- Category Hero -->
    <header class="category-hero">
        <div class="container">
            <div class="category-hero-content">
                <div>
                    <h1>{config['title']}</h1>
                    <p>{config['description']}</p>
                    <div class="category-stats">
                        <div class="category-stat">
                            <div class="category-stat-number">{tool_count}</div>
                            <div class="category-stat-label">Tools Reviewed</div>
                        </div>
                        <div class="category-stat">
                            <div class="category-stat-number">4.7★</div>
                            <div class="category-stat-label">Avg Rating</div>
                        </div>
                    </div>
                </div>
                <div class="category-icon-large">
                    <img src="../../assets/images/category-icons/{config['icon_svg']}" alt="{config['title']} Icon">
                </div>
            </div>
        </div>
    </header>

    <!-- Tools Section -->
    <main class="tools-section">
        <div class="container">
            <div class="tools-grid">
                {tool_cards_html}
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <a href="../../index.html" class="footer-logo">
                        <img src="../../assets/images/logo-neon.svg" alt="GenuisNet.ai Logo" style="height: 40px; width: auto;">
                    </a>
                    <p class="footer-desc">Your trusted source for AI tool reviews, comparisons, and guides.</p>
                </div>
                <div class="footer-links">
                    <h4>Categories</h4>
                    <ul>
                        <li><a href="ai-chatbots.html">AI Chatbots</a></li>
                        <li><a href="ai-writing.html">AI Writing</a></li>
                        <li><a href="ai-image.html">AI Image</a></li>
                        <li><a href="ai-coding.html">AI Coding</a></li>
                    </ul>
                </div>
                <div class="footer-links">
                    <h4>Resources</h4>
                    <ul>
                        <li><a href="../guides.html">Guides</a></li>
                        <li><a href="../about.html">About</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p class="copyright">© 2026 GenuisNet.ai. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <script src="../../js/animations.js"></script>
    <script src="../../js/theme.js"></script>
</body>
</html>'''

    return html_content

# Generate all category pages
print("🚀 Generating category pages with neon SVG icons...\n")

for category_slug, config in categories.items():
    output_path = os.path.join(base_path, f"pages/categories/ai-{category_slug}.html")

    html_content = generate_category_page(category_slug, config)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    reviews = get_reviews_for_category(category_slug)
    print(f"✓ Generated: ai-{category_slug}.html ({len(reviews)} tools)")

print(f"\n✅ All category pages updated with neon SVG icons!")
