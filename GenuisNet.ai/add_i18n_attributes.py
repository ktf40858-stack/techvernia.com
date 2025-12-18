#!/usr/bin/env python3
"""
Add data-i18n Attributes to All Pages
This script adds the necessary data-i18n attributes to make translations work
"""

import os
import re
from pathlib import Path

def add_nav_i18n_attributes(content):
    """Add data-i18n attributes to navigation links"""
    replacements = [
        # Navigation links
        (r'<a href="[^"]*index\.html"[^>]*class="nav-link[^"]*"[^>]*>Home</a>',
         r'<a href="index.html" class="nav-link" data-i18n="nav.home">Home</a>'),

        (r'<a href="[^"]*index\.html"[^>]*class="nav-link[^"]*"[^>]*>\s*Home\s*</a>',
         r'<a href="index.html" class="nav-link active" data-i18n="nav.home">Home</a>'),

        # Categories
        (r'(<a[^>]*class="nav-link[^"]*"[^>]*>)(Categories)(\s*<svg)',
         r'\1<span data-i18n="nav.categories">\2</span>\3'),

        (r'(<a[^>]*href="[^"]*categories\.html"[^>]*>)(Categories)(</a>)',
         r'\1<span data-i18n="nav.categories">\2</span>\3'),

        # Guides
        (r'(<a[^>]*class="nav-link[^"]*"[^>]*>)(Guides)(\s*<svg)',
         r'\1<span data-i18n="nav.guides">\2</span>\3'),

        (r'(<a[^>]*href="[^"]*guides\.html"[^>]*>)(Guides)(</a>)',
         r'\1<span data-i18n="nav.guides">\2</span>\3'),

        # Compare
        (r'(<a[^>]*href="[^"]*comparisons\.html"[^>]*>)(Compare)(</a>)',
         r'\1<span data-i18n="nav.compare">\2</span>\3'),

        # About
        (r'(<a[^>]*href="[^"]*about\.html"[^>]*>)(About)(</a>)',
         r'\1<span data-i18n="nav.about">\2</span>\3'),

        # Blog
        (r'(<a[^>]*href="[^"]*blog\.html"[^>]*>)(Blog)(</a>)',
         r'\1<span data-i18n="nav.blog">\2</span>\3'),
    ]

    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content)

    return content

def add_category_titles_i18n(content, category):
    """Add data-i18n to category titles based on the category"""

    category_map = {
        'ai-chatbots': 'cat.chatbots',
        'ai-writing': 'cat.writing',
        'ai-image': 'cat.image',
        'ai-video': 'cat.video',
        'ai-audio': 'cat.audio',
        'ai-coding': 'cat.coding',
        'ai-productivity': 'cat.productivity',
        'ai-seo': 'cat.seo',
        'ai-business': 'cat.business',
        'ai-networking': 'cat.networking',
        'ai-cybersecurity': 'cat.cybersecurity',
        'ai-architecture': 'cat.architecture',
        'ai-medical': 'cat.medical',
        'ai-analytics': 'cat.analytics',
        'ai-legal': 'cat.legal',
        'ai-customer-service': 'cat.customer-service',
        'ai-education': 'cat.education',
        'ai-sales': 'cat.sales',
        'ai-research': 'cat.research',
        'ai-hr': 'cat.hr',
        'ai-translation': 'cat.translation',
        'ai-gaming': 'cat.gaming',
        'ai-quantum': 'cat.quantum',
    }

    if category in category_map:
        i18n_key = category_map[category]

        # Add data-i18n to h1 titles if they don't have it
        if 'data-i18n' not in content:
            # Match h1 tags and add data-i18n
            content = re.sub(
                r'<h1>([^<]+)</h1>',
                f'<h1 data-i18n="{i18n_key}">\\1</h1>',
                content,
                count=1
            )

    return content

def add_common_i18n_attributes(content):
    """Add data-i18n to common elements"""

    # Common text replacements
    replacements = [
        # Stats
        (r'>(\d+)\s*Tools?(\s*Reviewed)?</div>', r' data-i18n="stats.tools">\1 Tools</div>'),
        (r'>Categories</div>', r' data-i18n="stats.categories">Categories</div>'),
        (r'>Guides</div>', r' data-i18n="stats.guides">Guides</div>'),

        # Common buttons
        (r'>Read Review</a>', r' data-i18n="btn.review">Read Review</a>'),
        (r'>Try Free</a>', r' data-i18n="btn.try">Try Free</a>'),
        (r'>Try Now</a>', r' data-i18n="btn.tryNow">Try Now</a>'),
        (r'>Learn More</a>', r' data-i18n="btn.learnMore">Learn More</a>'),
        (r'>Get Started</a>', r' data-i18n="btn.getStarted">Get Started</a>'),
        (r'>View Tools</a>', r' data-i18n="btn.viewTools">View Tools</a>'),
        (r'>Read Guide', r' data-i18n="btn.read">Read Guide'),

        # Footer
        (r'>Privacy Policy</a>', r' data-i18n="footer.privacy">Privacy Policy</a>'),
        (r'>Terms of Service</a>', r' data-i18n="footer.terms">Terms of Service</a>'),
        (r'>Contact</a>', r' data-i18n="footer.contact">Contact</a>'),
    ]

    for pattern, replacement in replacements:
        # Only add if data-i18n not already present
        if not re.search(pattern.replace('>', ' data-i18n='), content):
            content = re.sub(pattern, replacement, content)

    return content

def process_html_file(file_path):
    """Process a single HTML file to add i18n attributes"""
    print(f"Processing: {file_path}")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Add navigation i18n
        content = add_nav_i18n_attributes(content)

        # Add common i18n attributes
        content = add_common_i18n_attributes(content)

        # Detect category from filename
        filename = os.path.basename(file_path)
        if filename.startswith('ai-'):
            category = filename.replace('.html', '')
            content = add_category_titles_i18n(content, category)

        # Write back if changes were made
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✅ Updated with i18n attributes")
            return True
        else:
            print(f"  ℹ️  No changes needed")
            return False

    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False

def main():
    """Main function"""
    print("=" * 70)
    print("Adding data-i18n Attributes to Enable Translations")
    print("=" * 70)

    updated_count = 0
    total_count = 0

    # Process index.html (though it should already have them)
    if os.path.exists('index.html'):
        total_count += 1
        if process_html_file('index.html'):
            updated_count += 1

    # Process all pages
    for root, dirs, files in os.walk('pages'):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                total_count += 1
                if process_html_file(file_path):
                    updated_count += 1

    print("\n" + "=" * 70)
    print(f"✅ Complete! Updated {updated_count} out of {total_count} files")
    print("=" * 70)

    print("\n📝 Summary:")
    print(f"  - Navigation links now have data-i18n attributes")
    print(f"  - Category titles now have data-i18n attributes")
    print(f"  - Common buttons and links now have data-i18n attributes")
    print(f"\n🎯 Next: Open any page and test the language selector!")

if __name__ == '__main__':
    main()
