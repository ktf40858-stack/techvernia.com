#!/usr/bin/env python3
import sys, io, os, glob, re

if sys.platform=='win32':
    sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

print("🔧 AJOUT DATA-I18N AUX TITRES MANQUANTS")
print("=" * 100)

hr_files = glob.glob('GenuisNet.ai/pages/reviews/hr/*.html')
fixed_count = 0

for html_file in hr_files:
    if '.backup' in html_file:
        continue

    tool_name = os.path.basename(html_file).replace('.html', '')
    tool_display = tool_name.replace('-', ' ').title()

    print(f"\n📄 {tool_name}...")

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    changes = 0

    # 1. Hero Header - Title
    pattern = f'<h1>{tool_display} Review</h1>'
    replacement = f'<h1><span data-i18n="review.{tool_name}.hero.title">{tool_display} Review</span></h1>'
    if re.search(re.escape(pattern), content):
        content = content.replace(pattern, replacement)
        changes += 1

    # 2. Hero Header - Subtitle (company description)
    replacements = [
        # AI-Powered Hr Solution
        (r'<p class="company">AI-Powered Hr Solution</p>',
         f'<p class="company"><span data-i18n="review.{tool_name}.hero.subtitle">AI-Powered Hr Solution</span></p>'),

        # Top Choice badge
        (r'<span class="leader-badge">Top Choice 2026</span>',
         f'<span class="leader-badge"><span data-i18n="review.{tool_name}.hero.badge">Top Choice 2026</span></span>'),

        # Updated date
        (r'<span>Updated: December 2026</span>',
         f'<span><span data-i18n="review.{tool_name}.hero.updated">Updated</span>: December 2026</span>'),

        # AI-Powered meta
        (r'</svg></span><span>AI-Powered</span>',
         f'</svg></span><span><span data-i18n="review.{tool_name}.hero.ai-powered">AI-Powered</span></span>'),
    ]

    for pattern, replacement in replacements:
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content)
            changes += 1

    # 3. Feature Card Titles
    feature_titles = [
        ('AI-Powered Automation', 'ai-powered-automation'),
        ('Advanced Analytics', 'advanced-analytics'),
        ('Seamless Integrations', 'seamless-integrations'),
        ('Enterprise Security', 'enterprise-security'),
        ('Real-Time Collaboration', 'real-time-collaboration'),
        ('Mobile-First Design', 'mobile-first-design'),
    ]

    for title, slug in feature_titles:
        # Pattern: trouve le titre après le SVG dans le h4
        pattern = rf'(</svg>\s*)' + re.escape(title) + r'(</h4>)'
        replacement = rf'\1<span data-i18n="review.{tool_name}.feature.{slug}">{title}</span>\2'
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
