#!/usr/bin/env python3
"""
Ajouter les traductions pour les pages de reviews
Ce script ajoute les clés de traduction communes pour les reviews
"""

import re

# Nouvelles traductions à ajouter dans i18n.js
REVIEW_TRANSLATIONS = {
    "en": '''
        // Review Pages
        "review.rating": "Rating",
        "review.overall": "Overall Rating",
        "review.features": "Features",
        "review.pricing": "Pricing",
        "review.proscons": "Pros & Cons",
        "review.pros": "Pros",
        "review.cons": "Cons",
        "review.alternatives": "Alternatives",
        "review.verdict": "Final Verdict",
        "review.published": "Published",
        "review.updated": "Updated",
        "review.by": "By",
        "review.readTime": "min read",
        "review.overview": "Overview",
        "review.keyFeatures": "Key Features",
        "review.whoIsItFor": "Who Is It For?",
        "review.comparison": "Comparison",
        "review.faq": "Frequently Asked Questions",
        "review.getStarted": "Getting Started",
        "review.summary": "Summary"''',

    "fr": '''
        // Review Pages
        "review.rating": "Note",
        "review.overall": "Note Globale",
        "review.features": "Fonctionnalités",
        "review.pricing": "Tarifs",
        "review.proscons": "Avantages & Inconvénients",
        "review.pros": "Avantages",
        "review.cons": "Inconvénients",
        "review.alternatives": "Alternatives",
        "review.verdict": "Verdict Final",
        "review.published": "Publié le",
        "review.updated": "Mis à jour le",
        "review.by": "Par",
        "review.readTime": "min de lecture",
        "review.overview": "Aperçu",
        "review.keyFeatures": "Fonctionnalités Clés",
        "review.whoIsItFor": "Pour Qui?",
        "review.comparison": "Comparaison",
        "review.faq": "Questions Fréquentes",
        "review.getStarted": "Commencer",
        "review.summary": "Résumé"''',

    "es": '''
        // Review Pages
        "review.rating": "Calificación",
        "review.overall": "Calificación General",
        "review.features": "Características",
        "review.pricing": "Precios",
        "review.proscons": "Pros y Contras",
        "review.pros": "Pros",
        "review.cons": "Contras",
        "review.alternatives": "Alternativas",
        "review.verdict": "Veredicto Final",
        "review.published": "Publicado",
        "review.updated": "Actualizado",
        "review.by": "Por",
        "review.readTime": "min de lectura",
        "review.overview": "Descripción General",
        "review.keyFeatures": "Características Clave",
        "review.whoIsItFor": "¿Para Quién Es?",
        "review.comparison": "Comparación",
        "review.faq": "Preguntas Frecuentes",
        "review.getStarted": "Empezar",
        "review.summary": "Resumen"'''
}

def add_translations_to_i18n():
    """Ajoute les traductions de review dans i18n.js"""

    print("="*70)
    print("Ajout des Traductions pour les Pages de Review")
    print("="*70)

    i18n_file = 'js/i18n.js'

    with open(i18n_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Vérifier si déjà ajouté
    if '"review.rating"' in content:
        print("\n✅ Les traductions de review existent déjà!")
        return True

    # Ajouter pour chaque langue
    for lang, translations in REVIEW_TRANSLATIONS.items():
        # Trouver où insérer (après country.us de chaque langue)
        pattern = f'("{lang}".*?"country.us":[^,]*,)'

        if re.search(pattern, content, re.DOTALL):
            content = re.sub(
                pattern,
                f'\\1{translations},',
                content,
                flags=re.DOTALL
            )
            print(f"✅ Ajouté pour {lang.upper()}")

    # Sauvegarder
    with open(i18n_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\n💾 Traductions sauvegardées dans {i18n_file}")
    print("\n📝 Nouvelles clés disponibles:")
    print("  - review.rating, review.features, review.pricing")
    print("  - review.pros, review.cons, review.alternatives")
    print("  - Et 10+ autres clés!")

    return True

if __name__ == '__main__':
    add_translations_to_i18n()

    print("\n" + "="*70)
    print("✅ TERMINÉ!")
    print("="*70)
    print("\n📋 Prochaine étape:")
    print("  Utilisez ces clés dans vos pages de review:")
    print('  <h2 data-i18n="review.features">Features</h2>')
    print('  <h3 data-i18n="review.pros">Pros</h3>')
