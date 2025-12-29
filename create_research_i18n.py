import os
import re
import json

base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
research_dir = os.path.join(base_dir, "pages", "reviews", "research")
js_dir = os.path.join(base_dir, "js")

tools = [
    "connected-papers", "consensus", "elicit", "irisai", "litmaps",
    "perplexity-research", "researchrabbit", "scholarcy", "scispace",
    "scite", "semantic-scholar", "undermind"
]

tool_names = {
    "connected-papers": "Connected Papers",
    "consensus": "Consensus",
    "elicit": "Elicit",
    "irisai": "Iris.ai",
    "litmaps": "Litmaps",
    "perplexity-research": "Perplexity Research",
    "researchrabbit": "ResearchRabbit",
    "scholarcy": "Scholarcy",
    "scispace": "SciSpace",
    "scite": "Scite",
    "semantic-scholar": "Semantic Scholar",
    "undermind": "Undermind"
}

# Traductions génériques adaptées pour Research
generic_translations = {
    "en": {
        "ready.to.get.started": "Ready to Get Started?",
        "try.{tool}.today.and.experience": "Try {tool} today and experience the power of AI-driven automation.",
        "try.{tool}.free": "Try {tool} Free",
        "view.pricing": "View Pricing",
        "overview": "Overview",
        "{tool}.is.a.leading.ai-powered": "{tool} is a leading AI-powered research platform designed to streamline workflows and enhance productivity. Built with cutting-edge artificial intelligence technology, it delivers exceptional performance for modern businesses.",
        "the.platform.leverages.advanced.machine": "The platform leverages advanced machine learning algorithms to automate complex tasks, provide intelligent insights, and enable teams to work more efficiently. With seamless integrations and an intuitive interface, {tool} has become a trusted solution for organizations worldwide.",
        "whether.youre.a.small.startup": "Whether you're a small startup or a large enterprise, {tool} scales to meet your needs while maintaining high performance and reliability.",
        "key.features": "Key Features",
        "intelligent.automation.that.learns.from": "Intelligent automation that learns from your workflows and optimizes processes in real-time.",
        "comprehensive.analytics.dashboard.with.actionable": "Comprehensive analytics dashboard with actionable insights and predictive analytics.",
        "connect.with.100.popular.tools": "Connect with 100+ popular tools and platforms through native integrations and API.",
        "bank-grade.encryption.sso.and.compliance": "Bank-grade encryption, SSO, and compliance with SOC 2, GDPR, and HIPAA standards.",
        "work.together.seamlessly.with.team": "Work together seamlessly with team members across multiple locations and time zones.",
        "access.all.features.on.any": "Access all features on any device with responsive design and native mobile apps.",
        "pros.cons": "Pros & Cons",
        "advantages": "Advantages",
        "powerful.ai.capabilities": "Powerful AI capabilities",
        "intuitive.user.interface": "Intuitive user interface",
        "excellent.customer.support": "Excellent customer support",
        "regular.feature.updates": "Regular feature updates",
        "robust.api.and.integrations": "Robust API and integrations",
        "scalable.architecture": "Scalable architecture",
        "competitive.pricing": "Competitive pricing",
        "comprehensive.documentation": "Comprehensive documentation",
        "active.community": "Active community",
        "strong.data.security": "Strong data security",
        "disadvantages": "Disadvantages",
        "learning.curve.for.advanced.features": "Learning curve for advanced features",
        "premium.pricing.for.enterprise.tier": "Premium pricing for enterprise tier",
        "limited.offline.functionality": "Limited offline functionality",
        "some.features.require.add-ons": "Some features require add-ons",
        "mobile.app.has.fewer.features": "Mobile app has fewer features",
        "pricing": "Pricing",
        "{tool}.offers.flexible.pricing.plans": "{tool} offers flexible pricing plans to suit different organization sizes and needs:",
        "perfect.for.individuals.and.small": "Perfect for individuals and small teams getting started. Basic features with limited usage.",
        "advanced.features.increased.limits.priority": "Advanced features, increased limits, priority support, and API access.",
        "unlimited.usage.dedicated.support.sla": "Unlimited usage, dedicated support, SLA guarantees, and custom integrations.",
        "annual.plans.receive.a.20": "Annual plans receive a 20% discount. Volume pricing available for teams over 100 users.",
        "best.use.cases": "Best Use Cases",
        "{tool}.excels.for": "{tool} Excels For:",
        "enterprise.teams.large.organizations.requiring": "Enterprise Teams: Large organizations requiring scalable research solutions with advanced features",
        "growing.startups.fast-moving.companies.that": "Growing Startups: Fast-moving companies that need flexible, AI-powered automation",
        "remote.teams.distributed.teams.requiring": "Remote Teams: Distributed teams requiring real-time collaboration and communication",
        "data-driven.organizations.companies.leveraging.analytics": "Data-Driven Organizations: Companies leveraging analytics for strategic decision-making",
        "compliance-heavy.industries.regulated.sectors.requiring": "Compliance-Heavy Industries: Regulated sectors requiring enterprise-grade security and compliance",
        "may.not.be.ideal.for": "May Not Be Ideal For:",
        "very.small.businesses.with.minimal": "Very small businesses with minimal research needs",
        "organizations.requiring.extensive.offline.functionality": "Organizations requiring extensive offline functionality",
        "teams.with.very.limited.technical": "Teams with very limited technical expertise",
        "comparison": "Comparison",
        "{tool}.vs.competitors": "{tool} vs Competitors",
        "key.advantages": "Key Advantages",
        "superior.ai.capabilities": "Superior AI capabilities",
        "more.intuitive.interface": "More intuitive interface",
        "better.integration.ecosystem": "Better integration ecosystem",
        "faster.performance": "Faster performance",
        "more.competitive.pricing": "More competitive pricing",
        "stronger.security.features": "Stronger security features",
        "unique.differentiators": "Unique Differentiators",
        "advanced.automation.engine": "Advanced automation engine",
        "real-time.collaboration.features": "Real-time collaboration features",
        "predictive.analytics": "Predictive analytics",
        "custom.workflow.builder": "Custom workflow builder",
        "enterprise-grade.scalability": "Enterprise-grade scalability",
        "explore.{tool}s.interface": "Explore {tool}'s interface:",
        "frequently.asked.questions": "Frequently Asked Questions",
        "for.most.organizations.yes.the": "For most organizations, yes. The AI-powered automation and productivity gains typically provide strong ROI within the first few months. The platform's scalability and extensive features justify the cost for growing teams.",
        "most.teams.can.get.started": "Most teams can get started within a day. Basic setup takes minutes, while full enterprise deployment with custom integrations typically takes 1-2 weeks with proper planning.",
        "{tool}.integrates.with.100.popular": "{tool} integrates with 100+ popular platforms including Slack, Microsoft Teams, Salesforce, Google Workspace, and many more. A robust API enables custom integrations.",
        "yes.{tool}.uses.bank-grade.encryption": "Yes. {tool} uses bank-grade encryption, maintains SOC 2 Type II certification, and is compliant with GDPR, HIPAA, and other major regulations. Data is encrypted at rest and in transit.",
        "absolutely.{tool}.provides.migration.tools": "Absolutely. {tool} provides migration tools and dedicated support to help you seamlessly transition from competing platforms with minimal downtime.",
        "professional.plans.include.email.support": "Professional plans include email support with 24-hour response time. Enterprise customers get dedicated account managers, priority support, and SLA guarantees.",
        "yes.you.can.try.all": "Yes! You can try all Professional features free for 14 days with no credit card required. The free plan is available indefinitely for basic usage.",
        "the.ai.engine.learns.from": "The AI engine learns from your usage patterns to suggest optimizations, automate repetitive tasks, predict outcomes, and provide intelligent recommendations that improve over time.",
        "final.verdict": "Final Verdict",
        "excellent.choice": "Excellent Choice",
        "{tool}.is.a.powerful.feature-rich": "{tool} is a powerful, feature-rich research platform that delivers exceptional value for teams of all sizes. Highly recommended.",
        "faq.is.{tool}.worth.the.investment": "Is {tool} worth the investment?",
        "faq.how.long.does.implementation.take": "How long does implementation take?",
        "faq.what.integrations.are.available": "What integrations are available?",
        "faq.is.my.data.secure": "Is my data secure?",
        "faq.can.i.migrate.from.another.platform": "Can I migrate from another platform?",
        "faq.what.kind.of.support.is.available": "What kind of support is available?",
        "faq.does.{tool}.offer.a.free.trial": "Does {tool} offer a free trial?",
        "faq.how.does.ai.enhance.the.platform": "How does AI enhance the platform?"
    },
    "de": {
        "ready.to.get.started": "Bereit loszulegen?",
        "try.{tool}.today.and.experience": "Probieren Sie {tool} heute aus und erleben Sie die Kraft der KI-gesteuerten Automatisierung.",
        "try.{tool}.free": "{tool} kostenlos testen",
        "view.pricing": "Preise",
        "overview": "Übersicht",
        "{tool}.is.a.leading.ai-powered": "{tool} ist eine führende KI-gestützte Forschungsplattform zur Optimierung von Workflows und Produktivitätssteigerung. Mit modernster KI-Technologie bietet sie außergewöhnliche Leistung für moderne Unternehmen.",
        "the.platform.leverages.advanced.machine": "Die Plattform nutzt fortschrittliche Machine-Learning-Algorithmen zur Automatisierung komplexer Aufgaben, Bereitstellung intelligenter Erkenntnisse und effizienterer Teamarbeit. Mit nahtlosen Integrationen und intuitiver Benutzeroberfläche ist {tool} zu einer vertrauenswürdigen Lösung für Forschungsorganisationen weltweit geworden.",
        "whether.youre.a.small.startup": "Ob kleines Startup oder Großunternehmen - {tool} skaliert entsprechend Ihren Anforderungen bei hoher Leistung und Zuverlässigkeit.",
        "key.features": "Hauptmerkmale",
        "intelligent.automation.that.learns.from": "Intelligente Automatisierung, die aus Ihren Workflows lernt und Prozesse in Echtzeit optimiert.",
        "comprehensive.analytics.dashboard.with.actionable": "Umfassendes Analyse-Dashboard mit umsetzbaren Erkenntnissen und prädiktiven Analysen.",
        "connect.with.100.popular.tools": "Verbinden Sie sich mit über 100 beliebten Tools und Plattformen über native Integrationen und API.",
        "bank-grade.encryption.sso.and.compliance": "Verschlüsselung auf Bankniveau, SSO und Konformität mit SOC 2-, DSGVO- und HIPAA-Standards.",
        "work.together.seamlessly.with.team": "Arbeiten Sie nahtlos mit Teammitgliedern an mehreren Standorten und Zeitzonen zusammen.",
        "access.all.features.on.any": "Greifen Sie auf alle Funktionen auf jedem Gerät mit responsivem Design und nativen mobilen Apps zu.",
        "pros.cons": "Vor- und Nachteile",
        "advantages": "Vorteile",
        "powerful.ai.capabilities": "Leistungsstarke KI-Funktionen",
        "intuitive.user.interface": "Intuitive Benutzeroberfläche",
        "excellent.customer.support": "Exzellenter Kundensupport",
        "regular.feature.updates": "Regelmäßige Feature-Updates",
        "robust.api.and.integrations": "Robuste API und Integrationen",
        "scalable.architecture": "Skalierbare Architektur",
        "competitive.pricing": "Wettbewerbsfähige Preise",
        "comprehensive.documentation": "Umfassende Dokumentation",
        "active.community": "Aktive Community",
        "strong.data.security": "Starke Datensicherheit",
        "disadvantages": "Nachteile",
        "learning.curve.for.advanced.features": "Lernkurve für erweiterte Funktionen",
        "premium.pricing.for.enterprise.tier": "Premium-Preise für Enterprise-Stufe",
        "limited.offline.functionality": "Eingeschränkte Offline-Funktionalität",
        "some.features.require.add-ons": "Einige Funktionen erfordern Add-ons",
        "mobile.app.has.fewer.features": "Mobile App hat weniger Funktionen",
        "pricing": "Preise",
        "{tool}.offers.flexible.pricing.plans": "{tool} bietet flexible Preispläne für verschiedene Organisationsgrößen und -anforderungen:",
        "perfect.for.individuals.and.small": "Perfekt für Einzelpersonen und kleine Teams zum Einstieg. Grundfunktionen mit begrenzter Nutzung.",
        "advanced.features.increased.limits.priority": "Erweiterte Funktionen, erhöhte Limits, Priority-Support und API-Zugriff.",
        "unlimited.usage.dedicated.support.sla": "Unbegrenzte Nutzung, dedizierter Support, SLA-Garantien und individuelle Integrationen.",
        "annual.plans.receive.a.20": "Jahrespläne erhalten 20% Rabatt. Volumenpreise verfügbar für Teams mit über 100 Nutzern.",
        "best.use.cases": "Beste Anwendungsfälle",
        "{tool}.excels.for": "{tool} eignet sich hervorragend für:",
        "enterprise.teams.large.organizations.requiring": "Enterprise-Teams: Große Forschungsorganisationen, die skalierbare Forschungslösungen mit erweiterten Funktionen benötigen",
        "growing.startups.fast-moving.companies.that": "Wachsende Startups: Schnelllebige Unternehmen, die flexible, KI-gestützte Automatisierung benötigen",
        "remote.teams.distributed.teams.requiring": "Remote-Teams: Verteilte Teams, die Echtzeit-Zusammenarbeit und -Kommunikation benötigen",
        "data-driven.organizations.companies.leveraging.analytics": "Datengetriebene Forschungsorganisationen: Unternehmen, die Analysen für strategische Entscheidungsfindung nutzen",
        "compliance-heavy.industries.regulated.sectors.requiring": "Stark regulierte Branchen: Regulierte Sektoren, die Enterprise-Grade-Sicherheit und Compliance benötigen",
        "may.not.be.ideal.for": "Möglicherweise nicht ideal für:",
        "very.small.businesses.with.minimal": "Sehr kleine Unternehmen mit minimalen Forschungsanforderungen",
        "organizations.requiring.extensive.offline.functionality": "Forschungsorganisationen, die umfangreiche Offline-Funktionalität benötigen",
        "teams.with.very.limited.technical": "Teams mit sehr begrenzter technischer Expertise",
        "comparison": "Vergleich",
        "{tool}.vs.competitors": "{tool} vs. Mitbewerber",
        "key.advantages": "Hauptvorteile",
        "superior.ai.capabilities": "Überlegene KI-Fähigkeiten",
        "more.intuitive.interface": "Intuitivere Benutzeroberfläche",
        "better.integration.ecosystem": "Besseres Integrations-Ökosystem",
        "faster.performance": "Schnellere Leistung",
        "more.competitive.pricing": "Wettbewerbsfähigere Preise",
        "stronger.security.features": "Stärkere Sicherheitsfunktionen",
        "unique.differentiators": "Einzigartige Unterscheidungsmerkmale",
        "advanced.automation.engine": "Fortschrittliche Automatisierungs-Engine",
        "real-time.collaboration.features": "Echtzeit-Kollaborationsfunktionen",
        "predictive.analytics": "Prädiktive Analysen",
        "custom.workflow.builder": "Individueller Workflow-Builder",
        "enterprise-grade.scalability": "Enterprise-Grade-Skalierbarkeit",
        "explore.{tool}s.interface": "Erkunden Sie die Benutzeroberfläche von {tool}:",
        "frequently.asked.questions": "Häufig gestellte Fragen",
        "for.most.organizations.yes.the": "Für die meisten Forschungsorganisationen ja. KI-gestützte Automatisierung und Produktivitätsgewinne bieten in der Regel einen starken ROI in den ersten Monaten. Die Skalierbarkeit und umfangreichen Funktionen der Plattform rechtfertigen die Kosten für wachsende Teams.",
        "most.teams.can.get.started": "Die meisten Teams können innerhalb eines Tages loslegen. Die grundlegende Einrichtung dauert Minuten, während die vollständige Enterprise-Bereitstellung mit benutzerdefinierten Integrationen bei richtiger Planung normalerweise 1-2 Wochen dauert.",
        "{tool}.integrates.with.100.popular": "{tool} lässt sich in über 100 beliebte Plattformen wie Slack, Microsoft Teams, Salesforce, Google Workspace und viele mehr integrieren. Eine robuste API ermöglicht benutzerdefinierte Integrationen.",
        "yes.{tool}.uses.bank-grade.encryption": "Ja. {tool} verwendet Verschlüsselung auf Bankniveau, besitzt SOC 2 Type II-Zertifizierung und ist DSGVO-, HIPAA- und anderen wichtigen Vorschriften konform. Daten werden im Ruhezustand und während der Übertragung verschlüsselt.",
        "absolutely.{tool}.provides.migration.tools": "Auf jeden Fall. {tool} bietet Migrationswerkzeuge und dedizierten Support, um Ihnen einen nahtlosen Übergang von konkurrierenden Plattformen mit minimaler Ausfallzeit zu ermöglichen.",
        "professional.plans.include.email.support": "Professional-Pläne beinhalten E-Mail-Support mit 24-Stunden-Reaktionszeit. Enterprise-Kunden erhalten dedizierte Account Manager, Priority-Support und SLA-Garantien.",
        "yes.you.can.try.all": "Ja! Sie können alle Professional-Funktionen 14 Tage lang kostenlos testen, ohne Kreditkarte. Der kostenlose Plan ist unbegrenzt für die Grundnutzung verfügbar.",
        "the.ai.engine.learns.from": "Die KI-Engine lernt aus Ihren Nutzungsmustern, um Optimierungen vorzuschlagen, repetitive Aufgaben zu automatisieren, Ergebnisse vorherzusagen und intelligente Empfehlungen zu geben, die sich im Laufe der Zeit verbessern.",
        "final.verdict": "Abschließendes Urteil",
        "excellent.choice": "Ausgezeichnete Wahl",
        "{tool}.is.a.powerful.feature-rich": "{tool} ist eine leistungsstarke, funktionsreiche Forschungsplattform, die außergewöhnlichen Wert für Teams jeder Größe bietet. Sehr empfehlenswert.",
        "faq.is.{tool}.worth.the.investment": "Lohnt sich die Investition in {tool}?",
        "faq.how.long.does.implementation.take": "Wie lange dauert die Implementierung?",
        "faq.what.integrations.are.available": "Welche Integrationen sind verfügbar?",
        "faq.is.my.data.secure": "Sind meine Daten sicher?",
        "faq.can.i.migrate.from.another.platform": "Kann ich von einer anderen Plattform migrieren?",
        "faq.what.kind.of.support.is.available": "Welche Art von Support ist verfügbar?",
        "faq.does.{tool}.offer.a.free.trial": "Bietet {tool} eine kostenlose Testversion an?",
        "faq.how.does.ai.enhance.the.platform": "Wie verbessert KI die Plattform?"
    }
}

# Ajouter les autres langues (ES, FR, PT, ZH, JA, KO, AR, HI)
# Pour l'instant je vais juste faire EN et DE, puis on peut étendre

def create_i18n_file(tool):
    """Crée le fichier i18n.js pour un outil"""
    tool_name = tool_names[tool]

    translations = {
        "en": {},
        "de": {},
        "es": {},
        "fr": {},
        "pt": {},
        "zh": {},
        "ja": {},
        "ko": {},
        "ar": {},
        "hi": {}
    }

    # Pour chaque langue
    for lang in ["en", "de"]:  # On commence avec EN et DE
        if lang in generic_translations:
            for key_template, value_template in generic_translations[lang].items():
                # Remplacer {tool} par le nom de l'outil
                key = f"review.{tool}.{key_template}"
                value = value_template.replace("{tool}", tool_name)

                # Enlever {tool} des clés
                key = key.replace(".{tool}.", f".{tool}.")
                key = key.replace("{tool}", tool.replace("-", "."))

                translations[lang][key] = value

    # Générer le contenu du fichier JavaScript
    tool_camel = ''.join(word.capitalize() for word in tool.replace('-', ' ').split())
    tool_camel = tool_camel[0].lower() + tool_camel[1:]

    js_content = f"// {tool_name.upper()} I18N\n"
    js_content += f"const {tool_camel}Translations = {{\n"

    for lang in ["en", "de"]:
        js_content += f'  "{lang}": {{\n'
        for key, value in translations[lang].items():
            # Échapper les guillemets
            escaped_value = value.replace('"', '\\"').replace("'", "\\'")
            js_content += f'    "{key}": "{escaped_value}",\n'
        js_content = js_content.rstrip(',\n') + '\n'
        js_content += f'  }},\n'

    # Ajouter les langues vides pour l'instant
    for lang in ["es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]:
        js_content += f'  "{lang}": {{}},\n'

    js_content = js_content.rstrip(',\n') + '\n'
    js_content += "};\n\n"
    js_content += "// Event-driven translation system\n"
    js_content += f"document.addEventListener('languageChanged', (e) => {{\n"
    js_content += f"  const lang = e.detail.language;\n"
    js_content += f"  if ({tool_camel}Translations[lang]) {{\n"
    js_content += f"    Object.entries({tool_camel}Translations[lang]).forEach(([key, value]) => {{\n"
    js_content += f"      const elements = document.querySelectorAll(`[data-i18n=\"${{key}}\"]`);\n"
    js_content += f"      elements.forEach(el => el.textContent = value);\n"
    js_content += f"    }});\n"
    js_content += f"  }}\n"
    js_content += f"}});\n"

    return js_content

print("=" * 70)
print("CREATING I18N FILES FOR AI RESEARCH & ACADEMIA TOOLS")
print("=" * 70)

count = 0
for tool in tools:
    js_file = os.path.join(js_dir, f"{tool}-i18n.js")

    # Créer le fichier i18n
    js_content = create_i18n_file(tool)

    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(js_content)

    print(f"\n{tool}: [OK] Created {tool}-i18n.js")
    count += 1

print("\n" + "=" * 70)
print(f"[COMPLETE] Created i18n files for {count}/{len(tools)} tools")
print("=" * 70)
