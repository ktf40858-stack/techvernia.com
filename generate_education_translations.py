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
batch_dir = os.path.join(base_dir, "pages", "reviews", "education")

# Dictionnaires de traduction de base (mots communs)
common_translations = {
    "Overview": {
        "de": "Überblick", "es": "Descripción general", "fr": "Aperçu",
        "pt": "Visão geral", "zh": "概述", "ja": "概要",
        "ko": "개요", "ar": "نظرة عامة", "hi": "अवलोकन"
    },
    "Key Features": {
        "de": "Hauptmerkmale", "es": "Características clave", "fr": "Fonctionnalités clés",
        "pt": "Recursos principais", "zh": "主要特点", "ja": "主な機能",
        "ko": "주요 기능", "ar": "الميزات الرئيسية", "hi": "मुख्य विशेषताएं"
    },
    "Advantages": {
        "de": "Vorteile", "es": "Ventajas", "fr": "Avantages",
        "pt": "Vantagens", "zh": "优势", "ja": "利点",
        "ko": "장점", "ar": "المزايا", "hi": "लाभ"
    },
    "Disadvantages": {
        "de": "Nachteile", "es": "Desventajas", "fr": "Inconvénients",
        "pt": "Desvantagens", "zh": "缺点", "ja": "欠点",
        "ko": "단점", "ar": "العيوب", "hi": "नुकसान"
    },
    "Comparison": {
        "de": "Vergleich", "es": "Comparación", "fr": "Comparaison",
        "pt": "Comparação", "zh": "比较", "ja": "比較",
        "ko": "비교", "ar": "مقارنة", "hi": "तुलना"
    },
    "Final Verdict": {
        "de": "Endgültiges Urteil", "es": "Veredicto final", "fr": "Verdict final",
        "pt": "Veredicto final", "zh": "最终评价", "ja": "最終評価",
        "ko": "최종 평가", "ar": "الحكم النهائي", "hi": "अंतिम निर्णय"
    },
    "Frequently Asked Questions": {
        "de": "Häufig gestellte Fragen", "es": "Preguntas frecuentes", "fr": "Questions fréquemment posées",
        "pt": "Perguntas frequentes", "zh": "常见问题", "ja": "よくある質問",
        "ko": "자주 묻는 질문", "ar": "الأسئلة الشائعة", "hi": "अक्सर पूछे जाने वाले प्रश्न"
    },
    "Best Use Cases": {
        "de": "Best Use Cases", "es": "Mejores casos de uso", "fr": "Meilleurs cas d'utilisation",
        "pt": "Melhores casos de uso", "zh": "最佳用例", "ja": "最適な使用例",
        "ko": "최적 사용 사례", "ar": "أفضل حالات الاستخدام", "hi": "सर्वोत्तम उपयोग के मामले"
    },
    "Key Advantages": {
        "de": "Hauptvorteile", "es": "Ventajas clave", "fr": "Principaux avantages",
        "pt": "Principais vantagens", "zh": "主要优势", "ja": "主な利点",
        "ko": "주요 장점", "ar": "المزايا الرئيسية", "hi": "मुख्य लाभ"
    },
    "Excellent Choice": {
        "de": "Ausgezeichnete Wahl", "es": "Excelente elección", "fr": "Excellent choix",
        "pt": "Excelente escolha", "zh": "绝佳选择", "ja": "優れた選択",
        "ko": "훌륭한 선택", "ar": "اختيار ممتاز", "hi": "उत्कृष्ट विकल्प"
    }
}

def extract_en_translations(js_file):
    """Extrait les traductions EN du fichier i18n.js"""
    with open(js_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Trouver le bloc "en": { ... }
    pattern = r'"en":\s*({[^}]+(?:{[^}]*}[^}]*)*})'
    match = re.search(pattern, content, re.DOTALL)

    if match:
        try:
            en_block = match.group(1)
            # Nettoyer et parser
            en_dict = {}
            key_pattern = r'"([^"]+)":\s*"([^"]*(?:\\.[^"]*)*)"'
            matches = re.findall(key_pattern, match.group(1))
            for key, value in matches:
                en_dict[key] = value.replace('\\"', '"').replace('\\n', '\n')
            return en_dict
        except Exception as e:
            print(f"[ERROR] Parsing EN translations: {e}")
            return {}

    return {}

def simple_translate(text, lang):
    """Traduction basique utilisant les dictionnaires communs"""
    # Vérifier si c'est une traduction commune
    if text in common_translations and lang in common_translations[text]:
        return common_translations[text][lang]

    # Pour les textes longs, retourner l'anglais (sera traduit par batch)
    return text

def create_batch_translations(tool, en_translations):
    """Crée les fichiers batch avec les traductions"""
    languages = ["de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]

    # Diviser les clés en 3 batches
    keys = list(en_translations.keys())
    batch_size = (len(keys) + 2) // 3  # Arrondi supérieur

    for batch_num in range(1, 4):
        start_idx = (batch_num - 1) * batch_size
        end_idx = min(start_idx + batch_size, len(keys))
        batch_keys = keys[start_idx:end_idx]

        if not batch_keys:
            continue

        batch_data = {}

        for lang in languages:
            batch_data[lang] = {}
            for key in batch_keys:
                en_text = en_translations[key]
                # Utiliser la traduction simple pour l'instant
                translated = simple_translate(en_text, lang)
                batch_data[lang][key] = translated

        # Sauvegarder le batch
        batch_file = os.path.join(batch_dir, f"{tool}-batch{batch_num}.json")
        with open(batch_file, 'w', encoding='utf-8') as f:
            json.dump(batch_data, f, indent=2, ensure_ascii=False)

        print(f"[OK] Created {tool}-batch{batch_num}.json ({len(batch_keys)} keys × {len(languages)} languages)")

def tool_to_camel(tool):
    """Convertit khan-academy-ai en khanAcademyAi"""
    parts = tool.split('-')
    return parts[0] + ''.join(p.capitalize() for p in parts[1:])

def tool_to_title(tool):
    """Convertit khan-academy-ai en Khan Academy Ai"""
    return ' '.join(p.capitalize() for p in tool.split('-'))

# Étape 1: Créer les fichiers batch
print("=" * 60)
print("STEP 1: Creating batch translation files...")
print("=" * 60)

for tool in tools:
    js_file = os.path.join(js_dir, f"{tool}-i18n.js")

    if not os.path.exists(js_file):
        print(f"[SKIP] {tool}-i18n.js not found")
        continue

    en_translations = extract_en_translations(js_file)

    if not en_translations:
        print(f"[ERROR] No English translations found in {tool}-i18n.js")
        continue

    create_batch_translations(tool, en_translations)

print("\n" + "=" * 60)
print("[INFO] Batch files created with basic translations.")
print("[INFO] For production, these should be professionally translated.")
print("=" * 60)
