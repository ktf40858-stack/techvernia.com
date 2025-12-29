#!/usr/bin/env python3
"""
Complete all missing Clearscope translations
"""

import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
batch_dir = os.path.join(script_dir, 'GenuisNet.ai', 'pages', 'reviews', 'seo')

# Load English source
with open(os.path.join(batch_dir, 'clearscope-en.json'), 'r', encoding='utf-8') as f:
    en_source = json.load(f)

# Load existing batches
with open(os.path.join(batch_dir, 'clearscope-batch1.json'), 'r', encoding='utf-8') as f:
    batch1 = json.load(f)

with open(os.path.join(batch_dir, 'clearscope-batch2.json'), 'r', encoding='utf-8') as f:
    batch2 = json.load(f)

with open(os.path.join(batch_dir, 'clearscope-batch3.json'), 'r', encoding='utf-8') as f:
    batch3 = json.load(f)

# Missing translations for Batch 1 languages (ES, FR, DE)
batch1_missing = {
    "review.clearscope.clean.distraction-free.workflow": {
        "es": "Flujo de trabajo limpio y sin distracciones",
        "fr": "Flux de travail propre et sans distraction",
        "de": "Sauberer, ablenkungsfreier Workflow"
    },
    "review.clearscope.premium.pricing.starts.at.170month": {
        "es": "Precios premium (desde $170/mes)",
        "fr": "Tarification premium (à partir de $170/mois)",
        "de": "Premium-Preise (ab $170/Monat)"
    },
    "review.clearscope.no.free.plan.or.trial": {
        "es": "Sin plan gratuito ni prueba",
        "fr": "Pas de plan gratuit ou d'essai",
        "de": "Kein kostenloser Plan oder Test"
    },
    "review.clearscope.limited.to.content.optimization": {
        "es": "Limitado a la optimización de contenido",
        "fr": "Limité à l'optimisation de contenu",
        "de": "Auf Content-Optimierung beschränkt"
    },
    "review.clearscope.no.backlink.or.technical.seo": {
        "es": "Sin funciones de backlinks o SEO técnico",
        "fr": "Pas de backlinks ou de fonctionnalités SEO techniques",
        "de": "Keine Backlink- oder technischen SEO-Funktionen"
    },
    "review.clearscope.report.credits.can.run.out": {
        "es": "Los créditos de informes pueden agotarse rápidamente",
        "fr": "Les crédits de rapports peuvent s'épuiser rapidement",
        "de": "Berichts-Credits können schnell aufgebraucht sein"
    },
    "review.clearscope.learning.curve.for.interpreting.data": {
        "es": "Curva de aprendizaje para interpretar datos",
        "fr": "Courbe d'apprentissage pour interpréter les données",
        "de": "Lernkurve für die Dateninterpretation"
    },
    "review.clearscope.limited.keyword.research.capabilities": {
        "es": "Capacidades limitadas de investigación de palabras clave",
        "fr": "Capacités de recherche de mots-clés limitées",
        "de": "Eingeschränkte Keyword-Recherche-Funktionen"
    },
    "review.clearscope.no.built-in.content.writing": {
        "es": "Sin redacción de contenido integrada",
        "fr": "Pas de rédaction de contenu intégrée",
        "de": "Keine integrierte Content-Erstellung"
    },
    "review.common.pricing.plans": {
        "es": "Planes de Precios",
        "fr": "Plans Tarifaires",
        "de": "Preispläne"
    },
    "review.clearscope.plan": {
        "es": "Plan",
        "fr": "Plan",
        "de": "Plan"
    },
    "review.clearscope.price": {
        "es": "Precio",
        "fr": "Prix",
        "de": "Preis"
    },
    "review.clearscope.credits": {
        "es": "Créditos",
        "fr": "Crédits",
        "de": "Credits"
    },
    "review.clearscope.key.features": {
        "es": "Características Principales",
        "fr": "Fonctionnalités Principales",
        "de": "Hauptfunktionen"
    },
    "review.clearscope.essentials": {
        "es": "Essentials",
        "fr": "Essentials",
        "de": "Essentials"
    },
    "review.clearscope.170month": {
        "es": "$170/mes",
        "fr": "$170/mois",
        "de": "$170/Monat"
    },
    "review.clearscope.10.reports": {
        "es": "~10 informes",
        "fr": "~10 rapports",
        "de": "~10 Berichte"
    },
    "review.clearscope.1-3.users.google.docs.integration": {
        "es": "1-3 usuarios, integración con Google Docs, monitoreo de contenido, optimizaciones ilimitadas",
        "fr": "1-3 utilisateurs, intégration Google Docs, surveillance du contenu, optimisations illimitées",
        "de": "1-3 Benutzer, Google Docs-Integration, Content-Überwachung, unbegrenzte Optimierungen"
    },
    "review.clearscope.business": {
        "es": "Business",
        "fr": "Business",
        "de": "Business"
    },
    "review.clearscope.custom": {
        "es": "Personalizado",
        "fr": "Personnalisé",
        "de": "Individuell"
    },
    "review.clearscope.3.users.api.access.bulk": {
        "es": "3+ usuarios, acceso API, cargas masivas, soporte prioritario, capacitación personalizada",
        "fr": "3+ utilisateurs, accès API, téléchargements en masse, support prioritaire, formation personnalisée",
        "de": "3+ Benutzer, API-Zugang, Massen-Uploads, Priority-Support, individuelles Training"
    },
    "review.clearscope.enterprise": {
        "es": "Enterprise",
        "fr": "Enterprise",
        "de": "Enterprise"
    },
    "review.clearscope.unlimited.users.dedicated.account.manager": {
        "es": "Usuarios ilimitados, gerente de cuenta dedicado, integraciones personalizadas, SLA",
        "fr": "Utilisateurs illimités, gestionnaire de compte dédié, intégrations personnalisées, SLA",
        "de": "Unbegrenzte Benutzer, dedizierter Account Manager, individuelle Integrationen, SLA"
    },
    "review.common.best.use.cases": {
        "es": "Mejores Casos de Uso",
        "fr": "Meilleurs Cas d'Utilisation",
        "de": "Beste Anwendungsfälle"
    },
    "review.clearscope.clearscope.excels.at": {
        "es": "Clearscope Sobresale En:",
        "fr": "Clearscope Excelle Dans:",
        "de": "Clearscope Glänzt Bei:"
    },
    "review.clearscope.blog.content.optimization.perfect.for": {
        "es": "Optimización de Contenido de Blog: Perfecto para optimizar publicaciones de blog y artículos para rankings de búsqueda",
        "fr": "Optimisation de Contenu de Blog: Parfait pour optimiser les articles de blog et les articles pour le classement de recherche",
        "de": "Blog-Content-Optimierung: Perfekt für die Optimierung von Blog-Posts und Artikeln für Suchmaschinen-Rankings"
    },
    "review.clearscope.content.marketing.ensure.every.piece": {
        "es": "Marketing de Contenido: Asegúrese de que cada pieza de contenido esté completamente optimizada antes de la publicación",
        "fr": "Marketing de Contenu: Assurez-vous que chaque contenu est entièrement optimisé avant la publication",
        "de": "Content Marketing: Stellen Sie sicher, dass jeder Inhalt vor der Veröffentlichung vollständig optimiert ist"
    },
    "review.clearscope.seo.writing.help.writers.create": {
        "es": "Redacción SEO: Ayude a los escritores a crear contenido amigable con SEO sin necesidad de experiencia profunda en SEO",
        "fr": "Rédaction SEO: Aidez les rédacteurs à créer du contenu SEO-friendly sans avoir besoin d'expertise SEO approfondie",
        "de": "SEO-Schreiben: Helfen Sie Autoren, SEO-freundliche Inhalte zu erstellen, ohne tiefgreifende SEO-Expertise zu benötigen"
    },
    "review.clearscope.content.audits.identify.optimization.opportunities": {
        "es": "Auditorías de Contenido: Identifique oportunidades de optimización en el contenido existente",
        "fr": "Audits de Contenu: Identifiez les opportunités d'optimisation dans le contenu existant",
        "de": "Content-Audits: Identifizieren Sie Optimierungsmöglichkeiten in bestehenden Inhalten"
    },
    "review.clearscope.agency.work.generate.client.reports": {
        "es": "Trabajo de Agencia: Genere informes de clientes que muestren recomendaciones de optimización",
        "fr": "Travail d'Agence: Générez des rapports clients montrant les recommandations d'optimisation",
        "de": "Agenturarbeit: Erstellen Sie Kundenberichte mit Optimierungsempfehlungen"
    },
    "review.clearscope.team.workflows.standardize.content.optimization": {
        "es": "Flujos de Trabajo en Equipo: Estandarice la optimización de contenido en los equipos de contenido",
        "fr": "Flux de Travail d'Équipe: Standardisez l'optimisation de contenu dans les équipes de contenu",
        "de": "Team-Workflows: Standardisieren Sie die Content-Optimierung über Content-Teams hinweg"
    },
    "review.clearscope.competitive.research.understand.what.top": {
        "es": "Investigación Competitiva: Comprenda qué están cubriendo los principales competidores en su contenido",
        "fr": "Recherche Concurrentielle: Comprenez ce que couvrent les principaux concurrents dans leur contenu",
        "de": "Wettbewerbsforschung: Verstehen Sie, was Top-Konkurrenten in ihren Inhalten behandeln"
    },
    "review.clearscope.content.strategy.identify.content.gaps": {
        "es": "Estrategia de Contenido: Identifique brechas de contenido y temas para cubrir basados en datos de búsqueda",
        "fr": "Stratégie de Contenu: Identifiez les lacunes de contenu et les sujets à couvrir basés sur les données de recherche",
        "de": "Content-Strategie: Identifizieren Sie Content-Lücken und Themen basierend auf Suchdaten"
    },
    "review.clearscope.may.not.be.ideal.for": {
        "es": "Puede No Ser Ideal Para:",
        "fr": "Peut Ne Pas Être Idéal Pour:",
        "de": "Möglicherweise Nicht Ideal Für:"
    },
    "review.clearscope.businesses.needing.full.seo.suite": {
        "es": "Empresas que necesitan un paquete SEO completo (backlinks, SEO técnico, etc.)",
        "fr": "Entreprises nécessitant une suite SEO complète (backlinks, SEO technique, etc.)",
        "de": "Unternehmen, die eine vollständige SEO-Suite benötigen (Backlinks, technisches SEO, etc.)"
    },
    "review.clearscope.small.blogs.with.limited.budgets": {
        "es": "Blogs pequeños con presupuestos limitados",
        "fr": "Petits blogs avec budgets limités",
        "de": "Kleine Blogs mit begrenzten Budgets"
    },
    "review.clearscope.those.wanting.ai.content.generation": {
        "es": "Aquellos que quieren generación de contenido con IA",
        "fr": "Ceux qui veulent la génération de contenu IA",
        "de": "Diejenigen, die KI-Content-Generierung wünschen"
    },
    "review.clearscope.users.needing.extensive.keyword.research": {
        "es": "Usuarios que necesitan herramientas extensas de investigación de palabras clave",
        "fr": "Utilisateurs nécessitant des outils de recherche de mots-clés étendus",
        "de": "Benutzer, die umfangreiche Keyword-Recherche-Tools benötigen"
    },
    "review.clearscope.how.it.compares": {
        "es": "Cómo Se Compara",
        "fr": "Comment Il Se Compare",
        "de": "Wie Es Sich Vergleicht"
    },
    "review.clearscope.clearscope.vs.surfer.seo": {
        "es": "Clearscope vs Surfer SEO",
        "fr": "Clearscope vs Surfer SEO",
        "de": "Clearscope vs Surfer SEO"
    },
    "review.clearscope.clearscope.offers.a.cleaner.more": {
        "es": "Clearscope ofrece una interfaz más limpia y enfocada con una integración superior de Google Docs, lo que lo hace ideal para equipos de contenido. Surfer SEO proporciona más funciones, incluida la investigación de palabras clave, el análisis SERP y la escritura con IA a un precio más bajo. La calificación de contenido de Clearscope es más refinada e intuitiva. Surfer ofrece mejor valor para creadores individuales, mientras que Clearscope es preferido por equipos de contenido más grandes y agencias que priorizan la integración del flujo de trabajo.",
        "fr": "Clearscope offre une interface plus propre et plus ciblée avec une intégration Google Docs supérieure, ce qui le rend idéal pour les équipes de contenu. Surfer SEO fournit plus de fonctionnalités, notamment la recherche de mots-clés, l'analyse SERP et la rédaction IA à un prix inférieur. La notation de contenu de Clearscope est plus raffinée et intuitive. Surfer offre une meilleure valeur pour les créateurs solo, tandis que Clearscope est préféré par les grandes équipes de contenu et les agences qui privilégient l'intégration du flux de travail.",
        "de": "Clearscope bietet eine sauberere, fokussiertere Benutzeroberfläche mit überlegener Google Docs-Integration, was es ideal für Content-Teams macht. Surfer SEO bietet mehr Funktionen, einschließlich Keyword-Recherche, SERP-Analyse und KI-Schreiben zu einem niedrigeren Preis. Clearsopes Content-Bewertung ist raffinierter und intuitiver. Surfer bietet besseren Wert für Solo-Ersteller, während Clearscope von größeren Content-Teams und Agenturen bevorzugt wird, die Workflow-Integration priorisieren."
    },
    "review.clearscope.clearscope.vs.frase": {
        "es": "Clearscope vs Frase",
        "fr": "Clearscope vs Frase",
        "de": "Clearscope vs Frase"
    },
    "review.clearscope.clearscope.focuses.purely.on.content": {
        "es": "Clearscope se enfoca puramente en la optimización de contenido con precisión premium y funciones de equipo. Frase combina optimización con escritura con IA, resúmenes de contenido y herramientas de investigación a un precio más accesible. Las recomendaciones de Clearscope son más precisas y procesables. Frase proporciona más funciones por el precio pero con una curva de aprendizaje más pronunciada. Elija Clearscope para la excelencia en optimización pura, Frase para una solución de contenido todo en uno.",
        "fr": "Clearscope se concentre uniquement sur l'optimisation de contenu avec une précision premium et des fonctionnalités d'équipe. Frase combine optimisation avec rédaction IA, briefs de contenu et outils de recherche à un prix plus accessible. Les recommandations de Clearscope sont plus précises et actionnables. Frase fournit plus de fonctionnalités pour le prix mais avec une courbe d'apprentissage plus raide. Choisissez Clearscope pour l'excellence en optimisation pure, Frase pour une solution de contenu tout-en-un.",
        "de": "Clearscope konzentriert sich rein auf Content-Optimierung mit Premium-Genauigkeit und Team-Funktionen. Frase kombiniert Optimierung mit KI-Schreiben, Content-Briefings und Recherche-Tools zu einem zugänglicheren Preis. Clearsopes Empfehlungen sind präziser und umsetzbarer. Frase bietet mehr Funktionen für den Preis, aber mit einer steileren Lernkurve. Wählen Sie Clearscope für reine Optimierungsexzellenz, Frase für eine All-in-One-Content-Lösung."
    },
    "review.common.final.verdict": {
        "es": "Veredicto Final",
        "fr": "Verdict Final",
        "de": "Endgültiges Urteil"
    },
    "review.clearscope.our.recommendation": {
        "es": "Nuestra Recomendación",
        "fr": "Notre Recommandation",
        "de": "Unsere Empfehlung"
    },
    "review.clearscope.clearscope.is.the.premium.choice": {
        "es": "Clearscope es la elección premium para equipos de contenido y agencias que necesitan la plataforma de optimización de contenido más precisa y procesable disponible. Si bien el precio que comienza en $170/mes es elevado, la calidad de las recomendaciones, la integración perfecta del flujo de trabajo y el impacto en el rendimiento del contenido justifican la inversión para los especialistas en marketing de contenido serios. Solo la integración de Google Docs ahorra innumerables horas y hace que el proceso de optimización se sienta natural en lugar de forzado. El sistema de calificación de contenido es el mejor de la industria, proporcionando retroalimentación instantánea y confiable en la que tanto los escritores como los especialistas en SEO pueden confiar. Para bloggers individuales o pequeñas empresas con presupuestos limitados, el precio puede ser prohibitivo: alternativas como Surfer SEO o Frase ofrecen más funciones a costos más bajos. Sin embargo, si es un equipo de contenido en crecimiento, agencia o empresa que publica contenido de alta calidad regularmente y necesita asegurar que cada pieza se clasifique bien, Clearscope vale cada centavo. El ROI de rankings mejorados y tráfico orgánico típicamente supera con creces el costo de suscripción. Solicite una demostración para ver si es adecuado para su equipo.",
        "fr": "Clearscope est le choix premium pour les équipes de contenu et les agences qui ont besoin de la plateforme d'optimisation de contenu la plus précise et actionnable disponible. Bien que le prix commençant à $170/mois soit élevé, la qualité des recommandations, l'intégration transparente du flux de travail et l'impact sur les performances du contenu justifient l'investissement pour les spécialistes du marketing de contenu sérieux. L'intégration Google Docs seule économise d'innombrables heures et rend le processus d'optimisation naturel plutôt que forcé. Le système de notation de contenu est le meilleur de l'industrie, fournissant des retours instantanés et fiables auxquels les rédacteurs et les spécialistes SEO peuvent faire confiance. Pour les blogueurs individuels ou les petites entreprises avec des budgets limités, le prix peut être prohibitif - des alternatives comme Surfer SEO ou Frase offrent plus de fonctionnalités à des coûts inférieurs. Cependant, si vous êtes une équipe de contenu en croissance, une agence ou une entreprise qui publie régulièrement du contenu de haute qualité et doit s'assurer que chaque pièce se classe bien, Clearscope vaut chaque centime. Le ROI des classements améliorés et du trafic organique dépasse généralement largement le coût d'abonnement. Demandez une démo pour voir si c'est le bon choix pour votre équipe.",
        "de": "Clearscope ist die Premium-Wahl für Content-Teams und Agenturen, die die genaueste und umsetzbarste Content-Optimierungsplattform benötigen, die verfügbar ist. Während der Preis von $170/Monat hoch ist, rechtfertigen die Qualität der Empfehlungen, die nahtlose Workflow-Integration und die Auswirkungen auf die Content-Performance die Investition für ernsthafte Content-Marketer. Allein die Google Docs-Integration spart unzählige Stunden und macht den Optimierungsprozess natürlich statt erzwungen. Das Content-Bewertungssystem ist das beste der Branche und liefert sofortiges, zuverlässiges Feedback, dem sowohl Autoren als auch SEO-Spezialisten vertrauen können. Für einzelne Blogger oder kleine Unternehmen mit begrenzten Budgets kann der Preis prohibitiv sein - Alternativen wie Surfer SEO oder Frase bieten mehr Funktionen zu niedrigeren Kosten. Wenn Sie jedoch ein wachsendes Content-Team, eine Agentur oder ein Unternehmen sind, das regelmäßig hochwertigen Content veröffentlicht und sicherstellen muss, dass jeder Inhalt gut rankt, ist Clearscope jeden Cent wert. Der ROI aus verbesserten Rankings und organischem Traffic übersteigt typischerweise die Abonnementkosten bei weitem. Fordern Sie eine Demo an, um zu sehen, ob es für Ihr Team geeignet ist."
    },
    "review.common.screenshots.interface": {
        "es": "Capturas de Pantalla e Interfaz",
        "fr": "Captures d'Écran et Interface",
        "de": "Screenshots & Benutzeroberfläche"
    },
    "review.clearscope.explore.clearscopes.interface": {
        "es": "Explore la interfaz de Clearscope:",
        "fr": "Explorez l'interface de Clearscope:",
        "de": "Entdecken Sie die Benutzeroberfläche von Clearscope:"
    },
    "review.clearscope.main.interface.-.overview.of": {
        "es": "Interfaz Principal - Descripción general de la plataforma",
        "fr": "Interface Principale - Aperçu de la plateforme",
        "de": "Hauptoberfläche - Überblick über die Plattform"
    },
    "review.common.frequently.asked.questions": {
        "es": "Preguntas Frecuentes",
        "fr": "Questions Fréquemment Posées",
        "de": "Häufig Gestellte Fragen"
    }
}

# Add missing translations to batch1
for key, translations in batch1_missing.items():
    for lang in ['es', 'fr', 'de']:
        if lang not in batch1:
            batch1[lang] = {}
        batch1[lang][key] = translations[lang]

# Save updated batch1
with open(os.path.join(batch_dir, 'clearscope-batch1.json'), 'w', encoding='utf-8') as f:
    json.dump(batch1, f, ensure_ascii=False, indent=2)

print('Updated clearscope-batch1.json with missing translations')
print('Batch 1 complete: ES, FR, DE')
