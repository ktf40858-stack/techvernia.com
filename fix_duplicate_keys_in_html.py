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

def fix_duplicate_keys(html_file):
    """Corrige les clés dupliquées dans le HTML"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern pour trouver les occurrences de la clé qui se termine par .is.a
    pattern = r'<span data-i18n="(review\.[^"]+\.is\.a)">([^<]+)</span>'
    matches = list(re.finditer(pattern, content))

    if len(matches) > 1:
        # S'il y a plus d'une occurrence, renommer les suivantes
        for i, match in enumerate(matches):
            key = match.group(1)
            text = match.group(2)

            # Déterminer le nouveau nom de clé
            if i == 0:
                # Premier = leading (overview paragraph)
                if "leading" in text.lower():
                    new_key = key + ".leading"
                elif "powerful" in text.lower():
                    new_key = key + ".powerful"
                else:
                    new_key = key
            else:
                # Deuxième = powerful (final verdict paragraph)
                if "powerful" in text.lower():
                    new_key = key + ".powerful"
                elif "leading" in text.lower():
                    new_key = key + ".leading"
                else:
                    new_key = key + f".{i+1}"

            # Remplacer uniquement cette occurrence spécifique
            old_span = match.group(0)
            new_span = old_span.replace(f'data-i18n="{key}"', f'data-i18n="{new_key}"')
            content = content.replace(old_span, new_span, 1)

    # Sauvegarder
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)

    return len(matches)

# MAIN
print("=" * 70)
print("FIXING DUPLICATE KEYS IN HTML FILES")
print("=" * 70)

for tool in tools:
    html_file = os.path.join(edu_dir, f"{tool}.html")
    count = fix_duplicate_keys(html_file)
    if count > 1:
        print(f"  [FIXED] {tool}.html ({count} occurrences of .is.a key)")
    else:
        print(f"  [OK] {tool}.html (no duplicates)")

print("\n" + "=" * 70)
print("[COMPLETE] HTML files updated with unique keys!")
print("=" * 70)
