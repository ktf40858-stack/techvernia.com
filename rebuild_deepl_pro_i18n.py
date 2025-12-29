import os
import json

# Rebuild DeepL Pro i18n file with correct structure

deepl_pro_translations = {
    "en": {
        # Navigation & General
        "review.deepl-pro.overview": "Overview",
        "review.deepl-pro.key.features": "Key Features",
        "review.deepl-pro.pros.cons": "Pros & Cons",
        "review.deepl-pro.advantages": "Advantages",
        "review.deepl-pro.disadvantages": "Disadvantages",
        "review.deepl-pro.pricing": "Pricing",
        "review.deepl-pro.best.use.cases": "Best Use Cases",
        "review.deepl-pro.comparison": "Comparison",
        "review.deepl-pro.frequently.asked.questions": "Frequently Asked Questions",
        "review.deepl-pro.final.verdict": "Final Verdict",
        "review.deepl-pro.ready.to.get.started": "Ready to Get Started?",
        "review.deepl-pro.view.pricing": "View Pricing",

        # Overview section
        "review.deepl-pro.deepl-pro.is.a": "DeepL Pro is a powerful, feature-rich translation platform that delivers exceptional value for teams of all sizes. Highly recommended.",
        "review.deepl-pro.the.platform.leverages.advanced.machine": "The platform leverages advanced machine learning algorithms to automate complex tasks, provide intelligent insights, and enable teams to work more efficiently. With seamless integrations and an intuitive interface, DeepL Pro has become a trusted solution for translation organizations worldwide.",
        "review.deepl-pro.whether.youre.a.small.startup": "Whether you're a small startup or a large enterprise, DeepL Pro scales to meet your needs while maintaining high performance and reliability.",

        # Feature cards
        "review.deepl-pro.ai-powered.automation": "AI-Powered Automation",
        "review.deepl-pro.advanced.analytics": "Advanced Analytics",
        "review.deepl-pro.seamless.integrations": "Seamless Integrations",
        "review.deepl-pro.enterprise.security": "Enterprise Security",
        "review.deepl-pro.real-time.collaboration": "Real-Time Collaboration",
        "review.deepl-pro.mobile.access": "Mobile Access",

        # Feature descriptions
        "review.deepl-pro.intelligent.automation.that.learns.from": "Intelligent automation that learns from your workflows and optimizes processes in real-time.",
        "review.deepl-pro.comprehensive.analytics.dashboard.with.actionable": "Comprehensive analytics dashboard with actionable insights and predictive analytics.",
        "review.deepl-pro.connect.with.100.popular.tools": "Connect with 100+ popular tools and platforms through native integrations and API.",
        "review.deepl-pro.bank-grade.encryption.sso.and.compliance": "Bank-grade encryption, SSO, and compliance with SOC 2, GDPR, and HIPAA standards.",
        "review.deepl-pro.work.together.seamlessly.with.team": "Work together seamlessly with team members across multiple locations and time zones.",
        "review.deepl-pro.access.all.features.on.any": "Access all features on any device with responsive design and native mobile apps.",

        # Pros
        "review.deepl-pro.powerful.ai.capabilities": "Powerful AI capabilities",
        "review.deepl-pro.intuitive.user.interface": "Intuitive user interface",
        "review.deepl-pro.excellent.customer.support": "Excellent customer support",
        "review.deepl-pro.regular.feature.updates": "Regular feature updates",
        "review.deepl-pro.strong.data.security": "Strong data security",
        "review.deepl-pro.scalable.architecture": "Scalable architecture",
        "review.deepl-pro.comprehensive.documentation": "Comprehensive documentation",
        "review.deepl-pro.active.community": "Active community",
        "review.deepl-pro.competitive.pricing": "Competitive pricing",
        "review.deepl-pro.enterprise-grade.scalability": "Enterprise-grade scalability",

        # Cons
        "review.deepl-pro.learning.curve.for.advanced.features": "Learning curve for advanced features",
        "review.deepl-pro.premium.pricing.for.enterprise.tier": "Premium pricing for enterprise tier",
        "review.deepl-pro.limited.offline.functionality": "Limited offline functionality",
        "review.deepl-pro.mobile.app.has.fewer.features": "Mobile app has fewer features",
        "review.deepl-pro.some.features.require.add-ons": "Some features require add-ons",

        # Pricing
        "review.deepl-pro.deepl.pro.offers.flexible.pricing": "DeepL Pro offers flexible pricing plans for various organization sizes and needs:",
        "review.deepl-pro.free.plan": "Free Plan",
        "review.deepl-pro.professional.plan": "Professional",
        "review.deepl-pro.enterprise.plan": "Enterprise",
        "review.deepl-pro.custom.pricing": "Custom",
        "review.deepl-pro.perfect.for.individuals.and.small": "Perfect for individuals and small teams getting started. Basic features with limited usage.",
        "review.deepl-pro.advanced.features.increased.limits.priority": "Advanced features, increased limits, priority support, and API access.",
        "review.deepl-pro.unlimited.usage.dedicated.support.sla": "Unlimited usage, dedicated support, SLA guarantees, and custom integrations.",
        "review.deepl-pro.annual.plans.receive.a.20": "Annual plans receive a 20% discount. Volume pricing available for teams over 100 users.",

        # Use Cases
        "review.deepl-pro.deepl.pro.excels.for": "DeepL Pro Excels For:",
        "review.deepl-pro.enterprise.teams.large.organizations.requiring": "Enterprise Teams: Large organizations requiring scalable translation solutions with advanced features",
        "review.deepl-pro.growing.startups.fast-moving.companies.that": "Growing Startups: Fast-moving companies that need flexible AI-powered automation",
        "review.deepl-pro.remote.teams.distributed.teams.requiring": "Remote Teams: Distributed teams requiring real-time collaboration and communication",
        "review.deepl-pro.data-driven.organizations.companies.leveraging.analytics": "Data-Driven Organizations: Companies leveraging analytics for strategic decision-making",
        "review.deepl-pro.compliance-heavy.industries.regulated.sectors.requiring": "Compliance-Heavy Industries: Regulated sectors requiring enterprise-grade security and compliance",
        "review.deepl-pro.may.not.be.ideal.for": "May Not Be Ideal For:",
        "review.deepl-pro.very.small.businesses.with.minimal": "Very small businesses with minimal translation needs",
        "review.deepl-pro.organizations.requiring.extensive.offline.functionality": "Organizations requiring extensive offline functionality",
        "review.deepl-pro.teams.with.very.limited.technical": "Teams with very limited technical expertise",

        # Comparison
        "review.deepl-pro.key.advantages": "Key Advantages",
        "review.deepl-pro.superior.ai.capabilities": "Superior AI capabilities",
        "review.deepl-pro.more.intuitive.interface": "More intuitive interface",
        "review.deepl-pro.better.integration.ecosystem": "Better integration ecosystem",
        "review.deepl-pro.more.competitive.pricing": "More competitive pricing",
        "review.deepl-pro.faster.performance": "Faster performance",
        "review.deepl-pro.stronger.security.features": "Stronger security features",
        "review.deepl-pro.unique.differentiators": "Unique Differentiators",
        "review.deepl-pro.custom.workflow.builder": "Custom workflow builder",
        "review.deepl-pro.predictive.analytics": "Predictive analytics",
        "review.deepl-pro.excellent.choice": "Excellent Choice",

        # FAQ
        "review.deepl-pro.faq.is.worth.the.investment": "Is DeepL Pro worth the investment?",
        "review.deepl-pro.faq.how.long.does.implementation.take": "How long does implementation take?",
        "review.deepl-pro.faq.what.integrations.are.available": "What integrations are available?",
        "review.deepl-pro.faq.is.my.data.secure": "Is my data secure?",
        "review.deepl-pro.faq.can.i.migrate.from.another.platform": "Can I migrate from another platform?",
        "review.deepl-pro.faq.what.kind.of.support.is.available": "What kind of support is available?",
        "review.deepl-pro.faq.does.offer.a.free.trial": "Does DeepL Pro offer a free trial?",
        "review.deepl-pro.faq.how.does.ai.enhance.the.platform": "How does AI enhance the platform?",

        # FAQ Answers
        "review.deepl-pro.for.most.organizations.yes.the": "For most organizations, yes. The AI-powered automation and productivity gains typically provide strong ROI within the first few months. The platform's scalability and extensive features justify the cost for growing teams.",
        "review.deepl-pro.most.teams.can.get.started": "Most teams can get started within a day. Basic setup takes minutes, while full enterprise deployment with custom integrations typically takes 1-2 weeks with proper planning.",
        "review.deepl-pro.professional.plans.include.email.support": "Professional plans include email support with 24-hour response time. Enterprise customers get dedicated account managers, priority support, and SLA guarantees.",
        "review.deepl-pro.the.ai.engine.learns.from": "The AI engine learns from your usage patterns to suggest optimizations, automate repetitive tasks, predict outcomes, and provide intelligent recommendations that improve over time.",

        # CTA
        "review.deepl-pro.try.deepl.pro.today.and": "Try DeepL Pro today and experience the power of AI-driven automation.",
        "review.deepl-pro.try.deepl.pro.free": "Try DeepL Pro Free",
    },
    "de": {
        # Navigation & General
        "review.deepl-pro.overview": "Übersicht",
        "review.deepl-pro.key.features": "Hauptmerkmale",
        "review.deepl-pro.pros.cons": "Vor- und Nachteile",
        "review.deepl-pro.advantages": "Vorteile",
        "review.deepl-pro.disadvantages": "Nachteile",
        "review.deepl-pro.pricing": "Preisgestaltung",
        "review.deepl-pro.best.use.cases": "Beste Anwendungsfälle",
        "review.deepl-pro.comparison": "Vergleich",
        "review.deepl-pro.frequently.asked.questions": "Häufig gestellte Fragen",
        "review.deepl-pro.final.verdict": "Endgültiges Urteil",
        "review.deepl-pro.ready.to.get.started": "Bereit loszulegen?",
        "review.deepl-pro.view.pricing": "Preise ansehen",

        # Overview section
        "review.deepl-pro.deepl-pro.is.a": "DeepL Pro ist eine leistungsstarke, funktionsreiche Übersetzungsplattform, die außergewöhnlichen Wert für Teams jeder Größe bietet. Sehr empfehlenswert.",
        "review.deepl-pro.the.platform.leverages.advanced.machine": "Die Plattform nutzt fortschrittliche Machine-Learning-Algorithmen zur Automatisierung komplexer Aufgaben, Bereitstellung intelligenter Erkenntnisse und effizienterer Teamarbeit. Mit nahtlosen Integrationen und intuitiver Benutzeroberfläche ist DeepL Pro zu einer vertrauenswürdigen Lösung für Übersetzungsorganisationen weltweit geworden.",
        "review.deepl-pro.whether.youre.a.small.startup": "Ob kleines Startup oder Großunternehmen - DeepL Pro skaliert entsprechend Ihren Anforderungen bei hoher Leistung und Zuverlässigkeit.",

        # Feature cards
        "review.deepl-pro.ai-powered.automation": "KI-gestützte Automatisierung",
        "review.deepl-pro.advanced.analytics": "Erweiterte Analytik",
        "review.deepl-pro.seamless.integrations": "Nahtlose Integrationen",
        "review.deepl-pro.enterprise.security": "Unternehmenssicherheit",
        "review.deepl-pro.real-time.collaboration": "Echtzeit-Zusammenarbeit",
        "review.deepl-pro.mobile.access": "Mobiler Zugriff",

        # Feature descriptions
        "review.deepl-pro.intelligent.automation.that.learns.from": "Intelligente Automatisierung, die aus Ihren Workflows lernt und Prozesse in Echtzeit optimiert.",
        "review.deepl-pro.comprehensive.analytics.dashboard.with.actionable": "Umfassendes Analyse-Dashboard mit umsetzbaren Erkenntnissen und prädiktiven Analysen.",
        "review.deepl-pro.connect.with.100.popular.tools": "Verbinden Sie sich mit über 100 beliebten Tools und Plattformen durch native Integrationen und API.",
        "review.deepl-pro.bank-grade.encryption.sso.and.compliance": "Banksichere Verschlüsselung, SSO und Compliance mit SOC 2, GDPR und HIPAA-Standards.",
        "review.deepl-pro.work.together.seamlessly.with.team": "Arbeiten Sie nahtlos mit Teammitgliedern über mehrere Standorte und Zeitzonen hinweg zusammen.",
        "review.deepl-pro.access.all.features.on.any": "Greifen Sie auf alle Funktionen auf jedem Gerät mit responsivem Design und nativen mobilen Apps zu.",

        # Pros
        "review.deepl-pro.powerful.ai.capabilities": "Leistungsstarke KI-Funktionen",
        "review.deepl-pro.intuitive.user.interface": "Intuitive Benutzeroberfläche",
        "review.deepl-pro.excellent.customer.support": "Exzellenter Kundensupport",
        "review.deepl-pro.regular.feature.updates": "Regelmäßige Feature-Updates",
        "review.deepl-pro.strong.data.security": "Starke Datensicherheit",
        "review.deepl-pro.scalable.architecture": "Skalierbare Architektur",
        "review.deepl-pro.comprehensive.documentation": "Umfassende Dokumentation",
        "review.deepl-pro.active.community": "Aktive Community",
        "review.deepl-pro.competitive.pricing": "Wettbewerbsfähige Preise",
        "review.deepl-pro.enterprise-grade.scalability": "Skalierbarkeit auf Enterprise-Niveau",

        # Cons
        "review.deepl-pro.learning.curve.for.advanced.features": "Lernkurve für erweiterte Funktionen",
        "review.deepl-pro.premium.pricing.for.enterprise.tier": "Premium-Preise für Enterprise-Tier",
        "review.deepl-pro.limited.offline.functionality": "Eingeschränkte Offline-Funktionalität",
        "review.deepl-pro.mobile.app.has.fewer.features": "Mobile App hat weniger Funktionen",
        "review.deepl-pro.some.features.require.add-ons": "Einige Funktionen erfordern Add-ons",

        # Pricing
        "review.deepl-pro.deepl.pro.offers.flexible.pricing": "DeepL Pro bietet flexible Preispläne für verschiedene Organisationsgrößen und -anforderungen:",
        "review.deepl-pro.free.plan": "Kostenloser Plan",
        "review.deepl-pro.professional.plan": "Professional-Plan",
        "review.deepl-pro.enterprise.plan": "Enterprise-Plan",
        "review.deepl-pro.custom.pricing": "Individuelle Preisgestaltung",
        "review.deepl-pro.perfect.for.individuals.and.small": "Perfekt für Einzelpersonen und kleine Teams für den Einstieg. Grundfunktionen mit begrenzter Nutzung.",
        "review.deepl-pro.advanced.features.increased.limits.priority": "Erweiterte Funktionen, erhöhte Limits, priorisierter Support und API-Zugang.",
        "review.deepl-pro.unlimited.usage.dedicated.support.sla": "Unbegrenzte Nutzung, dedizierter Support, SLA-Garantien und benutzerdefinierte Integrationen.",
        "review.deepl-pro.annual.plans.receive.a.20": "Jahrespläne erhalten 20% Rabatt. Mengenpreise verfügbar für Teams über 100 Benutzer.",

        # Use Cases
        "review.deepl-pro.deepl.pro.excels.for": "DeepL Pro eignet sich hervorragend für:",
        "review.deepl-pro.enterprise.teams.large.organizations.requiring": "Enterprise-Teams: Große Organisationen, die skalierbare Übersetzungslösungen mit erweiterten Funktionen benötigen",
        "review.deepl-pro.growing.startups.fast-moving.companies.that": "Wachsende Startups: Schnelllebige Unternehmen, die flexible KI-gestützte Automatisierung benötigen",
        "review.deepl-pro.remote.teams.distributed.teams.requiring": "Remote-Teams: Verteilte Teams, die Echtzeit-Zusammenarbeit und Kommunikation benötigen",
        "review.deepl-pro.data-driven.organizations.companies.leveraging.analytics": "Datengesteuerte Organisationen: Unternehmen, die Analysen für strategische Entscheidungen nutzen",
        "review.deepl-pro.compliance-heavy.industries.regulated.sectors.requiring": "Compliance-intensive Branchen: Regulierte Sektoren, die Enterprise-Sicherheit und Compliance benötigen",
        "review.deepl-pro.may.not.be.ideal.for": "Möglicherweise nicht ideal für:",
        "review.deepl-pro.very.small.businesses.with.minimal": "Sehr kleine Unternehmen mit minimalen Übersetzungsbedürfnissen",
        "review.deepl-pro.organizations.requiring.extensive.offline.functionality": "Organisationen, die umfangreiche Offline-Funktionalität benötigen",
        "review.deepl-pro.teams.with.very.limited.technical": "Teams mit sehr begrenzter technischer Expertise",

        # Comparison
        "review.deepl-pro.key.advantages": "Hauptvorteile",
        "review.deepl-pro.superior.ai.capabilities": "Überlegene KI-Funktionen",
        "review.deepl-pro.more.intuitive.interface": "Intuitivere Benutzeroberfläche",
        "review.deepl-pro.better.integration.ecosystem": "Besseres Integrations-Ökosystem",
        "review.deepl-pro.more.competitive.pricing": "Wettbewerbsfähigere Preise",
        "review.deepl-pro.faster.performance": "Schnellere Leistung",
        "review.deepl-pro.stronger.security.features": "Stärkere Sicherheitsfunktionen",
        "review.deepl-pro.unique.differentiators": "Einzigartige Differenzierungsmerkmale",
        "review.deepl-pro.custom.workflow.builder": "Benutzerdefinierter Workflow-Builder",
        "review.deepl-pro.predictive.analytics": "Prädiktive Analytik",
        "review.deepl-pro.excellent.choice": "Ausgezeichnete Wahl",

        # FAQ
        "review.deepl-pro.faq.is.worth.the.investment": "Lohnt sich die Investition in DeepL Pro?",
        "review.deepl-pro.faq.how.long.does.implementation.take": "Wie lange dauert die Implementierung?",
        "review.deepl-pro.faq.what.integrations.are.available": "Welche Integrationen sind verfügbar?",
        "review.deepl-pro.faq.is.my.data.secure": "Sind meine Daten sicher?",
        "review.deepl-pro.faq.can.i.migrate.from.another.platform": "Kann ich von einer anderen Plattform migrieren?",
        "review.deepl-pro.faq.what.kind.of.support.is.available": "Welche Art von Support ist verfügbar?",
        "review.deepl-pro.faq.does.offer.a.free.trial": "Bietet DeepL Pro eine kostenlose Testversion an?",
        "review.deepl-pro.faq.how.does.ai.enhance.the.platform": "Wie verbessert KI die Plattform?",

        # FAQ Answers
        "review.deepl-pro.for.most.organizations.yes.the": "Für die meisten Organisationen ja. Die KI-gestützte Automatisierung und Produktivitätsgewinne bieten in der Regel einen starken ROI innerhalb der ersten Monate. Die Skalierbarkeit und umfangreichen Funktionen der Plattform rechtfertigen die Kosten für wachsende Teams.",
        "review.deepl-pro.most.teams.can.get.started": "Die meisten Teams können innerhalb eines Tages loslegen. Die Grundeinrichtung dauert Minuten, während die vollständige Enterprise-Bereitstellung mit benutzerdefinierten Integrationen bei guter Planung typischerweise 1-2 Wochen dauert.",
        "review.deepl-pro.professional.plans.include.email.support": "Professional-Pläne beinhalten E-Mail-Support mit 24-Stunden-Reaktionszeit. Enterprise-Kunden erhalten dedizierte Account Manager, priorisierten Support und SLA-Garantien.",
        "review.deepl-pro.the.ai.engine.learns.from": "Die KI-Engine lernt aus Ihren Nutzungsmustern, um Optimierungen vorzuschlagen, sich wiederholende Aufgaben zu automatisieren, Ergebnisse vorherzusagen und intelligente Empfehlungen zu geben, die sich im Laufe der Zeit verbessern.",

        # CTA
        "review.deepl-pro.try.deepl.pro.today.and": "Testen Sie DeepL Pro heute und erleben Sie die Kraft der KI-gesteuerten Automatisierung.",
        "review.deepl-pro.try.deepl.pro.free": "DeepL Pro kostenlos testen",
    }
}

# Write the file
output_file = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\js\deepl-pro-i18n.js"

with open(output_file, 'w', encoding='utf-8') as f:
    f.write("// DEEPL PRO I18N\n")
    f.write("const deeplProTranslations = ")

    # Write JSON with proper formatting
    json_str = json.dumps(deepl_pro_translations, ensure_ascii=False, indent=2)
    f.write(json_str)
    f.write(";\n\n")

    # Add event listener
    f.write("window.addEventListener('languageChanged', (e) => {\n")
    f.write("  const lang = e.detail.language;\n")
    f.write("  if (deeplProTranslations[lang]) {\n")
    f.write("    Object.entries(deeplProTranslations[lang]).forEach(([key, value]) => {\n")
    f.write("      const elements = document.querySelectorAll(`[data-i18n=\"${key}\"]`);\n")
    f.write("      elements.forEach(el => el.textContent = value);\n")
    f.write("    });\n")
    f.write("  }\n")
    f.write("});\n")

print("[OK] DeepL Pro i18n file rebuilt successfully")
print(f"  - English keys: {len(deepl_pro_translations['en'])}")
print(f"  - German keys: {len(deepl_pro_translations['de'])}")
print(f"  - File: {output_file}")
