import os
import re
import json

# Liste des 14 outils Education
tools = [
    "aleks", "carnegie-learning", "century-tech", "cognii",
    "coursera-coach", "duolingo-max", "gradescope", "khan-academy-ai",
    "knewton-alta", "querium", "quizlet-ai", "socratic-by-google",
    "squirrel-ai", "thinkster-math"
]

base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
js_dir = os.path.join(base_dir, "js")

# Templates de traduction professionnelle pour chaque langue
# Basé sur les patterns des fichiers Customer Service
translation_patterns = {
    "de": {
        "is a leading AI-powered": "ist eine führende KI-gestützte",
        "platform designed to": "Plattform, die entwickelt wurde, um",
        "streamline workflows and enhance productivity": "Arbeitsabläufe zu optimieren und die Produktivität zu steigern",
        "Built with cutting-edge": "Gebaut mit modernster",
        "artificial intelligence technology": "künstlicher Intelligenz-Technologie",
        "delivers exceptional performance": "liefert außergewöhnliche Leistung",
        "for modern businesses": "für moderne Unternehmen",
        "The platform leverages": "Die Plattform nutzt",
        "advanced machine learning algorithms": "fortschrittliche Machine-Learning-Algorithmen",
        "to automate complex tasks": "zur Automatisierung komplexer Aufgaben",
        "provide intelligent insights": "intelligente Einblicke bereitstellen",
        "enable teams to work more efficiently": "Teams befähigen, effizienter zu arbeiten",
        "With seamless integrations": "Mit nahtlosen Integrationen",
        "intuitive interface": "intuitive Benutzeroberfläche",
        "trusted solution": "vertrauenswürdige Lösung",
        "organizations worldwide": "Organisationen weltweit",
        "small startup": "kleines Startup",
        "large enterprise": "großes Unternehmen",
        "scales to meet your needs": "skaliert, um Ihre Anforderungen zu erfüllen",
        "maintaining high performance": "hohe Leistung aufrechterhält",
        "reliability": "Zuverlässigkeit",
        "Overview": "Überblick",
        "Key Features": "Hauptmerkmale",
        "Advantages": "Vorteile",
        "Disadvantages": "Nachteile",
        "Comparison": "Vergleich",
        "Final Verdict": "Endgültiges Urteil",
        "Frequently Asked Questions": "Häufig gestellte Fragen",
        "Best Use Cases": "Best Use Cases",
        "Key Advantages": "Hauptvorteile",
        "Excellent Choice": "Ausgezeichnete Wahl",
        "vs Competitors": "vs Wettbewerber",
        "Excels For:": "Exzelliert für:",
        "May Not Be Ideal For:": "Möglicherweise nicht ideal für:",
        "For most organizations, yes": "Für die meisten Organisationen ja",
        "AI-powered automation": "KI-gestützte Automatisierung",
        "productivity gains": "Produktivitätsgewinne",
        "typically provide strong ROI": "bieten typischerweise einen starken ROI",
        "within the first few months": "innerhalb der ersten Monate",
        "scalability and extensive features": "Skalierbarkeit und umfangreiche Funktionen",
        "justify the cost": "rechtfertigen die Kosten",
        "for growing teams": "für wachsende Teams",
        "Most teams can get started": "Die meisten Teams können beginnen",
        "within a day": "innerhalb eines Tages",
        "Basic setup takes minutes": "Die grundlegende Einrichtung dauert Minuten",
        "full enterprise deployment": "vollständige Enterprise-Bereitstellung",
        "with custom integrations": "mit kundenspezifischen Integrationen",
        "typically takes": "dauert typischerweise",
        "with proper planning": "mit ordentlicher Planung",
        "integrates with": "integriert sich mit",
        "popular platforms including": "beliebten Plattformen einschließlich",
        "and many more": "und viele mehr",
        "robust API": "robuste API",
        "enables custom integrations": "ermöglicht kundenspezifische Integrationen",
        "offers flexible pricing plans": "bietet flexible Preispläne",
        "to suit different organization sizes": "um verschiedene Organisationsgrößen anzupassen",
        "and needs": "und Bedürfnisse",
        "Advanced features": "Erweiterte Funktionen",
        "increased limits": "erhöhte Limits",
        "priority support": "Prioritätssupport",
        "API access": "API-Zugriff",
        "Annual plans receive": "Jährliche Pläne erhalten",
        "discount": "Rabatt",
        "Volume pricing available": "Mengenpreise verfügbar",
        "for teams over": "für Teams über",
        "users": "Benutzer",
        "Bank-grade encryption": "Verschlüsselung nach Bankstandard",
        "SSO": "SSO",
        "compliance with": "Compliance mit",
        "standards": "Standards",
        "Comprehensive analytics dashboard": "Umfassendes Analytics-Dashboard",
        "with actionable insights": "mit umsetzbaren Einblicken",
        "predictive analytics": "prädiktive Analytik",
        "Connect with": "Verbinden Sie sich mit",
        "popular tools and platforms": "beliebte Tools und Plattformen",
        "through native integrations": "durch native Integrationen",
        "Intelligent automation": "Intelligente Automatisierung",
        "that learns from your workflows": "die aus Ihren Arbeitsabläufen lernt",
        "optimizes processes": "optimiert Prozesse",
        "in real-time": "in Echtzeit",
        "Access all features": "Greifen Sie auf alle Funktionen zu",
        "on any device": "auf jedem Gerät",
        "responsive design": "responsives Design",
        "native mobile apps": "native mobile Apps",
        "Advanced automation engine": "Erweiterte Automatisierungsmaschine",
        "Custom workflow builder": "Benutzerdefinierter Workflow-Builder",
        "Enterprise-grade scalability": "Skalierbarkeit auf Enterprise-Niveau",
        "Excellent customer support": "Ausgezeichneter Kundensupport",
        "Comprehensive documentation": "Umfassende Dokumentation",
        "Active community": "Aktive Community",
        "Competitive pricing": "Wettbewerbsfähige Preise",
        "Intuitive user interface": "Intuitive Benutzeroberfläche",
        "Better integration ecosystem": "Besseres Integrations-Ökosystem",
        "Faster performance": "Schnellere Leistung",
        "More intuitive interface": "Intuitivere Benutzeroberfläche",
        "More competitive pricing": "Wettbewerbsfähigere Preise",
        "Learning curve for advanced features": "Lernkurve für erweiterte Funktionen",
        "Limited offline functionality": "Eingeschränkte Offline-Funktionalität",
        "Mobile app has fewer features": "Mobile App hat weniger Funktionen",
        "Enterprise Teams:": "Enterprise-Teams:",
        "Large organizations requiring": "Große Organisationen, die",
        "scalable": "skalierbare",
        "solutions with advanced features": "Lösungen mit erweiterten Funktionen benötigen",
        "Growing Startups:": "Wachsende Startups:",
        "Fast-moving companies that need": "Schnell wachsende Unternehmen, die",
        "flexible": "flexible",
        "automation": "Automatisierung benötigen",
        "Data-Driven Organizations:": "Datengetriebene Organisationen:",
        "Companies leveraging analytics": "Unternehmen, die Analytik nutzen",
        "for strategic decision-making": "für strategische Entscheidungsfindung",
        "Compliance-Heavy Industries:": "Compliance-lastige Branchen:",
        "Regulated sectors requiring": "Regulierte Sektoren, die",
        "enterprise-grade security": "Sicherheit auf Enterprise-Niveau",
        "compliance": "Compliance benötigen",
        "Organizations requiring": "Organisationen, die",
        "extensive offline functionality": "umfangreiche Offline-Funktionalität benötigen",
        "Explore": "Erkunden Sie",
        "interface:": "Benutzeroberfläche:"
    },
    "es": {
        "is a leading AI-powered": "es una plataforma líder impulsada por IA",
        "platform designed to": "diseñada para",
        "streamline workflows and enhance productivity": "optimizar flujos de trabajo y mejorar la productividad",
        "Built with cutting-edge": "Construida con",
        "artificial intelligence technology": "tecnología de inteligencia artificial de vanguardia",
        "delivers exceptional performance": "ofrece un rendimiento excepcional",
        "for modern businesses": "para empresas modernas",
        "The platform leverages": "La plataforma aprovecha",
        "advanced machine learning algorithms": "algoritmos avanzados de aprendizaje automático",
        "to automate complex tasks": "para automatizar tareas complejas",
        "provide intelligent insights": "proporcionar información inteligente",
        "enable teams to work more efficiently": "permitir que los equipos trabajen de manera más eficiente",
        "With seamless integrations": "Con integraciones perfectas",
        "intuitive interface": "interfaz intuitiva",
        "trusted solution": "solución confiable",
        "organizations worldwide": "organizaciones en todo el mundo",
        "small startup": "pequeña startup",
        "large enterprise": "gran empresa",
        "scales to meet your needs": "se escala para satisfacer sus necesidades",
        "maintaining high performance": "manteniendo un alto rendimiento",
        "reliability": "confiabilidad",
        "Overview": "Descripción general",
        "Key Features": "Características clave",
        "Advantages": "Ventajas",
        "Disadvantages": "Desventajas",
        "Comparison": "Comparación",
        "Final Verdict": "Veredicto final",
        "Frequently Asked Questions": "Preguntas frecuentes",
        "Best Use Cases": "Mejores casos de uso",
        "Key Advantages": "Ventajas clave",
        "Excellent Choice": "Excelente elección",
        "vs Competitors": "vs Competidores",
        "Excels For:": "Sobresale para:",
        "May Not Be Ideal For:": "Puede no ser ideal para:",
        "For most organizations, yes": "Para la mayoría de las organizaciones, sí",
        "AI-powered automation": "automatización impulsada por IA",
        "productivity gains": "ganancias de productividad",
        "typically provide strong ROI": "generalmente proporcionan un fuerte ROI",
        "within the first few months": "dentro de los primeros meses",
        "scalability and extensive features": "escalabilidad y características extensas",
        "justify the cost": "justifican el costo",
        "for growing teams": "para equipos en crecimiento",
        "Most teams can get started": "La mayoría de los equipos pueden comenzar",
        "within a day": "en un día",
        "Basic setup takes minutes": "La configuración básica toma minutos",
        "full enterprise deployment": "implementación empresarial completa",
        "with custom integrations": "con integraciones personalizadas",
        "typically takes": "generalmente toma",
        "with proper planning": "con una planificación adecuada",
        "integrates with": "se integra con",
        "popular platforms including": "plataformas populares incluyendo",
        "and many more": "y muchas más",
        "robust API": "API robusta",
        "enables custom integrations": "permite integraciones personalizadas",
        "offers flexible pricing plans": "ofrece planes de precios flexibles",
        "to suit different organization sizes": "para adaptarse a diferentes tamaños de organización",
        "and needs": "y necesidades",
        "Advanced features": "Características avanzadas",
        "increased limits": "límites aumentados",
        "priority support": "soporte prioritario",
        "API access": "acceso a API",
        "Annual plans receive": "Los planes anuales reciben",
        "discount": "descuento",
        "Volume pricing available": "Precios por volumen disponibles",
        "for teams over": "para equipos de más de",
        "users": "usuarios",
        "Bank-grade encryption": "Cifrado de grado bancario",
        "SSO": "SSO",
        "compliance with": "cumplimiento con",
        "standards": "estándares",
        "Comprehensive analytics dashboard": "Panel de análisis integral",
        "with actionable insights": "con información procesable",
        "predictive analytics": "análisis predictivo",
        "Connect with": "Conéctese con",
        "popular tools and platforms": "herramientas y plataformas populares",
        "through native integrations": "a través de integraciones nativas",
        "Intelligent automation": "Automatización inteligente",
        "that learns from your workflows": "que aprende de sus flujos de trabajo",
        "optimizes processes": "optimiza procesos",
        "in real-time": "en tiempo real",
        "Access all features": "Acceda a todas las funciones",
        "on any device": "en cualquier dispositivo",
        "responsive design": "diseño receptivo",
        "native mobile apps": "aplicaciones móviles nativas"
    }
}

# Continuer avec les autres langues...
# [TRUNCATED pour la lisibilité - le script complet contiendrait toutes les langues]

def extract_en_translations(js_file):
    """Extrait les traductions EN du fichier i18n.js"""
    with open(js_file, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'"en":\s*({[^}]+(?:{[^}]*}[^}]*)*})'
    match = re.search(pattern, content, re.DOTALL)

    if match:
        en_dict = {}
        key_pattern = r'"([^"]+)":\s*"([^"]*(?:\\.[^"]*)*)"'
        matches = re.findall(key_pattern, match.group(1))
        for key, value in matches:
            en_dict[key] = value.replace('\\"', '"').replace('\\n', '\n')
        return en_dict
    return {}

def translate_text(text, lang, tool_name):
    """Traduit un texte en utilisant les patterns"""
    if lang not in translation_patterns:
        return text

    translated = text
    patterns = translation_patterns[lang]

    # Remplacer le nom de l'outil
    tool_display = ' '.join(p.capitalize() for p in tool_name.split('-'))
    translated = translated.replace(tool_display, tool_display)  # Garder le nom

    # Appliquer les patterns de traduction
    for en_phrase, target_phrase in patterns.items():
        translated = translated.replace(en_phrase, target_phrase)

    return translated

def tool_to_camel(tool):
    """Convertit khan-academy-ai en khanAcademyAi"""
    parts = tool.split('-')
    return parts[0] + ''.join(p.capitalize() for p in parts[1:])

def tool_to_title(tool):
    """Convertit khan-academy-ai en Khan Academy Ai"""
    return ' '.join(p.capitalize() for p in tool.split('-'))

def update_i18n_file(tool):
    """Met à jour le fichier i18n avec toutes les traductions"""
    js_file = os.path.join(js_dir, f"{tool}-i18n.js")

    if not os.path.exists(js_file):
        print(f"[SKIP] {tool}-i18n.js not found")
        return

    en_translations = extract_en_translations(js_file)

    if not en_translations:
        print(f"[ERROR] No English translations in {tool}-i18n.js")
        return

    # Créer les traductions pour toutes les langues
    all_translations = {"en": en_translations}
    languages = ["de", "es"]  # Commencer avec 2 langues pour tester

    for lang in languages:
        all_translations[lang] = {}
        for key, en_text in en_translations.items():
            all_translations[lang][key] = translate_text(en_text, lang, tool)

    # Générer le nouveau fichier
    camel_name = tool_to_camel(tool)
    title_name = tool_to_title(tool)

    js_content = f"// {title_name.upper()} I18N\n"
    js_content += f"const {camel_name}Translations = {{\n"

    for idx, lang in enumerate(["en"] + languages):
        js_content += f'  "{lang}": {json.dumps(all_translations[lang], indent=4, ensure_ascii=False)}'
        if idx < len(languages):
            js_content += ","
        js_content += "\n"

    js_content += "};\n\n"

    js_content += f"""function get{title_name.replace(' ', '')}Translation(key, lang) {{
  if ({camel_name}Translations[lang] && {camel_name}Translations[lang][key]) {{
    return {camel_name}Translations[lang][key];
  }}
  if ({camel_name}Translations.en && {camel_name}Translations.en[key]) {{
    return {camel_name}Translations.en[key];
  }}
  return null;
}}

function apply{title_name.replace(' ', '')}Translations(lang) {{
  console.log(`Applying {tool} translations for: ${{lang}}`);
  let count = 0;
  document.querySelectorAll('[data-i18n]').forEach(element => {{
    const key = element.getAttribute('data-i18n');
    if (key && (key.startsWith('review.{tool}.') || key.startsWith('review.common.'))) {{
      const translation = get{title_name.replace(' ', '')}Translation(key, lang);
      if (translation) {{
        element.textContent = translation;
        count++;
      }}
    }}
  }});
  console.log(`Applied ${{count}} {tool} translations`);
}}

window.addEventListener('languageChanged', (e) => {{
  const lang = e.detail.language;
  setTimeout(() => apply{title_name.replace(' ', '')}Translations(lang), 200);
}});

if (document.readyState === 'loading') {{
  document.addEventListener('DOMContentLoaded', () => {{
    const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
    apply{title_name.replace(' ', '')}Translations(currentLang);
  }});
}} else {{
  const currentLang = window.i18n ? window.i18n.getCurrentLanguage() : 'en';
  apply{title_name.replace(' ', '')}Translations(currentLang);
}}

console.log('{tool} i18n loaded');
"""

    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(js_content)

    print(f"[OK] {tool}-i18n.js updated ({len(en_translations)} keys, {len(all_translations)} languages)")

# Traiter tous les outils
print("=" * 60)
print("Updating Education i18n files with translations...")
print("=" * 60)

for tool in tools:
    update_i18n_file(tool)

print("=" * 60)
print("[DONE] All Education i18n files updated!")
print("=" * 60)
