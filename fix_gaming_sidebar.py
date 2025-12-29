#!/usr/bin/env python3
"""
Fix sidebar translations in Gaming category HTML files
Add data-i18n attributes to all sidebar elements
"""

import re
import os

# Sidebar translations mapping
SIDEBAR_TRANSLATIONS = {
    # Rating Breakdown section
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

    # Quick Info section
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

    # Table of Contents
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
    # TOC items
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

GAMING_FILES = [
    "artomatix.html",
    "charismaai.html",
    "hidden-door.html",
    "inworld-ai.html",
    "latitude-ai-dungeon.html",
    "ludoai.html",
    "promethean-ai.html",
    "rct-ai.html",
    "replika.html",
    "rosebud-ai.html",
    "scenario.html"
]

def add_data_i18n_to_sidebar(html_path):
    """Add data-i18n attributes to sidebar elements"""

    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    updates = 0

    for text, data in SIDEBAR_TRANSLATIONS.items():
        i18n_key = data['key']

        # Skip if already has this key
        if f'data-i18n="{i18n_key}"' in content:
            continue

        # Pattern 1: <h3>...Text</h3> or <h3>emoji Text</h3>
        pattern1 = f'(<h3[^>]*>(?:[^<]*?))({re.escape(text)})(</h3>)'
        replacement1 = f'\\1<span data-i18n="{i18n_key}">\\2</span>\\3'

        # Pattern 2: <span class="label">Text</span>
        pattern2 = f'(<span class="(?:stat-)?label">)({re.escape(text)})(</span>)'
        replacement2 = f'\\1<span data-i18n="{i18n_key}">\\2</span>\\3'

        # Pattern 3: <span class="stat-value">Text</span>
        pattern3 = f'(<span class="stat-value">)({re.escape(text)})(</span>)'
        replacement3 = f'\\1<span data-i18n="{i18n_key}">\\2</span>\\3'

        # Pattern 4: <a ...>Text</a> (for TOC)
        pattern4 = f'(<a [^>]*>)({re.escape(text)})(</a>)'
        replacement4 = f'\\1<span data-i18n="{i18n_key}">\\2</span>\\3'

        # Try each pattern
        for pattern, replacement in [(pattern1, replacement1), (pattern2, replacement2), (pattern3, replacement3), (pattern4, replacement4)]:
            new_content = re.sub(pattern, replacement, content)
            if new_content != content:
                content = new_content
                updates += 1
                break

    if content != original_content:
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(content)

    return updates

def main():
    html_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\pages\reviews\gaming"

    print("="*60)
    print("FIXING SIDEBAR TRANSLATIONS IN GAMING CATEGORY")
    print("="*60)
    print()

    total_updates = 0

    for html_file in GAMING_FILES:
        html_path = os.path.join(html_dir, html_file)

        if not os.path.exists(html_path):
            print(f"[SKIP] File not found: {html_file}")
            continue

        updates = add_data_i18n_to_sidebar(html_path)
        print(f"[OK] {html_file}: {updates} data-i18n attributes added")
        total_updates += updates

    print()
    print("="*60)
    print(f"TOTAL SIDEBAR UPDATES: {total_updates}")
    print("="*60)
    print()
    print("Next step: Run script to add translations to i18n files...")

if __name__ == "__main__":
    main()
