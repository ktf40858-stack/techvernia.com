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

# Mapping of English values to translations
value_translations = {
    "de": {
        "Advanced automation engine": "Fortschrittliche Automatisierungs-Engine",
        "Real-time collaboration features": "Echtzeit-Kollaborationsfunktionen",
        "Robust API and integrations": "Robuste API und Integrationen",
        "Powerful AI capabilities": "Leistungsstarke KI-Funktionen",
        "Intuitive user interface": "Intuitive Benutzeroberfläche",
        "Excellent customer support": "Exzellenter Kundensupport",
        "Regular feature updates": "Regelmäßige Feature-Updates",
        "Strong data security": "Starke Datensicherheit",
        "Scalable architecture": "Skalierbare Architektur",
        "Comprehensive documentation": "Umfassende Dokumentation",
        "Active community": "Aktive Community",
        "Competitive pricing": "Wettbewerbsfähige Preise",
        "Enterprise-grade scalability": "Skalierbarkeit auf Enterprise-Niveau",
        "Learning curve for advanced features": "Lernkurve für erweiterte Funktionen",
        "Premium pricing for enterprise tier": "Premium-Preise für Enterprise-Tier",
        "Limited offline functionality": "Eingeschränkte Offline-Funktionalität",
        "Mobile app has fewer features": "Mobile App hat weniger Funktionen",
        "Some features require add-ons": "Einige Funktionen erfordern Add-ons",
        "Perfect for individuals and small teams getting started. Basic features with limited usage.": "Perfekt für Einzelpersonen und kleine Teams für den Einstieg. Grundfunktionen mit begrenzter Nutzung.",
        "Advanced features, increased limits, priority support, and API access.": "Erweiterte Funktionen, erhöhte Limits, priorisierter Support und API-Zugang.",
        "Unlimited usage, dedicated support, SLA guarantees, and custom integrations.": "Unbegrenzte Nutzung, dedizierter Support, SLA-Garantien und benutzerdefinierte Integrationen.",
        "Annual plans receive a 20% discount. Volume pricing available for teams over 100 users.": "Jahrespläne erhalten 20% Rabatt. Mengenpreise verfügbar für Teams über 100 Benutzer.",
        "Excellent Choice": "Ausgezeichnete Wahl",
        "Key Advantages": "Hauptvorteile",
        "Superior AI capabilities": "Überlegene KI-Funktionen",
        "More intuitive interface": "Intuitivere Benutzeroberfläche",
        "Better integration ecosystem": "Besseres Integrations-Ökosystem",
        "More competitive pricing": "Wettbewerbsfähigere Preise",
        "Faster performance": "Schnellere Leistung",
        "Stronger security features": "Stärkere Sicherheitsfunktionen",
        "Unique Differentiators": "Einzigartige Differenzierungsmerkmale",
        "Custom workflow builder": "Benutzerdefinierter Workflow-Builder",
        "Predictive analytics": "Prädiktive Analytik",
    },
    "es": {
        "Advanced automation engine": "Motor de automatización avanzado",
        "Real-time collaboration features": "Funciones de colaboración en tiempo real",
        "Robust API and integrations": "API e integraciones robustas",
        "Powerful AI capabilities": "Capacidades de IA potentes",
        "Intuitive user interface": "Interfaz de usuario intuitiva",
        "Excellent customer support": "Excelente soporte al cliente",
        "Regular feature updates": "Actualizaciones regulares de funciones",
        "Strong data security": "Seguridad de datos robusta",
        "Scalable architecture": "Arquitectura escalable",
        "Comprehensive documentation": "Documentación completa",
        "Active community": "Comunidad activa",
        "Competitive pricing": "Precios competitivos",
        "Enterprise-grade scalability": "Escalabilidad de nivel empresarial",
        "Learning curve for advanced features": "Curva de aprendizaje para funciones avanzadas",
        "Premium pricing for enterprise tier": "Precios premium para el nivel empresarial",
        "Limited offline functionality": "Funcionalidad offline limitada",
        "Mobile app has fewer features": "La app móvil tiene menos funciones",
        "Some features require add-ons": "Algunas funciones requieren complementos",
    },
    "fr": {
        "Advanced automation engine": "Moteur d'automatisation avancé",
        "Real-time collaboration features": "Fonctionnalités de collaboration en temps réel",
        "Robust API and integrations": "API et intégrations robustes",
        "Powerful AI capabilities": "Capacités IA puissantes",
        "Intuitive user interface": "Interface utilisateur intuitive",
        "Excellent customer support": "Excellent support client",
        "Regular feature updates": "Mises à jour régulières des fonctionnalités",
        "Strong data security": "Sécurité des données robuste",
        "Scalable architecture": "Architecture évolutive",
        "Comprehensive documentation": "Documentation complète",
        "Active community": "Communauté active",
        "Competitive pricing": "Tarification compétitive",
        "Enterprise-grade scalability": "Évolutivité de niveau entreprise",
    },
    "pt": {
        "Advanced automation engine": "Motor de automação avançado",
        "Real-time collaboration features": "Recursos de colaboração em tempo real",
        "Robust API and integrations": "API e integrações robustas",
        "Powerful AI capabilities": "Recursos de IA poderosos",
        "Intuitive user interface": "Interface de usuário intuitiva",
        "Excellent customer support": "Excelente suporte ao cliente",
        "Regular feature updates": "Atualizações regulares de recursos",
        "Strong data security": "Segurança de dados robusta",
        "Scalable architecture": "Arquitetura escalável",
        "Comprehensive documentation": "Documentação abrangente",
        "Active community": "Comunidade ativa",
        "Competitive pricing": "Preços competitivos",
        "Enterprise-grade scalability": "Escalabilidade de nível empresarial",
    },
    "zh": {
        "Advanced automation engine": "高级自动化引擎",
        "Real-time collaboration features": "实时协作功能",
        "Robust API and integrations": "强大的API和集成",
        "Powerful AI capabilities": "强大的AI功能",
        "Intuitive user interface": "直观的用户界面",
        "Excellent customer support": "出色的客户支持",
        "Regular feature updates": "定期功能更新",
        "Strong data security": "强大的数据安全性",
        "Scalable architecture": "可扩展架构",
        "Comprehensive documentation": "全面的文档",
        "Active community": "活跃的社区",
        "Competitive pricing": "有竞争力的价格",
        "Enterprise-grade scalability": "企业级可扩展性",
    },
    "ja": {
        "Advanced automation engine": "高度な自動化エンジン",
        "Real-time collaboration features": "リアルタイムコラボレーション機能",
        "Robust API and integrations": "堅牢なAPIと統合",
        "Powerful AI capabilities": "強力なAI機能",
        "Intuitive user interface": "直感的なユーザーインターフェース",
        "Excellent customer support": "優れたカスタマーサポート",
        "Regular feature updates": "定期的な機能更新",
        "Strong data security": "強力なデータセキュリティ",
        "Scalable architecture": "スケーラブルなアーキテクチャ",
        "Comprehensive documentation": "包括的なドキュメント",
        "Active community": "アクティブなコミュニティ",
        "Competitive pricing": "競争力のある価格",
        "Enterprise-grade scalability": "エンタープライズグレードのスケーラビリティ",
    },
    "ko": {
        "Advanced automation engine": "고급 자동화 엔진",
        "Real-time collaboration features": "실시간 협업 기능",
        "Robust API and integrations": "강력한 API 및 통합",
        "Powerful AI capabilities": "강력한 AI 기능",
        "Intuitive user interface": "직관적인 사용자 인터페이스",
        "Excellent customer support": "우수한 고객 지원",
        "Regular feature updates": "정기적인 기능 업데이트",
        "Strong data security": "강력한 데이터 보안",
        "Scalable architecture": "확장 가능한 아키텍처",
        "Comprehensive documentation": "포괄적인 문서",
        "Active community": "활발한 커뮤니티",
        "Competitive pricing": "경쟁력 있는 가격",
        "Enterprise-grade scalability": "엔터프라이즈급 확장성",
    },
    "ar": {
        "Advanced automation engine": "محرك أتمتة متقدم",
        "Real-time collaboration features": "ميزات التعاون في الوقت الفعلي",
        "Robust API and integrations": "واجهة برمجة تطبيقات قوية وتكاملات",
        "Powerful AI capabilities": "قدرات ذكاء اصطناعي قوية",
        "Intuitive user interface": "واجهة مستخدم بديهية",
        "Excellent customer support": "دعم عملاء ممتاز",
        "Regular feature updates": "تحديثات منتظمة للميزات",
        "Strong data security": "أمان بيانات قوي",
        "Scalable architecture": "بنية قابلة للتوسع",
        "Comprehensive documentation": "وثائق شاملة",
        "Active community": "مجتمع نشط",
        "Competitive pricing": "أسعار تنافسية",
        "Enterprise-grade scalability": "قابلية توسع على مستوى المؤسسات",
    },
    "hi": {
        "Advanced automation engine": "उन्नत स्वचालन इंजन",
        "Real-time collaboration features": "रियल-टाइम सहयोग सुविधाएं",
        "Robust API and integrations": "मजबूत API और एकीकरण",
        "Powerful AI capabilities": "शक्तिशाली AI क्षमताएं",
        "Intuitive user interface": "सहज उपयोगकर्ता इंटरफ़ेस",
        "Excellent customer support": "उत्कृष्ट ग्राहक सहायता",
        "Regular feature updates": "नियमित सुविधा अपडेट",
        "Strong data security": "मजबूत डेटा सुरक्षा",
        "Scalable architecture": "स्केलेबल आर्किटेक्चर",
        "Comprehensive documentation": "व्यापक दस्तावेज़ीकरण",
        "Active community": "सक्रिय समुदाय",
        "Competitive pricing": "प्रतिस्पर्धी मूल्य निर्धारण",
        "Enterprise-grade scalability": "एंटरप्राइज़-ग्रेड स्केलेबिलिटी",
    }
}

def translate_by_value_replacement(tool_key, tool_name):
    """Replace English values with translations using simple string replacement"""

    js_file = os.path.join(js_dir, f"{tool_key}-i18n.js")

    if not os.path.exists(js_file):
        return False

    with open(js_file, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    replacements_made = 0

    for lang, translations in value_translations.items():
        for english_text, translated_text in translations.items():
            # Simple string replacement within quotes
            old_str = f'": "{english_text}"'
            new_str = f'": "{translated_text}"'

            before_count = content.count(old_str)
            content = content.replace(old_str, new_str)
            after_count = content.count(old_str)

            replaced = before_count - after_count
            if replaced > 0:
                replacements_made += replaced

    if content != original_content:
        with open(js_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  [+] Made {replacements_made} replacements")
        return True

    return False

print("=" * 70)
print("TRANSLATING BY VALUE REPLACEMENT")
print("=" * 70)

fixed_count = 0

for tool_key, tool_name in translation_tools.items():
    print(f"\n{tool_name}:")
    if translate_by_value_replacement(tool_key, tool_name):
        fixed_count += 1
    else:
        print(f"  [OK] No replacements needed")

print("\n" + "=" * 70)
print(f"COMPLETE: {fixed_count}/10 tools updated")
print("=" * 70)
