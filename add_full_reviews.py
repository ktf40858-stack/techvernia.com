#!/usr/bin/env python3
"""
Script pour ajouter les descriptions .full pour les 12 catégories manquantes
"""

def add_full_reviews():
    """Ajoute les descriptions complètes (.full) pour toutes les catégories"""

    file_path = "GenuisNet.ai/js/i18n.js"

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # === SECTION ANGLAISE ===
    # Trouver où insérer dans la section EN (après cybersecurity.full)
    en_marker = '"cat.cybersecurity.full": "Darktrace, CrowdStrike, SentinelOne and more AI-powered security tools.",'

    if en_marker in content:
        en_full_additions = '''
        "cat.architecture.full": "ArchiCAD AI, Hypar, Spacemaker and more building design tools.",
        "cat.medical.full": "IBM Watson Health, PathAI, Tempus and more healthcare AI solutions.",
        "cat.analytics.full": "Tableau AI, Power BI Copilot, ThoughtSpot and more business intelligence tools.",
        "cat.legal.full": "LexisNexis AI, Casetext, Harvey AI and more legal research tools.",
        "cat.customer-service.full": "Zendesk AI, Intercom, Ada and more customer support automation tools.",
        "cat.education.full": "Khan Academy AI, Duolingo Max, Coursera Coach and more learning platforms.",
        "cat.sales.full": "Gong, Clari, Salesforce Einstein and more sales enablement tools.",
        "cat.research.full": "Elicit, Consensus, Scholarcy and more academic research tools.",
        "cat.hr.full": "HireVue, Pymetrics, Eightfold AI and more HR automation tools.",
        "cat.translation.full": "DeepL, Google Translate AI, Unbabel and more translation tools.",
        "cat.gaming.full": "Inworld AI, Scenario, Charisma AI and more game development tools.",
        "cat.quantum.full": "Zapata Computing, Xanadu, IBM Quantum and more quantum ML platforms.",'''

        content = content.replace(en_marker, en_marker + en_full_additions)
        print("✅ Ajouté: 12 descriptions .full (EN)")

    # === SECTION FRANÇAISE ===
    # Trouver la section FR (après cybersecurity.full français)
    fr_marker = '"cat.cybersecurity.full": "Darktrace, CrowdStrike, SentinelOne et autres outils de sécurité alimentés par l\'IA.",'

    if fr_marker in content:
        fr_full_additions = '''
        "cat.architecture.full": "ArchiCAD AI, Hypar, Spacemaker et autres outils de conception architecturale.",
        "cat.medical.full": "IBM Watson Health, PathAI, Tempus et autres solutions IA pour la santé.",
        "cat.analytics.full": "Tableau AI, Power BI Copilot, ThoughtSpot et autres outils d'intelligence d'affaires.",
        "cat.legal.full": "LexisNexis AI, Casetext, Harvey AI et autres outils de recherche juridique.",
        "cat.customer-service.full": "Zendesk AI, Intercom, Ada et autres outils d'automatisation du support client.",
        "cat.education.full": "Khan Academy AI, Duolingo Max, Coursera Coach et autres plateformes d'apprentissage.",
        "cat.sales.full": "Gong, Clari, Salesforce Einstein et autres outils de vente.",
        "cat.research.full": "Elicit, Consensus, Scholarcy et autres outils de recherche académique.",
        "cat.hr.full": "HireVue, Pymetrics, Eightfold AI et autres outils d'automatisation RH.",
        "cat.translation.full": "DeepL, Google Translate AI, Unbabel et autres outils de traduction.",
        "cat.gaming.full": "Inworld AI, Scenario, Charisma AI et autres outils de développement de jeux.",
        "cat.quantum.full": "Zapata Computing, Xanadu, IBM Quantum et autres plateformes de ML quantique.",'''

        content = content.replace(fr_marker, fr_marker + fr_full_additions)
        print("✅ Ajouté: 12 descriptions .full (FR)")

    # === SECTION ESPAGNOLE ===
    # Trouver la section ES (après cybersecurity.full espagnol)
    es_marker = '"cat.cybersecurity.full": "Darktrace, CrowdStrike, SentinelOne y más herramientas de seguridad impulsadas por IA.",'

    if es_marker in content:
        es_full_additions = '''
        "cat.architecture.full": "ArchiCAD AI, Hypar, Spacemaker y más herramientas de diseño arquitectónico.",
        "cat.medical.full": "IBM Watson Health, PathAI, Tempus y más soluciones de IA para la salud.",
        "cat.analytics.full": "Tableau AI, Power BI Copilot, ThoughtSpot y más herramientas de inteligencia empresarial.",
        "cat.legal.full": "LexisNexis AI, Casetext, Harvey AI y más herramientas de investigación legal.",
        "cat.customer-service.full": "Zendesk AI, Intercom, Ada y más herramientas de automatización de soporte.",
        "cat.education.full": "Khan Academy AI, Duolingo Max, Coursera Coach y más plataformas de aprendizaje.",
        "cat.sales.full": "Gong, Clari, Salesforce Einstein y más herramientas de ventas.",
        "cat.research.full": "Elicit, Consensus, Scholarcy y más herramientas de investigación académica.",
        "cat.hr.full": "HireVue, Pymetrics, Eightfold AI y más herramientas de automatización de RRHH.",
        "cat.translation.full": "DeepL, Google Translate AI, Unbabel y más herramientas de traducción.",
        "cat.gaming.full": "Inworld AI, Scenario, Charisma AI y más herramientas de desarrollo de juegos.",
        "cat.quantum.full": "Zapata Computing, Xanadu, IBM Quantum y más plataformas de ML cuántico.",'''

        content = content.replace(es_marker, es_marker + es_full_additions)
        print("✅ Ajouté: 12 descriptions .full (ES)")

    # Écrire les modifications
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print("\n✅ Toutes les descriptions complètes (.full) ont été ajoutées!")
        print("📊 Total: 12 catégories × 3 langues = 36 nouvelles traductions")
    else:
        print("\nℹ️  Aucune modification nécessaire")

if __name__ == "__main__":
    add_full_reviews()
