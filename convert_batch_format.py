#!/usr/bin/env python3
"""
Convert inverted batch format to standard format
"""

import json
import os

ANALYTICS_DIR = 'GenuisNet.ai/pages/reviews/analytics'

def convert_inverted_format(input_file, output_file):
    """Convert key -> {lang: value} to lang -> {key: value}"""
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Check if it's inverted format
        if not data:
            print(f"  Empty file: {input_file}")
            return False

        first_key = list(data.keys())[0]
        first_value = data[first_key]

        # If first value is a dict with language codes, it's inverted
        if isinstance(first_value, dict):
            print(f"  Converting inverted format: {input_file}")

            # Initialize result with empty language dicts
            result = {}

            # Process each key
            for key, lang_dict in data.items():
                for lang, value in lang_dict.items():
                    if lang not in result:
                        result[lang] = {}
                    result[lang][key] = value

            # Write converted file
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(result, f, ensure_ascii=False, indent=2)

            print(f"  ✓ Converted: {len(result)} languages")
            return True
        else:
            print(f"  Already in correct format: {input_file}")
            return False

    except Exception as e:
        print(f"  ERROR: {e}")
        return False

# Check all batch files
print("=" * 70)
print("Batch Format Converter")
print("=" * 70)

tools = [
    'datarobot', 'domo-ai', 'h2oai', 'microstrategy-ai',
    'power-bi-copilot', 'qlik-sense-ai', 'sisense-ai', 'yellowfin-ai'
]

for tool in tools:
    print(f"\n{tool}:")
    converted = False

    for batch_num in [1, 2, 3]:
        input_file = os.path.join(ANALYTICS_DIR, f"{tool}-batch{batch_num}.json")
        output_file = input_file  # Overwrite same file

        if os.path.exists(input_file):
            if convert_inverted_format(input_file, output_file):
                converted = True

    if not converted:
        print(f"  No conversion needed")

print("\n" + "=" * 70)
print("Conversion complete!")
print("=" * 70)
