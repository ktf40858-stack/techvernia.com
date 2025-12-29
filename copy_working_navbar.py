import os
import re

base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
edu_dir = os.path.join(base_dir, "pages", "reviews", "education")
sales_dir = os.path.join(base_dir, "pages", "reviews", "sales")

# Navbar complète copiée de ada.html (Customer Service)
WORKING_NAVBAR = '''<nav class="navbar" id="navbar">
<div class="nav-container">
<a class="logo" href="../../../index.html">
<img alt="GenuisNet.ai Logo" src="../../../assets/images/logo-neon.svg" style="height: 40px; width: auto;"/>
</a>
<ul class="nav-menu" id="nav-menu">
<li class="nav-item"><a class="nav-link" href="../../../index.html"><span data-i18n="nav.home">Home</span></a></li>
<li class="nav-item"><a class="nav-link" href="../../categories/ai-education.html"><span data-i18n="nav.categories">Categories</span></a></li>
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

# Navbar pour Sales (lien vers ai-sales au lieu de ai-education)
WORKING_NAVBAR_SALES = WORKING_NAVBAR.replace('ai-education.html', 'ai-sales.html')

edu_tools = [
    "aleks", "carnegie-learning", "century-tech", "cognii",
    "coursera-coach", "duolingo-max", "gradescope", "khan-academy-ai",
    "knewton-alta", "querium", "quizlet-ai", "socratic-by-google",
    "squirrel-ai", "thinkster-math"
]

sales_tools = [
    "6sense", "apolloio", "attention", "chorusai", "clari", "conversica",
    "exceedai", "gong", "hubspot-ai", "insidesales", "lavender", "outreach",
    "peopleai", "regieai", "salesforce-einstein-gpt", "troopsai"
]

def replace_navbar(html_file, new_navbar):
    """Remplace la navbar existante par la navbar fonctionnelle"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern pour trouver toute la navbar (de <nav jusqu'à </nav>)
    pattern = r'<nav class="navbar"[^>]*>.*?</nav>'
    match = re.search(pattern, content, re.DOTALL)

    if match:
        # Remplacer la navbar existante
        content = content[:match.start()] + new_navbar + content[match.end():]

        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)

        return True
    else:
        print(f"  [!] Navbar not found")
        return False

# MAIN
print("=" * 70)
print("COPYING WORKING NAVBAR FROM CUSTOMER SERVICE CATEGORY")
print("=" * 70)

print("\n[1/2] Updating Education tools...")
edu_count = 0
for tool in edu_tools:
    html_file = os.path.join(edu_dir, f"{tool}.html")
    if os.path.exists(html_file):
        if replace_navbar(html_file, WORKING_NAVBAR):
            print(f"  [OK] {tool}.html")
            edu_count += 1
    else:
        print(f"  [SKIP] {tool}.html not found")

print(f"\nEducation: {edu_count}/{len(edu_tools)} updated")

print("\n[2/2] Updating Sales tools...")
sales_count = 0
for tool in sales_tools:
    html_file = os.path.join(sales_dir, f"{tool}.html")
    if os.path.exists(html_file):
        if replace_navbar(html_file, WORKING_NAVBAR_SALES):
            print(f"  [OK] {tool}.html")
            sales_count += 1
    else:
        print(f"  [SKIP] {tool}.html not found")

print(f"\nSales: {sales_count}/{len(sales_tools)} updated")

print("\n" + "=" * 70)
print(f"[COMPLETE] {edu_count + sales_count} files updated with working navbar")
print("=" * 70)
