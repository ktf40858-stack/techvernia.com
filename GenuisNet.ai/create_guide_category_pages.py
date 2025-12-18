#!/usr/bin/env python3
"""
Crée les pages de catégories pour Beginner, Intermediate et Advanced guides
"""

from pathlib import Path

def create_category_page(level, color_start, color_end, rgb_color):
    """Crée une page de catégorie pour un niveau de guide."""

    levels_data = {
        'beginner': {
            'title': 'Beginner AI Guides',
            'description': 'Perfect starting point for AI newcomers. Learn the fundamentals with easy-to-follow guides that require no prior experience.',
            'badge': 'Beginner Level',
            'guides': [
                ('ai-fundamentals', 'AI Fundamentals', 'Master the core concepts of artificial intelligence, machine learning, and neural networks', '20 min', '5 lessons'),
                ('getting-started-chatgpt', 'Getting Started with ChatGPT', 'Learn how to use ChatGPT effectively for writing, coding, and problem-solving', '25 min', '6 lessons'),
                ('introduction-image-ai', 'Introduction to Image AI', 'Discover how to create stunning visuals with DALL-E, Midjourney, and Stable Diffusion', '30 min', '7 lessons'),
                ('ai-writing-tools-basics', 'AI Writing Tools Basics', 'Master AI-powered writing assistants for content creation and editing', '18 min', '4 lessons'),
                ('understanding-ai-models', 'Understanding AI Models', 'Learn about different types of AI models and their applications', '22 min', '5 lessons'),
                ('ai-safety-ethics-101', 'AI Safety & Ethics 101', 'Explore responsible AI use and ethical considerations', '15 min', '4 lessons'),
                ('prompt-engineering-basics', 'Prompt Engineering Basics', 'Learn to write effective prompts for better AI outputs', '28 min', '6 lessons'),
                ('ai-personal-productivity', 'AI for Personal Productivity', 'Boost your daily efficiency with AI tools and techniques', '20 min', '5 lessons'),
                ('voice-audio-ai-intro', 'Voice & Audio AI Intro', 'Get started with AI voice generation and audio processing', '25 min', '6 lessons'),
                ('ai-tools-comparison', 'AI Tools Comparison Guide', 'Compare popular AI tools to find the best fit for your needs', '30 min', '7 lessons')
            ]
        },
        'intermediate': {
            'title': 'Intermediate AI Guides',
            'description': 'Level up your AI skills with advanced techniques and workflows. Build on your foundation with professional-grade strategies.',
            'badge': 'Intermediate Level',
            'guides': [
                ('advanced-prompt-engineering', 'Advanced Prompt Engineering', 'Master complex prompting techniques for sophisticated AI interactions', '35 min', '8 lessons'),
                ('api-integration-mastery', 'API Integration Mastery', 'Connect AI capabilities to your applications via APIs', '38 min', '9 lessons'),
                ('multimodal-ai-applications', 'Multimodal AI Applications', 'Combine text, image, and audio AI for powerful solutions', '42 min', '10 lessons'),
                ('ai-content-strategy', 'AI Content Strategy', 'Develop professional content workflows using AI tools', '35 min', '8 lessons'),
                ('ai-data-analysis', 'AI Data Analysis', 'Leverage AI for advanced data processing and insights', '40 min', '9 lessons'),
                ('building-ai-chatbots', 'Building AI Chatbots', 'Create custom chatbots for business and personal use', '45 min', '10 lessons'),
                ('ai-video-animation', 'AI Video & Animation', 'Master AI tools for video creation and editing', '38 min', '9 lessons'),
                ('ai-testing-optimization', 'AI Testing & Optimization', 'Learn to test, benchmark, and improve AI outputs', '35 min', '8 lessons'),
                ('custom-ai-training', 'Custom AI Training Basics', 'Learn to fine-tune AI models for specialized tasks', '45 min', '10 lessons'),
                ('ai-workflow-automation', 'AI Workflow Automation', 'Build automated workflows combining multiple AI tools', '40 min', '9 lessons')
            ]
        },
        'advanced': {
            'title': 'Advanced AI Guides',
            'description': 'Expert-level techniques for AI professionals and researchers. Master cutting-edge AI development and deployment strategies.',
            'badge': 'Advanced Level',
            'guides': [
                ('enterprise-ai-architecture', 'Enterprise AI Architecture', 'Design scalable AI systems for large organizations', '50 min', '12 lessons'),
                ('ai-model-development', 'AI Model Development', 'Build and deploy custom AI models from scratch', '60 min', '14 lessons'),
                ('advanced-neural-networks', 'Advanced Neural Networks', 'Deep dive into transformer models and neural architecture', '55 min', '13 lessons'),
                ('ai-security-privacy', 'AI Security & Privacy', 'Implement robust security measures for AI systems', '45 min', '11 lessons'),
                ('production-ai-deployment', 'Production AI Deployment', 'Deploy and monitor AI models in production environments', '50 min', '12 lessons'),
                ('ai-performance-tuning', 'AI Performance Tuning', 'Optimize AI models for speed, cost, and accuracy', '48 min', '11 lessons'),
                ('custom-llm-finetuning', 'Custom LLM Fine-tuning', 'Train specialized language models for domain expertise', '58 min', '13 lessons'),
                ('ai-ethics-implementation', 'AI Ethics Implementation', 'Build ethical frameworks into AI systems and workflows', '42 min', '10 lessons'),
                ('multi-agent-ai-systems', 'Multi-Agent AI Systems', 'Orchestrate multiple AI agents for complex tasks', '52 min', '12 lessons'),
                ('ai-research-innovation', 'AI Research & Innovation', 'Explore cutting-edge AI research and experimental techniques', '55 min', '13 lessons')
            ]
        }
    }

    data = levels_data[level]

    # Générer les cartes de guides
    guide_cards = ''
    for slug, title, desc, time, lessons in data['guides']:
        guide_cards += f'''
                <a href="../guides/{slug}.html" class="tool-card-full" target="_blank">
                    <div class="tool-card-header" style="background: linear-gradient(135deg, rgba({rgb_color}, 0.1), rgba({rgb_color}, 0.05));">
                        <div class="tool-logo-large" style="background: linear-gradient(135deg, {color_start}, {color_end}); font-size: var(--text-lg);">
                            <svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" width="36" height="36">
                                <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/>
                                <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>
                            </svg>
                        </div>
                        <div class="tool-header-info">
                            <h3>{title}</h3>
                            <div class="company" style="color: {color_start};">{data['badge']}</div>
                        </div>
                    </div>
                    <div class="tool-card-body">
                        <p class="tool-description">{desc}</p>
                        <div class="tool-stats">
                            <div class="stat-item">
                                <div class="stat-value" style="color: {color_start};">
                                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width: 16px; height: 16px; display: inline-block; vertical-align: middle;">
                                        <circle cx="12" cy="12" r="10"/>
                                        <path d="M12 6v6l4 2"/>
                                    </svg>
                                    {time}
                                </div>
                                <div class="stat-label">Reading Time</div>
                            </div>
                            <div class="stat-item">
                                <div class="stat-value" style="color: {color_start};">{lessons}</div>
                                <div class="stat-label">Lessons</div>
                            </div>
                            <div class="stat-item">
                                <div class="stat-value" style="color: {color_start};">Free</div>
                                <div class="stat-label">Access</div>
                            </div>
                        </div>
                        <div style="text-align: center;">
                            <span class="btn btn-primary" style="display: inline-block; width: auto;">Start Learning →</span>
                        </div>
                    </div>
                </a>
'''

    return f'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{data['description']}">
    <title>{data['title']} | GenuisNet.ai</title>
    <link rel="stylesheet" href="../../css/style.css">
    <link rel="stylesheet" href="../../css/animations.css">
    <link rel="icon" type="image/svg+xml" href="../../assets/images/logo.svg">
    <style>
        .category-hero {{
            padding: calc(80px + var(--space-4xl)) var(--space-lg) var(--space-3xl);
            background: linear-gradient(135deg, rgba({rgb_color}, 0.05) 0%, transparent 50%);
        }}
        .category-hero-content {{
            max-width: 800px;
        }}
        .category-hero .hero-badge {{
            margin-bottom: var(--space-lg);
            display: inline-block;
            padding: var(--space-xs) var(--space-md);
            background: rgba({rgb_color}, 0.1);
            border: 1px solid rgba({rgb_color}, 0.3);
            border-radius: var(--radius-full);
            font-size: var(--text-sm);
            font-weight: 600;
            color: {color_start};
        }}
        .category-hero h1 {{
            font-size: clamp(var(--text-3xl), 6vw, var(--text-5xl));
            font-weight: 800;
            margin-bottom: var(--space-lg);
            background: linear-gradient(135deg, {color_start}, {color_end});
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        .category-hero p {{
            font-size: var(--text-lg);
            color: var(--text-secondary);
            line-height: 1.7;
        }}
        .tools-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: var(--space-lg);
        }}
        .tool-card-full {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-xl);
            overflow: hidden;
            transition: all var(--transition-normal);
            text-decoration: none;
            display: block;
        }}
        .tool-card-full:hover {{
            transform: translateY(-5px);
            border-color: {color_start};
            box-shadow: 0 20px 40px rgba({rgb_color}, 0.2);
        }}
        .tool-card-header {{
            padding: var(--space-xl);
            background: var(--bg-tertiary);
            display: flex;
            align-items: center;
            gap: var(--space-lg);
        }}
        .tool-logo-large {{
            width: 72px;
            height: 72px;
            border-radius: var(--radius-lg);
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }}
        .tool-header-info h3 {{
            font-size: var(--text-xl);
            font-weight: 700;
            margin-bottom: var(--space-xs);
            color: var(--text-primary);
        }}
        .tool-header-info .company {{
            font-size: var(--text-sm);
        }}
        .tool-card-body {{
            padding: var(--space-xl);
        }}
        .tool-description {{
            color: var(--text-secondary);
            line-height: 1.7;
            margin-bottom: var(--space-lg);
        }}
        .tool-stats {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: var(--space-md);
            padding: var(--space-lg);
            background: var(--bg-tertiary);
            border-radius: var(--radius-lg);
            margin-bottom: var(--space-lg);
        }}
        .stat-item {{
            text-align: center;
        }}
        .stat-value {{
            font-size: var(--text-lg);
            font-weight: 700;
            margin-bottom: var(--space-xs);
        }}
        .stat-label {{
            font-size: var(--text-xs);
            color: var(--text-tertiary);
        }}
    </style>
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar">
        <div class="container">
            <div class="nav-container">
                <a href="../../index.html" class="logo">
                    <img src="../../assets/images/logo.svg" alt="GenuisNet.ai" class="logo-image">
                </a>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="category-hero">
        <div class="container">
            <div class="category-hero-content">
                <div class="hero-badge">{data['badge']}</div>
                <h1>{data['title']}</h1>
                <p>{data['description']}</p>
            </div>
        </div>
    </section>

    <!-- Guides Grid -->
    <section style="padding: var(--space-3xl) var(--space-lg);">
        <div class="container">
            <div style="margin-bottom: var(--space-2xl);">
                <a href="../guides.html" style="color: var(--text-secondary); text-decoration: none; display: inline-flex; align-items: center; gap: var(--space-xs);">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width: 16px; height: 16px;">
                        <path d="M19 12H5M12 19l-7-7 7-7"/>
                    </svg>
                    Back to All Guides
                </a>
            </div>

            <div class="tools-grid">
{guide_cards}
            </div>

            <!-- Call to Action -->
            <div style="text-align: center; margin-top: var(--space-4xl); padding: var(--space-3xl); background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-2xl);">
                <h2 style="font-size: var(--text-2xl); font-weight: 700; margin-bottom: var(--space-md);">
                    Ready to Explore More?
                </h2>
                <p style="color: var(--text-secondary); margin-bottom: var(--space-xl); max-width: 600px; margin-left: auto; margin-right: auto;">
                    Browse all our guides or explore AI tools to find the perfect solutions for your needs.
                </p>
                <div style="display: flex; gap: var(--space-md); justify-content: center; flex-wrap: wrap;">
                    <a href="../guides.html" class="btn btn-primary">All Guides</a>
                    <a href="../../index.html#categories" class="btn btn-outline">Explore AI Tools</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <a href="../../index.html" class="footer-logo">
                        <img src="../../assets/images/logo.svg" alt="GenuisNet.ai Logo" class="footer-logo-image">
                    </a>
                    <p class="footer-description">Your trusted source for AI tool reviews and comparisons.</p>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2024 GenuisNet.ai. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <script>
        // Logo scroll behavior
        const logo = document.querySelector('.logo');
        window.addEventListener('scroll', () => {{
            if (window.pageYOffset > 100) {{
                logo.style.opacity = '0';
                logo.style.pointerEvents = 'none';
            }} else {{
                logo.style.opacity = '1';
                logo.style.pointerEvents = 'auto';
            }}
        }});
    </script>
</body>
</html>'''

def main():
    """Crée les 3 pages de catégories."""
    base_dir = Path('/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/categories')
    base_dir.mkdir(exist_ok=True)

    categories = {
        'beginner': ('#22C55E', '#10B981', '34, 197, 94'),
        'intermediate': ('#3B82F6', '#2563EB', '59, 130, 246'),
        'advanced': ('#A855F7', '#7C3AED', '168, 85, 247')
    }

    for level, (color_start, color_end, rgb_color) in categories.items():
        html_content = create_category_page(level, color_start, color_end, rgb_color)
        file_path = base_dir / f'guides-{level}.html'

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html_content)

        print(f"✅ {level.capitalize()} category page created")

    print(f"\n🎉 3 guide category pages created successfully!")

if __name__ == '__main__':
    main()
