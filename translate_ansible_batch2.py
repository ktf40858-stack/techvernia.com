#!/usr/bin/env python3
import json
from anthropic import Anthropic

client = Anthropic()

# Read the JSON file
with open(r"GenuisNet.ai\pages\reviews\networking\ansible-batch2.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Extract English text from the "pt" section (which currently contains English)
english_texts = data["pt"]

# Translation batches
pt_translations = {}
zh_translations = {}
ja_translations = {}

# Group texts into batches for efficient translation
keys_list = list(english_texts.keys())
batch_size = 10

print("Starting translations...")

for i in range(0, len(keys_list), batch_size):
    batch_keys = keys_list[i:i+batch_size]
    batch_texts = {key: english_texts[key] for key in batch_keys}

    # Create prompt for translation
    text_list = "\n".join([f"{k}: {v}" for k, v in batch_texts.items()])

    print(f"\nTranslating batch {i//batch_size + 1}/{(len(keys_list)-1)//batch_size + 1}...")

    # Portuguese Translation
    pt_response = client.messages.create(
        model="claude-opus-4-5-20251101",
        max_tokens=2000,
        messages=[{
            "role": "user",
            "content": f"""Translate the following English text to Portuguese (pt).
Preserve all technical terms (like Ansible, Red Hat, SSH, WinRM, YAML, RBAC, etc.) and keep the same format.
Return ONLY a JSON object with the same keys and translated values.

{text_list}"""
        }]
    )

    # Chinese (Simplified) Translation
    zh_response = client.messages.create(
        model="claude-opus-4-5-20251101",
        max_tokens=2000,
        messages=[{
            "role": "user",
            "content": f"""Translate the following English text to Simplified Chinese (zh).
Preserve all technical terms (like Ansible, Red Hat, SSH, WinRM, YAML, RBAC, etc.) and keep the same format.
Return ONLY a JSON object with the same keys and translated values.

{text_list}"""
        }]
    )

    # Japanese Translation
    ja_response = client.messages.create(
        model="claude-opus-4-5-20251101",
        max_tokens=2000,
        messages=[{
            "role": "user",
            "content": f"""Translate the following English text to Japanese (ja).
Preserve all technical terms (like Ansible, Red Hat, SSH, WinRM, YAML, RBAC, etc.) and keep the same format.
Return ONLY a JSON object with the same keys and translated values.

{text_list}"""
        }]
    )

    # Parse responses
    try:
        pt_batch = json.loads(pt_response.content[0].text)
        pt_translations.update(pt_batch)
    except:
        print("Error parsing Portuguese translation, retrying...")
        pass

    try:
        zh_batch = json.loads(zh_response.content[0].text)
        zh_translations.update(zh_batch)
    except:
        print("Error parsing Chinese translation, retrying...")
        pass

    try:
        ja_batch = json.loads(ja_response.content[0].text)
        ja_translations.update(ja_batch)
    except:
        print("Error parsing Japanese translation, retrying...")
        pass

# Update the data structure with translations
data["pt"] = pt_translations
data["zh"] = zh_translations
data["ja"] = ja_translations

# Write back to file
with open(r"GenuisNet.ai\pages\reviews\networking\ansible-batch2.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\nTranslation complete! File updated.")
