#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de pré-génération HTML multilingue pour TechVernia
Traduit les fichiers HTML en utilisant les dictionnaires de traduction
"""

import os
import re
import sys
from pathlib import Path
from html.parser import HTMLParser

# Dictionnaires de traduction
FR = {
    # Navigation
    'Home': 'Accueil',
    'Categories': 'Catégories',
    'Guides': 'Guides',
    'Compare': 'Comparer',
    'AI History': 'Histoire de l\'IA',
    'About': 'À propos',
    'Blog': 'Blog',
    'Contact': 'Contact',

    # Page titles
    'Getting Started with ChatGPT': 'Commencer avec ChatGPT',
    'AI Gaming & Entertainment': 'Jeux et Divertissement IA',

    # Contenu
    'Beginner Level': 'Niveau Débutant',
    'Introduction': 'Introduction',
    'Getting Started': 'Commencer',
    'Key Concepts': 'Concepts Clés',
    'Practical Applications': 'Applications Pratiques',
    'Common Challenges & Solutions': 'Défis Courants et Solutions',
    'Next Steps': 'Prochaines Étapes',
    'Continue Learning': 'Continuer l\'Apprentissage',
    'More Beginner Guides': 'Plus de Guides Débutants',
    'Intermediate Guides': 'Guides Intermédiaires',
    'Advanced Guides': 'Guides Avancés',
    'Back to Guides': 'Retour aux Guides',
    'What You\'ll Learn': 'Ce que vous apprendrez',
    'min read': 'min de lecture',
    'lessons': 'leçons',
    'Tools': 'Outils',
    'Market Size': 'Taille du Marché',

    # Pays
    'United States': 'États-Unis',
    'France': 'France',
    'Netherlands': 'Pays-Bas',
    'UK': 'Royaume-Uni',
    'Ireland': 'Irlande',

    # Gaming
    'NPC Intelligence': 'Intelligence PNJ',
    'Game Asset Generation': 'Génération d\'Assets',
    'Game Design AI': 'IA de Conception',
    'Interactive Stories': 'Histoires Interactives',
    'World Building': 'Construction de Monde',
    'Game Generation': 'Génération de Jeux',
    'Narrative Games': 'Jeux Narratifs',
    'Procedural Content': 'Contenu Procédural',
    '3D Asset Creation': 'Création d\'Assets 3D',
    'AI Companion': 'Compagnon IA',

    # Footer
    'Your trusted source for AI tool reviews, comparisons, and guides.':
        'Votre source de confiance pour les avis, comparaisons et guides d\'outils IA.',
    'All rights reserved': 'Tous droits réservés',

    # Contenu long
    'Welcome to this comprehensive guide on getting started with chatgpt. In this guide, you\'ll discover everything you need to know to master this essential aspect of AI technology.':
        'Bienvenue dans ce guide complet pour débuter avec ChatGPT. Dans ce guide, vous découvrirez tout ce que vous devez savoir pour maîtriser cet aspect essentiel de la technologie IA.',

    'Whether you\'re just getting started or looking to expand your knowledge, this guide will provide you with practical insights, actionable strategies, and expert tips to help you succeed.':
        'Que vous débutiez ou cherchiez à élargir vos connaissances, ce guide vous fournira des informations pratiques, des stratégies concrètes et des conseils d\'experts pour vous aider à réussir.',

    'Create intelligent NPCs, generate game content, and build immersive experiences. AI-powered game design, procedural generation, and dynamic storytelling.':
        'Créez des PNJ intelligents, générez du contenu de jeu et construisez des expériences immersives. Conception de jeux assistée par IA, génération procédurale et narration dynamique.',

    'Core concepts and fundamental principles': 'Concepts fondamentaux et principes de base',
    'Practical techniques and best practices': 'Techniques pratiques et meilleures pratiques',
    'Real-world examples and use cases': 'Exemples réels et cas d\'usage',
    'Tips for optimizing your workflow': 'Conseils pour optimiser votre flux de travail',
}

AR = {
    # Navigation
    'Home': 'البيت',
    'Categories': 'الفئات',
    'Guides': 'الأدلة',
    'Compare': 'قارن',
    'AI History': 'تاريخ الذكاء الاصطناعي',
    'About': 'عن',
    'Blog': 'المدونة',
    'Contact': 'اتصل',

    # Page titles
    'Getting Started with ChatGPT': 'البدء مع ChatGPT',
    'AI Gaming & Entertainment': 'الألعاب والترفيه بالذكاء الاصطناعي',

    # Contenu
    'Beginner Level': 'المستوى المبتدئ',
    'Introduction': 'مقدمة',
    'Getting Started': 'البدء',
    'Key Concepts': 'المفاهيم الأساسية',
    'Practical Applications': 'التطبيقات العملية',
    'Common Challenges & Solutions': 'التحديات والحلول الشائعة',
    'Next Steps': 'الخطوات التالية',
    'Continue Learning': 'مواصلة التعلم',
    'More Beginner Guides': 'المزيد من أدلة المبتدئين',
    'Intermediate Guides': 'أدلة متوسطة',
    'Advanced Guides': 'أدلة متقدمة',
    'Back to Guides': 'العودة إلى الأدلة',
    'What You\'ll Learn': 'ما سوف تتعلم',
    'min read': 'دقيقة قراءة',
    'lessons': 'دروس',
    'Tools': 'أدوات',
    'Market Size': 'حجم السوق',

    # Pays
    'United States': 'الولايات المتحدة',
    'France': 'فرنسا',
    'Netherlands': 'هولندا',
    'UK': 'المملكة المتحدة',
    'Ireland': 'أيرلندا',

    # Gaming
    'NPC Intelligence': 'ذكاء الشخصيات',
    'Game Asset Generation': 'توليد أصول اللعبة',
    'Game Design AI': 'ذكاء تصميم الألعاب',
    'Interactive Stories': 'قصص تفاعلية',
    'World Building': 'بناء العالم',
    'Game Generation': 'توليد الألعاب',
    'Narrative Games': 'ألعاب سردية',
    'Procedural Content': 'محتوى إجرائي',
    '3D Asset Creation': 'إنشاء أصول ثلاثية الأبعاد',
    'AI Companion': 'رفيق الذكاء الاصطناعي',

    # Footer
    'Your trusted source for AI tool reviews, comparisons, and guides.':
        'مصدرك الموثوق لمراجعات ومقارنات وأدلة أدوات الذكاء الاصطناعي.',
    'All rights reserved': 'كل الحقوق محفوظة',

    # Contenu long
    'Create intelligent NPCs, generate game content, and build immersive experiences. AI-powered game design, procedural generation, and dynamic storytelling.':
        'إنشاء شخصيات غير لاعبة ذكية، وتوليد محتوى الألعاب، وبناء تجارب غامرة. تصميم الألعاب المدعوم بالذكاء الاصطناعي، والتوليد الإجرائي، والسرد الديناميكي.',

    'Core concepts and fundamental principles': 'المفاهيم الأساسية والمبادئ الأساسية',
    'Practical techniques and best practices': 'تقنيات عملية وأفضل الممارسات',
    'Real-world examples and use cases': 'أمثلة من العالم الحقيقي وحالات الاستخدام',
    'Tips for optimizing your workflow': 'نصائح لتحسين سير عملك',
}

ES = {
    'Home': 'Inicio',
    'Categories': 'Categorías',
    'Guides': 'Guías',
    'Getting Started with ChatGPT': 'Comenzando con ChatGPT',
    'AI Gaming & Entertainment': 'Juegos y Entretenimiento IA',
    'United States': 'Estados Unidos',
}

DE = {
    'Home': 'Startseite',
    'Categories': 'Kategorien',
    'Guides': 'Anleitungen',
    'Getting Started with ChatGPT': 'Erste Schritte mit ChatGPT',
    'AI Gaming & Entertainment': 'KI-Gaming & Unterhaltung',
    'United States': 'Vereinigte Staaten',
}

PT = {
    'Home': 'Início',
    'Categories': 'Categorias',
    'Guides': 'Guias',
    'United States': 'Estados Unidos',
}

ZH = {
    'Home': '首页',
    'Categories': '分类',
    'Guides': '指南',
    'United States': '美国',
}

JA = {
    'Home': 'ホーム',
    'Categories': 'カテゴリー',
    'Guides': 'ガイド',
    'United States': 'アメリカ合衆国',
}

KO = {
    'Home': '홈',
    'Categories': '카테고리',
    'Guides': '가이드',
    'United States': '미국',
}

HI = {
    'Home': 'होम',
    'Categories': 'श्रेणियाँ',
    'Guides': 'गाइड',
    'United States': 'संयुक्त राज्य अमेरिका',
}

DICTIONARIES = {
    'fr': FR,
    'ar': AR,
    'es': ES,
    'de': DE,
    'pt': PT,
    'zh': ZH,
    'ja': JA,
    'ko': KO,
    'hi': HI
}

# Noms à ne jamais traduire
NEVER_TRANSLATE = [
    'ChatGPT', 'Claude', 'Gemini', 'GPT-4', 'GPT-3.5', 'Midjourney',
    'DALL-E', 'DALL·E', 'Copilot', 'Perplexity', 'Stable Diffusion',
    'Leonardo AI', 'Ideogram', 'Runway', 'Pika', 'Grok', 'Poe',
    'Deepseek', 'GitHub', 'Amazon Q', 'Tabnine', 'Replit',
    'Tableau', 'Looker', 'Salesforce', 'HubSpot', 'CrowdStrike',
    'Darktrace', 'Splunk', 'Cortex', 'SentinelOne',
    'TechVernia', 'Cursor', 'VS Code', 'Codeium', 'CodeWhisperer', 'Windsurf',
    'Inworld AI', 'Scenario', 'Ludo.ai', 'Latitude', 'AI Dungeon',
    'Promethean AI', 'Rosebud AI', 'Hidden Door', 'Charisma.ai',
    'Rct AI', 'Artomatix', 'Replika'
]


def translate_text(text, dictionary):
    """Traduit un texte en utilisant le dictionnaire"""
    if not text or not text.strip():
        return text

    # Ne pas traduire si contient un nom protégé
    has_protected = any(name in text for name in NEVER_TRANSLATE)

    # Trier les clés par longueur décroissante pour traduire les phrases longues en premier
    sorted_keys = sorted(dictionary.keys(), key=len, reverse=True)

    result = text
    for key in sorted_keys:
        if key in result:
            # Traduction simple par remplacement
            result = result.replace(key, dictionary[key])

    return result


def translate_html_file(source_path, target_path, lang):
    """Traduit un fichier HTML"""
    print(f"Traduction de {source_path} -> {target_path} ({lang})...")

    dictionary = DICTIONARIES.get(lang)
    if not dictionary:
        print(f"Aucun dictionnaire pour: {lang}")
        return

    # Lire le fichier source
    with open(source_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Tags à ne pas traduire
    skip_tags = ['script', 'style', 'svg', 'code', 'pre', 'noscript']

    # Pattern pour extraire le contenu entre les balises
    # On traduit le texte qui n'est pas dans les tags à ignorer
    def replace_text(match):
        tag = match.group(1)
        content = match.group(2)

        # Ne pas traduire certains tags
        if tag.lower() in skip_tags:
            return match.group(0)

        # Traduire le contenu
        translated = translate_text(content, dictionary)
        return f"<{tag}>{translated}</{tag}>" if tag else translated

    # Traduire le texte entre balises simples
    # Pattern plus simple: on cherche juste le texte visible
    lines = html.split('\n')
    translated_lines = []

    for line in lines:
        # Ne pas traduire les lignes de scripts, styles, etc.
        if any(f'<{tag}' in line.lower() or f'</{tag}>' in line.lower() for tag in skip_tags):
            translated_lines.append(line)
            continue

        # Traduire le texte visible (hors balises HTML)
        translated_line = line

        # Extraire et traduire le texte entre >...<
        parts = re.split(r'(<[^>]+>)', translated_line)
        result_parts = []

        for part in parts:
            if part.startswith('<'):
                # C'est une balise, ne pas traduire
                result_parts.append(part)
            else:
                # C'est du texte, traduire
                result_parts.append(translate_text(part, dictionary))

        translated_lines.append(''.join(result_parts))

    translated_html = '\n'.join(translated_lines)

    # Sauvegarder
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(translated_html)

    print(f"[OK] Fichier traduit: {target_path}")


def translate_language(lang, base_dir):
    """Traduit tous les fichiers d'une langue"""
    print(f"\n=== Traduction pour {lang} ===\n")

    docs_dir = os.path.join(base_dir, 'docs')
    lang_dir = os.path.join(docs_dir, lang)

    if not os.path.exists(lang_dir):
        print(f"Le dossier {lang_dir} n'existe pas")
        return

    # Parcourir tous les fichiers HTML
    for root, dirs, files in os.walk(lang_dir):
        # Ignorer certains dossiers
        dirs[:] = [d for d in dirs if d not in ['js', 'css', 'assets']]

        for file in files:
            if file.endswith('.html'):
                target_path = os.path.join(root, file)

                # Trouver le fichier source anglais
                rel_path = os.path.relpath(target_path, lang_dir)
                source_path = os.path.join(docs_dir, rel_path)

                if os.path.exists(source_path):
                    translate_html_file(source_path, target_path, lang)


def main():
    if len(sys.argv) < 2:
        print("Usage: python translate_html.py [langue]")
        print("Langues disponibles: fr, ar, es, de, pt, zh, ja, ko, hi, all")
        print("Exemple: python translate_html.py ar")
        print("Exemple: python translate_html.py all")
        sys.exit(1)

    lang = sys.argv[1]
    base_dir = os.path.dirname(os.path.abspath(__file__))

    if lang == 'all':
        for l in DICTIONARIES.keys():
            translate_language(l, base_dir)
    elif lang in DICTIONARIES:
        translate_language(lang, base_dir)
    else:
        print(f"Langue non supportée: {lang}")
        print(f"Langues disponibles: {', '.join(DICTIONARIES.keys())}")
        sys.exit(1)

    print("\n[OK] Traduction terminee!")


if __name__ == '__main__':
    main()
