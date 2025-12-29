"""
Add language selector to Networking category navbar
"""
import re

tools = [
    'ansible', 'cisco-ai', 'datadog', 'juniper-mist',
    'prtg', 'splunk', 'terraform', 'zabbix'
]

# Full navbar HTML with language selector and navigation
full_navbar = '''<nav class="navbar" id="navbar">
<div class="nav-container">
<a class="logo" href="../../../index.html">
<img alt="GenuisNet.ai Logo" src="../../../assets/images/logo-neon.svg" style="height: 40px; width: auto;"/>
</a>
<ul class="nav-menu" id="nav-menu">
<li class="nav-item"><a class="nav-link active" data-i18n="nav.home" href="../../../index.html">Home</a></li>
<li class="nav-item"><a class="nav-link active" href="../../categories/ai-networking.html">Categories</a></li>
<li class="nav-item"><a class="nav-link" href="../../guides.html"><span data-i18n="nav.guides">Guides</span></a></li>
<li class="nav-item"><a class="nav-link" href="../../comparisons.html"><span data-i18n="nav.compare">Compare</span></a></li>
<li class="nav-item"><a class="nav-link" href="../../about.html"><span data-i18n="nav.about">About</span></a></li>
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

for tool in tools:
    html_path = f'GenuisNet.ai/pages/reviews/networking/{tool}.html'

    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Replace the navbar
    pattern = r'<nav class="navbar" id="navbar">.*?</nav>'
    html = re.sub(pattern, full_navbar, html, flags=re.DOTALL)

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f'[OK] {tool}: Added complete navbar with language selector')

print('\nAll Networking HTML files updated with language selector!')
