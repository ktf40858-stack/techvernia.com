#!/usr/bin/env python3
"""
Reconstruit complètement les sections de guides avec le bon HTML
"""

import re
from pathlib import Path

def create_guide_card(title, description, time, lessons, icon_path, gradient_id, color_start, color_end, glow_rgb, slug):
    """Génère le HTML pour une carte de guide."""
    return f'''                <a href="guides/{slug}.html" class="guide-card">
                    <div class="guide-card-header">
                        <div class="guide-icon-container">
                            <div class="guide-icon-neon" style="background: linear-gradient(135deg, rgba({glow_rgb}, 0.1), rgba({glow_rgb}, 0.1)); border: 2px solid rgba({glow_rgb}, 0.3); --glow-rgb: {glow_rgb}; animation: glow 3s ease-in-out infinite;">
                                <svg viewBox="0 0 24 24" fill="none" stroke="url(#{gradient_id})" stroke-width="1.5" width="60" height="60" style="filter: drop-shadow(0 0 12px rgba({glow_rgb}, 0.8));">
                                    {icon_path}
                                </svg>
                                <svg width="0" height="0" style="position: absolute;">
                                    <defs>
                                        <linearGradient id="{gradient_id}" x1="0%" y1="0%" x2="100%" y2="100%">
                                            <stop offset="0%" style="stop-color:{color_start}"/>
                                            <stop offset="100%" style="stop-color:{color_end}"/>
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
                </a>
'''

def main():
    """Reconstruit les sections."""
    file_path = Path('/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/guides.html')

    # Données des guides
    beginner_guides = [
        ('AI Fundamentals', 'Master the core concepts of artificial intelligence, machine learning, and neural networks', '20 min', '5 lessons',
         '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/>', 'grad-beginner-1', '#22C55E', '#10B981', '34, 197, 94', 'ai-fundamentals'),
        ('Getting Started with ChatGPT', 'Learn how to use ChatGPT effectively for writing, coding, and problem-solving', '25 min', '6 lessons',
         '<path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>', 'grad-beginner-2', '#22C55E', '#10B981', '34, 197, 94', 'getting-started-chatgpt'),
        ('Introduction to Image AI', 'Discover how to create stunning visuals with DALL-E, Midjourney, and Stable Diffusion', '30 min', '7 lessons',
         '<rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/>', 'grad-beginner-3', '#22C55E', '#10B981', '34, 197, 94', 'introduction-image-ai'),
        ('AI Writing Tools Basics', 'Master AI-powered writing assistants for content creation and editing', '18 min', '4 lessons',
         '<path d="M12 19l7-7 3 3-7 7-3-3z"/><path d="M18 13l-1.5-7.5L2 2l3.5 14.5L13 18l5-5z"/><path d="M2 2l7.586 7.586"/>', 'grad-beginner-4', '#22C55E', '#10B981', '34, 197, 94', 'ai-writing-tools-basics'),
        ('Understanding AI Models', 'Learn about different types of AI models and their applications', '22 min', '5 lessons',
         '<path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>', 'grad-beginner-5', '#22C55E', '#10B981', '34, 197, 94', 'understanding-ai-models'),
        ('AI Safety & Ethics 101', 'Explore responsible AI use and ethical considerations', '15 min', '4 lessons',
         '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>', 'grad-beginner-6', '#22C55E', '#10B981', '34, 197, 94', 'ai-safety-ethics-101'),
        ('Prompt Engineering Basics', 'Learn to write effective prompts for better AI outputs', '28 min', '6 lessons',
         '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>', 'grad-beginner-7', '#22C55E', '#10B981', '34, 197, 94', 'prompt-engineering-basics'),
        ('AI for Personal Productivity', 'Boost your daily efficiency with AI tools and techniques', '20 min', '5 lessons',
         '<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><path d="M22 4L12 14.01l-3-3"/>', 'grad-beginner-8', '#22C55E', '#10B981', '34, 197, 94', 'ai-personal-productivity'),
        ('Voice & Audio AI Intro', 'Get started with AI voice generation and audio processing', '25 min', '6 lessons',
         '<path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2M12 19v4M8 23h8"/>', 'grad-beginner-9', '#22C55E', '#10B981', '34, 197, 94', 'voice-audio-ai-intro'),
        ('AI Tools Comparison Guide', 'Compare popular AI tools to find the best fit for your needs', '30 min', '7 lessons',
         '<path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/>', 'grad-beginner-10', '#22C55E', '#10B981', '34, 197, 94', 'ai-tools-comparison'),
    ]

    intermediate_guides = [
        ('Advanced Prompt Engineering', 'Master complex prompting techniques for sophisticated AI interactions', '35 min', '8 lessons',
         '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>', 'grad-inter-1', '#3B82F6', '#2563EB', '59, 130, 246', 'advanced-prompt-engineering'),
        ('API Integration Mastery', 'Connect AI capabilities to your applications via APIs', '38 min', '9 lessons',
         '<path d="M16 18l2-2-2-2M8 6L6 8l2 2"/><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"/>', 'grad-inter-2', '#3B82F6', '#2563EB', '59, 130, 246', 'api-integration-mastery'),
        ('Multimodal AI Applications', 'Combine text, image, and audio AI for powerful solutions', '42 min', '10 lessons',
         '<path d="M3 3v18h18M7 16l4-4 4 4 6-6"/>', 'grad-inter-3', '#3B82F6', '#2563EB', '59, 130, 246', 'multimodal-ai-applications'),
        ('AI Content Strategy', 'Develop professional content workflows using AI tools', '35 min', '8 lessons',
         '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M16 13H8M16 17H8M10 9H8"/>', 'grad-inter-4', '#3B82F6', '#2563EB', '59, 130, 246', 'ai-content-strategy'),
        ('AI Data Analysis', 'Leverage AI for advanced data processing and insights', '40 min', '9 lessons',
         '<path d="M3 3v18h18"/><path d="M18 17V9M13 17V5M8 17v-3"/>', 'grad-inter-5', '#3B82F6', '#2563EB', '59, 130, 246', 'ai-data-analysis'),
        ('Building AI Chatbots', 'Create custom chatbots for business and personal use', '45 min', '10 lessons',
         '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/><path d="M9 10h.01M15 10h.01M12 14h.01"/>', 'grad-inter-6', '#3B82F6', '#2563EB', '59, 130, 246', 'building-ai-chatbots'),
        ('AI Video & Animation', 'Master AI tools for video creation and editing', '38 min', '9 lessons',
         '<path d="M23 7l-7 5 7 5V7z"/><rect x="1" y="5" width="15" height="14" rx="2" ry="2"/>', 'grad-inter-7', '#3B82F6', '#2563EB', '59, 130, 246', 'ai-video-animation'),
        ('AI Testing & Optimization', 'Learn to test, benchmark, and improve AI outputs', '35 min', '8 lessons',
         '<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><path d="M22 4L12 14.01l-3-3"/>', 'grad-inter-8', '#3B82F6', '#2563EB', '59, 130, 246', 'ai-testing-optimization'),
        ('Custom AI Training Basics', 'Learn to fine-tune AI models for specialized tasks', '45 min', '10 lessons',
         '<rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>', 'grad-inter-9', '#3B82F6', '#2563EB', '59, 130, 246', 'custom-ai-training'),
        ('AI Workflow Automation', 'Build automated workflows combining multiple AI tools', '40 min', '9 lessons',
         '<path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><path d="M12 22V12M22 8.5l-10 5.75M2 8.5l10 5.75"/>', 'grad-inter-10', '#3B82F6', '#2563EB', '59, 130, 246', 'ai-workflow-automation'),
    ]

    advanced_guides = [
        ('Enterprise AI Architecture', 'Design scalable AI systems for large organizations', '50 min', '12 lessons',
         '<path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/>', 'grad-adv-1', '#A855F7', '#7C3AED', '168, 85, 247', 'enterprise-ai-architecture'),
        ('AI Model Development', 'Build and deploy custom AI models from scratch', '60 min', '14 lessons',
         '<rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>', 'grad-adv-2', '#A855F7', '#7C3AED', '168, 85, 247', 'ai-model-development'),
        ('Advanced Neural Networks', 'Deep dive into transformer models and neural architecture', '55 min', '13 lessons',
         '<circle cx="12" cy="12" r="3"/><path d="M12 1v6M12 17v6M4.22 4.22l4.24 4.24M15.54 15.54l4.24 4.24M1 12h6M17 12h6M4.22 19.78l4.24-4.24M15.54 8.46l4.24-4.24"/>', 'grad-adv-3', '#A855F7', '#7C3AED', '168, 85, 247', 'advanced-neural-networks'),
        ('AI Security & Privacy', 'Implement robust security measures for AI systems', '45 min', '11 lessons',
         '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M12 9v4M12 17h.01"/>', 'grad-adv-4', '#A855F7', '#7C3AED', '168, 85, 247', 'ai-security-privacy'),
        ('Production AI Deployment', 'Deploy and monitor AI models in production environments', '50 min', '12 lessons',
         '<path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5M2 12l10 5 10-5"/>', 'grad-adv-5', '#A855F7', '#7C3AED', '168, 85, 247', 'production-ai-deployment'),
        ('AI Performance Tuning', 'Optimize AI models for speed, cost, and accuracy', '48 min', '11 lessons',
         '<path d="M12 20v-6M6 20V10M18 20V4"/>', 'grad-adv-6', '#A855F7', '#7C3AED', '168, 85, 247', 'ai-performance-tuning'),
        ('Custom LLM Fine-tuning', 'Train specialized language models for domain expertise', '58 min', '13 lessons',
         '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>', 'grad-adv-7', '#A855F7', '#7C3AED', '168, 85, 247', 'custom-llm-finetuning'),
        ('AI Ethics Implementation', 'Build ethical frameworks into AI systems and workflows', '42 min', '10 lessons',
         '<path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/><path d="M12 15l-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/>', 'grad-adv-8', '#A855F7', '#7C3AED', '168, 85, 247', 'ai-ethics-implementation'),
        ('Multi-Agent AI Systems', 'Orchestrate multiple AI agents for complex tasks', '52 min', '12 lessons',
         '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>', 'grad-adv-9', '#A855F7', '#7C3AED', '168, 85, 247', 'multi-agent-ai-systems'),
        ('AI Research & Innovation', 'Explore cutting-edge AI research and experimental techniques', '55 min', '13 lessons',
         '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/>', 'grad-adv-10', '#A855F7', '#7C3AED', '168, 85, 247', 'ai-research-innovation'),
    ]

    # Générer le HTML pour chaque section
    beginner_html = '\n'.join([create_guide_card(*guide) for guide in beginner_guides])
    intermediate_html = '\n'.join([create_guide_card(*guide) for guide in intermediate_guides])
    advanced_html = '\n'.join([create_guide_card(*guide) for guide in advanced_guides])

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Supprimer tout entre "<!-- Section: Beginner Guides -->" et "Ready to Start"
    # Et le remplacer par les nouvelles sections propres
    pattern = r'(<!-- Section: Beginner Guides -->).*?(<!-- Ready to Start Section -->|<div style="text-align: center; margin: var\(--space-4xl\))'

    replacement = r'''<!-- Section: Beginner Guides -->
            <div id="beginner"></div>
            <div class="section-divider" style="margin-top: var(--space-4xl);">
                <div style="display: flex; align-items: center; justify-content: center; gap: var(--space-md); margin-bottom: var(--space-md);">
                    <svg viewBox="0 0 24 24" fill="none" stroke="url(#grad-beginner-section)" stroke-width="2" width="40" height="40" style="filter: drop-shadow(0 0 10px rgba(34, 197, 94, 0.6));">
                        <circle cx="12" cy="12" r="10"/>
                        <path d="M12 16v-4"/>
                        <path d="M12 8h.01"/>
                    </svg>
                    <h2>Beginner Guides</h2>
                </div>
                <a href="../categories/guides-beginner.html" target="_blank" class="btn btn-outline" style="border-color: #22C55E; color: #22C55E; margin-top: var(--space-md);">
                    View All Beginner Guides
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width: 16px; height: 16px; display: inline-block; vertical-align: middle; margin-left: 6px;">
                        <path d="M5 12h14M12 5l7 7-7 7"/>
                    </svg>
                </a>
                <p style="color: var(--text-secondary);">Perfect starting point for AI newcomers - no experience required</p>
                <svg width="0" height="0" style="position: absolute;">
                    <defs>
                        <linearGradient id="grad-beginner-section" x1="0%" y1="0%" x2="100%" y2="100%">
                            <stop offset="0%" style="stop-color:#22C55E"/>
                            <stop offset="100%" style="stop-color:#10B981"/>
                        </linearGradient>
                    </defs>
                </svg>
            </div>

            <div class="guides-grid">
''' + beginner_html + '''
            </div>

            <!-- Section: Intermediate Guides -->
            <div id="intermediate"></div>
            <div class="section-divider" style="margin-top: var(--space-4xl);">
                <div style="display: flex; align-items: center; justify-content: center; gap: var(--space-md); margin-bottom: var(--space-md);">
                    <svg viewBox="0 0 24 24" fill="none" stroke="url(#grad-intermediate-section)" stroke-width="2" width="40" height="40" style="filter: drop-shadow(0 0 10px rgba(59, 130, 246, 0.6));">
                        <polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/>
                        <polyline points="17 6 23 6 23 12"/>
                    </svg>
                    <h2>Intermediate Guides</h2>
                </div>
                <a href="../categories/guides-intermediate.html" target="_blank" class="btn btn-outline" style="border-color: #3B82F6; color: #3B82F6; margin-top: var(--space-md);">
                    View All Intermediate Guides
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width: 16px; height: 16px; display: inline-block; vertical-align: middle; margin-left: 6px;">
                        <path d="M5 12h14M12 5l7 7-7 7"/>
                    </svg>
                </a>
                <p style="color: var(--text-secondary);">Level up your AI skills with advanced techniques and workflows</p>
                <svg width="0" height="0" style="position: absolute;">
                    <defs>
                        <linearGradient id="grad-intermediate-section" x1="0%" y1="0%" x2="100%" y2="100%">
                            <stop offset="0%" style="stop-color:#3B82F6"/>
                            <stop offset="100%" style="stop-color:#2563EB"/>
                        </linearGradient>
                    </defs>
                </svg>
            </div>

            <div class="guides-grid">
''' + intermediate_html + '''
            </div>

            <!-- Section: Advanced Guides -->
            <div id="advanced"></div>
            <div class="section-divider" style="margin-top: var(--space-4xl);">
                <div style="display: flex; align-items: center; justify-content: center; gap: var(--space-md); margin-bottom: var(--space-md);">
                    <svg viewBox="0 0 24 24" fill="none" stroke="url(#grad-advanced-section)" stroke-width="2" width="40" height="40" style="filter: drop-shadow(0 0 10px rgba(168, 85, 247, 0.6));">
                        <path d="M12 2L2 7l10 5 10-5-10-5z"/>
                        <path d="M2 17l10 5 10-5"/>
                        <path d="M2 12l10 5 10-5"/>
                    </svg>
                    <h2>Advanced Guides</h2>
                </div>
                <a href="../categories/guides-advanced.html" target="_blank" class="btn btn-outline" style="border-color: #A855F7; color: #A855F7; margin-top: var(--space-md);">
                    View All Advanced Guides
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width: 16px; height: 16px; display: inline-block; vertical-align: middle; margin-left: 6px;">
                        <path d="M5 12h14M12 5l7 7-7 7"/>
                    </svg>
                </a>
                <p style="color: var(--text-secondary);">Expert-level techniques for AI professionals and researchers</p>
                <svg width="0" height="0" style="position: absolute;">
                    <defs>
                        <linearGradient id="grad-advanced-section" x1="0%" y1="0%" x2="100%" y2="100%">
                            <stop offset="0%" style="stop-color:#A855F7"/>
                            <stop offset="100%" style="stop-color:#7C3AED"/>
                        </linearGradient>
                    </defs>
                </svg>
            </div>

            <div class="guides-grid">
''' + advanced_html + '''
            </div>

            \2'''

    content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    # Écrire le fichier
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ Sections Beginner, Intermediate et Advanced reconstruites")
    print(f"   - {len(beginner_guides)} Beginner guides")
    print(f"   - {len(intermediate_guides)} Intermediate guides")
    print(f"   - {len(advanced_guides)} Advanced guides")
    print("\n🎉 Toutes les sections affichent maintenant leurs guides correctement!")

if __name__ == '__main__':
    main()
