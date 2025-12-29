#!/usr/bin/env python3
"""
Add sidebar translations to Gaming i18n files
"""

import re
import os

# Sidebar translations mapping (same as fix_gaming_sidebar.py)
SIDEBAR_TRANSLATIONS = {
    "Rating Breakdown": {
        "key": "sidebar.rating-breakdown",
        "translations": {
            "de": "Bewertungsaufschlüsselung",
            "fr": "Répartition des Notes",
            "es": "Desglose de Calificación",
            "pt": "Detalhamento da Avaliação",
            "zh": "评分详情",
            "ja": "評価の内訳",
            "ko": "평가 세부사항",
            "ar": "تفصيل التقييم",
            "hi": "रेटिंग विवरण"
        }
    },
    "Features": {
        "key": "sidebar.features",
        "translations": {
            "de": "Funktionen",
            "fr": "Fonctionnalités",
            "es": "Características",
            "pt": "Recursos",
            "zh": "功能",
            "ja": "機能",
            "ko": "기능",
            "ar": "الميزات",
            "hi": "विशेषताएं"
        }
    },
    "Ease of Use": {
        "key": "sidebar.ease-of-use",
        "translations": {
            "de": "Benutzerfreundlichkeit",
            "fr": "Facilité d'utilisation",
            "es": "Facilidad de uso",
            "pt": "Facilidade de uso",
            "zh": "易用性",
            "ja": "使いやすさ",
            "ko": "사용 편의성",
            "ar": "سهولة الاستخدام",
            "hi": "उपयोग में आसानी"
        }
    },
    "Value": {
        "key": "sidebar.value",
        "translations": {
            "de": "Wert",
            "fr": "Valeur",
            "es": "Valor",
            "pt": "Valor",
            "zh": "价值",
            "ja": "価値",
            "ko": "가치",
            "ar": "القيمة",
            "hi": "मूल्य"
        }
    },
    "Support": {
        "key": "sidebar.support",
        "translations": {
            "de": "Support",
            "fr": "Support",
            "es": "Soporte",
            "pt": "Suporte",
            "zh": "支持",
            "ja": "サポート",
            "ko": "지원",
            "ar": "الدعم",
            "hi": "सहायता"
        }
    },
    "Performance": {
        "key": "sidebar.performance",
        "translations": {
            "de": "Leistung",
            "fr": "Performance",
            "es": "Rendimiento",
            "pt": "Desempenho",
            "zh": "性能",
            "ja": "パフォーマンス",
            "ko": "성능",
            "ar": "الأداء",
            "hi": "प्रदर्शन"
        }
    },
    "Quick Info": {
        "key": "sidebar.quick-info",
        "translations": {
            "de": "Schnellinfo",
            "fr": "Infos Rapides",
            "es": "Información Rápida",
            "pt": "Informações Rápidas",
            "zh": "快速信息",
            "ja": "クイック情報",
            "ko": "빠른 정보",
            "ar": "معلومات سريعة",
            "hi": "त्वरित जानकारी"
        }
    },
    "Category": {
        "key": "sidebar.category",
        "translations": {
            "de": "Kategorie",
            "fr": "Catégorie",
            "es": "Categoría",
            "pt": "Categoria",
            "zh": "类别",
            "ja": "カテゴリー",
            "ko": "카테고리",
            "ar": "الفئة",
            "hi": "श्रेणी"
        }
    },
    "Gaming": {
        "key": "sidebar.category-gaming",
        "translations": {
            "de": "Gaming",
            "fr": "Gaming",
            "es": "Gaming",
            "pt": "Gaming",
            "zh": "游戏",
            "ja": "ゲーミング",
            "ko": "게이밍",
            "ar": "الألعاب",
            "hi": "गेमिंग"
        }
    },
    "Pricing": {
        "key": "sidebar.pricing",
        "translations": {
            "de": "Preise",
            "fr": "Tarifs",
            "es": "Precios",
            "pt": "Preços",
            "zh": "定价",
            "ja": "料金",
            "ko": "가격",
            "ar": "التسعير",
            "hi": "मूल्य निर्धारण"
        }
    },
    "From Free": {
        "key": "sidebar.pricing-from-free",
        "translations": {
            "de": "Ab Kostenlos",
            "fr": "Dès Gratuit",
            "es": "Desde Gratis",
            "pt": "A partir de Grátis",
            "zh": "从免费开始",
            "ja": "無料から",
            "ko": "무료부터",
            "ar": "من مجاني",
            "hi": "मुफ़्त से"
        }
    },
    "Free Trial": {
        "key": "sidebar.free-trial",
        "translations": {
            "de": "Kostenlose Testversion",
            "fr": "Essai Gratuit",
            "es": "Prueba Gratuita",
            "pt": "Teste Gratuito",
            "zh": "免费试用",
            "ja": "無料トライアル",
            "ko": "무료 체험",
            "ar": "تجربة مجانية",
            "hi": "निःशुल्क परीक्षण"
        }
    },
    "14 days": {
        "key": "sidebar.trial-14-days",
        "translations": {
            "de": "14 Tage",
            "fr": "14 jours",
            "es": "14 días",
            "pt": "14 dias",
            "zh": "14天",
            "ja": "14日間",
            "ko": "14일",
            "ar": "14 يومًا",
            "hi": "14 दिन"
        }
    },
    "Platform": {
        "key": "sidebar.platform",
        "translations": {
            "de": "Plattform",
            "fr": "Plateforme",
            "es": "Plataforma",
            "pt": "Plataforma",
            "zh": "平台",
            "ja": "プラットフォーム",
            "ko": "플랫폼",
            "ar": "المنصة",
            "hi": "प्लेटफ़ॉर्म"
        }
    },
    "Web, Mobile": {
        "key": "sidebar.platform-web-mobile",
        "translations": {
            "de": "Web, Mobil",
            "fr": "Web, Mobile",
            "es": "Web, Móvil",
            "pt": "Web, Móvel",
            "zh": "网页，移动",
            "ja": "ウェブ、モバイル",
            "ko": "웹, 모바일",
            "ar": "ويب، موبايل",
            "hi": "वेब, मोबाइल"
        }
    },
    "Table of Contents": {
        "key": "sidebar.table-of-contents",
        "translations": {
            "de": "Inhaltsverzeichnis",
            "fr": "Table des Matières",
            "es": "Tabla de Contenidos",
            "pt": "Índice",
            "zh": "目录",
            "ja": "目次",
            "ko": "목차",
            "ar": "جدول المحتويات",
            "hi": "विषय-सूची"
        }
    },
    "Overview": {
        "key": "toc.overview",
        "translations": {
            "de": "Überblick",
            "fr": "Aperçu",
            "es": "Resumen",
            "pt": "Visão Geral",
            "zh": "概览",
            "ja": "概要",
            "ko": "개요",
            "ar": "نظرة عامة",
            "hi": "अवलोकन"
        }
    },
    "Key Features": {
        "key": "toc.key-features",
        "translations": {
            "de": "Hauptmerkmale",
            "fr": "Fonctionnalités Clés",
            "es": "Características Clave",
            "pt": "Recursos Principais",
            "zh": "主要功能",
            "ja": "主な機能",
            "ko": "주요 기능",
            "ar": "الميزات الرئيسية",
            "hi": "मुख्य विशेषताएं"
        }
    },
    "Pros & Cons": {
        "key": "toc.pros-cons",
        "translations": {
            "de": "Vor- & Nachteile",
            "fr": "Avantages & Inconvénients",
            "es": "Pros & Contras",
            "pt": "Prós & Contras",
            "zh": "优缺点",
            "ja": "長所と短所",
            "ko": "장단점",
            "ar": "الإيجابيات والسلبيات",
            "hi": "फायदे और नुकसान"
        }
    },
    "Use Cases": {
        "key": "toc.use-cases",
        "translations": {
            "de": "Anwendungsfälle",
            "fr": "Cas d'Usage",
            "es": "Casos de Uso",
            "pt": "Casos de Uso",
            "zh": "使用场景",
            "ja": "使用例",
            "ko": "사용 사례",
            "ar": "حالات الاستخدام",
            "hi": "उपयोग के मामले"
        }
    },
    "Comparison": {
        "key": "toc.comparison",
        "translations": {
            "de": "Vergleich",
            "fr": "Comparaison",
            "es": "Comparación",
            "pt": "Comparação",
            "zh": "对比",
            "ja": "比較",
            "ko": "비교",
            "ar": "المقارنة",
            "hi": "तुलना"
        }
    },
    "FAQ": {
        "key": "toc.faq",
        "translations": {
            "de": "FAQ",
            "fr": "FAQ",
            "es": "FAQ",
            "pt": "FAQ",
            "zh": "常见问题",
            "ja": "よくある質問",
            "ko": "FAQ",
            "ar": "الأسئلة الشائعة",
            "hi": "सामान्य प्रश्न"
        }
    },
    "Final Verdict": {
        "key": "toc.final-verdict",
        "translations": {
            "de": "Endgültiges Urteil",
            "fr": "Verdict Final",
            "es": "Veredicto Final",
            "pt": "Veredicto Final",
            "zh": "最终评价",
            "ja": "最終評価",
            "ko": "최종 평가",
            "ar": "الحكم النهائي",
            "hi": "अंतिम निर्णय"
        }
    }
}

GAMING_I18N_FILES = [
    "artomatix-i18n.js",
    "charismaai-i18n.js",
    "hidden-door-i18n.js",
    "inworld-ai-i18n.js",
    "latitude-ai-dungeon-i18n.js",
    "ludoai-i18n.js",
    "promethean-ai-i18n.js",
    "rct-ai-i18n.js",
    "replika-i18n.js",
    "rosebud-ai-i18n.js",
    "scenario-i18n.js"
]

def add_sidebar_translations_to_i18n(i18n_path):
    """Add sidebar translations to i18n file"""

    with open(i18n_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    additions = 0

    # Add English translations first
    for text, data in SIDEBAR_TRANSLATIONS.items():
        key = data['key']

        # Check if already exists
        if f'"{key}"' in content:
            continue

        # Find the English section - add at the end before closing brace
        en_pattern = r'("en":\s*\{)([\s\S]*?)(\s*\})'
        match = re.search(en_pattern, content)

        if match:
            # Add before the closing brace of the en section
            insert_pos = match.end(2)
            new_entry = f',\n      "{key}": "{text}"'
            content = content[:insert_pos] + new_entry + content[insert_pos:]
            additions += 1

    # Add translations for each language
    for text, data in SIDEBAR_TRANSLATIONS.items():
        key = data['key']

        for lang_code, translation in data['translations'].items():
            # Check if translation already exists
            lang_pattern = f'"{lang_code}":[\\s\\S]*?"{key}"'
            if re.search(lang_pattern, content):
                continue

            # Find the language section
            lang_section_pattern = f'("{lang_code}":\\s*{{)([\\s\\S]*?)(\\s*}})'
            match = re.search(lang_section_pattern, content)

            if match:
                insert_pos = match.end(2)
                new_entry = f',\n      "{key}": "{translation}"'
                content = content[:insert_pos] + new_entry + content[insert_pos:]
                additions += 1

    if content != original_content:
        with open(i18n_path, 'w', encoding='utf-8') as f:
            f.write(content)

    return additions

def main():
    js_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\js"

    print("="*60)
    print("ADDING SIDEBAR TRANSLATIONS TO GAMING I18N FILES")
    print("="*60)
    print()

    total_additions = 0

    for i18n_file in GAMING_I18N_FILES:
        i18n_path = os.path.join(js_dir, i18n_file)

        if not os.path.exists(i18n_path):
            print(f"[SKIP] File not found: {i18n_file}")
            continue

        additions = add_sidebar_translations_to_i18n(i18n_path)
        print(f"[OK] {i18n_file}: {additions} translations added")
        total_additions += additions

    print()
    print("="*60)
    print(f"TOTAL SIDEBAR TRANSLATIONS ADDED: {total_additions}")
    print("="*60)
    print()
    print("Sidebar translation implementation complete!")

if __name__ == "__main__":
    main()
