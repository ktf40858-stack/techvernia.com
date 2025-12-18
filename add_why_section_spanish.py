#!/usr/bin/env python3
"""
Script pour ajouter les traductions espagnoles manquantes pour la section Why
"""

def add_why_section_spanish():
    """Ajoute les traductions espagnoles pour la section Why"""

    file_path = "GenuisNet.ai/js/i18n.js"

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Trouver la section espagnole (es:)
    es_start = content.find('es: {', content.find('// ==================== SPANISH ===================='))
    if es_start == -1:
        es_start = content.find('es: {')

    de_start = content.find('// ==================== GERMAN ====================')

    if es_start == -1 or de_start == -1:
        print("❌ Section espagnole non trouvée")
        return

    before_es = content[:es_start]
    es_section = content[es_start:de_start]
    after_es = content[de_start:]

    # Remplacements
    replacements = {
        '"section.why-genuisnetai": "Why GenuisNet.ai?",':
            '"section.why-genuisnetai": "¿Por qué GenuisNet.ai?",',

        '"section.your-trusted-companion-in-the-": "Your trusted companion in the AI journey",':
            '"section.your-trusted-companion-in-the-": "Tu compañero de confianza en el viaje de la IA",',
    }

    count = 0
    for old, new in replacements.items():
        if old in es_section:
            es_section = es_section.replace(old, new, 1)
            count += 1
            print(f"✅ Traduction ajoutée: {old.split('\"')[1]}")

    # Reconstruire le contenu
    content = before_es + es_section + after_es

    # Écrire les modifications
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"\n✅ {count} traductions ajoutées pour la section Why!")
    else:
        print("\nℹ️  Aucune modification nécessaire")

if __name__ == "__main__":
    add_why_section_spanish()
