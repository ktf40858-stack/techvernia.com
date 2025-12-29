#!/usr/bin/env python3
"""Update navigation bar with language selector for Customer Service & Support tools"""

import os
import re
import sys

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

CUSTOMER_SERVICE_DIR = 'GenuisNet.ai/pages/reviews/customer-service'

# List of all customer service tools
TOOLS = [
    'ada', 'certainly', 'cognigy', 'drift', 'forethought', 'freshdesk-ai',
    'helpshift', 'intercom-fin', 'kustomer', 'liveperson', 'netomi',
    'polyai', 'ultimateai', 'yellowai', 'zendesk-ai'
]

# Complete navigation with language selector
NEW_NAVIGATION = '''<nav class="navbar" id="navbar">
    <div class="nav-container">
        <a class="logo" href="../../../index.html">
            <img alt="GenuisNet.ai" src="../../../assets/images/logo-neon.svg" style="height: 50px; width: auto;"/>
        </a>
        <ul class="nav-menu" id="nav-menu">
            <li class="nav-item">
                <a class="nav-link" href="../../../index.html" data-i18n="nav.home">Home</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="../../../guides.html" data-i18n="nav.guides">Guides</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="../../../compare.html" data-i18n="nav.compare">Compare</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="../../../about.html" data-i18n="nav.about">About</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="../../../blog.html">Blog</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="../../../contact.html" data-i18n="nav.contact">Contact</a>
            </li>
        </ul>
        <div class="nav-actions">
            <div class="language-selector">
                <button class="lang-btn" id="lang-btn">
                    <span class="globe-icon">🌐</span>
                    <span class="lang-current" id="lang-current">EN</span>
                    <span class="dropdown-arrow">▼</span>
                </button>
                <div class="lang-dropdown" id="lang-dropdown">
                    <button class="lang-option active" data-lang="en">
                        <span class="flag">🇺🇸</span>
                        <span class="lang-name">English</span>
                    </button>
                    <button class="lang-option" data-lang="es">
                        <span class="flag">🇪🇸</span>
                        <span class="lang-name">Español</span>
                    </button>
                    <button class="lang-option" data-lang="fr">
                        <span class="flag">🇫🇷</span>
                        <span class="lang-name">Français</span>
                    </button>
                    <button class="lang-option" data-lang="de">
                        <span class="flag">🇩🇪</span>
                        <span class="lang-name">Deutsch</span>
                    </button>
                    <button class="lang-option" data-lang="pt">
                        <span class="flag">🇧🇷</span>
                        <span class="lang-name">Português</span>
                    </button>
                    <button class="lang-option" data-lang="zh">
                        <span class="flag">🇨🇳</span>
                        <span class="lang-name">中文</span>
                    </button>
                    <button class="lang-option" data-lang="ja">
                        <span class="flag">🇯🇵</span>
                        <span class="lang-name">日本語</span>
                    </button>
                    <button class="lang-option" data-lang="ko">
                        <span class="flag">🇰🇷</span>
                        <span class="lang-name">한국어</span>
                    </button>
                    <button class="lang-option" data-lang="ar">
                        <span class="flag">🇸🇦</span>
                        <span class="lang-name">العربية</span>
                    </button>
                    <button class="lang-option" data-lang="hi">
                        <span class="flag">🇮🇳</span>
                        <span class="lang-name">हिन्दी</span>
                    </button>
                </div>
            </div>
            <div class="hamburger" id="hamburger">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>
    </div>
</nav>'''

def update_navigation(html_file):
    """Replace navigation bar with complete version including language selector"""

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find and replace the navigation section
    # Pattern matches from <nav to </nav>
    nav_pattern = r'<nav class="navbar"[^>]*>.*?</nav>'

    if re.search(nav_pattern, content, re.DOTALL):
        content = re.sub(nav_pattern, NEW_NAVIGATION, content, flags=re.DOTALL)

        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False

print("=" * 70)
print("CUSTOMER SERVICE & SUPPORT - NAVIGATION UPDATE")
print("=" * 70)

updated = 0
failed = 0

for tool in TOOLS:
    html_file = os.path.join(CUSTOMER_SERVICE_DIR, f'{tool}.html')

    if not os.path.exists(html_file):
        print(f"\n❌ {tool}: File not found")
        failed += 1
        continue

    try:
        if update_navigation(html_file):
            print(f"\n✅ {tool}: Navigation updated")
            updated += 1
        else:
            print(f"\n⚠️  {tool}: No navigation found to update")
            failed += 1
    except Exception as e:
        print(f"\n❌ {tool}: Error - {str(e)}")
        failed += 1

print("\n" + "=" * 70)
print(f"SUMMARY: {updated} pages updated, {failed} failed")
print("=" * 70)
