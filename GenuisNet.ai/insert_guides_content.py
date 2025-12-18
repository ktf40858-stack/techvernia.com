#!/usr/bin/env python3
"""
Script pour insérer les cartes de guides dans les sections vides
"""

import re

def create_guide_card_html(title, description, time, lessons, icon_svg, color_rgb, gradient_start, gradient_end, level):
    """Génère le HTML d'une carte de guide."""
    gradient_id = f"grad-{title.lower().replace(' ', '-').replace('&', 'and')}"

    return f'''                <div class="guide-card" style="cursor: default;">
                    <div class="guide-card-header">
                        <div class="guide-icon-container">
                            <div class="guide-icon-neon" style="background: linear-gradient(135deg, rgba({color_rgb}, 0.1), rgba({color_rgb}, 0.1)); border: 2px solid rgba({color_rgb}, 0.3); --glow-rgb: {color_rgb}; animation: glow 3s ease-in-out infinite;">
                                <svg viewBox="0 0 24 24" fill="none" stroke="url(#{gradient_id})" stroke-width="1.5" width="60" height="60" style="filter: drop-shadow(0 0 12px rgba({color_rgb}, 0.8));">
                                    {icon_svg}
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
                    </div>
                    <div class="guide-card-body">
                        <div style="text-align: center;">
                            <span class="guide-level level-{level.lower()}">{level}</span>
                        </div>
                        <h3>{title}</h3>
                        <p class="guide-description">
                            {description}
                        </p>
                        <div class="guide-meta">
                            <div class="guide-meta-item">
                                <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2">
                                    <circle cx="8" cy="8" r="6"/>
                                    <path d="M8 4v4l2 2"/>
                                </svg>
                                <span>{time}</span>
                            </div>
                            <div class="guide-meta-item">
                                <span>{lessons}</span>
                            </div>
                        </div>
                    </div>
                </div>
'''

# Données des guides Beginner
beginner_guides = [
    ("AI Fundamentals", "Understand what AI really is, how it works, and why it matters. Learn the basic concepts without technical jargon.", "20 min read", "5 lessons", '<path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/>'),
    ("Getting Started with ChatGPT", "Your first steps with ChatGPT. Learn how to write effective prompts and get useful answers every time.", "30 min read", "7 lessons", '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/><circle cx="9" cy="10" r="1" fill="#22C55E"/><circle cx="12" cy="10" r="1" fill="#22C55E"/><circle cx="15" cy="10" r="1" fill="#22C55E"/>'),
    ("AI for Everyday Productivity", "Use AI to write emails, summarize documents, plan your day, and boost your productivity without technical skills.", "25 min read", "6 lessons", '<path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/>'),
    ("Understanding AI Image Generation", "Learn how DALL-E, Midjourney, and Stable Diffusion work. Create your first AI-generated images step by step.", "35 min read", "8 lessons", '<rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5" fill="#22C55E"/><polyline points="21 15 16 10 5 21"/>'),
    ("AI Writing Tools for Beginners", "Master Grammarly, Jasper, and Copy.ai to write better content faster. Perfect for non-writers.", "28 min read", "7 lessons", '<path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"/>'),
    ("Voice AI: Speech to Text", "Use Whisper, Otter.ai, and voice assistants. Convert speech to text and automate transcription tasks.", "22 min read", "5 lessons", '<path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/><line x1="8" y1="23" x2="16" y2="23"/>'),
    ("AI Research Assistant Basics", "Use Perplexity, Claude, and search tools to research faster. Find, verify, and summarize information efficiently.", "30 min read", "6 lessons", '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/>'),
    ("Simple AI Video Creation", "Create videos with Synthesia, D-ID, and HeyGen. No filming required - just text to video in minutes.", "32 min read", "7 lessons", '<polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2" ry="2"/>'),
    ("AI for Social Media Content", "Generate posts, captions, and hashtags with AI. Automate your social media presence across all platforms.", "26 min read", "6 lessons", '<path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"/>'),
    ("AI Safety & Ethics Intro", "Understand AI limitations, biases, and ethical use. Learn to use AI responsibly and avoid common pitfalls.", "24 min read", "5 lessons", '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>'),
]

# Données des guides Intermediate
intermediate_guides = [
    ("Advanced Prompt Engineering", "Master prompt engineering techniques: chain-of-thought, few-shot learning, role prompting, and structured outputs.", "50 min read", "10 lessons", '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>'),
    ("AI Workflow Automation", "Build automated workflows combining multiple AI tools. Zapier, Make, and custom integrations for maximum efficiency.", "45 min read", "8 lessons", '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M9 9h6v6H9z"/><path d="M9 3v6M15 9h6M15 15h6M9 15v6"/>'),
    ("Multi-Modal AI Mastery", "Work with text, images, audio, and video together. Create complete projects using GPT-4V, DALL-E, and more.", "55 min read", "9 lessons", '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/>'),
    ("Custom GPTs Development", "Build custom GPTs for specific tasks. Configure instructions, knowledge bases, and actions for specialized AI assistants.", "48 min read", "9 lessons", '<circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>'),
    ("AI for Data Analysis", "Analyze data with ChatGPT Code Interpreter, Claude, and specialized tools. Create charts, insights, and reports.", "52 min read", "10 lessons", '<line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/>'),
    ("API Integration Mastery", "Connect AI tools via APIs. Build custom integrations with OpenAI, Anthropic, and other AI service providers.", "60 min read", "11 lessons", '<polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>'),
    ("AI Content Production Pipeline", "Create end-to-end content pipelines. From ideation to publishing using AI for blogs, videos, and social media.", "47 min read", "9 lessons", '<line x1="12" y1="20" x2="12" y2="10"/><line x1="18" y1="20" x2="18" y2="4"/><line x1="6" y1="20" x2="6" y2="16"/>'),
    ("Vector Databases & Embeddings", "Understand embeddings, semantic search, and vector databases. Build intelligent search systems with Pinecone and Weaviate.", "58 min read", "10 lessons", '<path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/>'),
    ("AI for Business Intelligence", "Transform business data into insights. Use AI for forecasting, trend analysis, and strategic decision-making.", "54 min read", "10 lessons", '<polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>'),
    ("Conversational AI Design", "Design chatbots and voice assistants. Learn conversation flows, intent recognition, and natural dialogue systems.", "50 min read", "9 lessons", '<path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>'),
]

# Données des guides Advanced
advanced_guides = [
    ("Fine-Tuning & RAG Systems", "Build custom AI models with fine-tuning. Implement Retrieval-Augmented Generation for enterprise knowledge bases.", "90 min read", "12 lessons", '<path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/><circle cx="12" cy="12" r="3"/>'),
    ("AI Agent Development", "Build autonomous AI agents with LangChain and AutoGPT. Create agents that can reason, plan, and execute complex tasks.", "120 min read", "15 lessons", '<circle cx="12" cy="12" r="3"/><path d="M12 1v6m0 6v6M5.64 5.64l4.24 4.24m6.36 6.36l4.24 4.24M1 12h6m6 0h6M5.64 18.36l4.24-4.24m6.36-6.36l4.24-4.24"/>'),
    ("Enterprise AI Implementation", "Deploy AI at scale: security, compliance, cost optimization, monitoring, and governance for enterprise environments.", "100 min read", "14 lessons", '<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/><path d="M12 11h.01"/>'),
    ("LLM Architecture Deep Dive", "Understand transformer architecture, attention mechanisms, and model internals. Learn how LLMs actually work.", "110 min read", "16 lessons", '<path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/><circle cx="12" cy="12" r="2" fill="#A855F7"/>'),
    ("Production ML Pipelines", "Build production-grade ML pipelines. Data preprocessing, model training, deployment, and monitoring at scale.", "95 min read", "13 lessons", '<polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/><circle cx="12" cy="12" r="1" fill="#A855F7"/>'),
    ("AI Model Optimization", "Optimize models for speed and efficiency. Quantization, pruning, distillation, and deployment strategies.", "88 min read", "12 lessons", '<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>'),
    ("Multi-Agent Systems", "Orchestrate multiple AI agents working together. Build complex systems with specialized agents collaborating.", "105 min read", "14 lessons", '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2" fill="#A855F7"/>'),
    ("AI Security & Red Teaming", "Secure AI systems against attacks. Prompt injection, data poisoning, adversarial examples, and defense strategies.", "92 min read", "13 lessons", '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M12 8v4"/><path d="M12 16h.01"/>'),
    ("Custom Model Training", "Train models from scratch. Data collection, labeling, architecture selection, hyperparameter tuning, and evaluation.", "115 min read", "15 lessons", '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/>'),
    ("AI Infrastructure & DevOps", "Build AI infrastructure. GPU orchestration, model serving, CI/CD for ML, and cost optimization at scale.", "98 min read", "13 lessons", '<rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/>'),
]

def main():
    file_path = '/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/guides.html'

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Générer le HTML pour chaque section
    beginner_cards_html = ""
    for guide in beginner_guides:
        beginner_cards_html += create_guide_card_html(
            guide[0], guide[1], guide[2], guide[3], guide[4],
            "34, 197, 94", "#22C55E", "#10B981", "Beginner"
        )

    intermediate_cards_html = ""
    for guide in intermediate_guides:
        intermediate_cards_html += create_guide_card_html(
            guide[0], guide[1], guide[2], guide[3], guide[4],
            "59, 130, 246", "#3B82F6", "#2563EB", "Intermediate"
        )

    advanced_cards_html = ""
    for guide in advanced_guides:
        advanced_cards_html += create_guide_card_html(
            guide[0], guide[1], guide[2], guide[3], guide[4],
            "168, 85, 247", "#A855F7", "#7C3AED", "Advanced"
        )

    # Trouver et remplacer les grilles vides
    # Pour Beginner
    pattern_beginner = r'(<div id="beginner"></div>.*?<div class="guides-grid">)(.*?)(</div>\s*(?=<div id="intermediate"|</div>\s*<div style="text-align: center"))'
    content = re.sub(pattern_beginner, r'\1\n' + beginner_cards_html + r'\n            \3', content, flags=re.DOTALL)

    # Pour Intermediate
    pattern_intermediate = r'(<div id="intermediate"></div>.*?<div class="guides-grid">)(.*?)(</div>\s*(?=<div id="advanced"|</div>\s*<div style="text-align: center"))'
    content = re.sub(pattern_intermediate, r'\1\n' + intermediate_cards_html + r'\n            \3', content, flags=re.DOTALL)

    # Pour Advanced
    pattern_advanced = r'(<div id="advanced"></div>.*?<div class="guides-grid">)(.*?)(</div>\s*(?=</div>\s*<div style="text-align: center"))'
    content = re.sub(pattern_advanced, r'\1\n' + advanced_cards_html + r'\n            \3', content, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ Contenu des guides ajouté!")
    print(f"   Beginner: {len(beginner_guides)} guides")
    print(f"   Intermediate: {len(intermediate_guides)} guides")
    print(f"   Advanced: {len(advanced_guides)} guides")
    print(f"   Total: {len(beginner_guides) + len(intermediate_guides) + len(advanced_guides)} guides")

if __name__ == '__main__':
    main()
