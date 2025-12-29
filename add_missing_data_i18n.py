#!/usr/bin/env python3
import sys, io, os, glob, re
from bs4 import BeautifulSoup

if sys.platform=='win32':
    sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

print("🔧 AJOUT DES ATTRIBUTS DATA-I18N MANQUANTS")
print("=" * 100)

hr_files = glob.glob('GenuisNet.ai/pages/reviews/hr/*.html')
fixed_count = 0

for html_file in hr_files:
    if '.backup' in html_file:
        continue

    tool_name = os.path.basename(html_file).replace('.html', '')
    print(f"\n📄 {tool_name}...")

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    changes = 0

    # 1. Rating Breakdown Labels
    replacements = [
        (r'<span class="label">Features</span>',
         f'<span class="label" data-i18n="review.{tool_name}.rating.features">Features</span>'),
        (r'<span class="label">Ease of Use</span>',
         f'<span class="label" data-i18n="review.{tool_name}.rating.ease-of-use">Ease of Use</span>'),
        (r'<span class="label">Value</span>',
         f'<span class="label" data-i18n="review.{tool_name}.rating.value">Value</span>'),
        (r'<span class="label">Support</span>',
         f'<span class="label" data-i18n="review.{tool_name}.rating.support">Support</span>'),
        (r'<span class="label">Performance</span>',
         f'<span class="label" data-i18n="review.{tool_name}.rating.performance">Performance</span>'),

        # 2. Pricing Plan Titles
        (r'<h4>Free Plan</h4>',
         f'<h4><span data-i18n="review.{tool_name}.pricing.free-plan">Free Plan</span></h4>'),
        (r'<h4>Professional \(\$29/mo\)</h4>',
         f'<h4><span data-i18n="review.{tool_name}.pricing.professional-plan">Professional</span> ($29/mo)</h4>'),
        (r'<h4>Enterprise \(Custom\)</h4>',
         f'<h4><span data-i18n="review.{tool_name}.pricing.enterprise-plan">Enterprise</span> (Custom)</h4>'),

        # 3. Quick Info Labels
        (r'<span class="stat-label">Category</span>',
         f'<span class="stat-label" data-i18n="review.{tool_name}.info.category">Category</span>'),
        (r'<span class="stat-label">Pricing</span>',
         f'<span class="stat-label" data-i18n="review.{tool_name}.info.pricing">Pricing</span>'),
        (r'<span class="stat-label">Free Trial</span>',
         f'<span class="stat-label" data-i18n="review.{tool_name}.info.free-trial">Free Trial</span>'),
        (r'<span class="stat-label">Platform</span>',
         f'<span class="stat-label" data-i18n="review.{tool_name}.info.platform">Platform</span>'),

        # 4. Stat Values
        (r'<span class="stat-value">Hr</span>',
         f'<span class="stat-value" data-i18n="review.{tool_name}.info.category-hr">HR & Recruiting</span>'),
        (r'<span class="stat-value">From Free</span>',
         f'<span class="stat-value" data-i18n="review.{tool_name}.info.pricing-from-free">From Free</span>'),
        (r'<span class="stat-value">14 days</span>',
         f'<span class="stat-value" data-i18n="review.{tool_name}.info.trial-14-days">14 days</span>'),
        (r'<span class="stat-value">Web, Mobile</span>',
         f'<span class="stat-value" data-i18n="review.{tool_name}.info.platform-web-mobile">Web, Mobile</span>'),

        # 5. Table of Contents
        (r'>Overview</a>', f' data-i18n="review.{tool_name}.toc.overview">Overview</a>'),
        (r'>Key Features</a>', f' data-i18n="review.{tool_name}.toc.key-features">Key Features</a>'),
        (r'>Pros & Cons</a>', f' data-i18n="review.{tool_name}.toc.pros-cons">Pros & Cons</a>'),
        (r'>Pricing</a>', f' data-i18n="review.{tool_name}.toc.pricing">Pricing</a>'),
        (r'>Use Cases</a>', f' data-i18n="review.{tool_name}.toc.use-cases">Use Cases</a>'),
        (r'>Comparison</a>', f' data-i18n="review.{tool_name}.toc.comparison">Comparison</a>'),
        (r'>FAQ</a>', f' data-i18n="review.{tool_name}.toc.faq">FAQ</a>'),
        (r'>Final Verdict</a>', f' data-i18n="review.{tool_name}.toc.final-verdict">Final Verdict</a>'),

        # 6. Quick Info Title
        (r'<h3>ℹ️ Quick Info</h3>',
         f'<h3 data-i18n="review.{tool_name}.sidebar.quick-info">ℹ️ Quick Info</h3>'),
        (r'<h3>📑 Table of Contents</h3>',
         f'<h3 data-i18n="review.{tool_name}.sidebar.table-of-contents">📑 Table of Contents</h3>'),
    ]

    for pattern, replacement in replacements:
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content)
            changes += 1

    if changes > 0:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✅ {changes} attributs data-i18n ajoutés")
        fixed_count += 1
    else:
        print(f"  ⏭️  Aucun changement nécessaire")

print(f"\n{'='*100}")
print(f"✅ {fixed_count} fichiers modifiés")
print(f"{'='*100}")
