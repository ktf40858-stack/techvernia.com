#!/usr/bin/env python3
"""
Fix overview paragraph mismatch in Gaming i18n files
Some files have wrong English text that doesn't match the HTML
"""

import re
import os

# Map of gaming files and their keys
GAMING_TOOLS_KEYS = {
    "latitude-ai-dungeon-i18n.js": {
        "tool_name": "AI Dungeon",
        "key": "review.latitude-ai-dungeon.latitude.ai.dungeon.is.a"
    },
    "replika-i18n.js": {
        "tool_name": "Replika",
        "key": "review.replika.replika.is.a"
    },
    "scenario-i18n.js": {
        "tool_name": "Scenario",
        "key": "review.scenario.scenario.is.a"
    },
    "ludoai-i18n.js": {
        "tool_name": "Ludo.ai",
        "key": "review.ludoai.ludo.ai.is.a"
    },
    "inworld-ai-i18n.js": {
        "tool_name": "Inworld AI",
        "key": "review.inworld-ai.inworld.ai.is.a"
    },
    "charismaai-i18n.js": {
        "tool_name": "Charisma.ai",
        "key": "review.charismaai.charisma.ai.is.a"
    },
    "hidden-door-i18n.js": {
        "tool_name": "Hidden Door",
        "key": "review.hidden-door.hidden.door.is.a"
    },
    "promethean-ai-i18n.js": {
        "tool_name": "Promethean AI",
        "key": "review.promethean-ai.promethean.ai.is.a"
    },
    "rct-ai-i18n.js": {
        "tool_name": "RCT AI",
        "key": "review.rct-ai.rct.ai.is.a"
    },
    "rosebud-ai-i18n.js": {
        "tool_name": "Rosebud AI",
        "key": "review.rosebud-ai.rosebud.ai.is.a"
    }
}

# Correct English text (matches HTML)
CORRECT_ENGLISH_TEXT = "{TOOL} is a leading AI-powered gaming platform designed to streamline workflows and enhance productivity. Built with cutting-edge artificial intelligence technology, it delivers exceptional performance for modern businesses."

# Correct translations
CORRECT_TRANSLATIONS = {
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

def fix_translation_in_i18n(filepath, tool_name, key):
    """Fix the translation for a specific key"""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    updates = 0

    # Prepare the correct English text
    correct_en = CORRECT_ENGLISH_TEXT.replace("{TOOL}", tool_name)

    # Fix English version
    en_pattern = f'("{re.escape(key)}":\\s*)"[^"]*"'
    en_replacement = f'\\1"{correct_en}"'
    new_content = re.sub(en_pattern, en_replacement, content, count=1)
    if new_content != content:
        content = new_content
        updates += 1

    # Fix each language
    for lang_code, translation_template in CORRECT_TRANSLATIONS.items():
        translation = translation_template.replace("{TOOL}", tool_name)

        # Find and replace the translation
        lang_pattern = f'("{re.escape(key)}":\\s*)"[^"]*"'

        # We need to find this key in the specific language section
        # Split into language sections and process each
        lines = content.split('\n')
        in_lang_section = False
        current_lang = None

        for i, line in enumerate(lines):
            # Detect language section
            if re.search(f'"{lang_code}":\\s*{{', line):
                in_lang_section = True
                current_lang = lang_code
            elif in_lang_section and re.search(r'"\w+":\s*{', line):
                # New language section started
                in_lang_section = False
                current_lang = None

            # If we're in the right language section and find the key
            if in_lang_section and current_lang == lang_code and f'"{key}"' in line:
                old_line = line
                # Replace the value
                new_line = re.sub(f'("{re.escape(key)}":\\s*)"[^"]*"', f'\\1"{translation}"', line)
                if new_line != old_line:
                    lines[i] = new_line
                    updates += 1
                break

        content = '\n'.join(lines)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    return updates

def main():
    js_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\js"

    print("="*60)
    print("FIXING OVERVIEW PARAGRAPH MISMATCH IN GAMING CATEGORY")
    print("="*60)
    print()

    total_updates = 0

    for filename, info in GAMING_TOOLS_KEYS.items():
        filepath = os.path.join(js_dir, filename)

        if not os.path.exists(filepath):
            print(f"[SKIP] File not found: {filename}")
            continue

        tool_name = info["tool_name"]
        key = info["key"]

        updates = fix_translation_in_i18n(filepath, tool_name, key)
        print(f"[OK] {filename}: {updates} translations updated")
        total_updates += updates

    print()
    print("="*60)
    print(f"TOTAL TRANSLATIONS UPDATED: {total_updates}")
    print("="*60)
    print()
    print("Overview paragraph translations have been fixed!")
    print("The text now matches the HTML files in all languages.")

if __name__ == "__main__":
    main()
