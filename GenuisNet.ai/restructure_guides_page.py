#!/usr/bin/env python3
"""
Restructure la page guides.html pour afficher seulement un aperçu
et rendre les catégories cliquables comme les AI Tools
"""

from pathlib import Path

def create_category_card(level, title, description, color_start, color_end, rgb_color, icon_svg, guide_count):
    """Crée une carte de catégorie cliquable."""
    return f'''            <a href="categories/guides-{level}.html" class="category-card" style="text-decoration: none;">
                <div class="category-header" style="background: linear-gradient(135deg, rgba({rgb_color}, 0.1), rgba({rgb_color}, 0.05));">
                    <div class="category-icon" style="background: linear-gradient(135deg, {color_start}, {color_end});">
                        <svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" width="40" height="40">
                            {icon_svg}
                        </svg>
                    </div>
                    <div class="category-info">
                        <h2 style="margin: 0; font-size: var(--text-2xl); font-weight: 700; color: var(--text-primary);">{title}</h2>
                        <p style="margin: var(--space-xs) 0 0; color: {color_start}; font-weight: 600;">{guide_count} Guides</p>
                    </div>
                </div>
                <p class="category-description" style="color: var(--text-secondary); line-height: 1.7; margin-bottom: var(--space-lg);">
                    {description}
                </p>
                <div class="category-cta" style="display: flex; align-items: center; gap: var(--space-sm); color: {color_start}; font-weight: 600;">
                    <span>Explore Guides</span>
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width: 20px; height: 20px;">
                        <path d="M5 12h14M12 5l7 7-7 7"/>
                    </svg>
                </div>
            </a>
'''

def main():
    """Restructure la page guides.html."""

    # CSS pour les cartes de catégories
    category_styles = '''        .category-card {
            display: block;
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-xl);
            padding: var(--space-xl);
            transition: all var(--transition-normal);
        }
        .category-card:hover {
            transform: translateY(-5px);
            box-shadow: var(--shadow-glow);
            border-color: var(--border-color-hover);
        }
        .category-header {
            display: flex;
            align-items: center;
            gap: var(--space-lg);
            margin-bottom: var(--space-md);
            padding: var(--space-lg);
            border-radius: var(--radius-lg);
        }
        .category-icon {
            width: 72px;
            height: 72px;
            border-radius: var(--radius-lg);
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }
        .category-info {
            flex: 1;
        }
        .categories-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: var(--space-xl);
            margin-bottom: var(--space-4xl);
        }
'''

    # Lire le fichier guides.html actuel
    file_path = Path('/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/guides.html')

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Trouver où insérer les styles (avant </style>)
    content = content.replace('</style>', category_styles + '\n    </style>')

    # Créer les cartes de catégories
    beginner_card = create_category_card(
        'beginner',
        'Beginner Guides',
        'Perfect starting point for AI newcomers. Learn the fundamentals with easy-to-follow guides that require no prior experience.',
        '#22C55E', '#10B981', '34, 197, 94',
        '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/>',
        10
    )

    intermediate_card = create_category_card(
        'intermediate',
        'Intermediate Guides',
        'Level up your AI skills with advanced techniques and workflows. Build on your foundation with professional-grade strategies.',
        '#3B82F6', '#2563EB', '59, 130, 246',
        '<polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/>',
        10
    )

    advanced_card = create_category_card(
        'advanced',
        'Advanced Guides',
        'Expert-level techniques for AI professionals and researchers. Master cutting-edge AI development and deployment strategies.',
        '#A855F7', '#7C3AED', '168, 85, 247',
        '<path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/>',
        10
    )

    # Section Featured avec 3 guides populaires
    featured_section = f'''            <!-- Featured Guides -->
            <section style="margin-bottom: var(--space-4xl);">
                <div style="text-align: center; margin-bottom: var(--space-3xl);">
                    <div style="display: inline-block; padding: var(--space-xs) var(--space-md); background: rgba(var(--accent-primary-rgb), 0.1); border: 1px solid rgba(var(--accent-primary-rgb), 0.3); border-radius: var(--radius-full); font-size: var(--text-sm); font-weight: 600; color: var(--accent-primary); margin-bottom: var(--space-md);">
                        Featured
                    </div>
                    <h2 style="font-size: var(--text-3xl); font-weight: 800; margin-bottom: var(--space-md);">
                        Popular Guides
                    </h2>
                    <p style="color: var(--text-secondary); max-width: 600px; margin: 0 auto;">
                        Start with these hand-picked guides covering the most essential AI topics
                    </p>
                </div>

                <div class="guides-grid" style="grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));">
                    <a href="guides/ai-fundamentals.html" target="_blank" class="guide-card">
                        <div class="guide-card-header">
                            <div class="guide-icon-container">
                                <div class="guide-icon-neon" style="background: linear-gradient(135deg, rgba(34, 197, 94, 0.1), rgba(34, 197, 94, 0.1)); border: 2px solid rgba(34, 197, 94, 0.3); --glow-rgb: 34, 197, 94; animation: glow 3s ease-in-out infinite;">
                                    <svg viewBox="0 0 24 24" fill="none" stroke="url(#grad-feat-1)" stroke-width="1.5" width="60" height="60" style="filter: drop-shadow(0 0 12px rgba(34, 197, 94, 0.8));">
                                        <circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/>
                                    </svg>
                                    <svg width="0" height="0" style="position: absolute;">
                                        <defs>
                                            <linearGradient id="grad-feat-1" x1="0%" y1="0%" x2="100%" y2="100%">
                                                <stop offset="0%" style="stop-color:#22C55E"/>
                                                <stop offset="100%" style="stop-color:#10B981"/>
                                            </linearGradient>
                                        </defs>
                                    </svg>
                                </div>
                            </div>
                            <h3>AI Fundamentals</h3>
                        </div>
                        <p class="guide-description">Master the core concepts of artificial intelligence, machine learning, and neural networks</p>
                        <div class="guide-meta">
                            <span class="meta-item">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <circle cx="12" cy="12" r="10"/>
                                    <path d="M12 6v6l4 2"/>
                                </svg>
                                20 min
                            </span>
                            <span class="meta-item">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/>
                                    <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>
                                </svg>
                                5 lessons
                            </span>
                        </div>
                    </a>

                    <a href="guides/advanced-prompt-engineering.html" target="_blank" class="guide-card">
                        <div class="guide-card-header">
                            <div class="guide-icon-container">
                                <div class="guide-icon-neon" style="background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(59, 130, 246, 0.1)); border: 2px solid rgba(59, 130, 246, 0.3); --glow-rgb: 59, 130, 246; animation: glow 3s ease-in-out infinite;">
                                    <svg viewBox="0 0 24 24" fill="none" stroke="url(#grad-feat-2)" stroke-width="1.5" width="60" height="60" style="filter: drop-shadow(0 0 12px rgba(59, 130, 246, 0.8));">
                                        <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>
                                    </svg>
                                    <svg width="0" height="0" style="position: absolute;">
                                        <defs>
                                            <linearGradient id="grad-feat-2" x1="0%" y1="0%" x2="100%" y2="100%">
                                                <stop offset="0%" style="stop-color:#3B82F6"/>
                                                <stop offset="100%" style="stop-color:#2563EB"/>
                                            </linearGradient>
                                        </defs>
                                    </svg>
                                </div>
                            </div>
                            <h3>Advanced Prompt Engineering</h3>
                        </div>
                        <p class="guide-description">Master complex prompting techniques for sophisticated AI interactions</p>
                        <div class="guide-meta">
                            <span class="meta-item">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <circle cx="12" cy="12" r="10"/>
                                    <path d="M12 6v6l4 2"/>
                                </svg>
                                35 min
                            </span>
                            <span class="meta-item">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/>
                                    <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>
                                </svg>
                                8 lessons
                            </span>
                        </div>
                    </a>

                    <a href="guides/enterprise-ai-architecture.html" target="_blank" class="guide-card">
                        <div class="guide-card-header">
                            <div class="guide-icon-container">
                                <div class="guide-icon-neon" style="background: linear-gradient(135deg, rgba(168, 85, 247, 0.1), rgba(168, 85, 247, 0.1)); border: 2px solid rgba(168, 85, 247, 0.3); --glow-rgb: 168, 85, 247; animation: glow 3s ease-in-out infinite;">
                                    <svg viewBox="0 0 24 24" fill="none" stroke="url(#grad-feat-3)" stroke-width="1.5" width="60" height="60" style="filter: drop-shadow(0 0 12px rgba(168, 85, 247, 0.8));">
                                        <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/>
                                    </svg>
                                    <svg width="0" height="0" style="position: absolute;">
                                        <defs>
                                            <linearGradient id="grad-feat-3" x1="0%" y1="0%" x2="100%" y2="100%">
                                                <stop offset="0%" style="stop-color:#A855F7"/>
                                                <stop offset="100%" style="stop-color:#7C3AED"/>
                                            </linearGradient>
                                        </defs>
                                    </svg>
                                </div>
                            </div>
                            <h3>Enterprise AI Architecture</h3>
                        </div>
                        <p class="guide-description">Design scalable AI systems for large organizations</p>
                        <div class="guide-meta">
                            <span class="meta-item">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <circle cx="12" cy="12" r="10"/>
                                    <path d="M12 6v6l4 2"/>
                                </svg>
                                50 min
                            </span>
                            <span class="meta-item">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/>
                                    <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>
                                </svg>
                                12 lessons
                            </span>
                        </div>
                    </a>
                </div>
            </section>

            <!-- Browse by Level -->
            <section>
                <div style="text-align: center; margin-bottom: var(--space-3xl);">
                    <h2 style="font-size: var(--text-3xl); font-weight: 800; margin-bottom: var(--space-md);">
                        Browse by Skill Level
                    </h2>
                    <p style="color: var(--text-secondary); max-width: 600px; margin: 0 auto;">
                        Choose your path and explore guides tailored to your experience level
                    </p>
                </div>

                <div class="categories-grid">
{beginner_card}
{intermediate_card}
{advanced_card}
                </div>
            </section>
'''

    # Remplacer tout le contenu entre <!-- Featured Guides --> et le footer
    import re

    # Pattern: depuis le premier <a href="guides/ jusqu'à juste avant le footer
    pattern = r'(<main class="guides-page">.*?<div class="container">)(.*?)(<!-- Footer -->)'

    replacement = r'\1\n' + featured_section + '\n        \3'

    content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    # Écrire le fichier
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ Page guides.html restructurée!")
    print("   - Section Featured avec 3 guides populaires")
    print("   - Section Browse by Level avec 3 cartes cliquables")
    print("   - Les cartes ouvrent maintenant les pages complètes")
    print("\n🎉 Structure exactement comme AI Tools Categories!")

if __name__ == '__main__':
    main()
