import os
import re

js_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\js"

translation_tools = {
    "deepl-pro": "DeepL Pro"
}

def check_missing_translations(tool_key, tool_name):
    """Check which keys exist in English but are missing in other languages"""

    js_file = os.path.join(js_dir, f"{tool_key}-i18n.js")

    if not os.path.exists(js_file):
        print(f"File not found: {js_file}")
        return

    with open(js_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract English keys
    en_pattern = r'"en":\s*\{([^}]+(?:\{[^}]+\}[^}]*)*)\}'
    en_match = re.search(en_pattern, content, re.DOTALL)

    if not en_match:
        print("English section not found")
        return

    en_section = en_match.group(1)

    # Find all keys in English section
    key_pattern = r'"(review\.[^"]+)":'
    en_keys = set(re.findall(key_pattern, en_section))

    print(f"\n{tool_name}:")
    print(f"  Total English keys: {len(en_keys)}")

    # Check each other language
    languages = ["de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]

    for lang in languages:
        lang_pattern = rf'"{lang}":\s*\{{([^}}]+(?:\{{[^}}]+\}}[^}}]*)*)\}}'
        lang_match = re.search(lang_pattern, content, re.DOTALL)

        if not lang_match:
            print(f"  [{lang}] Language section not found")
            continue

        lang_section = lang_match.group(1)
        lang_keys = set(re.findall(key_pattern, lang_section))

        missing = en_keys - lang_keys

        if missing:
            print(f"  [{lang}] Missing {len(missing)} keys:")
            for key in sorted(missing)[:10]:  # Show first 10
                print(f"    - {key}")
            if len(missing) > 10:
                print(f"    ... and {len(missing) - 10} more")
        else:
            print(f"  [{lang}] All keys present ✓")

print("=" * 70)
print("CHECKING FOR MISSING TRANSLATIONS")
print("=" * 70)

for tool_key, tool_name in translation_tools.items():
    check_missing_translations(tool_key, tool_name)

print("\n" + "=" * 70)
