#!/usr/bin/env python3
"""
Script pour ajouter les screenshots aux pages de review
"""

import os
import re
from pathlib import Path

def get_tool_name_from_file(filename):
    """Extract tool name from HTML filename"""
    return Path(filename).stem

def find_screenshot_for_tool(category, tool_name):
    """Find the screenshot file for a tool"""
    screenshot_dir = f"GenuisNet.ai/assets/screenshots/{category}"

    # Common variations of the tool name
    variations = [
        tool_name,
        tool_name.lower(),
        tool_name.capitalize(),
        tool_name.replace('-', ' ').title(),
        tool_name.replace('-', '_'),
    ]

    # Look for matching files
    if os.path.exists(screenshot_dir):
        for file in os.listdir(screenshot_dir):
            file_lower = file.lower()
            for var in variations:
                if var.lower() in file_lower or file_lower.startswith(var.lower()):
                    return f"../../../assets/screenshots/{category}/{file}"

    return None

def add_screenshots_section(html_content, tool_name, category, screenshot_path):
    """Add screenshots section to review page"""

    # Check if screenshots section already exists
    if 'id="screenshots"' in html_content or 'Screenshots & Interface' in html_content:
        print(f"  ℹ️  Screenshots section already exists for {tool_name}")
        return html_content

    # Find where to insert (before FAQ or before </article>)
    insert_markers = [
        'id="faq"',
        'Frequently Asked Questions',
        '</article>'
    ]

    insert_pos = -1
    for marker in insert_markers:
        pos = html_content.find(marker)
        if pos != -1:
            # Go back to find the <h2 or <div before this marker
            search_start = max(0, pos - 500)
            section_start = html_content.rfind('<h2', search_start, pos)
            if section_start != -1:
                insert_pos = section_start
                break

    if insert_pos == -1:
        print(f"  ❌ Could not find insertion point for {tool_name}")
        return html_content

    # Get tool display name (capitalize properly)
    display_name = tool_name.replace('-', ' ').title()

    # Create screenshots section HTML
    screenshots_html = f'''
<h2 id="screenshots">Screenshots & Interface</h2>
<p>Explore {display_name}'s interface and key features through these detailed screenshots:</p>

<div class="screenshots-gallery-enhanced">
    <div class="screenshot-card" onclick="openLightbox(this)">
        <img src="{screenshot_path}" alt="{display_name} Interface">
        <div class="screenshot-overlay">
            <div class="screenshot-title">Main Interface</div>
            <div class="screenshot-description">Intuitive user interface with all key features</div>
        </div>
    </div>
</div>

'''

    # Insert the section
    html_content = html_content[:insert_pos] + screenshots_html + html_content[insert_pos:]

    # Check if lightbox modal exists
    if 'lightbox-modal' not in html_content:
        # Add lightbox modal before </article>
        lightbox_html = '''
<!-- Lightbox Modal -->
<div class="lightbox-modal" id="lightboxModal" onclick="closeLightbox()">
    <div class="lightbox-content" onclick="event.stopPropagation()">
        <button class="lightbox-close" onclick="closeLightbox()">×</button>
        <img id="lightboxImage" src="" alt="">
        <div class="lightbox-caption" id="lightboxCaption"></div>
    </div>
</div>
'''
        article_end = html_content.rfind('</article>')
        if article_end != -1:
            html_content = html_content[:article_end] + lightbox_html + html_content[article_end:]

    # Check if lightbox JavaScript exists
    if 'function openLightbox' not in html_content:
        # Add lightbox JavaScript before </script> tag at the end
        lightbox_js = '''
        // Lightbox functionality
        function openLightbox(element) {
            const modal = document.getElementById('lightboxModal');
            const img = document.getElementById('lightboxImage');
            const caption = document.getElementById('lightboxCaption');

            const imgSrc = element.querySelector('img').src;
            const title = element.querySelector('.screenshot-title')?.textContent || '';
            const description = element.querySelector('.screenshot-description')?.textContent || '';

            img.src = imgSrc;
            caption.textContent = title + (description ? ' - ' + description : '');
            modal.classList.add('active');

            // Prevent body scroll
            document.body.style.overflow = 'hidden';
        }

        function closeLightbox() {
            const modal = document.getElementById('lightboxModal');
            modal.classList.remove('active');

            // Restore body scroll
            document.body.style.overflow = '';
        }

        // Close lightbox with Escape key
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') {
                closeLightbox();
            }
        });
'''
        # Find the last <script> tag before </body>
        last_script_end = html_content.rfind('</script>')
        if last_script_end != -1:
            html_content = html_content[:last_script_end] + lightbox_js + '\n    ' + html_content[last_script_end:]

    print(f"  ✅ Added screenshots section for {tool_name}")
    return html_content

def process_category(category_name, category_folder):
    """Process all review pages in a category"""

    review_dir = f"GenuisNet.ai/pages/reviews/{category_folder}"

    if not os.path.exists(review_dir):
        print(f"❌ Directory not found: {review_dir}")
        return

    print(f"\n📁 Processing {category_name} ({category_folder})")

    count = 0
    for filename in os.listdir(review_dir):
        if filename.endswith('.html') and not filename.endswith('.backup'):
            file_path = os.path.join(review_dir, filename)
            tool_name = get_tool_name_from_file(filename)

            # Find screenshot
            screenshot_path = find_screenshot_for_tool(category_folder, tool_name)

            if not screenshot_path:
                print(f"  ⚠️  No screenshot found for {tool_name}")
                continue

            # Read HTML
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Add screenshots section
            new_content = add_screenshots_section(content, tool_name, category_folder, screenshot_path)

            if new_content != content:
                # Backup original
                backup_path = file_path + '.screenshot_backup'
                with open(backup_path, 'w', encoding='utf-8') as f:
                    f.write(content)

                # Write modified
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)

                count += 1

    print(f"✅ {count} files modified in {category_name}")

def main():
    """Main function"""

    categories = [
        ('Chatbots', 'chatbots'),
        ('Writing', 'writing'),
        ('Gaming', 'gaming'),
        ('Quantum Computing', 'quantum'),
        ('Translation', 'translation'),
    ]

    print("🖼️  Adding screenshots to review pages...")

    for cat_name, cat_folder in categories:
        process_category(cat_name, cat_folder)

    print("\n🎉 Screenshot implementation complete!")

if __name__ == "__main__":
    main()
