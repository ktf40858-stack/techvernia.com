#!/usr/bin/env python3
"""
Script pour ajouter les attributs data-i18n aux cartes de catégories
"""

def add_categories_i18n():
    """Ajoute les attributs data-i18n aux cartes de catégories"""

    file_path = "GenuisNet.ai/pages/categories.html"

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Liste des catégories avec leurs traductions
    categories = [
        {
            'title': 'AI Chatbots',
            'title_key': 'cat.chatbots-short',
            'desc': 'Conversational AI assistants for all your needs',
            'desc_key': 'cat.chatbots-card-desc'
        },
        {
            'title': 'AI Writing',
            'title_key': 'cat.writing-short',
            'desc': 'Create engaging content with AI-powered tools',
            'desc_key': 'cat.writing-card-desc'
        },
        {
            'title': 'AI Image Generation',
            'title_key': 'cat.image-generation',
            'desc': 'Transform text into stunning visuals',
            'desc_key': 'cat.image-card-desc'
        },
        {
            'title': 'AI Video',
            'title_key': 'cat.video-short',
            'desc': 'Generate and edit videos with AI',
            'desc_key': 'cat.video-card-desc'
        },
        {
            'title': 'AI Audio',
            'title_key': 'cat.audio-short',
            'desc': 'Voice synthesis and music generation',
            'desc_key': 'cat.audio-card-desc'
        },
        {
            'title': 'AI Coding',
            'title_key': 'cat.coding-short',
            'desc': 'Code faster with AI-powered assistants',
            'desc_key': 'cat.coding-card-desc'
        },
        {
            'title': 'AI Productivity',
            'title_key': 'cat.productivity-short',
            'desc': 'Automate workflows and boost efficiency',
            'desc_key': 'cat.productivity-card-desc'
        },
        {
            'title': 'AI SEO &amp; Marketing',
            'title_key': 'cat.seo-short',
            'desc': 'Optimize content and grow your audience',
            'desc_key': 'cat.seo-card-desc'
        },
        {
            'title': 'AI Business',
            'title_key': 'cat.business-short',
            'desc': 'Enterprise solutions and analytics',
            'desc_key': 'cat.business-card-desc'
        },
        {
            'title': 'AI Networking',
            'title_key': 'cat.networking-short',
            'desc': 'Network automation and AIOps',
            'desc_key': 'cat.networking-card-desc'
        },
        {
            'title': 'AI Cybersecurity',
            'title_key': 'cat.cybersecurity-short',
            'desc': 'Advanced threat detection and response',
            'desc_key': 'cat.cybersecurity-card-desc'
        },
        {
            'title': 'AI Architecture',
            'title_key': 'cat.architecture-short',
            'desc': 'Building design and planning tools',
            'desc_key': 'cat.architecture-card-desc'
        },
        {
            'title': 'AI Medical',
            'title_key': 'cat.medical-short',
            'desc': 'Healthcare and diagnostic solutions',
            'desc_key': 'cat.medical-card-desc'
        },
    ]

    count = 0

    # Remplacer les titres et descriptions
    for cat in categories:
        # Remplacer le titre
        old_title = f'<h3>{cat["title"]}</h3>'
        new_title = f'<h3><span data-i18n="{cat["title_key"]}">{cat["title"]}</span></h3>'

        if old_title in content:
            content = content.replace(old_title, new_title, 1)
            count += 1
            print(f"✅ Titre: {cat['title']}")

        # Remplacer la description
        old_desc = f'<p>{cat["desc"]}</p>'
        new_desc = f'<p><span data-i18n="{cat["desc_key"]}">{cat["desc"]}</span></p>'

        if old_desc in content:
            content = content.replace(old_desc, new_desc, 1)
            count += 1
            print(f"✅ Description: {cat['desc'][:40]}...")

    # Remplacer "tools" dans tool-count
    content = content.replace('<span class="tool-count">8 tools</span>', '<span class="tool-count">8 <span data-i18n="common.tools">tools</span></span>')
    content = content.replace('<span class="tool-count">7 tools</span>', '<span class="tool-count">7 <span data-i18n="common.tools">tools</span></span>')

    # Écrire les modifications
    if content != original_content:
        with open(file_path + '.backup_cat', 'w', encoding='utf-8') as f:
            f.write(original_content)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"\n✅ {count} éléments modifiés!")
        print("📝 Backup créé: categories.html.backup_cat")
    else:
        print("\nℹ️  Aucune modification nécessaire")

if __name__ == "__main__":
    add_categories_i18n()
