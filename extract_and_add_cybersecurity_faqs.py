"""
Extract FAQs from Cybersecurity HTML files and add data-i18n attributes
"""
import re
import json
import os

TOOLS = [
    'abnormal-security', 'carbon-black', 'cisco-securex', 'cortex-xdr',
    'crowdstrike', 'cyberark', 'cybereason', 'cylance', 'darktrace',
    'exabeam', 'fortinet', 'ibm-qradar', 'lacework', 'mcafee-mvision',
    'microsoft-sentinel', 'okta', 'palo-alto-ngfw', 'qualys', 'rapid7',
    'recorded-future', 'sentinelone', 'snyk', 'sophos-interceptx',
    'splunk-security', 'symantec-endpoint', 'tenable',
    'trend-micro-vision-one', 'vectra-ai', 'wiz', 'zerofox'
]

def extract_and_add_faqs(tool_name):
    """Extract FAQs and add data-i18n attributes to HTML"""
    html_path = f"GenuisNet.ai/pages/reviews/cybersecurity/{tool_name}.html"

    if not os.path.exists(html_path):
        return None

    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Check if FAQ section exists
    if 'id="faq"' not in html:
        return None

    # Pattern to find FAQ items (h4 question + p answer)
    # Looking for: <h4>Question?</h4> followed by <p>Answer</p>
    faq_pattern = r'<div class="feature-card"[^>]*>\s*<h4>([^<]+)</h4>\s*<p>([^<]+)</p>\s*</div>'
    matches = re.findall(faq_pattern, html, re.DOTALL)

    if not matches:
        return None

    faq_data = {}
    modified_html = html

    for i, (question, answer) in enumerate(matches, 1):
        # Clean up whitespace
        question = re.sub(r'\s+', ' ', question).strip()
        answer = re.sub(r'\s+', ' ', answer).strip()

        # Create keys
        q_key = f"review.{tool_name}.faq.q{i}"
        a_key = f"review.{tool_name}.faq.a{i}"

        faq_data[q_key] = question
        faq_data[a_key] = answer

        # Replace in HTML with data-i18n attributes
        old_pattern = f'<h4>{re.escape(question)}</h4>'
        new_h4 = f'<h4><span data-i18n="{q_key}">{question}</span></h4>'
        modified_html = modified_html.replace(old_pattern, new_h4, 1)

        old_p_pattern = f'<p>{re.escape(answer)}</p>'
        new_p = f'<p><span data-i18n="{a_key}">{answer}</span></p>'
        modified_html = modified_html.replace(old_p_pattern, new_p, 1)

    # Save modified HTML
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(modified_html)

    # Save FAQ English file
    if faq_data:
        en_faq_file = f"GenuisNet.ai/pages/reviews/cybersecurity/{tool_name}-faqs-en.json"
        with open(en_faq_file, 'w', encoding='utf-8') as f:
            json.dump(faq_data, f, ensure_ascii=False, indent=2)

        # Create 3 FAQ batch files
        for batch_num in range(1, 4):
            batch_file = f"GenuisNet.ai/pages/reviews/cybersecurity/{tool_name}-faqs-batch{batch_num}.json"
            batch_data = {"en": faq_data}
            with open(batch_file, 'w', encoding='utf-8') as f:
                json.dump(batch_data, f, ensure_ascii=False, indent=2)

    return faq_data

# Main extraction
print("\n" + "="*60)
print("CYBERSECURITY FAQs - EXTRACTION & INTEGRATION")
print("="*60)

total_faq_keys = 0
tools_with_faqs = []

for tool in TOOLS:
    faq_data = extract_and_add_faqs(tool)

    if faq_data:
        faq_count = len(faq_data)
        print(f"{tool}: {faq_count} FAQ keys extracted and integrated")
        total_faq_keys += faq_count
        tools_with_faqs.append(tool)
    else:
        print(f"{tool}: No FAQs found")

print("\n" + "="*60)
print("FAQ EXTRACTION SUMMARY")
print("="*60)
print(f"Total tools with FAQs: {len(tools_with_faqs)}")
print(f"Total FAQ keys: {total_faq_keys}")
print(f"FAQ files created: {len(tools_with_faqs) * 4} (EN + 3 batches per tool)")

if tools_with_faqs:
    print(f"\nTools with FAQs:")
    for tool in tools_with_faqs:
        print(f"  - {tool}")

print("\n" + "="*60)
print("HTML files updated with data-i18n attributes!")
print("="*60)
