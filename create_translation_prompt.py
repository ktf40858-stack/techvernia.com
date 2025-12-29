#!/usr/bin/env python3
"""Create translation prompts for Conversica batch3."""

import json

# Load the file
with open(r'C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\pages\reviews\business\conversica-batch3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Get English content
english = data['ko']

# Create a translation prompt file
prompt = """I need you to translate the following 126 English content strings to three languages: Korean (KO), Arabic (AR), and Hindi (HI).

For each language, provide the translations in JSON format with the same keys.

Here are all the English content strings to translate:

"""

# Add all English strings
for key, value in english.items():
    prompt += f'{key}: {value}\n'

prompt += """

Please provide the complete translations in this JSON format for all three languages:

{
  "ko": {
    "review.conversica.content.1": "[Korean translation]",
    ...
  },
  "ar": {
    "review.conversica.content.1": "[Arabic translation]",
    ...
  },
  "hi": {
    "review.conversica.content.1": "[Hindi translation]",
    ...
  }
}

Make sure all 126 keys are translated in each language. Keep the key names exactly the same."""

# Save the prompt
with open(r'C:\Users\Freddy\Desktop\GeniusNet.ai\translation_prompt.txt', 'w', encoding='utf-8') as f:
    f.write(prompt)

print("Translation prompt created successfully!")
print(f"Total strings to translate: {len(english)}")
