import os
import re

base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
research_dir = os.path.join(base_dir, "pages", "reviews", "research")
sales_reference = os.path.join(base_dir, "pages", "reviews", "sales", "salesforce-einstein-gpt.html")

tools = [
    "connected-papers", "consensus", "elicit", "irisai", "litmaps",
    "perplexity-research", "researchrabbit", "scholarcy", "scispace",
    "scite", "semantic-scholar", "undermind"
]

# Lire la navbar de référence depuis Sales
with open(sales_reference, 'r', encoding='utf-8') as f:
    sales_content = f.read()

# Extraire la navbar complète (lignes 94-158)
navbar_pattern = r'<nav class="navbar" id="navbar">.*?</nav>'
navbar_match = re.search(navbar_pattern, sales_content, re.DOTALL)

if not navbar_match:
    print("[ERROR] Could not find navbar in reference file")
    exit(1)

navbar_template = navbar_match.group(0)

# Adapter pour Research: changer le lien Categories
navbar_research = navbar_template.replace(
    'href="../../categories/ai-sales.html"',
    'href="../../categories/ai-research.html"'
)

print("=" * 70)
print("IMPLEMENTING NAVBAR FOR AI RESEARCH & ACADEMIA TOOLS")
print("=" * 70)

count = 0
for tool in tools:
    html_file = os.path.join(research_dir, f"{tool}.html")

    if not os.path.exists(html_file):
        print(f"\n{tool}: [SKIP] File not found")
        continue

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remplacer l'ancienne navbar par la nouvelle
    old_navbar_pattern = r'<nav class="navbar" id="navbar">.*?</nav>'

    if re.search(old_navbar_pattern, content, re.DOTALL):
        new_content = re.sub(old_navbar_pattern, navbar_research, content, flags=re.DOTALL)

        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"\n{tool}: [OK] Navbar updated")
        count += 1
    else:
        print(f"\n{tool}: [ERROR] No navbar found")

print("\n" + "=" * 70)
print(f"[COMPLETE] Updated navbar in {count}/{len(tools)} tools")
print("=" * 70)
