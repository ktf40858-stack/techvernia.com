#!/usr/bin/env python3
"""
Script pour ajouter tous les attributs data-i18n manquants dans la section spotlight
"""

import re

def add_all_spotlight_i18n():
    """Ajoute tous les attributs data-i18n manquants"""

    file_path = "GenuisNet.ai/index.html"

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Trouver la section spotlight
    spotlight_start = content.find('<!-- AI of the Moment - Rotating Showcase -->')
    spotlight_end = content.find('<!-- Why Choose Us -->')

    if spotlight_start == -1 or spotlight_end == -1:
        print("❌ Sections non trouvées")
        return

    before_spotlight = content[:spotlight_start]
    spotlight_section = content[spotlight_start:spotlight_end]
    after_spotlight = content[spotlight_end:]

    # 1. Midjourney stats
    spotlight_section = re.sub(
        r'<span class="mini-stat-label">Max Resolution</span>',
        r'<span class="mini-stat-label"><span data-i18n="section.max-resolution">Max Resolution</span></span>',
        spotlight_section
    )

    spotlight_section = re.sub(
        r'<span class="mini-stat-label">Users</span>',
        r'<span class="mini-stat-label"><span data-i18n="section.users">Users</span></span>',
        spotlight_section
    )

    # 2. Midjourney description
    spotlight_section = re.sub(
        r'<p class="spotlight-description">\n                            Midjourney leads the AI art revolution with stunning, photorealistic image generation\. From concept art to marketing materials, it transforms simple text prompts into professional-grade visuals\.\n                        </p>',
        r'<p class="spotlight-description"><span data-i18n="section.midjourney-leads-the-ai-art-re">Midjourney leads the AI art revolution with stunning, photorealistic image generation. From concept art to marketing materials, it transforms simple text prompts into professional-grade visuals.</span></p>',
        spotlight_section
    )

    # 3. Cursor stats
    spotlight_section = re.sub(
        r'<span class="mini-stat-label">Faster Coding</span>',
        r'<span class="mini-stat-label"><span data-i18n="section.faster-coding">Faster Coding</span></span>',
        spotlight_section
    )

    spotlight_section = re.sub(
        r'<span class="mini-stat-label">Languages</span>',
        r'<span class="mini-stat-label"><span data-i18n="section.languages">Languages</span></span>',
        spotlight_section
    )

    # 4. Cursor description
    spotlight_section = re.sub(
        r'<p class="spotlight-description">\n                            Cursor is revolutionizing software development with its AI-first approach\. Write code with natural language, refactor entire codebases, and debug faster than ever before\.\n                        </p>',
        r'<p class="spotlight-description"><span data-i18n="section.cursor-is-revolutionizing-soft">Cursor is revolutionizing software development with its AI-first approach. Write code with natural language, refactor entire codebases, and debug faster than ever before.</span></p>',
        spotlight_section
    )

    # 5. ChatGPT description
    spotlight_section = re.sub(
        r'<p class="spotlight-description">\n                            ChatGPT by OpenAI sparked the AI revolution\. From writing and coding to analysis and creativity, it\'s the most versatile AI assistant available today\.\n                        </p>',
        r'<p class="spotlight-description"><span data-i18n="section.chatgpt-by-openai-sparked-the-">ChatGPT by OpenAI sparked the AI revolution. From writing and coding to analysis and creativity, it\'s the most versatile AI assistant available today.</span></p>',
        spotlight_section
    )

    # 6. Runway stats
    spotlight_section = re.sub(
        r'<span class="mini-stat-label">Max Duration</span>',
        r'<span class="mini-stat-label"><span data-i18n="section.max-duration">Max Duration</span></span>',
        spotlight_section
    )

    # 7. Runway description
    spotlight_section = re.sub(
        r'<p class="spotlight-description">\n                            Runway is pushing the boundaries of AI video generation\. Create cinematic videos from text, extend footage seamlessly, and edit with unprecedented creative control\.\n                        </p>',
        r'<p class="spotlight-description"><span data-i18n="section.runway-is-pushing-the-boundari">Runway is pushing the boundaries of AI video generation. Create cinematic videos from text, extend footage seamlessly, and edit with unprecedented creative control.</span></p>',
        spotlight_section
    )

    # 8. ElevenLabs stats
    spotlight_section = re.sub(
        r'<span class="mini-stat-label">Voices</span>',
        r'<span class="mini-stat-label"><span data-i18n="section.voices">Voices</span></span>',
        spotlight_section
    )

    # 9. ElevenLabs description
    spotlight_section = re.sub(
        r'<p class="spotlight-description">\n                            ElevenLabs delivers the most natural-sounding AI voices on the market\. Perfect for audiobooks, podcasts, video narration, and multilingual content creation\.\n                        </p>',
        r'<p class="spotlight-description"><span data-i18n="section.elevenlabs-delivers-the-most-n">ElevenLabs delivers the most natural-sounding AI voices on the market. Perfect for audiobooks, podcasts, video narration, and multilingual content creation.</span></p>',
        spotlight_section
    )

    # Reconstruire le contenu
    content = before_spotlight + spotlight_section + after_spotlight

    # Compter les modifications
    changes_made = []
    if 'data-i18n="section.max-resolution"' in spotlight_section:
        changes_made.append("Max Resolution")
    if 'data-i18n="section.users"' in spotlight_section:
        changes_made.append("Users")
    if 'data-i18n="section.faster-coding"' in spotlight_section:
        changes_made.append("Faster Coding")
    if 'data-i18n="section.languages"' in spotlight_section:
        changes_made.append("Languages")
    if 'data-i18n="section.max-duration"' in spotlight_section:
        changes_made.append("Max Duration")
    if 'data-i18n="section.voices"' in spotlight_section:
        changes_made.append("Voices")

    # Écrire les modifications
    if content != original_content:
        with open(file_path + '.backup4', 'w', encoding='utf-8') as f:
            f.write(original_content)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print("✅ Modifications appliquées!")
        print("📝 Backup créé: index.html.backup4")
        print(f"📊 Éléments modifiés: {', '.join(changes_made)}")
    else:
        print("ℹ️  Aucune modification nécessaire")

if __name__ == "__main__":
    add_all_spotlight_i18n()
