"""
Automated extraction of content and FAQs from Networking category tools
Creates English source files and batch files for translation
"""
import json
import re
from html.parser import HTMLParser

TOOLS = ['ansible', 'cisco-ai', 'datadog', 'juniper-mist', 'prtg', 'splunk', 'terraform', 'zabbix']

LANGUAGES = {
    'batch1': ['es', 'fr', 'de'],
    'batch2': ['pt', 'zh', 'ja'],
    'batch3': ['ko', 'ar', 'hi']
}

class ContentExtractor(HTMLParser):
    """Extract content from HTML for i18n"""

    def __init__(self, tool_name):
        super().__init__()
        self.tool_name = tool_name
        self.in_article = False
        self.in_faq = False
        self.current_tag = None
        self.current_data = []
        self.content_keys = {}
        self.key_counter = 1

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)

        # Check if entering article section
        if tag == 'article' or (tag == 'div' and 'review-main' in attrs_dict.get('class', '')):
            self.in_article = True

        # Check if in FAQ section
        if 'faq-item' in attrs_dict.get('class', ''):
            self.in_faq = True

        self.current_tag = tag

    def handle_endtag(self, tag):
        # Process accumulated data when closing relevant tags
        if self.in_article and tag in ['p', 'h2', 'h3', 'h4', 'li'] and self.current_data:
            text = ''.join(self.current_data).strip()
            if text and len(text) > 3 and not text.startswith('<!--'):
                key = f"review.{self.tool_name}.content.{self.key_counter}"
                self.content_keys[key] = text
                self.key_counter += 1
            self.current_data = []

        if tag == 'article':
            self.in_article = False
        if tag == 'div' and self.in_faq:
            self.in_faq = False

        self.current_tag = None

    def handle_data(self, data):
        if self.in_article and not self.in_faq:
            # Clean up the data
            data = data.strip()
            if data:
                self.current_data.append(data)

def extract_faqs_from_html(tool_name):
    """Extract FAQs using regex pattern matching"""
    html_path = f"GenuisNet.ai/pages/reviews/networking/{tool_name}.html"

    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Pattern for FAQ items
    faq_pattern = r'<div class="faq-question">\\s*(.*?)\\s*<span>\\+</span>.*?</div>.*?<div class="faq-answer">\\s*(.*?)\\s*</div>'
    matches = re.findall(faq_pattern, html, re.DOTALL)

    faqs = {}
    for i, (question, answer) in enumerate(matches, 1):
        # Clean up whitespace and HTML tags
        question = re.sub(r'<[^>]+>', '', question)
        question = re.sub(r'\\s+', ' ', question).strip()

        answer = re.sub(r'<[^>]+>', '', answer)
        answer = re.sub(r'\\s+', ' ', answer).strip()

        if question and answer:
            faqs[f"review.{tool_name}.faq.q{i}"] = question
            faqs[f"review.{tool_name}.faq.a{i}"] = answer

    return faqs

def process_tool(tool_name):
    """Process a single tool: extract content and FAQs"""
    print(f"\\n{'='*60}")
    print(f"Processing {tool_name.upper()}")
    print(f"{'='*60}")

    html_path = f"GenuisNet.ai/pages/reviews/networking/{tool_name}.html"

    # Extract content using HTMLParser
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    extractor = ContentExtractor(tool_name)
    extractor.feed(html)

    content_data = extractor.content_keys

    # Extract FAQs
    faq_data = extract_faqs_from_html(tool_name)

    print(f"  Content keys extracted: {len(content_data)}")
    print(f"  FAQ pairs extracted: {len(faq_data) // 2}")

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
        print(f"  Created: {tool_name}-batch{batch_name[-1]}.json")

    # Create batch files for FAQs
    for batch_name, langs in LANGUAGES.items():
        batch_data = {}
        for lang in langs:
            batch_data[lang] = faq_data

        batch_path = f"GenuisNet.ai/pages/reviews/networking/{tool_name}-faqs-batch{batch_name[-1]}.json"
        with open(batch_path, 'w', encoding='utf-8') as f:
            json.dump(batch_data, f, indent=2, ensure_ascii=False)
        print(f"  Created: {tool_name}-faqs-batch{batch_name[-1]}.json")

    return len(content_data), len(faq_data)

# Process all tools
print("\\n" + "="*60)
print("PROCESSING ALL NETWORKING TOOLS")
print("="*60)

total_content_keys = 0
total_faq_keys = 0

for tool in TOOLS:
    try:
        content_count, faq_count = process_tool(tool)
        total_content_keys += content_count
        total_faq_keys += faq_count
    except Exception as e:
        print(f"  [ERROR] {tool}: {str(e)}")
        import traceback
        traceback.print_exc()

print("\\n" + "="*60)
print("EXTRACTION COMPLETE")
print("="*60)
print(f"\\nTotal content keys: {total_content_keys}")
print(f"Total FAQ keys: {total_faq_keys}")
print(f"Total keys: {total_content_keys + total_faq_keys}")
print(f"\\nFiles created:")
print(f"  - 16 English source files (8 content + 8 FAQ)")
print(f"  - 48 batch files (24 content + 24 FAQ)")
print(f"\\nReady for translation with {(total_content_keys + total_faq_keys) * 9} total translations!")
