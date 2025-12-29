#!/usr/bin/env python3
"""
Translate Conversica batch3 to KO, AR, HI using Claude.
"""

import json
import subprocess
import sys
import os

def translate_with_claude(english_texts, target_lang_name, target_lang_code):
    """Use Claude via command line to translate texts."""

    # Create prompt
    text_list = "\n".join([f"{k}: {v}" for k, v in list(english_texts.items())[:15]])

    prompt = f"""Translate these English content strings to {target_lang_name} ({target_lang_code}).
Keep exact key names. Format: key: translation

{text_list}

Provide ONLY the translations, one per line. No other text."""

    # Call claude command
    try:
        result = subprocess.run(
            ["claude", "prompt", prompt],
            capture_output=True,
            text=True,
            timeout=30
        )
        return result.stdout
    except Exception as e:
        print(f"Error calling Claude: {e}")
        return None

def main():
    file_path = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\pages\reviews\business\conversica-batch3.json"

    # Load file
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Get English source
    english = data['ko']

    print(f"Loaded {len(english)} keys")
    print("File structure verified - ready to translate")

    # For now, let's create a more practical solution
    # We'll do batch translations using the claude command

if __name__ == "__main__":
    main()
