#!/usr/bin/env python3
"""
Corrige tous les liens incorrects dans les cartes de guides
"""

import re
from pathlib import Path

def main():
    """Corrige les liens des cartes."""
    file_path = Path('/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/guides.html')

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Mapping titre -> slug correct
    correct_links = {
        'AI Fundamentals': 'ai-fundamentals',
        'Getting Started with ChatGPT': 'getting-started-chatgpt',
        'Introduction to Image AI': 'introduction-image-ai',
        'AI Writing Tools Basics': 'ai-writing-tools-basics',
        'Understanding AI Models': 'understanding-ai-models',
        'AI Safety &amp; Ethics 101': 'ai-safety-ethics-101',
        'Prompt Engineering Basics': 'prompt-engineering-basics',
        'AI for Personal Productivity': 'ai-personal-productivity',
        'Voice &amp; Audio AI Intro': 'voice-audio-ai-intro',
        'AI Tools Comparison Guide': 'ai-tools-comparison',
        'Advanced Prompt Engineering': 'advanced-prompt-engineering',
        'API Integration Mastery': 'api-integration-mastery',
        'Multimodal AI Applications': 'multimodal-ai-applications',
        'AI Content Strategy': 'ai-content-strategy',
        'AI Data Analysis': 'ai-data-analysis',
        'Building AI Chatbots': 'building-ai-chatbots',
        'AI Video &amp; Animation': 'ai-video-animation',
        'AI Testing &amp; Optimization': 'ai-testing-optimization',
        'Custom AI Training Basics': 'custom-ai-training',
        'AI Workflow Automation': 'ai-workflow-automation',
        'Enterprise AI Architecture': 'enterprise-ai-architecture',
        'AI Model Development': 'ai-model-development',
        'Advanced Neural Networks': 'advanced-neural-networks',
        'AI Security &amp; Privacy': 'ai-security-privacy',
        'Production AI Deployment': 'production-ai-deployment',
        'AI Performance Tuning': 'ai-performance-tuning',
        'Custom LLM Fine-tuning': 'custom-llm-finetuning',
        'AI Ethics Implementation': 'ai-ethics-implementation',
        'Multi-Agent AI Systems': 'multi-agent-ai-systems',
        'AI Research &amp; Innovation': 'ai-research-innovation'
    }

    fixed_count = 0

    # Pour chaque titre, trouver sa carte et corriger le lien
    for title, correct_slug in correct_links.items():
        # Pattern: trouve <a href="guides/ANYTHING.html"> suivi éventuellement de beaucoup de contenu, puis <h3>TITRE</h3>
        pattern = r'(<a href="guides/)[^"]+?(\.html" class="guide-card">.*?<h3>' + re.escape(title) + r'</h3>)'

        # Remplacement
        replacement = r'\1' + correct_slug + r'\2'

        # Compter les occurrences avant
        before_count = len(re.findall(pattern, content, flags=re.DOTALL))

        # Remplacer
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)

        if before_count > 0:
            fixed_count += before_count
            print(f"✅ Corrigé: {title} -> guides/{correct_slug}.html")

    # Écrire le fichier
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\n🎉 {fixed_count} liens corrigés!")

if __name__ == '__main__':
    main()
