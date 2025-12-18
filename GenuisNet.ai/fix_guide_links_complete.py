#!/usr/bin/env python3
"""
Script pour convertir toutes les cartes div en liens a
"""

import re
from pathlib import Path

def main():
    """Convertit toutes les div guide-card en liens."""
    file_path = Path('/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/guides.html')

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

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

    new_lines = []
    i = 0
    modified_count = 0

    while i < len(lines):
        line = lines[i]

        # Chercher les divs guide-card qui n'ont pas style="cursor: default;"
        if '<div class="guide-card" style="cursor: default;">' in line:
            # Trouver le titre dans les lignes suivantes
            title_found = None
            for j in range(i, min(i + 50, len(lines))):
                if '<h3>' in lines[j]:
                    title_match = re.search(r'<h3>(.*?)</h3>', lines[j])
                    if title_match:
                        title_found = title_match.group(1)
                        break

            # Si on a trouvé un titre qui correspond à nos guides
            if title_found and title_found in guide_slugs:
                # Remplacer div par a
                new_line = line.replace(
                    '<div class="guide-card" style="cursor: default;">',
                    f'<a href="guides/{guide_slugs[title_found]}.html" class="guide-card">'
                )
                new_lines.append(new_line)
                modified_count += 1

                # Trouver la fermeture correspondante et la remplacer
                depth = 1
                i += 1
                while i < len(lines) and depth > 0:
                    if '<div' in lines[i]:
                        depth += lines[i].count('<div')
                    if '</div>' in lines[i]:
                        depth -= lines[i].count('</div>')

                    if depth == 0:
                        # C'est la fermeture de notre carte
                        new_lines.append(lines[i].replace('</div>', '</a>', 1))
                    else:
                        new_lines.append(lines[i])

                    i += 1
                continue

        new_lines.append(line)
        i += 1

    # Écrire le fichier
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

    print(f"✅ {modified_count} cartes converties en liens")
    print(f"\n🎉 Fichier guides.html mis à jour!")

if __name__ == '__main__':
    main()
