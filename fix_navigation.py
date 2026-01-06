import os
import re
import glob

# Base directory
base_dir = r"C:\Users\Freddy\Desktop\techvernia.com\techvernia.com\pages\reviews"

# Correct navigation HTML
correct_nav = '''<ul class="nav-menu" id="nav-menu">
<li class="nav-item">
    <a href="../../../index.html" class="nav-link" data-i18n="nav.home">Home</a>
</li>
<li class="nav-item dropdown">
    <a href="../../../pages/categories.html" class="nav-link dropdown-toggle" data-i18n="nav.categories">
        <span data-i18n="nav.categories">Categories</span>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"></path></svg>
    </a>
</li>
<li class="nav-item">
    <a href="../../../pages/guides.html" class="nav-link" data-i18n="nav.guides">Guides</a>
</li>
<li class="nav-item">
    <a href="../../../pages/comparisons.html" class="nav-link" data-i18n="nav.compare">Compare</a>
</li>
<li class="nav-item">
    <a href="../../../pages/ai-history.html" class="nav-link" data-i18n="nav.ai-history">AI History</a>
</li>
<li class="nav-item">
    <a href="../../../pages/blog.html" class="nav-link" data-i18n="nav.blog">Blog</a>
</li>
<li class="nav-item">
    <a href="../../../pages/about.html" class="nav-link" data-i18n="nav.about">About</a>
</li>
<li class="nav-item">
    <a href="../../../pages/contact.html" class="nav-link" data-i18n="nav.contact">Contact</a>
</li>
</ul>'''

# Pattern to match the nav-menu section (matches various formats)
nav_pattern = re.compile(
    r'<ul class="nav-menu" id="nav-menu">.*?</ul>',
    re.DOTALL
)

def fix_navigation(file_path):
    """Fix navigation in a single HTML file"""
    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if file has nav-menu
        if 'nav-menu' not in content:
            print(f"  [WARNING] No nav-menu found in {os.path.basename(file_path)}")
            return False

        # Replace the nav-menu section
        new_content = nav_pattern.sub(correct_nav, content)

        # Check if replacement happened
        if new_content == content:
            print(f"  [INFO] No changes needed for {os.path.basename(file_path)}")
            return False

        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"  [OK] Fixed {os.path.basename(file_path)}")
        return True
    except Exception as e:
        print(f"  [ERROR] Error processing {os.path.basename(file_path)}: {e}")
        return False

def process_directory(subdirectory):
    """Process all HTML files in a subdirectory"""
    dir_path = os.path.join(base_dir, subdirectory)

    if not os.path.exists(dir_path):
        print(f"\n[WARNING] Directory not found: {subdirectory}")
        return 0

    # Find all HTML files (excluding backup files)
    html_files = glob.glob(os.path.join(dir_path, "*.html"))
    html_files = [f for f in html_files if '.backup.' not in f]

    if not html_files:
        print(f"\n[INFO] {subdirectory}: No HTML files found")
        return 0

    print(f"\n[PROCESSING] {subdirectory} ({len(html_files)} files):")

    fixed_count = 0
    for file_path in html_files:
        if fix_navigation(file_path):
            fixed_count += 1

    return fixed_count

# Directories to process (excluding chatbots which is already done)
directories = [
    "coding",
    "writing",
    "video",
    "audio",
    "image",
    "seo",
    "productivity",
    "networking",
    "medical",
    "legal",
    "business",
    "analytics",
    "architecture",
    "sales",
    "research",
    "translation",
    "hr",
    "customer-service",
    "education",
    "gaming",
    "quantum",
    "cybersecurity"
]

# Main execution
if __name__ == "__main__":
    print("=" * 80)
    print("NAVIGATION FIX SCRIPT")
    print("=" * 80)
    print(f"Base directory: {base_dir}")
    print(f"Processing {len(directories)} subdirectories...")

    total_fixed = 0
    processed_dirs = []

    for directory in directories:
        fixed = process_directory(directory)
        total_fixed += fixed
        if fixed > 0:
            processed_dirs.append(f"{directory} ({fixed})")

    print("\n" + "=" * 80)
    print(f"SUMMARY")
    print("=" * 80)
    print(f"Total files fixed: {total_fixed}")
    if processed_dirs:
        print(f"\nDirectories with changes:")
        for d in processed_dirs:
            print(f"  - {d}")
    print("\n[SUCCESS] Navigation fix complete!")
