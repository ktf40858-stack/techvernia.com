#!/usr/bin/env python3
"""
Site Audit Script for GenuisNet.ai
Checks all pages for icons and trial links
"""

import os
import re
from pathlib import Path

# Base directory
BASE_DIR = Path("/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai")

def audit_review_pages():
    """Audit all review pages for trial links and icons"""
    review_dir = BASE_DIR / "pages" / "reviews"
    results = {
        'total_reviews': 0,
        'missing_trial_links': [],
        'missing_icons': [],
        'by_category': {}
    }

    for category in review_dir.iterdir():
        if category.is_dir() and not category.name.startswith('.'):
            cat_name = category.name
            results['by_category'][cat_name] = {
                'total': 0,
                'files': []
            }

            for html_file in category.glob('*.html'):
                results['total_reviews'] += 1
                results['by_category'][cat_name]['total'] += 1
                results['by_category'][cat_name]['files'].append(html_file.name)

                # Read file content
                try:
                    content = html_file.read_text(encoding='utf-8')

                    # Check for trial/CTA links
                    has_trial = bool(re.search(r'(Try Free|Get Started|Start Trial|Free Trial)', content, re.IGNORECASE))
                    has_cta = bool(re.search(r'class="btn btn-primary"', content))

                    if not (has_trial or has_cta):
                        results['missing_trial_links'].append(f"{cat_name}/{html_file.name}")

                    # Check for icon/logo references
                    has_icon = bool(re.search(r'(tool-logo|assets/images/tools|\.png|\.svg)', content))

                    if not has_icon:
                        results['missing_icons'].append(f"{cat_name}/{html_file.name}")

                except Exception as e:
                    print(f"Error reading {html_file}: {e}")

    return results

def audit_category_pages():
    """Audit category pages"""
    cat_dir = BASE_DIR / "pages" / "categories"
    results = {
        'total_categories': 0,
        'categories': []
    }

    for html_file in cat_dir.glob('ai-*.html'):
        if '.bak' not in html_file.name and 'backup' not in html_file.name:
            results['total_categories'] += 1
            cat_name = html_file.stem

            try:
                content = html_file.read_text(encoding='utf-8')

                # Count tool cards
                tool_cards = len(re.findall(r'class="tool-card', content))

                results['categories'].append({
                    'name': cat_name,
                    'file': html_file.name,
                    'tool_count': tool_cards
                })

            except Exception as e:
                print(f"Error reading {html_file}: {e}")

    return results

def generate_report():
    """Generate comprehensive audit report"""
    print("=" * 80)
    print("GENUISNET.AI SITE AUDIT REPORT")
    print("=" * 80)
    print()

    # Audit reviews
    print("REVIEWING ALL REVIEW PAGES...")
    review_results = audit_review_pages()

    print(f"\n📊 REVIEW PAGES SUMMARY")
    print(f"   Total reviews: {review_results['total_reviews']}")
    print(f"   Missing trial links: {len(review_results['missing_trial_links'])}")
    print(f"   Missing icons: {len(review_results['missing_icons'])}")
    print()

    print("📁 BY CATEGORY:")
    for cat, data in sorted(review_results['by_category'].items()):
        print(f"   {cat}: {data['total']} reviews")
    print()

    if review_results['missing_trial_links']:
        print("⚠️  MISSING TRIAL LINKS:")
        for page in review_results['missing_trial_links']:
            print(f"   - {page}")
        print()

    if review_results['missing_icons']:
        print("⚠️  MISSING ICONS:")
        for page in review_results['missing_icons']:
            print(f"   - {page}")
        print()

    # Audit category pages
    print("\nREVIEWING CATEGORY PAGES...")
    cat_results = audit_category_pages()

    print(f"\n📂 CATEGORY PAGES SUMMARY")
    print(f"   Total categories: {cat_results['total_categories']}")
    print()

    print("📄 CATEGORY DETAILS:")
    for cat in sorted(cat_results['categories'], key=lambda x: x['name']):
        print(f"   {cat['name']}: {cat['tool_count']} tools")
    print()

    # Summary
    print("=" * 80)
    print("RECOMMENDATIONS")
    print("=" * 80)
    print()
    print("1. Add tool logos to assets/images/tools/[category]/")
    print("2. Update review pages to reference logo images")
    print("3. Ensure all reviews have 'Try Free' CTA buttons")
    print("4. Verify all external links work correctly")
    print("5. Add rel='nofollow sponsored' to affiliate links")
    print()
    print("✅ AUDIT COMPLETE")
    print("=" * 80)

if __name__ == "__main__":
    generate_report()
