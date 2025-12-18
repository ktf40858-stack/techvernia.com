#!/usr/bin/env python3
"""
Script pour ajouter tous les attributs data-i18n manquants dans index.html
"""

def add_remaining_i18n():
    """Ajoute tous les attributs data-i18n manquants"""

    file_path = "GenuisNet.ai/index.html"

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Hero Section - Stats labels
    content = content.replace(
        '<div class="stat-label">AI Tools</div>',
        '<div class="stat-label"><span data-i18n="stats.tools">AI Tools</span></div>'
    )

    content = content.replace(
        '<div class="stat-label">Expert Reviews</div>',
        '<div class="stat-label"><span data-i18n="stats.reviews">Expert Reviews</span></div>'
    )

    # Hero Section - CTA Button
    content = content.replace(
        '<span class="btn-text">Explore AI Tools</span>',
        '<span class="btn-text"><span data-i18n="btn.explore-ai-tools">Explore AI Tools</span></span>'
    )

    # Hero Section - Trusted label
    content = content.replace(
        '<div class="trusted-label">Featuring tools from</div>',
        '<div class="trusted-label"><span data-i18n="hero.featuring-tools-from">Featuring tools from</span></div>'
    )

    # Value Proposition Section - Descriptions
    content = content.replace(
        '<p>Handpicked AI tools across 22 categories, tested and reviewed by experts</p>',
        '<p><span data-i18n="card.curated-selection-desc">Handpicked AI tools across 22 categories, tested and reviewed by experts</span></p>'
    )

    content = content.replace(
        '<p>Fresh reviews and comparisons to keep you ahead in the AI revolution</p>',
        '<p><span data-i18n="card.always-updated-desc">Fresh reviews and comparisons to keep you ahead in the AI revolution</span></p>'
    )

    content = content.replace(
        '<p>In-depth analysis from beginners to enterprise solutions</p>',
        '<p><span data-i18n="card.expert-insights-desc">In-depth analysis from beginners to enterprise solutions</span></p>'
    )

    # CTA Section - Button
    content = content.replace(
        '                        Browse Categories\n                        <svg fill="none" stroke="currentColor" stroke-width="2" viewbox="0 0 24 24">',
        '                        <span data-i18n="btn.browse-categories">Browse Categories</span>\n                        <svg fill="none" stroke="currentColor" stroke-width="2" viewbox="0 0 24 24">'
    )

    # Compter les modifications
    changes = []
    if 'data-i18n="stats.tools"' in content:
        changes.append("AI Tools")
    if 'data-i18n="stats.reviews"' in content:
        changes.append("Expert Reviews")
    if 'data-i18n="btn.explore-ai-tools"' in content:
        changes.append("Explore AI Tools")
    if 'data-i18n="hero.featuring-tools-from"' in content:
        changes.append("Featuring tools from")
    if 'data-i18n="card.curated-selection-desc"' in content:
        changes.append("Curated Selection desc")
    if 'data-i18n="card.always-updated-desc"' in content:
        changes.append("Always Updated desc")
    if 'data-i18n="card.expert-insights-desc"' in content:
        changes.append("Expert Insights desc")
    if 'data-i18n="btn.browse-categories"' in content:
        changes.append("Browse Categories")

    # Écrire les modifications
    if content != original_content:
        with open(file_path + '.backup5', 'w', encoding='utf-8') as f:
            f.write(original_content)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print("✅ Attributs data-i18n ajoutés!")
        print("📝 Backup créé: index.html.backup5")
        print(f"📊 Éléments modifiés: {', '.join(changes)}")
    else:
        print("ℹ️  Aucune modification nécessaire")

if __name__ == "__main__":
    add_remaining_i18n()
