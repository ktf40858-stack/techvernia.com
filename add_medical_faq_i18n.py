#!/usr/bin/env python3
"""Add data-i18n attributes to Medical FAQ questions and answers."""
import re
from pathlib import Path

MEDICAL_TOOLS = [
    'aidoc', 'butterfly-iq', 'nuance-dragon', 'paige-ai',
    'pathai', 'tempus', 'viz-ai', 'zebra-medical'
]

HTML_DIR = Path("GenuisNet.ai/pages/reviews/medical")

def slugify(text):
    """Convert text to a slug for use in data-i18n keys."""
    # Remove special characters, convert to lowercase, replace spaces with dots
    slug = text.lower()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[-\s]+', '.', slug)
    slug = slug[:60]  # Limit length
    return slug

def add_faq_i18n_attributes(html_path, tool_name):
    """Add data-i18n attributes to FAQ questions and answers."""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    faq_counter = 0

    def replace_faq_question(match):
        nonlocal faq_counter
        faq_counter += 1
        question_text = match.group(1)
        slug = slugify(question_text)
        key = f"review.{tool_name}.faq.{faq_counter}.question.{slug}"
        return f'<div class="faq-question"><span data-i18n="{key}">{question_text}</span><span>+</span></div>'

    def replace_faq_answer(match):
        answer_text = match.group(1)
        slug = slugify(answer_text[:50])  # Use first 50 chars for slug
        key = f"review.{tool_name}.faq.{faq_counter}.answer.{slug}"
        return f'<div class="faq-answer"><span data-i18n="{key}">{answer_text}</span></div>'

    # Replace FAQ questions
    content = re.sub(
        r'<div class="faq-question">([^<]+)<span>\+</span></div>',
        replace_faq_question,
        content
    )

    # Reset counter for answers
    faq_counter = 0

    # Replace FAQ answers - capture everything until </div>
    def replace_faq_answer_multiline(match):
        nonlocal faq_counter
        faq_counter += 1
        answer_text = match.group(1)
        slug = slugify(answer_text[:50])
        key = f"review.{tool_name}.faq.{faq_counter}.answer.{slug}"
        return f'<div class="faq-answer"><span data-i18n="{key}">{answer_text}</span></div>'

    content = re.sub(
        r'<div class="faq-answer">(.+?)</div>',
        replace_faq_answer_multiline,
        content,
        flags=re.DOTALL
    )

    # Write back
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return faq_counter

def main():
    print("="*60)
    print("ADDING DATA-I18N TO MEDICAL FAQ SECTIONS")
    print("="*60)

    total_faqs = 0

    for tool in MEDICAL_TOOLS:
        html_file = HTML_DIR / f"{tool}.html"

        if not html_file.exists():
            print(f"[SKIP] {tool}: HTML file not found")
            continue

        try:
            faq_count = add_faq_i18n_attributes(html_file, tool)
            print(f"[OK] {tool}: Added data-i18n to {faq_count} FAQ pairs")
            total_faqs += faq_count
        except Exception as e:
            print(f"[FAIL] {tool}: {e}")

    print("="*60)
    print(f"TOTAL FAQ PAIRS PROCESSED: {total_faqs}")
    print("="*60)

if __name__ == "__main__":
    main()
