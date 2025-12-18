#!/usr/bin/env python3
"""
Create neon SVG icons for each category to replace emoji icons.
"""

import os

base_path = "/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai"
assets_path = os.path.join(base_path, "assets/images/category-icons")

# Create directory if it doesn't exist
os.makedirs(assets_path, exist_ok=True)

# Category icon configurations with neon designs
category_icons = {
    'chatbots': {
        'gradient': '#00D9FF, #6666FF',
        'svg': '''<svg width="120" height="120" viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="grad-chatbots" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#00D9FF;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#6666FF;stop-opacity:1" />
        </linearGradient>
        <filter id="glow-chatbots">
            <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
            <feMerge>
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
    </defs>
    <!-- Chat bubble -->
    <rect x="20" y="30" width="60" height="45" rx="8" stroke="url(#grad-chatbots)" stroke-width="3" fill="none" filter="url(#glow-chatbots)"/>
    <rect x="40" y="50" width="60" height="45" rx="8" stroke="url(#grad-chatbots)" stroke-width="3" fill="none" filter="url(#glow-chatbots)"/>
    <!-- Dots inside chat -->
    <circle cx="55" cy="70" r="4" fill="url(#grad-chatbots)" filter="url(#glow-chatbots)"/>
    <circle cx="68" cy="70" r="4" fill="url(#grad-chatbots)" filter="url(#glow-chatbots)"/>
    <circle cx="81" cy="70" r="4" fill="url(#grad-chatbots)" filter="url(#glow-chatbots)"/>
</svg>'''
    },
    'writing': {
        'gradient': '#A855F7, #6366F1',
        'svg': '''<svg width="120" height="120" viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="grad-writing" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#A855F7;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#6366F1;stop-opacity:1" />
        </linearGradient>
        <filter id="glow-writing">
            <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
            <feMerge>
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
    </defs>
    <!-- Pen/Pencil -->
    <path d="M 75 25 L 95 45 L 50 90 L 30 95 L 35 75 L 75 25 Z" stroke="url(#grad-writing)" stroke-width="3" fill="none" filter="url(#glow-writing)"/>
    <line x1="70" y1="30" x2="90" y2="50" stroke="url(#grad-writing)" stroke-width="2" filter="url(#glow-writing)"/>
    <!-- Lines representing text -->
    <line x1="25" y1="40" x2="50" y2="40" stroke="url(#grad-writing)" stroke-width="2" filter="url(#glow-writing)"/>
    <line x1="25" y1="55" x2="45" y2="55" stroke="url(#grad-writing)" stroke-width="2" filter="url(#glow-writing)"/>
</svg>'''
    },
    'image': {
        'gradient': '#F472B6, #EC4899',
        'svg': '''<svg width="120" height="120" viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="grad-image" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#F472B6;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#EC4899;stop-opacity:1" />
        </linearGradient>
        <filter id="glow-image">
            <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
            <feMerge>
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
    </defs>
    <!-- Palette shape -->
    <path d="M 60 25 C 38 25 20 43 20 65 C 20 87 38 95 50 95 C 54 95 58 93 62 90 C 66 93 70 95 75 95 C 87 95 100 87 100 65 C 100 43 82 25 60 25 Z" stroke="url(#grad-image)" stroke-width="3" fill="none" filter="url(#glow-image)"/>
    <!-- Paint dots -->
    <circle cx="45" cy="50" r="5" fill="url(#grad-image)" filter="url(#glow-image)"/>
    <circle cx="65" cy="45" r="5" fill="url(#grad-image)" filter="url(#glow-image)"/>
    <circle cx="75" cy="60" r="5" fill="url(#grad-image)" filter="url(#glow-image)"/>
    <circle cx="50" cy="70" r="5" fill="url(#grad-image)" filter="url(#glow-image)"/>
</svg>'''
    },
    'video': {
        'gradient': '#FB923C, #F97316',
        'svg': '''<svg width="120" height="120" viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="grad-video" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#FB923C;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#F97316;stop-opacity:1" />
        </linearGradient>
        <filter id="glow-video">
            <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
            <feMerge>
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
    </defs>
    <!-- Play button in film frame -->
    <rect x="20" y="35" width="80" height="50" rx="5" stroke="url(#grad-video)" stroke-width="3" fill="none" filter="url(#glow-video)"/>
    <polygon points="50,50 50,70 70,60" fill="url(#grad-video)" filter="url(#glow-video)"/>
    <!-- Film holes -->
    <rect x="22" y="30" width="5" height="5" fill="url(#grad-video)" filter="url(#glow-video)"/>
    <rect x="93" y="30" width="5" height="5" fill="url(#grad-video)" filter="url(#glow-video)"/>
    <rect x="22" y="85" width="5" height="5" fill="url(#grad-video)" filter="url(#glow-video)"/>
    <rect x="93" y="85" width="5" height="5" fill="url(#grad-video)" filter="url(#glow-video)"/>
</svg>'''
    },
    'audio': {
        'gradient': '#4ADE80, #22C55E',
        'svg': '''<svg width="120" height="120" viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="grad-audio" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#4ADE80;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#22C55E;stop-opacity:1" />
        </linearGradient>
        <filter id="glow-audio">
            <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
            <feMerge>
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
    </defs>
    <!-- Waveform bars -->
    <rect x="30" y="45" width="6" height="30" rx="3" fill="url(#grad-audio)" filter="url(#glow-audio)"/>
    <rect x="42" y="35" width="6" height="50" rx="3" fill="url(#grad-audio)" filter="url(#glow-audio)"/>
    <rect x="54" y="25" width="6" height="70" rx="3" fill="url(#grad-audio)" filter="url(#glow-audio)"/>
    <rect x="66" y="40" width="6" height="40" rx="3" fill="url(#grad-audio)" filter="url(#glow-audio)"/>
    <rect x="78" y="30" width="6" height="60" rx="3" fill="url(#grad-audio)" filter="url(#glow-audio)"/>
    <rect x="90" y="50" width="6" height="20" rx="3" fill="url(#grad-audio)" filter="url(#glow-audio)"/>
</svg>'''
    },
    'coding': {
        'gradient': '#38BDF8, #0EA5E9',
        'svg': '''<svg width="120" height="120" viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="grad-coding" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#38BDF8;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#0EA5E9;stop-opacity:1" />
        </linearGradient>
        <filter id="glow-coding">
            <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
            <feMerge>
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
    </defs>
    <!-- Code brackets <> -->
    <path d="M 45 35 L 25 60 L 45 85" stroke="url(#grad-coding)" stroke-width="3" stroke-linecap="round" fill="none" filter="url(#glow-coding)"/>
    <path d="M 75 35 L 95 60 L 75 85" stroke="url(#grad-coding)" stroke-width="3" stroke-linecap="round" fill="none" filter="url(#glow-coding)"/>
    <path d="M 65 40 L 55 80" stroke="url(#grad-coding)" stroke-width="3" stroke-linecap="round" filter="url(#glow-coding)"/>
</svg>'''
    },
    'productivity': {
        'gradient': '#FACC15, #EAB308',
        'svg': '''<svg width="120" height="120" viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="grad-productivity" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#FACC15;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#EAB308;stop-opacity:1" />
        </linearGradient>
        <filter id="glow-productivity">
            <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
            <feMerge>
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
    </defs>
    <!-- Lightning bolt -->
    <path d="M 60 20 L 45 60 L 60 60 L 50 100 L 75 55 L 60 55 L 70 20 Z" fill="url(#grad-productivity)" filter="url(#glow-productivity)"/>
</svg>'''
    },
    'seo': {
        'gradient': '#34D399, #10B981',
        'svg': '''<svg width="120" height="120" viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="grad-seo" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#34D399;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#10B981;stop-opacity:1" />
        </linearGradient>
        <filter id="glow-seo">
            <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
            <feMerge>
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
    </defs>
    <!-- Search magnifying glass -->
    <circle cx="50" cy="50" r="20" stroke="url(#grad-seo)" stroke-width="3" fill="none" filter="url(#glow-seo)"/>
    <line x1="65" y1="65" x2="85" y2="85" stroke="url(#grad-seo)" stroke-width="3" stroke-linecap="round" filter="url(#glow-seo)"/>
    <!-- Upward trending arrow inside -->
    <path d="M 42 55 L 50 45 L 58 55" stroke="url(#grad-seo)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none" filter="url(#glow-seo)"/>
</svg>'''
    },
    'business': {
        'gradient': '#818CF8, #6366F1',
        'svg': '''<svg width="120" height="120" viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="grad-business" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#818CF8;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#6366F1;stop-opacity:1" />
        </linearGradient>
        <filter id="glow-business">
            <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
            <feMerge>
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
    </defs>
    <!-- Briefcase -->
    <rect x="30" y="45" width="60" height="40" rx="4" stroke="url(#grad-business)" stroke-width="3" fill="none" filter="url(#glow-business)"/>
    <path d="M 45 45 L 45 35 L 75 35 L 75 45" stroke="url(#grad-business)" stroke-width="3" fill="none" filter="url(#glow-business)"/>
    <line x1="30" y1="60" x2="90" y2="60" stroke="url(#grad-business)" stroke-width="2" filter="url(#glow-business)"/>
</svg>'''
    },
    'architecture': {
        'gradient': '#0EA5E9, #38BDF8',
        'svg': '''<svg width="120" height="120" viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="grad-architecture" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#0EA5E9;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#38BDF8;stop-opacity:1" />
        </linearGradient>
        <filter id="glow-architecture">
            <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
            <feMerge>
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
    </defs>
    <!-- Building/structure -->
    <path d="M 60 25 L 30 45 L 30 90 L 90 90 L 90 45 Z" stroke="url(#grad-architecture)" stroke-width="3" fill="none" filter="url(#glow-architecture)"/>
    <line x1="60" y1="25" x2="60" y2="90" stroke="url(#grad-architecture)" stroke-width="2" filter="url(#glow-architecture)"/>
    <rect x="45" y="60" width="12" height="15" stroke="url(#grad-architecture)" stroke-width="2" fill="none" filter="url(#glow-architecture)"/>
    <rect x="68" y="60" width="12" height="15" stroke="url(#grad-architecture)" stroke-width="2" fill="none" filter="url(#glow-architecture)"/>
</svg>'''
    },
    'medical': {
        'gradient': '#3B82F6, #60A5FA',
        'svg': '''<svg width="120" height="120" viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="grad-medical" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#3B82F6;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#60A5FA;stop-opacity:1" />
        </linearGradient>
        <filter id="glow-medical">
            <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
            <feMerge>
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
    </defs>
    <!-- Medical cross -->
    <rect x="52" y="30" width="16" height="60" rx="2" fill="url(#grad-medical)" filter="url(#glow-medical)"/>
    <rect x="37" y="45" width="46" height="16" rx="2" fill="url(#grad-medical)" filter="url(#glow-medical)"/>
    <!-- Heartbeat line -->
    <path d="M 25 95 L 40 95 L 45 85 L 50 105 L 55 95 L 95 95" stroke="url(#grad-medical)" stroke-width="2" fill="none" filter="url(#glow-medical)"/>
</svg>'''
    },
    'cybersecurity': {
        'gradient': '#EF4444, #DC2626',
        'svg': '''<svg width="120" height="120" viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="grad-cybersecurity" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#EF4444;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#DC2626;stop-opacity:1" />
        </linearGradient>
        <filter id="glow-cybersecurity">
            <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
            <feMerge>
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
    </defs>
    <!-- Shield -->
    <path d="M 60 25 L 35 40 L 35 60 C 35 75 45 87 60 95 C 75 87 85 75 85 60 L 85 40 Z" stroke="url(#grad-cybersecurity)" stroke-width="3" fill="none" filter="url(#glow-cybersecurity)"/>
    <!-- Lock inside shield -->
    <rect x="52" y="55" width="16" height="18" rx="2" stroke="url(#grad-cybersecurity)" stroke-width="2" fill="none" filter="url(#glow-cybersecurity)"/>
    <path d="M 55 55 L 55 50 C 55 46 57 44 60 44 C 63 44 65 46 65 50 L 65 55" stroke="url(#grad-cybersecurity)" stroke-width="2" fill="none" filter="url(#glow-cybersecurity)"/>
</svg>'''
    }
}

# Generate SVG files
print("🎨 Creating neon SVG icons for categories...\n")

for category, data in category_icons.items():
    filename = f"{category}-neon.svg"
    filepath = os.path.join(assets_path, filename)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(data['svg'])

    print(f"✓ Created: {filename}")

print(f"\n✅ All neon SVG icons created!")
print(f"📁 Location: {assets_path}/")
