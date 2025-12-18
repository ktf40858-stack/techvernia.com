#!/usr/bin/env python3
"""
Dictionnaires de traduction pour les 10 langues
Termes communs utilisés dans toutes les pages de review
"""

# Structure: EN -> {lang: translation}
TRANSLATIONS = {
    # ==================== SECTION TITLES ====================
    "Overview": {
        "en": "Overview",
        "fr": "Aperçu",
        "es": "Resumen",
        "de": "Überblick",
        "pt": "Visão Geral",
        "zh": "概述",
        "ja": "概要",
        "ko": "개요",
        "ar": "نظرة عامة",
        "hi": "अवलोकन"
    },
    "Key Features": {
        "en": "Key Features",
        "fr": "Fonctionnalités Clés",
        "es": "Características Clave",
        "de": "Hauptfunktionen",
        "pt": "Recursos Principais",
        "zh": "主要功能",
        "ja": "主な機能",
        "ko": "주요 기능",
        "ar": "الميزات الرئيسية",
        "hi": "मुख्य विशेषताएं"
    },
    "Additional Features": {
        "en": "Additional Features",
        "fr": "Fonctionnalités Supplémentaires",
        "es": "Características Adicionales",
        "de": "Zusätzliche Funktionen",
        "pt": "Recursos Adicionais",
        "zh": "附加功能",
        "ja": "追加機能",
        "ko": "추가 기능",
        "ar": "ميزات إضافية",
        "hi": "अतिरिक्त विशेषताएं"
    },
    "Pros & Cons": {
        "en": "Pros & Cons",
        "fr": "Avantages & Inconvénients",
        "es": "Ventajas y Desventajas",
        "de": "Vor- & Nachteile",
        "pt": "Prós e Contras",
        "zh": "优缺点",
        "ja": "長所と短所",
        "ko": "장단점",
        "ar": "المزايا والعيوب",
        "hi": "फायदे और नुकसान"
    },
    "Advantages": {
        "en": "Advantages",
        "fr": "Avantages",
        "es": "Ventajas",
        "de": "Vorteile",
        "pt": "Vantagens",
        "zh": "优势",
        "ja": "利点",
        "ko": "장점",
        "ar": "المزايا",
        "hi": "फायदे"
    },
    "Disadvantages": {
        "en": "Disadvantages",
        "fr": "Inconvénients",
        "es": "Desventajas",
        "de": "Nachteile",
        "pt": "Desvantagens",
        "zh": "缺点",
        "ja": "欠点",
        "ko": "단점",
        "ar": "العيوب",
        "hi": "नुकसान"
    },
    "Pricing Plans": {
        "en": "Pricing Plans",
        "fr": "Plans Tarifaires",
        "es": "Planes de Precios",
        "de": "Preispläne",
        "pt": "Planos de Preços",
        "zh": "价格方案",
        "ja": "料金プラン",
        "ko": "가격 플랜",
        "ar": "خطط التسعير",
        "hi": "मूल्य निर्धारण योजनाएं"
    },
    "Pricing": {
        "en": "Pricing",
        "fr": "Tarification",
        "es": "Precios",
        "de": "Preise",
        "pt": "Preços",
        "zh": "定价",
        "ja": "価格",
        "ko": "가격",
        "ar": "التسعير",
        "hi": "मूल्य निर्धारण"
    },
    "Best Use Cases": {
        "en": "Best Use Cases",
        "fr": "Meilleurs Cas d'Usage",
        "es": "Mejores Casos de Uso",
        "de": "Beste Anwendungsfälle",
        "pt": "Melhores Casos de Uso",
        "zh": "最佳用例",
        "ja": "最適な使用例",
        "ko": "최상의 사용 사례",
        "ar": "أفضل حالات الاستخدام",
        "hi": "सर्वोत्तम उपयोग के मामले"
    },
    "Use Cases": {
        "en": "Use Cases",
        "fr": "Cas d'Usage",
        "es": "Casos de Uso",
        "de": "Anwendungsfälle",
        "pt": "Casos de Uso",
        "zh": "用例",
        "ja": "使用例",
        "ko": "사용 사례",
        "ar": "حالات الاستخدام",
        "hi": "उपयोग के मामले"
    },
    "Comparison with Competitors": {
        "en": "Comparison with Competitors",
        "fr": "Comparaison avec les Concurrents",
        "es": "Comparación con Competidores",
        "de": "Vergleich mit Konkurrenten",
        "pt": "Comparação com Concorrentes",
        "zh": "与竞争对手的比较",
        "ja": "競合他社との比較",
        "ko": "경쟁사와의 비교",
        "ar": "مقارنة مع المنافسين",
        "hi": "प्रतिस्पर्धियों के साथ तुलना"
    },
    "Comparison": {
        "en": "Comparison",
        "fr": "Comparaison",
        "es": "Comparación",
        "de": "Vergleich",
        "pt": "Comparação",
        "zh": "比较",
        "ja": "比較",
        "ko": "비교",
        "ar": "مقارنة",
        "hi": "तुलना"
    },
    "Screenshots & Interface": {
        "en": "Screenshots & Interface",
        "fr": "Captures d'Écran et Interface",
        "es": "Capturas de Pantalla e Interfaz",
        "de": "Screenshots & Benutzeroberfläche",
        "pt": "Capturas de Tela e Interface",
        "zh": "截图和界面",
        "ja": "スクリーンショットとインターフェース",
        "ko": "스크린샷 및 인터페이스",
        "ar": "لقطات الشاشة والواجهة",
        "hi": "स्क्रीनशॉट और इंटरफेस"
    },
    "Screenshots": {
        "en": "Screenshots",
        "fr": "Captures d'Écran",
        "es": "Capturas de Pantalla",
        "de": "Screenshots",
        "pt": "Capturas de Tela",
        "zh": "截图",
        "ja": "スクリーンショット",
        "ko": "스크린샷",
        "ar": "لقطات الشاشة",
        "hi": "स्क्रीनशॉट"
    },
    "Final Verdict": {
        "en": "Final Verdict",
        "fr": "Verdict Final",
        "es": "Veredicto Final",
        "de": "Abschließendes Urteil",
        "pt": "Veredicto Final",
        "zh": "最终评价",
        "ja": "最終評価",
        "ko": "최종 평가",
        "ar": "الحكم النهائي",
        "hi": "अंतिम निर्णय"
    },
    "Verdict": {
        "en": "Verdict",
        "fr": "Verdict",
        "es": "Veredicto",
        "de": "Urteil",
        "pt": "Veredicto",
        "zh": "评价",
        "ja": "評価",
        "ko": "평가",
        "ar": "الحكم",
        "hi": "निर्णय"
    },
    "Frequently Asked Questions": {
        "en": "Frequently Asked Questions",
        "fr": "Questions Fréquemment Posées",
        "es": "Preguntas Frecuentes",
        "de": "Häufig Gestellte Fragen",
        "pt": "Perguntas Frequentes",
        "zh": "常见问题",
        "ja": "よくある質問",
        "ko": "자주 묻는 질문",
        "ar": "الأسئلة الشائعة",
        "hi": "अक्सर पूछे जाने वाले प्रश्न"
    },
    "FAQ": {
        "en": "FAQ",
        "fr": "FAQ",
        "es": "Preguntas Frecuentes",
        "de": "FAQ",
        "pt": "FAQ",
        "zh": "常见问题",
        "ja": "FAQ",
        "ko": "FAQ",
        "ar": "الأسئلة الشائعة",
        "hi": "सामान्य प्रश्न"
    },

    # ==================== BADGES & LABELS ====================
    "Free Tier Available": {
        "en": "Free Tier Available",
        "fr": "Niveau Gratuit Disponible",
        "es": "Nivel Gratis Disponible",
        "de": "Kostenlose Stufe Verfügbar",
        "pt": "Nível Gratuito Disponível",
        "zh": "免费版本可用",
        "ja": "無料版利用可能",
        "ko": "무료 등급 이용 가능",
        "ar": "مستوى مجاني متاح",
        "hi": "निःशुल्क स्तर उपलब्ध"
    },
    "Most Popular": {
        "en": "Most Popular",
        "fr": "Plus Populaire",
        "es": "Más Popular",
        "de": "Am Beliebtesten",
        "pt": "Mais Popular",
        "zh": "最受欢迎",
        "ja": "最も人気",
        "ko": "가장 인기 있는",
        "ar": "الأكثر شعبية",
        "hi": "सबसे लोकप्रिय"
    },
    "Expert Rating": {
        "en": "Expert Rating",
        "fr": "Note d'Expert",
        "es": "Calificación de Expertos",
        "de": "Expertenbewertung",
        "pt": "Avaliação de Especialistas",
        "zh": "专家评分",
        "ja": "専門家評価",
        "ko": "전문가 평가",
        "ar": "تقييم الخبراء",
        "hi": "विशेषज्ञ रेटिंग"
    },

    # ==================== BUTTONS & CTA ====================
    "Try Free": {
        "en": "Try Free",
        "fr": "Essayer Gratuitement",
        "es": "Probar Gratis",
        "de": "Kostenlos Testen",
        "pt": "Experimentar Grátis",
        "zh": "免费试用",
        "ja": "無料で試す",
        "ko": "무료 체험",
        "ar": "جرب مجانا",
        "hi": "मुफ्त में आजमाएं"
    },
    "View Pricing": {
        "en": "View Pricing",
        "fr": "Voir les Tarifs",
        "es": "Ver Precios",
        "de": "Preise Ansehen",
        "pt": "Ver Preços",
        "zh": "查看价格",
        "ja": "料金を見る",
        "ko": "가격 보기",
        "ar": "عرض الأسعار",
        "hi": "मूल्य देखें"
    },
    "Try It Now": {
        "en": "Try It Now",
        "fr": "Essayer Maintenant",
        "es": "Pruébalo Ahora",
        "de": "Jetzt Ausprobieren",
        "pt": "Experimente Agora",
        "zh": "立即试用",
        "ja": "今すぐ試す",
        "ko": "지금 시도하기",
        "ar": "جربه الآن",
        "hi": "अभी आज़माएं"
    },
    "Learn More": {
        "en": "Learn More",
        "fr": "En Savoir Plus",
        "es": "Saber Más",
        "de": "Mehr Erfahren",
        "pt": "Saiba Mais",
        "zh": "了解更多",
        "ja": "詳細を見る",
        "ko": "자세히 알아보기",
        "ar": "اعرف المزيد",
        "hi": "और जानें"
    },
    "Get Started": {
        "en": "Get Started",
        "fr": "Commencer",
        "es": "Comenzar",
        "de": "Loslegen",
        "pt": "Começar",
        "zh": "开始",
        "ja": "始める",
        "ko": "시작하기",
        "ar": "ابدأ",
        "hi": "शुरू करें"
    },

    # ==================== STATS & METRICS ====================
    "Monthly Active Users": {
        "en": "Monthly Active Users",
        "fr": "Utilisateurs Actifs Mensuels",
        "es": "Usuarios Activos Mensuales",
        "de": "Monatlich Aktive Benutzer",
        "pt": "Usuários Ativos Mensais",
        "zh": "每月活跃用户",
        "ja": "月間アクティブユーザー",
        "ko": "월간 활성 사용자",
        "ar": "المستخدمون النشطون شهريًا",
        "hi": "मासिक सक्रिय उपयोगकर्ता"
    },
    "Context Window": {
        "en": "Context Window",
        "fr": "Fenêtre de Contexte",
        "es": "Ventana de Contexto",
        "de": "Kontextfenster",
        "pt": "Janela de Contexto",
        "zh": "上下文窗口",
        "ja": "コンテキストウィンドウ",
        "ko": "컨텍스트 창",
        "ar": "نافذة السياق",
        "hi": "संदर्भ विंडो"
    },
    "Languages Supported": {
        "en": "Languages Supported",
        "fr": "Langues Supportées",
        "es": "Idiomas Soportados",
        "de": "Unterstützte Sprachen",
        "pt": "Idiomas Suportados",
        "zh": "支持的语言",
        "ja": "対応言語",
        "ko": "지원 언어",
        "ar": "اللغات المدعومة",
        "hi": "समर्थित भाषाएँ"
    },
    "Starting Price": {
        "en": "Starting Price",
        "fr": "Prix de Départ",
        "es": "Precio Inicial",
        "de": "Startpreis",
        "pt": "Preço Inicial",
        "zh": "起始价格",
        "ja": "開始価格",
        "ko": "시작 가격",
        "ar": "السعر الأولي",
        "hi": "प्रारंभिक मूल्य"
    },
    "Launch Year": {
        "en": "Launch Year",
        "fr": "Année de Lancement",
        "es": "Año de Lanzamiento",
        "de": "Startjahr",
        "pt": "Ano de Lançamento",
        "zh": "发布年份",
        "ja": "リリース年",
        "ko": "출시 연도",
        "ar": "سنة الإطلاق",
        "hi": "लॉन्च वर्ष"
    },

    # ==================== TABLE HEADERS ====================
    "Plan": {
        "en": "Plan",
        "fr": "Plan",
        "es": "Plan",
        "de": "Plan",
        "pt": "Plano",
        "zh": "计划",
        "ja": "プラン",
        "ko": "플랜",
        "ar": "الخطة",
        "hi": "योजना"
    },
    "Price": {
        "en": "Price",
        "fr": "Prix",
        "es": "Precio",
        "de": "Preis",
        "pt": "Preço",
        "zh": "价格",
        "ja": "価格",
        "ko": "가격",
        "ar": "السعر",
        "hi": "मूल्य"
    },
    "Features": {
        "en": "Features",
        "fr": "Fonctionnalités",
        "es": "Características",
        "de": "Funktionen",
        "pt": "Recursos",
        "zh": "功能",
        "ja": "機能",
        "ko": "기능",
        "ar": "الميزات",
        "hi": "विशेषताएं"
    },
    "Feature": {
        "en": "Feature",
        "fr": "Fonctionnalité",
        "es": "Característica",
        "de": "Funktion",
        "pt": "Recurso",
        "zh": "功能",
        "ja": "機能",
        "ko": "기능",
        "ar": "الميزة",
        "hi": "विशेषता"
    },

    # ==================== COMMON WORDS ====================
    "Yes": {
        "en": "Yes",
        "fr": "Oui",
        "es": "Sí",
        "de": "Ja",
        "pt": "Sim",
        "zh": "是",
        "ja": "はい",
        "ko": "예",
        "ar": "نعم",
        "hi": "हाँ"
    },
    "No": {
        "en": "No",
        "fr": "Non",
        "es": "No",
        "de": "Nein",
        "pt": "Não",
        "zh": "否",
        "ja": "いいえ",
        "ko": "아니요",
        "ar": "لا",
        "hi": "नहीं"
    },
    "Free": {
        "en": "Free",
        "fr": "Gratuit",
        "es": "Gratis",
        "de": "Kostenlos",
        "pt": "Grátis",
        "zh": "免费",
        "ja": "無料",
        "ko": "무료",
        "ar": "مجاني",
        "hi": "निःशुल्क"
    },
    "Custom": {
        "en": "Custom",
        "fr": "Personnalisé",
        "es": "Personalizado",
        "de": "Benutzerdefiniert",
        "pt": "Personalizado",
        "zh": "定制",
        "ja": "カスタム",
        "ko": "맞춤",
        "ar": "مخصص",
        "hi": "कस्टम"
    },

    # ==================== SIDEBAR ====================
    "Table of Contents": {
        "en": "Table of Contents",
        "fr": "Table des Matières",
        "es": "Tabla de Contenidos",
        "de": "Inhaltsverzeichnis",
        "pt": "Índice",
        "zh": "目录",
        "ja": "目次",
        "ko": "목차",
        "ar": "جدول المحتويات",
        "hi": "विषय सूची"
    },
    "Compare With": {
        "en": "Compare With",
        "fr": "Comparer Avec",
        "es": "Comparar Con",
        "de": "Vergleichen Mit",
        "pt": "Comparar Com",
        "zh": "比较",
        "ja": "比較する",
        "ko": "비교",
        "ar": "قارن مع",
        "hi": "के साथ तुलना करें"
    },
    "Quick Info": {
        "en": "Quick Info",
        "fr": "Infos Rapides",
        "es": "Información Rápida",
        "de": "Schnellinfo",
        "pt": "Informação Rápida",
        "zh": "快速信息",
        "ja": "クイック情報",
        "ko": "빠른 정보",
        "ar": "معلومات سريعة",
        "hi": "त्वरित जानकारी"
    },
    "Company": {
        "en": "Company",
        "fr": "Entreprise",
        "es": "Empresa",
        "de": "Unternehmen",
        "pt": "Empresa",
        "zh": "公司",
        "ja": "会社",
        "ko": "회사",
        "ar": "الشركة",
        "hi": "कंपनी"
    },
    "Founded": {
        "en": "Founded",
        "fr": "Fondée",
        "es": "Fundada",
        "de": "Gegründet",
        "pt": "Fundada",
        "zh": "成立",
        "ja": "設立",
        "ko": "설립",
        "ar": "تأسست",
        "hi": "स्थापित"
    },
    "Headquarters": {
        "en": "Headquarters",
        "fr": "Siège Social",
        "es": "Sede",
        "de": "Hauptsitz",
        "pt": "Sede",
        "zh": "总部",
        "ja": "本社",
        "ko": "본사",
        "ar": "المقر الرئيسي",
        "hi": "मुख्यालय"
    },
    "Platform": {
        "en": "Platform",
        "fr": "Plateforme",
        "es": "Plataforma",
        "de": "Plattform",
        "pt": "Plataforma",
        "zh": "平台",
        "ja": "プラットフォーム",
        "ko": "플랫폼",
        "ar": "المنصة",
        "hi": "प्लेटफ़ॉर्म"
    },
    "API Available": {
        "en": "API Available",
        "fr": "API Disponible",
        "es": "API Disponible",
        "de": "API Verfügbar",
        "pt": "API Disponível",
        "zh": "API可用",
        "ja": "API利用可能",
        "ko": "API 이용 가능",
        "ar": "واجهة برمجة التطبيقات متاحة",
        "hi": "API उपलब्ध"
    },

    # ==================== RATING LABELS ====================
    "Ease of Use": {
        "en": "Ease of Use",
        "fr": "Facilité d'Utilisation",
        "es": "Facilidad de Uso",
        "de": "Benutzerfreundlichkeit",
        "pt": "Facilidade de Uso",
        "zh": "易用性",
        "ja": "使いやすさ",
        "ko": "사용 편의성",
        "ar": "سهولة الاستخدام",
        "hi": "उपयोग में आसानी"
    },
    "Value": {
        "en": "Value",
        "fr": "Rapport Qualité-Prix",
        "es": "Valor",
        "de": "Preis-Leistung",
        "pt": "Valor",
        "zh": "性价比",
        "ja": "コストパフォーマンス",
        "ko": "가치",
        "ar": "القيمة",
        "hi": "मूल्य"
    },
    "Performance": {
        "en": "Performance",
        "fr": "Performance",
        "es": "Rendimiento",
        "de": "Leistung",
        "pt": "Desempenho",
        "zh": "性能",
        "ja": "パフォーマンス",
        "ko": "성능",
        "ar": "الأداء",
        "hi": "प्रदर्शन"
    },
    "Support": {
        "en": "Support",
        "fr": "Support",
        "es": "Soporte",
        "de": "Support",
        "pt": "Suporte",
        "zh": "支持",
        "ja": "サポート",
        "ko": "지원",
        "ar": "الدعم",
        "hi": "समर्थन"
    },

    # ==================== REVIEW TERMS ====================
    "Review": {
        "en": "Review",
        "fr": "Avis",
        "es": "Revisión",
        "de": "Bewertung",
        "pt": "Avaliação",
        "zh": "评测",
        "ja": "レビュー",
        "ko": "리뷰",
        "ar": "مراجعة",
        "hi": "समीक्षा"
    },
    "by": {
        "en": "by",
        "fr": "par",
        "es": "por",
        "de": "von",
        "pt": "por",
        "zh": "由",
        "ja": "by",
        "ko": "제작",
        "ar": "بواسطة",
        "hi": "द्वारा"
    },
    "Our Recommendation": {
        "en": "Our Recommendation",
        "fr": "Notre Recommandation",
        "es": "Nuestra Recomendación",
        "de": "Unsere Empfehlung",
        "pt": "Nossa Recomendação",
        "zh": "我们的推荐",
        "ja": "推奨事項",
        "ko": "권장사항",
        "ar": "توصيتنا",
        "hi": "हमारी सिफारिश"
    },
}

def get_translation(english_text, language_code):
    """Get translation for a given English text in specified language"""
    if english_text in TRANSLATIONS:
        return TRANSLATIONS[english_text].get(language_code, english_text)
    return english_text

def get_all_translations_for_text(english_text):
    """Get all 10 language translations for a text"""
    if english_text in TRANSLATIONS:
        return TRANSLATIONS[english_text]
    # Return English for all if not in dictionary
    return {lang: english_text for lang in ['en', 'fr', 'es', 'de', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']}
