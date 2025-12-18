#!/usr/bin/env python3
"""
Script pour ajouter les liens href aux cartes de guides et corriger les cartes incomplètes
"""

import re
from pathlib import Path

def main():
    """Ajoute les liens et corrige les cartes."""
    file_path = Path('/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/guides.html')

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Mapping des titres vers les slugs
    guide_slugs = {
        # Beginner
        'AI Fundamentals': 'ai-fundamentals',
        'Getting Started with ChatGPT': 'getting-started-chatgpt',
        'Introduction to Image AI': 'introduction-image-ai',
        'AI Writing Tools Basics': 'ai-writing-tools-basics',
        'Understanding AI Models': 'understanding-ai-models',
        'AI Safety & Ethics 101': 'ai-safety-ethics-101',
        'Prompt Engineering Basics': 'prompt-engineering-basics',
        'AI for Personal Productivity': 'ai-personal-productivity',
        'Voice & Audio AI Intro': 'voice-audio-ai-intro',
        'AI Tools Comparison Guide': 'ai-tools-comparison',

        # Intermediate
        'Advanced Prompt Engineering': 'advanced-prompt-engineering',
        'API Integration Mastery': 'api-integration-mastery',
        'Multimodal AI Applications': 'multimodal-ai-applications',
        'AI Content Strategy': 'ai-content-strategy',
        'AI Data Analysis': 'ai-data-analysis',
        'Building AI Chatbots': 'building-ai-chatbots',
        'AI Video & Animation': 'ai-video-animation',
        'AI Testing & Optimization': 'ai-testing-optimization',
        'Custom AI Training Basics': 'custom-ai-training',
        'AI Workflow Automation': 'ai-workflow-automation',

        # Advanced
        'Enterprise AI Architecture': 'enterprise-ai-architecture',
        'AI Model Development': 'ai-model-development',
        'Advanced Neural Networks': 'advanced-neural-networks',
        'AI Security & Privacy': 'ai-security-privacy',
        'Production AI Deployment': 'production-ai-deployment',
        'AI Performance Tuning': 'ai-performance-tuning',
        'Custom LLM Fine-tuning': 'custom-llm-finetuning',
        'AI Ethics Implementation': 'ai-ethics-implementation',
        'Multi-Agent AI Systems': 'multi-agent-ai-systems',
        'AI Research & Innovation': 'ai-research-innovation'
    }

    # Trouver et corriger la première carte Intermediate incomplète (ligne 579-595)
    # Cette carte a des divs manquantes
    broken_card_pattern = r'(<div class="guide-card" style="cursor: default;">.*?<div class="guide-icon-container">.*?<div class="guide-icon-neon".*?</svg>\s*</div>\s*)(\s*<div class="guide-card")'

    # Ajouter la fermeture manquante
    fix_closure = r'\1</div>\n                    </div>\n                    <h3>Advanced Prompt Engineering</h3>\n                </div>\n                <p class="guide-description">Master complex prompting techniques for sophisticated AI interactions</p>\n                <div class="guide-meta">\n                    <span class="meta-item">\n                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n                            <circle cx="12" cy="12" r="10"/>\n                            <path d="M12 6v6l4 2"/>\n                        </svg>\n                        35 min\n                    </span>\n                    <span class="meta-item">\n                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n                            <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/>\n                            <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>\n                        </svg>\n                        8 lessons\n                    </span>\n                </div>\n            </div>\n\n            \2'

    content = re.sub(broken_card_pattern, fix_closure, content, flags=re.DOTALL)

    # Remplacer tous les <div class="guide-card" style="cursor: default;"> par des liens <a>
    for title, slug in guide_slugs.items():
        # Pattern pour trouver les cartes avec ce titre
        pattern = r'<div class="guide-card" style="cursor: default;">(.*?<h3>' + re.escape(title) + r'</h3>.*?)</div>(\s*</div>)?(\s*<div class="guide-card"|$)'

        # Remplacement avec lien
        replacement = r'<a href="guides/' + slug + r'.html" class="guide-card">\1</a>\3'

        content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    # Écrire le fichier
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ Liens ajoutés à toutes les cartes de guides")
    print("✅ Carte Intermediate incomplète corrigée")
    print(f"\n🎉 Fichier guides.html mis à jour avec succès!")

if __name__ == '__main__':
    main()
