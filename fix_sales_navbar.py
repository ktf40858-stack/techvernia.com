import os
import re

base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
sales_dir = os.path.join(base_dir, "pages", "reviews", "sales")

tools = [
    "6sense",
    "apolloio",
    "attention",
    "chorusai",
    "clari",
    "conversica",
    "exceedai",
    "gong",
    "hubspot-ai",
    "insidesales",
    "lavender",
    "outreach",
    "peopleai",
    "regieai",
    "salesforce-einstein-gpt",
    "troopsai"
]

# Navbar complète avec menu et sélecteur de langue
complete_navbar = '''<nav class="navbar" id="navbar">
<div class="nav-container">
<a class="logo" href="../../../index.html">
<img alt="GenuisNet.ai Logo" src="../../../assets/images/logo-neon.svg" style="height: 40px; width: auto;"/>
</a>
<ul class="nav-menu" id="nav-menu">
<li class="nav-item"><a class="nav-link" href="../../../index.html"><span data-i18n="nav.home">Home</span></a></li>
<li class="nav-item dropdown">
<a class="nav-link dropdown-toggle" href="#"><span data-i18n="nav.categories">Categories</span></a>
<div class="dropdown-menu">
<a class="dropdown-item" href="../../../pages/reviews.html"><span data-i18n="nav.all_reviews">All Reviews</span></a>
<a class="dropdown-item" href="../../../pages/categories/chatbots.html"><span data-i18n="nav.chatbots">AI Chatbots</span></a>
<a class="dropdown-item" href="../../../pages/categories/writing.html"><span data-i18n="nav.writing">AI Writing</span></a>
<a class="dropdown-item" href="../../../pages/categories/image.html"><span data-i18n="nav.image">AI Image</span></a>
<a class="dropdown-item" href="../../../pages/categories/video.html"><span data-i18n="nav.video">AI Video</span></a>
<a class="dropdown-item" href="../../../pages/categories/coding.html"><span data-i18n="nav.coding">AI Coding</span></a>
</div>
</li>
<li class="nav-item"><a class="nav-link" href="../../../pages/guides.html"><span data-i18n="nav.guides">Guides</span></a></li>
<li class="nav-item"><a class="nav-link" href="../../../pages/news.html"><span data-i18n="nav.news">News</span></a></li>
<li class="nav-item"><a class="nav-link" href="../../../pages/about.html"><span data-i18n="nav.about">About</span></a></li>
</ul>
<div class="language-selector">
<button class="language-btn" id="language-btn">
<svg class="icon" fill="none" height="20" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="20">
<circle cx="12" cy="12" r="10"></circle>
<line x1="2" x2="22" y1="12" y2="12"></line>
<path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
</svg>
<span id="current-language">EN</span>
<svg class="chevron" fill="none" height="16" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="16">
<polyline points="6 9 12 15 18 9"></polyline>
</svg>
</button>
<div class="language-dropdown" id="language-dropdown">
<div class="language-option" data-lang="en">
<span class="flag">🇬🇧</span>
<span>English</span>
</div>
<div class="language-option" data-lang="de">
<span class="flag">🇩🇪</span>
<span>Deutsch</span>
</div>
<div class="language-option" data-lang="es">
<span class="flag">🇪🇸</span>
<span>Español</span>
</div>
<div class="language-option" data-lang="fr">
<span class="flag">🇫🇷</span>
<span>Français</span>
</div>
<div class="language-option" data-lang="pt">
<span class="flag">🇵🇹</span>
<span>Português</span>
</div>
<div class="language-option" data-lang="zh">
<span class="flag">🇨🇳</span>
<span>中文</span>
</div>
<div class="language-option" data-lang="ja">
<span class="flag">🇯🇵</span>
<span>日本語</span>
</div>
<div class="language-option" data-lang="ko">
<span class="flag">🇰🇷</span>
<span>한국어</span>
</div>
<div class="language-option" data-lang="ar">
<span class="flag">🇸🇦</span>
<span>العربية</span>
</div>
<div class="language-option" data-lang="hi">
<span class="flag">🇮🇳</span>
<span>हिन्दी</span>
</div>
</div>
</div>
<div class="hamburger" id="hamburger">
<span></span>
<span></span>
<span></span>
</div>
</div>
</nav>'''

def fix_navbar(html_file):
    """Remplace la navbar simplifiée par la navbar complète"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern pour trouver la navbar existante (simplifiée)
    pattern = r'<nav class="navbar" id="navbar">.*?</nav>'
    match = re.search(pattern, content, re.DOTALL)

    if match:
        # Remplacer par la navbar complète
        content = content[:match.start()] + complete_navbar + content[match.end():]

        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)

        return True
    else:
        print(f"  [!] Could not find navbar")
        return False

# MAIN
print("=" * 70)
print("FIXING SALES NAVBAR - ADDING FULL MENU & LANGUAGE SELECTOR")
print("=" * 70)

total_modified = 0
for tool in tools:
    html_file = os.path.join(sales_dir, f"{tool}.html")

    if os.path.exists(html_file):
        print(f"\n{tool}.html:")
        if fix_navbar(html_file):
            print(f"  [OK] Navbar updated with menu and language selector")
            total_modified += 1
    else:
        print(f"\n{tool}.html: [SKIP] File not found")

print("\n" + "=" * 70)
print(f"[COMPLETE] Modified {total_modified} files")
print("=" * 70)
