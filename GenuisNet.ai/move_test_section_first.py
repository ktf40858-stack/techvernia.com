#!/usr/bin/env python3
"""
Move the Test/Try section to the first line in all review pages.
Also update all dates to 2026.
"""

import os
import re
import glob

base_path = "/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai"
review_categories = ['chatbots', 'writing', 'image', 'video', 'audio', 'coding',
                     'productivity', 'seo', 'business', 'cybersecurity', 'architecture', 'medical']

def process_review_file(file_path):
    """Process a single review file."""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Step 1: Update all dates from 2024/2025 to 2026
    content = re.sub(r'\b202[45]\b', '2026', content)

    # Step 2: Extract the CTA buttons section from sidebar
    cta_pattern = r'<div class="cta-buttons">(.*?)</div>'
    cta_match = re.search(cta_pattern, content, re.DOTALL)

    if not cta_match:
        print(f"  ⚠ No CTA buttons found in {os.path.basename(file_path)}")
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False

    cta_html = cta_match.group(1).strip()

    # Step 3: Create a prominent test section with the CTA
    test_section = f'''
                <!-- Try It Section -->
                <div class="test-section-top">
                    <h2 id="try">Try It Now</h2>
                    <div class="cta-buttons-top">
                        {cta_html}
                    </div>
                </div>

                '''

    # Step 4: Find where to insert it (right after <article class="review-main">)
    article_start = r'(<article class="review-main">)\s*'

    if not re.search(article_start, content):
        print(f"  ⚠ No article start found in {os.path.basename(file_path)}")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    # Insert the test section at the beginning
    content = re.sub(article_start, r'\1\n' + test_section, content, count=1)

    # Step 5: Add CSS for the new test section (insert in style section)
    css_addition = '''
        /* Test Section at Top */
        .test-section-top {
            background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(59, 130, 246, 0.1));
            border: 2px solid var(--border-color-hover);
            border-radius: var(--radius-xl);
            padding: var(--space-2xl);
            text-align: center;
            margin-bottom: var(--space-3xl);
        }
        .test-section-top h2 {
            margin-top: 0;
            margin-bottom: var(--space-lg);
            font-size: var(--text-2xl);
        }
        .cta-buttons-top {
            display: flex;
            gap: var(--space-md);
            justify-content: center;
            flex-wrap: wrap;
        }
        .cta-buttons-top .btn {
            min-width: 200px;
        }
        @media (max-width: 768px) {
            .cta-buttons-top {
                flex-direction: column;
                align-items: stretch;
            }
        }
'''

    # Find the closing </style> tag and insert CSS before it
    if '</style>' in content:
        content = content.replace('</style>', css_addition + '    </style>', 1)

    # Step 6: Write the updated content
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False

# Process all review files
print("🚀 Moving Test sections to top and updating dates to 2026...\n")

updated_count = 0
total_count = 0

for category in review_categories:
    review_path = os.path.join(base_path, f"pages/reviews/{category}")

    if not os.path.exists(review_path):
        continue

    review_files = glob.glob(os.path.join(review_path, "*.html"))

    for file_path in sorted(review_files):
        total_count += 1
        filename = os.path.basename(file_path)

        if process_review_file(file_path):
            updated_count += 1
            print(f"✓ Updated: {category}/{filename}")
        else:
            print(f"  Skipped: {category}/{filename} (no changes)")

print(f"\n✅ Process complete!")
print(f"📊 Updated {updated_count}/{total_count} review files")
print(f"✓ All dates changed to 2026")
print(f"✓ Test sections moved to top")
