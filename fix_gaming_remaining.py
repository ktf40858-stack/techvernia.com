#!/usr/bin/env python3
"""Fix remaining untranslated keys in Gaming files"""

import re
import os

# Specific Gaming translations for the main description key
GAMING_MAIN_DESCRIPTION = {
    "{TOOL} is a powerful, feature-rich gaming platform that delivers exceptional value for teams of all sizes. Highly recommended.": {
        "de": "{TOOL} ist eine leistungsstarke, funktionsreiche Gaming-Plattform, die außergewöhnlichen Wert für Teams jeder Größe bietet. Sehr empfehlenswert.",
        "fr": "{TOOL} est une plateforme de gaming puissante et riche en fonctionnalités qui offre une valeur exceptionnelle pour les équipes de toutes tailles. Hautement recommandé.",
        "es": "{TOOL} es una plataforma de gaming potente y rica en funciones que ofrece un valor excepcional para equipos de todos los tamaños. Muy recomendado.",
        "pt": "{TOOL} é uma plataforma de gaming poderosa e rica em recursos que oferece valor excepcional para equipes de todos os tamanhos. Altamente recomendado.",
        "zh": "{TOOL} 是一个功能强大、功能丰富的游戏平台，为各种规模的团队提供卓越的价值。强烈推荐。",
        "ja": "{TOOL}は、あらゆる規模のチームに卓越した価値を提供する、強力で機能豊富なゲーミングプラットフォームです。強くお勧めします。",
        "ko": "{TOOL}는 모든 규모의 팀에 뛰어난 가치를 제공하는 강력하고 기능이 풍부한 게이밍 플랫폼입니다. 적극 권장합니다.",
        "ar": "{TOOL} هي منصة ألعاب قوية وغنية بالميزات تقدم قيمة استثنائية للفرق من جميع الأحجام. موصى بها بشدة.",
        "hi": "{TOOL} एक शक्तिशाली, सुविधा संपन्न गेमिंग प्लेटफ़ॉर्म है जो सभी आकारों की टीमों के लिए असाधारण मूल्य प्रदान करता है। अत्यधिक अनुशंसित।"
    }
}

GAMING_FILES = [
    "artomatix-i18n.js",
    "charismaai-i18n.js",
    "hidden-door-i18n.js",
    "inworld-ai-i18n.js",
    "latitude-ai-dungeon-i18n.js",
    "ludoai-i18n.js",
    "promethean-ai-i18n.js",
    "rct-ai-i18n.js",
    "replika-i18n.js",
    "rosebud-ai-i18n.js",
    "scenario-i18n.js"
]

GAMING_TOOL_NAMES = {
    "artomatix": "Artomatix",
    "charismaai": "Charisma.ai",
    "hidden-door": "Hidden Door",
    "inworld-ai": "Inworld AI",
    "latitude-ai-dungeon": "AI Dungeon",
    "ludoai": "Ludo.ai",
    "promethean-ai": "Promethean AI",
    "rct-ai": "RCT AI",
    "replika": "Replika",
    "rosebud-ai": "Rosebud AI",
    "scenario": "Scenario"
}

def get_tool_name(filename):
    for key in GAMING_TOOL_NAMES:
        if filename.startswith(key):
            return GAMING_TOOL_NAMES[key]
    return "Tool"

def fix_file(filepath):
    filename = os.path.basename(filepath)
    tool_name = get_tool_name(filename)

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    updates = 0

    for english_template, translations in GAMING_MAIN_DESCRIPTION.items():
        english_text = english_template.replace("{TOOL}", tool_name)

        for lang_code, translation_template in translations.items():
            translated_text = translation_template.replace("{TOOL}", tool_name)
            english_escaped = re.escape(english_text)

            pattern = f'("{lang_code}":[\\s\\S]*?)(".*?":\\s*)("{english_escaped}")'

            def replacer(match):
                nonlocal updates
                updates += 1
                return match.group(1) + match.group(2) + '"' + translated_text + '"'

            content = re.sub(pattern, replacer, content)

    if updates > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    return updates

def main():
    base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\js"
    total = 0

    print("Fixing remaining Gaming translations...")
    for filename in GAMING_FILES:
        filepath = os.path.join(base_dir, filename)
        if os.path.exists(filepath):
            count = fix_file(filepath)
            if count > 0:
                print(f"  {filename}: {count} fixes")
                total += count

    print(f"\nTotal fixes: {total}")

if __name__ == "__main__":
    main()
