import os
import re
import glob

# Base directory
base_dir = r"C:\Users\Freddy\Desktop\techvernia.com\techvernia.com\pages"

# Directories to process
directories = [
    "certifications",
    "comparisons/coding",
    "comparisons/image",
    "categories",  # Process the guides subdirectory pages
    "compare",
    "guides"
]

def fix_navigation(file_path):
    """Add AI History link to navigation if missing"""
    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if AI History already exists
        if 'ai-history' in content:
            print(f"  [SKIP] {os.path.basename(file_path)} - already has AI History")
            return False

        # Check if file has nav-menu
        if 'nav-menu' not in content:
            print(f"  [WARNING] No nav-menu found in {os.path.basename(file_path)}")
            return False

        # Pattern 1: After Compare link with <span> tags
        pattern1 = re.compile(
            r'(<li class="nav-item">\s*<a[^>]*>\s*<span[^>]*data-i18n="nav\.compare"[^>]*>.*?</span>\s*</a>\s*</li>)\s*(<li class="nav-item">)',
            re.DOTALL
        )

        # Pattern 2: After Compare link without <span> tags
        pattern2 = re.compile(
            r'(<li class="nav-item">\s*<a[^>]+data-i18n="nav\.compare"[^>]*>.*?</a>\s*</li>)\s*(<li class="nav-item">)',
            re.DOTALL
        )

        # AI History link to insert
        ai_history_link = '''
                <li class="nav-item">
                    <a href="ai-history.html" class="nav-link"><span data-i18n="nav.ai-history">AI History</span></a>
                </li>
'''

        # Try pattern 1 first
        new_content = pattern1.sub(r'\1' + ai_history_link + r'\2', content)

        # If no match, try pattern 2
        if new_content == content:
            new_content = pattern2.sub(r'\1' + ai_history_link + r'\2', content)

        # Check if replacement happened
        if new_content == content:
            print(f"  [INFO] No suitable location found in {os.path.basename(file_path)}")
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
    html_files = [f for f in html_files if '.backup.' not in f and 'backup_' not in f]

    if not html_files:
        print(f"\n[INFO] {subdirectory}: No HTML files found")
        return 0

    print(f"\n[PROCESSING] {subdirectory} ({len(html_files)} files):")

    fixed_count = 0
    for file_path in html_files:
        if fix_navigation(file_path):
            fixed_count += 1

    return fixed_count

# Main execution
if __name__ == "__main__":
    print("=" * 80)
    print("ADD AI HISTORY LINK SCRIPT")
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
    print("\n[SUCCESS] AI History link addition complete!")
