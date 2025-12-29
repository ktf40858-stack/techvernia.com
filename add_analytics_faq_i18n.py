#!/usr/bin/env python3
"""Add data-i18n attributes to Analytics FAQ questions."""
import re
from pathlib import Path

ANALYTICS_TOOLS = [
    'alteryx-ai', 'amazon-quicksight-q', 'datarobot', 'domo-ai', 'h2oai',
    'looker-ai', 'microstrategy-ai', 'mode-analytics', 'power-bi-copilot',
    'prophet-meta', 'qlik-sense-ai', 'sisense-ai', 'tableau-pulse',
    'thoughtspot', 'yellowfin-ai'
]

HTML_DIR = Path("GenuisNet.ai/pages/reviews/analytics")

def slugify(text):
    """Convert text to a slug for use in data-i18n keys."""
    slug = text.lower()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[-\s]+', '.', slug)
    slug = slug[:60]
    return slug

def add_faq_i18n_attributes(html_path, tool_name):
    """Add data-i18n attributes to FAQ questions (h4 tags in FAQ section)."""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find FAQ section
    faq_section_match = re.search(
        r'(<section class="review-section" id="faq">.*?</section>)',
        content,
        re.DOTALL
    )

    if not faq_section_match:
        return 0

    faq_section = faq_section_match.group(1)
    faq_counter = 0

    def replace_faq_h4(match):
        nonlocal faq_counter
        faq_counter += 1
        question_text = match.group(1)
        slug = slugify(question_text)
        key = f"review.{tool_name}.faq.{faq_counter}.question.{slug}"
        return f'<h4><span data-i18n="{key}">{question_text}</span></h4>'

    # Replace h4 tags in FAQ section
    new_faq_section = re.sub(
        r'<h4>([^<]+)</h4>',
        replace_faq_h4,
        faq_section
    )

    # Replace FAQ section in content
    content = content.replace(faq_section, new_faq_section)

    # Write back
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return faq_counter

def main():
    print("="*60)
    print("ADDING DATA-I18N TO ANALYTICS FAQ QUESTIONS")
    print("="*60)

    total_faqs = 0

    for tool in ANALYTICS_TOOLS:
        html_file = HTML_DIR / f"{tool}.html"

        if not html_file.exists():
            print(f"[SKIP] {tool}: HTML file not found")
            continue

        try:
            faq_count = add_faq_i18n_attributes(html_file, tool)
            print(f"[OK] {tool}: Added data-i18n to {faq_count} FAQ questions")
            total_faqs += faq_count
        except Exception as e:
            print(f"[FAIL] {tool}: {e}")

    print("="*60)
    print(f"TOTAL FAQ QUESTIONS PROCESSED: {total_faqs}")
    print("="*60)

if __name__ == "__main__":
    main()
