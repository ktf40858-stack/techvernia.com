#!/usr/bin/env python3
"""
Script pour ajouter les traductions des 10 catégories restantes dans i18n.js
"""

def add_remaining_translations():
    """Ajoute les traductions des 10 catégories restantes"""

    file_path = "GenuisNet.ai/js/i18n.js"

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Trouver où insérer dans la section EN (après medical)
    en_marker = '"cat.medical-card-desc": "Healthcare and diagnostic solutions",'

    if en_marker in content:
        en_additions = '''
        "cat.analytics-short": "AI Analytics & BI",
        "cat.analytics-card-desc": "Data insights and business intelligence",
        "cat.legal-short": "AI Legal & Compliance",
        "cat.legal-card-desc": "Legal research and contract analysis",
        "cat.customer-service-short": "AI Customer Service",
        "cat.customer-service-card-desc": "Support automation and chatbots",
        "cat.education-short": "AI Education & E-Learning",
        "cat.education-card-desc": "Learning platforms and tutoring",
        "cat.sales-short": "AI Sales & CRM",
        "cat.sales-card-desc": "Sales automation and forecasting",
        "cat.research-short": "AI Research & Academia",
        "cat.research-card-desc": "Academic research and literature review",
        "cat.hr-short": "AI HR & Recruiting",
        "cat.hr-card-desc": "Talent acquisition and HR automation",
        "cat.translation-short": "AI Translation & Localization",
        "cat.translation-card-desc": "Multilingual and localization tools",
        "cat.gaming-short": "AI Gaming & Entertainment",
        "cat.gaming-card-desc": "Game development and NPCs",
        "cat.quantum-short": "AI Quantum Computing",
        "cat.quantum-card-desc": "Quantum ML and optimization",'''

        content = content.replace(en_marker, en_marker + en_additions)
        print("✅ Ajouté: 10 catégories EN")

    # Trouver où insérer dans la section ES (après medical)
    es_marker = '"cat.medical-card-desc": "Soluciones de salud y diagnóstico",'

    if es_marker in content:
        es_additions = '''
        "cat.analytics-short": "IA Análisis y BI",
        "cat.analytics-card-desc": "Información de datos e inteligencia empresarial",
        "cat.legal-short": "IA Legal y Cumplimiento",
        "cat.legal-card-desc": "Investigación legal y análisis de contratos",
        "cat.customer-service-short": "IA Servicio al Cliente",
        "cat.customer-service-card-desc": "Automatización de soporte y chatbots",
        "cat.education-short": "IA Educación y E-Learning",
        "cat.education-card-desc": "Plataformas de aprendizaje y tutoría",
        "cat.sales-short": "IA Ventas y CRM",
        "cat.sales-card-desc": "Automatización de ventas y pronósticos",
        "cat.research-short": "IA Investigación y Academia",
        "cat.research-card-desc": "Investigación académica y revisión de literatura",
        "cat.hr-short": "IA RRHH y Reclutamiento",
        "cat.hr-card-desc": "Adquisición de talento y automatización de RRHH",
        "cat.translation-short": "IA Traducción y Localización",
        "cat.translation-card-desc": "Herramientas multilingües y de localización",
        "cat.gaming-short": "IA Juegos y Entretenimiento",
        "cat.gaming-card-desc": "Desarrollo de juegos y NPCs",
        "cat.quantum-short": "IA Computación Cuántica",
        "cat.quantum-card-desc": "ML cuántico y optimización",'''

        content = content.replace(es_marker, es_marker + es_additions)
        print("✅ Ajouté: 10 catégories ES")

    # Écrire les modifications
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print("\n✅ Toutes les traductions des 10 catégories restantes ont été ajoutées!")
    else:
        print("\nℹ️  Aucune modification nécessaire")

if __name__ == "__main__":
    add_remaining_translations()
