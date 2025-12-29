#!/usr/bin/env python3
"""
Add complete navigation bar and language selector to Gaming category HTML files
Based on the HR category navbar structure
"""

import os
import re

# Gaming HTML files
GAMING_FILES = [
    "artomatix.html",
    "charismaai.html",
    "hidden-door.html",
    "inworld-ai.html",
    "latitude-ai-dungeon.html",
    "ludoai.html",
    "promethean-ai.html",
    "rct-ai.html",
    "replika.html",
    "rosebud-ai.html",
    "scenario.html"
]

# Complete navbar HTML structure (from HR category)
NAVBAR_HTML = '''<nav class="navbar" id="navbar">
<div class="nav-container">
<a class="logo" href="../../../index.html">
<img alt="GenuisNet.ai Logo" src="../../../assets/images/logo-neon.svg" style="height: 40px; width: auto;"/>
</a>
<ul class="nav-menu" id="nav-menu">
<li class="nav-item"><a class="nav-link" href="../../../index.html"><span data-i18n="nav.home">Home</span></a></li>
<li class="nav-item"><a class="nav-link" href="../../categories/ai-gaming.html"><span data-i18n="nav.categories">Categories</span></a></li>
<li class="nav-item"><a class="nav-link" href="../../guides.html"><span data-i18n="nav.guides">Guides</span></a></li>
<li class="nav-item"><a class="nav-link" href="../../comparisons.html"><span data-i18n="nav.compare">Compare</span></a></li>
<li class="nav-item"><a class="nav-link" href="../../blog.html"><span data-i18n="nav.blog">Blog</span></a></li>
<li class="nav-item"><a class="nav-link" href="../../about.html"><span data-i18n="nav.about">About</span></a></li>
<li class="nav-item"><a class="nav-link" href="../../contact.html"><span data-i18n="nav.contact">Contact</span></a></li>
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
<span class="flag">🇵🇹</span> Português
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
<button class="menu-toggle" id="menu-toggle">
<span></span>
<span></span>
<span></span>
</button>
</div>
</div>
</nav>'''

def update_navbar(filepath):
    """Update navbar in a Gaming HTML file"""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to match the existing minimal navbar
    # From <nav class="navbar" to </nav>
    navbar_pattern = r'<nav class="navbar"[^>]*>.*?</nav>'

    # Replace the minimal navbar with the complete one
    updated_content = re.sub(navbar_pattern, NAVBAR_HTML, content, flags=re.DOTALL)

    # Also ensure nav-i18n.js script is included if not present
    if 'nav-i18n.js' not in updated_content:
        # Add nav-i18n.js before the tool-specific i18n script
        script_pattern = r'(<script src="../../../js/complete-translate\.js"></script>)'
        replacement = r'\1\n<script src="../../../js/nav-i18n.js"></script>'
        updated_content = re.sub(script_pattern, replacement, updated_content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    return True

def main():
    base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\pages\reviews\gaming"

    print("="*60)
    print("ADDING NAVBAR AND LANGUAGE SELECTOR TO GAMING CATEGORY")
    print("="*60)
    print()

    updated_count = 0

    for filename in GAMING_FILES:
        filepath = os.path.join(base_dir, filename)
        if not os.path.exists(filepath):
            print(f"[SKIP] File not found: {filename}")
            continue

        try:
            update_navbar(filepath)
            print(f"[OK] {filename}")
            updated_count += 1
        except Exception as e:
            print(f"[ERROR] {filename}: {str(e)}")

    print()
    print("="*60)
    print(f"FILES UPDATED: {updated_count}/{len(GAMING_FILES)}")
    print("="*60)

if __name__ == "__main__":
    main()
