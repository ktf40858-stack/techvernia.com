#!/usr/bin/env python3
"""
Script final pour convertir TOUTES les cartes div en liens a
"""

from pathlib import Path

def main():
    """Convertit toutes les div guide-card en liens."""
    file_path = Path('/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/guides.html')

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Mapping complet titre -> slug
    replacements = {
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

    modified_count = 0

    # Pour chaque guide, trouver sa carte et la convertir
    for title, slug in replacements.items():
        # Chercher la balise <h3> avec ce titre
        h3_tag = f'<h3>{title}</h3>'

        if h3_tag in content:
            # Trouver le début de la carte avant ce h3
            # Chercher en arrière jusqu'à trouver <div class="guide-card"
            parts = content.split(h3_tag)

            for i in range(len(parts) - 1):
                before = parts[i]
                after = parts[i + 1]

                # Chercher la dernière occurrence de <div class="guide-card" dans before
                last_div_start = before.rfind('<div class="guide-card"')

                if last_div_start != -1:
                    # Extraire depuis cette position jusqu'à la fin
                    card_start = before[last_div_start:]

                    # Trouver la fermeture </div> correspondante dans after
                    # Compter les divs pour trouver la bonne fermeture
                    depth = card_start.count('<div') - card_start.count('</div>')

                    end_pos = 0
                    temp_after = after
                    while depth > 0 and end_pos < len(after):
                        if '</div>' in temp_after:
                            first_close = temp_after.find('</div>')
                            end_pos += first_close + 6
                            depth -= 1
                            temp_after = temp_after[first_close + 6:]
                        else:
                            break

                    if depth == 0:
                        # On a trouvé la fermeture
                        # Remplacer la div d'ouverture par un lien
                        new_card_start = card_start.replace(
                            '<div class="guide-card" style="cursor: default;">',
                            f'<a href="guides/{slug}.html" class="guide-card">',
                            1
                        )

                        # Si pas de style cursor: default, essayer sans
                        if new_card_start == card_start:
                            # Trouver le pattern exact
                            import re
                            div_pattern = r'<div class="guide-card"[^>]*>'
                            new_card_start = re.sub(
                                div_pattern,
                                f'<a href="guides/{slug}.html" class="guide-card">',
                                card_start,
                                count=1
                            )

                        # Remplacer la dernière fermeture </div> par </a>
                        card_end = after[:end_pos]
                        # Trouver le dernier </div>
                        last_close_pos = card_end.rfind('</div>')
                        if last_close_pos != -1:
                            new_card_end = card_end[:last_close_pos] + '</a>' + card_end[last_close_pos + 6:]

                            # Reconstruire le contenu
                            parts[i] = before[:last_div_start] + new_card_start
                            parts[i + 1] = new_card_end + after[end_pos:]

                            modified_count += 1

            # Rejoindre les parts avec le h3
            content = h3_tag.join(parts)

    # Écrire le fichier
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ {modified_count} cartes converties en liens")
    print(f"\n🎉 Toutes les cartes sont maintenant cliquables!")

if __name__ == '__main__':
    main()
