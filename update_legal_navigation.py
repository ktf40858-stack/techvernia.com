#!/usr/bin/env python3
"""Update navigation with language selector in all Legal tool pages"""

import os
import re
import sys

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

LEGAL_DIR = 'GenuisNet.ai/pages/reviews/legal'
TOOLS = ['blue-j-legal', 'casetext', 'cocounsel', 'everlaw', 'harvey-ai', 'kira-systems', 'lawgeex', 'lex-machina', 'luminance', 'primer', 'ravel-law', 'ross-intelligence']

# Complete navigation HTML with language selector
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
                <button aria-label="Select Language" class="lang-btn" id="lang-btn">
                    <span class="lang-icon"><svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewbox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><line x1="2" x2="22" y1="12" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg></span>
                    <span class="lang-current">EN</span>
                    <svg class="chevron" fill="currentColor" viewbox="0 0 20 20">
                        <path d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" fill-rule="evenodd"></path>
                    </svg>
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
            <div class="hamburger" id="hamburger">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>
    </div>
</nav>'''

print("=" * 70)
print("UPDATING LEGAL PAGES WITH COMPLETE NAVIGATION")
print("=" * 70)

for tool in TOOLS:
    html_file = os.path.join(LEGAL_DIR, f"{tool}.html")

    if not os.path.exists(html_file):
        print(f"\n{tool}: [X] HTML file not found")
        continue

    # Read the HTML file
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find and replace the navigation section
    # Pattern to match from <nav> to </nav>
    nav_pattern = r'<nav class="navbar"[^>]*>.*?</nav>'

    match = re.search(nav_pattern, content, re.DOTALL)

    if match:
        # Replace the old navigation with new one
        new_content = content.replace(match.group(0), NEW_NAVIGATION)

        # Write back
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"\n{tool}: [OK] Navigation updated")
    else:
        print(f"\n{tool}: [ERROR] Could not find navigation section")

print("\n" + "=" * 70)
print("Navigation update complete!")
print("=" * 70)
