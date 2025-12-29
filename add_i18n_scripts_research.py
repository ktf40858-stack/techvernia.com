import os
import re

base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
research_dir = os.path.join(base_dir, "pages", "reviews", "research")

tools = [
    "connected-papers", "consensus", "elicit", "irisai", "litmaps",
    "perplexity-research", "researchrabbit", "scholarcy", "scispace",
    "scite", "semantic-scholar", "undermind"
]

print("=" * 70)
print("ADDING I18N SCRIPTS TO RESEARCH HTML FILES")
print("=" * 70)

count = 0
for tool in tools:
    html_file = os.path.join(research_dir, f"{tool}.html")

    if not os.path.exists(html_file):
        print(f"\n{tool}: [SKIP] File not found")
        continue

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Vérifier si les scripts ne sont pas déjà présents
    if f'src="../../../js/{tool}-i18n.js"' in content:
        print(f"\n{tool}: [SKIP] Scripts already added")
        continue

    # Trouver la balise </body>
    if '</body>' not in content:
        print(f"\n{tool}: [ERROR] No </body> tag found")
        continue

    # Créer les balises script à ajouter
    scripts_to_add = f'''<script src="../../../js/i18n.js"></script>
<script src="../../../js/nav-i18n.js"></script>
<script src="../../../js/{tool}-i18n.js"></script>
</body>'''

    # Remplacer </body> par les scripts + </body>
    new_content = content.replace('</body>', scripts_to_add)

    # Écrire le fichier modifié
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"\n{tool}: [OK] Added i18n scripts")
    count += 1

print("\n" + "=" * 70)
print(f"[COMPLETE] Added scripts to {count}/{len(tools)} tools")
print("=" * 70)
