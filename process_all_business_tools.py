"""
Master script to process ALL 8 AI Business tools for i18n
Automatically extracts content, generates keys, and creates batch files
"""
import json
import os
import re
from html.parser import HTMLParser

# All 8 AI Business tools
TOOLS = ['chorusai', 'conversica', 'drift', 'gong', 'hubspot-ai', 'looker', 'salesforce-einstein', 'tableau']

# Target languages
LANGUAGES = {
    'batch1': ['es', 'fr', 'de'],
    'batch2': ['pt', 'zh', 'ja'],
    'batch3': ['ko', 'ar', 'hi']
}

class ContentExtractor(HTMLParser):
    def __init__(self, tool_name):
        super().__init__()
        self.tool_name = tool_name
        self.in_article = False
        self.in_faq = False
        self.current_tag = None
        self.current_class = ''
        self.content_keys = {}
        self.faq_keys = {}
        self.key_counter = 1
        self.faq_counter = 1
        self.skip_tags = {'script', 'style', 'svg', 'path'}
        self.current_data = ''

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)

        # Check if we're in article
        if tag == 'article':
            self.in_article = True

        # Check if we're in FAQ section
        if 'class' in attrs_dict and 'faq-question' in attrs_dict.get('class', ''):
            self.in_faq = True

        if self.in_article and tag not in self.skip_tags:
            self.current_tag = tag
            self.current_class = attrs_dict.get('class', '')

    def handle_data(self, data):
        data = data.strip()

        # Skip short content, symbols, and already translated content
        if not data or len(data) < 5 or data in ['+', '−', '→']:
            return

        # Skip if it already has data-i18n (check review.common patterns)
        if 'review.common.' in data:
            return

        if self.in_article and self.current_tag not in self.skip_tags:
            # Generate appropriate key based on context
            if self.in_faq:
                # FAQ keys
                if 'faq-question' in self.current_class:
                    key = f"review.{self.tool_name}.faq.q{self.faq_counter}"
                    self.faq_keys[key] = data
                elif 'faq-answer' in self.current_class:
                    key = f"review.{self.tool_name}.faq.a{self.faq_counter}"
                    self.faq_keys[key] = data
                    self.faq_counter += 1
            else:
                # Content keys
                key = f"review.{self.tool_name}.content.{self.key_counter}"
                self.content_keys[key] = data
                self.key_counter += 1

    def handle_endtag(self, tag):
        if tag == 'article':
            self.in_article = False
        if tag == 'div' and self.in_faq:
            self.in_faq = False
        self.current_tag = None
        self.current_class = ''

def process_tool(tool_name):
    """Process a single tool and create all necessary files"""
    print(f"\n{'='*60}")
    print(f"Processing {tool_name.upper()}")
    print(f"{'='*60}")

    html_path = f"GenuisNet.ai/pages/reviews/business/{tool_name}.html"

    if not os.path.exists(html_path):
        print(f"ERROR: {html_path} not found!")
        return False

    # Read HTML file
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Extract content
    parser = ContentExtractor(tool_name)
    parser.feed(html_content)

    content_count = len(parser.content_keys)
    faq_count = len(parser.faq_keys)
    total_keys = content_count + faq_count

    print(f"Extracted:")
    print(f"  - Content keys: {content_count}")
    print(f"  - FAQ keys: {faq_count}")
    print(f"  - TOTAL: {total_keys}")

    # Create English files
    en_content_path = f"GenuisNet.ai/pages/reviews/business/{tool_name}-en.json"
    en_faq_path = f"GenuisNet.ai/pages/reviews/business/{tool_name}-faqs-en.json"

    with open(en_content_path, 'w', encoding='utf-8') as f:
        json.dump(parser.content_keys, f, indent=2, ensure_ascii=False)
    print(f"Created: {en_content_path}")

    with open(en_faq_path, 'w', encoding='utf-8') as f:
        json.dump(parser.faq_keys, f, indent=2, ensure_ascii=False)
    print(f"Created: {en_faq_path}")

    # Create batch files for content
    for batch_name, langs in LANGUAGES.items():
        batch_data = {}
        for lang in langs:
            batch_data[lang] = parser.content_keys

        batch_path = f"GenuisNet.ai/pages/reviews/business/{tool_name}-{batch_name}.json"
        with open(batch_path, 'w', encoding='utf-8') as f:
            json.dump(batch_data, f, indent=2, ensure_ascii=False)
        print(f"Created: {tool_name}-{batch_name}.json ({len(langs)} languages)")

    # Create batch files for FAQs
    for batch_name, langs in LANGUAGES.items():
        batch_data = {}
        for lang in langs:
            batch_data[lang] = parser.faq_keys

        batch_path = f"GenuisNet.ai/pages/reviews/business/{tool_name}-faqs-{batch_name}.json"
        with open(batch_path, 'w', encoding='utf-8') as f:
            json.dump(batch_data, f, indent=2, ensure_ascii=False)
        print(f"Created: {tool_name}-faqs-{batch_name}.json ({len(langs)} languages)")

    return True

# Process all tools
print("\n" + "="*60)
print("AI BUSINESS TOOLS - BATCH PROCESSING")
print("="*60)

success_count = 0
for tool in TOOLS:
    if process_tool(tool):
        success_count += 1

print(f"\n{'='*60}")
print(f"SUMMARY: Successfully processed {success_count}/{len(TOOLS)} tools")
print(f"{'='*60}")
print("\nNext step: Launch translation agents for all batch files")
print(f"Total agents to launch: {success_count * 6} agents (6 per tool)")
