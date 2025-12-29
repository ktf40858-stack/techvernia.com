#!/usr/bin/env python3
"""
Create Claude Batch API files for translating customer-service tools
This script generates proper Batch API format requests for translation
"""

import json
import os
from pathlib import Path

# Base paths
BASE_DIR = Path(r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai")
PAGES_DIR = BASE_DIR / "pages" / "reviews" / "customer-service"

# Tools that need complete translation
TOOLS = [
    "intercom-fin",
    "kustomer",
    "liveperson",
    "netomi",
    "ultimateai",
    "yellowai",
    "zendesk-ai"
]

# Language batches
BATCHES = {
    1: ["de", "es", "fr"],
    2: ["pt", "zh", "ja"],
    3: ["ko", "ar", "hi"]
}

LANG_NAMES = {
    "de": "German",
    "es": "Spanish",
    "fr": "French",
    "pt": "Portuguese",
    "zh": "Chinese",
    "ja": "Japanese",
    "ko": "Korean",
    "ar": "Arabic",
    "hi": "Hindi"
}

def create_batch_request(tool_name, batch_num, en_content):
    """Create a Batch API request for translation"""

    langs = BATCHES[batch_num]
    lang_list = ", ".join([f"{LANG_NAMES[l]} ({l})" for l in langs])

    prompt = f"""Translate the following JSON content into {lang_list}.

Return a JSON object where the top-level keys are language codes ({', '.join(langs)}), and each contains all the translated key-value pairs.

CRITICAL REQUIREMENTS:
- Maintain the exact same keys, only translate the values
- Translate EVERY value completely - no English should remain
- Professional, accurate translations appropriate for a customer service AI platform review
- Keep proper nouns like "{tool_name.replace('-', ' ').title()}", "API", "SSO", "GDPR", "HIPAA" untranslated
- Ensure grammatically correct, natural-sounding translations

JSON to translate:
{json.dumps(en_content, indent=2, ensure_ascii=False)}"""

    request = {
        "custom_id": f"{tool_name}-batch{batch_num}",
        "method": "POST",
        "url": "/v1/messages",
        "body": {
            "model": "claude-3-5-sonnet-20241022",
            "max_tokens": 16000,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
    }

    return request

def main():
    print("="*70)
    print("Creating Claude Batch API Translation Requests")
    print("="*70)
    print()

    all_requests = []

    for tool in TOOLS:
        print(f"Processing {tool}...")

        # Load English source
        en_file = PAGES_DIR / f"{tool}-en.json"
        with open(en_file, 'r', encoding='utf-8') as f:
            en_content = json.load(f)

        # Create 3 batch requests
        for batch_num in [1, 2, 3]:
            request = create_batch_request(tool, batch_num, en_content)
            all_requests.append(request)
            print(f"  Created batch{batch_num} request ({', '.join(BATCHES[batch_num])})")

    # Save all requests to a single JSONL file
    output_file = Path("customer-service-translations-batch-api.jsonl")
    with open(output_file, 'w', encoding='utf-8') as f:
        for request in all_requests:
            f.write(json.dumps(request, ensure_ascii=False) + '\n')

    print()
    print("="*70)
    print(f"Created {len(all_requests)} batch API requests")
    print(f"Saved to: {output_file}")
    print("="*70)
    print()
    print("Next steps:")
    print("1. Upload customer-service-translations-batch-api.jsonl to Claude Batch API")
    print("2. Wait for translations to complete")
    print("3. Download results and extract to batch files")
    print("4. Run: python generate_customer_service_i18n.py")

if __name__ == "__main__":
    main()
