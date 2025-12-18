#!/usr/bin/env python3
"""
Script to update tool counts in all category pages and home page.
"""

import os
import re

# Base path
base_path = "/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai"

# Count tools in each category
categories = {
    'chatbots': 'pages/reviews/chatbots',
    'writing': 'pages/reviews/writing',
    'image': 'pages/reviews/image',
    'video': 'pages/reviews/video',
    'audio': 'pages/reviews/audio',
    'coding': 'pages/reviews/coding',
    'productivity': 'pages/reviews/productivity',
    'seo': 'pages/reviews/seo',
    'business': 'pages/reviews/business',
    'cybersecurity': 'pages/reviews/cybersecurity',
    'architecture': 'pages/reviews/architecture',
    'medical': 'pages/reviews/medical',
}

# Count tools in each category
counts = {}
for cat_name, cat_path in categories.items():
    full_path = os.path.join(base_path, cat_path)
    if os.path.exists(full_path):
        html_files = [f for f in os.listdir(full_path) if f.endswith('.html')]
        counts[cat_name] = len(html_files)
        print(f"{cat_name}: {len(html_files)} tools")
    else:
        counts[cat_name] = 0
        print(f"{cat_name}: directory not found")

print(f"\nTotal tools: {sum(counts.values())}")

# Update category pages
category_pages = {
    'ai-chatbots.html': counts['chatbots'],
    'ai-writing.html': counts['writing'],
    'ai-image.html': counts['image'],
    'ai-video.html': counts['video'],
    'ai-audio.html': counts['audio'],
    'ai-coding.html': counts['coding'],
    'ai-productivity.html': counts['productivity'],
    'ai-seo.html': counts['seo'],
    'ai-business.html': counts['business'],
    'ai-cybersecurity.html': counts['cybersecurity'],
    'ai-architecture.html': counts['architecture'],
    'ai-medical.html': counts['medical'],
}

updated_files = []

for page_name, tool_count in category_pages.items():
    page_path = os.path.join(base_path, 'pages', 'categories', page_name)

    if os.path.exists(page_path):
        with open(page_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update pattern: <span>X Tools Reviewed</span>
        new_content = re.sub(
            r'<span>\d+ Tools Reviewed</span>',
            f'<span>{tool_count} Tools Reviewed</span>',
            content
        )

        if new_content != content:
            with open(page_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            updated_files.append(page_name)
            print(f"✓ Updated: {page_name} -> {tool_count} tools")

# Update home_hero_enhanced.html
hero_path = os.path.join(base_path, 'home_hero_enhanced.html')
if os.path.exists(hero_path):
    with open(hero_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update the three preview cards
    # Card 1: AI Chatbots
    content = re.sub(
        r'(<div class="card-title">AI Chatbots</div>\s*<div class="card-count">)\d+ Tools(</div>)',
        f'\\g<1>{counts["chatbots"]} Tools\\g<2>',
        content
    )

    # Card 2: Image Gen
    content = re.sub(
        r'(<div class="card-title">Image Gen</div>\s*<div class="card-count">)\d+ Tools(</div>)',
        f'\\g<1>{counts["image"]} Tools\\g<2>',
        content
    )

    # Card 3: AI Coding
    content = re.sub(
        r'(<div class="card-title">AI Coding</div>\s*<div class="card-count">)\d+ Tools(</div>)',
        f'\\g<1>{counts["coding"]} Tools\\g<2>',
        content
    )

    with open(hero_path, 'w', encoding='utf-8') as f:
        f.write(content)
    updated_files.append('home_hero_enhanced.html')
    print(f"✓ Updated: home_hero_enhanced.html")

print(f"\n✓ Total files updated: {len(updated_files)}")
