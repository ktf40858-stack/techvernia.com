"""
Add language selector to all Cybersecurity HTML files
Adds complete navbar with language dropdown for 10 languages
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

# Complete navbar with language selector
NAVBAR_WITH_SELECTOR = '''<nav class="navbar" id="navbar">
        <div class="nav-container">
            <a class="logo" href="../../../index.html">
                <span class="logo-icon">🧠</span>
                <span>GeniusNet.AI</span>
            </a>

            <ul class="nav-menu" id="nav-menu">
                <li><a href="../../../index.html" data-i18n="nav.home">Home</a></li>
                <li><a href="../../../pages/about.html" data-i18n="nav.about">About</a></li>
                <li><a href="../../../pages/guides.html" data-i18n="nav.guides">Guides</a></li>
                <li><a href="../../../pages/compare.html" data-i18n="nav.compare">Compare</a></li>
            </ul>

            <div class="nav-actions">
                <!-- Language Selector -->
                <div class="language-selector">
                    <button class="language-btn" id="language-btn" aria-label="Select language">
                        <span class="globe-icon">🌐</span>
                        <span class="current-lang" id="current-lang">EN</span>
                        <span class="arrow">▼</span>
                    </button>
                    <div class="language-dropdown" id="language-dropdown">
                        <div class="language-option" data-lang="en">
                            <span class="flag">🇺🇸</span>
                            <span>English</span>
                        </div>
                        <div class="language-option" data-lang="es">
                            <span class="flag">🇪🇸</span>
                            <span>Español</span>
                        </div>
                        <div class="language-option" data-lang="fr">
                            <span class="flag">🇫🇷</span>
                            <span>Français</span>
                        </div>
                        <div class="language-option" data-lang="de">
                            <span class="flag">🇩🇪</span>
                            <span>Deutsch</span>
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
        </div>
    </nav>'''

def add_language_selector(tool_name):
    """Add language selector to HTML file"""
    html_path = f"GenuisNet.ai/pages/reviews/cybersecurity/{tool_name}.html"

    if not os.path.exists(html_path):
        return False

    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Check if language selector already exists
    if 'language-selector' in html:
        return 'already_exists'

    # Find and replace the navbar
    # Look for the opening <nav> tag and replace up to closing </nav>
    navbar_pattern = r'<nav class="navbar"[^>]*>.*?</nav>'

    if re.search(navbar_pattern, html, re.DOTALL):
        # Replace existing navbar
        modified_html = re.sub(navbar_pattern, NAVBAR_WITH_SELECTOR, html, flags=re.DOTALL)

        # Save modified HTML
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(modified_html)

        return True
    else:
        return False

def add_i18n_script(tool_name):
    """Add i18n.js script if not present"""
    html_path = f"GenuisNet.ai/pages/reviews/cybersecurity/{tool_name}.html"

    if not os.path.exists(html_path):
        return False

    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Check if i18n.js already exists
    if 'js/i18n.js' in html:
        return 'already_exists'

    # Find the pattern: tool-i18n.js followed by auto-translate.js
    # We want to insert i18n.js between them
    pattern = rf'(<script src="../../../js/{tool_name}-i18n\.js"></script>)\s*(<script src="../../../js/auto-translate\.js"></script>)'

    if re.search(pattern, html):
        # Insert i18n.js between tool-i18n.js and auto-translate.js
        replacement = r'\1\n    <script src="../../../js/i18n.js"></script>\n    \2'
        modified_html = re.sub(pattern, replacement, html)

        # Save modified HTML
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(modified_html)

        return True
    else:
        return False

# Main processing
print("\n" + "=" * 60)
print("CYBERSECURITY - ADD LANGUAGE SELECTOR")
print("=" * 60)

navbar_added = 0
navbar_existed = 0
navbar_failed = 0

script_added = 0
script_existed = 0
script_failed = 0

for tool in TOOLS:
    print(f"\n{tool}:")

    # Add language selector
    result = add_language_selector(tool)
    if result == True:
        print(f"  [OK] Language selector added")
        navbar_added += 1
    elif result == 'already_exists':
        print(f"  [SKIP] Language selector already exists")
        navbar_existed += 1
    else:
        print(f"  [FAIL] Could not add language selector")
        navbar_failed += 1

    # Add i18n.js script
    script_result = add_i18n_script(tool)
    if script_result == True:
        print(f"  [OK] i18n.js script added")
        script_added += 1
    elif script_result == 'already_exists':
        print(f"  [SKIP] i18n.js script already exists")
        script_existed += 1
    else:
        print(f"  [FAIL] Could not add i18n.js script")
        script_failed += 1

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"Language selector:")
print(f"  - Added: {navbar_added}")
print(f"  - Already existed: {navbar_existed}")
print(f"  - Failed: {navbar_failed}")

print(f"\ni18n.js script:")
print(f"  - Added: {script_added}")
print(f"  - Already existed: {script_existed}")
print(f"  - Failed: {script_failed}")

print("\n" + "=" * 60)
print("Language selector integration complete!")
print("=" * 60)
