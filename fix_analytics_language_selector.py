#!/usr/bin/env python3
"""Replace language selector in Analytics files with Medical format."""
import re
from pathlib import Path

ANALYTICS_TOOLS = [
    'alteryx-ai', 'amazon-quicksight-q', 'datarobot', 'domo-ai', 'h2oai',
    'looker-ai', 'microstrategy-ai', 'mode-analytics', 'power-bi-copilot',
    'prophet-meta', 'qlik-sense-ai', 'sisense-ai', 'tableau-pulse',
    'thoughtspot', 'yellowfin-ai'
]

HTML_DIR = Path("GenuisNet.ai/pages/reviews/analytics")

# Medical-style language selector with flags
MEDICAL_STYLE_SELECTOR = '''<!-- Language Selector -->
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
            </div>'''

def replace_language_selector(html_path):
    """Replace language selector with Medical-style format."""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to match the entire language selector div
    pattern = r'<!-- Language Selector -->.*?</div>\s*</div>'

    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, MEDICAL_STYLE_SELECTOR, content, flags=re.DOTALL)
    else:
        print(f"[WARN] Could not find language selector in {html_path.name}")
        return False

    # Write back
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return True

def main():
    print("="*60)
    print("FIXING LANGUAGE SELECTOR IN ANALYTICS HTML FILES")
    print("(Using Medical-style format with flags)")
    print("="*60)

    stats = {"updated": 0, "failed": 0}

    for tool in ANALYTICS_TOOLS:
        html_file = HTML_DIR / f"{tool}.html"

        if not html_file.exists():
            print(f"[FAIL] {tool}: HTML file not found")
            stats["failed"] += 1
            continue

        try:
            if replace_language_selector(html_file):
                print(f"[OK] {tool}: Updated language selector")
                stats["updated"] += 1
            else:
                print(f"[FAIL] {tool}: Could not update selector")
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
