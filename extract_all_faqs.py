"""
Extract ALL FAQs from business tools and create proper FAQ files
"""
import json
import os
import re

TOOLS = ['chorusai', 'conversica', 'drift', 'gong', 'hubspot-ai', 'looker', 'salesforce-einstein', 'tableau']
LANGUAGES = {
    'batch1': ['es', 'fr', 'de'],
    'batch2': ['pt', 'zh', 'ja'],
    'batch3': ['ko', 'ar', 'hi']
}

def extract_faqs_from_html(tool_name):
    """Extract ALL FAQ questions and answers from HTML"""
    html_path = f"GenuisNet.ai/pages/reviews/business/{tool_name}.html"

    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find all FAQ items using regex
    faq_pattern = r'<div class="faq-item">.*?<div class="faq-question">\s*(.*?)\s*<span>\+</span>.*?</div>.*?<div class="faq-answer">\s*(.*?)\s*</div>'
    matches = re.findall(faq_pattern, html, re.DOTALL)

    faqs = {}
    for i, (question, answer) in enumerate(matches, 1):
        # Clean up whitespace and HTML
        question = re.sub(r'\s+', ' ', question).strip()
        answer = re.sub(r'\s+', ' ', answer).strip()

        faqs[f"review.{tool_name}.faq.q{i}"] = question
        faqs[f"review.{tool_name}.faq.a{i}"] = answer

    return faqs

# Process all tools
print("\n" + "="*60)
print("EXTRACTING ALL FAQS FROM AI BUSINESS TOOLS")
print("="*60)

for tool in TOOLS:
    print(f"\nProcessing {tool}...")

    faqs = extract_faqs_from_html(tool)
    num_faqs = len(faqs) // 2  # Divide by 2 because we have Q+A

    print(f"  Found {num_faqs} FAQs ({len(faqs)} total keys)")

    # Create English FAQ file
    en_faq_path = f"GenuisNet.ai/pages/reviews/business/{tool}-faqs-en.json"
    with open(en_faq_path, 'w', encoding='utf-8') as f:
        json.dump(faqs, f, indent=2, ensure_ascii=False)
    print(f"  Created: {tool}-faqs-en.json")

    # Create batch files
    for batch_name, langs in LANGUAGES.items():
        batch_data = {}
        for lang in langs:
            batch_data[lang] = faqs

        batch_path = f"GenuisNet.ai/pages/reviews/business/{tool}-faqs-{batch_name}.json"
        with open(batch_path, 'w', encoding='utf-8') as f:
            json.dump(batch_data, f, indent=2, ensure_ascii=False)
        print(f"  Created: {tool}-faqs-{batch_name}.json")

print("\n" + "="*60)
print("DONE! All FAQ files recreated successfully")
print("="*60)
