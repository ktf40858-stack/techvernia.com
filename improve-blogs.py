#!/usr/bin/env python3
"""
Blog Articles Improvement Script
Applies CSS styling and content structure from reference article to all blog posts
"""

import re
import os
from pathlib import Path

# Configuration
BLOG_DIR = Path("GenuisNet.ai/pages/blog")
REFERENCE_FILE = BLOG_DIR / "chatgpt-vs-claude-subscription.html"

# CSS Template to inject
BLOG_CSS_TEMPLATE = """    <style>
        .article-hero {
            padding: calc(80px + var(--space-4xl)) 0 var(--space-3xl);
            background: var(--bg-secondary);
            border-bottom: 1px solid var(--border-color);
        }
        .article-title {
            font-size: clamp(2rem, 5vw, 3rem);
            font-weight: 800;
            line-height: 1.2;
            margin-bottom: var(--space-lg);
        }
        .article-excerpt {
            font-size: var(--text-lg);
            color: var(--text-secondary);
            line-height: 1.7;
            max-width: 700px;
        }
        .article-content {
            padding: var(--space-3xl) 0;
        }
        .article-body {
            max-width: 800px;
            margin: 0 auto;
        }
        .article-body h2 {
            font-size: var(--text-2xl);
            font-weight: 700;
            margin: var(--space-3xl) 0 var(--space-lg);
            padding-top: var(--space-lg);
            border-top: 1px solid var(--border-color);
        }
        .article-body h3 {
            font-size: var(--text-xl);
            font-weight: 600;
            margin: var(--space-2xl) 0 var(--space-md);
        }
        .article-body p {
            font-size: var(--text-base);
            line-height: 1.8;
            color: var(--text-secondary);
            margin-bottom: var(--space-lg);
        }
        .article-body ul, .article-body ol {
            margin-bottom: var(--space-lg);
            padding-left: var(--space-xl);
        }
        .article-body li {
            font-size: var(--text-base);
            line-height: 1.8;
            color: var(--text-secondary);
            margin-bottom: var(--space-sm);
        }
        .comparison-table {
            width: 100%;
            border-collapse: collapse;
            margin: var(--space-2xl) 0;
            border-radius: var(--radius-lg);
            overflow: hidden;
            border: 1px solid var(--border-color);
        }
        .comparison-table th,
        .comparison-table td {
            padding: var(--space-md) var(--space-lg);
            text-align: left;
            border-bottom: 1px solid var(--border-color);
        }
        .comparison-table th {
            background: var(--bg-secondary);
            font-weight: 600;
            color: var(--text-primary);
        }
        .comparison-table td {
            color: var(--text-secondary);
        }
        .comparison-table tr:last-child td {
            border-bottom: none;
        }
        .check-icon { color: var(--accent-success); }
        .cross-icon { color: var(--accent-error); }
        .winner {
            background: rgba(16, 185, 129, 0.1);
            color: #10b981;
            font-weight: 600;
        }

        /* Affiliate CTA Box */
        .affiliate-box {
            background: linear-gradient(135deg, rgba(0, 217, 255, 0.1) 0%, rgba(124, 58, 237, 0.1) 100%);
            border: 2px solid var(--accent-primary);
            border-radius: var(--radius-xl);
            padding: var(--space-2xl);
            margin: var(--space-2xl) 0;
            text-align: center;
        }
        .affiliate-box h4 {
            font-size: var(--text-xl);
            font-weight: 700;
            margin-bottom: var(--space-sm);
        }
        .affiliate-box p {
            color: var(--text-secondary);
            margin-bottom: var(--space-lg);
        }
        .affiliate-box .btn {
            display: inline-flex;
            margin: 0 var(--space-sm);
        }

        /* Pros/Cons Box */
        .pros-cons {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: var(--space-lg);
            margin: var(--space-2xl) 0;
        }
        .pros-box, .cons-box {
            padding: var(--space-lg);
            border-radius: var(--radius-lg);
        }
        .pros-box {
            background: rgba(16, 185, 129, 0.1);
            border: 1px solid rgba(16, 185, 129, 0.3);
        }
        .cons-box {
            background: rgba(239, 68, 68, 0.1);
            border: 1px solid rgba(239, 68, 68, 0.3);
        }
        .pros-box h4, .cons-box h4 {
            font-size: var(--text-lg);
            font-weight: 600;
            margin-bottom: var(--space-md);
        }
        .pros-box h4 { color: var(--accent-success); }
        .cons-box h4 { color: var(--accent-error); }
        .pros-box li::marker { content: "[OK] "; color: var(--accent-success); }
        .cons-box li::marker { content: "✗ "; color: var(--accent-error); }

        /* Verdict Box */
        .verdict-box {
            background: var(--bg-secondary);
            border-radius: var(--radius-xl);
            padding: var(--space-2xl);
            margin: var(--space-3xl) 0;
            border-left: 4px solid var(--accent-primary);
        }
        .verdict-box h3 {
            color: var(--accent-primary);
            margin-bottom: var(--space-md);
        }

        /* Icon sizing */
        .neon-icon {
            width: 18px;
            height: 18px;
            display: inline-block;
            vertical-align: middle;
        }
        td .neon-icon {
            width: 16px;
            height: 16px;
        }

        /* Related Articles */
        .related-section {
            background: var(--bg-secondary);
            padding: var(--space-3xl) 0;
            border-top: 1px solid var(--border-color);
        }
        .related-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: var(--space-xl);
        }

        @media (max-width: 768px) {
            .pros-cons {
                grid-template-columns: 1fr;
            }
            .related-grid {
                grid-template-columns: 1fr;
            }
            .affiliate-box .btn {
                display: block;
                width: 100%;
                margin: var(--space-sm) 0;
            }
        }
    </style>"""

# Related Articles Section Template
RELATED_ARTICLES_TEMPLATE = """
    <!-- Related Articles -->
    <section class="related-section">
        <div class="container">
            <div class="section-header">
                <h2 class="section-title">Related Articles</h2>
            </div>
            <div class="related-grid">
                <article class="blog-card">
                    <div class="blog-content">
                        <h3 class="blog-title">The Rise of AI Agents: How Autonomous AI is Changing Everything</h3>
                        <a href="ai-agents-2024.html" class="blog-link">Read More →</a>
                    </div>
                </article>
                <article class="blog-card">
                    <div class="blog-content">
                        <h3 class="blog-title">ChatGPT Plus vs Claude Pro: Which Subscription is Worth It?</h3>
                        <a href="chatgpt-vs-claude-subscription.html" class="blog-link">Read More →</a>
                    </div>
                </article>
                <article class="blog-card">
                    <div class="blog-content">
                        <h3 class="blog-title">Best Free AI Coding Tools in 2026</h3>
                        <a href="free-ai-coding-tools.html" class="blog-link">Read More →</a>
                    </div>
                </article>
            </div>
        </div>
    </section>
"""

# Improved Footer Template
FOOTER_TEMPLATE = """
    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <a href="../../index.html" class="footer-logo">
                        <img alt="GenuisNet.ai Logo" src="../../assets/images/logo-neon.svg" style="height: 40px; width: auto;"/>
                    </a>
                    <p class="footer-desc">
                        Your trusted source for AI tool reviews, comparisons, and guides.
                    </p>
                </div>
                <div class="footer-links">
                    <h4>Categories</h4>
                    <ul>
                        <li><a href="../categories/ai-chatbots.html">AI Chatbots</a></li>
                        <li><a href="../categories/ai-coding.html">AI Coding</a></li>
                        <li><a href="../categories/ai-image.html">AI Image</a></li>
                    </ul>
                </div>
                <div class="footer-links">
                    <h4>Resources</h4>
                    <ul>
                        <li><a href="../guides.html">Guides</a></li>
                        <li><a href="../comparisons.html">Comparisons</a></li>
                        <li><a href="../blog.html">Blog</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p class="copyright">© 2026 GenuisNet.ai. All rights reserved.</p>
            </div>
        </div>
    </footer>
"""


def improve_blog_article(filepath):
    """Apply improvements to a single blog article"""
    print(f"Processing: {filepath.name}")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip reference file
    if filepath.name == "chatgpt-vs-claude-subscription.html":
        print(f"  [OK] Skipping reference file")
        return

    # 1. Replace/inject CSS if needed
    if '<style>' in content:
        # Replace existing style block
        content = re.sub(
            r'<style>.*?</style>',
            BLOG_CSS_TEMPLATE,
            content,
            flags=re.DOTALL
        )
        print(f"  [OK] Updated CSS styling")
    else:
        # Insert CSS before </head>
        content = content.replace('</head>', f'{BLOG_CSS_TEMPLATE}\n</head>')
        print(f"  [OK] Added CSS styling")

    # 2. Add Related Articles section if not present
    if 'related-section' not in content and '</main>' in content:
        content = content.replace('</main>', f'</main>\n{RELATED_ARTICLES_TEMPLATE}')
        print(f"  [OK] Added Related Articles section")

    # 3. Improve footer if needed
    if 'footer-grid' not in content and '<footer' in content:
        # Replace simple footer with full footer
        content = re.sub(
            r'<footer class="footer">.*?</footer>',
            FOOTER_TEMPLATE,
            content,
            flags=re.DOTALL
        )
        print(f"  [OK] Updated footer")

    # 4. Ensure proper navigation structure
    if 'nav-menu' in content and 'nav-item' not in content:
        # Improve navigation
        old_nav = r'<ul class="nav-menu"[^>]*>.*?</ul>'
        new_nav = '''<ul class="nav-menu" id="nav-menu">
                <li class="nav-item"><a href="../../index.html" class="nav-link">Home</a></li>
                <li class="nav-item"><a href="../guides.html" class="nav-link">Guides</a></li>
                <li class="nav-item"><a href="../comparisons.html" class="nav-link">Compare</a></li>
                <li class="nav-item"><a href="../blog.html" class="nav-link active">Blog</a></li>
                <li class="nav-item"><a href="../about.html" class="nav-link">About</a></li>
            </ul>'''
        content = re.sub(old_nav, new_nav, content, flags=re.DOTALL)
        print(f"  [OK] Improved navigation")

    # 5. Fix any inline styles to use proper classes
    content = content.replace(
        'style="padding: calc(80px + var(--space-4xl)) 0 var(--space-3xl); background: var(--bg-secondary);"',
        'class="article-hero"'
    )

    # 6. Ensure article body wrapper
    if 'article-body' not in content and '<article' in content:
        # Wrap content in article-body if needed
        content = re.sub(
            r'(<article[^>]*>)',
            r'\1\n            <div class="article-body">',
            content
        )
        content = re.sub(
            r'(</article>)',
            r'            </div>\n\1',
            content
        )
        print(f"  [OK] Added article-body wrapper")

    # Write improved content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  [DONE] Completed!\n")


def main():
    """Main execution function"""
    print("=" * 60)
    print("BLOG ARTICLES IMPROVEMENT SCRIPT")
    print("=" * 60)
    print()

    # Get all HTML files in blog directory
    blog_files = list(BLOG_DIR.glob("*.html"))
    blog_files = [f for f in blog_files if not f.name.endswith('.logo_backup')]

    print(f"Found {len(blog_files)} blog articles to process\n")

    # Process each file
    for filepath in sorted(blog_files):
        improve_blog_article(filepath)

    print("=" * 60)
    print("[DONE] ALL BLOG ARTICLES IMPROVED SUCCESSFULLY!")
    print("=" * 60)
    print("\nImprovements applied:")
    print("  • Complete CSS styling (pros/cons, CTAs, tables, etc.)")
    print("  • Related Articles section")
    print("  • Improved navigation")
    print("  • Professional footer")
    print("  • Icon sizing fixes")
    print("  • Responsive design")
    print("\nYou can now view the improved articles in your browser!")


if __name__ == "__main__":
    main()
