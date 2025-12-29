"""
Extract FAQs from Networking HTML files and add data-i18n attributes
"""
import json
import re

TOOLS = ['ansible', 'cisco-ai', 'datadog', 'juniper-mist', 'prtg', 'splunk', 'terraform', 'zabbix']

LANGUAGES = {
    'batch1': ['es', 'fr', 'de'],
    'batch2': ['pt', 'zh', 'ja'],
    'batch3': ['ko', 'ar', 'hi']
}

def extract_and_add_faqs(tool_name):
    """Extract FAQs and add data-i18n attributes to HTML"""
    print(f"\n{'='*60}")
    print(f"Processing FAQs for {tool_name.upper()}")
    print(f"{'='*60}")

    html_path = f"GenuisNet.ai/pages/reviews/networking/{tool_name}.html"

    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Pattern to find FAQ items
    faq_pattern = r'<div class="faq-item"><div class="faq-question">([^<]+)</div><div class="faq-answer">([^<]+)</div></div>'
    matches = re.findall(faq_pattern, html, re.DOTALL)

    if not matches:
        print(f"  No FAQs found")
        return 0

    faq_data = {}

    # Extract FAQs and add to JSON
    for i, (question, answer) in enumerate(matches, 1):
        # Clean up
        question = re.sub(r'\s+', ' ', question).strip()
        answer = re.sub(r'\s+', ' ', answer).strip()

        q_key = f"review.{tool_name}.faq.q{i}"
        a_key = f"review.{tool_name}.faq.a{i}"

        faq_data[q_key] = question
        faq_data[a_key] = answer

        # Replace in HTML with data-i18n attributes
        old_faq = f'<div class="faq-item"><div class="faq-question">{question}</div><div class="faq-answer">{answer}</div></div>'
        new_faq = f'<div class="faq-item"><div class="faq-question"><span data-i18n="{q_key}">{question}</span> <span>+</span></div><div class="faq-answer"><span data-i18n="{a_key}">{answer}</span></div></div>'

        html = html.replace(old_faq, new_faq, 1)

    print(f"  Found {len(matches)} FAQ pairs")

    # Update existing faqs-en.json or create new one
    faq_json_path = f"GenuisNet.ai/pages/reviews/networking/{tool_name}-faqs-en.json"

    # Check if file exists and merge
    try:
        with open(faq_json_path, 'r', encoding='utf-8') as f:
            existing_faqs = json.load(f)
            existing_faqs.update(faq_data)
            faq_data = existing_faqs
    except:
        pass

    # Save FAQ JSON
    with open(faq_json_path, 'w', encoding='utf-8') as f:
        json.dump(faq_data, f, indent=2, ensure_ascii=False)
    print(f"  Updated: {tool_name}-faqs-en.json")

    # Create batch files for FAQs
    for batch_name, langs in LANGUAGES.items():
        batch_data = {}
        for lang in langs:
            batch_data[lang] = faq_data

        batch_path = f"GenuisNet.ai/pages/reviews/networking/{tool_name}-faqs-batch{batch_name[-1]}.json"
        with open(batch_path, 'w', encoding='utf-8') as f:
            json.dump(batch_data, f, indent=2, ensure_ascii=False)

    # Save updated HTML
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  Updated HTML with data-i18n attributes")

    return len(faq_data)

# Process all tools
print("\n" + "="*60)
print("EXTRACTING AND ADDING FAQ DATA-I18N ATTRIBUTES")
print("="*60)

total_faq_keys = 0

for tool in TOOLS:
    try:
        faq_count = extract_and_add_faqs(tool)
        total_faq_keys += faq_count
    except Exception as e:
        print(f"  [ERROR] {tool}: {str(e)}")
        import traceback
        traceback.print_exc()

print("\n" + "="*60)
print("FAQ EXTRACTION COMPLETE")
print("="*60)
print(f"\nTotal FAQ keys added: {total_faq_keys}")
print(f"FAQ translations needed: {total_faq_keys * 9}")
