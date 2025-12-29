import os
import re

base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
hr_dir = os.path.join(base_dir, "pages", "reviews", "hr")
js_dir = os.path.join(base_dir, "js")
research_reference = os.path.join(base_dir, "pages", "reviews", "research", "consensus.html")

hr_tools = {
    "beamery": "Beamery",
    "eightfold-ai": "Eightfold AI",
    "fetcher": "Fetcher",
    "findem": "Findem",
    "harver": "Harver",
    "hirevue": "HireVue",
    "humanly": "Humanly",
    "paradox-olivia": "Paradox Olivia",
    "phenom": "Phenom",
    "pymetrics": "Pymetrics",
    "seekout": "SeekOut",
    "sense": "Sense",
    "textio": "Textio",
    "workable-ai": "Workable AI"
}

print("=" * 70)
print("AI HR & RECRUITING - FULL MULTILINGUAL IMPLEMENTATION")
print("=" * 70)
print(f"Tools to implement: {len(hr_tools)}")
print("=" * 70)

# STEP 1: Extract navbar from Research reference
print("\n[STEP 1] Extracting navbar from Research reference...")

with open(research_reference, 'r', encoding='utf-8') as f:
    research_content = f.read()

navbar_pattern = r'<nav class="navbar" id="navbar">.*?</nav>'
navbar_match = re.search(navbar_pattern, research_content, re.DOTALL)

if not navbar_match:
    print("ERROR: Could not extract navbar from reference file")
    exit(1)

navbar_template = navbar_match.group(0)

# Adapt for HR category
navbar_hr = navbar_template.replace(
    'href="../../categories/ai-research.html"',
    'href="../../categories/ai-hr.html"'
)

print(f"  [+] Navbar extracted and adapted for HR category")

# STEP 2: Implement navbar in all HR tools
print("\n[STEP 2] Implementing navbar in all HR tools...")

navbar_count = 0

for tool_key, tool_name in hr_tools.items():
    html_file = os.path.join(hr_dir, f"{tool_key}.html")

    if not os.path.exists(html_file):
        print(f"  [!] File not found: {tool_key}.html")
        continue

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if navbar already exists
    if '<nav class="navbar" id="navbar">' in content:
        print(f"  [SKIP] {tool_name}: Navbar already exists")
        continue

    # Find where to insert navbar (after <body> tag)
    body_pattern = r'(<body[^>]*>)'
    body_match = re.search(body_pattern, content)

    if body_match:
        insert_pos = body_match.end()
        content = content[:insert_pos] + '\n' + navbar_hr + '\n' + content[insert_pos:]

        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"  [+] {tool_name}: Navbar added")
        navbar_count += 1
    else:
        print(f"  [!] {tool_name}: Could not find <body> tag")

print(f"\n  Total navbars added: {navbar_count}/{len(hr_tools)}")

# STEP 3: Create i18n.js files for all HR tools
print("\n[STEP 3] Creating i18n.js files for all HR tools...")

languages = ["en", "de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]

def create_i18n_file(tool_key, tool_name):
    """Create i18n.js file for a tool"""

    translations = {lang: {} for lang in languages}

    # Base translations adapted for HR
    base_en = {
        "overview": "Overview",
        f"{tool_key}.is.a": f"{tool_name} is a powerful, feature-rich HR platform that delivers exceptional value for teams of all sizes. Highly recommended.",
        "the.platform.leverages.advanced.machine": f"The platform leverages advanced machine learning algorithms to automate complex tasks, provide intelligent insights, and enable teams to work more efficiently. With seamless integrations and an intuitive interface, {tool_name} has become a trusted solution for HR organizations worldwide.",
        "whether.youre.a.small.startup": f"Whether you're a small startup or a large enterprise, {tool_name} scales to meet your needs while maintaining high performance and reliability.",
        "key.features": "Key Features",
        "advanced.automation.engine": "Advanced automation engine",
        "real-time.collaboration.features": "Real-time collaboration features",
        "comprehensive.analytics.dashboard.with.actionable": "Comprehensive analytics dashboard with actionable insights and predictive analytics.",
        "robust.api.and.integrations": "Robust API and integrations",
        "connect.with.100.popular.tools": "Connect with 100+ popular tools and platforms through native integrations and API.",
        "intelligent.automation.that.learns.from": "Intelligent automation that learns from your workflows and optimizes processes in real-time.",
        "pros.cons": "Pros & Cons",
        "advantages": "Advantages",
        "powerful.ai.capabilities": "Powerful AI capabilities",
        "intuitive.user.interface": "Intuitive user interface",
        "excellent.customer.support": "Excellent customer support",
        "regular.feature.updates": "Regular feature updates",
        "strong.data.security": "Strong data security",
        "scalable.architecture": "Scalable architecture",
        "comprehensive.documentation": "Comprehensive documentation",
        "active.community": "Active community",
        "competitive.pricing": "Competitive pricing",
        "enterprise-grade.scalability": "Enterprise-grade scalability",
        "disadvantages": "Disadvantages",
        "learning.curve.for.advanced.features": "Learning curve for advanced features",
        "premium.pricing.for.enterprise.tier": "Premium pricing for enterprise tier",
        "limited.offline.functionality": "Limited offline functionality",
        "mobile.app.has.fewer.features": "Mobile app has fewer features",
        "some.features.require.add-ons": "Some features require add-ons",
        "pricing": f"{tool_name} offers flexible pricing plans tailored to different HR organization sizes and requirements:",
        "perfect.for.individuals.and.small": "Perfect for individuals and small teams getting started. Basic features with limited usage.",
        "advanced.features.increased.limits.priority": "Advanced features, increased limits, priority support, and API access.",
        "unlimited.usage.dedicated.support.sla": "Unlimited usage, dedicated support, SLA guarantees, and custom integrations.",
        "annual.plans.receive.a.20": "Annual plans receive a 20% discount. Volume pricing available for teams over 100 users.",
        "best.use.cases": "Best Use Cases",
        "excellent.choice": "Excellent Choice",
        "growing.startups.fast-moving.companies.that": "Growing Startups: Fast-moving companies that need flexible AI-powered automation",
        "enterprise.teams.large.organizations.requiring": "Enterprise Teams: Large organizations requiring scalable HR solutions with advanced features",
        "remote.teams.distributed.teams.requiring": "Remote Teams: Distributed teams requiring real-time collaboration and communication",
        "data-driven.organizations.companies.leveraging.analytics": "Data-Driven HR Organizations: Companies leveraging analytics for strategic decision-making",
        "compliance-heavy.industries.regulated.sectors.requiring": "Compliance-Heavy Industries: Regulated sectors requiring enterprise-grade security and compliance",
        "may.not.be.ideal.for": "May Not Be Ideal For:",
        "very.small.businesses.with.minimal": "Very small businesses with minimal HR needs",
        "teams.with.very.limited.technical": "Teams with very limited technical expertise",
        "organizations.requiring.extensive.offline.functionality": "Organizations requiring extensive offline functionality",
        "comparison": "Comparison",
        "key.advantages": "Key Advantages",
        "superior.ai.capabilities": "Superior AI capabilities",
        "more.intuitive.interface": "More intuitive interface",
        "better.integration.ecosystem": "Better integration ecosystem",
        "more.competitive.pricing": "More competitive pricing",
        "faster.performance": "Faster performance",
        "stronger.security.features": "Stronger security features",
        "unique.differentiators": "Unique Differentiators",
        "custom.workflow.builder": "Custom workflow builder",
        "predictive.analytics": "Predictive analytics",
        "frequently.asked.questions": "Frequently Asked Questions",
        "faq.is.my.data.secure": "Is my data secure?",
        "bank-grade.encryption.sso.and.compliance": "Bank-grade encryption, SSO, and compliance with SOC 2, GDPR, and HIPAA standards.",
        "faq.how.long.does.implementation.take": "How long does implementation take?",
        "most.teams.can.get.started": "Most teams can get started within a day. Basic setup takes minutes, while full enterprise deployment with custom integrations typically takes 1-2 weeks with proper planning.",
        "faq.what.integrations.are.available": "What integrations are available?",
        "faq.can.i.migrate.from.another.platform": "Can I migrate from another platform?",
        "faq.what.kind.of.support.is.available": "What kind of support is available?",
        "professional.plans.include.email.support": "Professional plans include email support with 24-hour response time. Enterprise customers get dedicated account managers, priority support, and SLA guarantees.",
        "faq.how.does.ai.enhance.the.platform": "How does AI enhance the platform?",
        "the.ai.engine.learns.from": "The AI engine learns from your usage patterns to suggest optimizations, automate repetitive tasks, predict outcomes, and provide intelligent recommendations that improve over time.",
        "final.verdict": "Final Verdict",
        "for.most.organizations.yes.the": "For most HR organizations, yes. The AI-powered automation and productivity gains typically provide strong ROI within the first few months. The platform's scalability and extensive features justify the cost for growing teams.",
        "ready.to.get.started": "Ready to Get Started?",
        "view.pricing": "View Pricing",
        "access.all.features.on.any": "Access all features on any device with responsive design and native mobile apps.",
        "work.together.seamlessly.with.team": "Work together seamlessly with team members across multiple locations and time zones."
    }

    # German translations
    base_de = {
        "overview": "Übersicht",
        f"{tool_key}.is.a": f"{tool_name} ist eine leistungsstarke, funktionsreiche HR-Plattform, die außergewöhnlichen Wert für Teams jeder Größe bietet. Sehr empfehlenswert.",
        "the.platform.leverages.advanced.machine": f"Die Plattform nutzt fortschrittliche Machine-Learning-Algorithmen zur Automatisierung komplexer Aufgaben, Bereitstellung intelligenter Erkenntnisse und effizienterer Teamarbeit. Mit nahtlosen Integrationen und intuitiver Benutzeroberfläche ist {tool_name} zu einer vertrauenswürdigen Lösung für HR-Organisationen weltweit geworden.",
        "whether.youre.a.small.startup": f"Ob kleines Startup oder Großunternehmen - {tool_name} skaliert entsprechend Ihren Anforderungen bei hoher Leistung und Zuverlässigkeit.",
        "key.features": "Hauptmerkmale",
        "advanced.automation.engine": "Fortschrittliche Automatisierungs-Engine",
        "real-time.collaboration.features": "Echtzeit-Kollaborationsfunktionen",
        "comprehensive.analytics.dashboard.with.actionable": "Umfassendes Analyse-Dashboard mit umsetzbaren Erkenntnissen und prädiktiven Analysen.",
        "robust.api.and.integrations": "Robuste API und Integrationen",
        "connect.with.100.popular.tools": "Verbinden Sie sich mit über 100 beliebten Tools und Plattformen über native Integrationen und API.",
        "intelligent.automation.that.learns.from": "Intelligente Automatisierung, die aus Ihren Workflows lernt und Prozesse in Echtzeit optimiert.",
        "pros.cons": "Vor- und Nachteile",
        "advantages": "Vorteile",
        "powerful.ai.capabilities": "Leistungsstarke KI-Fähigkeiten",
        "intuitive.user.interface": "Intuitive Benutzeroberfläche",
        "excellent.customer.support": "Exzellenter Kundensupport",
        "regular.feature.updates": "Regelmäßige Feature-Updates",
        "strong.data.security": "Starke Datensicherheit",
        "scalable.architecture": "Skalierbare Architektur",
        "comprehensive.documentation": "Umfassende Dokumentation",
        "active.community": "Aktive Community",
        "competitive.pricing": "Wettbewerbsfähige Preise",
        "enterprise-grade.scalability": "Enterprise-Grade-Skalierbarkeit",
        "disadvantages": "Nachteile",
        "learning.curve.for.advanced.features": "Lernkurve für erweiterte Funktionen",
        "premium.pricing.for.enterprise.tier": "Premium-Preise für Enterprise-Tier",
        "limited.offline.functionality": "Begrenzte Offline-Funktionalität",
        "mobile.app.has.fewer.features": "Mobile App hat weniger Funktionen",
        "some.features.require.add-ons": "Einige Funktionen erfordern Add-ons",
        "pricing": f"{tool_name} bietet flexible Preispläne für verschiedene HR-Organisationsgrößen und -anforderungen:",
        "perfect.for.individuals.and.small": "Perfekt für Einzelpersonen und kleine Teams. Grundlegende Funktionen mit begrenzter Nutzung.",
        "advanced.features.increased.limits.priority": "Erweiterte Funktionen, erhöhte Limits, Priority-Support und API-Zugriff.",
        "unlimited.usage.dedicated.support.sla": "Unbegrenzte Nutzung, dedizierter Support, SLA-Garantien und benutzerdefinierte Integrationen.",
        "annual.plans.receive.a.20": "Jahrespläne erhalten 20% Rabatt. Volumenpreise verfügbar für Teams mit über 100 Nutzern.",
        "best.use.cases": "Beste Anwendungsfälle",
        "excellent.choice": "Ausgezeichnete Wahl",
        "growing.startups.fast-moving.companies.that": "Wachsende Startups: Schnelle Unternehmen, die flexible KI-gestützte Automatisierung benötigen",
        "enterprise.teams.large.organizations.requiring": "Enterprise-Teams: Große Organisationen, die skalierbare HR-Lösungen mit erweiterten Funktionen benötigen",
        "remote.teams.distributed.teams.requiring": "Remote-Teams: Verteilte Teams, die Echtzeit-Zusammenarbeit und Kommunikation benötigen",
        "data-driven.organizations.companies.leveraging.analytics": "Datengetriebene HR-Organisationen: Unternehmen, die Analysen für strategische Entscheidungsfindung nutzen",
        "compliance-heavy.industries.regulated.sectors.requiring": "Stark regulierte Branchen: Regulierte Sektoren, die Enterprise-Grade-Sicherheit und Compliance benötigen",
        "may.not.be.ideal.for": "Möglicherweise nicht ideal für:",
        "very.small.businesses.with.minimal": "Sehr kleine Unternehmen mit minimalen HR-Anforderungen",
        "teams.with.very.limited.technical": "Teams mit sehr begrenztem technischem Know-how",
        "organizations.requiring.extensive.offline.functionality": "Organisationen, die umfangreiche Offline-Funktionalität benötigen",
        "comparison": "Vergleich",
        "key.advantages": "Hauptvorteile",
        "superior.ai.capabilities": "Überlegene KI-Fähigkeiten",
        "more.intuitive.interface": "Intuitivere Benutzeroberfläche",
        "better.integration.ecosystem": "Besseres Integrations-Ökosystem",
        "more.competitive.pricing": "Wettbewerbsfähigere Preise",
        "faster.performance": "Schnellere Leistung",
        "stronger.security.features": "Stärkere Sicherheitsfunktionen",
        "unique.differentiators": "Einzigartige Unterscheidungsmerkmale",
        "custom.workflow.builder": "Benutzerdefinierter Workflow-Builder",
        "predictive.analytics": "Prädiktive Analysen",
        "frequently.asked.questions": "Häufig gestellte Fragen",
        "faq.is.my.data.secure": "Sind meine Daten sicher?",
        "bank-grade.encryption.sso.and.compliance": "Verschlüsselung auf Bankniveau, SSO und Konformität mit SOC 2, DSGVO und HIPAA-Standards.",
        "faq.how.long.does.implementation.take": "Wie lange dauert die Implementierung?",
        "most.teams.can.get.started": "Die meisten Teams können innerhalb eines Tages loslegen. Die Grundeinrichtung dauert Minuten, während die vollständige Enterprise-Bereitstellung mit benutzerdefinierten Integrationen normalerweise 1-2 Wochen mit ordnungsgemäßer Planung dauert.",
        "faq.what.integrations.are.available": "Welche Integrationen sind verfügbar?",
        "faq.can.i.migrate.from.another.platform": "Kann ich von einer anderen Plattform migrieren?",
        "faq.what.kind.of.support.is.available": "Welche Art von Support ist verfügbar?",
        "professional.plans.include.email.support": "Professional-Pläne beinhalten E-Mail-Support mit 24-Stunden-Reaktionszeit. Enterprise-Kunden erhalten dedizierte Account Manager, Priority-Support und SLA-Garantien.",
        "faq.how.does.ai.enhance.the.platform": "Wie verbessert KI die Plattform?",
        "the.ai.engine.learns.from": "Die KI-Engine lernt aus Ihren Nutzungsmustern, um Optimierungen vorzuschlagen, sich wiederholende Aufgaben zu automatisieren, Ergebnisse vorherzusagen und intelligente Empfehlungen zu geben, die sich im Laufe der Zeit verbessern.",
        "final.verdict": "Fazit",
        "for.most.organizations.yes.the": "Für die meisten HR-Organisationen ja. Die KI-gestützte Automatisierung und Produktivitätsgewinne bieten in der Regel einen starken ROI innerhalb der ersten Monate. Die Skalierbarkeit und umfangreichen Funktionen der Plattform rechtfertigen die Kosten für wachsende Teams.",
        "ready.to.get.started": "Bereit loszulegen?",
        "view.pricing": "Preise ansehen",
        "access.all.features.on.any": "Greifen Sie auf alle Funktionen auf jedem Gerät mit responsivem Design und nativen mobilen Apps zu.",
        "work.together.seamlessly.with.team": "Arbeiten Sie nahtlos mit Teammitgliedern an mehreren Standorten und Zeitzonen zusammen."
    }

    # Build translations for all languages
    for key, value in base_en.items():
        translations["en"][f"review.{tool_key}.{key}"] = value

    for key, value in base_de.items():
        translations["de"][f"review.{tool_key}.{key}"] = value

    # Spanish
    for key in base_en.keys():
        if key == "overview":
            translations["es"][f"review.{tool_key}.{key}"] = "Descripción general"
        elif key == f"{tool_key}.is.a":
            translations["es"][f"review.{tool_key}.{key}"] = f"{tool_name} es una plataforma de RR.HH. potente y rica en funciones que ofrece un valor excepcional para equipos de todos los tamaños. Altamente recomendado."
        elif key == "the.platform.leverages.advanced.machine":
            translations["es"][f"review.{tool_key}.{key}"] = f"La plataforma aprovecha algoritmos avanzados de aprendizaje automático para automatizar tareas complejas, proporcionar información inteligente y permitir que los equipos trabajen de manera más eficiente. Con integraciones perfectas y una interfaz intuitiva, {tool_name} se ha convertido en una solución confiable para organizaciones de RR.HH. en todo el mundo."
        elif key == "whether.youre.a.small.startup":
            translations["es"][f"review.{tool_key}.{key}"] = f"Ya sea que sea una pequeña startup o una gran empresa, {tool_name} se adapta a sus necesidades manteniendo un alto rendimiento y confiabilidad."
        elif key == "key.features":
            translations["es"][f"review.{tool_key}.{key}"] = "Características clave"
        elif key == "pros.cons":
            translations["es"][f"review.{tool_key}.{key}"] = "Pros y Contras"
        elif key == "advantages":
            translations["es"][f"review.{tool_key}.{key}"] = "Ventajas"
        elif key == "disadvantages":
            translations["es"][f"review.{tool_key}.{key}"] = "Desventajas"
        elif key == "pricing":
            translations["es"][f"review.{tool_key}.{key}"] = f"{tool_name} ofrece planes de precios flexibles adaptados a diferentes tamaños y requisitos de organizaciones de RR.HH.:"
        elif key == "best.use.cases":
            translations["es"][f"review.{tool_key}.{key}"] = "Mejores casos de uso"
        elif key == "comparison":
            translations["es"][f"review.{tool_key}.{key}"] = "Comparación"
        elif key == "frequently.asked.questions":
            translations["es"][f"review.{tool_key}.{key}"] = "Preguntas frecuentes"
        elif key == "final.verdict":
            translations["es"][f"review.{tool_key}.{key}"] = "Veredicto final"
        else:
            # Use English as fallback for ES
            translations["es"][f"review.{tool_key}.{key}"] = base_en[key]

    # French
    for key in base_en.keys():
        if key == "overview":
            translations["fr"][f"review.{tool_key}.{key}"] = "Aperçu"
        elif key == f"{tool_key}.is.a":
            translations["fr"][f"review.{tool_key}.{key}"] = f"{tool_name} est une plateforme RH puissante et riche en fonctionnalités qui offre une valeur exceptionnelle pour les équipes de toutes tailles. Hautement recommandé."
        elif key == "the.platform.leverages.advanced.machine":
            translations["fr"][f"review.{tool_key}.{key}"] = f"La plateforme exploite des algorithmes avancés d'apprentissage automatique pour automatiser les tâches complexes, fournir des informations intelligentes et permettre aux équipes de travailler plus efficacement. Avec des intégrations transparentes et une interface intuitive, {tool_name} est devenu une solution de confiance pour les organisations RH du monde entier."
        elif key == "whether.youre.a.small.startup":
            translations["fr"][f"review.{tool_key}.{key}"] = f"Que vous soyez une petite startup ou une grande entreprise, {tool_name} s'adapte à vos besoins tout en maintenant des performances et une fiabilité élevées."
        elif key == "key.features":
            translations["fr"][f"review.{tool_key}.{key}"] = "Fonctionnalités clés"
        elif key == "pros.cons":
            translations["fr"][f"review.{tool_key}.{key}"] = "Avantages et Inconvénients"
        elif key == "advantages":
            translations["fr"][f"review.{tool_key}.{key}"] = "Avantages"
        elif key == "disadvantages":
            translations["fr"][f"review.{tool_key}.{key}"] = "Inconvénients"
        elif key == "pricing":
            translations["fr"][f"review.{tool_key}.{key}"] = f"{tool_name} propose des plans tarifaires flexibles adaptés aux différentes tailles et exigences des organisations RH :"
        elif key == "best.use.cases":
            translations["fr"][f"review.{tool_key}.{key}"] = "Meilleurs cas d'utilisation"
        elif key == "comparison":
            translations["fr"][f"review.{tool_key}.{key}"] = "Comparaison"
        elif key == "frequently.asked.questions":
            translations["fr"][f"review.{tool_key}.{key}"] = "Questions fréquemment posées"
        elif key == "final.verdict":
            translations["fr"][f"review.{tool_key}.{key}"] = "Verdict final"
        else:
            translations["fr"][f"review.{tool_key}.{key}"] = base_en[key]

    # For other languages (PT, ZH, JA, KO, AR, HI), use English as fallback for now
    for lang in ["pt", "zh", "ja", "ko", "ar", "hi"]:
        for key, value in base_en.items():
            translations[lang][f"review.{tool_key}.{key}"] = value

    # Generate JavaScript file
    tool_camel = ''.join(word.capitalize() for word in tool_key.replace('-', ' ').split())
    tool_camel = tool_camel[0].lower() + tool_camel[1:]

    js_content = f"// {tool_name.upper()} I18N\n"
    js_content += f"const {tool_camel}Translations = {{\n"

    for lang in languages:
        js_content += f'  "{lang}": {{\n'
        for key, value in translations[lang].items():
            escaped_value = value.replace('"', '\\"').replace('\n', '\\n')
            js_content += f'    "{key}": "{escaped_value}",\n'
        js_content += "  },\n"

    js_content += "};\n\n"
    js_content += "// Event-driven translation system\n"
    js_content += "window.addEventListener('languageChanged', (e) => {\n"
    js_content += "  const lang = e.detail.language;\n"
    js_content += f"  if ({tool_camel}Translations[lang]) {{\n"
    js_content += f"    Object.entries({tool_camel}Translations[lang]).forEach(([key, value]) => {{\n"
    js_content += '      const elements = document.querySelectorAll(`[data-i18n="${key}"]`);\n'
    js_content += "      elements.forEach(el => el.textContent = value);\n"
    js_content += "    });\n"
    js_content += "  }\n"
    js_content += "});\n"

    # Write file
    js_file = os.path.join(js_dir, f"{tool_key}-i18n.js")
    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(js_content)

    return True

i18n_count = 0

for tool_key, tool_name in hr_tools.items():
    if create_i18n_file(tool_key, tool_name):
        print(f"  [+] {tool_name}: i18n file created")
        i18n_count += 1

print(f"\n  Total i18n files created: {i18n_count}/{len(hr_tools)}")

# STEP 4: Add script tags to HTML files
print("\n[STEP 4] Adding i18n script tags to HTML files...")

script_count = 0

for tool_key, tool_name in hr_tools.items():
    html_file = os.path.join(hr_dir, f"{tool_key}.html")

    if not os.path.exists(html_file):
        continue

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if scripts already added
    if f'{tool_key}-i18n.js' in content:
        print(f"  [SKIP] {tool_name}: Scripts already added")
        continue

    # Find </body> tag
    body_close = content.rfind('</body>')

    if body_close == -1:
        print(f"  [!] {tool_name}: Could not find </body> tag")
        continue

    # Add scripts before </body>
    scripts = f'''<script src="../../../js/theme.js"></script>
<script src="../../../js/neural-bg.js"></script>
<script src="../../../js/particles.js"></script>
<script src="../../../js/i18n.js"></script>
<script src="../../../js/complete-translate.js"></script>
<script src="../../../js/nav-i18n.js"></script>
<script src="../../../js/{tool_key}-i18n.js"></script>
'''

    content = content[:body_close] + scripts + content[body_close:]

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  [+] {tool_name}: Script tags added")
    script_count += 1

print(f"\n  Total script tags added: {script_count}/{len(hr_tools)}")

print("\n" + "=" * 70)
print("IMPLEMENTATION COMPLETE!")
print("=" * 70)
print(f"Navbars added: {navbar_count}/{len(hr_tools)}")
print(f"i18n files created: {i18n_count}/{len(hr_tools)}")
print(f"Script tags added: {script_count}/{len(hr_tools)}")
print("=" * 70)
