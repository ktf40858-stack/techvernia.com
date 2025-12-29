#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Rebuild ALL Translation & Localization i18n files with clean structure
Fixes corruption caused by multiple scripts modifying files incorrectly
"""

import os
import json

# Base directory
base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
js_dir = os.path.join(base_dir, "js")

# All 10 Translation & Localization tools
translation_tools = {
    "deepl-pro": {
        "name": "DeepL Pro",
        "key_part": "deepl.pro",
        "description": "a powerful, feature-rich translation platform that offers exceptional value for teams of any size. Highly recommended.",
        "description_de": "eine leistungsstarke, funktionsreiche Übersetzungsplattform, die außergewöhnlichen Wert für Teams jeder Größe bietet. Sehr empfehlenswert."
    },
    "google-translate-ai": {
        "name": "Google Translate AI",
        "key_part": "google.translate.ai",
        "description": "a comprehensive, AI-powered translation solution that provides excellent capabilities for businesses worldwide.",
        "description_de": "eine umfassende, KI-gestützte Übersetzungslösung, die ausgezeichnete Funktionen für Unternehmen weltweit bietet."
    },
    "lilt": {
        "name": "Lilt",
        "key_part": "lilt",
        "description": "an innovative adaptive translation platform that combines AI with human expertise for superior quality.",
        "description_de": "eine innovative adaptive Übersetzungsplattform, die KI mit menschlicher Expertise für überlegene Qualität kombiniert."
    },
    "lokalise": {
        "name": "Lokalise",
        "key_part": "lokalise",
        "description": "a collaborative translation management platform designed for agile teams and continuous localization.",
        "description_de": "eine kollaborative Übersetzungsmanagement-Plattform für agile Teams und kontinuierliche Lokalisierung."
    },
    "microsoft-translator": {
        "name": "Microsoft Translator",
        "key_part": "microsoft.translator",
        "description": "a robust enterprise translation service with powerful AI capabilities and seamless Microsoft ecosystem integration.",
        "description_de": "ein robuster Unternehmens-Übersetzungsdienst mit leistungsstarken KI-Funktionen und nahtloser Microsoft-Ökosystem-Integration."
    },
    "modernmt": {
        "name": "ModernMT",
        "key_part": "modernmt",
        "description": "a context-aware neural machine translation platform that learns and adapts from user feedback in real-time.",
        "description_de": "eine kontextbewusste neuronale maschinelle Übersetzungsplattform, die in Echtzeit aus Benutzerfeedback lernt und sich anpasst."
    },
    "phrase": {
        "name": "Phrase",
        "key_part": "phrase",
        "description": "a comprehensive localization platform that streamlines translation workflows for software and content teams.",
        "description_de": "eine umfassende Lokalisierungsplattform, die Übersetzungs-Workflows für Software- und Content-Teams optimiert."
    },
    "smartling": {
        "name": "Smartling",
        "key_part": "smartling",
        "description": "a cloud-based translation management system with advanced automation and quality assurance features.",
        "description_de": "ein cloudbasiertes Übersetzungsmanagementsystem mit erweiterten Automatisierungs- und Qualitätssicherungsfunktionen."
    },
    "systran": {
        "name": "SYSTRAN",
        "key_part": "systran",
        "description": "a pioneer in neural machine translation with specialized industry solutions and high-security standards.",
        "description_de": "ein Pionier in der neuronalen maschinellen Übersetzung mit spezialisierten Branchenlösungen und hohen Sicherheitsstandards."
    },
    "unbabel": {
        "name": "Unbabel",
        "key_part": "unbabel",
        "description": "a human-in-the-loop translation platform that combines AI speed with human quality for customer support.",
        "description_de": "eine Human-in-the-Loop-Übersetzungsplattform, die KI-Geschwindigkeit mit menschlicher Qualität für Kundensupport kombiniert."
    }
}

def generate_translations(tool_key, tool_info):
    """Generate complete translation object for a tool"""

    name = tool_info["name"]
    key_part = tool_info["key_part"]
    desc = tool_info["description"]
    desc_de = tool_info["description_de"]

    translations = {
        "en": {
            # Overview section
            f"review.{tool_key}.overview": "Overview",
            f"review.{tool_key}.{tool_key}.is.a": f"{name} is {desc}",
            f"review.{tool_key}.the.platform.leverages.advanced": f"The platform leverages advanced machine learning algorithms to automate complex tasks, provide intelligent insights, and enable teams to work more efficiently. With seamless integrations and an intuitive user interface, {name} has become a trusted solution for translation organizations worldwide.",
            f"review.{tool_key}.whether.you're.a.small": f"Whether you're a small startup or a large enterprise, {name} scales to meet your needs while maintaining high performance and reliability.",

            # Features section
            f"review.{tool_key}.key.features": "Key Features",
            f"review.{tool_key}.ai-powered.automation": "AI-Powered Automation",
            f"review.{tool_key}.intelligent.automation.that.learns.from": "Intelligent automation that learns from your workflows and optimizes processes in real-time.",
            f"review.{tool_key}.advanced.analytics": "Advanced Analytics",
            f"review.{tool_key}.comprehensive.analytics.dashboard.with.actionable": "Comprehensive analytics dashboard with actionable insights and predictive analytics.",
            f"review.{tool_key}.seamless.integrations": "Seamless Integrations",
            f"review.{tool_key}.native.integrations.with.popular": "Native integrations with popular tools and platforms your team already uses daily.",
            f"review.{tool_key}.enterprise.security": "Enterprise Security",
            f"review.{tool_key}.bank-level.security.with.encryption": "Bank-level security with encryption, compliance certifications, and advanced access controls.",
            f"review.{tool_key}.real-time.collaboration": "Real-Time Collaboration",
            f"review.{tool_key}.collaborate.seamlessly.with.team": "Collaborate seamlessly with team members across different time zones and locations.",
            f"review.{tool_key}.customizable.workflows": "Customizable Workflows",
            f"review.{tool_key}.tailor.the.platform.to": "Tailor the platform to your specific business processes and requirements.",

            # Pros & Cons
            f"review.{tool_key}.pros.and.cons": "Pros & Cons",
            f"review.{tool_key}.advantages": "Advantages",
            f"review.{tool_key}.powerful.ai.capabilities": "Powerful AI capabilities that deliver measurable results",
            f"review.{tool_key}.intuitive.interface.with.minimal": "Intuitive interface with minimal learning curve",
            f"review.{tool_key}.excellent.customer.support.and": "Excellent customer support and comprehensive documentation",
            f"review.{tool_key}.strong.security.features.and": "Strong security features and compliance certifications",
            f"review.{tool_key}.disadvantages": "Disadvantages",
            f"review.{tool_key}.premium.pricing.may.be": "Premium pricing may be high for very small teams",
            f"review.{tool_key}.some.advanced.features.require": "Some advanced features require technical expertise",
            f"review.{tool_key}.limited.offline.functionality": "Limited offline functionality",

            # Pricing
            f"review.{tool_key}.pricing": "Pricing",
            f"review.{tool_key}.{key_part}.offers.flexible.pricing": f"{name} offers flexible pricing plans for different organizational sizes and needs:",
            f"review.{tool_key}.free.plan": "Free Plan",
            f"review.{tool_key}.perfect.for.individuals.and.small": "Perfect for individuals and small teams getting started. Includes basic features with limited usage.",
            f"review.{tool_key}.starter.plan": "Starter Plan",
            f"review.{tool_key}.professional.plan": "Professional",
            f"review.{tool_key}.advanced.features.increased.limits.priority": "Advanced features, increased limits, priority support, and API access.",
            f"review.{tool_key}.enterprise.plan": "Enterprise",
            f"review.{tool_key}.custom.pricing": "Custom",
            f"review.{tool_key}.unlimited.usage.dedicated.support.sla": "Unlimited usage, dedicated support, SLA guarantees, and custom integrations.",
            f"review.{tool_key}.annual.plans.receive.a.20": "Annual plans receive a 20% discount. Volume pricing available for teams over 100 users.",

            # Use Cases
            f"review.{tool_key}.best.use.cases": "Best Use Cases",
            f"review.{tool_key}.{key_part}.excels.for": f"{name} Excels For:",
            f"review.{tool_key}.enterprise.teams.large.organizations.requiring": f"Enterprise Teams: Large organizations requiring scalable translation solutions with advanced features",
            f"review.{tool_key}.growing.startups.fast-moving.companies": f"Growing Startups: Fast-moving companies that need flexible AI-powered automation",
            f"review.{tool_key}.remote.teams.distributed.teams": f"Remote Teams: Distributed teams requiring real-time collaboration and communication",
            f"review.{tool_key}.data-driven.organizations.companies.leveraging": f"Data-Driven Organizations: Companies leveraging analytics for strategic decision-making",
            f"review.{tool_key}.compliance-heavy.industries.regulated.sectors": f"Compliance-Heavy Industries: Regulated sectors requiring enterprise-grade security and compliance",
            f"review.{tool_key}.may.not.be.ideal.for": "May Not Be Ideal For:",
            f"review.{tool_key}.very.small.businesses.with": f"Very small businesses with minimal translation needs",
            f"review.{tool_key}.organizations.requiring.extensive.offline": f"Organizations requiring extensive offline functionality",
            f"review.{tool_key}.teams.with.very.limited": f"Teams with very limited technical expertise",

            # Comparison
            f"review.{tool_key}.comparison.with.competitors": "Comparison with Competitors",
            f"review.{tool_key}.key.advantages": "Key Advantages",
            f"review.{tool_key}.advanced.automation.engine": "Advanced automation engine",
            f"review.{tool_key}.superior.analytics.and.reporting": "Superior analytics and reporting capabilities",
            f"review.{tool_key}.more.comprehensive.integration.ecosystem": "More comprehensive integration ecosystem",
            f"review.{tool_key}.better.suited.for.enterprise": "Better suited for enterprise-scale deployments",

            # FAQ
            f"review.{tool_key}.frequently.asked.questions": "Frequently Asked Questions",
            f"review.{tool_key}.is.{tool_key}.worth.the": f"Is {name} worth the investment?",
            f"review.{tool_key}.for.most.organizations.yes": f"For most organizations, yes. {name} delivers strong ROI through automation, efficiency gains, and improved translation quality. The platform pays for itself quickly for teams handling significant translation volumes.",
            f"review.{tool_key}.how.long.does.it": "How long does it take to get started?",
            f"review.{tool_key}.most.teams.are.up": "Most teams are up and running within 24-48 hours. The intuitive interface and excellent onboarding support make implementation straightforward.",
            f"review.{tool_key}.what.kind.of.support": "What kind of support is available?",
            f"review.{tool_key}.{tool_key}.offers.comprehensive.support": f"{name} offers comprehensive support including 24/7 email support, live chat, extensive documentation, video tutorials, and dedicated account managers for Enterprise customers.",
            f"review.{tool_key}.can.i.integrate.{tool_key}": f"Can I integrate {name} with existing tools?",
            f"review.{tool_key}.yes.{tool_key}.offers.native": f"Yes, {name} offers native integrations with popular platforms and a robust API for custom integrations.",

            # CTA
            f"review.{tool_key}.try.{tool_key}.free": f"Try {name} Free",
            f"review.{tool_key}.view.pricing": "View Pricing"
        },
        "de": {
            # Overview section
            f"review.{tool_key}.overview": "Übersicht",
            f"review.{tool_key}.{tool_key}.is.a": f"{name} ist {desc_de}",
            f"review.{tool_key}.the.platform.leverages.advanced": f"Die Plattform nutzt fortschrittliche Machine-Learning-Algorithmen zur Automatisierung komplexer Aufgaben, Bereitstellung intelligenter Erkenntnisse und effizienterer Teamarbeit. Mit nahtlosen Integrationen und intuitiver Benutzeroberfläche ist {name} zu einer vertrauenswürdigen Lösung für Übersetzungsorganisationen weltweit geworden.",
            f"review.{tool_key}.whether.you're.a.small": f"Ob kleines Startup oder Großunternehmen - {name} skaliert entsprechend Ihren Anforderungen bei hoher Leistung und Zuverlässigkeit.",

            # Features section
            f"review.{tool_key}.key.features": "Hauptmerkmale",
            f"review.{tool_key}.ai-powered.automation": "KI-gestützte Automatisierung",
            f"review.{tool_key}.intelligent.automation.that.learns.from": "Intelligente Automatisierung, die aus Ihren Workflows lernt und Prozesse in Echtzeit optimiert.",
            f"review.{tool_key}.advanced.analytics": "Erweiterte Analytik",
            f"review.{tool_key}.comprehensive.analytics.dashboard.with.actionable": "Umfassendes Analyse-Dashboard mit umsetzbaren Erkenntnissen und prädiktiven Analysen.",
            f"review.{tool_key}.seamless.integrations": "Nahtlose Integrationen",
            f"review.{tool_key}.native.integrations.with.popular": "Native Integrationen mit beliebten Tools und Plattformen, die Ihr Team täglich nutzt.",
            f"review.{tool_key}.enterprise.security": "Unternehmenssicherheit",
            f"review.{tool_key}.bank-level.security.with.encryption": "Bankensicherheit mit Verschlüsselung, Compliance-Zertifizierungen und erweiterten Zugriffskontrollen.",
            f"review.{tool_key}.real-time.collaboration": "Echtzeit-Zusammenarbeit",
            f"review.{tool_key}.collaborate.seamlessly.with.team": "Nahtlose Zusammenarbeit mit Teammitgliedern über verschiedene Zeitzonen und Standorte hinweg.",
            f"review.{tool_key}.customizable.workflows": "Anpassbare Workflows",
            f"review.{tool_key}.tailor.the.platform.to": "Passen Sie die Plattform an Ihre spezifischen Geschäftsprozesse und Anforderungen an.",

            # Pros & Cons
            f"review.{tool_key}.pros.and.cons": "Vor- und Nachteile",
            f"review.{tool_key}.advantages": "Vorteile",
            f"review.{tool_key}.powerful.ai.capabilities": "Leistungsstarke KI-Funktionen, die messbare Ergebnisse liefern",
            f"review.{tool_key}.intuitive.interface.with.minimal": "Intuitive Benutzeroberfläche mit minimaler Lernkurve",
            f"review.{tool_key}.excellent.customer.support.and": "Exzellenter Kundensupport und umfassende Dokumentation",
            f"review.{tool_key}.strong.security.features.and": "Starke Sicherheitsfunktionen und Compliance-Zertifizierungen",
            f"review.{tool_key}.disadvantages": "Nachteile",
            f"review.{tool_key}.premium.pricing.may.be": "Premium-Preise können für sehr kleine Teams hoch sein",
            f"review.{tool_key}.some.advanced.features.require": "Einige erweiterte Funktionen erfordern technisches Fachwissen",
            f"review.{tool_key}.limited.offline.functionality": "Eingeschränkte Offline-Funktionalität",

            # Pricing
            f"review.{tool_key}.pricing": "Preisgestaltung",
            f"review.{tool_key}.{key_part}.offers.flexible.pricing": f"{name} bietet flexible Preispläne für verschiedene Organisationsgrößen und -anforderungen:",
            f"review.{tool_key}.free.plan": "Kostenloser Plan",
            f"review.{tool_key}.perfect.for.individuals.and.small": "Perfekt für Einzelpersonen und kleine Teams für den Einstieg. Enthält Grundfunktionen mit begrenzter Nutzung.",
            f"review.{tool_key}.starter.plan": "Starter-Plan",
            f"review.{tool_key}.professional.plan": "Professional-Plan",
            f"review.{tool_key}.advanced.features.increased.limits.priority": "Erweiterte Funktionen, erhöhte Limits, priorisierter Support und API-Zugang.",
            f"review.{tool_key}.enterprise.plan": "Enterprise-Plan",
            f"review.{tool_key}.custom.pricing": "Individuelle Preisgestaltung",
            f"review.{tool_key}.unlimited.usage.dedicated.support.sla": "Unbegrenzte Nutzung, dedizierter Support, SLA-Garantien und benutzerdefinierte Integrationen.",
            f"review.{tool_key}.annual.plans.receive.a.20": "Jahrespläne erhalten 20% Rabatt. Mengenpreise verfügbar für Teams über 100 Benutzer.",

            # Use Cases
            f"review.{tool_key}.best.use.cases": "Beste Anwendungsfälle",
            f"review.{tool_key}.{key_part}.excels.for": f"{name} eignet sich hervorragend für:",
            f"review.{tool_key}.enterprise.teams.large.organizations.requiring": f"Enterprise-Teams: Große Organisationen, die skalierbare Übersetzungslösungen mit erweiterten Funktionen benötigen",
            f"review.{tool_key}.growing.startups.fast-moving.companies": f"Wachsende Startups: Schnelllebige Unternehmen, die flexible KI-gestützte Automatisierung benötigen",
            f"review.{tool_key}.remote.teams.distributed.teams": f"Remote-Teams: Verteilte Teams, die Echtzeit-Zusammenarbeit und Kommunikation benötigen",
            f"review.{tool_key}.data-driven.organizations.companies.leveraging": f"Datengesteuerte Organisationen: Unternehmen, die Analytik für strategische Entscheidungsfindung nutzen",
            f"review.{tool_key}.compliance-heavy.industries.regulated.sectors": f"Compliance-intensive Branchen: Regulierte Sektoren, die Sicherheit und Compliance auf Unternehmensniveau benötigen",
            f"review.{tool_key}.may.not.be.ideal.for": "Möglicherweise nicht ideal für:",
            f"review.{tool_key}.very.small.businesses.with": f"Sehr kleine Unternehmen mit minimalen Übersetzungsbedürfnissen",
            f"review.{tool_key}.organizations.requiring.extensive.offline": f"Organisationen, die umfangreiche Offline-Funktionalität benötigen",
            f"review.{tool_key}.teams.with.very.limited": f"Teams mit sehr begrenztem technischen Fachwissen",

            # Comparison
            f"review.{tool_key}.comparison.with.competitors": "Vergleich mit Mitbewerbern",
            f"review.{tool_key}.key.advantages": "Hauptvorteile",
            f"review.{tool_key}.advanced.automation.engine": "Fortschrittliche Automatisierungs-Engine",
            f"review.{tool_key}.superior.analytics.and.reporting": "Überlegene Analyse- und Berichtsfunktionen",
            f"review.{tool_key}.more.comprehensive.integration.ecosystem": "Umfassenderes Integrations-Ökosystem",
            f"review.{tool_key}.better.suited.for.enterprise": "Besser geeignet für Unternehmens-Deployments",

            # FAQ
            f"review.{tool_key}.frequently.asked.questions": "Häufig gestellte Fragen",
            f"review.{tool_key}.is.{tool_key}.worth.the": f"Lohnt sich die Investition in {name}?",
            f"review.{tool_key}.for.most.organizations.yes": f"Für die meisten Organisationen ja. {name} liefert einen starken ROI durch Automatisierung, Effizienzgewinne und verbesserte Übersetzungsqualität. Die Plattform amortisiert sich schnell für Teams mit bedeutendem Übersetzungsvolumen.",
            f"review.{tool_key}.how.long.does.it": "Wie lange dauert der Einstieg?",
            f"review.{tool_key}.most.teams.are.up": "Die meisten Teams sind innerhalb von 24-48 Stunden einsatzbereit. Die intuitive Benutzeroberfläche und exzellente Onboarding-Unterstützung machen die Implementierung unkompliziert.",
            f"review.{tool_key}.what.kind.of.support": "Welche Art von Support ist verfügbar?",
            f"review.{tool_key}.{tool_key}.offers.comprehensive.support": f"{name} bietet umfassenden Support einschließlich 24/7-E-Mail-Support, Live-Chat, ausführliche Dokumentation, Video-Tutorials und dedizierte Account-Manager für Enterprise-Kunden.",
            f"review.{tool_key}.can.i.integrate.{tool_key}": f"Kann ich {name} mit bestehenden Tools integrieren?",
            f"review.{tool_key}.yes.{tool_key}.offers.native": f"Ja, {name} bietet native Integrationen mit beliebten Plattformen und eine robuste API für benutzerdefinierte Integrationen.",

            # CTA
            f"review.{tool_key}.try.{tool_key}.free": f"{name} kostenlos testen",
            f"review.{tool_key}.view.pricing": "Preisgestaltung ansehen"
        }
    }

    return translations

def rebuild_i18n_file(tool_key, tool_info):
    """Rebuild a single i18n file with clean structure"""

    filename = f"{tool_key}-i18n.js"
    filepath = os.path.join(js_dir, filename)

    # Generate translations
    translations = generate_translations(tool_key, tool_info)

    # Write file
    with open(filepath, 'w', encoding='utf-8') as f:
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

    return len(translations["en"]), len(translations["de"])

# Main execution
print("=" * 70)
print("REBUILDING ALL TRANSLATION & LOCALIZATION I18N FILES")
print("=" * 70)
print()

results = []

for tool_key, tool_info in translation_tools.items():
    print(f"Processing {tool_info['name']}...")

    try:
        en_count, de_count = rebuild_i18n_file(tool_key, tool_info)
        results.append({
            "tool": tool_info["name"],
            "status": "SUCCESS",
            "en_keys": en_count,
            "de_keys": de_count
        })
        print(f"  [OK] English keys: {en_count}")
        print(f"  [OK] German keys: {de_count}")
    except Exception as e:
        results.append({
            "tool": tool_info["name"],
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
failed_count = sum(1 for r in results if r["status"] == "FAILED")

print(f"Total tools: {len(results)}")
print(f"Successful: {success_count}")
print(f"Failed: {failed_count}")
print()

if success_count > 0:
    print("Successfully rebuilt:")
    for r in results:
        if r["status"] == "SUCCESS":
            print(f"  - {r['tool']}: {r['en_keys']} EN keys, {r['de_keys']} DE keys")

if failed_count > 0:
    print()
    print("Failed:")
    for r in results:
        if r["status"] == "FAILED":
            print(f"  - {r['tool']}: {r['error']}")

print()
print("=" * 70)
print(f"Files written to: {js_dir}")
print("=" * 70)
