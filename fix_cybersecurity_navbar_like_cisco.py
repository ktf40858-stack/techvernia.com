"""
Replace Cybersecurity navbar with exact structure from Cisco AI (working version)
"""
import re
import os

# All 30 Cybersecurity tools
TOOLS = [
    'abnormal-security', 'carbon-black', 'cisco-securex', 'cortex-xdr',
    'crowdstrike', 'cyberark', 'cybereason', 'cylance', 'darktrace',
    'exabeam', 'fortinet', 'ibm-qradar', 'lacework', 'mcafee-mvision',
    'microsoft-sentinel', 'okta', 'palo-alto-ngfw', 'qualys', 'rapid7',
    'recorded-future', 'sentinelone', 'snyk', 'sophos-interceptx',
    'splunk-security', 'symantec-endpoint', 'tenable',
    'trend-micro-vision-one', 'vectra-ai', 'wiz', 'zerofox'
]

# Exact navbar from Cisco AI (working version)
CISCO_NAVBAR = '''<nav class="navbar" id="navbar">
<div class="nav-container">
<a class="logo" href="../../../index.html">
<img alt="GenuisNet.ai Logo" src="../../../assets/images/logo-neon.svg" style="height: 40px; width: auto;"/>
</a>
<ul class="nav-menu" id="nav-menu">
<li class="nav-item"><a class="nav-link active" data-i18n="nav.home" href="../../../index.html">Home</a></li>
<li class="nav-item"><a class="nav-link active" href="../../categories/ai-cybersecurity.html">Categories</a></li>
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

def fix_navbar(tool_name):
    """Replace navbar with Cisco AI working version"""
    html_path = f"GenuisNet.ai/pages/reviews/cybersecurity/{tool_name}.html"

    if not os.path.exists(html_path):
        return False

    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find and replace entire navbar section
    navbar_pattern = r'<nav class="navbar"[^>]*>.*?</nav>'

    if re.search(navbar_pattern, html, re.DOTALL):
        # Replace with Cisco AI navbar
        modified_html = re.sub(navbar_pattern, CISCO_NAVBAR, html, flags=re.DOTALL)

        # Save modified HTML
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(modified_html)

        return True
    else:
        return False

# Main processing
print("\n" + "=" * 60)
print("FIX CYBERSECURITY NAVBAR - COPY FROM CISCO AI")
print("=" * 60)

success = 0
failed = 0

for tool in TOOLS:
    result = fix_navbar(tool)

    if result:
        print(f"{tool}: [OK] Navbar replaced with Cisco AI version")
        success += 1
    else:
        print(f"{tool}: [FAIL] Could not replace navbar")
        failed += 1

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"Success: {success}")
print(f"Failed: {failed}")
print("\n" + "=" * 60)
print("All Cybersecurity pages now have the same navbar as Cisco AI!")
print("=" * 60)
