import os
import re

js_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\js"

translation_tools = {
    "deepl-pro": "DeepL Pro",
    "google-translate-ai": "Google Translate AI",
    "lilt": "Lilt",
    "lokalise": "Lokalise",
    "microsoft-translator": "Microsoft Translator",
    "modernmt": "ModernMT",
    "phrase": "Phrase",
    "smartling": "Smartling",
    "systran": "SYSTRAN",
    "unbabel": "Unbabel"
}

# Mapping English values to German translations
value_replacements_de = {
    "DeepL Pro Excels For:": "DeepL Pro eignet sich hervorragend für:",
    "Google Translate AI Excels For:": "Google Translate AI eignet sich hervorragend für:",
    "Lilt Excels For:": "Lilt eignet sich hervorragend für:",
    "Lokalise Excels For:": "Lokalise eignet sich hervorragend für:",
    "Microsoft Translator Excels For:": "Microsoft Translator eignet sich hervorragend für:",
    "ModernMT Excels For:": "ModernMT eignet sich hervorragend für:",
    "Phrase Excels For:": "Phrase eignet sich hervorragend für:",
    "Smartling Excels For:": "Smartling eignet sich hervorragend für:",
    "SYSTRAN Excels For:": "SYSTRAN eignet sich hervorragend für:",
    "Unbabel Excels For:": "Unbabel eignet sich hervorragend für:",

    "Enterprise Teams: Large organizations requiring scalable translation solutions with advanced features": "Enterprise-Teams: Große Organisationen, die skalierbare Übersetzungslösungen mit erweiterten Funktionen benötigen",
    "Growing Startups: Fast-moving companies that need flexible AI-powered automation": "Wachsende Startups: Schnelllebige Unternehmen, die flexible KI-gestützte Automatisierung benötigen",
    "Remote Teams: Distributed teams requiring real-time collaboration and communication": "Remote-Teams: Verteilte Teams, die Echtzeit-Zusammenarbeit und Kommunikation benötigen",
    "Data-Driven Organizations: Companies leveraging analytics for strategic decision-making": "Datengesteuerte Organisationen: Unternehmen, die Analysen für strategische Entscheidungen nutzen",
    "Compliance-Heavy Industries: Regulated sectors requiring enterprise-grade security and compliance": "Compliance-intensive Branchen: Regulierte Sektoren, die Enterprise-Sicherheit und Compliance benötigen",

    "May Not Be Ideal For:": "Möglicherweise nicht ideal für:",
    "Very small businesses with minimal translation needs": "Sehr kleine Unternehmen mit minimalen Übersetzungsbedürfnissen",
    "Organizations requiring extensive offline functionality": "Organisationen, die umfangreiche Offline-Funktionalität benötigen",
    "Teams with very limited technical expertise": "Teams mit sehr begrenzter technischer Expertise",
}

value_replacements_es = {
    "DeepL Pro Excels For:": "DeepL Pro Destaca Para:",
    "Google Translate AI Excels For:": "Google Translate AI Destaca Para:",
    "Lilt Excels For:": "Lilt Destaca Para:",
    "Lokalise Excels For:": "Lokalise Destaca Para:",
    "Microsoft Translator Excels For:": "Microsoft Translator Destaca Para:",
    "ModernMT Excels For:": "ModernMT Destaca Para:",
    "Phrase Excels For:": "Phrase Destaca Para:",
    "Smartling Excels For:": "Smartling Destaca Para:",
    "SYSTRAN Excels For:": "SYSTRAN Destaca Para:",
    "Unbabel Excels For:": "Unbabel Destaca Para:",

    "Enterprise Teams: Large organizations requiring scalable translation solutions with advanced features": "Equipos Empresariales: Grandes organizaciones que requieren soluciones de traducción escalables con funciones avanzadas",
    "Growing Startups: Fast-moving companies that need flexible AI-powered automation": "Startups en Crecimiento: Empresas ágiles que necesitan automatización impulsada por IA flexible",
    "Remote Teams: Distributed teams requiring real-time collaboration and communication": "Equipos Remotos: Equipos distribuidos que requieren colaboración y comunicación en tiempo real",
    "Data-Driven Organizations: Companies leveraging analytics for strategic decision-making": "Organizaciones Orientadas a Datos: Empresas que aprovechan análisis para toma de decisiones estratégicas",
    "Compliance-Heavy Industries: Regulated sectors requiring enterprise-grade security and compliance": "Industrias con Alta Compliance: Sectores regulados que requieren seguridad y cumplimiento de nivel empresarial",

    "May Not Be Ideal For:": "Puede No Ser Ideal Para:",
    "Very small businesses with minimal translation needs": "Empresas muy pequeñas con necesidades mínimas de traducción",
    "Organizations requiring extensive offline functionality": "Organizaciones que requieren funcionalidad offline extensa",
    "Teams with very limited technical expertise": "Equipos con experiencia técnica muy limitada",
}

value_replacements_fr = {
    "DeepL Pro Excels For:": "DeepL Pro Excelle Pour:",
    "Google Translate AI Excels For:": "Google Translate AI Excelle Pour:",
    "Lilt Excels For:": "Lilt Excelle Pour:",
    "Lokalise Excels For:": "Lokalise Excelle Pour:",
    "Microsoft Translator Excels For:": "Microsoft Translator Excelle Pour:",
    "ModernMT Excels For:": "ModernMT Excelle Pour:",
    "Phrase Excels For:": "Phrase Excelle Pour:",
    "Smartling Excels For:": "Smartling Excelle Pour:",
    "SYSTRAN Excels For:": "SYSTRAN Excelle Pour:",
    "Unbabel Excels For:": "Unbabel Excelle Pour:",

    "Enterprise Teams: Large organizations requiring scalable translation solutions with advanced features": "Équipes d'Entreprise: Grandes organisations nécessitant des solutions de traduction évolutives avec fonctionnalités avancées",
    "Growing Startups: Fast-moving companies that need flexible AI-powered automation": "Startups en Croissance: Entreprises agiles nécessitant une automatisation IA flexible",
    "Remote Teams: Distributed teams requiring real-time collaboration and communication": "Équipes Distantes: Équipes distribuées nécessitant collaboration et communication en temps réel",
    "Data-Driven Organizations: Companies leveraging analytics for strategic decision-making": "Organisations Axées sur les Données: Entreprises exploitant l'analyse pour la prise de décisions stratégiques",
    "Compliance-Heavy Industries: Regulated sectors requiring enterprise-grade security and compliance": "Secteurs à Forte Conformité: Secteurs réglementés nécessitant sécurité et conformité de niveau entreprise",

    "May Not Be Ideal For:": "Peut Ne Pas Convenir Pour:",
    "Very small businesses with minimal translation needs": "Très petites entreprises avec besoins minimaux en traduction",
    "Organizations requiring extensive offline functionality": "Organisations nécessitant des fonctionnalités hors ligne étendues",
    "Teams with very limited technical expertise": "Équipes avec expertise technique très limitée",
}

def fix_use_case_values(tool_key, tool_name):
    """Fix use case values by replacing English with correct translations"""

    js_file = os.path.join(js_dir, f"{tool_key}-i18n.js")

    if not os.path.exists(js_file):
        return False

    with open(js_file, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    replacements_made = 0

    # Apply German replacements
    for eng, de in value_replacements_de.items():
        old = f'": "{eng}"'
        new = f'": "{de}"'
        before = content.count(old)
        content = content.replace(old, new)
        after = content.count(old)
        replacements_made += (before - after)

    # Apply Spanish replacements
    for eng, es in value_replacements_es.items():
        old = f'": "{eng}"'
        new = f'": "{es}"'
        before = content.count(old)
        content = content.replace(old, new)
        after = content.count(old)
        replacements_made += (before - after)

    # Apply French replacements
    for eng, fr in value_replacements_fr.items():
        old = f'": "{eng}"'
        new = f'": "{fr}"'
        before = content.count(old)
        content = content.replace(old, new)
        after = content.count(old)
        replacements_made += (before - after)

    if content != original_content:
        with open(js_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  [+] Made {replacements_made} replacements")
        return True

    return False

print("=" * 70)
print("FIXING USE CASE VALUE TRANSLATIONS")
print("=" * 70)

fixed_count = 0

for tool_key, tool_name in translation_tools.items():
    print(f"\n{tool_name}:")
    if fix_use_case_values(tool_key, tool_name):
        fixed_count += 1
    else:
        print(f"  [OK] No changes needed")

print("\n" + "=" * 70)
print(f"COMPLETE: {fixed_count}/10 tools updated")
print("=" * 70)
print("\nUse case sections now have correct translations!")
print("=" * 70)
