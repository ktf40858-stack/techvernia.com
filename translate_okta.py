import json
import anthropic

# Read the English content
with open(r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\pages\reviews\cybersecurity\okta-batch3.json", "r", encoding="utf-8") as f:
    data = json.load(f)

en_content = data["en"]

# Initialize Anthropic client
client = anthropic.Anthropic()

# Languages to translate to
languages = {
    "ko": "Korean",
    "ar": "Arabic",
    "hi": "Hindi"
}

translations = {"en": en_content}

for lang_code, lang_name in languages.items():
    print(f"Translating to {lang_name}...")

    prompt = f"""Translate the following English text to {lang_name}.
Keep the JSON keys exactly the same, only translate the values.
Return ONLY valid JSON without any markdown or extra text.

English content:
{json.dumps(en_content, ensure_ascii=False, indent=2)}

Return the translated version as valid JSON with the same keys."""

    message = client.messages.create(
        model="claude-opus-4-5-20251101",
        max_tokens=4000,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    response_text = message.content[0].text
    # Clean up the response if it contains markdown code blocks
    if "```json" in response_text:
        response_text = response_text.split("```json")[1].split("```")[0].strip()
    elif "```" in response_text:
        response_text = response_text.split("```")[1].split("```")[0].strip()

    translated_dict = json.loads(response_text)
    translations[lang_code] = translated_dict
    print(f"  Completed {lang_name}")

# Save back to file
output_path = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\pages\reviews\cybersecurity\okta-batch3.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(translations, f, ensure_ascii=False, indent=2)

print(f"\nTranslations saved to okta-batch3.json")
