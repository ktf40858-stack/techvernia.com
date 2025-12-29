#!/usr/bin/env python3
"""Add complete navigation bar to Analytics HTML files."""
import re
from pathlib import Path

ANALYTICS_TOOLS = [
    'alteryx-ai', 'amazon-quicksight-q', 'datarobot', 'domo-ai', 'h2oai',
    'looker-ai', 'microstrategy-ai', 'mode-analytics', 'power-bi-copilot',
    'prophet-meta', 'qlik-sense-ai', 'sisense-ai', 'tableau-pulse',
    'thoughtspot', 'yellowfin-ai'
]

HTML_DIR = Path("GenuisNet.ai/pages/reviews/analytics")

# Complete navbar with all navigation links
COMPLETE_NAVBAR = '''<nav class="navbar" id="navbar">
    <div class="nav-container">
        <a class="logo" href="../../../index.html">
            <img alt="GenuisNet.ai" src="../../../assets/images/logo-neon.svg" style="height: 50px; width: auto;"/>
        </a>
        <ul class="nav-menu" id="nav-menu">
            <li class="nav-item">
                <a class="nav-link" href="../../../index.html" data-i18n="nav.home">Home</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="../../../pages/guides.html" data-i18n="nav.guides">Guides</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="../../../pages/compare.html" data-i18n="nav.compare">Compare</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="../../../pages/about.html" data-i18n="nav.about">About</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="../../../pages/blog.html" data-i18n="nav.blog">Blog</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="../../../pages/contact.html" data-i18n="nav.contact">Contact</a>
            </li>
        </ul>
        <div class="nav-actions">
            <!-- Language Selector -->
            <div class="language-selector">
                <button id="language-selector" class="language-btn" aria-label="Select Language">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="12" cy="12" r="10"></circle>
                        <line x1="2" y1="12" x2="22" y2="12"></line>
                        <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
                    </svg>
                    <span id="current-language">EN</span>
                </button>
                <div id="language-dropdown" class="language-dropdown">
                    <button data-lang="en">English</button>
                    <button data-lang="es">Español</button>
                    <button data-lang="fr">Français</button>
                    <button data-lang="de">Deutsch</button>
                    <button data-lang="pt">Português</button>
                    <button data-lang="zh">中文</button>
                    <button data-lang="ja">日本語</button>
                    <button data-lang="ko">한국어</button>
                    <button data-lang="ar">العربية</button>
                    <button data-lang="hi">हिन्दी</button>
                </div>
            </div>
        </div>
    </div>
</nav>'''

def replace_navbar(html_path):
    """Replace simple navbar with complete navbar."""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find and replace the entire <nav> section
    nav_pattern = r'<nav class="navbar"[^>]*>.*?</nav>'
    if re.search(nav_pattern, content, re.DOTALL):
        content = re.sub(nav_pattern, COMPLETE_NAVBAR, content, flags=re.DOTALL)
    else:
        print(f"[WARN] No navbar found in {html_path.name}")
        return False

    # Write back
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return True

def main():
    print("="*60)
    print("ADDING COMPLETE NAVBAR TO ANALYTICS HTML FILES")
    print("="*60)

    stats = {"updated": 0, "failed": 0}

    for tool in ANALYTICS_TOOLS:
        html_file = HTML_DIR / f"{tool}.html"

        if not html_file.exists():
            print(f"[FAIL] {tool}: HTML file not found")
            stats["failed"] += 1
            continue

        try:
            if replace_navbar(html_file):
                print(f"[OK] {tool}: Updated navbar")
                stats["updated"] += 1
            else:
                print(f"[FAIL] {tool}: Could not update navbar")
                stats["failed"] += 1
        except Exception as e:
            print(f"[FAIL] {tool}: {e}")
            stats["failed"] += 1

    print("\n" + "="*60)
    print(f"UPDATED: {stats['updated']}")
    print(f"FAILED: {stats['failed']}")
    print("="*60)

if __name__ == "__main__":
    main()
