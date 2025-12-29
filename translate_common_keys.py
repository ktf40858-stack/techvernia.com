import os
import re

js_dir = r"C:\Users\Freddy\Desktop\GeniisNet.ai\GenuisNet.ai\js"

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

# Common translations that don't depend on tool name
common_translations = {
    "de": {
        # Features
        "advanced.automation.engine": "Fortschrittliche Automatisierungs-Engine",
        "real-time.collaboration.features": "Echtzeit-Kollaborationsfunktionen",
        "robust.api.and.integrations": "Robuste API und Integrationen",

        # Pros
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

        # Cons
        "learning.curve.for.advanced.features": "Lernkurve für erweiterte Funktionen",
        "premium.pricing.for.enterprise.tier": "Premium-Preise für Enterprise-Tier",
        "limited.offline.functionality": "Eingeschränkte Offline-Funktionalität",
        "mobile.app.has.fewer.features": "Mobile App hat weniger Funktionen",
        "some.features.require.add-ons": "Einige Funktionen erfordern Add-ons",

        # Pricing
        "perfect.for.individuals.and.small": "Perfekt für Einzelpersonen und kleine Teams für den Einstieg. Grundfunktionen mit begrenzter Nutzung.",
        "advanced.features.increased.limits.priority": "Erweiterte Funktionen, erhöhte Limits, priorisierter Support und API-Zugang.",
        "unlimited.usage.dedicated.support.sla": "Unbegrenzte Nutzung, dedizierter Support, SLA-Garantien und benutzerdefinierte Integrationen.",
        "annual.plans.receive.a.20": "Jahrespläne erhalten 20% Rabatt. Mengenpreise verfügbar für Teams über 100 Benutzer.",

        # Use Cases
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

        # Comparison
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

        # FAQ Answers
        "most.teams.can.get.started": "Die meisten Teams können innerhalb eines Tages loslegen. Die Grundeinrichtung dauert Minuten, während die vollständige Enterprise-Bereitstellung mit benutzerdefinierten Integrationen bei guter Planung typischerweise 1-2 Wochen dauert.",
        "professional.plans.include.email.support": "Professional-Pläne beinhalten E-Mail-Support mit 24-Stunden-Reaktionszeit. Enterprise-Kunden erhalten dedizierte Account Manager, priorisierten Support und SLA-Garantien.",
        "the.ai.engine.learns.from": "Die KI-Engine lernt aus Ihren Nutzungsmustern, um Optimierungen vorzuschlagen, sich wiederholende Aufgaben zu automatisieren, Ergebnisse vorherzusagen und intelligente Empfehlungen zu geben, die sich im Laufe der Zeit verbessern.",
    },
    "es": {
        # Features
        "advanced.automation.engine": "Motor de automatización avanzado",
        "real-time.collaboration.features": "Funciones de colaboración en tiempo real",
        "robust.api.and.integrations": "API e integraciones robustas",

        # Pros
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

        # Cons
        "learning.curve.for.advanced.features": "Curva de aprendizaje para funciones avanzadas",
        "premium.pricing.for.enterprise.tier": "Precios premium para el nivel empresarial",
        "limited.offline.functionality": "Funcionalidad offline limitada",
        "mobile.app.has.fewer.features": "La app móvil tiene menos funciones",
        "some.features.require.add-ons": "Algunas funciones requieren complementos",

        # Pricing
        "perfect.for.individuals.and.small": "Perfecto para individuos y equipos pequeños que comienzan. Funciones básicas con uso limitado.",
        "advanced.features.increased.limits.priority": "Funciones avanzadas, límites aumentados, soporte prioritario y acceso a API.",
        "unlimited.usage.dedicated.support.sla": "Uso ilimitado, soporte dedicado, garantías SLA e integraciones personalizadas.",
        "annual.plans.receive.a.20": "Los planes anuales reciben un 20% de descuento. Precios por volumen disponibles para equipos de más de 100 usuarios.",

        # Use Cases
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

        # Comparison
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

        # FAQ Answers
        "most.teams.can.get.started": "La mayoría de los equipos pueden comenzar en un día. La configuración básica toma minutos, mientras que la implementación empresarial completa con integraciones personalizadas generalmente toma 1-2 semanas con una planificación adecuada.",
        "professional.plans.include.email.support": "Los planes profesionales incluyen soporte por correo electrónico con tiempo de respuesta de 24 horas. Los clientes empresariales obtienen gerentes de cuenta dedicados, soporte prioritario y garantías SLA.",
        "the.ai.engine.learns.from": "El motor de IA aprende de sus patrones de uso para sugerir optimizaciones, automatizar tareas repetitivas, predecir resultados y proporcionar recomendaciones inteligentes que mejoran con el tiempo.",
    },
    "fr": {
        # Features
        "advanced.automation.engine": "Moteur d'automatisation avancé",
        "real-time.collaboration.features": "Fonctionnalités de collaboration en temps réel",
        "robust.api.and.integrations": "API et intégrations robustes",

        # Pros
        "powerful.ai.capabilities": "Capacités IA puissantes",
        "intuitive.user.interface": "Interface utilisateur intuitive",
        "excellent.customer.support": "Excellent support client",
        "regular.feature.updates": "Mises à jour régulières des fonctionnalités",
        "strong.data.security": "Sécurité des données robuste",
        "scalable.architecture": "Architecture évolutive",
        "comprehensive.documentation": "Documentation complète",
        "active.community": "Communauté active",
        "competitive.pricing": "Tarification compétitive",
        "enterprise-grade.scalability": "Évolutivité de niveau entreprise",

        # Cons
        "learning.curve.for.advanced.features": "Courbe d'apprentissage pour les fonctionnalités avancées",
        "premium.pricing.for.enterprise.tier": "Tarification premium pour le niveau entreprise",
        "limited.offline.functionality": "Fonctionnalité hors ligne limitée",
        "mobile.app.has.fewer.features": "L'application mobile a moins de fonctionnalités",
        "some.features.require.add-ons": "Certaines fonctionnalités nécessitent des modules complémentaires",
    },
    "pt": {
        # Features
        "advanced.automation.engine": "Motor de automação avançado",
        "real-time.collaboration.features": "Recursos de colaboração em tempo real",
        "robust.api.and.integrations": "API e integrações robustas",

        # Pros
        "powerful.ai.capabilities": "Recursos de IA poderosos",
        "intuitive.user.interface": "Interface de usuário intuitiva",
        "excellent.customer.support": "Excelente suporte ao cliente",
        "regular.feature.updates": "Atualizações regulares de recursos",
        "strong.data.security": "Segurança de dados robusta",
        "scalable.architecture": "Arquitetura escalável",
        "comprehensive.documentation": "Documentação abrangente",
        "active.community": "Comunidade ativa",
        "competitive.pricing": "Preços competitivos",
        "enterprise-grade.scalability": "Escalabilidade de nível empresarial",
    },
    "zh": {
        "advanced.automation.engine": "高级自动化引擎",
        "real-time.collaboration.features": "实时协作功能",
        "robust.api.and.integrations": "强大的API和集成",
        "powerful.ai.capabilities": "强大的AI功能",
        "intuitive.user.interface": "直观的用户界面",
        "excellent.customer.support": "出色的客户支持",
        "regular.feature.updates": "定期功能更新",
        "strong.data.security": "强大的数据安全性",
        "scalable.architecture": "可扩展架构",
        "comprehensive.documentation": "全面的文档",
        "active.community": "活跃的社区",
        "competitive.pricing": "有竞争力的价格",
        "enterprise-grade.scalability": "企业级可扩展性",
    },
    "ja": {
        "advanced.automation.engine": "高度な自動化エンジン",
        "real-time.collaboration.features": "リアルタイムコラボレーション機能",
        "robust.api.and.integrations": "堅牢なAPIと統合",
        "powerful.ai.capabilities": "強力なAI機能",
        "intuitive.user.interface": "直感的なユーザーインターフェース",
        "excellent.customer.support": "優れたカスタマーサポート",
        "regular.feature.updates": "定期的な機能更新",
        "strong.data.security": "強力なデータセキュリティ",
        "scalable.architecture": "スケーラブルなアーキテクチャ",
        "comprehensive.documentation": "包括的なドキュメント",
        "active.community": "アクティブなコミュニティ",
        "competitive.pricing": "競争力のある価格",
        "enterprise-grade.scalability": "エンタープライズグレードのスケーラビリティ",
    },
    "ko": {
        "advanced.automation.engine": "고급 자동화 엔진",
        "real-time.collaboration.features": "실시간 협업 기능",
        "robust.api.and.integrations": "강력한 API 및 통합",
        "powerful.ai.capabilities": "강력한 AI 기능",
        "intuitive.user.interface": "직관적인 사용자 인터페이스",
        "excellent.customer.support": "우수한 고객 지원",
        "regular.feature.updates": "정기적인 기능 업데이트",
        "strong.data.security": "강력한 데이터 보안",
        "scalable.architecture": "확장 가능한 아키텍처",
        "comprehensive.documentation": "포괄적인 문서",
        "active.community": "활발한 커뮤니티",
        "competitive.pricing": "경쟁력 있는 가격",
        "enterprise-grade.scalability": "엔터프라이즈급 확장성",
    },
    "ar": {
        "advanced.automation.engine": "محرك أتمتة متقدم",
        "real-time.collaboration.features": "ميزات التعاون في الوقت الفعلي",
        "robust.api.and.integrations": "واجهة برمجة تطبيقات قوية وتكاملات",
        "powerful.ai.capabilities": "قدرات ذكاء اصطناعي قوية",
        "intuitive.user.interface": "واجهة مستخدم بديهية",
        "excellent.customer.support": "دعم عملاء ممتاز",
        "regular.feature.updates": "تحديثات منتظمة للميزات",
        "strong.data.security": "أمان بيانات قوي",
        "scalable.architecture": "بنية قابلة للتوسع",
        "comprehensive.documentation": "وثائق شاملة",
        "active.community": "مجتمع نشط",
        "competitive.pricing": "أسعار تنافسية",
        "enterprise-grade.scalability": "قابلية توسع على مستوى المؤسسات",
    },
    "hi": {
        "advanced.automation.engine": "उन्नत स्वचालन इंजन",
        "real-time.collaboration.features": "रियल-टाइम सहयोग सुविधाएं",
        "robust.api.and.integrations": "मजबूत API और एकीकरण",
        "powerful.ai.capabilities": "शक्तिशाली AI क्षमताएं",
        "intuitive.user.interface": "सहज उपयोगकर्ता इंटरफ़ेस",
        "excellent.customer.support": "उत्कृष्ट ग्राहक सहायता",
        "regular.feature.updates": "नियमित सुविधा अपडेट",
        "strong.data.security": "मजबूत डेटा सुरक्षा",
        "scalable.architecture": "स्केलेबल आर्किटेक्चर",
        "comprehensive.documentation": "व्यापक दस्तावेज़ीकरण",
        "active.community": "सक्रिय समुदाय",
        "competitive.pricing": "प्रतिस्पर्धी मूल्य निर्धारण",
        "enterprise-grade.scalability": "एंटरप्राइज़-ग्रेड स्केलेबिलिटी",
    }
}

def replace_common_translations(tool_key, tool_name):
    """Replace common English placeholders with proper translations"""

    js_file = os.path.join(js_dir, f"{tool_key}-i18n.js")

    if not os.path.exists(js_file):
        return False

    with open(js_file, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False

    for lang, translations in common_translations.items():
        for key_suffix, translation in translations.items():
            full_key = f"review.{tool_key}.{key_suffix}"

            # Find and replace the English placeholder
            # Pattern: "full_key": "English text",
            pattern = rf'("{re.escape(full_key)}":\s*)"([^"\\]*(?:\\.[^"\\]*)*)"'

            def replacer(match):
                nonlocal modified
                current_value = match.group(2)
                # Only replace if current value is in English (contains common English words)
                english_markers = ["Advanced", "Real-time", "Robust", "Powerful", "Intuitive",
                                 "Excellent", "Regular", "Strong", "Scalable", "Comprehensive",
                                 "Active", "Competitive", "Enterprise", "Learning", "Premium",
                                 "Limited", "Perfect", "Unlimited", "Growing", "Remote",
                                 "Data-driven", "Compliance", "Superior", "Better", "Faster",
                                 "Stronger", "Custom", "Predictive", "Most teams"]

                if any(marker in current_value for marker in english_markers):
                    modified = True
                    escaped_translation = translation.replace('"', '\\"')
                    return f'{match.group(1)}"{escaped_translation}"'
                return match.group(0)

            content = re.sub(pattern, replacer, content)

    if modified:
        with open(js_file, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False

print("=" * 70)
print("TRANSLATING COMMON KEYS")
print("=" * 70)

fixed_count = 0

for tool_key, tool_name in translation_tools.items():
    print(f"\n{tool_name}:")
    if replace_common_translations(tool_key, tool_name):
        print(f"  [+] Common translations applied")
        fixed_count += 1
    else:
        print(f"  [OK] Already translated or not applicable")

print("\n" + "=" * 70)
print(f"COMPLETE: {fixed_count}/10 tools updated with proper translations")
print("=" * 70)
