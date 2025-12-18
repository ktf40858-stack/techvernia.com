#!/usr/bin/env python3
"""
Fix GenuisNet.ai logo in cybersecurity review files
"""

import re
from pathlib import Path

BASE_DIR = Path("/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai")
CYBER_DIR = BASE_DIR / "pages" / "reviews" / "cybersecurity"

# Pattern for minified navigation
OLD_PATTERN = r'<nav class="navbar" id="navbar"><div class="nav-container"><a href="\.\.\/\.\.\/\.\.\/index\.html" class="logo"><span class="logo-text">Genuis<span class="highlight">Net</span>\.ai</span></a></div></nav>'

NEW_NAV = '''<nav class="navbar" id="navbar">
        <div class="nav-container">
            <a href="../../../index.html" class="logo">
                <img src="../../../assets/images/logo-neon.svg" alt="GenuisNet.ai" style="height: 50px; width: auto;">
            </a>
        </div>
    </nav>'''

def update_file(file_path):
    """Update navigation logo in file"""
    content = file_path.read_text(encoding='utf-8')

    # Check if already updated
    if "logo-neon.svg" in content:
        return False, "Already updated"

    # Update the navigation
    if re.search(OLD_PATTERN, content):
        new_content = re.sub(OLD_PATTERN, NEW_NAV, content)
        file_path.write_text(new_content, encoding='utf-8')
        return True, "Updated"

    return False, "Pattern not found"

def main():
    print("🔄 Updating cybersecurity review logos...\n")

    updated = 0
    skipped = 0

    for file in sorted(CYBER_DIR.glob("*.html")):
        success, message = update_file(file)
        if success:
            print(f"  ✅ {file.stem}")
            updated += 1
        else:
            skipped += 1

    print(f"\n✅ Updated: {updated} files")
    print(f"⏭️  Skipped: {skipped} files")

if __name__ == "__main__":
    main()
