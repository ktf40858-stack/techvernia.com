#!/usr/bin/env python3
"""
Script pour corriger les attributs data-i18n manquants restants
"""

import re

def fix_remaining_i18n():
    """Corrige les attributs data-i18n manquants"""

    file_path = "GenuisNet.ai/index.html"

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # 1. Stats labels - utiliser une approche différente
    # Trouver toutes les occurrences de <span class="mini-stat-label">...</span>
    # dans la section spotlight

    # Diviser le contenu en sections
    spotlight_start = content.find('<!-- AI of the Moment - Rotating Showcase -->')
    spotlight_end = content.find('<!-- Why Choose Us -->')

    if spotlight_start == -1 or spotlight_end == -1:
        print("❌ Sections non trouvées")
        return

    before_spotlight = content[:spotlight_start]
    spotlight_section = content[spotlight_start:spotlight_end]
    after_spotlight = content[spotlight_end:]

    # Remplacements des stat labels
    stat_labels = [
        ('Context Window', 'section.context-window'),
        ('Coding Benchmarks', 'section.coding-benchmarks'),
        ('Max Resolution', 'section.max-resolution'),
        ('Users', 'section.users'),
        ('Faster Coding', 'section.faster-coding'),
        ('Languages', 'section.languages'),
        ('Max Duration', 'section.max-duration'),
        ('Resolution', 'section.resolution'),
        ('Voices', 'section.voices'),
    ]

    for label, key in stat_labels:
        # Pattern pour trouver les labels sans data-i18n
        pattern = f'<span class="mini-stat-label">{re.escape(label)}</span>'
        replacement = f'<span class="mini-stat-label"><span data-i18n="{key}">{label}</span></span>'

        # Remplacer uniquement si ce n'est pas déjà fait
        if pattern in spotlight_section:
            count = spotlight_section.count(pattern)
            spotlight_section = spotlight_section.replace(pattern, replacement)
            print(f"✅ {label}: {count}x remplacé par {key}")

    # 2. Descriptions
    descriptions = [
        (
            'Claude by Anthropic represents the cutting edge of conversational AI. With its massive 200K token context window and exceptional coding abilities, it\'s revolutionizing how we interact with AI assistants.',
            'section.claude-by-anthropic-represents'
        ),
        (
            'Midjourney leads the AI art revolution with stunning, photorealistic image generation. From concept art to marketing materials, it transforms simple text prompts into professional-grade visuals.',
            'section.midjourney-leads-the-ai-art-re'
        ),
        (
            'Cursor is revolutionizing software development with its AI-first approach. Write code with natural language, refactor entire codebases, and debug faster than ever before.',
            'section.cursor-is-revolutionizing-soft'
        ),
        (
            'ChatGPT by OpenAI sparked the AI revolution. From writing and coding to analysis and creativity, it\'s the most versatile AI assistant available today.',
            'section.chatgpt-by-openai-sparked-the-'
        ),
        (
            'Runway is pushing the boundaries of AI video generation. Create cinematic videos from text, extend footage seamlessly, and edit with unprecedented creative control.',
            'section.runway-is-pushing-the-boundari'
        ),
        (
            'ElevenLabs delivers the most natural-sounding AI voices on the market. Perfect for audiobooks, podcasts, video narration, and multilingual content creation.',
            'section.elevenlabs-delivers-the-most-n'
        ),
    ]

    for desc, key in descriptions:
        # Pattern pour trouver les descriptions sans data-i18n
        pattern = f'<p class="spotlight-description">\n                            {re.escape(desc)}\n                        </p>'

        if pattern in spotlight_section:
            replacement = f'<p class="spotlight-description"><span data-i18n="{key}">{desc}</span></p>'
            spotlight_section = spotlight_section.replace(pattern, replacement)
            print(f"✅ Description ajoutée: {key}")

    # Reconstruire le contenu
    content = before_spotlight + spotlight_section + after_spotlight

    # Écrire les modifications
    if content != original_content:
        with open(file_path + '.backup3', 'w', encoding='utf-8') as f:
            f.write(original_content)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print("\n✅ Corrections appliquées!")
        print("📝 Backup créé: index.html.backup3")
    else:
        print("\nℹ️  Aucune modification nécessaire")

if __name__ == "__main__":
    fix_remaining_i18n()
