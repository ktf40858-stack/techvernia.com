import os
import re

js_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\js"

translation_tools = {
    "deepl-pro": {"name": "DeepL Pro", "key_part": "deepl.pro"},
    "google-translate-ai": {"name": "Google Translate AI", "key_part": "google.translate.ai"},
    "lilt": {"name": "Lilt", "key_part": "lilt"},
    "lokalise": {"name": "Lokalise", "key_part": "lokalise"},
    "microsoft-translator": {"name": "Microsoft Translator", "key_part": "microsoft.translator"},
    "modernmt": {"name": "ModernMT", "key_part": "modernmt"},
    "phrase": {"name": "Phrase", "key_part": "phrase"},
    "smartling": {"name": "Smartling", "key_part": "smartling"},
    "systran": {"name": "SYSTRAN", "key_part": "systran"},
    "unbabel": {"name": "Unbabel", "key_part": "unbabel"}
}

def fix_use_case_key_names(tool_key, tool_info):
    """Fix use case key names to match HTML expectations"""

    js_file = os.path.join(js_dir, f"{tool_key}-i18n.js")
    tool_name = tool_info["name"]
    key_part = tool_info["key_part"]

    if not os.path.exists(js_file):
        return False

    with open(js_file, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Fix the "excels for" key - replace tool-key.tool-key with tool-key.key_part
    wrong_key = f'"review.{tool_key}.{tool_key}.excels.for"'
    correct_key = f'"review.{tool_key}.{key_part}.excels.for"'

    content = content.replace(wrong_key, correct_key)

    if content != original_content:
        with open(js_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  [+] Fixed key names")
        return True

    return False

print("=" * 70)
print("FIXING USE CASE KEY NAMES TO MATCH HTML")
print("=" * 70)

fixed_count = 0

for tool_key, tool_info in translation_tools.items():
    print(f"\n{tool_info['name']}:")
    if fix_use_case_key_names(tool_key, tool_info):
        fixed_count += 1
    else:
        print(f"  [OK] Keys already correct")

print("\n" + "=" * 70)
print(f"COMPLETE: {fixed_count}/10 tools updated")
print("=" * 70)
print("\nUse case keys now match HTML expectations!")
print("=" * 70)
