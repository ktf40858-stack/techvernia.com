#!/usr/bin/env python3
"""
Script pour ajouter les attributs data-i18n aux 10 catégories restantes
"""

def add_remaining_categories():
    """Ajoute les attributs data-i18n aux catégories restantes"""

    file_path = "GenuisNet.ai/pages/categories.html"

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Liste des catégories restantes
    categories = [
        ('AI Analytics &amp; BI', 'cat.analytics-short', 'Data insights and business intelligence', 'cat.analytics-card-desc'),
        ('AI Legal &amp; Compliance', 'cat.legal-short', 'Legal research and contract analysis', 'cat.legal-card-desc'),
        ('AI Customer Service', 'cat.customer-service-short', 'Support automation and chatbots', 'cat.customer-service-card-desc'),
        ('AI Education &amp; E-Learning', 'cat.education-short', 'Learning platforms and tutoring', 'cat.education-card-desc'),
        ('AI Sales &amp; CRM', 'cat.sales-short', 'Sales automation and forecasting', 'cat.sales-card-desc'),
        ('AI Research &amp; Academia', 'cat.research-short', 'Academic research and literature review', 'cat.research-card-desc'),
        ('AI HR &amp; Recruiting', 'cat.hr-short', 'Talent acquisition and HR automation', 'cat.hr-card-desc'),
        ('AI Translation &amp; Localization', 'cat.translation-short', 'Multilingual and localization tools', 'cat.translation-card-desc'),
        ('AI Gaming &amp; Entertainment', 'cat.gaming-short', 'Game development and NPCs', 'cat.gaming-card-desc'),
        ('AI Quantum Computing', 'cat.quantum-short', 'Quantum ML and optimization', 'cat.quantum-card-desc'),
    ]

    count = 0

    for title, title_key, desc, desc_key in categories:
        # Remplacer le titre
        old_title = f'<h3>{title}</h3>'
        new_title = f'<h3><span data-i18n="{title_key}">{title}</span></h3>'

        if old_title in content:
            content = content.replace(old_title, new_title, 1)
            count += 1
            print(f"✅ Titre: {title}")

        # Remplacer la description
        old_desc = f'<p>{desc}</p>'
        new_desc = f'<p><span data-i18n="{desc_key}">{desc}</span></p>'

        if old_desc in content:
            content = content.replace(old_desc, new_desc, 1)
            count += 1
            print(f"✅ Description: {desc[:40]}...")

    # Remplacer les tool counts restants
    for num in ['15', '12', '14', '16', '10', '11']:
        old = f'<span class="tool-count">{num} tools</span>'
        new = f'<span class="tool-count">{num} <span data-i18n="common.tools">tools</span></span>'
        content = content.replace(old, new)

    # Écrire les modifications
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"\n✅ {count} éléments modifiés!")
    else:
        print("\nℹ️  Aucune modification nécessaire")

if __name__ == "__main__":
    add_remaining_categories()
