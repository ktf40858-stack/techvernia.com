import os
import re

hr_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\pages\reviews\hr"

hr_tools = {
    "beamery": "Beamery",
    "eightfold-ai": "Eightfold AI",
    "fetcher": "Fetcher",
    "findem": "Findem",
    "harver": "Harver",
    "hirevue": "HireVue",
    "humanly": "Humanly",
    "paradox-olivia": "Paradox (Olivia)",
    "phenom": "Phenom",
    "pymetrics": "Pymetrics",
    "seekout": "SeekOut",
    "sense": "Sense",
    "textio": "Textio",
    "workable-ai": "Workable AI"
}

# FAQ questions mapping
faq_questions = {
    "worth the investment": "faq.is.worth.the.investment",
    "How long does implementation take": "faq.how.long.does.implementation.take",
    "What integrations are available": "faq.what.integrations.are.available",
    "Is my data secure": "faq.is.my.data.secure",
    "Can I migrate from another platform": "faq.can.i.migrate.from.another.platform",
    "What kind of support is available": "faq.what.kind.of.support.is.available",
    "offer a free trial": "faq.does.offer.a.free.trial",
    "How does AI enhance the platform": "faq.how.does.ai.enhance.the.platform"
}

def add_faq_data_i18n(tool_key, tool_name):
    """Add data-i18n attributes to FAQ question h4 tags"""

    html_file = os.path.join(hr_dir, f"{tool_key}.html")

    if not os.path.exists(html_file):
        print(f"  [!] File not found: {tool_key}.html")
        return False

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False

    # For each FAQ question pattern
    for pattern, key_suffix in faq_questions.items():
        # Find h4 tags containing this pattern that DON'T already have data-i18n
        h4_pattern = rf'<h4>([^<]*{re.escape(pattern)}[^<]*)</h4>'

        matches = list(re.finditer(h4_pattern, content))

        for match in matches:
            full_match = match.group(0)
            question_text = match.group(1)

            # Skip if already has data-i18n
            if 'data-i18n' in full_match:
                continue

            # Create the replacement with data-i18n
            full_key = f"review.{tool_key}.{key_suffix}"
            replacement = f'<h4><span data-i18n="{full_key}">{question_text}</span></h4>'

            # Replace this specific occurrence
            content = content.replace(full_match, replacement, 1)
            modified = True

    if modified:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False

print("=" * 70)
print("ADDING data-i18n ATTRIBUTES TO FAQ QUESTIONS")
print("=" * 70)

fixed_count = 0

for tool_key, tool_name in hr_tools.items():
    print(f"\n{tool_name}:")
    if add_faq_data_i18n(tool_key, tool_name):
        print(f"  [+] Added data-i18n to FAQ questions")
        fixed_count += 1
    else:
        print(f"  [OK] Already has data-i18n or no FAQs found")

print("\n" + "=" * 70)
print(f"COMPLETE: Fixed {fixed_count}/{len(hr_tools)} tools")
print("=" * 70)
print("\nFAQ questions will now translate in all 10 languages!")
print("=" * 70)
