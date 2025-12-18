#!/usr/bin/env python3
"""
Script pour ajouter les meilleurs AI tools manquants dans chaque catégorie
"""

# Liste des meilleurs AI tools à ajouter par catégorie
BEST_AI_TOOLS = {
    'ai-chatbots.html': [
        {
            'name': 'Grok',
            'company': 'xAI',
            'country': '🇺🇸',
            'rating': '4.5',
            'badge': 'X Integration',
            'description': "Grok is xAI's conversational AI with real-time access to X (Twitter) data. Created by Elon Musk's team, it offers unique insights from social media and current events.",
            'features': ['Grok-2', 'Real-time X Data', 'Humor Mode', 'Current Events', 'Uncensored'],
            'price': '$16/mo',
        }
    ],
    'ai-coding.html': [
        {
            'name': 'DeepSeek Coder',
            'company': 'DeepSeek AI',
            'country': '🇨🇳',
            'rating': '4.8',
            'badge': 'Best Value',
            'description': "DeepSeek Coder is a highly efficient code generation model that rivals GitHub Copilot. Open-source, cost-effective, and excellent for multiple programming languages.",
            'features': ['DeepSeek-Coder-V2', '236B Parameters', '128K Context', 'Multi-language', 'Open Source'],
            'price': '$0.14/1M tokens',
        },
        {
            'name': 'Windsurf',
            'company': 'Codeium',
            'country': '🇺🇸',
            'rating': '4.7',
            'badge': 'New & Free',
            'description': "Windsurf is Codeium's new AI IDE with advanced flow state features. Completely free and offers real-time collaboration between you and AI.",
            'features': ['Free Forever', 'Flow State', 'Cascade AI', 'Multi-file Edit', 'VS Code Compatible'],
            'price': 'Free',
        }
    ],
    'ai-image.html': [
        {
            'name': 'Ideogram',
            'company': 'Ideogram',
            'country': '🇺🇸',
            'rating': '4.6',
            'badge': 'Best for Text',
            'description': "Ideogram excels at generating text within images, a weakness of most AI image generators. Great for posters, logos, and designs with typography.",
            'features': ['Ideogram 2.0', 'Perfect Text', 'Magic Prompt', 'Style Transfer', 'Free Tier'],
            'price': 'Free / $8-20/mo',
        }
    ],
    'ai-video.html': [
        {
            'name': 'Kling AI',
            'company': 'Kuaishou',
            'country': '🇨🇳',
            'rating': '4.7',
            'badge': 'Long Videos',
            'description': "Kling AI from China creates impressive long-form videos up to 2 minutes. Known for realistic motion and physics simulation.",
            'features': ['Kling 1.5', '2-min Videos', 'Realistic Physics', '1080p Output', 'Free Credits'],
            'price': 'Free credits / Pay-as-go',
        }
    ],
}

print("=" * 70)
print("📋 LISTE DES MEILLEURS AI TOOLS À AJOUTER")
print("=" * 70)
print()

for category, tools in BEST_AI_TOOLS.items():
    print(f"\n🔹 {category}:")
    for tool in tools:
        print(f"   • {tool['name']} {tool['country']} - {tool['company']}")
        print(f"     Rating: {tool['rating']}★ | Badge: {tool['badge']}")
        print(f"     Price: {tool['price']}")

print("\n" + "=" * 70)
print("Total AI tools à ajouter:", sum(len(tools) for tools in BEST_AI_TOOLS.values()))
print("=" * 70)
