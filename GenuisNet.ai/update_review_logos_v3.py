#!/usr/bin/env python3
"""
Update the logo in all review pages to use logo-neon.svg.
Uses a simpler find and replace approach.
"""

import os
import glob

base_path = "/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai"
review_categories = ['chatbots', 'writing', 'image', 'video', 'audio', 'coding',
                     'productivity', 'seo', 'business', 'cybersecurity', 'architecture', 'medical']

# The exact old logo HTML to find
old_logo = '''<a href="../../../index.html" class="logo">
                <span class="logo-icon">
                    <svg viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="20" cy="20" r="18" stroke="url(#logoGradient)" stroke-width="2"/>
                        <circle cx="20" cy="20" r="8" fill="url(#logoGradient)"/>
                        <defs>
                            <linearGradient id="logoGradient" x1="0" y1="0" x2="40" y2="40">
                                <stop offset="0%" stop-color="#00D9FF"/>
                                <stop offset="100%" stop-color="#7C3AED"/>
                            </linearGradient>
                        </defs>
                    </svg>
                </span>
                <span class="logo-text">Genuis<span class="highlight">Net</span>.ai</span>
            </a>'''

# The new logo to replace it with
new_logo = '''<a href="../../../index.html" class="logo">
                <img src="../../../assets/images/logo-neon.svg" alt="GenuisNet.ai Logo" style="height: 40px; width: auto;">
            </a>'''

# Footer versions
old_footer_logo = '''<a href="../../../index.html" class="footer-logo">
                        <span class="logo-icon">
                            <svg viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <circle cx="20" cy="20" r="18" stroke="url(#logoGradient)" stroke-width="2"/>
                                <circle cx="20" cy="20" r="8" fill="url(#logoGradient)"/>
                                <defs>
                                    <linearGradient id="logoGradient" x1="0" y1="0" x2="40" y2="40">
                                        <stop offset="0%" stop-color="#00D9FF"/>
                                        <stop offset="100%" stop-color="#7C3AED"/>
                                    </linearGradient>
                                </defs>
                            </svg>
                        </span>
                        <span class="logo-text">Genuis<span class="highlight">Net</span>.ai</span>
                    </a>'''

new_footer_logo = '''<a href="../../../index.html" class="footer-logo">
                        <img src="../../../assets/images/logo-neon.svg" alt="GenuisNet.ai Logo" style="height: 40px; width: auto;">
                    </a>'''

def update_logo_in_review(file_path):
    """Update logo in a review file."""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Replace navbar logo
    content = content.replace(old_logo, new_logo)

    # Replace footer logo
    content = content.replace(old_footer_logo, new_footer_logo)

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
