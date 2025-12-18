#!/usr/bin/env python3
"""
Script pour ajouter les attributs data-i18n manquants dans la section "AI of the Moment"
et "Why GenuisNet.ai"
"""

import re

def add_i18n_attributes():
    """Ajoute les attributs data-i18n manquants dans index.html"""

    file_path = "GenuisNet.ai/index.html"

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # 1. Badge "AI of the Moment"
    content = re.sub(
        r'<div class="spotlight-badge">AI of the Moment</div>',
        r'<div class="spotlight-badge"><span data-i18n="section.ai-of-the-moment">AI of the Moment</span></div>',
        content
    )

    # 2. Taglines
    content = re.sub(
        r'<p class="spotlight-tagline">The AI assistant that thinks before it speaks</p>',
        r'<p class="spotlight-tagline"><span data-i18n="section.the-ai-assistant-that-thinks-b">The AI assistant that thinks before it speaks</span></p>',
        content
    )

    content = re.sub(
        r'<p class="spotlight-tagline">The most realistic AI voices</p>',
        r'<p class="spotlight-tagline"><span data-i18n="section.the-most-realistic-ai-voices">The most realistic AI voices</span></p>',
        content
    )

    content = re.sub(
        r'<p class="spotlight-tagline">The AI-first code editor</p>',
        r'<p class="spotlight-tagline"><span data-i18n="section.the-ai-first-code-editor">The AI-first code editor</span></p>',
        content
    )

    content = re.sub(
        r'<p class="spotlight-tagline">The AI that started it all</p>',
        r'<p class="spotlight-tagline"><span data-i18n="section.the-ai-that-started-it-all">The AI that started it all</span></p>',
        content
    )

    # 3. Stats labels
    stat_labels = {
        'Context Window': 'section.context-window',
        'Coding Benchmarks': 'section.coding-benchmarks',
        'Max Resolution': 'section.max-resolution',
        'Users': 'section.users',
        'Rating': 'section.rating',
        'Voices': 'section.voices',
        'Languages': 'section.languages',
        'Faster Coding': 'section.faster-coding',
        'Prompts/Day': 'section.prompts-day',
        'Scenes/Min': 'section.scenes-min',
        'Video Quality': 'section.video-quality',
    }

    for label, key in stat_labels.items():
        # Pour éviter de matcher plusieurs fois le même pattern, on utilise un pattern plus spécifique
        pattern = f'<span class="mini-stat-label">{re.escape(label)}</span>'
        replacement = f'<span class="mini-stat-label"><span data-i18n="{key}">{label}</span></span>'

        # On limite le remplacement à la section spotlight
        # D'abord, on trouve la section spotlight
        spotlight_start = content.find('<!-- AI of the Moment - Rotating Showcase -->')
        spotlight_end = content.find('<!-- Why Choose Us -->')

        if spotlight_start != -1 and spotlight_end != -1:
            before = content[:spotlight_start]
            spotlight_section = content[spotlight_start:spotlight_end]
            after = content[spotlight_end:]

            spotlight_section = spotlight_section.replace(pattern, replacement)
            content = before + spotlight_section + after

    # 4. Descriptions
    descriptions = {
        'Claude by Anthropic represents the cutting edge of conversational AI. With its massive 200K token context window and exceptional coding abilities, it\'s revolutionizing how we interact with AI assistants.':
            'section.claude-by-anthropic-represents',
        'Midjourney leads the AI art revolution with stunning, photorealistic image generation. From concept art to marketing materials, it transforms simple text prompts into professional-grade visuals.':
            'section.midjourney-leads-the-ai-art-re',
        'ElevenLabs delivers the most natural-sounding AI voices on the market. Perfect for audiobooks, podcasts, video narration, and multilingual content creation.':
            'section.elevenlabs-delivers-the-most-n',
    }

    for desc, key in descriptions.items():
        pattern = f'<p class="spotlight-description">\n                            {re.escape(desc)}\n                        </p>'
        replacement = f'<p class="spotlight-description"><span data-i18n="{key}">{desc}</span></p>'
        content = content.replace(pattern, replacement)

    # 5. Boutons "Read Full Review" sans data-i18n
    content = re.sub(
        r'<a class="btn btn-primary" href="([^"]+)">Read Full Review</a>',
        r'<a class="btn btn-primary" href="\1"><span data-i18n="btn.read-full-review">Read Full Review</span></a>',
        content
    )

    # 6. Section "Why GenuisNet.ai"
    content = re.sub(
        r'<h2 class="section-title">Why GenuisNet\.ai\?</h2>',
        r'<h2 class="section-title"><span data-i18n="section.why-genuisnetai">Why GenuisNet.ai?</span></h2>',
        content
    )

    content = re.sub(
        r'<p class="section-subtitle">Your trusted companion in the AI journey</p>',
        r'<p class="section-subtitle"><span data-i18n="section.your-trusted-companion-in-the-">Your trusted companion in the AI journey</span></p>',
        content
    )

    # 7. Why items
    why_items = {
        'Comprehensive Coverage': 'section.comprehensive-coverage',
        'Real-World Testing': 'section.real-world-testing',
        'Practical Guides': 'section.practical-guides',
        'Community Driven': 'section.community-driven',
    }

    for title, key in why_items.items():
        content = re.sub(
            f'<h4>{re.escape(title)}</h4>',
            f'<h4><span data-i18n="{key}">{title}</span></h4>',
            content
        )

    # Descriptions des why items
    why_descs = {
        'From ChatGPT to specialized enterprise solutions, we cover every AI tool that matters':
            'section.from-chatgpt-to-specialized-en',
        'Every tool is tested in actual workflows, not just theoretical benchmarks':
            'section.every-tool-is-tested-in-actual',
        'Step-by-step tutorials and comparisons to help you make informed decisions':
            'section.step-by-step-tutorials-and-com',
        'Ratings and reviews from a global community of AI enthusiasts':
            'section.ratings-and-reviews-from-a-glo',
    }

    for desc, key in why_descs.items():
        pattern = f'<p>{re.escape(desc)}</p>'
        replacement = f'<p><span data-i18n="{key}">{desc}</span></p>'

        # Limiter au contexte de la section "Why Choose Us"
        why_start = content.find('<!-- Why Choose Us -->')
        why_end = content.find('<!-- Call to Action -->')

        if why_start != -1 and why_end != -1:
            before = content[:why_start]
            why_section = content[why_start:why_end]
            after = content[why_end:]

            why_section = why_section.replace(pattern, replacement)
            content = before + why_section + after

    # Comparer avec le contenu original
    if content != original_content:
        # Créer un backup
        with open(file_path + '.backup2', 'w', encoding='utf-8') as f:
            f.write(original_content)

        # Écrire les modifications
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print("✅ Modifications appliquées avec succès!")
        print("📝 Backup créé: index.html.backup2")

        # Compter les changements
        changes = sum(1 for a, b in zip(original_content, content) if a != b)
        print(f"📊 Nombre de caractères modifiés: {changes}")
    else:
        print("ℹ️  Aucune modification nécessaire")

if __name__ == "__main__":
    add_i18n_attributes()
