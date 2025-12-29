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

# Complete translations for all missing keys
# Using generic translations that work for all translation tools
all_translations = {
    "de": {
        "advanced.automation.engine": "Fortschrittliche Automatisierungs-Engine",
        "real-time.collaboration.features": "Echtzeit-Kollaborationsfunktionen",
        "robust.api.and.integrations": "Robuste API und Integrationen",
        "powerful.ai.capabilities": "Leistungsstarke KI-Funktionen",
        "intuitive.user.interface": "Intuitive Benutzeroberfläche",
        "excellent.customer.support": "Exzellenter Kundensupport",
        "regular.feature.updates": "Regelmäßige Feature-Updates",
        "strong.data.security": "Starke Datensicherheit",
        "scalable.architecture": "Skalierbare Architektur",
        "comprehensive.documentation": "Umfassende Dokumentation",
        "active.community": "Aktive Community",
        "competitive.pricing": "Wettbewerbsfähige Preise",
        "enterprise-grade.scalability": "Skalierbarkeit auf Enterprise-Niveau",
        "learning.curve.for.advanced.features": "Lernkurve für erweiterte Funktionen",
        "premium.pricing.for.enterprise.tier": "Premium-Preise für Enterprise-Tier",
        "limited.offline.functionality": "Eingeschränkte Offline-Funktionalität",
        "mobile.app.has.fewer.features": "Mobile App hat weniger Funktionen",
        "some.features.require.add-ons": "Einige Funktionen erfordern Add-ons",
        "perfect.for.individuals.and.small": "Perfekt für Einzelpersonen und kleine Teams für den Einstieg. Grundfunktionen mit begrenzter Nutzung.",
        "advanced.features.increased.limits.priority": "Erweiterte Funktionen, erhöhte Limits, priorisierter Support und API-Zugang.",
        "unlimited.usage.dedicated.support.sla": "Unbegrenzte Nutzung, dedizierter Support, SLA-Garantien und benutzerdefinierte Integrationen.",
        "annual.plans.receive.a.20": "Jahrespläne erhalten 20% Rabatt. Mengenpreise verfügbar für Teams über 100 Benutzer.",
        "excellent.choice": "Ausgezeichnete Wahl",
        "growing.startups.fast-moving.companies.that": "Wachsende Startups: Schnelllebige Unternehmen, die flexible KI-gestützte Automatisierung benötigen",
        "enterprise.teams.large.organizations.requiring": "Enterprise-Teams: Große Organisationen, die skalierbare Übersetzungslösungen mit erweiterten Funktionen benötigen",
        "remote.teams.distributed.teams.requiring": "Remote-Teams: Verteilte Teams, die Echtzeit-Zusammenarbeit und Kommunikation benötigen",
        "data-driven.organizations.companies.leveraging.analytics": "Datengesteuerte Organisationen: Unternehmen, die Analysen für strategische Entscheidungen nutzen",
        "compliance-heavy.industries.regulated.sectors.requiring": "Compliance-intensive Branchen: Regulierte Sektoren, die Enterprise-Sicherheit und Compliance benötigen",
        "may.not.be.ideal.for": "Möglicherweise nicht ideal für:",
        "very.small.businesses.with.minimal": "Sehr kleine Unternehmen mit minimalen Übersetzungsbedürfnissen",
        "teams.with.very.limited.technical": "Teams mit sehr begrenzter technischer Expertise",
        "organizations.requiring.extensive.offline.functionality": "Organisationen, die umfangreiche Offline-Funktionalität benötigen",
        "key.advantages": "Hauptvorteile",
        "superior.ai.capabilities": "Überlegene KI-Funktionen",
        "more.intuitive.interface": "Intuitivere Benutzeroberfläche",
        "better.integration.ecosystem": "Besseres Integrations-Ökosystem",
        "more.competitive.pricing": "Wettbewerbsfähigere Preise",
        "faster.performance": "Schnellere Leistung",
        "stronger.security.features": "Stärkere Sicherheitsfunktionen",
        "unique.differentiators": "Einzigartige Differenzierungsmerkmale",
        "custom.workflow.builder": "Benutzerdefinierter Workflow-Builder",
        "predictive.analytics": "Prädiktive Analytik",
        "most.teams.can.get.started": "Die meisten Teams können innerhalb eines Tages loslegen. Die Grundeinrichtung dauert Minuten, während die vollständige Enterprise-Bereitstellung mit benutzerdefinierten Integrationen bei guter Planung typischerweise 1-2 Wochen dauert.",
        "professional.plans.include.email.support": "Professional-Pläne beinhalten E-Mail-Support mit 24-Stunden-Reaktionszeit. Enterprise-Kunden erhalten dedizierte Account Manager, priorisierten Support und SLA-Garantien.",
        "the.ai.engine.learns.from": "Die KI-Engine lernt aus Ihren Nutzungsmustern, um Optimierungen vorzuschlagen, sich wiederholende Aufgaben zu automatisieren, Ergebnisse vorherzusagen und intelligente Empfehlungen zu geben, die sich im Laufe der Zeit verbessern.",
        "for.most.organizations.yes.the": "Für die meisten Organisationen ja. Die KI-gestützte Automatisierung und Produktivitätsgewinne bieten in der Regel einen starken ROI innerhalb der ersten Monate. Die Skalierbarkeit und umfangreichen Funktionen der Plattform rechtfertigen die Kosten für wachsende Teams.",
        "try.deepl.pro.today.and": "Testen Sie DeepL Pro heute und erleben Sie die Kraft der KI-gesteuerten Automatisierung.",
        "try.deepl.pro.free": "DeepL Pro kostenlos testen",
    },
    "es": {
        "advanced.automation.engine": "Motor de automatización avanzado",
        "real-time.collaboration.features": "Funciones de colaboración en tiempo real",
        "robust.api.and.integrations": "API e integraciones robustas",
        "powerful.ai.capabilities": "Capacidades de IA potentes",
        "intuitive.user.interface": "Interfaz de usuario intuitiva",
        "excellent.customer.support": "Excelente soporte al cliente",
        "regular.feature.updates": "Actualizaciones regulares de funciones",
        "strong.data.security": "Seguridad de datos robusta",
        "scalable.architecture": "Arquitectura escalable",
        "comprehensive.documentation": "Documentación completa",
        "active.community": "Comunidad activa",
        "competitive.pricing": "Precios competitivos",
        "enterprise-grade.scalability": "Escalabilidad de nivel empresarial",
        "learning.curve.for.advanced.features": "Curva de aprendizaje para funciones avanzadas",
        "premium.pricing.for.enterprise.tier": "Precios premium para el nivel empresarial",
        "limited.offline.functionality": "Funcionalidad offline limitada",
        "mobile.app.has.fewer.features": "La app móvil tiene menos funciones",
        "some.features.require.add-ons": "Algunas funciones requieren complementos",
        "perfect.for.individuals.and.small": "Perfecto para individuos y equipos pequeños que comienzan. Funciones básicas con uso limitado.",
        "advanced.features.increased.limits.priority": "Funciones avanzadas, límites aumentados, soporte prioritario y acceso a API.",
        "unlimited.usage.dedicated.support.sla": "Uso ilimitado, soporte dedicado, garantías SLA e integraciones personalizadas.",
        "annual.plans.receive.a.20": "Los planes anuales reciben un 20% de descuento. Precios por volumen disponibles para equipos de más de 100 usuarios.",
        "excellent.choice": "Excelente elección",
        "growing.startups.fast-moving.companies.that": "Startups en crecimiento: Empresas ágiles que necesitan automatización impulsada por IA flexible",
        "enterprise.teams.large.organizations.requiring": "Equipos empresariales: Grandes organizaciones que requieren soluciones de traducción escalables con funciones avanzadas",
        "remote.teams.distributed.teams.requiring": "Equipos remotos: Equipos distribuidos que requieren colaboración y comunicación en tiempo real",
        "data-driven.organizations.companies.leveraging.analytics": "Organizaciones orientadas a datos: Empresas que aprovechan análisis para toma de decisiones estratégicas",
        "compliance-heavy.industries.regulated.sectors.requiring": "Industrias con alta compliance: Sectores regulados que requieren seguridad y cumplimiento de nivel empresarial",
        "may.not.be.ideal.for": "Puede no ser ideal para:",
        "very.small.businesses.with.minimal": "Empresas muy pequeñas con necesidades mínimas de traducción",
        "teams.with.very.limited.technical": "Equipos con experiencia técnica muy limitada",
        "organizations.requiring.extensive.offline.functionality": "Organizaciones que requieren funcionalidad offline extensa",
        "key.advantages": "Ventajas clave",
        "superior.ai.capabilities": "Capacidades de IA superiores",
        "more.intuitive.interface": "Interfaz más intuitiva",
        "better.integration.ecosystem": "Mejor ecosistema de integración",
        "more.competitive.pricing": "Precios más competitivos",
        "faster.performance": "Rendimiento más rápido",
        "stronger.security.features": "Funciones de seguridad más robustas",
        "unique.differentiators": "Diferenciadores únicos",
        "custom.workflow.builder": "Constructor de flujo de trabajo personalizado",
        "predictive.analytics": "Análisis predictivo",
        "most.teams.can.get.started": "La mayoría de los equipos pueden comenzar en un día. La configuración básica toma minutos, mientras que la implementación empresarial completa con integraciones personalizadas generalmente toma 1-2 semanas con una planificación adecuada.",
        "professional.plans.include.email.support": "Los planes profesionales incluyen soporte por correo electrónico con tiempo de respuesta de 24 horas. Los clientes empresariales obtienen gerentes de cuenta dedicados, soporte prioritario y garantías SLA.",
        "the.ai.engine.learns.from": "El motor de IA aprende de sus patrones de uso para sugerir optimizaciones, automatizar tareas repetitivas, predecir resultados y proporcionar recomendaciones inteligentes que mejoran con el tiempo.",
        "for.most.organizations.yes.the": "Para la mayoría de las organizaciones, sí. La automatización impulsada por IA y las ganancias de productividad suelen proporcionar un ROI sólido en los primeros meses. La escalabilidad y las amplias funciones de la plataforma justifican el costo para equipos en crecimiento.",
    },
    # For brevity, I'll add FR, PT, ZH, JA, KO, AR, HI with shorter lists
    # In production, these would all be complete
}

# Due to size constraints, let me create a more targeted fix
# I'll regenerate the ENTIRE i18n files with ALL translations from the original implementation script

print("=" * 70)
print("This script would be very large. Let me create a different approach.")
print("I'll copy all English keys to other languages as a base.")
print("=" * 70)

def copy_english_to_all_languages(tool_key, tool_name):
    """Copy all English keys to other languages if missing"""

    js_file = os.path.join(js_dir, f"{tool_key}-i18n.js")

    if not os.path.exists(js_file):
        return False

    with open(js_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract all English key-value pairs
    en_pattern = r'"en":\s*\{([^}]+(?:\{[^}]+\}[^}]*)*)\}'
    en_match = re.search(en_pattern, content, re.DOTALL)

    if not en_match:
        return False

    en_section = en_match.group(1)

    # Extract individual key-value pairs
    kv_pattern = r'    "([^"]+)":\s*"([^"\\]*(?:\\.[^"\\]*)*)"'
    en_pairs = re.findall(kv_pattern, en_section)

    print(f"\n{tool_name}:")
    print(f"  Found {len(en_pairs)} English keys")

    # This approach is too simple - we need proper translations
    # Instead, let me suggest regenerating from the original comprehensive data

    return False

# The right solution is to regenerate the i18n files completely
# with the full translation data from the original implementation

print("\nThe issue: Initial i18n files were created with only ~20-30 keys")
print("But the HTML has data-i18n attributes for 80+ keys")
print("\nSolution: Need to regenerate i18n files with ALL translations")
print("This requires the complete translation dictionary from the original script")
