#!/usr/bin/env python3
"""
Script pour traduire les 130 clés de contenu Adobe Firefly
"""
import json
import sys

# Dictionnaire de traductions pour les termes techniques courants
TECH_TERMS = {
    'en': {
        'Adobe Firefly': 'Adobe Firefly',
        'AI': 'AI',
        'Creative Cloud': 'Creative Cloud',
        'Photoshop': 'Photoshop',
        'Illustrator': 'Illustrator',
        'DALL-E': 'DALL-E',
        'Midjourney': 'Midjourney',
    }
}

# Traductions manuelles pour les phrases clés (exemples)
MANUAL_TRANSLATIONS = {
    'es': {
        'Adobe Firefly represents Adobe\'s strategic entry into generative AI, designed specifically for creative professionals who demand commercial safety and seamless integration with existing workflows. Unlike standalone AI generators, Firefly is deeply embedded within Adobe\'s Creative Cloud suite, bringing AI capabilities directly into Photoshop, Illustrator, and Express.':
        'Adobe Firefly representa la entrada estratégica de Adobe en la IA generativa, diseñada específicamente para profesionales creativos que exigen seguridad comercial e integración perfecta con los flujos de trabajo existentes. A diferencia de los generadores de IA independientes, Firefly está profundamente integrado en el conjunto Creative Cloud de Adobe, llevando las capacidades de IA directamente a Photoshop, Illustrator y Express.',

        'What sets Firefly apart is its training approach. Adobe trained Firefly exclusively on licensed content from Adobe Stock, public domain works, and expired copyright materials, ensuring every generated image is commercially safe. This makes it the go-to choice for businesses and professionals who can\'t risk copyright issues with their AI-generated content.':
        'Lo que distingue a Firefly es su enfoque de entrenamiento. Adobe entrenó a Firefly exclusivamente con contenido licenciado de Adobe Stock, obras de dominio público y materiales con derechos de autor vencidos, garantizando que cada imagen generada sea comercialmente segura. Esto lo convierte en la opción preferida para empresas y profesionales que no pueden arriesgar problemas de derechos de autor con su contenido generado por IA.',
    },
    'fr': {
        'Adobe Firefly represents Adobe\'s strategic entry into generative AI, designed specifically for creative professionals who demand commercial safety and seamless integration with existing workflows. Unlike standalone AI generators, Firefly is deeply embedded within Adobe\'s Creative Cloud suite, bringing AI capabilities directly into Photoshop, Illustrator, and Express.':
        'Adobe Firefly représente l\'entrée stratégique d\'Adobe dans l\'IA générative, conçue spécifiquement pour les professionnels créatifs qui exigent la sécurité commerciale et une intégration transparente avec les flux de travail existants. Contrairement aux générateurs d\'IA autonomes, Firefly est profondément intégré dans la suite Creative Cloud d\'Adobe, apportant les capacités d\'IA directement dans Photoshop, Illustrator et Express.',

        'What sets Firefly apart is its training approach. Adobe trained Firefly exclusively on licensed content from Adobe Stock, public domain works, and expired copyright materials, ensuring every generated image is commercially safe. This makes it the go-to choice for businesses and professionals who can\'t risk copyright issues with their AI-generated content.':
        'Ce qui distingue Firefly est son approche d\'entraînement. Adobe a entraîné Firefly exclusivement sur du contenu sous licence d\'Adobe Stock, des œuvres du domaine public et des matériaux dont les droits d\'auteur ont expiré, garantissant que chaque image générée est commercialement sûre. Cela en fait le choix privilégié pour les entreprises et les professionnels qui ne peuvent pas risquer de problèmes de droits d\'auteur avec leur contenu généré par IA.',
    },
    'de': {
        'Adobe Firefly represents Adobe\'s strategic entry into generative AI, designed specifically for creative professionals who demand commercial safety and seamless integration with existing workflows. Unlike standalone AI generators, Firefly is deeply embedded within Adobe\'s Creative Cloud suite, bringing AI capabilities directly into Photoshop, Illustrator, and Express.':
        'Adobe Firefly stellt Adobes strategischen Einstieg in generative KI dar, speziell entwickelt für kreative Profis, die kommerzielle Sicherheit und nahtlose Integration in bestehende Workflows verlangen. Im Gegensatz zu eigenständigen KI-Generatoren ist Firefly tief in die Adobe Creative Cloud Suite eingebettet und bringt KI-Funktionen direkt in Photoshop, Illustrator und Express.',

        'What sets Firefly apart is its training approach. Adobe trained Firefly exclusively on licensed content from Adobe Stock, public domain works, and expired copyright materials, ensuring every generated image is commercially safe. This makes it the go-to choice for businesses and professionals who can\'t risk copyright issues with their AI-generated content.':
        'Was Firefly auszeichnet, ist sein Trainingsansatz. Adobe hat Firefly ausschließlich mit lizenzierten Inhalten von Adobe Stock, gemeinfreien Werken und abgelaufenen urheberrechtlich geschützten Materialien trainiert, wodurch sichergestellt wird, dass jedes generierte Bild kommerziell sicher ist. Dies macht es zur bevorzugten Wahl für Unternehmen und Fachleute, die keine Urheberrechtsprobleme mit ihren KI-generierten Inhalten riskieren können.',
    }
}

def translate_with_api(text, target_lang):
    """
    Traduction via API (DeepL, Google, ou OpenAI)
    Pour l'instant, retourne une traduction de démonstration
    """
    # Si on a une traduction manuelle, on l'utilise
    if target_lang in MANUAL_TRANSLATIONS and text in MANUAL_TRANSLATIONS[target_lang]:
        return MANUAL_TRANSLATIONS[target_lang][text]

    # Sinon, on retourne une version avec [LANG] pour montrer que ça doit être traduit
    return f"[{target_lang.upper()}] {text}"

def main():
    # Charger les clés à traduire
    print("Chargement des clés à traduire...")
    with open('image_content_keys_to_translate.json', 'r', encoding='utf-8') as f:
        keys_to_translate = json.load(f)

    print(f"✓ {len(keys_to_translate)} clés à traduire")
    print()

    # Langues cibles
    languages = {
        'es': 'Espagnol',
        'fr': 'Français',
        'de': 'Allemand',
        'ar': 'Arabe',
        'pt': 'Portugais',
        'hi': 'Hindi',
        'ja': 'Japonais',
        'ko': 'Coréen',
        'zh': 'Chinois'
    }

    # Pour chaque langue, traduire et intégrer
    for lang_code, lang_name in languages.items():
        print(f"Traduction en {lang_name} ({lang_code})...")

        # Charger le fichier de traduction existant
        translation_file = f'all_full_translations_{lang_code}.json'
        try:
            with open(translation_file, 'r', encoding='utf-8') as f:
                translations = json.load(f)
        except FileNotFoundError:
            translations = {}

        # Traduire chaque clé
        translated_count = 0
        for key, en_text in keys_to_translate.items():
            # Traduire le texte
            translated_text = translate_with_api(en_text, lang_code)

            # Ajouter/mettre à jour dans le dictionnaire
            translations[key] = translated_text
            translated_count += 1

        # Sauvegarder
        with open(translation_file, 'w', encoding='utf-8') as f:
            json.dump(translations, f, ensure_ascii=False, indent=2)

        print(f"✓ {translated_count} clés traduites et sauvegardées dans {translation_file}")

    print()
    print("=" * 80)
    print("TRADUCTION TERMINÉE!")
    print("=" * 80)
    print()
    print("NOTE: Les traductions marquées [LANG] sont des placeholders.")
    print("Pour des vraies traductions, vous devez:")
    print("1. Obtenir une clé API (DeepL, Google Translate, ou OpenAI)")
    print("2. Modifier ce script pour utiliser l'API")
    print()

if __name__ == '__main__':
    main()
