import os
import re

js_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\js"

translation_tools = {
    "deepl-pro": "DeepL Pro",
    "google-translate-ai": "Google Translate AI",
    "lilt": "Lilt",
    "lokalise": "Lokalise",
    "microsoft-translator": "Microsoft Translator",
    "modernmt": "ModernMT",
    "phrase": "Phrase",
    "smartling": "Smartling",
    "systran": "SYSTRAN",
    "unbabel": "Unbabel"
}

def extract_kv_pairs(section_text):
    """Extract key-value pairs from a language section"""
    # Match key: value pairs, handling escaped quotes
    kv_pattern = r'    "([^"]+)":\s*"([^"\\]*(?:\\.[^"\\]*)*)"'
    return dict(re.findall(kv_pattern, section_text))

def get_section_bounds(content, lang):
    """Get start and end positions of a language section"""
    # Find section start: "lang": {
    start_pattern = rf'  "{lang}":\s*{{\n'
    start_match = re.search(start_pattern, content)

    if not start_match:
        return None, None

    start_pos = start_match.end()

    # Find section end: either next language or closing of translations object
    # Count braces to find the matching closing brace
    brace_count = 1
    pos = start_pos

    while pos < len(content) and brace_count > 0:
        if content[pos] == '{':
            brace_count += 1
        elif content[pos] == '}':
            brace_count -= 1
        pos += 1

    end_pos = pos - 2  # Before the closing brace

    return start_pos, end_pos

def copy_missing_english_keys(tool_key, tool_name):
    """Copy all missing English keys to other languages"""

    js_file = os.path.join(js_dir, f"{tool_key}-i18n.js")

    if not os.path.exists(js_file):
        print(f"  [!] File not found")
        return False

    with open(js_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract English section
    en_start, en_end = get_section_bounds(content, "en")
    if en_start is None:
        print(f"  [!] English section not found")
        return False

    en_section = content[en_start:en_end]
    en_pairs = extract_kv_pairs(en_section)

    if not en_pairs:
        print(f"  [!] No English keys found")
        return False

    print(f"\n{tool_name}:")
    print(f"  English keys: {len(en_pairs)}")

    languages = ["de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]
    modified = False

    for lang in languages:
        lang_start, lang_end = get_section_bounds(content, lang)

        if lang_start is None:
            print(f"  [{lang}] Section not found - skipping")
            continue

        lang_section = content[lang_start:lang_end]
        lang_pairs = extract_kv_pairs(lang_section)

        # Find missing keys
        missing_keys = set(en_pairs.keys()) - set(lang_pairs.keys())

        if not missing_keys:
            print(f"  [{lang}] All keys present ✓")
            continue

        # Add missing keys with English text
        lines_to_add = []
        for key in sorted(missing_keys):
            value = en_pairs[key]
            lines_to_add.append(f'    "{key}": "{value}",\n')

        if lines_to_add:
            # Insert at the beginning of the language section
            new_content = ''.join(lines_to_add)
            content = content[:lang_start] + new_content + content[lang_start:]
            modified = True
            print(f"  [{lang}] Added {len(lines_to_add)} missing keys")

    if modified:
        with open(js_file, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False

print("=" * 70)
print("COPYING MISSING ENGLISH KEYS TO ALL LANGUAGES")
print("=" * 70)
print("Note: This copies English text as placeholder.")
print("Translations can be refined later.")
print("=" * 70)

fixed_count = 0

for tool_key, tool_name in translation_tools.items():
    if copy_missing_english_keys(tool_key, tool_name):
        fixed_count += 1

print("\n" + "=" * 70)
print(f"COMPLETE: {fixed_count}/10 tools updated")
print("=" * 70)
print("\nAll keys now exist in all languages!")
print("English text is used as placeholder where translations are missing.")
print("=" * 70)
