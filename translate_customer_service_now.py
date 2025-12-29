#!/usr/bin/env python3
"""
Translate customer-service tools using Claude API directly
Fast real-time translation for immediate deployment
"""

import json
import os
import sys
from pathlib import Path
import anthropic

# Base paths
BASE_DIR = Path(r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai")
PAGES_DIR = BASE_DIR / "pages" / "reviews" / "customer-service"

# Tools that need translation
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
    1: {"de": "German", "es": "Spanish", "fr": "French"},
    2: {"pt": "Portuguese", "zh": "Chinese", "ja": "Japanese"},
    3: {"ko": "Korean", "ar": "Arabic", "hi": "Hindi"}
}

def translate_batch(client, tool_name, batch_num, en_content):
    """Translate content for one batch using Claude API"""

    langs = BATCHES[batch_num]
    lang_list = ", ".join([f"{name} ({code})" for code, name in langs.items()])

    prompt = f"""Translate the following JSON content into {lang_list}.

Return ONLY a valid JSON object (no markdown, no code blocks) where the top-level keys are language codes ({', '.join(langs.keys())}), and each contains all the translated key-value pairs.

CRITICAL REQUIREMENTS:
- Maintain the exact same keys, only translate the values
- Translate EVERY value completely - no English should remain
- Professional, accurate translations appropriate for a customer service AI platform review
- Keep proper nouns like "{tool_name.replace('-', ' ').title()}", "API", "SSO", "GDPR", "HIPAA", "SLA" untranslated
- Ensure grammatically correct, natural-sounding translations
- Return ONLY the JSON object, nothing else

JSON to translate:
{json.dumps(en_content, indent=2, ensure_ascii=False)}"""

    try:
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=16000,
            messages=[{"role": "user", "content": prompt}]
        )

        response_text = message.content[0].text.strip()

        # Remove markdown code blocks if present
        if response_text.startswith('```'):
            lines = response_text.split('\n')
            response_text = '\n'.join(lines[1:-1] if lines[-1].strip() == '```' else lines[1:])
            if response_text.startswith('json'):
                response_text = response_text[4:].strip()

        translations = json.loads(response_text)
        return translations

    except Exception as e:
        print(f"Error translating {tool_name} batch{batch_num}: {e}")
        return None

def main():
    # Get API key from environment
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY environment variable not set")
        print("Set it with: set ANTHROPIC_API_KEY=your-key-here")
        return

    client = anthropic.Anthropic(api_key=api_key)

    print("="*70)
    print("Translating Customer Service Tools - Real-Time")
    print("="*70)
    print()

    total_success = 0
    total_failed = 0

    for tool in TOOLS:
        print(f"\nTranslating {tool}...")

        # Load English source
        en_file = PAGES_DIR / f"{tool}-en.json"
        with open(en_file, 'r', encoding='utf-8') as f:
            en_content = json.load(f)

        # Translate each batch
        for batch_num in [1, 2, 3]:
            print(f"  Batch {batch_num} ({', '.join(BATCHES[batch_num].keys())})...", end=" ")

            translations = translate_batch(client, tool, batch_num, en_content)

            if translations:
                # Save batch file
                batch_file = PAGES_DIR / f"{tool}-batch{batch_num}.json"
                with open(batch_file, 'w', encoding='utf-8') as f:
                    json.dump(translations, f, indent=2, ensure_ascii=False)
                print("DONE")
                total_success += 1
            else:
                print("FAILED")
                total_failed += 1

    print()
    print("="*70)
    print(f"Translation Complete: {total_success} successful, {total_failed} failed")
    print("="*70)
    print()
    print("Next step: Run python generate_customer_service_i18n.py")

if __name__ == "__main__":
    main()
