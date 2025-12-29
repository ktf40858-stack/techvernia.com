import os
import re

research_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\pages\reviews\research"

research_tools = [
    "connected-papers",
    "consensus",
    "elicit",
    "irisai",
    "litmaps",
    "perplexity-research",
    "researchrabbit",
    "scholarcy",
    "scispace",
    "scite",
    "semantic-scholar",
    "undermind"
]

def fix_tool(tool_key):
    """Fix the incorrect key in Final Verdict section"""
    html_file = os.path.join(research_dir, f"{tool_key}.html")

    if not os.path.exists(html_file):
        print(f"  [!] File not found: {tool_key}.html")
        return False

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern pour trouver la mauvaise clé (avec .is.a.powerful.feature-rich ou .is.a.leading)
    # Remplacer le nom de l'outil avec points ou traits d'union
    tool_name_pattern = tool_key.replace("-", ".")

    # Chercher les patterns incorrects
    patterns = [
        rf'data-i18n="review\.{re.escape(tool_key)}\.{re.escape(tool_name_pattern)}\.is\.a\.powerful\.feature-rich"',
        rf'data-i18n="review\.{re.escape(tool_key)}\.{re.escape(tool_name_pattern)}\.is\.a\.leading"',
        rf'data-i18n="review\.{re.escape(tool_key)}\.{re.escape(tool_key)}\.is\.a\.powerful\.feature-rich"',
        rf'data-i18n="review\.{re.escape(tool_key)}\.{re.escape(tool_key)}\.is\.a\.powerful"',
        rf'data-i18n="review\.{re.escape(tool_key)}\.{re.escape(tool_key)}\.is\.a\.leading"',
    ]

    correct_key = f'data-i18n="review.{tool_key}.{tool_key}.is.a"'

    modified = False
    for pattern in patterns:
        if re.search(pattern, content):
            content = re.sub(pattern, correct_key, content)
            modified = True

    if modified:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False

print("=" * 70)
print("FIXING ALL RESEARCH TOOL TRANSLATION KEYS")
print("=" * 70)

fixed_count = 0

for tool in research_tools:
    print(f"\n{tool}:")
    if fix_tool(tool):
        print(f"  [+] Fixed incorrect translation key")
        fixed_count += 1
    else:
        print(f"  [OK] No changes needed")

print("\n" + "=" * 70)
print(f"COMPLETE: Fixed {fixed_count}/{len(research_tools)} tools")
print("=" * 70)
