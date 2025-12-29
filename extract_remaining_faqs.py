import json
import re

def extract_faqs_from_html(html_file, tool_name):
    """Extrait les FAQs d'un fichier HTML et crée le fichier -en.json"""
    print(f"\nExtraction des FAQs de {html_file}...")

    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Pattern pour trouver les FAQ items
    faq_pattern = r'<div class="faq-item"><div class="faq-question">(.*?)<span>\+</span></div><div class="faq-answer">(.*?)</div></div>'

    matches = re.findall(faq_pattern, html_content, re.DOTALL)

    if not matches:
        print(f"Aucun FAQ trouve dans {html_file}")
        return None

    faqs = {}
    faq_num = 1

    for question, answer in matches:
        # Nettoyer les balises HTML
        question_text = re.sub(r'<[^>]+>', '', question).strip()
        answer_text = re.sub(r'<[^>]+>', '', answer).strip()

        # Créer les clés
        q_key = f"review.{tool_name}.faq.q{faq_num}"
        a_key = f"review.{tool_name}.faq.a{faq_num}"

        faqs[q_key] = question_text
        faqs[a_key] = answer_text

        faq_num += 1

    print(f"Trouve {len(matches)} FAQs dans {html_file}")
    return faqs

def create_en_json(tool_name, faqs):
    """Crée le fichier -en.json"""
    output_file = f"GenuisNet.ai/pages/reviews/seo/{tool_name}-faqs-en.json"

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(faqs, f, indent=2, ensure_ascii=False)

    print(f"Cree: {output_file}")
    return output_file

# Extraire les FAQs pour NeuronWriter
neuron_faqs = extract_faqs_from_html(
    "GenuisNet.ai/pages/reviews/seo/neuronwriter.html",
    "neuronwriter"
)

if neuron_faqs:
    create_en_json("neuronwriter", neuron_faqs)

# Extraire les FAQs pour Scalenut
scalenut_faqs = extract_faqs_from_html(
    "GenuisNet.ai/pages/reviews/seo/scalenut.html",
    "scalenut"
)

if scalenut_faqs:
    create_en_json("scalenut", scalenut_faqs)

print("\nExtraction terminee!")
