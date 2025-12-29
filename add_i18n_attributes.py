"""
Add data-i18n attributes to all Business category HTML files
Also adds i18n script integration and FAQ sticky positioning
"""
import json
import re
import os

TOOLS = ['chorusai', 'conversica', 'drift', 'gong', 'hubspot-ai', 'looker', 'salesforce-einstein', 'tableau']

def escape_for_regex(text):
    """Escape special regex characters but preserve the text structure"""
    # Escape special regex characters
    text = re.escape(text)
    # Allow flexible whitespace
    text = re.sub(r'\\ ', r'\\s+', text)
    return text

def add_i18n_to_html(tool_name):
    """Add data-i18n attributes to HTML file based on English JSON"""
    print(f"\n{'='*60}")
    print(f"Processing {tool_name.upper()}")
    print(f"{'='*60}")

    html_path = f"GenuisNet.ai/pages/reviews/business/{tool_name}.html"
    content_json_path = f"GenuisNet.ai/pages/reviews/business/{tool_name}-en.json"
    faq_json_path = f"GenuisNet.ai/pages/reviews/business/{tool_name}-faqs-en.json"

    # Read HTML
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    original_html = html

    # Read content translations
    with open(content_json_path, 'r', encoding='utf-8') as f:
        content_data = json.load(f)

    # Read FAQ translations
    with open(faq_json_path, 'r', encoding='utf-8') as f:
        faq_data = json.load(f)

    replacements_made = 0

    # Process content keys
    for key, text in content_data.items():
        # Skip very short or common texts that might cause false matches
        if len(text) < 10 or text in ['Overview', 'Pricing', 'Key Features']:
            continue

        # Create pattern to find the text in HTML (handling multiline)
        # Look for the text in <p>, <h2>, <h3>, <h4>, <li>, etc.
        escaped_text = escape_for_regex(text[:100])  # Use first 100 chars for matching

        # Pattern for paragraph tags
        pattern_p = rf'(<p>)({re.escape(text)})(</p>)'
        if re.search(pattern_p, html, re.DOTALL):
            html = re.sub(pattern_p, rf'\1<span data-i18n="{key}">\2</span>\3', html, count=1, flags=re.DOTALL)
            replacements_made += 1
            continue

        # Pattern for h4 tags (feature titles)
        pattern_h4 = rf'(<h4>)({re.escape(text)})(</h4>)'
        if re.search(pattern_h4, html):
            html = re.sub(pattern_h4, rf'\1<span data-i18n="{key}">\2</span>\3', html, count=1)
            replacements_made += 1
            continue

        # Pattern for list items
        pattern_li = rf'(<li>)({re.escape(text)})(</li>)'
        if re.search(pattern_li, html):
            html = re.sub(pattern_li, rf'\1<span data-i18n="{key}">\2</span>\3', html, count=1)
            replacements_made += 1
            continue

    # Process FAQ keys with sticky positioning
    for key, text in faq_data.items():
        if '.faq.q' in key:
            # FAQ question - add data-i18n and ensure visibility when expanded
            pattern_faq_q = rf'(<div class="faq-question">)\s*({re.escape(text)})\s*(<span>)'
            if re.search(pattern_faq_q, html):
                html = re.sub(pattern_faq_q, rf'\1<span data-i18n="{key}">\2</span> \3', html, count=1)
                replacements_made += 1
        elif '.faq.a' in key:
            # FAQ answer - add data-i18n
            pattern_faq_a = rf'(<div class="faq-answer">)\s*({re.escape(text)})\s*(</div>)'
            if re.search(pattern_faq_a, html, re.DOTALL):
                html = re.sub(pattern_faq_a, rf'\1<span data-i18n="{key}">\2</span>\3', html, count=1, flags=re.DOTALL)
                replacements_made += 1

    # Add i18n JavaScript before closing body tag if not already present
    i18n_script = f'<script src="../../../js/{tool_name}-i18n.js"></script>'
    if i18n_script not in html:
        html = html.replace('</body>', f'    {i18n_script}\n</body>')
        print(f"  Added i18n script reference")

    # Add FAQ sticky positioning CSS if FAQs exist and not already present
    if faq_data and '.faq-question {' not in html:
        faq_css = """
        /* FAQ sticky positioning - keeps question visible when expanded */
        .faq-question {
            position: sticky;
            top: 80px;
            background: var(--bg-card);
            z-index: 10;
            padding: var(--space-md);
            margin: calc(var(--space-md) * -1);
            margin-bottom: var(--space-md);
        }
        """
        # Insert before </style> in the head
        html = html.replace('</style>', f'{faq_css}\n    </style>', 1)
        print(f"  Added FAQ sticky positioning CSS")

    # Save modified HTML
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"  Content keys: {len(content_data)}")
    print(f"  FAQ keys: {len(faq_data)}")
    print(f"  Replacements made: {replacements_made}")
    print(f"  [OK] {tool_name} HTML updated")

# Process all tools
print("\n" + "="*60)
print("ADDING I18N ATTRIBUTES TO ALL BUSINESS HTML FILES")
print("="*60)

for tool in TOOLS:
    try:
        add_i18n_to_html(tool)
    except Exception as e:
        print(f"\n  [ERROR] processing {tool}: {str(e)}")

print("\n" + "="*60)
print("ALL HTML FILES UPDATED!")
print("="*60)
print("\nNext: Test multilingual functionality")
