#!/usr/bin/env python3
"""
Script pour ajouter data-i18n à TOUS les éléments de texte dans chatgpt.html
"""

import re
import json
from pathlib import Path

def add_i18n_to_review():
    """Ajoute data-i18n à tous les éléments textuels de la review ChatGPT"""

    file_path = "GenuisNet.ai/pages/reviews/chatbots/chatgpt.html"

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    translations_en = {}
    translations_es = {}

    # Structure: (pattern, key_base, translation_en, translation_es)
    replacements = [
        # === HERO SECTION ===
        ('<h1>ChatGPT Review 2026</h1>',
         'review.chatgpt.title',
         '<h1><span data-i18n="review.chatgpt.title">ChatGPT Review 2026</span></h1>',
         'ChatGPT Review 2026',
         'Revisión de ChatGPT 2026'),

        ('<p class="company">by OpenAI</p>',
         'review.chatgpt.company',
         '<p class="company"><span data-i18n="review.chatgpt.company">by OpenAI</span></p>',
         'by OpenAI',
         'por OpenAI'),

        ('<span class="badge badge-popular">Most Popular AI</span>',
         'review.chatgpt.badge.popular',
         '<span class="badge badge-popular"><span data-i18n="review.chatgpt.badge.popular">Most Popular AI</span></span>',
         'Most Popular AI',
         'IA Más Popular'),

        ('<span class="badge badge-new">GPT-4 Turbo</span>',
         'review.chatgpt.badge.gpt4',
         '<span class="badge badge-new"><span data-i18n="review.chatgpt.badge.gpt4">GPT-4 Turbo</span></span>',
         'GPT-4 Turbo',
         'GPT-4 Turbo'),

        ('<span class="badge" style="background: rgba(16, 185, 129, 0.1); color: #10B981;">Free Tier Available</span>',
         'review.chatgpt.badge.free',
         '<span class="badge" style="background: rgba(16, 185, 129, 0.1); color: #10B981;"><span data-i18n="review.chatgpt.badge.free">Free Tier Available</span></span>',
         'Free Tier Available',
         'Nivel Gratis Disponible'),

        ('<div class="rating-label">Expert Rating</div>',
         'review.chatgpt.rating',
         '<div class="rating-label"><span data-i18n="review.chatgpt.rating">Expert Rating</span></div>',
         'Expert Rating',
         'Calificación de Expertos'),

        # === QUICK STATS ===
        ('<div class="quick-stat-label">Monthly Active Users</div>',
         'review.chatgpt.stats.users',
         '<div class="quick-stat-label"><span data-i18n="review.chatgpt.stats.users">Monthly Active Users</span></div>',
         'Monthly Active Users',
         'Usuarios Activos Mensuales'),

        ('<div class="quick-stat-label">Context Window</div>',
         'review.chatgpt.stats.context',
         '<div class="quick-stat-label"><span data-i18n="review.chatgpt.stats.context">Context Window</span></div>',
         'Context Window',
         'Ventana de Contexto'),

        ('<div class="quick-stat-label">Languages Supported</div>',
         'review.chatgpt.stats.languages',
         '<div class="quick-stat-label"><span data-i18n="review.chatgpt.stats.languages">Languages Supported</span></div>',
         'Languages Supported',
         'Idiomas Soportados'),

        ('<div class="quick-stat-label">Starting Price</div>',
         'review.chatgpt.stats.price',
         '<div class="quick-stat-label"><span data-i18n="review.chatgpt.stats.price">Starting Price</span></div>',
         'Starting Price',
         'Precio Inicial'),

        ('<div class="quick-stat-label">Launch Year</div>',
         'review.chatgpt.stats.year',
         '<div class="quick-stat-label"><span data-i18n="review.chatgpt.stats.year">Launch Year</span></div>',
         'Launch Year',
         'Año de Lanzamiento'),

        # === CTA BUTTONS ===
        ('<h2 id="try">Try It Now</h2>',
         'review.chatgpt.cta.title',
         '<h2 id="try"><span data-i18n="review.chatgpt.cta.title">Try It Now</span></h2>',
         'Try It Now',
         'Pruébalo Ahora'),

        ('>Try Free →<',
         'review.chatgpt.btn.try',
         '><span data-i18n="review.chatgpt.btn.try">Try Free</span> →<',
         'Try Free',
         'Probar Gratis'),

        ('>View Pricing<',
         'review.chatgpt.btn.pricing',
         '><span data-i18n="review.chatgpt.btn.pricing">View Pricing</span><',
         'View Pricing',
         'Ver Precios'),
    ]

    # Apply replacements
    for pattern, key, replacement, text_en, text_es in replacements:
        if pattern in content:
            content = content.replace(pattern, replacement, 1)
            translations_en[key] = text_en
            translations_es[key] = text_es
            print(f"✅ {key}")

    # Save modified HTML
    if content != original_content:
        # Create backup
        backup_path = file_path + '.i18n_backup'
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(original_content)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        # Save translations
        with open('chatgpt_translations_en.json', 'w', encoding='utf-8') as f:
            json.dump(translations_en, f, indent=2, ensure_ascii=False)

        with open('chatgpt_translations_es.json', 'w', encoding='utf-8') as f:
            json.dump(translations_es, f, indent=2, ensure_ascii=False)

        print(f"\n✅ {len(translations_en)} éléments modifiés!")
        print(f"📝 Backup: {backup_path}")
        print(f"📄 Traductions EN: chatgpt_translations_en.json")
        print(f"📄 Traductions ES: chatgpt_translations_es.json")
    else:
        print("\nℹ️  Aucune modification")

if __name__ == "__main__":
    add_i18n_to_review()
