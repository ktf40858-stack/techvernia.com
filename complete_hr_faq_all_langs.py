import os
import re

js_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\js"

hr_tools = {
    "beamery": "Beamery",
    "eightfold-ai": "Eightfold AI",
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
    "workable-ai": "Workable AI"
}

# FAQ questions that need to be added to all languages
faq_missing = {
    "de": {
        "faq.is.worth.the.investment": "Lohnt sich die Investition in {tool}?",
        "faq.does.offer.a.free.trial": "Bietet {tool} eine kostenlose Testversion an?"
    },
    "es": {
        "faq.is.worth.the.investment": "¿Vale la pena la inversión en {tool}?",
        "faq.does.offer.a.free.trial": "¿Ofrece {tool} una prueba gratuita?"
    },
    "fr": {
        "faq.is.worth.the.investment": "Est-ce que {tool} vaut l'investissement ?",
        "faq.does.offer.a.free.trial": "Est-ce que {tool} propose un essai gratuit ?"
    },
    "pt": {
        "faq.is.worth.the.investment": "Vale a pena o investimento em {tool}?",
        "faq.does.offer.a.free.trial": "{tool} oferece um teste gratuito?"
    },
    "zh": {
        "faq.is.worth.the.investment": "{tool}值得投资吗？",
        "faq.does.offer.a.free.trial": "{tool}提供免费试用吗？"
    },
    "ja": {
        "faq.is.worth.the.investment": "{tool}は投資する価値がありますか？",
        "faq.does.offer.a.free.trial": "{tool}は無料トライアルを提供していますか？"
    },
    "ko": {
        "faq.is.worth.the.investment": "{tool}는 투자할 가치가 있나요?",
        "faq.does.offer.a.free.trial": "{tool}는 무료 평가판을 제공하나요?"
    },
    "ar": {
        "faq.is.worth.the.investment": "هل يستحق {tool} الاستثمار؟",
        "faq.does.offer.a.free.trial": "هل يقدم {tool} نسخة تجريبية مجانية؟"
    },
    "hi": {
        "faq.is.worth.the.investment": "क्या {tool} निवेश के लायक है?",
        "faq.does.offer.a.free.trial": "क्या {tool} निःशुल्क परीक्षण प्रदान करता है?"
    }
}

def add_missing_faq(tool_key, tool_name):
    """Add missing FAQ translations to all languages"""

    js_file = os.path.join(js_dir, f"{tool_key}-i18n.js")

    if not os.path.exists(js_file):
        return False

    with open(js_file, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False

    # For each language
    for lang, questions in faq_missing.items():
        # Find language section
        lang_pattern = rf'"{lang}":\s*\{{'
        lang_match = re.search(lang_pattern, content)

        if not lang_match:
            continue

        # For each FAQ question
        for key_suffix, question_template in questions.items():
            full_key = f"review.{tool_key}.{key_suffix}"

            # Check if key already exists in this language
            # Search within the language section only
            lang_section_start = lang_match.end()
            # Find next language section or end
            next_lang_pattern = r'  "},\s*"[a-z]{2}":\s*\{|  "}\s*};'
            next_match = re.search(next_lang_pattern, content[lang_section_start:])

            if next_match:
                lang_section_end = lang_section_start + next_match.start()
            else:
                lang_section_end = len(content)

            lang_section = content[lang_section_start:lang_section_end]

            # Skip if key already exists in this language section
            if f'"{full_key}"' in lang_section:
                continue

            # Replace {tool} placeholder
            question = question_template.replace("{tool}", tool_name)

            # Add the translation at the beginning of the language section
            insert_pos = lang_match.end()
            escaped_value = question.replace('"', '\\"')
            new_line = f'\n    "{full_key}": "{escaped_value}",'
            content = content[:insert_pos] + new_line + content[insert_pos:]
            modified = True

    if modified:
        with open(js_file, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False

print("=" * 70)
print("COMPLETING FAQ TRANSLATIONS IN ALL LANGUAGES")
print("=" * 70)

completed = 0

for tool_key, tool_name in hr_tools.items():
    if add_missing_faq(tool_key, tool_name):
        print(f"  [+] {tool_name}: FAQ translations completed")
        completed += 1
    else:
        print(f"  [OK] {tool_name}: Already complete")

print("\n" + "=" * 70)
print(f"COMPLETE: {completed}/{len(hr_tools)} tools updated")
print("=" * 70)
