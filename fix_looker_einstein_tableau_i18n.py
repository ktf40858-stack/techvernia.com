"""
Fix i18n keys for Looker, Salesforce Einstein, and Tableau HTML files
Replace incorrect keys with proper content.X keys by matching text content
"""
import json
import re

TOOLS = ['looker', 'salesforce-einstein', 'tableau']

def normalize_text(text):
    """Normalize text for comparison"""
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    # Remove common punctuation differences
    text = text.replace(chr(8212), '-')  # em dash
    text = text.replace(chr(8217), "'")  # right single quote
    text = text.replace(chr(8220), '"')  # left double quote
    text = text.replace(chr(8221), '"')  # right double quote
    return text.lower()[:100]  # Use first 100 chars for matching

def fix_i18n_keys(tool_name):
    """Fix all i18n keys in HTML file"""
    print(f"\n{'='*60}")
    print(f"Fixing {tool_name.upper()}")
    print(f"{'='*60}")

    html_path = f"GenuisNet.ai/pages/reviews/business/{tool_name}.html"
    content_json = f"GenuisNet.ai/pages/reviews/business/{tool_name}-en.json"
    faq_json = f"GenuisNet.ai/pages/reviews/business/{tool_name}-faqs-en.json"

    # Read HTML
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Read JSON files
    with open(content_json, 'r', encoding='utf-8') as f:
        content_data = json.load(f)

    with open(faq_json, 'r', encoding='utf-8') as f:
        faq_data = json.load(f)

    # Create reverse lookup: text -> correct key
    text_to_key = {}
    for key, text in content_data.items():
        norm_text = normalize_text(text)
        text_to_key[norm_text] = key

    for key, text in faq_data.items():
        norm_text = normalize_text(text)
        text_to_key[norm_text] = key

    # Find all data-i18n spans and fix them
    pattern = r'<span data-i18n="([^"]+)">([^<]+)</span>'
    replacements = 0
    incorrect_keys = 0

    def replace_key(match):
        nonlocal replacements, incorrect_keys
        old_key = match.group(1)
        text = match.group(2)

        # Skip if already correct (content.X or faq.X)
        if '.content.' in old_key or '.faq.' in old_key:
            return match.group(0)

        # Skip common keys
        if old_key.startswith('review.common.'):
            return match.group(0)

        # Find correct key by matching text
        norm_text = normalize_text(text)
        if norm_text in text_to_key:
            correct_key = text_to_key[norm_text]
            if old_key != correct_key:
                incorrect_keys += 1
                replacements += 1
                return f'<span data-i18n="{correct_key}">{text}</span>'

        # If no match found, keep original but count as incorrect
        incorrect_keys += 1
        return match.group(0)

    html = re.sub(pattern, replace_key, html)

    # Save fixed HTML
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)

    # Count final stats
    total_correct_keys = len(re.findall(rf'data-i18n="review\.{tool_name}\.(content|faq)\.', html))
    total_keys_expected = len(content_data) + len(faq_data)

    print(f"  Content keys in JSON: {len(content_data)}")
    print(f"  FAQ keys in JSON: {len(faq_data)}")
    print(f"  Total expected: {total_keys_expected}")
    print(f"  Incorrect keys found: {incorrect_keys}")
    print(f"  Keys fixed: {replacements}")
    print(f"  Correct keys in HTML: {total_correct_keys}/{total_keys_expected}")
    print(f"  Coverage: {(total_correct_keys/total_keys_expected)*100:.1f}%")
    print(f"  [OK] {tool_name} processed")

# Process all three tools
print("\n" + "="*60)
print("FIXING I18N KEYS FOR LOOKER, SALESFORCE EINSTEIN, TABLEAU")
print("="*60)

for tool in TOOLS:
    try:
        fix_i18n_keys(tool)
    except Exception as e:
        print(f"  [ERROR] {tool}: {str(e)}")
        import traceback
        traceback.print_exc()

print("\n" + "="*60)
print("I18N KEY FIXING COMPLETE")
print("="*60)
