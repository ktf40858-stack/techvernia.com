#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour corriger complètement les traductions i18n de la catégorie HR
Extrait les traductions des catégories fonctionnelles et les applique correctement
"""

import re
import json
from pathlib import Path

# Fix Windows encoding
import sys
import io
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Mapping de traductions communes pour chaque langue
COMMON_TRANSLATIONS = {
    "zh": {
        "Overview": "概述",
        "Key Features": "主要功能",
        "Pros & Cons": "优缺点",
        "Advantages": "优势",
        "Disadvantages": "劣势",
        "Pricing": "定价",
        "Best Use Cases": "最佳使用场景",
        "Comparison": "对比",
        "Key Advantages": "主要优势",
        "Unique Differentiators": "独特优势",
        "Frequently Asked Questions": "常见问题",
        "Final Verdict": "最终评价",
        "Excellent Choice": "优秀选择",
        "Ready to Get Started?": "准备开始了吗？",
        "View Pricing": "查看定价",

        # Features
        "AI-Powered Automation": "AI智能自动化",
        "Advanced Analytics": "高级分析",
        "Seamless Integrations": "无缝集成",
        "Enterprise Security": "企业级安全",
        "Real-Time Collaboration": "实时协作",
        "Mobile-First Design": "移动优先设计",

        # Common advantages
        "Powerful AI capabilities": "强大的AI功能",
        "Intuitive user interface": "直观的用户界面",
        "Excellent customer support": "出色的客户支持",
        "Regular feature updates": "定期功能更新",
        "Robust API and integrations": "强大的API和集成",
        "Scalable architecture": "可扩展架构",
        "Competitive pricing": "有竞争力的定价",
        "Comprehensive documentation": "全面的文档",
        "Active community": "活跃的社区",
        "Strong data security": "强大的数据安全",

        # Common disadvantages
        "Learning curve for advanced features": "高级功能学习曲线",
        "Premium pricing for enterprise tier": "企业版定价较高",
        "Limited offline functionality": "离线功能有限",
        "Some features require add-ons": "某些功能需要附加组件",
        "Mobile app has fewer features": "移动应用功能较少",

        # Pricing
        "Free Plan": "免费计划",
        "Professional": "专业版",
        "Enterprise": "企业版",
        "Custom": "定制",

        # FAQ common
        "Is my data secure?": "我的数据安全吗？",
        "How long does implementation take?": "实施需要多长时间？",
        "What integrations are available?": "有哪些集成可用？",
        "Can I migrate from another platform?": "我可以从其他平台迁移吗？",
        "What kind of support is available?": "提供什么样的支持？",
        "How does AI enhance the platform?": "AI如何增强平台？",
    },

    "ja": {
        "Overview": "概要",
        "Key Features": "主な機能",
        "Pros & Cons": "メリット・デメリット",
        "Advantages": "メリット",
        "Disadvantages": "デメリット",
        "Pricing": "料金",
        "Best Use Cases": "最適な使用例",
        "Comparison": "比較",
        "Key Advantages": "主な利点",
        "Unique Differentiators": "独自の差別化要因",
        "Frequently Asked Questions": "よくある質問",
        "Final Verdict": "最終評価",
        "Excellent Choice": "優れた選択",
        "Ready to Get Started?": "始める準備はできましたか？",
        "View Pricing": "料金を見る",

        # Features
        "AI-Powered Automation": "AI駆動の自動化",
        "Advanced Analytics": "高度な分析",
        "Seamless Integrations": "シームレスな統合",
        "Enterprise Security": "エンタープライズセキュリティ",
        "Real-Time Collaboration": "リアルタイムコラボレーション",
        "Mobile-First Design": "モバイルファースト設計",

        # Common advantages
        "Powerful AI capabilities": "強力なAI機能",
        "Intuitive user interface": "直感的なユーザーインターフェース",
        "Excellent customer support": "優れたカスタマーサポート",
        "Regular feature updates": "定期的な機能更新",
        "Robust API and integrations": "堅牢なAPIと統合",
        "Scalable architecture": "スケーラブルなアーキテクチャ",
        "Competitive pricing": "競争力のある価格",
        "Comprehensive documentation": "包括的なドキュメント",
        "Active community": "活発なコミュニティ",
        "Strong data security": "強力なデータセキュリティ",

        # Common disadvantages
        "Learning curve for advanced features": "高度な機能の学習曲線",
        "Premium pricing for enterprise tier": "エンタープライズ層の高価格",
        "Limited offline functionality": "限定的なオフライン機能",
        "Some features require add-ons": "一部の機能にはアドオンが必要",
        "Mobile app has fewer features": "モバイルアプリの機能が少ない",

        # Pricing
        "Free Plan": "無料プラン",
        "Professional": "プロフェッショナル",
        "Enterprise": "エンタープライズ",
        "Custom": "カスタム",

        # FAQ common
        "Is my data secure?": "データは安全ですか？",
        "How long does implementation take?": "実装にはどのくらいかかりますか？",
        "What integrations are available?": "どのような統合が利用できますか？",
        "Can I migrate from another platform?": "他のプラットフォームから移行できますか？",
        "What kind of support is available?": "どのようなサポートが利用できますか？",
        "How does AI enhance the platform?": "AIはどのようにプラットフォームを強化しますか？",
    },

    "ko": {
        "Overview": "개요",
        "Key Features": "주요 기능",
        "Pros & Cons": "장단점",
        "Advantages": "장점",
        "Disadvantages": "단점",
        "Pricing": "가격",
        "Best Use Cases": "최적 사용 사례",
        "Comparison": "비교",
        "Key Advantages": "주요 장점",
        "Unique Differentiators": "독특한 차별화 요소",
        "Frequently Asked Questions": "자주 묻는 질문",
        "Final Verdict": "최종 평가",
        "Excellent Choice": "탁월한 선택",
        "Ready to Get Started?": "시작할 준비가 되셨나요?",
        "View Pricing": "가격 보기",

        # Features
        "AI-Powered Automation": "AI 기반 자동화",
        "Advanced Analytics": "고급 분석",
        "Seamless Integrations": "원활한 통합",
        "Enterprise Security": "엔터프라이즈 보안",
        "Real-Time Collaboration": "실시간 협업",
        "Mobile-First Design": "모바일 우선 디자인",

        # Common advantages
        "Powerful AI capabilities": "강력한 AI 기능",
        "Intuitive user interface": "직관적인 사용자 인터페이스",
        "Excellent customer support": "우수한 고객 지원",
        "Regular feature updates": "정기적인 기능 업데이트",
        "Robust API and integrations": "강력한 API 및 통합",
        "Scalable architecture": "확장 가능한 아키텍처",
        "Competitive pricing": "경쟁력 있는 가격",
        "Comprehensive documentation": "포괄적인 문서",
        "Active community": "활발한 커뮤니티",
        "Strong data security": "강력한 데이터 보안",

        # Common disadvantages
        "Learning curve for advanced features": "고급 기능 학습 곡선",
        "Premium pricing for enterprise tier": "엔터프라이즈 계층의 프리미엄 가격",
        "Limited offline functionality": "제한적인 오프라인 기능",
        "Some features require add-ons": "일부 기능에는 추가 기능 필요",
        "Mobile app has fewer features": "모바일 앱 기능 부족",

        # Pricing
        "Free Plan": "무료 플랜",
        "Professional": "프로페셔널",
        "Enterprise": "엔터프라이즈",
        "Custom": "맞춤형",

        # FAQ common
        "Is my data secure?": "내 데이터가 안전한가요?",
        "How long does implementation take?": "구현하는 데 얼마나 걸리나요?",
        "What integrations are available?": "어떤 통합을 사용할 수 있나요?",
        "Can I migrate from another platform?": "다른 플랫폼에서 마이그레이션할 수 있나요?",
        "What kind of support is available?": "어떤 종류의 지원을 받을 수 있나요?",
        "How does AI enhance the platform?": "AI가 플랫폼을 어떻게 향상시키나요?",
    },

    "ar": {
        "Overview": "نظرة عامة",
        "Key Features": "الميزات الرئيسية",
        "Pros & Cons": "الإيجابيات والسلبيات",
        "Advantages": "المزايا",
        "Disadvantages": "العيوب",
        "Pricing": "التسعير",
        "Best Use Cases": "أفضل حالات الاستخدام",
        "Comparison": "المقارنة",
        "Key Advantages": "المزايا الرئيسية",
        "Unique Differentiators": "المميزات الفريدة",
        "Frequently Asked Questions": "الأسئلة الشائعة",
        "Final Verdict": "الحكم النهائي",
        "Excellent Choice": "اختيار ممتاز",
        "Ready to Get Started?": "هل أنت مستعد للبدء؟",
        "View Pricing": "عرض التسعير",

        # Features
        "AI-Powered Automation": "الأتمتة المدعومة بالذكاء الاصطناعي",
        "Advanced Analytics": "التحليلات المتقدمة",
        "Seamless Integrations": "التكامل السلس",
        "Enterprise Security": "أمان المؤسسات",
        "Real-Time Collaboration": "التعاون في الوقت الفعلي",
        "Mobile-First Design": "تصميم يعطي الأولوية للموبايل",

        # Common advantages
        "Powerful AI capabilities": "قدرات ذكاء اصطناعي قوية",
        "Intuitive user interface": "واجهة مستخدم بديهية",
        "Excellent customer support": "دعم عملاء ممتاز",
        "Regular feature updates": "تحديثات منتظمة للميزات",
        "Robust API and integrations": "واجهة برمجية قوية وتكاملات",
        "Scalable architecture": "هندسة قابلة للتطوير",
        "Competitive pricing": "أسعار تنافسية",
        "Comprehensive documentation": "توثيق شامل",
        "Active community": "مجتمع نشط",
        "Strong data security": "أمان بيانات قوي",

        # Common disadvantages
        "Learning curve for advanced features": "منحنى تعلم للميزات المتقدمة",
        "Premium pricing for enterprise tier": "أسعار مميزة لمستوى المؤسسات",
        "Limited offline functionality": "وظائف محدودة دون اتصال",
        "Some features require add-ons": "بعض الميزات تتطلب إضافات",
        "Mobile app has fewer features": "تطبيق الموبايل به ميزات أقل",

        # Pricing
        "Free Plan": "خطة مجانية",
        "Professional": "احترافي",
        "Enterprise": "مؤسسات",
        "Custom": "مخصص",

        # FAQ common
        "Is my data secure?": "هل بياناتي آمنة؟",
        "How long does implementation take?": "كم من الوقت يستغرق التنفيذ؟",
        "What integrations are available?": "ما هي التكاملات المتاحة؟",
        "Can I migrate from another platform?": "هل يمكنني الانتقال من منصة أخرى؟",
        "What kind of support is available?": "ما نوع الدعم المتاح؟",
        "How does AI enhance the platform?": "كيف يعزز الذكاء الاصطناعي المنصة؟",
    },

    "hi": {
        "Overview": "अवलोकन",
        "Key Features": "मुख्य विशेषताएं",
        "Pros & Cons": "फायदे और नुकसान",
        "Advantages": "फायदे",
        "Disadvantages": "नुकसान",
        "Pricing": "मूल्य निर्धारण",
        "Best Use Cases": "सर्वोत्तम उपयोग के मामले",
        "Comparison": "तुलना",
        "Key Advantages": "मुख्य फायदे",
        "Unique Differentiators": "अनूठे अंतर",
        "Frequently Asked Questions": "अक्सर पूछे जाने वाले प्रश्न",
        "Final Verdict": "अंतिम फैसला",
        "Excellent Choice": "उत्कृष्ट विकल्प",
        "Ready to Get Started?": "शुरू करने के लिए तैयार हैं?",
        "View Pricing": "मूल्य देखें",

        # Features
        "AI-Powered Automation": "AI-संचालित स्वचालन",
        "Advanced Analytics": "उन्नत विश्लेषण",
        "Seamless Integrations": "सहज एकीकरण",
        "Enterprise Security": "एंटरप्राइज़ सुरक्षा",
        "Real-Time Collaboration": "रीयल-टाइम सहयोग",
        "Mobile-First Design": "मोबाइल-प्रथम डिज़ाइन",

        # Common advantages
        "Powerful AI capabilities": "शक्तिशाली AI क्षमताएं",
        "Intuitive user interface": "सहज उपयोगकर्ता इंटरफ़ेस",
        "Excellent customer support": "उत्कृष्ट ग्राहक समर्थन",
        "Regular feature updates": "नियमित सुविधा अपडेट",
        "Robust API and integrations": "मजबूत API और एकीकरण",
        "Scalable architecture": "स्केलेबल वास्तुकला",
        "Competitive pricing": "प्रतिस्पर्धी मूल्य निर्धारण",
        "Comprehensive documentation": "व्यापक दस्तावेज़ीकरण",
        "Active community": "सक्रिय समुदाय",
        "Strong data security": "मजबूत डेटा सुरक्षा",

        # Common disadvantages
        "Learning curve for advanced features": "उन्नत सुविधाओं के लिए सीखने की अवस्था",
        "Premium pricing for enterprise tier": "एंटरप्राइज़ स्तर के लिए प्रीमियम मूल्य",
        "Limited offline functionality": "सीमित ऑफ़लाइन कार्यक्षमता",
        "Some features require add-ons": "कुछ सुविधाओं के लिए ऐड-ऑन की आवश्यकता है",
        "Mobile app has fewer features": "मोबाइल ऐप में कम सुविधाएं हैं",

        # Pricing
        "Free Plan": "मुफ्त योजना",
        "Professional": "पेशेवर",
        "Enterprise": "एंटरप्राइज़",
        "Custom": "कस्टम",

        # FAQ common
        "Is my data secure?": "क्या मेरा डेटा सुरक्षित है?",
        "How long does implementation take?": "कार्यान्वयन में कितना समय लगता है?",
        "What integrations are available?": "कौन से एकीकरण उपलब्ध हैं?",
        "Can I migrate from another platform?": "क्या मैं किसी अन्य प्लेटफ़ॉर्म से माइग्रेट कर सकता हूं?",
        "What kind of support is available?": "किस प्रकार का समर्थन उपलब्ध है?",
        "How does AI enhance the platform?": "AI प्लेटफ़ॉर्म को कैसे बेहतर बनाता है?",
    },

    "de": {
        "Overview": "Übersicht",
        "Key Features": "Hauptmerkmale",
        "Pros & Cons": "Vor- und Nachteile",
        "Advantages": "Vorteile",
        "Disadvantages": "Nachteile",
        "Pricing": "Preise",
        "Best Use Cases": "Beste Anwendungsfälle",
        "Comparison": "Vergleich",
        "Key Advantages": "Hauptvorteile",
        "Unique Differentiators": "Alleinstellungsmerkmale",
        "Frequently Asked Questions": "Häufig gestellte Fragen",
        "Final Verdict": "Abschließendes Urteil",
        "Excellent Choice": "Ausgezeichnete Wahl",
        "Ready to Get Started?": "Bereit anzufangen?",
        "View Pricing": "Preise ansehen",

        # Features
        "AI-Powered Automation": "KI-gestützte Automatisierung",
        "Advanced Analytics": "Erweiterte Analysen",
        "Seamless Integrations": "Nahtlose Integrationen",
        "Enterprise Security": "Unternehmenssicherheit",
        "Real-Time Collaboration": "Echtzeit-Zusammenarbeit",
        "Mobile-First Design": "Mobile-First-Design",

        # Common advantages
        "Powerful AI capabilities": "Leistungsstarke KI-Funktionen",
        "Intuitive user interface": "Intuitive Benutzeroberfläche",
        "Excellent customer support": "Exzellenter Kundensupport",
        "Regular feature updates": "Regelmäßige Feature-Updates",
        "Robust API and integrations": "Robuste API und Integrationen",
        "Scalable architecture": "Skalierbare Architektur",
        "Competitive pricing": "Wettbewerbsfähige Preise",
        "Comprehensive documentation": "Umfassende Dokumentation",
        "Active community": "Aktive Community",
        "Strong data security": "Starke Datensicherheit",

        # Common disadvantages
        "Learning curve for advanced features": "Lernkurve für erweiterte Funktionen",
        "Premium pricing for enterprise tier": "Premium-Preise für Enterprise-Tier",
        "Limited offline functionality": "Begrenzte Offline-Funktionalität",
        "Some features require add-ons": "Einige Funktionen erfordern Add-ons",
        "Mobile app has fewer features": "Mobile App hat weniger Funktionen",

        # Pricing
        "Free Plan": "Kostenloser Plan",
        "Professional": "Professional",
        "Enterprise": "Enterprise",
        "Custom": "Individuell",

        # FAQ common
        "Is my data secure?": "Sind meine Daten sicher?",
        "How long does implementation take?": "Wie lange dauert die Implementierung?",
        "What integrations are available?": "Welche Integrationen sind verfügbar?",
        "Can I migrate from another platform?": "Kann ich von einer anderen Plattform migrieren?",
        "What kind of support is available?": "Welche Art von Support ist verfügbar?",
        "How does AI enhance the platform?": "Wie verbessert KI die Plattform?",
    },

    "es": {
        "Overview": "Descripción general",
        "Key Features": "Características principales",
        "Pros & Cons": "Pros y contras",
        "Advantages": "Ventajas",
        "Disadvantages": "Desventajas",
        "Pricing": "Precios",
        "Best Use Cases": "Mejores casos de uso",
        "Comparison": "Comparación",
        "Key Advantages": "Ventajas clave",
        "Unique Differentiators": "Diferenciadores únicos",
        "Frequently Asked Questions": "Preguntas frecuentes",
        "Final Verdict": "Veredicto final",
        "Excellent Choice": "Excelente elección",
        "Ready to Get Started?": "¿Listo para comenzar?",
        "View Pricing": "Ver precios",

        # Features
        "AI-Powered Automation": "Automatización impulsada por IA",
        "Advanced Analytics": "Análisis avanzados",
        "Seamless Integrations": "Integraciones perfectas",
        "Enterprise Security": "Seguridad empresarial",
        "Real-Time Collaboration": "Colaboración en tiempo real",
        "Mobile-First Design": "Diseño móvil primero",

        # Common advantages
        "Powerful AI capabilities": "Potentes capacidades de IA",
        "Intuitive user interface": "Interfaz de usuario intuitiva",
        "Excellent customer support": "Excelente soporte al cliente",
        "Regular feature updates": "Actualizaciones regulares de funciones",
        "Robust API and integrations": "API e integraciones robustas",
        "Scalable architecture": "Arquitectura escalable",
        "Competitive pricing": "Precios competitivos",
        "Comprehensive documentation": "Documentación completa",
        "Active community": "Comunidad activa",
        "Strong data security": "Fuerte seguridad de datos",

        # Common disadvantages
        "Learning curve for advanced features": "Curva de aprendizaje para funciones avanzadas",
        "Premium pricing for enterprise tier": "Precios premium para nivel empresarial",
        "Limited offline functionality": "Funcionalidad offline limitada",
        "Some features require add-ons": "Algunas funciones requieren complementos",
        "Mobile app has fewer features": "La app móvil tiene menos funciones",

        # Pricing
        "Free Plan": "Plan gratuito",
        "Professional": "Profesional",
        "Enterprise": "Empresarial",
        "Custom": "Personalizado",

        # FAQ common
        "Is my data secure?": "¿Están seguros mis datos?",
        "How long does implementation take?": "¿Cuánto tiempo tarda la implementación?",
        "What integrations are available?": "¿Qué integraciones están disponibles?",
        "Can I migrate from another platform?": "¿Puedo migrar desde otra plataforma?",
        "What kind of support is available?": "¿Qué tipo de soporte está disponible?",
        "How does AI enhance the platform?": "¿Cómo mejora la IA la plataforma?",
    },

    "fr": {
        "Overview": "Aperçu",
        "Key Features": "Fonctionnalités clés",
        "Pros & Cons": "Avantages et inconvénients",
        "Advantages": "Avantages",
        "Disadvantages": "Inconvénients",
        "Pricing": "Tarification",
        "Best Use Cases": "Meilleurs cas d'utilisation",
        "Comparison": "Comparaison",
        "Key Advantages": "Avantages clés",
        "Unique Differentiators": "Différenciateurs uniques",
        "Frequently Asked Questions": "Questions fréquentes",
        "Final Verdict": "Verdict final",
        "Excellent Choice": "Excellent choix",
        "Ready to Get Started?": "Prêt à commencer?",
        "View Pricing": "Voir les tarifs",

        # Features
        "AI-Powered Automation": "Automatisation alimentée par l'IA",
        "Advanced Analytics": "Analyses avancées",
        "Seamless Integrations": "Intégrations transparentes",
        "Enterprise Security": "Sécurité d'entreprise",
        "Real-Time Collaboration": "Collaboration en temps réel",
        "Mobile-First Design": "Conception mobile d'abord",

        # Common advantages
        "Powerful AI capabilities": "Puissantes capacités d'IA",
        "Intuitive user interface": "Interface utilisateur intuitive",
        "Excellent customer support": "Excellent support client",
        "Regular feature updates": "Mises à jour régulières des fonctionnalités",
        "Robust API and integrations": "API et intégrations robustes",
        "Scalable architecture": "Architecture évolutive",
        "Competitive pricing": "Tarification compétitive",
        "Comprehensive documentation": "Documentation complète",
        "Active community": "Communauté active",
        "Strong data security": "Sécurité des données robuste",

        # Common disadvantages
        "Learning curve for advanced features": "Courbe d'apprentissage pour les fonctionnalités avancées",
        "Premium pricing for enterprise tier": "Tarification premium pour niveau entreprise",
        "Limited offline functionality": "Fonctionnalité hors ligne limitée",
        "Some features require add-ons": "Certaines fonctionnalités nécessitent des modules complémentaires",
        "Mobile app has fewer features": "L'application mobile a moins de fonctionnalités",

        # Pricing
        "Free Plan": "Plan gratuit",
        "Professional": "Professionnel",
        "Enterprise": "Entreprise",
        "Custom": "Personnalisé",

        # FAQ common
        "Is my data secure?": "Mes données sont-elles sécurisées?",
        "How long does implementation take?": "Combien de temps prend l'implémentation?",
        "What integrations are available?": "Quelles intégrations sont disponibles?",
        "Can I migrate from another platform?": "Puis-je migrer depuis une autre plateforme?",
        "What kind of support is available?": "Quel type de support est disponible?",
        "How does AI enhance the platform?": "Comment l'IA améliore-t-elle la plateforme?",
    },

    "pt": {
        "Overview": "Visão geral",
        "Key Features": "Recursos principais",
        "Pros & Cons": "Prós e contras",
        "Advantages": "Vantagens",
        "Disadvantages": "Desvantagens",
        "Pricing": "Preços",
        "Best Use Cases": "Melhores casos de uso",
        "Comparison": "Comparação",
        "Key Advantages": "Principais vantagens",
        "Unique Differentiators": "Diferenciais únicos",
        "Frequently Asked Questions": "Perguntas frequentes",
        "Final Verdict": "Veredicto final",
        "Excellent Choice": "Excelente escolha",
        "Ready to Get Started?": "Pronto para começar?",
        "View Pricing": "Ver preços",

        # Features
        "AI-Powered Automation": "Automação alimentada por IA",
        "Advanced Analytics": "Análises avançadas",
        "Seamless Integrations": "Integrações perfeitas",
        "Enterprise Security": "Segurança empresarial",
        "Real-Time Collaboration": "Colaboração em tempo real",
        "Mobile-First Design": "Design mobile first",

        # Common advantages
        "Powerful AI capabilities": "Capacidades poderosas de IA",
        "Intuitive user interface": "Interface de usuário intuitiva",
        "Excellent customer support": "Excelente suporte ao cliente",
        "Regular feature updates": "Atualizações regulares de recursos",
        "Robust API and integrations": "API e integrações robustas",
        "Scalable architecture": "Arquitetura escalável",
        "Competitive pricing": "Preços competitivos",
        "Comprehensive documentation": "Documentação abrangente",
        "Active community": "Comunidade ativa",
        "Strong data security": "Forte segurança de dados",

        # Common disadvantages
        "Learning curve for advanced features": "Curva de aprendizado para recursos avançados",
        "Premium pricing for enterprise tier": "Preços premium para nível empresarial",
        "Limited offline functionality": "Funcionalidade offline limitada",
        "Some features require add-ons": "Alguns recursos requerem complementos",
        "Mobile app has fewer features": "App móvel tem menos recursos",

        # Pricing
        "Free Plan": "Plano gratuito",
        "Professional": "Profissional",
        "Enterprise": "Empresarial",
        "Custom": "Personalizado",

        # FAQ common
        "Is my data secure?": "Meus dados estão seguros?",
        "How long does implementation take?": "Quanto tempo leva a implementação?",
        "What integrations are available?": "Quais integrações estão disponíveis?",
        "Can I migrate from another platform?": "Posso migrar de outra plataforma?",
        "What kind of support is available?": "Que tipo de suporte está disponível?",
        "How does AI enhance the platform?": "Como a IA melhora a plataforma?",
    }
}


def fix_i18n_file(file_path, tool_name):
    """Corrige un fichier i18n HR en appliquant les traductions correctes"""

    print(f"\n🔧 Correction de {tool_name}...")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pour chaque langue, on remplace les traductions
    for lang_code, translations in COMMON_TRANSLATIONS.items():
        # Trouver le début et la fin de la section de langue
        lang_pattern = f'"{lang_code}":\\s*{{([^}}]+(?:}}[^}}]+)*)}}'
        lang_match = re.search(lang_pattern, content, re.DOTALL)

        if not lang_match:
            print(f"  ⚠️  Section {lang_code} non trouvée")
            continue

        lang_section = lang_match.group(0)
        new_lang_section = lang_section

        # Remplacer chaque traduction dans cette section spécifique
        replacements = 0
        for english, translated in translations.items():
            # Échapper les caractères spéciaux pour regex
            escaped_english = re.escape(english)

            # Pattern simplifié qui cherche n'importe quelle clé avec la valeur en anglais
            # Ne pas échapper tool_name car il contient déjà des tirets
            pattern = f'("review\\.[^"]+"):\\s*"{escaped_english}"'
            replacement = f'\\1: "{translated}"'

            # Compter et remplacer
            new_section, count = re.subn(pattern, replacement, new_lang_section)
            if count > 0:
                new_lang_section = new_section
                replacements += count

        # Remplacer la section complète dans le contenu
        content = content.replace(lang_section, new_lang_section)

        print(f"  ✅ {lang_code}: {replacements} traductions corrigées")

    # Sauvegarder le fichier corrigé
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  💾 Fichier sauvegardé")
    return True


def main():
    hr_tools = [
        'beamery', 'eightfold-ai', 'fetcher', 'findem', 'harver', 'hirevue',
        'humanly', 'paradox-olivia', 'phenom', 'pymetrics', 'seekout',
        'sense', 'textio', 'workable-ai'
    ]

    base_path = Path('GenuisNet.ai/js')

    print("="*80)
    print("CORRECTION COMPLÈTE DES TRADUCTIONS i18n - CATÉGORIE HR")
    print("="*80)
    print(f"\n📦 {len(hr_tools)} outils à corriger")
    print(f"🌍 {len(COMMON_TRANSLATIONS)} langues à traiter")
    print(f"🔑 ~{len(COMMON_TRANSLATIONS['zh'])} traductions par langue")
    print()

    success = 0
    failed = 0

    for tool in hr_tools:
        i18n_file = base_path / f'{tool}-i18n.js'

        if not i18n_file.exists():
            print(f"❌ {tool}: Fichier non trouvé")
            failed += 1
            continue

        try:
            fix_i18n_file(i18n_file, tool)
            success += 1
        except Exception as e:
            print(f"❌ {tool}: Erreur - {e}")
            failed += 1

    print("\n" + "="*80)
    print("RÉSULTAT")
    print("="*80)
    print(f"✅ Réussite: {success}/{len(hr_tools)}")
    print(f"❌ Échec: {failed}/{len(hr_tools)}")

    if success == len(hr_tools):
        print("\n🎉 TOUS LES FICHIERS ONT ÉTÉ CORRIGÉS AVEC SUCCÈS!")

    print("="*80)


if __name__ == "__main__":
    main()
