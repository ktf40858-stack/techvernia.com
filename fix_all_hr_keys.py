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
    "paradox-olivia": "Paradox Olivia",
    "phenom": "Phenom",
    "pymetrics": "Pymetrics",
    "seekout": "SeekOut",
    "sense": "Sense",
    "textio": "Textio",
    "workable-ai": "Workable AI"
}

def fix_html_keys(tool_key, tool_name):
    """Fix incorrect translation keys in HTML"""
    html_file = os.path.join(hr_dir, f"{tool_key}.html")

    if not os.path.exists(html_file):
        print(f"  [!] File not found: {tool_key}.html")
        return False

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False

    # Fix Overview section - Replace long text with short version
    overview_patterns = [
        # Pattern 1: .is.a.leading.ai-powered or similar long keys
        (
            rf'<p><span data-i18n="review\.{re.escape(tool_key)}\.{re.escape(tool_key)}\.is\.a\.leading[^"]*">[^<]+</span></p>',
            f'<p><span data-i18n="review.{tool_key}.{tool_key}.is.a">{tool_name} is a powerful, feature-rich HR platform that delivers exceptional value for teams of all sizes. Highly recommended.</span></p>'
        ),
        # Pattern 2: For tools with dots instead of hyphens
        (
            rf'<p><span data-i18n="review\.{re.escape(tool_key)}\.{re.escape(tool_key.replace("-", "."))}\.is\.a\.leading[^"]*">[^<]+</span></p>',
            f'<p><span data-i18n="review.{tool_key}.{tool_key}.is.a">{tool_name} is a powerful, feature-rich HR platform that delivers exceptional value for teams of all sizes. Highly recommended.</span></p>'
        ),
    ]

    for pattern, replacement in overview_patterns:
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content)
            modified = True

    # Fix Final Verdict section - Only fix the key, keep the text
    verdict_patterns = [
        # .is.a.powerful.feature-rich
        rf'data-i18n="review\.{re.escape(tool_key)}\.{re.escape(tool_key)}\.is\.a\.powerful\.feature-rich"',
        # .is.a.powerful
        rf'data-i18n="review\.{re.escape(tool_key)}\.{re.escape(tool_key)}\.is\.a\.powerful"',
        # For tools with dots instead of hyphens
        rf'data-i18n="review\.{re.escape(tool_key)}\.{re.escape(tool_key.replace("-", "."))}\.is\.a\.powerful[^"]*"',
    ]

    correct_key = f'data-i18n="review.{tool_key}.{tool_key}.is.a"'

    for pattern in verdict_patterns:
        if re.search(pattern, content):
            content = re.sub(pattern, correct_key, content)
            modified = True

    if modified:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False

print("=" * 70)
print("FIXING ALL HR TOOL TRANSLATION KEYS")
print("=" * 70)

fixed_count = 0

for tool_key, tool_name in hr_tools.items():
    print(f"\n{tool_name}:")
    if fix_html_keys(tool_key, tool_name):
        print(f"  [+] Fixed incorrect translation keys")
        fixed_count += 1
    else:
        print(f"  [OK] No changes needed")

print("\n" + "=" * 70)
print(f"COMPLETE: Fixed {fixed_count}/{len(hr_tools)} tools")
print("=" * 70)
