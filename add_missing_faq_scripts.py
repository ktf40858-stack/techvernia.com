import os

# Outils qui ont besoin du script FAQs i18n
tools_needing_script = ['ahrefs', 'semrush', 'surfer-seo']

for tool in tools_needing_script:
    html_file = f"GenuisNet.ai/pages/reviews/seo/{tool}.html"
    script_tag = f'<script src="../../js/{tool}-faqs-i18n.js"></script>'

    if not os.path.exists(html_file):
        print(f"Fichier {html_file} non trouve")
        continue

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Vérifier si le script est déjà présent
    if script_tag in content:
        print(f"{tool}.html a deja le script FAQs i18n")
        continue

    # Ajouter le script avant </body>
    new_content = content.replace('</body>', f'    {script_tag}\n</body>')

    # Sauvegarder
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"Ajoute le script FAQs i18n a {tool}.html")

print("\nTermine!")
