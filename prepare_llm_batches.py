#!/usr/bin/env python3
"""
PREPARE LLM TRANSLATION BATCHES
Creates batches of 50 items for quick translation via Claude/ChatGPT
Much faster than API calls - can translate 1500 items in minutes
"""

import json
import os

def create_llm_batches(input_file='translation_batch_input.json', batch_size=50):
    """Create batches for LLM translation"""

    if not os.path.exists(input_file):
        print(f"❌ Input file not found: {input_file}")
        return

    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    items = data['items']
    total = len(items)

    print("="*70)
    print("  LLM BATCH TRANSLATION PREPARATION")
    print("="*70)
    print(f"\n📊 Total items: {total}")
    print(f"   Batch size: {batch_size}")
    print(f"   Number of batches: {(total + batch_size - 1) // batch_size}")

    # Create batches
    batches = []

    for i in range(0, total, batch_size):
        batch = items[i:i+batch_size]
        batches.append(batch)

    # Create prompt for each batch
    os.makedirs('llm_batches', exist_ok=True)

    batch_files = []

    for batch_num, batch in enumerate(batches, 1):
        # Create JSON for this batch
        batch_data = {
            'batch_number': batch_num,
            'total_batches': len(batches),
            'items_in_batch': len(batch),
            'items': batch
        }

        batch_file = f'llm_batches/batch_{batch_num:03d}.json'

        with open(batch_file, 'w', encoding='utf-8') as f:
            json.dump(batch_data, f, indent=2, ensure_ascii=False)

        batch_files.append(batch_file)

        # Create prompt for LLM
        prompt = f"""Please translate the following {len(batch)} English phrases into these 9 languages:
- French (fr)
- Spanish (es)
- German (de)
- Portuguese (pt)
- Chinese (zh)
- Japanese (ja)
- Korean (ko)
- Arabic (ar)
- Hindi (hi)

Return ONLY a JSON object with this structure (no markdown, no explanation):
{{
  "fr": {{"key1": "translation1", "key2": "translation2", ...}},
  "es": {{"key1": "translation1", "key2": "translation2", ...}},
  "de": {{"key1": "translation1", "key2": "translation2", ...}},
  "pt": {{"key1": "translation1", "key2": "translation2", ...}},
  "zh": {{"key1": "translation1", "key2": "translation2", ...}},
  "ja": {{"key1": "translation1", "key2": "translation2", ...}},
  "ko": {{"key1": "translation1", "key2": "translation2", ...}},
  "ar": {{"key1": "translation1", "key2": "translation2", ...}},
  "hi": {{"key1": "translation1", "key2": "translation2", ...}}
}}

Here are the items to translate:

"""

        for item in batch:
            prompt += f'\n"{item["key"]}": "{item["text"]}"'

        prompt_file = f'llm_batches/prompt_{batch_num:03d}.txt'

        with open(prompt_file, 'w', encoding='utf-8') as f:
            f.write(prompt)

        print(f"\n✅ Batch {batch_num}/{len(batches)}: {len(batch)} items")
        print(f"   JSON: {batch_file}")
        print(f"   Prompt: {prompt_file}")

    # Create master instructions
    instructions = f"""
=============================================================================
LLM BATCH TRANSLATION INSTRUCTIONS
=============================================================================

You have {len(batches)} batches to translate.

QUICK METHOD (Recommended):
---------------------------
1. Open Claude/ChatGPT in your browser
2. For each batch (001 to {len(batches):03d}):
   a. Copy content from llm_batches/prompt_XXX.txt
   b. Paste into Claude/ChatGPT
   c. Copy the JSON response
   d. Save to llm_batches/result_XXX.json

3. When all batches are done, run:
   python3 merge_llm_translations.py

This will merge all results into final translation files.

ESTIMATED TIME:
--------------
- Per batch: ~30 seconds with Claude/ChatGPT
- Total time: ~{len(batches) * 0.5:.0f} minutes
- Much faster than API calls (2+ hours)!

TIPS:
-----
- Use Claude Sonnet 3.5 or ChatGPT-4 for best translation quality
- Copy-paste is faster than using API
- Can do batches in parallel if you have multiple LLM tabs open

=============================================================================
"""

    with open('llm_batches/INSTRUCTIONS.txt', 'w', encoding='utf-8') as f:
        f.write(instructions)

    print(f"\n{'='*70}")
    print("📦 BATCH PREPARATION COMPLETE!")
    print(f"{'='*70}")
    print(f"\n📁 Created {len(batches)} batches in llm_batches/ folder")
    print(f"\n📖 Read llm_batches/INSTRUCTIONS.txt for next steps")
    print(f"\n⏱️  Estimated translation time: {len(batches) * 0.5:.0f} minutes with LLM")
    print(f"{'='*70}")

if __name__ == "__main__":
    create_llm_batches()
