import re
import os

seo_tools = [
    'ahrefs', 'clearscope', 'frase', 'marketmuse',
    'neuronwriter', 'scalenut', 'semrush', 'surfer-seo'
]

def add_data_i18n_to_faqs(html_file, tool_name):
    """Ajoute data-i18n aux FAQs dans un fichier HTML"""
    print(f"\nTraitement de {html_file}...")

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern pour trouver les FAQs sans data-i18n
    faq_pattern = r'<div class="faq-item"><div class="faq-question">([^<]+)<span>\+</span></div><div class="faq-answer">([^<]+)</div></div>'

    faq_num = 1
    modified = False

    def replace_faq(match):
        nonlocal faq_num, modified
        question = match.group(1).strip()
        answer = match.group(2).strip()

        # Créer la nouvelle structure avec data-i18n
        new_faq = f'<div class="faq-item">'
        new_faq += f'<div class="faq-question">'
        new_faq += f'<span data-i18n="review.{tool_name}.faq.q{faq_num}">{question}</span>'
        new_faq += f'<span>+</span>'
        new_faq += f'</div>'
        new_faq += f'<div class="faq-answer">'
        new_faq += f'<span data-i18n="review.{tool_name}.faq.a{faq_num}">{answer}</span>'
        new_faq += f'</div>'
        new_faq += f'</div>'

        faq_num += 1
        modified = True
        return new_faq

    # Remplacer tous les FAQs
    new_content = re.sub(faq_pattern, replace_faq, content)

    # Ajouter le script si pas déjà présent
    script_tag = f'<script src="../../js/{tool_name}-faqs-i18n.js"></script>'
    if script_tag not in new_content and modified:
        # Trouver où insérer le script (avant </body>)
        new_content = new_content.replace('</body>', f'    {script_tag}\n</body>')
        print(f"  - Ajoute le script {tool_name}-faqs-i18n.js")

    if modified:
        # Sauvegarder le fichier
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  - Ajoute data-i18n a {faq_num - 1} FAQs")
        return True
    else:
        print(f"  - Aucune modification necessaire")
        return False

# Traiter tous les fichiers SEO
modified_count = 0
for tool in seo_tools:
    html_file = f"GenuisNet.ai/pages/reviews/seo/{tool}.html"
    if os.path.exists(html_file):
        if add_data_i18n_to_faqs(html_file, tool):
            modified_count += 1
    else:
        print(f"\nFichier {html_file} non trouve")

print(f"\nTermine! {modified_count} fichiers modifies")
