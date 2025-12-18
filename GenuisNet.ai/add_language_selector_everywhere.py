#!/usr/bin/env python3
"""
Add Language Selector to All Pages
This script adds the language selector and i18n support to all HTML pages in the site
"""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup

# Language selector HTML (to be inserted)
LANGUAGE_SELECTOR_HTML = '''                <!-- Language Selector -->
                <div class="language-selector">
                    <button class="lang-btn" id="lang-btn" aria-label="Select Language">
                        <span class="lang-icon">🌐</span>
                        <span class="lang-current">EN</span>
                        <svg class="chevron" viewBox="0 0 20 20" fill="currentColor">
                            <path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"/>
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
'''

def get_relative_path(file_path):
    """Get the relative path depth for a file (to calculate ../../)"""
    depth = len(Path(file_path).relative_to('.').parts) - 1
    return '../' * depth if depth > 0 else './'

def add_i18n_script(html_content, file_path):
    """Add i18n.js script to HTML if not present"""
    if 'i18n.js' in html_content:
        return html_content

    relative_path = get_relative_path(file_path)
    script_tag = f'    <script src="{relative_path}js/i18n.js"></script>'

    # Add before closing </body> tag
    if '</body>' in html_content:
        html_content = html_content.replace('</body>', f'{script_tag}\n</body>')

    return html_content

def add_language_selector(html_content, file_path):
    """Add language selector to navigation if not present"""
    # Check if already has language selector
    if 'language-selector' in html_content or 'lang-btn' in html_content:
        print(f"  ✓ Language selector already exists")
        return html_content

    # Find nav-actions div
    nav_actions_pattern = r'<div class="nav-actions">'

    if re.search(nav_actions_pattern, html_content):
        # Insert language selector after nav-actions opening tag
        html_content = re.sub(
            r'(<div class="nav-actions">)',
            r'\1\n' + LANGUAGE_SELECTOR_HTML,
            html_content,
            count=1
        )
        print(f"  ✓ Added language selector to nav-actions")
        return html_content

    # If no nav-actions, try to add it before hamburger menu or at end of nav
    hamburger_pattern = r'(<button class="hamburger")'
    if re.search(hamburger_pattern, html_content):
        nav_actions_with_selector = f'''
            <div class="nav-actions">
{LANGUAGE_SELECTOR_HTML}
            </div>

            '''
        html_content = re.sub(
            hamburger_pattern,
            nav_actions_with_selector + r'\1',
            html_content,
            count=1
        )
        print(f"  ✓ Created nav-actions and added language selector")
        return html_content

    print(f"  ⚠ Could not find suitable location for language selector")
    return html_content

def process_html_file(file_path):
    """Process a single HTML file"""
    print(f"\nProcessing: {file_path}")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Add language selector
        content = add_language_selector(content, file_path)

        # Add i18n script
        content = add_i18n_script(content, file_path)

        # Only write if changes were made
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✅ Updated successfully")
        else:
            print(f"  ℹ️  No changes needed")

    except Exception as e:
        print(f"  ❌ Error: {e}")

def main():
    """Main function to process all HTML files"""
    print("=" * 60)
    print("Adding Language Selector to All Pages")
    print("=" * 60)

    # Skip index.html as it already has the selector
    files_to_process = []

    # Find all HTML files in pages directory
    for root, dirs, files in os.walk('pages'):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                files_to_process.append(file_path)

    print(f"\nFound {len(files_to_process)} HTML files to process")

    # Process each file
    for file_path in sorted(files_to_process):
        process_html_file(file_path)

    print("\n" + "=" * 60)
    print(f"✅ Processing complete! Updated {len(files_to_process)} files")
    print("=" * 60)

    print("\n📝 Next steps:")
    print("1. Add data-i18n attributes to text elements")
    print("2. Test language switching on different pages")
    print("3. Verify all translations are working")

if __name__ == '__main__':
    main()
