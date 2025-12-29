#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Rebuild Translation i18n files based on actual HTML keys
Extracts English content from HTML and generates proper German translations
"""

import os
import re
import json
from bs4 import BeautifulSoup

# Base directory
base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
pages_dir = os.path.join(base_dir, "pages", "reviews", "translation")
js_dir = os.path.join(base_dir, "js")

# All 10 Translation tools
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

def extract_keys_and_content(html_path, tool_key):
    """Extract all data-i18n keys and their English content from HTML"""

    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    translations = {}

    # Find all elements with data-i18n attribute
    elements = soup.find_all(attrs={'data-i18n': True})

    for elem in elements:
        key = elem.get('data-i18n')

        # Only process keys for this tool
        if not key.startswith(f'review.{tool_key}'):
            continue

        # Get text content (remove extra whitespace)
        text = elem.get_text(strip=True)
        text = ' '.join(text.split())  # Normalize whitespace

        if text:
            translations[key] = text

    return translations

# Common German translations for translation tools
german_translations_map = {
    # Intro/Overview
    "is a powerful, feature-rich translation platform": "ist eine leistungsstarke, funktionsreiche Übersetzungsplattform",
    "is a comprehensive, AI-powered translation solution": "ist eine umfassende, KI-gestützte Übersetzungslösung",
    "is an innovative adaptive translation platform": "ist eine innovative adaptive Übersetzungsplattform",
    "is a collaborative translation management platform": "ist eine kollaborative Übersetzungsmanagement-Plattform",
    "is a robust enterprise translation service": "ist ein robuster Unternehmens-Übersetzungsdienst",
    "is a context-aware neural machine translation platform": "ist eine kontextbewusste neuronale maschinelle Übersetzungsplattform",
    "is a comprehensive localization platform": "ist eine umfassende Lokalisierungsplattform",
    "is a cloud-based translation management system": "ist ein cloudbasiertes Übersetzungsmanagementsystem",
    "is a pioneer in neural machine translation": "ist ein Pionier in der neuronalen maschinellen Übersetzung",
    "is a human-in-the-loop translation platform": "ist eine Human-in-the-Loop-Übersetzungsplattform",

    # Common phrases
    "The platform leverages advanced machine learning algorithms to automate complex tasks, provide intelligent insights, and enable teams to work more efficiently. With seamless integrations and an intuitive interface": "Die Plattform nutzt fortschrittliche Machine-Learning-Algorithmen zur Automatisierung komplexer Aufgaben, Bereitstellung intelligenter Erkenntnisse und effizienterer Teamarbeit. Mit nahtlosen Integrationen und intuitiver Benutzeroberfläche",

    "has become a trusted solution for organizations worldwide.": "ist zu einer vertrauenswürdigen Lösung für Organisationen weltweit geworden.",

    "Whether you're a small startup or a large enterprise": "Ob kleines Startup oder Großunternehmen",
    "scales to meet your needs while maintaining high performance and reliability.": "skaliert entsprechend Ihren Anforderungen bei hoher Leistung und Zuverlässigkeit.",

    # Features
    "Key Features": "Hauptmerkmale",
    "AI-Powered Automation": "KI-gestützte Automatisierung",
    "Intelligent automation that learns from your workflows and optimizes processes in real-time.": "Intelligente Automatisierung, die aus Ihren Workflows lernt und Prozesse in Echtzeit optimiert.",
    "Advanced Analytics": "Erweiterte Analytik",
    "Comprehensive analytics dashboard with actionable insights and predictive analytics.": "Umfassendes Analyse-Dashboard mit umsetzbaren Erkenntnissen und prädiktiven Analysen.",
    "Seamless Integrations": "Nahtlose Integrationen",
    "Connect with 100+ popular tools and platforms your team already uses.": "Verbindung mit über 100 beliebten Tools und Plattformen, die Ihr Team bereits nutzt.",
    "Enterprise Security": "Unternehmenssicherheit",
    "Bank-grade encryption, SSO, and compliance with SOC 2, GDPR, and HIPAA.": "Bankensicherheit, SSO und Compliance mit SOC 2, GDPR und HIPAA.",
    "Real-Time Collaboration": "Echtzeit-Zusammenarbeit",
    "Work together seamlessly with team members across different time zones.": "Nahtlose Zusammenarbeit mit Teammitgliedern über verschiedene Zeitzonen hinweg.",
    "Access all features on any device - desktop, mobile, or tablet.": "Zugriff auf alle Funktionen auf jedem Gerät - Desktop, Mobil oder Tablet.",

    # Pros & Cons
    "Pros & Cons": "Vor- und Nachteile",
    "Advantages": "Vorteile",
    "Powerful AI capabilities": "Leistungsstarke KI-Funktionen",
    "Intuitive user interface": "Intuitive Benutzeroberfläche",
    "Excellent customer support": "Exzellenter Kundensupport",
    "Regular feature updates": "Regelmäßige Feature-Updates",
    "Robust API and integrations": "Robuste API und Integrationen",
    "Scalable architecture": "Skalierbare Architektur",
    "Competitive pricing": "Wettbewerbsfähige Preise",
    "Comprehensive documentation": "Umfassende Dokumentation",
    "Active community": "Aktive Community",
    "Strong data security": "Starke Datensicherheit",
    "Disadvantages": "Nachteile",
    "Learning curve for advanced features": "Lernkurve für erweiterte Funktionen",
    "Premium pricing for enterprise tier": "Premium-Preise für Enterprise-Tier",
    "Limited offline functionality": "Eingeschränkte Offline-Funktionalität",
    "Some features require add-ons": "Einige Funktionen erfordern Add-ons",
    "Mobile app has fewer features": "Mobile App hat weniger Funktionen",

    # Pricing
    "Pricing": "Preisgestaltung",
    "offers flexible pricing plans for different organizational sizes and needs:": "bietet flexible Preispläne für verschiedene Organisationsgrößen und -anforderungen:",
    "Free Plan": "Kostenloser Plan",
    "Perfect for individuals and small teams getting started with basic features.": "Perfekt für Einzelpersonen und kleine Teams für den Einstieg mit Grundfunktionen.",
    "Professional Plan": "Professional-Plan",
    "Advanced features, increased limits, priority support, and API access.": "Erweiterte Funktionen, erhöhte Limits, priorisierter Support und API-Zugang.",
    "Enterprise Plan": "Enterprise-Plan",
    "Custom Pricing": "Individuelle Preisgestaltung",
    "Unlimited usage, dedicated support, SLA guarantees, and custom integrations.": "Unbegrenzte Nutzung, dedizierter Support, SLA-Garantien und benutzerdefinierte Integrationen.",
    "Annual plans receive a 20% discount. Volume pricing available for teams over 100 users.": "Jahrespläne erhalten 20% Rabatt. Mengenpreise verfügbar für Teams über 100 Benutzer.",

    # Use Cases
    "Best Use Cases": "Beste Anwendungsfälle",
    "Excels For:": "eignet sich hervorragend für:",
    "Enterprise Teams: Large organizations requiring scalable translation solutions with advanced features": "Enterprise-Teams: Große Organisationen, die skalierbare Übersetzungslösungen mit erweiterten Funktionen benötigen",
    "Growing Startups: Fast-moving companies that need flexible AI-powered automation": "Wachsende Startups: Schnelllebige Unternehmen, die flexible KI-gestützte Automatisierung benötigen",
    "Remote Teams: Distributed teams requiring real-time collaboration and communication": "Remote-Teams: Verteilte Teams, die Echtzeit-Zusammenarbeit und Kommunikation benötigen",
    "Data-Driven Organizations: Companies leveraging analytics for strategic decision-making": "Datengesteuerte Organisationen: Unternehmen, die Analytik für strategische Entscheidungsfindung nutzen",
    "Compliance-Heavy Industries: Regulated sectors requiring enterprise-grade security and compliance": "Compliance-intensive Branchen: Regulierte Sektoren, die Sicherheit und Compliance auf Unternehmensniveau benötigen",
    "May Not Be Ideal For:": "Möglicherweise nicht ideal für:",
    "Very small businesses with minimal translation needs": "Sehr kleine Unternehmen mit minimalen Übersetzungsbedürfnissen",
    "Organizations requiring extensive offline functionality": "Organisationen, die umfangreiche Offline-Funktionalität benötigen",
    "Teams with very limited technical expertise": "Teams mit sehr begrenztem technischen Fachwissen",

    # Comparison
    "Comparison": "Vergleich",
    "vs. Competitors": "vs. Mitbewerber",
    "Key Advantages": "Hauptvorteile",
    "Superior AI capabilities": "Überlegene KI-Funktionen",
    "More intuitive interface": "Intuitivere Benutzeroberfläche",
    "Better integration ecosystem": "Besseres Integrations-Ökosystem",
    "Faster performance": "Schnellere Leistung",
    "More competitive pricing": "Wettbewerbsfähigere Preise",
    "Stronger security features": "Stärkere Sicherheitsfunktionen",
    "Unique Differentiators": "Einzigartige Unterscheidungsmerkmale",
    "Advanced automation engine": "Fortschrittliche Automatisierungs-Engine",
    "Real-time collaboration features": "Echtzeit-Kollaborationsfunktionen",
    "Predictive analytics": "Prädiktive Analytik",
    "Custom workflow builder": "Benutzerdefinierter Workflow-Builder",
    "Enterprise-grade scalability": "Skalierbarkeit auf Unternehmensniveau",
    "Explore": "Erkunden",
    "Interface": "Benutzeroberfläche",

    # FAQ
    "Frequently Asked Questions": "Häufig gestellte Fragen",
    "Is worth the investment?": "Lohnt sich die Investition?",
    "For most organizations, yes. The platform delivers strong ROI through automation, efficiency gains, and improved translation quality. The investment pays for itself quickly for teams handling significant translation volumes.": "Für die meisten Organisationen ja. Die Plattform liefert einen starken ROI durch Automatisierung, Effizienzgewinne und verbesserte Übersetzungsqualität. Die Investition amortisiert sich schnell für Teams mit bedeutendem Übersetzungsvolumen.",
    "How long does implementation take?": "Wie lange dauert die Implementierung?",
    "Most teams can get started within 24-48 hours. The intuitive interface and excellent onboarding support make implementation straightforward, even for teams without technical expertise.": "Die meisten Teams können innerhalb von 24-48 Stunden beginnen. Die intuitive Benutzeroberfläche und exzellente Onboarding-Unterstützung machen die Implementierung unkompliziert, auch für Teams ohne technisches Fachwissen.",
    "What integrations are available?": "Welche Integrationen sind verfügbar?",
    "integrates with 100+ popular platforms including Slack, Microsoft Teams, Google Workspace, Salesforce, and more. A robust API enables custom integrations for unique workflows.": "integriert sich mit über 100 beliebten Plattformen, darunter Slack, Microsoft Teams, Google Workspace, Salesforce und mehr. Eine robuste API ermöglicht benutzerdefinierte Integrationen für einzigartige Workflows.",
    "Is my data secure?": "Sind meine Daten sicher?",
    "uses bank-grade encryption, maintains SOC 2 compliance, and offers enterprise SSO. All data is encrypted in transit and at rest, with strict access controls and regular security audits.": "verwendet Bankensicherheit, hält SOC 2-Compliance ein und bietet Enterprise-SSO. Alle Daten sind während der Übertragung und im Ruhezustand verschlüsselt, mit strengen Zugriffskontrollen und regelmäßigen Sicherheitsaudits.",
    "Can I migrate from another platform?": "Kann ich von einer anderen Plattform migrieren?",
    "Absolutely. provides migration assistance including data import, workflow recreation, and dedicated onboarding support to ensure a smooth transition.": "Auf jeden Fall. bietet Migrationsunterstützung einschließlich Datenimport, Workflow-Wiederherstellung und dedizierter Onboarding-Unterstützung für einen reibungslosen Übergang.",
    "What kind of support is available?": "Welche Art von Support ist verfügbar?",
    "Professional plans include email support, live chat, and comprehensive documentation. Enterprise customers receive dedicated account managers, priority support, and custom training sessions.": "Professional-Pläne umfassen E-Mail-Support, Live-Chat und umfassende Dokumentation. Enterprise-Kunden erhalten dedizierte Account-Manager, Priority-Support und benutzerdefinierte Schulungen.",
    "Does offer a free trial?": "Gibt es eine kostenlose Testversion?",
    "Yes, you can try all Professional features free for 14 days. No credit card required to start your trial.": "Ja, Sie können alle Professional-Funktionen 14 Tage kostenlos testen. Keine Kreditkarte erforderlich, um Ihre Testversion zu starten.",
    "How does AI enhance the platform?": "Wie verbessert KI die Plattform?",
    "The AI engine learns from your workflows to provide intelligent automation, predictive analytics, and personalized recommendations. It continuously improves translation quality and identifies optimization opportunities.": "Die KI-Engine lernt aus Ihren Workflows, um intelligente Automatisierung, prädiktive Analytik und personalisierte Empfehlungen bereitzustellen. Sie verbessert kontinuierlich die Übersetzungsqualität und identifiziert Optimierungsmöglichkeiten.",

    # Final/CTA
    "Final Verdict": "Abschließendes Urteil",
    "Excellent Choice": "Ausgezeichnete Wahl",
    "Ready to get started?": "Bereit loszulegen?",
    "Try today and experience the power of AI-driven translation": "Probieren Sie es heute aus und erleben Sie die Kraft der KI-gestützten Übersetzung",
    "Try Free": "Kostenlos testen",
    "View Pricing": "Preisgestaltung ansehen",
    "Overview": "Übersicht"
}

def translate_to_german(english_text, tool_name):
    """Translate English text to German using mapping"""

    # Direct match
    if english_text in german_translations_map:
        return german_translations_map[english_text]

    # Check for partial matches and replace tool name
    for en_key, de_value in german_translations_map.items():
        if en_key in english_text:
            result = english_text.replace(en_key, de_value)
            # Replace tool name if present
            if tool_name in result:
                continue  # Keep tool name in English for now
            return result

    # Sentence-based translation for complex strings
    german_text = english_text

    # Replace common phrases
    for en_phrase, de_phrase in german_translations_map.items():
        german_text = german_text.replace(en_phrase, de_phrase)

    return german_text

def rebuild_tool_i18n(tool_key, tool_name):
    """Rebuild i18n file for a single tool based on HTML keys"""

    html_file = os.path.join(pages_dir, f"{tool_key}.html")

    if not os.path.exists(html_file):
        print(f"  [SKIP] HTML file not found: {html_file}")
        return None, None

    # Extract keys and English content from HTML
    en_translations = extract_keys_and_content(html_file, tool_key)

    # Generate German translations
    de_translations = {}
    for key, en_text in en_translations.items():
        de_text = translate_to_german(en_text, tool_name)
        de_translations[key] = de_text

    # Build full translation object
    translations = {
        "en": en_translations,
        "de": de_translations
    }

    # Write i18n file
    i18n_file = os.path.join(js_dir, f"{tool_key}-i18n.js")

    with open(i18n_file, 'w', encoding='utf-8') as f:
        f.write("// Translation data\n")
        f.write(f"const {tool_key.replace('-', '_')}_translations = ")

        # Write JSON
        json_str = json.dumps(translations, ensure_ascii=False, indent=2)
        f.write(json_str)
        f.write(";\n\n")

        # Add event listener
        f.write("// Listen for language changes\n")
        f.write("window.addEventListener('languageChanged', (e) => {\n")
        f.write("  const lang = e.detail.language;\n")
        f.write(f"  const translations = {tool_key.replace('-', '_')}_translations[lang] || {tool_key.replace('-', '_')}_translations['en'];\n")
        f.write("  \n")
        f.write("  // Update all elements with data-i18n attributes\n")
        f.write("  document.querySelectorAll('[data-i18n]').forEach(element => {\n")
        f.write("    const key = element.getAttribute('data-i18n');\n")
        f.write("    if (translations[key]) {\n")
        f.write("      element.textContent = translations[key];\n")
        f.write("    }\n")
        f.write("  });\n")
        f.write("});\n")

    return len(en_translations), len(de_translations)

# Main execution
print("=" * 70)
print("REBUILDING TRANSLATION I18N FILES FROM HTML")
print("=" * 70)
print()

results = []

for tool_key, tool_name in translation_tools.items():
    print(f"Processing {tool_name}...")

    try:
        en_count, de_count = rebuild_tool_i18n(tool_key, tool_name)

        if en_count and de_count:
            results.append({
                "tool": tool_name,
                "status": "SUCCESS",
                "en_keys": en_count,
                "de_keys": de_count
            })
            print(f"  [OK] EN: {en_count} keys, DE: {de_count} keys")
        else:
            results.append({
                "tool": tool_name,
                "status": "SKIPPED",
                "reason": "HTML not found"
            })
    except Exception as e:
        results.append({
            "tool": tool_name,
            "status": "FAILED",
            "error": str(e)
        })
        print(f"  [ERROR] {str(e)}")

    print()

# Summary
print("=" * 70)
print("REBUILD SUMMARY")
print("=" * 70)
print()

success_count = sum(1 for r in results if r["status"] == "SUCCESS")
print(f"Successfully rebuilt: {success_count}/{len(results)}")
print()

for r in results:
    if r["status"] == "SUCCESS":
        print(f"  [OK] {r['tool']}: {r['en_keys']} keys")
    elif r["status"] == "SKIPPED":
        print(f"  [SKIP] {r['tool']}: {r['reason']}")
    elif r["status"] == "FAILED":
        print(f"  [ERROR] {r['tool']}: {r['error']}")

print()
print("=" * 70)
