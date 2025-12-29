#!/usr/bin/env python3
"""Add language selector to Analytics AI HTML files."""
import re
from pathlib import Path

ANALYTICS_TOOLS = [
    'alteryx-ai', 'amazon-quicksight-q', 'datarobot', 'domo-ai', 'h2oai',
    'looker-ai', 'microstrategy-ai', 'mode-analytics', 'power-bi-copilot',
    'prophet-meta', 'qlik-sense-ai', 'sisense-ai', 'tableau-pulse',
    'thoughtspot', 'yellowfin-ai'
]

HTML_DIR = Path("GenuisNet.ai/pages/reviews/analytics")

LANGUAGE_SELECTOR_HTML = '''        <!-- Language Selector -->
        <div class="language-selector">
            <button id="language-selector" class="language-btn" aria-label="Select Language">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="12" cy="12" r="10"></circle>
                    <line x1="2" y1="12" x2="22" y2="12"></line>
                    <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
                </svg>
                <span id="current-language">EN</span>
            </button>
            <div id="language-dropdown" class="language-dropdown">
                <button data-lang="en">English</button>
                <button data-lang="es">Español</button>
                <button data-lang="fr">Français</button>
                <button data-lang="de">Deutsch</button>
                <button data-lang="pt">Português</button>
                <button data-lang="zh">中文</button>
                <button data-lang="ja">日本語</button>
                <button data-lang="ko">한국어</button>
                <button data-lang="ar">العربية</button>
                <button data-lang="hi">हिन्दी</button>
            </div>
        </div>'''

def add_language_selector(html_path):
    """Add language selector to HTML file if not present."""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if already has language selector
    if 'id="language-selector"' in content:
        return False

    # Find the nav closing tag and insert before it
    if '</nav>' in content:
        content = content.replace('</nav>', f'{LANGUAGE_SELECTOR_HTML}\n    </nav>')
    else:
        print(f"[WARN] No </nav> tag found in {html_path.name}")
        return False

    # Write back
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return True

def main():
    print("="*60)
    print("ADDING LANGUAGE SELECTORS TO ANALYTICS HTML FILES")
    print("="*60)

    stats = {"added": 0, "skipped": 0, "failed": 0}

    for tool in ANALYTICS_TOOLS:
        html_file = HTML_DIR / f"{tool}.html"

        if not html_file.exists():
            print(f"[FAIL] {tool}: HTML file not found")
            stats["failed"] += 1
            continue

        try:
            if add_language_selector(html_file):
                print(f"[OK] {tool}: Added language selector")
                stats["added"] += 1
            else:
                print(f"[SKIP] {tool}: Already has language selector")
                stats["skipped"] += 1
        except Exception as e:
            print(f"[FAIL] {tool}: {e}")
            stats["failed"] += 1

    print("\n" + "="*60)
    print(f"ADDED: {stats['added']}")
    print(f"SKIPPED: {stats['skipped']}")
    print(f"FAILED: {stats['failed']}")
    print("="*60)

if __name__ == "__main__":
    main()
