#!/usr/bin/env python3
"""
Add Missing Translations to i18n.js
This script adds the missing translation keys needed for full site translation
"""

# New translations to add (will be inserted before the closing brace of each language)
NEW_TRANSLATIONS = {
    "en": '''
        // Additional Stats & Labels
        "stats.toolsReviewed": "Tools Reviewed",
        "stats.avgRating": "Avg Rating",

        // Additional Buttons
        "btn.fullReview": "Full Review",
        "btn.viewReview": "View Review",

        // Countries
        "country.us": "United States",
        "country.uk": "United Kingdom",
        "country.canada": "Canada",
        "country.germany": "Germany",
        "country.france": "France",
        "country.japan": "Japan",
        "country.china": "China",

        // Common Terms
        "common.tools": "Tools",
        "common.aiTools": "AI Tools",
        "common.reviews": "Reviews",
        "common.rating": "Rating",
        "common.pricing": "Pricing",
        "common.features": "Features"''',

    "fr": '''
        // Additional Stats & Labels
        "stats.toolsReviewed": "Outils Analysés",
        "stats.avgRating": "Note Moyenne",

        // Additional Buttons
        "btn.fullReview": "Avis Complet",
        "btn.viewReview": "Voir l'Avis",

        // Countries
        "country.us": "États-Unis",
        "country.uk": "Royaume-Uni",
        "country.canada": "Canada",
        "country.germany": "Allemagne",
        "country.france": "France",
        "country.japan": "Japon",
        "country.china": "Chine",

        // Common Terms
        "common.tools": "Outils",
        "common.aiTools": "Outils IA",
        "common.reviews": "Avis",
        "common.rating": "Note",
        "common.pricing": "Tarifs",
        "common.features": "Fonctionnalités"''',

    "es": '''
        // Additional Stats & Labels
        "stats.toolsReviewed": "Herramientas Revisadas",
        "stats.avgRating": "Calificación Promedio",

        // Additional Buttons
        "btn.fullReview": "Reseña Completa",
        "btn.viewReview": "Ver Reseña",

        // Countries
        "country.us": "Estados Unidos",
        "country.uk": "Reino Unido",
        "country.canada": "Canadá",
        "country.germany": "Alemania",
        "country.france": "Francia",
        "country.japan": "Japón",
        "country.china": "China",

        // Common Terms
        "common.tools": "Herramientas",
        "common.aiTools": "Herramientas IA",
        "common.reviews": "Reseñas",
        "common.rating": "Calificación",
        "common.pricing": "Precios",
        "common.features": "Características"''',

    "de": '''
        // Additional Stats & Labels
        "stats.toolsReviewed": "Bewertete Tools",
        "stats.avgRating": "Durchschnittliche Bewertung",

        // Additional Buttons
        "btn.fullReview": "Vollständige Bewertung",
        "btn.viewReview": "Bewertung Ansehen",

        // Countries
        "country.us": "Vereinigte Staaten",
        "country.uk": "Vereinigtes Königreich",
        "country.canada": "Kanada",
        "country.germany": "Deutschland",
        "country.france": "Frankreich",
        "country.japan": "Japan",
        "country.china": "China",

        // Common Terms
        "common.tools": "Werkzeuge",
        "common.aiTools": "KI-Tools",
        "common.reviews": "Bewertungen",
        "common.rating": "Bewertung",
        "common.pricing": "Preise",
        "common.features": "Funktionen"''',

    "pt": '''
        // Additional Stats & Labels
        "stats.toolsReviewed": "Ferramentas Avaliadas",
        "stats.avgRating": "Classificação Média",

        // Additional Buttons
        "btn.fullReview": "Avaliação Completa",
        "btn.viewReview": "Ver Avaliação",

        // Countries
        "country.us": "Estados Unidos",
        "country.uk": "Reino Unido",
        "country.canada": "Canadá",
        "country.germany": "Alemanha",
        "country.france": "França",
        "country.japan": "Japão",
        "country.china": "China",

        // Common Terms
        "common.tools": "Ferramentas",
        "common.aiTools": "Ferramentas IA",
        "common.reviews": "Avaliações",
        "common.rating": "Classificação",
        "common.pricing": "Preços",
        "common.features": "Recursos"'''
}

def add_translations():
    """Add missing translations to i18n.js"""
    print("=" * 70)
    print("Adding Missing Translations to i18n.js")
    print("=" * 70)

    i18n_file = 'js/i18n.js'

    try:
        with open(i18n_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if translations already exist
        if '"stats.toolsReviewed"' in content:
            print("\n✅ Translations already exist in i18n.js")
            return True

        original_content = content

        # Add translations for each language
        for lang_code, translations in NEW_TRANSLATIONS.items():
            # Find the closing brace of this language section
            # Look for pattern: language_code: { ... },
            pattern = f'({lang_code}:\\s*{{[^}}]*"filter\\.[^"]*":[^,]*,)'

            if re.search(pattern, content, re.DOTALL):
                # Insert new translations before the last item
                content = re.sub(
                    pattern,
                    f'\\1{translations},',
                    content,
                    flags=re.DOTALL
                )
                print(f"✅ Added translations for {lang_code.upper()}")

        # Save the modified file
        with open(i18n_file, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"\n💾 Saved translations to {i18n_file}")
        print("=" * 70)
        return True

    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    import re
    add_translations()
