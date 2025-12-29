#!/usr/bin/env python3
"""Final translations for remaining English keys"""

import re
import os

# Remaining translations
FINAL_TRANSLATIONS = {
    "Explore {TOOL}'s interface:": {
        "de": "Erkunden Sie die Benutzeroberfläche von {TOOL}:",
        "fr": "Explorez l'interface de {TOOL} :",
        "es": "Explora la interfaz de {TOOL}:",
        "pt": "Explore a interface do {TOOL}:",
        "zh": "探索 {TOOL} 的界面：",
        "ja": "{TOOL}のインターフェースを探索：",
        "ko": "{TOOL}의 인터페이스 살펴보기:",
        "ar": "استكشف واجهة {TOOL}:",
        "hi": "{TOOL} के इंटरफ़ेस का अन्वेषण करें:"
    },
    "Overview": {
        "de": "Überblick",
        "fr": "Aperçu",
        "es": "Descripción General",
        "pt": "Visão Geral",
        "zh": "概览",
        "ja": "概要",
        "ko": "개요",
        "ar": "نظرة عامة",
        "hi": "अवलोकन"
    },
    "Pricing": {
        "de": "Preise",
        "fr": "Tarification",
        "es": "Precios",
        "pt": "Preços",
        "zh": "定价",
        "ja": "価格",
        "ko": "가격",
        "ar": "التسعير",
        "hi": "मूल्य निर्धारण"
    },
    "Pros & Cons": {
        "de": "Vor- & Nachteile",
        "fr": "Avantages & Inconvénients",
        "es": "Pros & Contras",
        "pt": "Vantagens & Desvantagens",
        "zh": "优点与缺点",
        "ja": "長所と短所",
        "ko": "장점과 단점",
        "ar": "المزايا والعيوب",
        "hi": "फायदे और नुकसान"
    },
    "View Pricing": {
        "de": "Preise Ansehen",
        "fr": "Voir la Tarification",
        "es": "Ver Precios",
        "pt": "Ver Preços",
        "zh": "查看定价",
        "ja": "価格を見る",
        "ko": "가격 보기",
        "ar": "عرض الأسعار",
        "hi": "मूल्य देखें"
    },
    "Yes. {TOOL} uses bank-grade encryption, maintains SOC 2 Type II certification, and is compliant with GDPR, HIPAA, and other major regulations. Data is encrypted at rest and in transit.": {
        "de": "Ja. {TOOL} verwendet Verschlüsselung auf Bankniveau, verfügt über SOC 2 Type II-Zertifizierung und ist konform mit GDPR, HIPAA und anderen wichtigen Vorschriften. Daten werden im Ruhezustand und während der Übertragung verschlüsselt.",
        "fr": "Oui. {TOOL} utilise un chiffrement de grade bancaire, maintient la certification SOC 2 Type II et est conforme aux réglementations GDPR, HIPAA et autres réglementations majeures. Les données sont chiffrées au repos et en transit.",
        "es": "Sí. {TOOL} utiliza cifrado de grado bancario, mantiene la certificación SOC 2 Type II y cumple con GDPR, HIPAA y otras regulaciones importantes. Los datos están cifrados en reposo y en tránsito.",
        "pt": "Sim. {TOOL} usa criptografia de nível bancário, mantém certificação SOC 2 Type II e está em conformidade com GDPR, HIPAA e outros regulamentos importantes. Os dados são criptografados em repouso e em trânsito.",
        "zh": "是的。{TOOL} 使用银行级加密，拥有 SOC 2 Type II 认证，并符合 GDPR、HIPAA 和其他主要法规。数据在静止和传输时都经过加密。",
        "ja": "はい。{TOOL}は銀行グレードの暗号化を使用し、SOC 2 Type II認証を維持し、GDPR、HIPAA、その他の主要な規制に準拠しています。データは保存時および転送時に暗号化されます。",
        "ko": "네. {TOOL}는 은행급 암호화를 사용하고 SOC 2 Type II 인증을 유지하며 GDPR, HIPAA 및 기타 주요 규정을 준수합니다. 데이터는 저장 및 전송 시 암호화됩니다.",
        "ar": "نعم. يستخدم {TOOL} تشفيرًا من الدرجة المصرفية، ويحافظ على شهادة SOC 2 Type II، ويتوافق مع GDPR وHIPAA واللوائح الرئيسية الأخرى. يتم تشفير البيانات أثناء الراحة وأثناء النقل.",
        "hi": "हां। {TOOL} बैंक-ग्रेड एन्क्रिप्शन का उपयोग करता है, SOC 2 Type II प्रमाणन बनाए रखता है, और GDPR, HIPAA और अन्य प्रमुख विनियमों का अनुपालन करता है। डेटा आराम और पारगमन दोनों में एन्क्रिप्ट किया गया है।"
    },
}

FILES = [
    "deepl-pro-i18n.js",
    "google-translate-ai-i18n.js",
    "lilt-i18n.js",
    "lokalise-i18n.js",
    "microsoft-translator-i18n.js",
    "modernmt-i18n.js",
    "phrase-i18n.js",
    "smartling-i18n.js",
    "systran-i18n.js",
    "unbabel-i18n.js"
]

TOOL_NAMES = {
    "deepl-pro": "DeepL Pro",
    "google-translate-ai": "Google Translate AI",
    "lilt": "Lilt",
    "lokalise": "Lokalise",
    "microsoft-translator": "Microsoft Translator",
    "modernmt": "ModernMT",
    "phrase": "Phrase",
    "smartling": "Smartling",
    "systran": "Systran",
    "unbabel": "Unbabel"
}

def get_tool_name(filename):
    for key in TOOL_NAMES:
        if filename.startswith(key):
            return TOOL_NAMES[key]
    return "Tool"

def update_final(filepath):
    filename = os.path.basename(filepath)
    tool_name = get_tool_name(filename)

    print(f"Processing {filename}...")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    updates_count = 0

    for english_template, translations in FINAL_TRANSLATIONS.items():
        english_text = english_template.replace("{TOOL}", tool_name)

        for lang_code, translation_template in translations.items():
            translated_text = translation_template.replace("{TOOL}", tool_name)
            english_escaped = re.escape(english_text)

            pattern = f'("{lang_code}":[\\s\\S]*?)(".*?":\\s*")({english_escaped})(")'

            def replacer(match):
                nonlocal updates_count
                updates_count += 1
                return match.group(1) + match.group(2) + translated_text + match.group(4)

            content = re.sub(pattern, replacer, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  [OK] Updated {updates_count} translations")
    return updates_count

def main():
    base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\js"
    total = 0

    for filename in FILES:
        filepath = os.path.join(base_dir, filename)
        if os.path.exists(filepath):
            count = update_final(filepath)
            total += count

    print(f"\n{'='*60}")
    print(f"TOTAL: {total} translations updated")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
