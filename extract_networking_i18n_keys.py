"""
Extract existing i18n keys from Networking HTML files
These files already have data-i18n attributes - extract them to create JSON files
"""
import json
import re

TOOLS = ['ansible', 'cisco-ai', 'datadog', 'juniper-mist', 'prtg', 'splunk', 'terraform', 'zabbix']

LANGUAGES = {
    'batch1': ['es', 'fr', 'de'],
    'batch2': ['pt', 'zh', 'ja'],
    'batch3': ['ko', 'ar', 'hi']
}

def extract_i18n_from_html(tool_name):
    """Extract all data-i18n keys and their English text from HTML"""
    print(f"\\n{'='*60}")
    print(f"Extracting from {tool_name.upper()}")
    print(f"{'='*60}")

    html_path = f"GenuisNet.ai/pages/reviews/networking/{tool_name}.html"

    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Pattern to find data-i18n with content
    pattern = r'<span data-i18n="([^"]+)">([^<]+)</span>'
    matches = re.findall(pattern, html)

    content_data = {}
    faq_data = {}

    for key, text in matches:
        # Clean up text
        text = re.sub(r'\\s+', ' ', text).strip()

        if not text or len(text) < 2:
            continue

        # Separate FAQ keys from content keys
        if '.faq.' in key:
            faq_data[key] = text
        else:
            content_data[key] = text

    print(f"  Content keys: {len(content_data)}")
    print(f"  FAQ keys: {len(faq_data)}")

    # Save English content file
    content_path = f"GenuisNet.ai/pages/reviews/networking/{tool_name}-en.json"
    with open(content_path, 'w', encoding='utf-8') as f:
        json.dump(content_data, f, indent=2, ensure_ascii=False)
    print(f"  Created: {tool_name}-en.json")

    # Save English FAQ file
    faq_path = f"GenuisNet.ai/pages/reviews/networking/{tool_name}-faqs-en.json"
    with open(faq_path, 'w', encoding='utf-8') as f:
        json.dump(faq_data, f, indent=2, ensure_ascii=False)
    print(f"  Created: {tool_name}-faqs-en.json")

    # Create batch files for content
    for batch_name, langs in LANGUAGES.items():
        batch_data = {}
        for lang in langs:
            batch_data[lang] = content_data

        batch_path = f"GenuisNet.ai/pages/reviews/networking/{tool_name}-batch{batch_name[-1]}.json"
        with open(batch_path, 'w', encoding='utf-8') as f:
            json.dump(batch_data, f, indent=2, ensure_ascii=False)

    # Create batch files for FAQs
    if faq_data:
        for batch_name, langs in LANGUAGES.items():
            batch_data = {}
            for lang in langs:
                batch_data[lang] = faq_data

            batch_path = f"GenuisNet.ai/pages/reviews/networking/{tool_name}-faqs-batch{batch_name[-1]}.json"
            with open(batch_path, 'w', encoding='utf-8') as f:
                json.dump(batch_data, f, indent=2, ensure_ascii=False)

    return len(content_data), len(faq_data)

# Process all tools
print("\\n" + "="*60)
print("EXTRACTING I18N KEYS FROM NETWORKING TOOLS")
print("="*60)

total_content = 0
total_faq = 0

for tool in TOOLS:
    try:
        content, faq = extract_i18n_from_html(tool)
        total_content += content
        total_faq += faq
    except Exception as e:
        print(f"  [ERROR] {tool}: {str(e)}")
        import traceback
        traceback.print_exc()

total_keys = total_content + total_faq

print("\\n" + "="*60)
print("EXTRACTION COMPLETE")
print("="*60)
print(f"\\nTotal content keys: {total_content}")
print(f"Total FAQ keys: {total_faq}")
print(f"Total keys: {total_keys}")
print(f"\\nReady for {total_keys * 9} translations across 9 languages!")
print(f"\\n48 translation agents ready to launch (6 per tool)")
