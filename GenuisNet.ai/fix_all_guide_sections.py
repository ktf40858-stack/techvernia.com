#!/usr/bin/env python3
"""
Script to properly insert Beginner and Intermediate guide cards
"""

import re
from pathlib import Path

def create_guide_card(title, description, time, lessons, icon_path, gradient_id, gradient_start, gradient_end, glow_rgb):
    """Generate HTML for a single guide card."""
    return f'''                <div class="guide-card" style="cursor: default;">
                    <div class="guide-card-header">
                        <div class="guide-icon-container">
                            <div class="guide-icon-neon" style="background: linear-gradient(135deg, rgba({glow_rgb}, 0.1), rgba({glow_rgb}, 0.1)); border: 2px solid rgba({glow_rgb}, 0.3); --glow-rgb: {glow_rgb}; animation: glow 3s ease-in-out infinite;">
                                <svg viewBox="0 0 24 24" fill="none" stroke="url(#{gradient_id})" stroke-width="1.5" width="60" height="60" style="filter: drop-shadow(0 0 12px rgba({glow_rgb}, 0.8));">
                                    {icon_path}
                                </svg>
                                <svg width="0" height="0" style="position: absolute;">
                                    <defs>
                                        <linearGradient id="{gradient_id}" x1="0%" y1="0%" x2="100%" y2="100%">
                                            <stop offset="0%" style="stop-color:{gradient_start}"/>
                                            <stop offset="100%" style="stop-color:{gradient_end}"/>
                                        </linearGradient>
                                    </defs>
                                </svg>
                            </div>
                        </div>
                        <h3>{title}</h3>
                    </div>
                    <p class="guide-description">{description}</p>
                    <div class="guide-meta">
                        <span class="meta-item">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <circle cx="12" cy="12" r="10"/>
                                <path d="M12 6v6l4 2"/>
                            </svg>
                            {time}
                        </span>
                        <span class="meta-item">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/>
                                <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>
                            </svg>
                            {lessons}
                        </span>
                    </div>
                </div>
'''

def main():
    """Insert Beginner and Intermediate guide cards."""

    # Beginner Guides (Green theme)
    beginner_guides = [
        ("AI Fundamentals", "Master the core concepts of artificial intelligence, machine learning, and neural networks", "20 min", "5 lessons",
         '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/>', "grad-beginner-1", "#22C55E", "#10B981", "34, 197, 94"),

        ("Getting Started with ChatGPT", "Learn how to use ChatGPT effectively for writing, coding, and problem-solving", "25 min", "6 lessons",
         '<path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>', "grad-beginner-2", "#22C55E", "#10B981", "34, 197, 94"),

        ("Introduction to Image AI", "Discover how to create stunning visuals with DALL-E, Midjourney, and Stable Diffusion", "30 min", "7 lessons",
         '<rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/>', "grad-beginner-3", "#22C55E", "#10B981", "34, 197, 94"),

        ("AI Writing Tools Basics", "Master AI-powered writing assistants for content creation and editing", "18 min", "4 lessons",
         '<path d="M12 19l7-7 3 3-7 7-3-3z"/><path d="M18 13l-1.5-7.5L2 2l3.5 14.5L13 18l5-5z"/><path d="M2 2l7.586 7.586"/>', "grad-beginner-4", "#22C55E", "#10B981", "34, 197, 94"),

        ("Understanding AI Models", "Learn about different types of AI models and their applications", "22 min", "5 lessons",
         '<path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>', "grad-beginner-5", "#22C55E", "#10B981", "34, 197, 94"),

        ("AI Safety & Ethics 101", "Explore responsible AI use and ethical considerations", "15 min", "4 lessons",
         '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>', "grad-beginner-6", "#22C55E", "#10B981", "34, 197, 94"),

        ("Prompt Engineering Basics", "Learn to write effective prompts for better AI outputs", "28 min", "6 lessons",
         '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>', "grad-beginner-7", "#22C55E", "#10B981", "34, 197, 94"),

        ("AI for Personal Productivity", "Boost your daily efficiency with AI tools and techniques", "20 min", "5 lessons",
         '<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><path d="M22 4L12 14.01l-3-3"/>', "grad-beginner-8", "#22C55E", "#10B981", "34, 197, 94"),

        ("Voice & Audio AI Intro", "Get started with AI voice generation and audio processing", "25 min", "6 lessons",
         '<path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2M12 19v4M8 23h8"/>', "grad-beginner-9", "#22C55E", "#10B981", "34, 197, 94"),

        ("AI Tools Comparison Guide", "Compare popular AI tools to find the best fit for your needs", "30 min", "7 lessons",
         '<path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/>', "grad-beginner-10", "#22C55E", "#10B981", "34, 197, 94"),
    ]

    # Intermediate Guides (Blue theme)
    intermediate_guides = [
        ("API Integration Mastery", "Connect AI capabilities to your applications via APIs", "38 min", "9 lessons",
         '<path d="M16 18l2-2-2-2M8 6L6 8l2 2"/><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"/>', "grad-inter-2", "#3B82F6", "#2563EB", "59, 130, 246"),

        ("Multimodal AI Applications", "Combine text, image, and audio AI for powerful solutions", "42 min", "10 lessons",
         '<path d="M3 3v18h18M7 16l4-4 4 4 6-6"/>', "grad-inter-3", "#3B82F6", "#2563EB", "59, 130, 246"),

        ("AI Content Strategy", "Develop professional content workflows using AI tools", "35 min", "8 lessons",
         '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M16 13H8M16 17H8M10 9H8"/>', "grad-inter-4", "#3B82F6", "#2563EB", "59, 130, 246"),

        ("AI Data Analysis", "Leverage AI for advanced data processing and insights", "40 min", "9 lessons",
         '<path d="M3 3v18h18"/><path d="M18 17V9M13 17V5M8 17v-3"/>', "grad-inter-5", "#3B82F6", "#2563EB", "59, 130, 246"),

        ("Building AI Chatbots", "Create custom chatbots for business and personal use", "45 min", "10 lessons",
         '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/><path d="M9 10h.01M15 10h.01M12 14h.01"/>', "grad-inter-6", "#3B82F6", "#2563EB", "59, 130, 246"),

        ("AI Video & Animation", "Master AI tools for video creation and editing", "38 min", "9 lessons",
         '<path d="M23 7l-7 5 7 5V7z"/><rect x="1" y="5" width="15" height="14" rx="2" ry="2"/>', "grad-inter-7", "#3B82F6", "#2563EB", "59, 130, 246"),

        ("AI Testing & Optimization", "Learn to test, benchmark, and improve AI outputs", "35 min", "8 lessons",
         '<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><path d="M22 4L12 14.01l-3-3"/>', "grad-inter-8", "#3B82F6", "#2563EB", "59, 130, 246"),

        ("Custom AI Training Basics", "Learn to fine-tune AI models for specialized tasks", "45 min", "10 lessons",
         '<rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>', "grad-inter-9", "#3B82F6", "#2563EB", "59, 130, 246"),

        ("AI Workflow Automation", "Build automated workflows combining multiple AI tools", "40 min", "9 lessons",
         '<path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><path d="M12 22V12M22 8.5l-10 5.75M2 8.5l10 5.75"/>', "grad-inter-10", "#3B82F6", "#2563EB", "59, 130, 246"),
    ]

    # Generate HTML
    beginner_html = '\n'.join([create_guide_card(*guide) for guide in beginner_guides])
    intermediate_html = '\n'.join([create_guide_card(*guide) for guide in intermediate_guides])

    # Read the file
    file_path = Path('/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/guides.html')
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Insert Beginner guides right after the Beginner section header
    # Look for the section-divider closing </div> followed by empty space before Advanced section
    beginner_pattern = r'(<!-- Section: Beginner Guides -->.*?</div>\s*\n\s*\n)(\s*<!-- Section: Advanced Guides -->)'
    beginner_replacement = r'\1            <div class="guides-grid">\n' + beginner_html + '\n            </div>\n\n\2'
    content = re.sub(beginner_pattern, beginner_replacement, content, flags=re.DOTALL)

    # Insert Intermediate guides after the existing intermediate guide card
    # Find the last closing </div> of the existing intermediate card and add more cards
    intermediate_pattern = r'(<!-- Section: Intermediate Guides -->.*?<div class="guides-grid">.*?</div>\s*</div>)(\s*</div>)'

    # First, let's find and replace more carefully
    # Look for the intermediate section and insert after the first guide card
    lines = content.split('\n')
    new_lines = []
    in_intermediate_grid = False
    intermediate_card_count = 0
    inserted_intermediate = False

    for i, line in enumerate(lines):
        new_lines.append(line)

        # Check if we're in the intermediate guides section
        if 'Intermediate Guides' in ''.join(lines[max(0, i-20):i]):
            if '<div class="guides-grid">' in line:
                in_intermediate_grid = True

        # Count guide cards in intermediate section
        if in_intermediate_grid and '</div>' in line and 'guide-card' in ''.join(lines[max(0, i-50):i]):
            # Check if this is the closing div of a guide-card
            depth = 0
            for j in range(i, max(0, i-100), -1):
                if '</div>' in lines[j]:
                    depth += 1
                if '<div class="guide-card"' in lines[j]:
                    depth -= 1
                    if depth == 0:
                        # This is indeed a guide-card closing
                        intermediate_card_count += 1
                        if intermediate_card_count == 1 and not inserted_intermediate:
                            # Insert after first card
                            new_lines.append('\n' + intermediate_html)
                            inserted_intermediate = True
                            in_intermediate_grid = False
                        break

    content = '\n'.join(new_lines)

    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ Inserted 10 Beginner guides")
    print("✅ Inserted 9 additional Intermediate guides (10 total)")
    print(f"\n🎉 All guide sections now populated!")

if __name__ == '__main__':
    main()
