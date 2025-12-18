#!/usr/bin/env python3
"""
Script to update all category pages with:
1. Neon gaming SVG icons for category cards (replacing emojis)
2. Country flags next to ratings for each AI tool
"""

import re
import os

# Mapping of AI tools to their country flags
AI_COUNTRIES = {
    # Chatbots
    'ChatGPT': '🇺🇸',  # OpenAI - USA
    'Claude': '🇺🇸',  # Anthropic - USA
    'Google Gemini': '🇺🇸',  # Google - USA
    'Gemini': '🇺🇸',  # Google - USA
    'Perplexity': '🇺🇸',  # USA
    'Microsoft Copilot': '🇺🇸',  # Microsoft - USA
    'Copilot': '🇺🇸',  # Microsoft - USA
    'Poe': '🇺🇸',  # Quora - USA
    'DeepSeek': '🇨🇳',  # China

    # Coding
    'GitHub Copilot': '🇺🇸',
    'Cursor': '🇺🇸',
    'Codeium': '🇺🇸',
    'Tabnine': '🇮🇱',  # Israel
    'Replit': '🇺🇸',
    'Amazon CodeWhisperer': '🇺🇸',
    'CodeWhisperer': '🇺🇸',

    # Video
    'Runway': '🇺🇸',
    'HeyGen': '🇨🇳',  # China
    'Synthesia': '🇬🇧',  # UK
    'Sora': '🇺🇸',  # OpenAI

    # Image
    'Midjourney': '🇺🇸',
    'DALL-E': '🇺🇸',
    'Stable Diffusion': '🇬🇧',  # Stability AI - UK
    'Flux': '🇺🇸',

    # Audio
    'ElevenLabs': '🇺🇸',
    'Suno': '🇺🇸',
    'Udio': '🇺🇸',
    'Murf AI': '🇺🇸',

    # Networking
    'Cisco AI': '🇺🇸',
    'Juniper Mist': '🇺🇸',
    'Mist AI': '🇺🇸',
    'Datadog': '🇺🇸',
    'Splunk': '🇺🇸',
    'Ansible': '🇺🇸',
    'Terraform': '🇺🇸',
    'PRTG': '🇩🇪',  # Germany
    'Zabbix': '🇱🇻',  # Latvia

    # Cybersecurity
    'CrowdStrike': '🇺🇸',
    'Darktrace': '🇬🇧',  # UK
    'SentinelOne': '🇺🇸',
    'Palo Alto': '🇺🇸',
    'Fortinet': '🇺🇸',
    'Splunk Security': '🇺🇸',
    'Microsoft Sentinel': '🇺🇸',
    'Wiz': '🇺🇸',
    'Snyk': '🇬🇧',  # UK
    'CyberArk': '🇮🇱',  # Israel
    'Okta': '🇺🇸',
    'Tenable': '🇺🇸',
    'Qualys': '🇺🇸',
    'Rapid7': '🇺🇸',
    'Vectra AI': '🇺🇸',
    'Lacework': '🇺🇸',
    'Abnormal Security': '🇺🇸',
    'Cortex XDR': '🇺🇸',  # Palo Alto
    'IBM QRadar': '🇺🇸',
    'Cisco SecureX': '🇺🇸',
    'Cylance': '🇺🇸',
}

# SVG icons for categories (neon gaming style)
SVG_ICONS = {
    'writing': '''<svg viewBox="0 0 24 24" fill="none" stroke="url(#gradient-writing)" stroke-width="1.5">
                            <path d="M12 19l7-7 3 3-7 7-3-3z"/>
                            <path d="M18 13l-1.5-7.5L2 2l3.5 14.5L13 18l5-5z"/>
                            <path d="M2 2l7.586 7.586"/>
                            <circle cx="11" cy="11" r="2"/>
                        </svg>''',
    'coding': '''<svg viewBox="0 0 24 24" fill="none" stroke="url(#gradient-coding)" stroke-width="1.5">
                            <polyline points="16 18 22 12 16 6"/>
                            <polyline points="8 6 2 12 8 18"/>
                        </svg>''',
    'productivity': '''<svg viewBox="0 0 24 24" fill="none" stroke="url(#gradient-productivity)" stroke-width="1.5">
                            <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>
                        </svg>''',
    'image': '''<svg viewBox="0 0 24 24" fill="none" stroke="url(#gradient-image)" stroke-width="1.5">
                            <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
                            <circle cx="8.5" cy="8.5" r="1.5"/>
                            <polyline points="21 15 16 10 5 21"/>
                        </svg>''',
    'video': '''<svg viewBox="0 0 24 24" fill="none" stroke="url(#gradient-video)" stroke-width="1.5">
                            <polygon points="23 7 16 12 23 17 23 7"/>
                            <rect x="1" y="5" width="15" height="14" rx="2" ry="2"/>
                        </svg>''',
    'audio': '''<svg viewBox="0 0 24 24" fill="none" stroke="url(#gradient-audio)" stroke-width="1.5">
                            <path d="M9 18V5l12-2v13"/>
                            <circle cx="6" cy="18" r="3"/>
                            <circle cx="18" cy="16" r="3"/>
                        </svg>''',
    'chatbots': '''<svg viewBox="0 0 24 24" fill="none" stroke="url(#gradient-chatbots)" stroke-width="1.5">
                            <path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>
                            <path d="M8 12h.01M12 12h.01M16 12h.01" stroke-linecap="round"/>
                        </svg>''',
    'seo': '''<svg viewBox="0 0 24 24" fill="none" stroke="url(#gradient-seo)" stroke-width="1.5">
                            <line x1="18" y1="20" x2="18" y2="10"/>
                            <line x1="12" y1="20" x2="12" y2="4"/>
                            <line x1="6" y1="20" x2="6" y2="14"/>
                            <path d="M3 20h18"/>
                        </svg>''',
    'business': '''<svg viewBox="0 0 24 24" fill="none" stroke="url(#gradient-business)" stroke-width="1.5">
                            <rect x="2" y="7" width="20" height="14" rx="2" ry="2"/>
                            <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>
                        </svg>''',
    'networking': '''<svg viewBox="0 0 24 24" fill="none" stroke="url(#gradient-networking)" stroke-width="1.5">
                            <rect x="9" y="9" width="6" height="6" rx="1"/>
                            <path d="M5 9a2 2 0 0 1 2-2h1"/>
                            <path d="M5 15a2 2 0 0 0 2 2h1"/>
                            <path d="M19 9a2 2 0 0 0-2-2h-1"/>
                            <path d="M19 15a2 2 0 0 1-2 2h-1"/>
                            <path d="M5 12H3"/>
                            <path d="M21 12h-2"/>
                            <path d="M12 5V3"/>
                            <path d="M12 21v-2"/>
                        </svg>''',
    'cybersecurity': '''<svg viewBox="0 0 24 24" fill="none" stroke="url(#gradient-cybersecurity)" stroke-width="1.5">
                            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                            <path d="M9 12l2 2 4-4"/>
                        </svg>''',
}

# Gradient definitions
GRADIENTS_SVG = '''<!-- SVG Gradients for Neon Icons -->
            <svg width="0" height="0" style="position:absolute">
                <defs>
                    <linearGradient id="gradient-chatbots" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:#00D9FF"/>
                        <stop offset="100%" style="stop-color:#0066FF"/>
                    </linearGradient>
                    <linearGradient id="gradient-writing" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:#A855F7"/>
                        <stop offset="100%" style="stop-color:#6366F1"/>
                    </linearGradient>
                    <linearGradient id="gradient-image" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:#F472B6"/>
                        <stop offset="100%" style="stop-color:#EC4899"/>
                    </linearGradient>
                    <linearGradient id="gradient-video" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:#FB923C"/>
                        <stop offset="100%" style="stop-color:#F97316"/>
                    </linearGradient>
                    <linearGradient id="gradient-audio" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:#4ADE80"/>
                        <stop offset="100%" style="stop-color:#22C55E"/>
                    </linearGradient>
                    <linearGradient id="gradient-coding" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:#38BDF8"/>
                        <stop offset="100%" style="stop-color:#0EA5E9"/>
                    </linearGradient>
                    <linearGradient id="gradient-productivity" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:#FACC15"/>
                        <stop offset="100%" style="stop-color:#EAB308"/>
                    </linearGradient>
                    <linearGradient id="gradient-seo" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:#34D399"/>
                        <stop offset="100%" style="stop-color:#10B981"/>
                    </linearGradient>
                    <linearGradient id="gradient-business" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:#818CF8"/>
                        <stop offset="100%" style="stop-color:#6366F1"/>
                    </linearGradient>
                    <linearGradient id="gradient-networking" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:#2DD4BF"/>
                        <stop offset="100%" style="stop-color:#14B8A6"/>
                    </linearGradient>
                    <linearGradient id="gradient-cybersecurity" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" style="stop-color:#F87171"/>
                        <stop offset="100%" style="stop-color:#EF4444"/>
                    </linearGradient>
                </defs>
            </svg>

'''

def add_flag_to_rating(content, tool_name):
    """Add country flag next to rating for a specific tool"""
    if tool_name not in AI_COUNTRIES:
        return content

    flag = AI_COUNTRIES[tool_name]

    # Pattern to find the rating badge and add flag
    pattern = r'(<span class="badge badge-rating">[^<]+</span>)'
    replacement = rf'\1\n                                <span class="country-flag" style="font-size: 1.2em; opacity: 0.7;">{flag}</span>'

    # Only replace once per tool
    return content.replace(pattern, replacement, 1)

print("Script de mise à jour des icônes néon et drapeaux")
print("=" * 60)
print("\nCe script va :")
print("1. Remplacer les emojis par des icônes SVG néon dans les catégories")
print("2. Ajouter les drapeaux des pays à côté des ratings")
print("\nVoulez-vous continuer? (y/n): ", end='')
