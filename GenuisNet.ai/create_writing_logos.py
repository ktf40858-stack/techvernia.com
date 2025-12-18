#!/usr/bin/env python3
"""
Create better logos for AI Writing Tools based on actual brand designs.
"""

import os

base_path = "/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/assets/images/tools/writing"

# Writing tool logos with brand-appropriate designs
writing_logos = {
    'copyai': '''<svg width="200" height="200" viewBox="0 0 200 200" fill="none" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="gradCopy" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#10B981;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#059669;stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect width="200" height="200" rx="40" fill="url(#gradCopy)"/>
    <!-- Copy.ai icon: document with sparkle -->
    <rect x="60" y="50" width="80" height="100" rx="8" fill="white" opacity="0.9"/>
    <line x1="75" y1="70" x2="125" y2="70" stroke="url(#gradCopy)" stroke-width="4" stroke-linecap="round"/>
    <line x1="75" y1="90" x2="115" y2="90" stroke="url(#gradCopy)" stroke-width="4" stroke-linecap="round"/>
    <line x1="75" y1="110" x2="120" y2="110" stroke="url(#gradCopy)" stroke-width="4" stroke-linecap="round"/>
    <!-- Sparkle -->
    <path d="M 150 40 L 155 50 L 165 55 L 155 60 L 150 70 L 145 60 L 135 55 L 145 50 Z" fill="white"/>
</svg>''',

    'grammarly': '''<svg width="200" height="200" viewBox="0 0 200 200" fill="none" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="gradGram" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#15C39A;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#0D9470;stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect width="200" height="200" rx="40" fill="url(#gradGram)"/>
    <!-- Grammarly G circle -->
    <circle cx="100" cy="100" r="60" fill="white"/>
    <circle cx="100" cy="100" r="50" fill="url(#gradGram)"/>
    <path d="M 100 60 A 40 40 0 0 1 100 140" stroke="white" stroke-width="8" fill="none" stroke-linecap="round"/>
    <line x1="100" y1="100" x2="130" y2="100" stroke="white" stroke-width="8" stroke-linecap="round"/>
</svg>''',

    'quillbot': '''<svg width="200" height="200" viewBox="0 0 200 200" fill="none" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="gradQuill" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#00B67A;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#008C5E;stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect width="200" height="200" rx="40" fill="url(#gradQuill)"/>
    <!-- Quill feather icon -->
    <path d="M 80 50 Q 90 45 100 50 Q 110 45 120 50 L 110 140 Q 105 150 100 155 Q 95 150 90 140 Z" fill="white"/>
    <line x1="90" y1="70" x2="95" y2="70" stroke="url(#gradQuill)" stroke-width="2"/>
    <line x1="92" y1="90" x2="97" y2="90" stroke="url(#gradQuill)" stroke-width="2"/>
    <line x1="94" y1="110" x2="99" y2="110" stroke="url(#gradQuill)" stroke-width="2"/>
</svg>''',

    'rytr': '''<svg width="200" height="200" viewBox="0 0 200 200" fill="none" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="gradRytr" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#7C3AED;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#6D28D9;stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect width="200" height="200" rx="40" fill="url(#gradRytr)"/>
    <!-- Rytr R icon -->
    <text x="100" y="135" font-family="Arial, sans-serif" font-size="100" font-weight="900" fill="white" text-anchor="middle">R</text>
    <circle cx="140" cy="60" r="12" fill="white"/>
</svg>''',

    'wordtune': '''<svg width="200" height="200" viewBox="0 0 200 200" fill="none" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="gradWord" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#0052CC;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#003D99;stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect width="200" height="200" rx="40" fill="url(#gradWord)"/>
    <!-- Wordtune tuning fork / sound wave -->
    <path d="M 60 100 Q 80 60 100 100 Q 120 140 140 100" stroke="white" stroke-width="8" fill="none" stroke-linecap="round"/>
    <path d="M 70 100 Q 85 75 100 100 Q 115 125 130 100" stroke="white" stroke-width="6" fill="none" stroke-linecap="round" opacity="0.6"/>
</svg>''',

    'writesonic': '''<svg width="200" height="200" viewBox="0 0 200 200" fill="none" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="gradWrite" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#8B5CF6;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#7C3AED;stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect width="200" height="200" rx="40" fill="url(#gradWrite)"/>
    <!-- Writesonic sonic waves -->
    <circle cx="100" cy="100" r="20" fill="white"/>
    <circle cx="100" cy="100" r="35" stroke="white" stroke-width="6" fill="none" opacity="0.6"/>
    <circle cx="100" cy="100" r="50" stroke="white" stroke-width="4" fill="none" opacity="0.4"/>
    <circle cx="100" cy="100" r="65" stroke="white" stroke-width="3" fill="none" opacity="0.2"/>
</svg>''',

    'jasper-ai': '''<svg width="200" height="200" viewBox="0 0 200 200" fill="none" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="gradJasper" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#8B5CF6;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#7C3AED;stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect width="200" height="200" rx="40" fill="url(#gradJasper)"/>
    <!-- Jasper lightning bolt -->
    <path d="M 100 30 L 70 100 L 100 95 L 85 170 L 130 90 L 100 95 Z" fill="white"/>
</svg>'''
}

print("🎨 Creating official-style logos for Writing Tools...\n")

created_count = 0

for filename, svg_content in writing_logos.items():
    logo_path = os.path.join(base_path, f"{filename}.svg")

    with open(logo_path, 'w', encoding='utf-8') as f:
        f.write(svg_content)

    created_count += 1
    print(f"✓ Created: {filename}.svg")

print(f"\n✅ Created {created_count} writing tool logos!")
print("📁 Location: assets/images/tools/writing/")
