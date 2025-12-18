#!/usr/bin/env python3
"""
Script pour implémenter les screenshots téléchargés dans les pages HTML
Remplace les placeholders par les vrais chemins d'images
"""

from pathlib import Path
import re

BASE_DIR = Path(__file__).parent.parent
REVIEWS_DIR = BASE_DIR / "pages" / "reviews"
SCREENSHOTS_DIR = BASE_DIR / "assets" / "screenshots"

def get_screenshot_path(category: str, tool_name: str) -> str:
    """Retourne le chemin relatif vers un screenshot s'il existe"""
    screenshot_file = SCREENSHOTS_DIR / category / f"{tool_name}.png"

    if screenshot_file.exists():
        # Chemin relatif depuis pages/reviews/[category]/
        return f"../../../assets/screenshots/{category}/{tool_name}.png"

    return None

def update_chatgpt_page():
    """Met à jour la page ChatGPT avec le vrai screenshot"""
    html_file = REVIEWS_DIR / "chatbots" / "chatgpt.html"

    if not html_file.exists():
        print(f"✗ File not found: {html_file}")
        return False

    # Lire le contenu
    content = html_file.read_text(encoding='utf-8')

    # Vérifier si nous avons le screenshot
    screenshot_path = get_screenshot_path('chatbots', 'chatgpt')

    if not screenshot_path:
        print("✗ ChatGPT screenshot not found")
        return False

    print(f"✓ ChatGPT screenshot found: {screenshot_path}")

    # Remplacer les placeholders par le vrai screenshot
    # On remplace juste la première image (Main Interface) avec notre screenshot
    original_content = content

    content = re.sub(
        r'<img src="https://via\.placeholder\.com/[^"]*ChatGPT\+Main\+Interface[^"]*" alt="ChatGPT Main Interface">',
        f'<img src="{screenshot_path}" alt="ChatGPT Main Interface">',
        content,
        count=1
    )

    if content != original_content:
        # Sauvegarder
        html_file.write_text(content, encoding='utf-8')
        print(f"✓ Updated: {html_file.name}")
        return True
    else:
        print(f"⚠ No changes made to {html_file.name}")
        return False

def add_screenshots_to_all_reviews():
    """Ajoute une section screenshot à toutes les pages de review qui ont un screenshot"""
    updated_count = 0
    skipped_count = 0

    for category_dir in sorted(SCREENSHOTS_DIR.iterdir()):
        if not category_dir.is_dir():
            continue

        category = category_dir.name

        for screenshot_file in category_dir.glob("*.png"):
            tool_name = screenshot_file.stem
            html_file = REVIEWS_DIR / category / f"{tool_name}.html"

            if not html_file.exists():
                print(f"⚠ HTML not found for screenshot: {category}/{tool_name}")
                continue

            content = html_file.read_text(encoding='utf-8')

            # Vérifier si la page a déjà une section screenshots
            if 'screenshots-gallery' in content.lower():
                print(f"⊳ Already has screenshots: {category}/{tool_name}")
                skipped_count += 1
                continue

            # Créer la section screenshots
            screenshot_path = f"../../../assets/screenshots/{category}/{tool_name}.png"

            screenshot_section = f'''
        <h2 id="screenshots">Screenshots & Interface</h2>
        <p>Explore {tool_name.replace('-', ' ').title()}'s interface:</p>

        <div class="screenshots-gallery-enhanced">
            <div class="screenshot-card">
                <img src="{screenshot_path}" alt="{tool_name.replace('-', ' ').title()} Interface">
                <div class="screenshot-overlay">
                    <div class="screenshot-title">Main Interface</div>
                    <div class="screenshot-description">Overview of the main interface and features</div>
                </div>
            </div>
        </div>
'''

            # Chercher où insérer (avant la section "Alternatives" ou "Conclusion")
            insertion_patterns = [
                r'(<h2[^>]*>Alternatives[^<]*</h2>)',
                r'(<h2[^>]*>Conclusion[^<]*</h2>)',
                r'(<h2[^>]*>Final Verdict[^<]*</h2>)',
                r'(<footer)',
            ]

            inserted = False
            for pattern in insertion_patterns:
                match = re.search(pattern, content, re.IGNORECASE)
                if match:
                    # Insérer avant cette section
                    insert_pos = match.start()
                    content = content[:insert_pos] + screenshot_section + '\n\n' + content[insert_pos:]
                    inserted = True
                    break

            if inserted:
                html_file.write_text(content, encoding='utf-8')
                print(f"✓ Added screenshots to: {category}/{tool_name}")
                updated_count += 1
            else:
                print(f"⚠ Could not find insertion point: {category}/{tool_name}")

    return updated_count, skipped_count

def main():
    print("=" * 70)
    print("Screenshot Implementation Script")
    print("=" * 70)

    # Compter les screenshots disponibles
    total_screenshots = sum(1 for cat_dir in SCREENSHOTS_DIR.iterdir()
                          if cat_dir.is_dir()
                          for _ in cat_dir.glob("*.png"))

    print(f"\n📸 Found {total_screenshots} screenshots to implement\n")

    # 1. Mettre à jour ChatGPT spécifiquement
    print("📝 Updating ChatGPT page...")
    update_chatgpt_page()

    print("\n" + "-" * 70)
    print("📝 Adding screenshot sections to all review pages...")
    print("-" * 70 + "\n")

    # 2. Ajouter des sections screenshots à toutes les pages
    updated, skipped = add_screenshots_to_all_reviews()

    # Rapport final
    print("\n" + "=" * 70)
    print("📊 Implementation Report")
    print("=" * 70)
    print(f"Total screenshots available: {total_screenshots}")
    print(f"✓ Pages updated: {updated}")
    print(f"⊳ Pages skipped (already have screenshots): {skipped}")
    print(f"⚠ Pages without HTML: {total_screenshots - updated - skipped}")
    print("=" * 70)

    print("\n✅ Done! Check your website to see the screenshots.")

if __name__ == "__main__":
    main()
