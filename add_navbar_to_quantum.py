#!/usr/bin/env python3
"""
Add complete navbar with language selector to Quantum Computing HTML files
"""

import re
import os

QUANTUM_FILES = [
    "amazon-braket.html",
    "azure-quantum.html",
    "d-wave-leap.html",
    "google-cirq.html",
    "ibm-quantum.html",
    "ionq.html",
    "rigetti-qcs.html",
    "xanadu-pennylane.html"
]

COMPLETE_NAVBAR = '''<nav class="navbar" id="navbar">
<div class="nav-container">
<a class="logo" href="../../../index.html">
<img alt="GenuisNet.ai Logo" src="../../../assets/images/logo-neon.svg" style="height: 40px; width: auto;"/>
</a>
<ul class="nav-menu" id="nav-menu">
<li class="nav-item"><a class="nav-link" href="../../../index.html"><span data-i18n="nav.home">Home</span></a></li>
<li class="nav-item"><a class="nav-link" href="../../categories/ai-quantum.html"><span data-i18n="nav.categories">Categories</span></a></li>
<li class="nav-item"><a class="nav-link" href="../../guides.html"><span data-i18n="nav.guides">Guides</span></a></li>
<li class="nav-item"><a class="nav-link" href="../../blog.html"><span data-i18n="nav.blog">Blog</span></a></li>
<li class="nav-item"><a class="nav-link" href="../../about.html"><span data-i18n="nav.about">About</span></a></li>
</ul>
<div class="nav-actions">
<div class="language-selector">
<button aria-label="Select Language" class="lang-btn" id="lang-btn">
<span class="lang-current">EN</span>
<svg class="chevron-icon" fill="none" height="16" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="16">
<polyline points="6 9 12 15 18 9"></polyline>
</svg>
</button>
<div class="lang-dropdown" id="lang-dropdown">
<button class="lang-option active" data-lang="en">🇺🇸 English</button>
<button class="lang-option" data-lang="fr">🇫🇷 Français</button>
<button class="lang-option" data-lang="de">🇩🇪 Deutsch</button>
<button class="lang-option" data-lang="es">🇪🇸 Español</button>
<button class="lang-option" data-lang="pt">🇵🇹 Português</button>
<button class="lang-option" data-lang="zh">🇨🇳 中文</button>
<button class="lang-option" data-lang="ja">🇯🇵 日本語</button>
<button class="lang-option" data-lang="ko">🇰🇷 한국어</button>
<button class="lang-option" data-lang="ar">🇸🇦 العربية</button>
<button class="lang-option" data-lang="hi">🇮🇳 हिन्दी</button>
</div>
</div>
<button class="hamburger" id="hamburger">
<span></span>
<span></span>
<span></span>
</button>
</div>
</div>
</nav>'''

def add_complete_navbar(html_path):
    """Replace minimal navbar with complete navbar"""

    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Pattern to match the minimal navbar
    pattern = r'<nav class="navbar" id="navbar">.*?</nav>'

    # Replace with complete navbar
    content = re.sub(pattern, COMPLETE_NAVBAR, content, flags=re.DOTALL)

    if content != original_content:
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False

def main():
    html_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\pages\reviews\quantum"

    print("="*60)
    print("ADDING COMPLETE NAVBAR TO QUANTUM COMPUTING CATEGORY")
    print("="*60)
    print()

    updated = 0

    for html_file in QUANTUM_FILES:
        html_path = os.path.join(html_dir, html_file)

        if not os.path.exists(html_path):
            print(f"[SKIP] File not found: {html_file}")
            continue

        if add_complete_navbar(html_path):
            print(f"[OK] {html_file}: Navbar updated")
            updated += 1
        else:
            print(f"[NO CHANGE] {html_file}")

    print()
    print("="*60)
    print(f"TOTAL FILES UPDATED: {updated}/{len(QUANTUM_FILES)}")
    print("="*60)
    print()
    print("Complete navbar with language selector added!")

if __name__ == "__main__":
    main()
