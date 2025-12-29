#!/usr/bin/env python3
"""Extract FAQ-only content from Medical EN files."""
import json
from pathlib import Path

MEDICAL_TOOLS = [
    'aidoc', 'butterfly-iq', 'nuance-dragon', 'paige-ai',
    'pathai', 'tempus', 'viz-ai', 'zebra-medical'
]

BASE_DIR = Path("GenuisNet.ai/pages/reviews/medical")

def extract_faq_keys(tool_name):
    """Extract only FAQ keys from EN file."""
    en_file = BASE_DIR / f"{tool_name}-en.json"

    with open(en_file, 'r', encoding='utf-8') as f:
        all_content = json.load(f)

    # Filter only FAQ keys
    faq_content = {k: v for k, v in all_content.items() if '.faq.' in k}

    return faq_content

def main():
    print("="*60)
    print("EXTRACTING FAQ CONTENT FROM MEDICAL TOOLS")
    print("="*60)

    total_faq_keys = 0

    for tool in MEDICAL_TOOLS:
        faq_content = extract_faq_keys(tool)

        # Save FAQ-only file
        output_file = BASE_DIR / f"{tool}-faqs-en.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(faq_content, f, ensure_ascii=False, indent=2)

        print(f"[OK] {tool}: {len(faq_content)} FAQ keys -> {output_file.name}")
        total_faq_keys += len(faq_content)

    print("="*60)
    print(f"TOTAL FAQ KEYS: {total_faq_keys}")
    print("="*60)

if __name__ == "__main__":
    main()
