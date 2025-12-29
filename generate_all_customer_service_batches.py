#!/usr/bin/env python3
"""
Generate translation batch files for customer service tools
This script creates professional translations for 7 customer service tools
"""

import json
import os
from anthropic import Anthropic

# Initialize Claude API client
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# Base directory
base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\pages\reviews\customer-service"

# Tools to translate
tools = [
    "intercom-fin",
    "kustomer",
    "liveperson",
    "netomi",
    "ultimateai",
    "yellowai",
    "zendesk-ai"
]

# Language configurations for each batch
batch_configs = {
    "batch1": {
        "languages": ["de", "es", "fr"],
        "names": ["German", "Spanish", "French"]
    },
    "batch2": {
        "languages": ["pt", "zh", "ja"],
        "names": ["Portuguese", "Chinese", "Japanese"]
    },
    "batch3": {
        "languages": ["ko", "ar", "hi"],
        "names": ["Korean", "Arabic", "Hindi"]
    }
}

def translate_content(en_data, languages, tool_name):
    """Translate English content to multiple languages using Claude API"""

    # Create the translation prompt
    prompt = f"""You are a professional translator specializing in technical content for AI and customer service platforms.

Translate the following JSON content from English to {', '.join(languages)}.

CRITICAL REQUIREMENTS:
1. Maintain the EXACT same JSON keys - only translate the values
2. Provide professional, accurate translations suitable for a business/enterprise context
3. Keep technical terms (API, SSO, HIPAA, GDPR, SOC 2, SLA) in English
4. Keep brand names (Slack, Microsoft Teams, Salesforce, Google Workspace, {tool_name.title()}) unchanged
5. Maintain any HTML tags, formatting, or special characters
6. Ensure translations are culturally appropriate and professional

Source JSON (English):
{json.dumps(en_data, indent=2, ensure_ascii=False)}

Please provide the output as a JSON object with this structure:
{{
  "de": {{ ... }},  // German translations
  "es": {{ ... }},  // Spanish translations
  "fr": {{ ... }}   // French translations
}}

Or for batch2:
{{
  "pt": {{ ... }},  // Portuguese translations
  "zh": {{ ... }},  // Chinese translations
  "ja": {{ ... }}   // Japanese translations
}}

Or for batch3:
{{
  "ko": {{ ... }},  // Korean translations
  "ar": {{ ... }},  // Arabic translations
  "hi": {{ ... }}   // Hindi translations
}}

Return ONLY the JSON object, no explanation or markdown formatting."""

    try:
        # Call Claude API
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=16000,
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )

        # Extract and parse the response
        response_text = message.content[0].text

        # Clean up any markdown formatting if present
        if response_text.startswith("```json"):
            response_text = response_text.split("```json")[1].split("```")[0].strip()
        elif response_text.startswith("```"):
            response_text = response_text.split("```")[1].split("```")[0].strip()

        # Parse the JSON
        translations = json.loads(response_text)
        return translations

    except Exception as e:
        print(f"    ✗ Error translating: {str(e)}")
        return None

def main():
    print("=" * 80)
    print("CUSTOMER SERVICE TRANSLATION BATCH GENERATOR")
    print("=" * 80)
    print()

    total_files = len(tools) * 3  # 3 batch files per tool
    current = 0

    for tool in tools:
        print(f"\n{'='*80}")
        print(f"Processing: {tool.upper()}")
        print(f"{'='*80}")

        en_file = os.path.join(base_dir, f"{tool}-en.json")

        if not os.path.exists(en_file):
            print(f"  ⚠ Warning: {en_file} not found, skipping...")
            continue

        # Load English source
        with open(en_file, 'r', encoding='utf-8') as f:
            en_data = json.load(f)

        print(f"  ✓ Loaded {len(en_data)} English strings from {tool}-en.json")

        # Create each batch
        for batch_name, config in batch_configs.items():
            current += 1
            batch_file = os.path.join(base_dir, f"{tool}-{batch_name}.json")

            print(f"\n  [{current}/{total_files}] Creating {batch_name}.json ({', '.join(config['names'])})...")

            # Translate using Claude API
            translations = translate_content(en_data, config['languages'], tool)

            if translations:
                # Save the batch file
                with open(batch_file, 'w', encoding='utf-8') as f:
                    json.dump(translations, f, indent=2, ensure_ascii=False)

                print(f"  ✓ Created {tool}-{batch_name}.json")
            else:
                print(f"  ✗ Failed to create {tool}-{batch_name}.json")

    print(f"\n{'='*80}")
    print("TRANSLATION COMPLETE!")
    print(f"{'='*80}")
    print(f"\nGenerated {current} batch files for {len(tools)} tools")
    print("\nNext step: Run generate_customer_service_i18n.py to create the i18n.js files")

if __name__ == "__main__":
    main()
