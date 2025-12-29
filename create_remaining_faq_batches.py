import json
import os

# Les 3 outils restants
tools = ['neuronwriter', 'scalenut', 'surfer-seo']

# Langues cibles
languages = ['es', 'fr', 'de', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']

def create_batches_for_tool(tool_name):
    """Crée les 3 fichiers batch pour un outil"""
    en_file = f"GenuisNet.ai/pages/reviews/seo/{tool_name}-faqs-en.json"

    if not os.path.exists(en_file):
        print(f"Fichier {en_file} non trouve")
        return

    with open(en_file, 'r', encoding='utf-8') as f:
        en_data = json.load(f)

    # Diviser les clés en 3 batches (3 langues par batch)
    batch1_langs = languages[0:3]  # es, fr, de
    batch2_langs = languages[3:6]  # pt, zh, ja
    batch3_langs = languages[6:9]  # ko, ar, hi

    batches = [
        (1, batch1_langs),
        (2, batch2_langs),
        (3, batch3_langs)
    ]

    for batch_num, langs in batches:
        batch_data = {}

        for lang in langs:
            batch_data[lang] = {}
            for key in en_data.keys():
                batch_data[lang][key] = en_data[key]

        # Sauvegarder le fichier batch
        output_file = f"GenuisNet.ai/pages/reviews/seo/{tool_name}-faqs-batch{batch_num}.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(batch_data, f, indent=2, ensure_ascii=False)

        print(f"Cree: {output_file} avec langues {langs}")

# Créer les batches pour les 3 outils
for tool in tools:
    print(f"\n=== {tool.upper()} ===")
    create_batches_for_tool(tool)

print("\n✓ Tous les fichiers batch ont ete crees!")
print("\nProchaine etape: Envoyer ces fichiers a l'API de traduction")
print("Fichiers a traduire:")
for tool in tools:
    for i in range(1, 4):
        print(f"  - GenuisNet.ai/pages/reviews/seo/{tool}-faqs-batch{i}.json")
