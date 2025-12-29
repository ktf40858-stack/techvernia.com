import os
import re

base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
edu_dir = os.path.join(base_dir, "pages", "reviews", "education")

tools = [
    "aleks", "carnegie-learning", "century-tech", "cognii",
    "coursera-coach", "duolingo-max", "gradescope", "khan-academy-ai",
    "knewton-alta", "querium", "quizlet-ai", "socratic-by-google",
    "squirrel-ai", "thinkster-math"
]

def fix_english_text(html_file):
    """Remplace les textes erronés dans le HTML"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    replacements = [
        ("modern businesses", "modern educational institutions"),
        ("organizations worldwide", "educational institutions worldwide"),
        ("customer service", "education"),
        ("customer-service", "education")
    ]

    fixed_count = 0
    for old_text, new_text in replacements:
        if old_text in content:
            content = content.replace(old_text, new_text)
            fixed_count += 1

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)

    return fixed_count

# MAIN
print("=" * 70)
print("FIXING ENGLISH TEXT IN HTML FILES")
print("=" * 70)

for tool in tools:
    html_file = os.path.join(edu_dir, f"{tool}.html")
    count = fix_english_text(html_file)
    if count > 0:
        print(f"  [FIXED] {tool}.html ({count} replacements)")
    else:
        print(f"  [OK] {tool}.html")

print("\n" + "=" * 70)
print("[COMPLETE] HTML files updated with correct English text!")
print("=" * 70)
