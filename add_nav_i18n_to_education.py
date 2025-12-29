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

def add_nav_i18n_script(html_file):
    """Ajoute le script nav-i18n.js si absent"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Vérifier si nav-i18n.js existe déjà
    if 'nav-i18n.js' in content:
        return False

    # Trouver la position après i18n.js
    pattern = r'(<script src="../../../js/i18n\.js"></script>)'
    match = re.search(pattern, content)

    if match:
        # Insérer nav-i18n.js après i18n.js
        insertion_point = match.end()
        new_script = '\n<script src="../../../js/nav-i18n.js"></script>'
        content = content[:insertion_point] + new_script + content[insertion_point:]

        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)

        return True
    else:
        print(f"  [!] Could not find i18n.js script tag")
        return False

# MAIN
print("=" * 70)
print("ADDING NAV-I18N.JS TO EDUCATION TOOLS")
print("=" * 70)

total_modified = 0
for tool in tools:
    html_file = os.path.join(edu_dir, f"{tool}.html")

    if os.path.exists(html_file):
        if add_nav_i18n_script(html_file):
            print(f"  [+] {tool}.html - Added nav-i18n.js")
            total_modified += 1
        else:
            print(f"  [OK] {tool}.html - Already has nav-i18n.js")
    else:
        print(f"  [SKIP] {tool}.html - File not found")

print("\n" + "=" * 70)
print(f"[COMPLETE] Modified {total_modified} files")
print("=" * 70)
