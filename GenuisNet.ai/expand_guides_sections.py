#!/usr/bin/env python3
"""
Script pour étendre les sections à 10 guides chacune
"""

import re

# 10 Guides Beginner (Vert #22C55E)
BEGINNER_GUIDES = [
    {
        "title": "AI Fundamentals",
        "description": "Understand what AI really is, how it works, and why it matters. Learn the basic concepts without technical jargon.",
        "time": "20 min read",
        "lessons": "5 lessons",
        "icon": '<path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/>'
    },
    {
        "title": "Getting Started with ChatGPT",
        "description": "Your first steps with ChatGPT. Learn how to write effective prompts and get useful answers every time.",
        "time": "30 min read",
        "lessons": "7 lessons",
        "icon": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/><circle cx="9" cy="10" r="1" fill="#22C55E"/><circle cx="12" cy="10" r="1" fill="#22C55E"/><circle cx="15" cy="10" r="1" fill="#22C55E"/>'
    },
    {
        "title": "AI for Everyday Productivity",
        "description": "Use AI to write emails, summarize documents, plan your day, and boost your productivity without technical skills.",
        "time": "25 min read",
        "lessons": "6 lessons",
        "icon": '<path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/>'
    },
    {
        "title": "Understanding AI Image Generation",
        "description": "Learn how DALL-E, Midjourney, and Stable Diffusion work. Create your first AI-generated images step by step.",
        "time": "35 min read",
        "lessons": "8 lessons",
        "icon": '<rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5" fill="#22C55E"/><polyline points="21 15 16 10 5 21"/>'
    },
    {
        "title": "AI Writing Tools for Beginners",
        "description": "Master Grammarly, Jasper, and Copy.ai to write better content faster. Perfect for non-writers.",
        "time": "28 min read",
        "lessons": "7 lessons",
        "icon": '<path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"/>'
    },
    {
        "title": "Voice AI: From Speech to Text",
        "description": "Use Whisper, Otter.ai, and voice assistants. Convert speech to text and automate transcription tasks.",
        "time": "22 min read",
        "lessons": "5 lessons",
        "icon": '<path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/><line x1="8" y1="23" x2="16" y2="23"/>'
    },
    {
        "title": "AI Research Assistant Basics",
        "description": "Use Perplexity, Claude, and search tools to research faster. Find, verify, and summarize information efficiently.",
        "time": "30 min read",
        "lessons": "6 lessons",
        "icon": '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/>'
    },
    {
        "title": "Simple AI Video Creation",
        "description": "Create videos with Synthesia, D-ID, and HeyGen. No filming required - just text to video in minutes.",
        "time": "32 min read",
        "lessons": "7 lessons",
        "icon": '<polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2" ry="2"/>'
    },
    {
        "title": "AI for Social Media Content",
        "description": "Generate posts, captions, and hashtags with AI. Automate your social media presence across all platforms.",
        "time": "26 min read",
        "lessons": "6 lessons",
        "icon": '<path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"/>'
    },
    {
        "title": "AI Safety & Ethics Intro",
        "description": "Understand AI limitations, biases, and ethical use. Learn to use AI responsibly and avoid common pitfalls.",
        "time": "24 min read",
        "lessons": "5 lessons",
        "icon": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>'
    }
]

# 10 Guides Intermediate (Bleu #3B82F6)
INTERMEDIATE_GUIDES = [
    {
        "title": "Advanced Prompt Engineering",
        "description": "Master prompt engineering techniques: chain-of-thought, few-shot learning, role prompting, and structured outputs.",
        "time": "50 min read",
        "lessons": "10 lessons",
        "icon": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>'
    },
    {
        "title": "AI Workflow Automation",
        "description": "Build automated workflows combining multiple AI tools. Zapier, Make, and custom integrations for maximum efficiency.",
        "time": "45 min read",
        "lessons": "8 lessons",
        "icon": '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M9 9h6v6H9z"/><path d="M9 3v6M15 9h6M15 15h6M9 15v6"/>'
    },
    {
        "title": "Multi-Modal AI Mastery",
        "description": "Work with text, images, audio, and video together. Create complete projects using GPT-4V, DALL-E, and more.",
        "time": "55 min read",
        "lessons": "9 lessons",
        "icon": '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/>'
    },
    {
        "title": "Custom GPTs Development",
        "description": "Build custom GPTs for specific tasks. Configure instructions, knowledge bases, and actions for specialized AI assistants.",
        "time": "48 min read",
        "lessons": "9 lessons",
        "icon": '<circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>'
    },
    {
        "title": "AI for Data Analysis",
        "description": "Analyze data with ChatGPT Code Interpreter, Claude, and specialized tools. Create charts, insights, and reports.",
        "time": "52 min read",
        "lessons": "10 lessons",
        "icon": '<line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/>'
    },
    {
        "title": "API Integration Mastery",
        "description": "Connect AI tools via APIs. Build custom integrations with OpenAI, Anthropic, and other AI service providers.",
        "time": "60 min read",
        "lessons": "11 lessons",
        "icon": '<polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>'
    },
    {
        "title": "AI Content Production Pipeline",
        "description": "Create end-to-end content pipelines. From ideation to publishing using AI for blogs, videos, and social media.",
        "time": "47 min read",
        "lessons": "9 lessons",
        "icon": '<line x1="12" y1="20" x2="12" y2="10"/><line x1="18" y1="20" x2="18" y2="4"/><line x1="6" y1="20" x2="6" y2="16"/>'
    },
    {
        "title": "Vector Databases & Embeddings",
        "description": "Understand embeddings, semantic search, and vector databases. Build intelligent search systems with Pinecone and Weaviate.",
        "time": "58 min read",
        "lessons": "10 lessons",
        "icon": '<path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="7.5 4.21 12 6.81 16.5 4.21"/><polyline points="7.5 19.79 7.5 14.6 3 12"/><polyline points="21 12 16.5 14.6 16.5 19.79"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/>'
    },
    {
        "title": "AI for Business Intelligence",
        "description": "Transform business data into insights. Use AI for forecasting, trend analysis, and strategic decision-making.",
        "time": "54 min read",
        "lessons": "10 lessons",
        "icon": '<polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>'
    },
    {
        "title": "Conversational AI Design",
        "description": "Design chatbots and voice assistants. Learn conversation flows, intent recognition, and natural dialogue systems.",
        "time": "50 min read",
        "lessons": "9 lessons",
        "icon": '<path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>'
    }
]

# 10 Guides Advanced (Violet #A855F7)
ADVANCED_GUIDES = [
    {
        "title": "Fine-Tuning & RAG Systems",
        "description": "Build custom AI models with fine-tuning. Implement Retrieval-Augmented Generation for enterprise knowledge bases.",
        "time": "90 min read",
        "lessons": "12 lessons",
        "icon": '<path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/><circle cx="12" cy="12" r="3"/>'
    },
    {
        "title": "AI Agent Development",
        "description": "Build autonomous AI agents with LangChain and AutoGPT. Create agents that can reason, plan, and execute complex tasks.",
        "time": "120 min read",
        "lessons": "15 lessons",
        "icon": '<circle cx="12" cy="12" r="3"/><path d="M12 1v6m0 6v6M5.64 5.64l4.24 4.24m6.36 6.36l4.24 4.24M1 12h6m6 0h6M5.64 18.36l4.24-4.24m6.36-6.36l4.24-4.24"/>'
    },
    {
        "title": "Enterprise AI Implementation",
        "description": "Deploy AI at scale: security, compliance, cost optimization, monitoring, and governance for enterprise environments.",
        "time": "100 min read",
        "lessons": "14 lessons",
        "icon": '<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/><path d="M12 11h.01"/>'
    },
    {
        "title": "LLM Architecture Deep Dive",
        "description": "Understand transformer architecture, attention mechanisms, and model internals. Learn how LLMs actually work.",
        "time": "110 min read",
        "lessons": "16 lessons",
        "icon": '<path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/><circle cx="12" cy="12" r="2" fill="#A855F7"/>'
    },
    {
        "title": "Production ML Pipelines",
        "description": "Build production-grade ML pipelines. Data preprocessing, model training, deployment, and monitoring at scale.",
        "time": "95 min read",
        "lessons": "13 lessons",
        "icon": '<polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/><circle cx="12" cy="12" r="1" fill="#A855F7"/>'
    },
    {
        "title": "AI Model Optimization",
        "description": "Optimize models for speed and efficiency. Quantization, pruning, distillation, and deployment strategies.",
        "time": "88 min read",
        "lessons": "12 lessons",
        "icon": '<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>'
    },
    {
        "title": "Multi-Agent Systems",
        "description": "Orchestrate multiple AI agents working together. Build complex systems with specialized agents collaborating.",
        "time": "105 min read",
        "lessons": "14 lessons",
        "icon": '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2" fill="#A855F7"/>'
    },
    {
        "title": "AI Security & Red Teaming",
        "description": "Secure AI systems against attacks. Prompt injection, data poisoning, adversarial examples, and defense strategies.",
        "time": "92 min read",
        "lessons": "13 lessons",
        "icon": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M12 8v4"/><path d="M12 16h.01"/>'
    },
    {
        "title": "Custom Model Training",
        "description": "Train models from scratch. Data collection, labeling, architecture selection, hyperparameter tuning, and evaluation.",
        "time": "115 min read",
        "lessons": "15 lessons",
        "icon": '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/>'
    },
    {
        "title": "AI Infrastructure & DevOps",
        "description": "Build AI infrastructure. GPU orchestration, model serving, CI/CD for ML, and cost optimization at scale.",
        "time": "98 min read",
        "lessons": "13 lessons",
        "icon": '<rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/>'
    }
]

def generate_guide_card(guide, color, gradient_id):
    """Génère le HTML pour une carte de guide."""
    return f'''                <div class="guide-card" style="cursor: default;">
                    <div class="guide-card-header">
                        <div class="guide-icon-container">
                            <div class="guide-icon-neon" style="background: linear-gradient(135deg, rgba({color}, 0.1), rgba({color}, 0.1)); border: 2px solid rgba({color}, 0.3); --glow-rgb: {color}; animation: glow 3s ease-in-out infinite;">
                                <svg viewBox="0 0 24 24" fill="none" stroke="url(#{gradient_id})" stroke-width="1.5" width="60" height="60" style="filter: drop-shadow(0 0 12px rgba({color}, 0.8));">
                                    {guide['icon']}
                                </svg>
                                <svg width="0" height="0" style="position: absolute;">
                                    <defs>
                                        <linearGradient id="{gradient_id}" x1="0%" y1="0%" x2="100%" y2="100%">
                                            <stop offset="0%" style="stop-color:{gradient_id.split('-')[1]}"/>
                                            <stop offset="100%" style="stop-color:{gradient_id.split('-')[2]}"/>
                                        </linearGradient>
                                    </defs>
                                </svg>
                            </div>
                        </div>
                    </div>
                    <div class="guide-card-body">
                        <div style="text-align: center;">
                            <span class="guide-level level-{gradient_id.split('-')[0]}">{gradient_id.split('-')[0].capitalize()}</span>
                        </div>
                        <h3>{guide['title']}</h3>
                        <p class="guide-description">
                            {guide['description']}
                        </p>
                        <div class="guide-meta">
                            <div class="guide-meta-item">
                                <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2">
                                    <circle cx="8" cy="8" r="6"/>
                                    <path d="M8 4v4l2 2"/>
                                </svg>
                                <span>{guide['time']}</span>
                            </div>
                            <div class="guide-meta-item">
                                <span>{guide['lessons']}</span>
                            </div>
                        </div>
                    </div>
                </div>
'''

def create_section_html(section_name, guides, color, gradient_colors, icon_svg):
    """Crée le HTML complet pour une section."""
    gradient_id = f"{section_name.lower()}-section"

    html = f'''
            <!-- Section: {section_name} Guides -->
            <div id="{section_name.lower()}"></div>
            <div class="section-divider" style="margin-top: var(--space-4xl);">
                <div style="display: flex; align-items: center; justify-content: center; gap: var(--space-md); margin-bottom: var(--space-md);">
                    <svg viewBox="0 0 24 24" fill="none" stroke="url(#{gradient_id})" stroke-width="2" width="40" height="40" style="filter: drop-shadow(0 0 10px rgba({color}, 0.6));">
                        {icon_svg}
                    </svg>
                    <h2>{section_name} Guides</h2>
                </div>
                <p style="color: var(--text-secondary);">{
                    "Perfect starting point for AI newcomers - no experience required" if section_name == "Beginner" else
                    "Level up your AI skills with advanced techniques and workflows" if section_name == "Intermediate" else
                    "Expert-level techniques for AI professionals and power users"
                }</p>
                <svg width="0" height="0" style="position: absolute;">
                    <defs>
                        <linearGradient id="{gradient_id}" x1="0%" y1="0%" x2="100%" y2="100%">
                            <stop offset="0%" style="stop-color:{gradient_colors[0]}"/>
                            <stop offset="100%" style="stop-color:{gradient_colors[1]}"/>
                        </linearGradient>
                    </defs>
                </svg>
            </div>

            <div class="guides-grid">
'''

    for i, guide in enumerate(guides):
        guide_gradient_id = f"{section_name.lower()}-{gradient_colors[0].replace('#', '')}-{gradient_colors[1].replace('#', '')}"
        html += generate_guide_card(guide, color, guide_gradient_id)

    html += '            </div>\n'

    return html

def main():
    file_path = '/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/guides.html'

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Supprimer les anciennes sections Beginner, Intermediate, Advanced
    content = re.sub(
        r'<!-- Section: Beginner Guides -->.*?<!-- Section: Intermediate Guides -->',
        '',
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'<!-- Section: Intermediate Guides -->.*?<!-- Section: Advanced Guides -->',
        '',
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'<!-- Section: Advanced Guides -->.*?<!-- CTA Section -->',
        '',
        content,
        flags=re.DOTALL
    )

    # Créer les nouvelles sections
    beginner_html = create_section_html(
        "Beginner",
        BEGINNER_GUIDES,
        "34, 197, 94",
        ["#22C55E", "#10B981"],
        '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/>'
    )

    intermediate_html = create_section_html(
        "Intermediate",
        INTERMEDIATE_GUIDES,
        "59, 130, 246",
        ["#3B82F6", "#2563EB"],
        '<polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/>'
    )

    advanced_html = create_section_html(
        "Advanced",
        ADVANCED_GUIDES,
        "168, 85, 247",
        ["#A855F7", "#7C3AED"],
        '<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>'
    )

    # Insérer avant le CTA
    cta_pattern = r'<!-- CTA Section -->'
    replacement = beginner_html + '\n' + intermediate_html + '\n' + advanced_html + '\n\n            <!-- CTA Section -->'

    content = re.sub(cta_pattern, replacement, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ Sections étendues avec succès!")
    print("\n📊 Contenu ajouté:")
    print(f"  ✓ Section Beginner: {len(BEGINNER_GUIDES)} guides")
    print(f"  ✓ Section Intermediate: {len(INTERMEDIATE_GUIDES)} guides")
    print(f"  ✓ Section Advanced: {len(ADVANCED_GUIDES)} guides")
    print(f"\n🎯 Total: {len(BEGINNER_GUIDES) + len(INTERMEDIATE_GUIDES) + len(ADVANCED_GUIDES)} guides ajoutés!")

if __name__ == '__main__':
    main()
