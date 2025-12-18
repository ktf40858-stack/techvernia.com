#!/usr/bin/env python3
"""
Verify that all tools in all categories have their official logos.
Check if logo files exist and are valid SVG files (not HTML documents).
"""

import os
import glob

base_path = "/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai"
review_categories = ['chatbots', 'writing', 'image', 'video', 'audio', 'coding',
                     'productivity', 'seo', 'business', 'cybersecurity', 'architecture', 'medical']

def check_logo_exists(category, tool_slug):
    """Check if logo exists and is valid SVG."""
    logo_path = os.path.join(base_path, f"assets/images/tools/{category}/{tool_slug}.svg")

    if not os.path.exists(logo_path):
        return False, "Missing"

    # Check file size - HTML documents are usually large (>10KB)
    file_size = os.path.getsize(logo_path)
    if file_size > 50000:  # 50KB
        return False, f"Too large ({file_size} bytes, likely HTML)"

    # Check if it's actually an SVG
    with open(logo_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read(500)  # Read first 500 chars
        if not ('<svg' in content or '<?xml' in content):
            return False, "Not SVG format"

    return True, f"OK ({file_size} bytes)"

print("🔍 Verifying tool logos across all categories...\n")

missing_logos = []
invalid_logos = []
valid_logos = []

for category in review_categories:
    review_path = os.path.join(base_path, f"pages/reviews/{category}")

    if not os.path.exists(review_path):
        continue

    print(f"\n📁 {category.upper()}")
    print("=" * 60)

    review_files = sorted(glob.glob(os.path.join(review_path, "*.html")))

    for file_path in review_files:
        tool_slug = os.path.basename(file_path).replace('.html', '')
        tool_name = tool_slug.replace('-', ' ').title()

        is_valid, status = check_logo_exists(category, tool_slug)

        if is_valid:
            valid_logos.append((category, tool_slug))
            print(f"  ✓ {tool_name:<30} {status}")
        elif "Missing" in status:
            missing_logos.append((category, tool_slug, tool_name))
            print(f"  ✗ {tool_name:<30} ❌ {status}")
        else:
            invalid_logos.append((category, tool_slug, tool_name, status))
            print(f"  ⚠ {tool_name:<30} ⚠️  {status}")

print("\n" + "=" * 60)
print(f"\n📊 SUMMARY")
print("=" * 60)
print(f"✓ Valid logos:   {len(valid_logos)}")
print(f"✗ Missing logos: {len(missing_logos)}")
print(f"⚠ Invalid logos: {len(invalid_logos)}")

if missing_logos:
    print(f"\n❌ MISSING LOGOS ({len(missing_logos)}):")
    print("-" * 60)
    for category, slug, name in missing_logos:
        print(f"  • {category}/{slug}.svg ({name})")

if invalid_logos:
    print(f"\n⚠️  INVALID LOGOS ({len(invalid_logos)}):")
    print("-" * 60)
    for category, slug, name, reason in invalid_logos:
        print(f"  • {category}/{slug}.svg ({name}) - {reason}")

if not missing_logos and not invalid_logos:
    print("\n🎉 All tool logos are present and valid!")
else:
    print(f"\n⚠️  Total issues: {len(missing_logos) + len(invalid_logos)}")
