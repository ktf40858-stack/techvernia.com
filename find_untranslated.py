#!/usr/bin/env python3
"""Find all untranslated keys in translation i18n files"""

import re

def find_untranslated_keys(filepath, sample_size=30):
    """Find keys that are still in English in non-English language sections"""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract French section as sample
    fr_match = re.search(r'"fr":\s*\{(.*?)\n  \},\s*"es":', content, re.DOTALL)
    if not fr_match:
        print(f"Could not find French section in {filepath}")
        return

    fr_section = fr_match.group(1)

    # Find all key-value pairs
    pattern = r'"([^"]+)":\s*"([^"]+)"'
    matches = re.findall(pattern, fr_section)

    # Check which values contain English indicators
    english_indicators = [
        'is a ', 'are ', 'the ', 'with ', 'for ', 'and ', 'can ',
        'you ', 'your ', 'our ', 'all ', 'this ', 'that ', 'from ',
        'have ', 'been ', 'will ', 'Pro ', 'Excels For', 'vs ',
        'interface:', 'Questions', 'Verdict'
    ]

    untranslated = []
    for key, value in matches:
        # Check if value is likely in English
        if any(indicator.lower() in value.lower() for indicator in english_indicators):
            untranslated.append((key, value))

    print(f"\n{'='*80}")
    print(f"File: {filepath}")
    print(f"Total keys in French section: {len(matches)}")
    print(f"Untranslated keys: {len(untranslated)}")
    print(f"{'='*80}\n")

    print(f"First {sample_size} untranslated keys:\n")
    for i, (key, value) in enumerate(untranslated[:sample_size], 1):
        # Truncate long values
        display_value = value if len(value) <= 60 else value[:57] + "..."
        print(f"{i:2d}. {key}")
        print(f"    EN: {display_value}\n")

    return untranslated

if __name__ == "__main__":
    files = [
        r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\js\deepl-pro-i18n.js",
        r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\js\lilt-i18n.js",
    ]

    for filepath in files:
        try:
            find_untranslated_keys(filepath)
        except Exception as e:
            print(f"Error processing {filepath}: {e}")
