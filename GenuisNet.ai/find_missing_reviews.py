#!/usr/bin/env python3
"""
Find all AI tools in category pages that don't have review files.
"""

import os
import re
import glob

base_path = "/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai"
categories = ['chatbots', 'writing', 'image', 'video', 'audio', 'coding',
              'productivity', 'seo', 'business', 'cybersecurity', 'architecture', 'medical']

def get_tools_from_category_page(category):
    """Extract tool names from category HTML page."""
    page_path = os.path.join(base_path, f"pages/categories/ai-{category}.html")

    if not os.path.exists(page_path):
        return []

    with open(page_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all hrefs pointing to reviews
    pattern = r'href="\.\.\/reviews\/' + category + r'\/([^"]+)\.html"'
    matches = re.findall(pattern, content)

    return list(set(matches))  # Remove duplicates

def check_review_exists(category, tool_slug):
    """Check if review file exists."""
    review_path = os.path.join(base_path, f"pages/reviews/{category}/{tool_slug}.html")
    return os.path.exists(review_path)

# Find missing reviews
print("🔍 Scanning for AI tools without full reviews...\n")

missing_reviews = {}
total_tools = 0
total_missing = 0

for category in categories:
    tools = get_tools_from_category_page(category)
    total_tools += len(tools)

    missing = []
    for tool in tools:
        if not check_review_exists(category, tool):
            missing.append(tool)
            total_missing += 1

    if missing:
        missing_reviews[category] = missing

# Display results
print("=" * 70)
print("📊 RESULTS")
print("=" * 70)
print(f"Total tools found: {total_tools}")
print(f"Tools with reviews: {total_tools - total_missing}")
print(f"Tools WITHOUT reviews: {total_missing}")
print("=" * 70)

if missing_reviews:
    print("\n❌ MISSING REVIEWS:\n")
    for category, tools in missing_reviews.items():
        print(f"📁 {category.upper()} ({len(tools)} missing)")
        for tool in sorted(tools):
            print(f"   • {tool}")
        print()
else:
    print("\n✅ All tools have reviews!")

# Save to file for reference
if missing_reviews:
    output_file = os.path.join(base_path, "MISSING_REVIEWS.txt")
    with open(output_file, 'w') as f:
        f.write("AI Tools Missing Reviews\n")
        f.write("=" * 70 + "\n\n")
        for category, tools in missing_reviews.items():
            f.write(f"{category.upper()}\n")
            f.write("-" * 70 + "\n")
            for tool in sorted(tools):
                f.write(f"{tool}\n")
            f.write("\n")

    print(f"📄 List saved to: MISSING_REVIEWS.txt")
