#!/usr/bin/env python3
"""Fix remaining untranslated keys in HR files"""

import re
import os

# Specific HR translations for the main description key
HR_MAIN_DESCRIPTION = {
    "{TOOL} is a powerful, feature-rich hr platform that delivers exceptional value for teams of all sizes. Highly recommended.": {
        "de": "{TOOL} ist eine leistungsstarke, funktionsreiche HR-Plattform, die außergewöhnlichen Wert für Teams jeder Größe bietet. Sehr empfehlenswert.",
        "fr": "{TOOL} est une plateforme RH puissante et riche en fonctionnalités qui offre une valeur exceptionnelle pour les équipes de toutes tailles. Hautement recommandé.",
        "es": "{TOOL} es una plataforma de RR.HH. potente y rica en funciones que ofrece un valor excepcional para equipos de todos los tamaños. Muy recomendado.",
        "pt": "{TOOL} é uma plataforma de RH poderosa e rica em recursos que oferece valor excepcional para equipes de todos os tamanhos. Altamente recomendado.",
        "zh": "{TOOL} 是一个功能强大、功能丰富的人力资源平台，为各种规模的团队提供卓越的价值。强烈推荐。",
        "ja": "{TOOL}は、あらゆる規模のチームに卓越した価値を提供する、強力で機能豊富なHRプラットフォームです。強くお勧めします。",
        "ko": "{TOOL}는 모든 규모의 팀에 뛰어난 가치를 제공하는 강력하고 기능이 풍부한 HR 플랫폼입니다. 적극 권장합니다.",
        "ar": "{TOOL} هي منصة موارد بشرية قوية وغنية بالميزات تقدم قيمة استثنائية للفرق من جميع الأحجام. موصى بها بشدة.",
        "hi": "{TOOL} एक शक्तिशाली, सुविधा संपन्न HR प्लेटफ़ॉर्म है जो सभी आकारों की टीमों के लिए असाधारण मूल्य प्रदान करता है। अत्यधिक अनुशंसित।"
    }
}

HR_FILES = [
    "beamery-i18n.js",
    "eightfold-ai-i18n.js",
    "fetcher-i18n.js",
    "findem-i18n.js",
    "harver-i18n.js",
    "hirevue-i18n.js",
    "humanly-i18n.js",
    "paradox-olivia-i18n.js",
    "phenom-i18n.js",
    "pymetrics-i18n.js",
    "seekout-i18n.js",
    "sense-i18n.js",
    "textio-i18n.js",
    "workable-ai-i18n.js"
]

HR_TOOL_NAMES = {
    "beamery": "Beamery",
    "eightfold-ai": "Eightfold.ai",
    "fetcher": "Fetcher",
    "findem": "Findem",
    "harver": "Harver",
    "hirevue": "HireVue",
    "humanly": "Humanly",
    "paradox-olivia": "Paradox (Olivia)",
    "phenom": "Phenom",
    "pymetrics": "Pymetrics",
    "seekout": "SeekOut",
    "sense": "Sense",
    "textio": "Textio",
    "workable-ai": "Workable"
}

def get_tool_name(filename):
    for key in HR_TOOL_NAMES:
        if filename.startswith(key):
            return HR_TOOL_NAMES[key]
    return "Tool"

def fix_file(filepath):
    filename = os.path.basename(filepath)
    tool_name = get_tool_name(filename)

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    updates = 0

    for english_template, translations in HR_MAIN_DESCRIPTION.items():
        english_text = english_template.replace("{TOOL}", tool_name)

        for lang_code, translation_template in translations.items():
            translated_text = translation_template.replace("{TOOL}", tool_name)
            english_escaped = re.escape(english_text)

            pattern = f'("{lang_code}":[\\s\\S]*?)(".*?":\\s*")({english_escaped})(")'

            def replacer(match):
                nonlocal updates
                updates += 1
                return match.group(1) + match.group(2) + translated_text + match.group(4)

            content = re.sub(pattern, replacer, content)

    if updates > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    return updates

def main():
    base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\js"
    total = 0

    print("Fixing remaining HR translations...")
    for filename in HR_FILES:
        filepath = os.path.join(base_dir, filename)
        if os.path.exists(filepath):
            count = fix_file(filepath)
            if count > 0:
                print(f"  {filename}: {count} fixes")
                total += count

    print(f"\nTotal fixes: {total}")

if __name__ == "__main__":
    main()
