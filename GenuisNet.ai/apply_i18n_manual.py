#!/usr/bin/env python3
"""
Appliquer data-i18n manuellement avec regex pour préserver la structure HTML
"""

import re

def apply_i18n_to_index():
    """Appliquer les data-i18n à index.html de manière précise"""

    print("\n" + "="*80)
    print("🔧 APPLICATION MANUELLE DES data-i18n")
    print("="*80 + "\n")

    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Compteur de modifications
    modifications = 0

    # 1. Hero section - Titre principal
    content = re.sub(
        r'(<span class="gradient-text">)\s*Discover the Future\s*(</span>)',
        r'\1<span data-i18n="hero.discover-the-future">Discover the Future</span>\2',
        content
    )
    modifications += 1

    content = re.sub(
        r'(<span class="gradient-text-alt">)\s*of AI Tools\s*(</span>)',
        r'\1<span data-i18n="hero.of-ai-tools">of AI Tools</span>\2',
        content
    )
    modifications += 1

    # 2. Navigation - Ne PAS toucher au mega menu, juste les liens principaux
    nav_items = {
        'Home': 'nav.home',
        'Categories': 'nav.categories',
        'Guides': 'nav.guides',
        'Compare': 'nav.compare',
        'About': 'nav.about',
        'Blog': 'nav.blog',
        'Contact': 'nav.contact',
    }

    for text, key in nav_items.items():
        # Seulement dans la navigation principale, pas dans le mega menu
        pattern = rf'(<a[^>]*class="nav-link"[^>]*>)\s*{text}\s*(</a>)'
        replacement = rf'\1<span data-i18n="{key}">{text}</span>\2'
        content, count = re.subn(pattern, replacement, content)
        modifications += count

    # 3. Boutons CTA
    cta_buttons = [
        ('Explore AI Tools', 'btn.explore-ai-tools'),
        ('Read Guides', 'btn.read-guides'),
        ('Browse Categories', 'btn.browse-categories'),
        ('Read Full Review', 'btn.read-full-review'),
        ('Try ChatGPT Free', 'btn.try-chatgpt-free'),
        ('Try Claude Free', 'btn.try-claude-free'),
        ('Try Midjourney', 'btn.try-midjourney'),
        ('Try Cursor Free', 'btn.try-cursor-free'),
        ('Try ElevenLabs', 'btn.try-elevenlabs'),
        ('Try Runway', 'btn.try-runway'),
    ]

    for text, key in cta_buttons:
        pattern = rf'(<(?:a|button)[^>]*>)\s*{re.escape(text)}\s*(</(?:a|button)>)'
        replacement = rf'\1<span data-i18n="{key}">{text}</span>\2'
        content, count = re.subn(pattern, replacement, content, count=1)
        modifications += count

    # 4. Sections spotlight - Titres des outils
    tool_titles = [
        ('ChatGPT-4', 'section.chatgpt-4'),
        ('Claude 4.5 Sonnet', 'section.claude-45-sonnet'),
        ('Midjourney V6', 'section.midjourney-v6'),
        ('Cursor', 'section.cursor'),
        ('Runway Gen-3', 'section.runway-gen-3'),
        ('ElevenLabs', 'section.elevenlabs'),
    ]

    for text, key in tool_titles:
        pattern = rf'(<h2[^>]*>)\s*{re.escape(text)}\s*(</h2>)'
        replacement = rf'\1<span data-i18n="{key}">{text}</span>\2'
        content, count = re.subn(pattern, replacement, content)
        modifications += count

    # 5. Taglines des outils
    taglines = [
        ('Create breathtaking art from text', 'section.create-breathtaking-art-from-t'),
        ('Hollywood-quality AI video generation', 'section.hollywood-quality-ai-video-gen'),
        ('Faster Coding', 'section.faster-coding'),
    ]

    for text, key in taglines:
        pattern = rf'(<p[^>]*class="[^"]*spotlight-tagline[^"]*"[^>]*>)\s*{re.escape(text)}\s*(</p>)'
        replacement = rf'\1<span data-i18n="{key}">{text}</span>\2'
        content, count = re.subn(pattern, replacement, content)
        modifications += count

    # 6. Footer - Liens
    footer_items = {
        'AI Chatbots': 'footer.ai-chatbots',
        'AI Writing': 'footer.ai-writing',
        'AI Image': 'footer.ai-image',
        'AI Video': 'footer.ai-video',
        'AI Coding': 'footer.ai-coding',
        'AI Networking': 'footer.ai-networking',
        'All Tools': 'footer.all-tools',
        'Comparisons': 'footer.comparisons',
        'About Us': 'footer.about-us',
        'Privacy Policy': 'footer.privacy-policy',
        'Terms of Service': 'footer.terms-of-service',
        'Affiliate Disclosure': 'footer.affiliate-disclosure',
    }

    for text, key in footer_items.items():
        pattern = rf'(<(?:a|li)[^>]*>)\s*{re.escape(text)}\s*(</(?:a|li)>)'
        replacement = rf'\1<span data-i18n="{key}">{text}</span>\2'
        content, count = re.subn(pattern, replacement, content)
        modifications += count

    # 7. Cards features
    feature_cards = [
        ('Curated Selection', 'card.curated-selection'),
        ('Expert Insights', 'card.expert-insights'),
        ('Always Updated', 'card.always-updated'),
    ]

    for text, key in feature_cards:
        pattern = rf'(<h3[^>]*>)\s*{re.escape(text)}\s*(</h3>)'
        replacement = rf'\1<span data-i18n="{key}">{text}</span>\2'
        content, count = re.subn(pattern, replacement, content)
        modifications += count

    # 8. Attributs alt des images (quelques clés seulement pour ne pas surcharger)
    img_alts = [
        ('GenuisNet.ai Logo', 'nav.genuisnetai-logo'),
        ('ChatGPT', 'section.chatgpt'),
        ('Claude', 'section.claude'),
        ('Midjourney', 'section.midjourney'),
        ('Cursor', 'section.cursor'),
    ]

    for text, key in img_alts:
        pattern = rf'(<img[^>]*alt="){re.escape(text)}("[^>]*>)'
        replacement = rf'\1{text}\2'
        # Ajouter data-i18n-alt avant le >
        pattern2 = rf'(<img[^>]*alt="{re.escape(text)}"[^>]*)(>)'
        replacement2 = rf'\1 data-i18n-alt="{key}"\2'
        content, count = re.subn(pattern2, replacement2, content)
        modifications += count

    # Sauvegarder
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ {modifications} modifications appliquées")
    print(f"✅ index.html mis à jour")
    print(f"\n{'='*80}")
    print(f"✅ APPLICATION TERMINÉE")
    print(f"{'='*80}\n")

    return modifications

if __name__ == "__main__":
    apply_i18n_to_index()
