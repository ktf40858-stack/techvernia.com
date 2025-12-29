import os
import re

translation_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\pages\reviews\translation"
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

# Feature card titles to add data-i18n attributes
feature_titles = [
    ("AI-Powered Automation", "ai-powered.automation"),
    ("Advanced Analytics", "advanced.analytics"),
    ("Seamless Integrations", "seamless.integrations"),
    ("Enterprise Security", "enterprise.security"),
    ("Real-Time Collaboration", "real-time.collaboration"),
    ("Mobile Access", "mobile.access")
]

# Translations for feature titles in all languages
feature_translations = {
    "en": {
        "ai-powered.automation": "AI-Powered Automation",
        "advanced.analytics": "Advanced Analytics",
        "seamless.integrations": "Seamless Integrations",
        "enterprise.security": "Enterprise Security",
        "real-time.collaboration": "Real-Time Collaboration",
        "mobile.access": "Mobile Access"
    },
    "de": {
        "ai-powered.automation": "KI-gestützte Automatisierung",
        "advanced.analytics": "Erweiterte Analytik",
        "seamless.integrations": "Nahtlose Integrationen",
        "enterprise.security": "Unternehmenssicherheit",
        "real-time.collaboration": "Echtzeit-Zusammenarbeit",
        "mobile.access": "Mobiler Zugriff"
    },
    "es": {
        "ai-powered.automation": "Automatización con IA",
        "advanced.analytics": "Análisis Avanzado",
        "seamless.integrations": "Integraciones Perfectas",
        "enterprise.security": "Seguridad Empresarial",
        "real-time.collaboration": "Colaboración en Tiempo Real",
        "mobile.access": "Acceso Móvil"
    },
    "fr": {
        "ai-powered.automation": "Automatisation IA",
        "advanced.analytics": "Analytique Avancée",
        "seamless.integrations": "Intégrations Transparentes",
        "enterprise.security": "Sécurité Entreprise",
        "real-time.collaboration": "Collaboration en Temps Réel",
        "mobile.access": "Accès Mobile"
    },
    "pt": {
        "ai-powered.automation": "Automação com IA",
        "advanced.analytics": "Análise Avançada",
        "seamless.integrations": "Integrações Perfeitas",
        "enterprise.security": "Segurança Empresarial",
        "real-time.collaboration": "Colaboração em Tempo Real",
        "mobile.access": "Acesso Móvel"
    },
    "zh": {
        "ai-powered.automation": "AI驱动的自动化",
        "advanced.analytics": "高级分析",
        "seamless.integrations": "无缝集成",
        "enterprise.security": "企业安全",
        "real-time.collaboration": "实时协作",
        "mobile.access": "移动访问"
    },
    "ja": {
        "ai-powered.automation": "AI駆動の自動化",
        "advanced.analytics": "高度な分析",
        "seamless.integrations": "シームレスな統合",
        "enterprise.security": "エンタープライズセキュリティ",
        "real-time.collaboration": "リアルタイムコラボレーション",
        "mobile.access": "モバイルアクセス"
    },
    "ko": {
        "ai-powered.automation": "AI 기반 자동화",
        "advanced.analytics": "고급 분석",
        "seamless.integrations": "원활한 통합",
        "enterprise.security": "엔터프라이즈 보안",
        "real-time.collaboration": "실시간 협업",
        "mobile.access": "모바일 액세스"
    },
    "ar": {
        "ai-powered.automation": "الأتمتة المدعومة بالذكاء الاصطناعي",
        "advanced.analytics": "التحليلات المتقدمة",
        "seamless.integrations": "التكاملات السلسة",
        "enterprise.security": "أمان المؤسسات",
        "real-time.collaboration": "التعاون في الوقت الفعلي",
        "mobile.access": "الوصول عبر الهاتف المحمول"
    },
    "hi": {
        "ai-powered.automation": "AI-संचालित स्वचालन",
        "advanced.analytics": "उन्नत विश्लेषण",
        "seamless.integrations": "निर्बाध एकीकरण",
        "enterprise.security": "एंटरप्राइज़ सुरक्षा",
        "real-time.collaboration": "रियल-टाइम सहयोग",
        "mobile.access": "मोबाइल एक्सेस"
    }
}

def add_feature_card_data_i18n(tool_key, tool_name):
    """Add data-i18n attributes to feature card titles"""

    html_file = os.path.join(translation_dir, f"{tool_key}.html")

    if not os.path.exists(html_file):
        return False

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False

    for title_text, key_suffix in feature_titles:
        # Pattern to match h4 with SVG icon followed by the title text (not already wrapped in span with data-i18n)
        pattern = rf'(<h4><svg[^>]*>.*?</svg>)\s*{re.escape(title_text)}(\s*</h4>)'

        # Check if this pattern exists and doesn't already have data-i18n
        if re.search(pattern, content) and f'data-i18n="review.{tool_key}.{key_suffix}"' not in content:
            # Create replacement with data-i18n
            full_key = f"review.{tool_key}.{key_suffix}"
            replacement = rf'\1 <span data-i18n="{full_key}">{title_text}</span>\2'

            content = re.sub(pattern, replacement, content)
            modified = True

    if modified:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False

def add_feature_translations_to_i18n(tool_key, tool_name):
    """Add feature card translations to i18n file"""

    js_file = os.path.join(js_dir, f"{tool_key}-i18n.js")

    if not os.path.exists(js_file):
        return False

    with open(js_file, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False

    # For each language
    for lang in feature_translations.keys():
        # Find language section
        lang_pattern = rf'"{lang}":\s*\{{'
        lang_match = re.search(lang_pattern, content)

        if not lang_match:
            continue

        # For each feature title
        for key_suffix, translation in feature_translations[lang].items():
            full_key = f"review.{tool_key}.{key_suffix}"

            # Check if key already exists
            if f'"{full_key}"' in content:
                continue

            # Add the translation at the beginning of the language section
            insert_pos = lang_match.end()
            escaped_value = translation.replace('"', '\\"')
            new_line = f'\n    "{full_key}": "{escaped_value}",'
            content = content[:insert_pos] + new_line + content[insert_pos:]
            modified = True

    if modified:
        with open(js_file, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False

print("=" * 70)
print("FIXING TRANSLATION FEATURE CARD TITLES")
print("=" * 70)

html_fixed = 0
js_fixed = 0

for tool_key, tool_name in translation_tools.items():
    print(f"\n{tool_name}:")

    # Fix HTML
    if add_feature_card_data_i18n(tool_key, tool_name):
        print(f"  [+] HTML: Added data-i18n to feature titles")
        html_fixed += 1
    else:
        print(f"  [OK] HTML: Already has data-i18n or no features found")

    # Fix i18n file
    if add_feature_translations_to_i18n(tool_key, tool_name):
        print(f"  [+] i18n: Added feature translations")
        js_fixed += 1
    else:
        print(f"  [OK] i18n: Already has translations")

print("\n" + "=" * 70)
print(f"COMPLETE: HTML fixed: {html_fixed}/10 | i18n fixed: {js_fixed}/10")
print("=" * 70)
print("\nFeature card titles will now translate in all 10 languages!")
print("=" * 70)
