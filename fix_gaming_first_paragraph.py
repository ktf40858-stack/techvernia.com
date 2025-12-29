#!/usr/bin/env python3
"""
Fix first paragraph translations in Gaming i18n files
The HTML has "leading AI-powered" but i18n files have "powerful, feature-rich"
Need to update all i18n files with correct translations
"""

import re
import os

# Correct translations for the first paragraph
FIRST_PARAGRAPH_TRANSLATIONS = {
    "de": "{TOOL} ist eine führende KI-gestützte Gaming-Plattform, die entwickelt wurde, um Workflows zu optimieren und die Produktivität zu steigern. Mit modernster Technologie der künstlichen Intelligenz bietet sie außergewöhnliche Leistung für moderne Unternehmen.",
    "fr": "{TOOL} est une plateforme de gaming alimentée par l'IA de premier plan, conçue pour rationaliser les flux de travail et améliorer la productivité. Construite avec une technologie d'intelligence artificielle de pointe, elle offre des performances exceptionnelles pour les entreprises modernes.",
    "es": "{TOOL} es una plataforma de gaming impulsada por IA líder diseñada para optimizar flujos de trabajo y mejorar la productividad. Construida con tecnología de inteligencia artificial de vanguardia, ofrece un rendimiento excepcional para las empresas modernas.",
    "pt": "{TOOL} é uma plataforma de gaming alimentada por IA líder projetada para otimizar fluxos de trabalho e aumentar a produtividade. Construída com tecnologia de inteligência artificial de ponta, oferece desempenho excepcional para empresas modernas.",
    "zh": "{TOOL} 是一个领先的AI驱动游戏平台，旨在简化工作流程并提高生产力。采用尖端人工智能技术构建，为现代企业提供卓越性能。",
    "ja": "{TOOL}は、ワークフローを合理化し生産性を向上させるために設計された、AI駆動の主要なゲーミングプラットフォームです。最先端の人工知能技術で構築され、現代のビジネスに卓越したパフォーマンスを提供します。",
    "ko": "{TOOL}는 워크플로우를 간소화하고 생산성을 향상시키도록 설계된 선도적인 AI 기반 게이밍 플랫폼입니다. 최첨단 인공지능 기술로 구축되어 현대 비즈니스에 탁월한 성능을 제공합니다.",
    "ar": "{TOOL} هي منصة ألعاب رائدة مدعومة بالذكاء الاصطناعي مصممة لتبسيط سير العمل وتعزيز الإنتاجية. مبنية بتكنولوجيا الذكاء الاصطناعي المتطورة، توفر أداءً استثنائيًا للشركات الحديثة.",
    "hi": "{TOOL} एक अग्रणी AI-संचालित गेमिंग प्लेटफ़ॉर्म है जो वर्कफ़्लो को सुव्यवस्थित करने और उत्पादकता बढ़ाने के लिए डिज़ाइन किया गया है। अत्याधुनिक आर्टिफिशियल इंटेलिजेंस तकनीक से निर्मित, यह आधुनिक व्यवसायों के लिए असाधारण प्रदर्शन प्रदान करता है।"
}

GAMING_TOOLS = {
    "artomatix-i18n.js": "Artomatix",
    "charismaai-i18n.js": "Charisma.ai",
    "hidden-door-i18n.js": "Hidden Door",
    "inworld-ai-i18n.js": "Inworld AI",
    "latitude-ai-dungeon-i18n.js": "AI Dungeon",
    "ludoai-i18n.js": "Ludo.ai",
    "promethean-ai-i18n.js": "Promethean AI",
    "rct-ai-i18n.js": "RCT AI",
    "replika-i18n.js": "Replika",
    "rosebud-ai-i18n.js": "Rosebud AI",
    "scenario-i18n.js": "Scenario"
}

def get_i18n_key(filename):
    """Get the i18n key prefix for a tool"""
    base = filename.replace("-i18n.js", "")
    return base

def fix_first_paragraph_translation(filepath, tool_name, tool_key):
    """Fix the first paragraph translation in i18n file"""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    updates = 0

    i18n_key = f"review.{tool_key}.{tool_key}.is.a"

    # For each language, find and replace the wrong translation
    for lang_code, translation_template in FIRST_PARAGRAPH_TRANSLATIONS.items():
        translation = translation_template.replace("{TOOL}", tool_name)

        # Find the language section and locate the key
        # Pattern: "review.tool.tool.is.a": "old text"
        # Replace with new translation

        pattern = f'("{i18n_key}":\\s*)"[^"]*"'
        replacement = f'\\1"{translation}"'

        new_content = re.sub(pattern, replacement, content)
        if new_content != content:
            content = new_content
            updates += 1

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    return updates

def main():
    js_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\js"

    print("="*60)
    print("FIXING FIRST PARAGRAPH TRANSLATIONS IN GAMING CATEGORY")
    print("="*60)
    print()

    total_updates = 0

    for filename, tool_name in GAMING_TOOLS.items():
        filepath = os.path.join(js_dir, filename)

        if not os.path.exists(filepath):
            print(f"[SKIP] File not found: {filename}")
            continue

        tool_key = get_i18n_key(filename)
        updates = fix_first_paragraph_translation(filepath, tool_name, tool_key)

        print(f"[OK] {filename}: {updates} translations updated")
        total_updates += updates

    print()
    print("="*60)
    print(f"TOTAL TRANSLATIONS UPDATED: {total_updates}")
    print("="*60)
    print()
    print("First paragraph translations have been fixed!")
    print("The text now matches the HTML files.")

if __name__ == "__main__":
    main()
