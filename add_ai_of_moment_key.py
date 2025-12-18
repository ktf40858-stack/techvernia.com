#!/usr/bin/env python3
"""
Script pour ajouter la clé "section.ai-of-the-moment" dans toutes les langues restantes
"""

import re

def add_key_to_all_languages():
    """Ajoute la clé ai-of-the-moment dans toutes les langues"""

    file_path = "GenuisNet.ai/js/i18n.js"

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Traductions pour chaque langue
    translations = {
        'de': 'KI des Moments',  # Allemand
        'pt': 'IA do Momento',   # Portugais
        'zh': '当下AI',          # Chinois simplifié
        'ja': '今のAI',          # Japonais
        'ko': '순간의 AI',        # Coréen
        'ar': 'الذكاء الاصطناعي اللحظة',  # Arabe
        'hi': 'पल का AI',        # Hindi
    }

    # Remplacements pour chaque langue
    replacements = {
        'de': {
            'pattern': r'("section\.claude-by-anthropic-represents": "Claude by Anthropic.*?",\n        "section\.coding-benchmarks": "Coding-Benchmarks",)',
            'insertion': 'section.coding-benchmarks'
        },
        'pt': {
            'pattern': r'("section\.claude-by-anthropic-represents": "Claude by Anthropic.*?",\n        "section\.coding-benchmarks": "Benchmarks de Código",)',
            'insertion': 'section.coding-benchmarks'
        },
        'zh': {
            'pattern': r'("section\.claude-by-anthropic-represents": "Claude by Anthropic.*?",\n        "section\.coding-benchmarks": "编码基准",)',
            'insertion': 'section.coding-benchmarks'
        },
        'ja': {
            'pattern': r'("section\.claude-by-anthropic-represents": "Claude by Anthropic.*?",\n        "section\.coding-benchmarks": "コーディングベンチマーク",)',
            'insertion': 'section.coding-benchmarks'
        },
        'ko': {
            'pattern': r'("section\.claude-by-anthropic-represents": "Claude by Anthropic.*?",\n        "section\.coding-benchmarks": "코딩 벤치마크",)',
            'insertion': 'section.coding-benchmarks'
        },
        'ar': {
            'pattern': r'("section\.claude-by-anthropic-represents": "Claude by Anthropic.*?",\n        "section\.coding-benchmarks": "معايير البرمجة",)',
            'insertion': 'section.coding-benchmarks'
        },
        'hi': {
            'pattern': r'("section\.claude-by-anthropic-represents": "Claude by Anthropic.*?",\n        "section\.coding-benchmarks": "कोडिंग बेंचमार्क",)',
            'insertion': 'section.coding-benchmarks'
        },
    }

    # Trouver et remplacer pour chaque langue
    for lang_code in ['de', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']:
        # Trouver la section de coding-benchmarks pour cette langue
        if lang_code == 'de':
            old = '"section.coding-benchmarks": "Coding-Benchmarks",'
            new = '"section.ai-of-the-moment": "KI des Moments",\n        "section.coding-benchmarks": "Coding-Benchmarks",'
        elif lang_code == 'pt':
            old = '"section.coding-benchmarks": "Benchmarks de Código",\n        "section.community-driven": "Impulsionado pela Comunidade",'
            new = '"section.ai-of-the-moment": "IA do Momento",\n        "section.coding-benchmarks": "Benchmarks de Código",\n        "section.community-driven": "Impulsionado pela Comunidade",'
        elif lang_code == 'zh':
            old = '"section.coding-benchmarks": "编码基准",\n        "section.community-driven": "社区驱动",'
            new = '"section.ai-of-the-moment": "当下AI",\n        "section.coding-benchmarks": "编码基准",\n        "section.community-driven": "社区驱动",'
        elif lang_code == 'ja':
            old = '"section.coding-benchmarks": "コーディングベンチマーク",\n        "section.community-driven": "コミュニティ主導",'
            new = '"section.ai-of-the-moment": "今のAI",\n        "section.coding-benchmarks": "コーディングベンチマーク",\n        "section.community-driven": "コミュニティ主導",'
        elif lang_code == 'ko':
            old = '"section.coding-benchmarks": "코딩 벤치마크",\n        "section.community-driven": "커뮤니티 주도",'
            new = '"section.ai-of-the-moment": "순간의 AI",\n        "section.coding-benchmarks": "코딩 벤치마크",\n        "section.community-driven": "커뮤니티 주도",'
        elif lang_code == 'ar':
            old = '"section.coding-benchmarks": "معايير البرمجة",\n        "section.community-driven": "مدعوم من المجتمع",'
            new = '"section.ai-of-the-moment": "الذكاء الاصطناعي اللحظة",\n        "section.coding-benchmarks": "معايير البرمجة",\n        "section.community-driven": "مدعوم من المجتمع",'
        elif lang_code == 'hi':
            old = '"section.coding-benchmarks": "कोडिंग बेंचमार्क",\n        "section.community-driven": "समुदाय संचालित",'
            new = '"section.ai-of-the-moment": "पल का AI",\n        "section.coding-benchmarks": "कोडिंग बेंचमार्क",\n        "section.community-driven": "समुदाय संचालित",'

        # Remplacer dans le contenu
        if old in content:
            content = content.replace(old, new, 1)
            print(f"✅ {lang_code}: clé ajoutée - {translations[lang_code]}")
        else:
            print(f"⚠️  {lang_code}: pattern non trouvé")

    # Écrire les modifications
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("\n✅ Toutes les clés ont été ajoutées!")
    else:
        print("\nℹ️  Aucune modification apportée")

if __name__ == "__main__":
    add_key_to_all_languages()
