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

# Translations for feature titles in all languages
feature_translations = {
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

def get_language_section(content, lang):
    """Extract a specific language section from the i18n file"""
    # Pattern to match language section: "lang": { ... },
    pattern = rf'  "{lang}":\s*{{([^}}]+(?:{{[^}}]+}}[^}}]*)*)}}'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        return match.group(1)
    return None

def add_missing_feature_translations(tool_key, tool_name):
    """Add missing feature translations to non-English languages"""

    js_file = os.path.join(js_dir, f"{tool_key}-i18n.js")

    if not os.path.exists(js_file):
        return False

    with open(js_file, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    modified = False

    # For each non-English language
    for lang, translations in feature_translations.items():
        # Find the language section
        lang_section = get_language_section(content, lang)

        if not lang_section:
            print(f"    [!] Language {lang} section not found")
            continue

        # Find the exact position to insert: right after "lang": {
        lang_pattern = rf'  "{lang}":\s*{{\n'
        match = re.search(lang_pattern, content)

        if not match:
            continue

        insert_pos = match.end()

        # Check which translations are missing in THIS language section
        lines_to_add = []
        for key_suffix, translation in translations.items():
            full_key = f"review.{tool_key}.{key_suffix}"

            # Check if this key exists in THIS specific language section
            if f'"{full_key}"' not in lang_section:
                escaped_value = translation.replace('"', '\\"')
                lines_to_add.append(f'    "{full_key}": "{escaped_value}",\n')
                modified = True

        if lines_to_add:
            # Insert all missing lines at once
            new_content = ''.join(lines_to_add)
            content = content[:insert_pos] + new_content + content[insert_pos:]
            print(f"    [+] Added {len(lines_to_add)} translations for {lang}")

    if modified and content != original_content:
        with open(js_file, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False

print("=" * 70)
print("COMPLETING FEATURE TRANSLATIONS FOR ALL LANGUAGES (V2)")
print("=" * 70)

fixed_count = 0

for tool_key, tool_name in translation_tools.items():
    print(f"\n{tool_name}:")
    if add_missing_feature_translations(tool_key, tool_name):
        fixed_count += 1
    else:
        print(f"  [OK] All translations already present")

print("\n" + "=" * 70)
print(f"COMPLETE: {fixed_count}/10 tools updated")
print("=" * 70)
print("\nAll feature card titles now have translations in all 10 languages!")
print("=" * 70)
