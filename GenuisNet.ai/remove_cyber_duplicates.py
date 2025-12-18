#!/usr/bin/env python3
"""
Script to remove duplicate tool cards from cybersecurity page.
"""

import re

page_path = "/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/categories/ai-cybersecurity.html"

# Read the file
with open(page_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find all tool cards with their content
# Pattern: <a href="...">...</a> including the entire tool card
pattern = r'<a\s+href="[^"]*"\s+class="tool-card">(.*?)</a>'
cards = re.findall(pattern, content, flags=re.DOTALL)

print(f"Total tool cards found: {len(cards)}")

# Track seen tool names and their full card HTML
seen_tools = {}
duplicates_found = []

# Find all complete card patterns
card_pattern = r'(<a\s+href="[^"]*"\s+class="tool-card">.*?</a>)'
all_cards = re.findall(card_pattern, content, flags=re.DOTALL)

for card_html in all_cards:
    # Extract tool name from h3
    h3_match = re.search(r'<h3>([^<]+)</h3>', card_html)
    if h3_match:
        tool_name = h3_match.group(1).strip()

        if tool_name in seen_tools:
            # This is a duplicate
            duplicates_found.append((tool_name, card_html))
            print(f"⚠ Duplicate found: {tool_name}")
        else:
            # First occurrence, keep it
            seen_tools[tool_name] = card_html

print(f"\nUnique tools: {len(seen_tools)}")
print(f"Duplicates to remove: {len(duplicates_found)}")

# Remove duplicates from content
for tool_name, duplicate_html in duplicates_found:
    # Escape special regex characters in the HTML
    escaped_html = re.escape(duplicate_html)
    # Remove this exact duplicate (only remove it once)
    content = re.sub(escaped_html, '', content, count=1)
    print(f"✓ Removed duplicate: {tool_name}")

# Write the cleaned content back
with open(page_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n✓ File updated successfully!")
print(f"✓ Removed {len(duplicates_found)} duplicate tool cards")
