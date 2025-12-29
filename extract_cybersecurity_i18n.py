"""
Extract i18n keys from Cybersecurity category HTML files
Creates English source files and translation batch files
"""
import re
import json
import os

# All 30 Cybersecurity tools
TOOLS = [
    'abnormal-security', 'carbon-black', 'cisco-securex', 'cortex-xdr',
    'crowdstrike', 'cyberark', 'cybereason', 'cylance', 'darktrace',
    'exabeam', 'fortinet', 'ibm-qradar', 'lacework', 'mcafee-mvision',
    'microsoft-sentinel', 'okta', 'palo-alto-ngfw', 'qualys', 'rapid7',
    'recorded-future', 'sentinelone', 'snyk', 'sophos-interceptx',
    'splunk-security', 'symantec-endpoint', 'tenable',
    'trend-micro-vision-one', 'vectra-ai', 'wiz', 'zerofox'
]

def extract_i18n_from_html(tool_name):
    """Extract data-i18n keys and content from HTML file"""
    html_path = f"GenuisNet.ai/pages/reviews/cybersecurity/{tool_name}.html"

    if not os.path.exists(html_path):
        print(f"  [SKIP] {tool_name}: File not found")
        return None, None

    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Pattern to find data-i18n with content
    pattern = r'<span data-i18n="([^"]+)">([^<]+)</span>'
    matches = re.findall(pattern, html)

    content_data = {}
    faq_data = {}

    for key, text in matches:
        # Clean up text
        text = re.sub(r'\s+', ' ', text).strip()

        # Skip empty or very short content
        if len(text) < 2:
            continue

        # Separate FAQ from content
        if '.faq.' in key:
            faq_data[key] = text
        else:
            content_data[key] = text

    return content_data, faq_data

def create_batch_files(tool_name, content_data, faq_data):
    """Create English source files and empty batch files for translation"""

    # Create English content file
    if content_data:
        en_file = f"GenuisNet.ai/pages/reviews/cybersecurity/{tool_name}-en.json"
        with open(en_file, 'w', encoding='utf-8') as f:
            json.dump(content_data, f, ensure_ascii=False, indent=2)

        # Create 3 batch files for content (ES/FR/DE, PT/ZH/JA, KO/AR/HI)
        for batch_num in range(1, 4):
            batch_file = f"GenuisNet.ai/pages/reviews/cybersecurity/{tool_name}-batch{batch_num}.json"

            # Create structure with English as placeholder
            batch_data = {
                "en": content_data
            }

            with open(batch_file, 'w', encoding='utf-8') as f:
                json.dump(batch_data, f, ensure_ascii=False, indent=2)

    # Create English FAQ file if FAQs exist
    if faq_data:
        en_faq_file = f"GenuisNet.ai/pages/reviews/cybersecurity/{tool_name}-faqs-en.json"
        with open(en_faq_file, 'w', encoding='utf-8') as f:
            json.dump(faq_data, f, ensure_ascii=False, indent=2)

        # Create 3 batch files for FAQs
        for batch_num in range(1, 4):
            batch_file = f"GenuisNet.ai/pages/reviews/cybersecurity/{tool_name}-faqs-batch{batch_num}.json"

            batch_data = {
                "en": faq_data
            }

            with open(batch_file, 'w', encoding='utf-8') as f:
                json.dump(batch_data, f, ensure_ascii=False, indent=2)

# Main extraction
print("\n" + "="*60)
print("CYBERSECURITY CATEGORY - I18N EXTRACTION")
print("="*60)

total_content_keys = 0
total_faq_keys = 0
tools_with_faqs = []

for tool in TOOLS:
    print(f"\n{tool}:")

    content_data, faq_data = extract_i18n_from_html(tool)

    if content_data is None:
        continue

    content_count = len(content_data)
    faq_count = len(faq_data)

    print(f"  Content keys: {content_count}")
    print(f"  FAQ keys: {faq_count}")

    total_content_keys += content_count
    total_faq_keys += faq_count

    if faq_count > 0:
        tools_with_faqs.append(tool)

    # Create batch files
    create_batch_files(tool, content_data, faq_data)
    print(f"  [OK] Created English files + 3 batch files")

print("\n" + "="*60)
print("EXTRACTION SUMMARY")
print("="*60)
print(f"Total tools: {len(TOOLS)}")
print(f"Total content keys: {total_content_keys}")
print(f"Total FAQ keys: {total_faq_keys}")
print(f"Total keys: {total_content_keys + total_faq_keys}")
print(f"\nTools with FAQs: {len(tools_with_faqs)}")
if tools_with_faqs:
    print(f"  {', '.join(tools_with_faqs)}")

print(f"\nFiles created:")
print(f"  - {len(TOOLS)} English content files")
print(f"  - {len(tools_with_faqs)} English FAQ files")
print(f"  - {len(TOOLS) * 3} content batch files")
print(f"  - {len(tools_with_faqs) * 3} FAQ batch files")
print(f"  - Total: {len(TOOLS) * 4 + len(tools_with_faqs) * 4} files")

print("\n" + "="*60)
print("Ready for translation!")
print("="*60)
