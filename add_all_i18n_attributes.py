"""
Comprehensive i18n attribute addition using structural HTML parsing
Maps all extracted content keys to their corresponding HTML elements in order
"""
import json
import re
from html.parser import HTMLParser

TOOLS = ['chorusai', 'conversica', 'drift', 'gong', 'hubspot-ai', 'looker', 'salesforce-einstein', 'tableau']

class I18nAttributeAdder(HTMLParser):
    """Add data-i18n attributes to HTML elements based on extracted keys"""

    def __init__(self, tool_name, content_keys, faq_keys):
        super().__init__()
        self.tool_name = tool_name
        self.content_keys = list(content_keys.items())
        self.faq_keys = dict(faq_keys)
        self.key_index = 0
        self.output = []
        self.in_article = False
        self.in_faq_question = False
        self.in_faq_answer = False
        self.current_content = []
        self.skip_next_data = False

    def handle_starttag(self, tag, attrs):
        # Check if we're entering article or FAQ section
        attrs_dict = dict(attrs)
        if tag == 'article' or (tag == 'div' and attrs_dict.get('class') == 'review-main'):
            self.in_article = True
        elif tag == 'div' and 'faq-question' in attrs_dict.get('class', ''):
            self.in_faq_question = True
        elif tag == 'div' and 'faq-answer' in attrs_dict.get('class', ''):
            self.in_faq_answer = True

        # Build tag with attributes
        attrs_str = ''.join(f' {k}="{v}"' if v is not None else f' {k}' for k, v in attrs)
        self.output.append(f'<{tag}{attrs_str}>')

    def handle_endtag(self, tag):
        self.output.append(f'</{tag}>')

        if tag == 'article' or (tag == 'div' and self.in_article):
            self.in_article = False
        elif tag == 'div' and self.in_faq_question:
            self.in_faq_question = False
        elif tag == 'div' and self.in_faq_answer:
            self.in_faq_answer = False

    def handle_data(self, data):
        # Just pass through the data as-is
        # The wrapping with spans will be handled separately
        self.output.append(data)

    def handle_startendtag(self, tag, attrs):
        attrs_str = ''.join(f' {k}="{v}"' if v is not None else f' {k}' for k, v in attrs)
        self.output.append(f'<{tag}{attrs_str}/>')

    def get_html(self):
        return ''.join(self.output)


def add_i18n_comprehensively(tool_name):
    """Add data-i18n attributes using manual pattern matching"""
    print(f"\n{'='*60}")
    print(f"Processing {tool_name.upper()} - Comprehensive Approach")
    print(f"{'='*60}")

    html_path = f"GenuisNet.ai/pages/reviews/business/{tool_name}.html"
    content_json = f"GenuisNet.ai/pages/reviews/business/{tool_name}-en.json"
    faq_json = f"GenuisNet.ai/pages/reviews/business/{tool_name}-faqs-en.json"

    # Read files
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    with open(content_json, 'r', encoding='utf-8') as f:
        content_data = json.load(f)

    with open(faq_json, 'r', encoding='utf-8') as f:
        faq_data = json.load(f)

    modifications = 0

    # Strategy: Wrap content in data-i18n spans where not already present
    for key, text in content_data.items():
        # Escape text for regex
        escaped = re.escape(text)

        # Skip if already has data-i18n
        if f'data-i18n="{key}"' in html:
            continue

        # Try different patterns
        patterns = [
            # Paragraph without span
            (rf'(<p>)({escaped})(</p>)', rf'\1<span data-i18n="{key}">\2</span>\3'),
            # H2 span content
            (rf'(<h2><span[^>]*>)({escaped})(</span></h2>)', rf'\1<span data-i18n="{key}">\2</span>\3'),
            # H4 without span
            (rf'(<h4>)({escaped})(</h4>)', rf'\1<span data-i18n="{key}">\2</span>\3'),
            # Li without span
            (rf'(<li>)({escaped})(</li>)', rf'\1<span data-i18n="{key}">\2</span>\3'),
            # Span without data-i18n
            (rf'(<span>)({escaped})(</span>)', rf'<span data-i18n="{key}">\2</span>'),
            # Button text
            (rf'(<a[^>]*class="[^"]*btn[^"]*"[^>]*>)({escaped})(</a>)', rf'\1<span data-i18n="{key}">\2</span>\3'),
        ]

        for pattern, replacement in patterns:
            if re.search(pattern, html, re.DOTALL):
                html = re.sub(pattern, replacement, html, count=1, flags=re.DOTALL)
                modifications += 1
                break

    # Handle FAQ data-i18n
    for key, text in faq_data.items():
        if f'data-i18n="{key}"' in html:
            continue

        escaped = re.escape(text)

        if '.faq.q' in key:
            # FAQ question
            pattern = rf'(<div class="faq-question">)\s*({escaped})\s*(<span)'
            replacement = rf'\1<span data-i18n="{key}">\2</span> \3'
            if re.search(pattern, html):
                html = re.sub(pattern, replacement, html, count=1)
                modifications += 1
        elif '.faq.a' in key:
            # FAQ answer
            pattern = rf'(<div class="faq-answer">)\s*({escaped})\s*(</div>)'
            replacement = rf'\1<span data-i18n="{key}">\2</span>\3'
            if re.search(pattern, html, re.DOTALL):
                html = re.sub(pattern, replacement, html, count=1, flags=re.DOTALL)
                modifications += 1

    # Save
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"  Total content keys: {len(content_data)}")
    print(f"  Total FAQ keys: {len(faq_data)}")
    print(f"  Modifications made in this pass: {modifications}")

    # Count total data-i18n attributes now present
    total_i18n = len(re.findall(rf'data-i18n="review\.{tool_name}\.(content|faq)\.', html))
    coverage = (total_i18n / (len(content_data) + len(faq_data))) * 100
    print(f"  Total data-i18n attributes: {total_i18n}/{len(content_data) + len(faq_data)} ({coverage:.1f}%)")
    print(f"  [OK] {tool_name} processed")

# Process all tools
print("\n" + "="*60)
print("COMPREHENSIVE I18N ATTRIBUTE ADDITION")
print("="*60)

for tool in TOOLS:
    try:
        add_i18n_comprehensively(tool)
    except Exception as e:
        print(f"  [ERROR] {tool}: {str(e)}")
        import traceback
        traceback.print_exc()

print("\n" + "="*60)
print("COMPREHENSIVE PROCESSING COMPLETE")
print("="*60)
