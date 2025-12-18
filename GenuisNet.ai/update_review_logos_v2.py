#!/usr/bin/env python3
"""
Update the logo in all review pages to use logo-neon.svg instead of inline SVG.
"""

import os
import re
import glob

base_path = "/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai"
review_categories = ['chatbots', 'writing', 'image', 'video', 'audio', 'coding',
                     'productivity', 'seo', 'business', 'cybersecurity', 'architecture', 'medical']

def update_logo_in_review(file_path):
    """Update logo in a review file."""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Pattern to match the old inline SVG logo (multiline, more flexible)
    # Match from <a href...class="logo"> to </a>
    old_logo_pattern = r'<a href="\.\.\.\/\.\.\.\/index\.html" class="logo">.*?<\/a>'

    # New logo with img tag
    new_logo = '''<a href="../../../index.html" class="logo">
                <img src="../../../assets/images/logo-neon.svg" alt="GenuisNet.ai Logo" style="height: 40px; width: auto;">
            </a>'''

    # Count matches before replacement
    matches = re.findall(old_logo_pattern, content, flags=re.DOTALL)

    # Replace the logo
    content = re.sub(old_logo_pattern, new_logo, content, flags=re.DOTALL)

    # Also update footer logo if it exists
    old_footer_logo_pattern = r'<a href="\.\.\.\/\.\.\.\/index\.html" class="footer-logo">.*?<\/a>'

    new_footer_logo = '''<a href="../../../index.html" class="footer-logo">
                        <img src="../../../assets/images/logo-neon.svg" alt="GenuisNet.ai Logo" style="height: 40px; width: auto;">
                    </a>'''

    content = re.sub(old_footer_logo_pattern, new_footer_logo, content, flags=re.DOTALL)

    # Write back if changed
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False

# Process all review files
print("🔄 Updating logos in all review pages...\n")

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

        if update_logo_in_review(file_path):
            updated_count += 1
            print(f"✓ Updated: {category}/{filename}")

print(f"\n✅ Process complete!")
print(f"📊 Updated {updated_count}/{total_count} review files")
print(f"✓ All logos now use logo-neon.svg")
