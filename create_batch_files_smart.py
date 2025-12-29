#!/usr/bin/env python3
"""
Smart translation batch file creator
Creates batch translation files using pattern matching and templates
"""

import json
import os

base_dir = r"GenuisNet.ai\pages\reviews\customer-service"

# Tools and their display names
TOOLS = {
    "intercom-fin": "Intercom Fin",
    "kustomer": "Kustomer",
    "liveperson": "LivePerson",
    "netomi": "Netomi",
    "ultimateai": "Ultimate.ai",
    "yellowai": "Yellow.ai",
    "zendesk-ai": "Zendesk AI"
}

# Comprehensive translation patterns for Batch 1 (de, es, fr)
TRANSLATIONS_BATCH1 = {
    "de": {
        # Headers and CTAs
        "Ready to Get Started?": "Bereit loszulegen?",
        "today and experience the power of AI-driven automation.": "noch heute und erleben Sie die Kraft der KI-gesteuerten Automatisierung.",
        "View Pricing": "Preise anzeigen",
        "Overview": "Überblick",

        # Features section
        "Key Features": "Hauptfunktionen",
        "Intelligent automation that learns from your workflows and optimizes processes in real-time.": "Intelligente Automatisierung, die aus Ihren Arbeitsabläufen lernt und Prozesse in Echtzeit optimiert.",
        "Comprehensive analytics dashboard with actionable insights and predictive analytics.": "Umfassendes Analyse-Dashboard mit umsetzbaren Erkenntnissen und prädiktiver Analytik.",
        "Connect with 100+ popular tools and platforms through native integrations and API.": "Verbinden Sie sich mit über 100 beliebten Tools und Plattformen durch native Integrationen und API.",
        "Bank-grade encryption, SSO, and compliance with SOC 2, GDPR, and HIPAA standards.": "Verschlüsselung auf Bankniveau, SSO und Compliance mit SOC 2, DSGVO und HIPAA-Standards.",
        "Work together seamlessly with team members across multiple locations and time zones.": "Arbeiten Sie nahtlos mit Teammitgliedern über mehrere Standorte und Zeitzonen hinweg zusammen.",
        "Access all features on any device with responsive design and native mobile apps.": "Greifen Sie auf alle Funktionen auf jedem Gerät mit responsivem Design und nativen mobilen Apps zu.",

        # Pros & Cons
        "Pros & Cons": "Vor- und Nachteile",
        "Advantages": "Vorteile",
        "Powerful AI capabilities": "Leistungsstarke KI-Funktionen",
        "Intuitive user interface": "Intuitive Benutzeroberfläche",
        "Excellent customer support": "Ausgezeichneter Kundensupport",
        "Regular feature updates": "Regelmäßige Feature-Updates",
        "Robust API and integrations": "Robuste API und Integrationen",
        "Scalable architecture": "Skalierbare Architektur",
        "Competitive pricing": "Wettbewerbsfähige Preise",
        "Comprehensive documentation": "Umfassende Dokumentation",
        "Active community": "Aktive Community",
        "Strong data security": "Starke Datensicherheit",
        "Disadvantages": "Nachteile",
        "Learning curve for advanced features": "Lernkurve für erweiterte Funktionen",
        "Premium pricing for enterprise tier": "Premium-Preise für Enterprise-Stufe",
        "Limited offline functionality": "Eingeschränkte Offline-Funktionalität",
        "Some features require add-ons": "Einige Funktionen erfordern Add-ons",
        "Mobile app has fewer features": "Mobile App hat weniger Funktionen",

        # Pricing
        "Pricing": "Preise",
        "Perfect for individuals and small teams getting started. Basic features with limited usage.": "Perfekt für Einzelpersonen und kleine Teams zum Einstieg. Basisfunktionen mit begrenzter Nutzung.",
        "Advanced features, increased limits, priority support, and API access.": "Erweiterte Funktionen, erhöhte Limits, vorrangiger Support und API-Zugang.",
        "Unlimited usage, dedicated support, SLA guarantees, and custom integrations.": "Unbegrenzte Nutzung, dedizierter Support, SLA-Garantien und individuelle Integrationen.",
        "Annual plans receive a 20% discount. Volume pricing available for teams over 100 users.": "Jahrespläne erhalten 20% Rabatt. Mengenpreise verfügbar für Teams über 100 Benutzer.",

        # Use Cases
        "Best Use Cases": "Beste Anwendungsfälle",
        "Enterprise Teams: Large organizations requiring scalable customer-service solutions with advanced features": "Enterprise-Teams: Große Organisationen, die skalierbare Kundenservice-Lösungen mit erweiterten Funktionen benötigen",
        "Growing Startups: Fast-moving companies that need flexible, AI-powered automation": "Wachsende Startups: Schnell wachsende Unternehmen, die flexible, KI-gestützte Automatisierung benötigen",
        "Remote Teams: Distributed teams requiring real-time collaboration and communication": "Remote-Teams: Verteilte Teams, die Echtzeit-Zusammenarbeit und Kommunikation benötigen",
        "Data-Driven Organizations: Companies leveraging analytics for strategic decision-making": "Datengetriebene Organisationen: Unternehmen, die Analysen für strategische Entscheidungen nutzen",
        "Compliance-Heavy Industries: Regulated sectors requiring enterprise-grade security and compliance": "Stark regulierte Branchen: Regulierte Sektoren, die Sicherheit und Compliance auf Unternehmensniveau benötigen",
        "May Not Be Ideal For:": "Möglicherweise nicht ideal für:",
        "Very small businesses with minimal customer-service needs": "Sehr kleine Unternehmen mit minimalen Kundenservice-Anforderungen",
        "Organizations requiring extensive offline functionality": "Organisationen, die umfassende Offline-Funktionalität benötigen",
        "Teams with very limited technical expertise": "Teams mit sehr begrenztem technischem Fachwissen",

        # Comparison
        "Comparison": "Vergleich",
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

        # Screenshots & FAQs
        "Screenshots & Interface": "Screenshots & Benutzeroberfläche",
        "Frequently Asked Questions": "Häufig gestellte Fragen",
        "For most organizations, yes. The AI-powered automation and productivity gains typically provide strong ROI within the first few months. The platform's scalability and extensive features justify the cost for growing teams.": "Für die meisten Organisationen ja. Die KI-gesteuerte Automatisierung und Produktivitätssteigerungen bieten in der Regel innerhalb der ersten Monate einen starken ROI. Die Skalierbarkeit und umfangreichen Funktionen der Plattform rechtfertigen die Kosten für wachsende Teams.",
        "Most teams can get started within a day. Basic setup takes minutes, while full enterprise deployment with custom integrations typically takes 1-2 weeks with proper planning.": "Die meisten Teams können innerhalb eines Tages beginnen. Die grundlegende Einrichtung dauert Minuten, während die vollständige Enterprise-Bereitstellung mit benutzerdefinierten Integrationen bei ordnungsgemäßer Planung typischerweise 1-2 Wochen dauert.",
        "integrates with 100+ popular platforms including Slack, Microsoft Teams, Salesforce, Google Workspace, and many more. A robust API enables custom integrations.": "integriert sich mit über 100 beliebten Plattformen, darunter Slack, Microsoft Teams, Salesforce, Google Workspace und viele mehr. Eine robuste API ermöglicht individuelle Integrationen.",
        "uses bank-grade encryption, maintains SOC 2 Type II certification, and is compliant with GDPR, HIPAA, and other major regulations. Data is encrypted at rest and in transit.": "verwendet Verschlüsselung auf Bankniveau, hält die SOC 2 Type II-Zertifizierung aufrecht und ist konform mit DSGVO, HIPAA und anderen wichtigen Vorschriften. Daten werden im Ruhezustand und während der Übertragung verschlüsselt.",
        "Yes.": "Ja.",
        "Absolutely.": "Auf jeden Fall.",
        "provides migration tools and dedicated support to help you seamlessly transition from competing platforms with minimal downtime.": "bietet Migrationswerkzeuge und dedizierten Support, um Ihnen einen nahtlosen Übergang von konkurrierenden Plattformen mit minimaler Ausfallzeit zu ermöglichen.",
        "Professional plans include email support with 24-hour response time. Enterprise customers get dedicated account managers, priority support, and SLA guarantees.": "Professional-Pläne beinhalten E-Mail-Support mit 24-Stunden-Reaktionszeit. Enterprise-Kunden erhalten dedizierte Account-Manager, vorrangigen Support und SLA-Garantien.",
        "Yes! You can try all Professional features free for 14 days with no credit card required. The free plan is available indefinitely for basic usage.": "Ja! Sie können alle Professional-Funktionen 14 Tage lang kostenlos ohne Kreditkarte testen. Der kostenlose Plan ist unbegrenzt für die Basisnutzung verfügbar.",
        "The AI engine learns from your usage patterns to suggest optimizations, automate repetitive tasks, predict outcomes, and provide intelligent recommendations that improve over time.": "Die KI-Engine lernt aus Ihren Nutzungsmustern, um Optimierungen vorzuschlagen, sich wiederholende Aufgaben zu automatisieren, Ergebnisse vorherzusagen und intelligente Empfehlungen bereitzustellen, die sich im Laufe der Zeit verbessern.",

        # Final Verdict
        "Final Verdict": "Endgültiges Urteil",
        "Excellent Choice": "Ausgezeichnete Wahl"
    },
    "es": {
        # Headers and CTAs
        "Ready to Get Started?": "¿Listo para comenzar?",
        "today and experience the power of AI-driven automation.": "hoy y experimenta el poder de la automatización impulsada por IA.",
        "View Pricing": "Ver precios",
        "Overview": "Descripción general",

        # Features section
        "Key Features": "Características clave",
        "Intelligent automation that learns from your workflows and optimizes processes in real-time.": "Automatización inteligente que aprende de tus flujos de trabajo y optimiza procesos en tiempo real.",
        "Comprehensive analytics dashboard with actionable insights and predictive analytics.": "Panel de análisis completo con información procesable y análisis predictivo.",
        "Connect with 100+ popular tools and platforms through native integrations and API.": "Conéctate con más de 100 herramientas y plataformas populares a través de integraciones nativas y API.",
        "Bank-grade encryption, SSO, and compliance with SOC 2, GDPR, and HIPAA standards.": "Cifrado de nivel bancario, SSO y cumplimiento con estándares SOC 2, RGPD e HIPAA.",
        "Work together seamlessly with team members across multiple locations and time zones.": "Trabaja sin problemas con miembros del equipo en múltiples ubicaciones y zonas horarias.",
        "Access all features on any device with responsive design and native mobile apps.": "Accede a todas las funciones en cualquier dispositivo con diseño responsivo y aplicaciones móviles nativas.",

        # Pros & Cons
        "Pros & Cons": "Pros y contras",
        "Advantages": "Ventajas",
        "Powerful AI capabilities": "Capacidades de IA potentes",
        "Intuitive user interface": "Interfaz de usuario intuitiva",
        "Excellent customer support": "Excelente soporte al cliente",
        "Regular feature updates": "Actualizaciones regulares de funciones",
        "Robust API and integrations": "API e integraciones robustas",
        "Scalable architecture": "Arquitectura escalable",
        "Competitive pricing": "Precios competitivos",
        "Comprehensive documentation": "Documentación completa",
        "Active community": "Comunidad activa",
        "Strong data security": "Seguridad de datos sólida",
        "Disadvantages": "Desventajas",
        "Learning curve for advanced features": "Curva de aprendizaje para funciones avanzadas",
        "Premium pricing for enterprise tier": "Precios premium para nivel empresarial",
        "Limited offline functionality": "Funcionalidad offline limitada",
        "Some features require add-ons": "Algunas funciones requieren complementos",
        "Mobile app has fewer features": "La app móvil tiene menos funciones",

        # Pricing
        "Pricing": "Precios",
        "Perfect for individuals and small teams getting started. Basic features with limited usage.": "Perfecto para individuos y pequeños equipos que comienzan. Funciones básicas con uso limitado.",
        "Advanced features, increased limits, priority support, and API access.": "Funciones avanzadas, límites aumentados, soporte prioritario y acceso a API.",
        "Unlimited usage, dedicated support, SLA guarantees, and custom integrations.": "Uso ilimitado, soporte dedicado, garantías SLA e integraciones personalizadas.",
        "Annual plans receive a 20% discount. Volume pricing available for teams over 100 users.": "Los planes anuales reciben un 20% de descuento. Precios por volumen disponibles para equipos de más de 100 usuarios.",

        # Use Cases
        "Best Use Cases": "Mejores casos de uso",
        "Enterprise Teams: Large organizations requiring scalable customer-service solutions with advanced features": "Equipos empresariales: Grandes organizaciones que requieren soluciones de servicio al cliente escalables con funciones avanzadas",
        "Growing Startups: Fast-moving companies that need flexible, AI-powered automation": "Startups en crecimiento: Empresas de rápido movimiento que necesitan automatización flexible impulsada por IA",
        "Remote Teams: Distributed teams requiring real-time collaboration and communication": "Equipos remotos: Equipos distribuidos que requieren colaboración y comunicación en tiempo real",
        "Data-Driven Organizations: Companies leveraging analytics for strategic decision-making": "Organizaciones basadas en datos: Empresas que aprovechan análisis para toma de decisiones estratégicas",
        "Compliance-Heavy Industries: Regulated sectors requiring enterprise-grade security and compliance": "Industrias de alto cumplimiento: Sectores regulados que requieren seguridad y cumplimiento de nivel empresarial",
        "May Not Be Ideal For:": "Puede no ser ideal para:",
        "Very small businesses with minimal customer-service needs": "Empresas muy pequeñas con necesidades mínimas de servicio al cliente",
        "Organizations requiring extensive offline functionality": "Organizaciones que requieren funcionalidad offline extensa",
        "Teams with very limited technical expertise": "Equipos con experiencia técnica muy limitada",

        # Comparison
        "Comparison": "Comparación",
        "Key Advantages": "Ventajas clave",
        "Superior AI capabilities": "Capacidades de IA superiores",
        "More intuitive interface": "Interfaz más intuitiva",
        "Better integration ecosystem": "Mejor ecosistema de integración",
        "Faster performance": "Rendimiento más rápido",
        "More competitive pricing": "Precios más competitivos",
        "Stronger security features": "Funciones de seguridad más sólidas",
        "Unique Differentiators": "Diferenciadores únicos",
        "Advanced automation engine": "Motor de automatización avanzado",
        "Real-time collaboration features": "Funciones de colaboración en tiempo real",
        "Predictive analytics": "Análisis predictivo",
        "Custom workflow builder": "Constructor de flujos de trabajo personalizado",
        "Enterprise-grade scalability": "Escalabilidad de nivel empresarial",

        # Screenshots & FAQs
        "Screenshots & Interface": "Capturas de pantalla e interfaz",
        "Frequently Asked Questions": "Preguntas frecuentes",
        "For most organizations, yes. The AI-powered automation and productivity gains typically provide strong ROI within the first few months. The platform's scalability and extensive features justify the cost for growing teams.": "Para la mayoría de las organizaciones, sí. La automatización impulsada por IA y las ganancias de productividad generalmente proporcionan un ROI sólido dentro de los primeros meses. La escalabilidad de la plataforma y las funciones extensas justifican el costo para equipos en crecimiento.",
        "Most teams can get started within a day. Basic setup takes minutes, while full enterprise deployment with custom integrations typically takes 1-2 weeks with proper planning.": "La mayoría de los equipos pueden comenzar en un día. La configuración básica toma minutos, mientras que la implementación empresarial completa con integraciones personalizadas generalmente toma de 1 a 2 semanas con planificación adecuada.",
        "integrates with 100+ popular platforms including Slack, Microsoft Teams, Salesforce, Google Workspace, and many more. A robust API enables custom integrations.": "se integra con más de 100 plataformas populares incluyendo Slack, Microsoft Teams, Salesforce, Google Workspace y muchas más. Una API robusta permite integraciones personalizadas.",
        "uses bank-grade encryption, maintains SOC 2 Type II certification, and is compliant with GDPR, HIPAA, and other major regulations. Data is encrypted at rest and in transit.": "utiliza cifrado de nivel bancario, mantiene certificación SOC 2 Type II y cumple con RGPD, HIPAA y otras regulaciones importantes. Los datos se cifran en reposo y en tránsito.",
        "Yes.": "Sí.",
        "Absolutely.": "Absolutamente.",
        "provides migration tools and dedicated support to help you seamlessly transition from competing platforms with minimal downtime.": "proporciona herramientas de migración y soporte dedicado para ayudarte a realizar una transición sin problemas desde plataformas competidoras con tiempo de inactividad mínimo.",
        "Professional plans include email support with 24-hour response time. Enterprise customers get dedicated account managers, priority support, and SLA guarantees.": "Los planes profesionales incluyen soporte por correo electrónico con tiempo de respuesta de 24 horas. Los clientes empresariales obtienen gerentes de cuenta dedicados, soporte prioritario y garantías SLA.",
        "Yes! You can try all Professional features free for 14 days with no credit card required. The free plan is available indefinitely for basic usage.": "¡Sí! Puedes probar todas las funciones profesionales gratis durante 14 días sin requerir tarjeta de crédito. El plan gratuito está disponible indefinidamente para uso básico.",
        "The AI engine learns from your usage patterns to suggest optimizations, automate repetitive tasks, predict outcomes, and provide intelligent recommendations that improve over time.": "El motor de IA aprende de tus patrones de uso para sugerir optimizaciones, automatizar tareas repetitivas, predecir resultados y proporcionar recomendaciones inteligentes que mejoran con el tiempo.",

        # Final Verdict
        "Final Verdict": "Veredicto final",
        "Excellent Choice": "Excelente opción"
    },
    "fr": {
        # Headers and CTAs
        "Ready to Get Started?": "Prêt à commencer ?",
        "today and experience the power of AI-driven automation.": "aujourd'hui et découvrez la puissance de l'automatisation pilotée par IA.",
        "View Pricing": "Voir les tarifs",
        "Overview": "Vue d'ensemble",

        # Features section
        "Key Features": "Fonctionnalités clés",
        "Intelligent automation that learns from your workflows and optimizes processes in real-time.": "Automatisation intelligente qui apprend de vos flux de travail et optimise les processus en temps réel.",
        "Comprehensive analytics dashboard with actionable insights and predictive analytics.": "Tableau de bord analytique complet avec des informations exploitables et des analyses prédictives.",
        "Connect with 100+ popular tools and platforms through native integrations and API.": "Connectez-vous avec plus de 100 outils et plateformes populaires via des intégrations natives et une API.",
        "Bank-grade encryption, SSO, and compliance with SOC 2, GDPR, and HIPAA standards.": "Chiffrement de niveau bancaire, SSO et conformité aux normes SOC 2, RGPD et HIPAA.",
        "Work together seamlessly with team members across multiple locations and time zones.": "Travaillez en toute fluidité avec les membres de l'équipe à travers plusieurs emplacements et fuseaux horaires.",
        "Access all features on any device with responsive design and native mobile apps.": "Accédez à toutes les fonctionnalités sur n'importe quel appareil avec un design responsive et des applications mobiles natives.",

        # Pros & Cons
        "Pros & Cons": "Avantages et inconvénients",
        "Advantages": "Avantages",
        "Powerful AI capabilities": "Capacités IA puissantes",
        "Intuitive user interface": "Interface utilisateur intuitive",
        "Excellent customer support": "Excellent support client",
        "Regular feature updates": "Mises à jour régulières des fonctionnalités",
        "Robust API and integrations": "API et intégrations robustes",
        "Scalable architecture": "Architecture évolutive",
        "Competitive pricing": "Tarification compétitive",
        "Comprehensive documentation": "Documentation complète",
        "Active community": "Communauté active",
        "Strong data security": "Sécurité des données solide",
        "Disadvantages": "Inconvénients",
        "Learning curve for advanced features": "Courbe d'apprentissage pour fonctionnalités avancées",
        "Premium pricing for enterprise tier": "Tarification premium pour niveau entreprise",
        "Limited offline functionality": "Fonctionnalité hors ligne limitée",
        "Some features require add-ons": "Certaines fonctionnalités nécessitent des modules complémentaires",
        "Mobile app has fewer features": "L'application mobile a moins de fonctionnalités",

        # Pricing
        "Pricing": "Tarification",
        "Perfect for individuals and small teams getting started. Basic features with limited usage.": "Parfait pour les particuliers et petites équipes qui débutent. Fonctionnalités de base avec utilisation limitée.",
        "Advanced features, increased limits, priority support, and API access.": "Fonctionnalités avancées, limites augmentées, support prioritaire et accès API.",
        "Unlimited usage, dedicated support, SLA guarantees, and custom integrations.": "Utilisation illimitée, support dédié, garanties SLA et intégrations personnalisées.",
        "Annual plans receive a 20% discount. Volume pricing available for teams over 100 users.": "Les plans annuels bénéficient d'une réduction de 20 %. Tarification en volume disponible pour les équipes de plus de 100 utilisateurs.",

        # Use Cases
        "Best Use Cases": "Meilleurs cas d'usage",
        "Enterprise Teams: Large organizations requiring scalable customer-service solutions with advanced features": "Équipes d'entreprise : Grandes organisations nécessitant des solutions de service client évolutives avec fonctionnalités avancées",
        "Growing Startups: Fast-moving companies that need flexible, AI-powered automation": "Startups en croissance : Entreprises dynamiques nécessitant une automatisation flexible alimentée par IA",
        "Remote Teams: Distributed teams requiring real-time collaboration and communication": "Équipes distantes : Équipes distribuées nécessitant collaboration et communication en temps réel",
        "Data-Driven Organizations: Companies leveraging analytics for strategic decision-making": "Organisations axées sur les données : Entreprises exploitant les analyses pour prise de décision stratégique",
        "Compliance-Heavy Industries: Regulated sectors requiring enterprise-grade security and compliance": "Industries fortement réglementées : Secteurs réglementés nécessitant sécurité et conformité de niveau entreprise",
        "May Not Be Ideal For:": "Peut ne pas être idéal pour :",
        "Very small businesses with minimal customer-service needs": "Très petites entreprises avec besoins minimaux de service client",
        "Organizations requiring extensive offline functionality": "Organisations nécessitant fonctionnalité hors ligne étendue",
        "Teams with very limited technical expertise": "Équipes avec expertise technique très limitée",

        # Comparison
        "Comparison": "Comparaison",
        "Key Advantages": "Avantages clés",
        "Superior AI capabilities": "Capacités IA supérieures",
        "More intuitive interface": "Interface plus intuitive",
        "Better integration ecosystem": "Meilleur écosystème d'intégration",
        "Faster performance": "Performances plus rapides",
        "More competitive pricing": "Tarification plus compétitive",
        "Stronger security features": "Fonctionnalités de sécurité plus fortes",
        "Unique Differentiators": "Différenciateurs uniques",
        "Advanced automation engine": "Moteur d'automatisation avancé",
        "Real-time collaboration features": "Fonctionnalités de collaboration en temps réel",
        "Predictive analytics": "Analyses prédictives",
        "Custom workflow builder": "Constructeur de flux de travail personnalisé",
        "Enterprise-grade scalability": "Évolutivité de niveau entreprise",

        # Screenshots & FAQs
        "Screenshots & Interface": "Captures d'écran et interface",
        "Frequently Asked Questions": "Questions fréquemment posées",
        "For most organizations, yes. The AI-powered automation and productivity gains typically provide strong ROI within the first few months. The platform's scalability and extensive features justify the cost for growing teams.": "Pour la plupart des organisations, oui. L'automatisation alimentée par IA et les gains de productivité fournissent généralement un ROI solide dans les premiers mois. L'évolutivité de la plateforme et les fonctionnalités étendues justifient le coût pour les équipes en croissance.",
        "Most teams can get started within a day. Basic setup takes minutes, while full enterprise deployment with custom integrations typically takes 1-2 weeks with proper planning.": "La plupart des équipes peuvent démarrer en un jour. La configuration de base prend quelques minutes, tandis que le déploiement complet en entreprise avec intégrations personnalisées prend généralement 1 à 2 semaines avec une planification appropriée.",
        "integrates with 100+ popular platforms including Slack, Microsoft Teams, Salesforce, Google Workspace, and many more. A robust API enables custom integrations.": "s'intègre avec plus de 100 plateformes populaires incluant Slack, Microsoft Teams, Salesforce, Google Workspace et bien d'autres. Une API robuste permet des intégrations personnalisées.",
        "uses bank-grade encryption, maintains SOC 2 Type II certification, and is compliant with GDPR, HIPAA, and other major regulations. Data is encrypted at rest and in transit.": "utilise un chiffrement de niveau bancaire, maintient la certification SOC 2 Type II et est conforme au RGPD, HIPAA et autres réglementations majeures. Les données sont chiffrées au repos et en transit.",
        "Yes.": "Oui.",
        "Absolutely.": "Absolument.",
        "provides migration tools and dedicated support to help you seamlessly transition from competing platforms with minimal downtime.": "fournit des outils de migration et un support dédié pour vous aider à effectuer une transition fluide depuis des plateformes concurrentes avec un temps d'arrêt minimal.",
        "Professional plans include email support with 24-hour response time. Enterprise customers get dedicated account managers, priority support, and SLA guarantees.": "Les plans professionnels incluent le support par e-mail avec temps de réponse de 24 heures. Les clients entreprise obtiennent des gestionnaires de compte dédiés, support prioritaire et garanties SLA.",
        "Yes! You can try all Professional features free for 14 days with no credit card required. The free plan is available indefinitely for basic usage.": "Oui ! Vous pouvez essayer toutes les fonctionnalités professionnelles gratuitement pendant 14 jours sans carte de crédit requise. Le plan gratuit est disponible indéfiniment pour utilisation de base.",
        "The AI engine learns from your usage patterns to suggest optimizations, automate repetitive tasks, predict outcomes, and provide intelligent recommendations that improve over time.": "Le moteur IA apprend de vos modèles d'utilisation pour suggérer des optimisations, automatiser les tâches répétitives, prédire les résultats et fournir des recommandations intelligentes qui s'améliorent avec le temps.",

        # Final Verdict
        "Final Verdict": "Verdict final",
        "Excellent Choice": "Excellent choix"
    }
}

def smart_translate(text, trans_dict, tool_name):
    """Smart translation using pattern matching"""
    # Check for exact match first
    if text in trans_dict:
        return trans_dict[text]

    # Try to find partial matches and substitute
    result = text
    matched = False

    # Sort by length (longest first) to avoid partial replacements
    for en_phrase in sorted(trans_dict.keys(), key=len, reverse=True):
        if en_phrase in result:
            result = result.replace(en_phrase, trans_dict[en_phrase])
            matched = True

    # Replace tool names in result
    for tool_key, tool_display in TOOLS.items():
        result = result.replace(tool_display, tool_name)

    return result if matched else text  # Return original if no match

def create_batch1_for_tool(tool_key, tool_name):
    """Create batch1 file (de, es, fr) for a specific tool"""
    en_file = os.path.join(base_dir, f"{tool_key}-en.json")

    if not os.path.exists(en_file):
        print(f"  [FAIL] {en_file} not found")
        return False

    # Load English source
    with open(en_file, 'r', encoding='utf-8') as f:
        en_data = json.load(f)

    # Create translations
    batch1 = {"de": {}, "es": {}, "fr": {}}

    for key, en_value in en_data.items():
        for lang in ["de", "es", "fr"]:
            batch1[lang][key] = smart_translate(en_value, TRANSLATIONS_BATCH1[lang], tool_name)

    # Save batch file
    batch1_file = os.path.join(base_dir, f"{tool_key}-batch1.json")
    with open(batch1_file, 'w', encoding='utf-8') as f:
        json.dump(batch1, f, indent=2, ensure_ascii=False)

    return True

def main():
    print("="*80)
    print("CREATING BATCH1 TRANSLATION FILES (German, Spanish, French)")
    print("="*80)

    created = 0
    failed = 0

    for tool_key, tool_name in TOOLS.items():
        print(f"\n[{tool_key}] Processing...")
        if create_batch1_for_tool(tool_key, tool_name):
            print(f"  [OK] Created {tool_key}-batch1.json")
            created += 1
        else:
            print(f"  [FAIL] Failed to create {tool_key}-batch1.json")
            failed += 1

    print(f"\n{'='*80}")
    print(f"RESULTS: {created} created, {failed} failed")
    print(f"{'='*80}")

if __name__ == "__main__":
    main()
