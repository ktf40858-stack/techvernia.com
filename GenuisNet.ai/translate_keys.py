#!/usr/bin/env python3
"""
Script de Traduction Automatique des Clés i18n
Utilise un dictionnaire de traductions communes + traductions manuelles pour qualité
"""

import json
import os
import sys

PROJECT_ROOT = "/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai"

# Dictionnaire de traductions communes pour accélérer le processus
COMMON_TRANSLATIONS = {
    # Boutons et actions
    "Explore": {"es": "Explorar", "fr": "Explorer", "de": "Erkunden", "pt": "Explorar", "zh": "探索", "ja": "探索する", "ko": "탐색", "ar": "استكشف", "hi": "एक्सप्लोर करें"},
    "Read": {"es": "Leer", "fr": "Lire", "de": "Lesen", "pt": "Ler", "zh": "阅读", "ja": "読む", "ko": "읽기", "ar": "اقرأ", "hi": "पढ़ें"},
    "Browse": {"es": "Navegar", "fr": "Parcourir", "de": "Durchsuchen", "pt": "Navegar", "zh": "浏览", "ja": "閲覧", "ko": "탐색", "ar": "تصفح", "hi": "ब्राउज़ करें"},
    "Try": {"es": "Probar", "fr": "Essayer", "de": "Testen", "pt": "Experimentar", "zh": "试用", "ja": "試す", "ko": "시도", "ar": "جرب", "hi": "प्रयास करें"},
    "Search": {"es": "Buscar", "fr": "Rechercher", "de": "Suchen", "pt": "Pesquisar", "zh": "搜索", "ja": "検索", "ko": "검색", "ar": "بحث", "hi": "खोजें"},
    "Free": {"es": "Gratis", "fr": "Gratuit", "de": "Kostenlos", "pt": "Grátis", "zh": "免费", "ja": "無料", "ko": "무료", "ar": "مجاني", "hi": "मुक्त"},
    "Categories": {"es": "Categorías", "fr": "Catégories", "de": "Kategorien", "pt": "Categorias", "zh": "类别", "ja": "カテゴリー", "ko": "카테고리", "ar": "الفئات", "hi": "श्रेणियाँ"},
    "Tools": {"es": "Herramientas", "fr": "Outils", "de": "Werkzeuge", "pt": "Ferramentas", "zh": "工具", "ja": "ツール", "ko": "도구", "ar": "الأدوات", "hi": "टूल्स"},
    "AI Tools": {"es": "Herramientas IA", "fr": "Outils IA", "de": "KI-Tools", "pt": "Ferramentas IA", "zh": "AI工具", "ja": "AIツール", "ko": "AI 도구", "ar": "أدوات الذكاء الاصطناعي", "hi": "AI टूल्स"},
    "Review": {"es": "Reseña", "fr": "Revue", "de": "Bewertung", "pt": "Avaliação", "zh": "评论", "ja": "レビュー", "ko": "리뷰", "ar": "مراجعة", "hi": "समीक्षा"},
    "Full Review": {"es": "Reseña Completa", "fr": "Revue Complète", "de": "Vollständige Bewertung", "pt": "Avaliação Completa", "zh": "完整评论", "ja": "完全なレビュー", "ko": "전체 리뷰", "ar": "المراجعة الكاملة", "hi": "पूर्ण समीक्षा"},
    "Guides": {"es": "Guías", "fr": "Guides", "de": "Anleitungen", "pt": "Guias", "zh": "指南", "ja": "ガイド", "ko": "가이드", "ar": "الأدلة", "hi": "गाइड"},
    "Latest": {"es": "Últimas", "fr": "Dernières", "de": "Neueste", "pt": "Últimas", "zh": "最新", "ja": "最新", "ko": "최신", "ar": "الأحدث", "hi": "नवीनतम"},
    "Popular": {"es": "Popular", "fr": "Populaire", "de": "Beliebt", "pt": "Popular", "zh": "热门", "ja": "人気", "ko": "인기", "ar": "شائع", "hi": "लोकप्रिय"},
    "Featured": {"es": "Destacado", "fr": "En vedette", "de": "Empfohlen", "pt": "Destaque", "zh": "精选", "ja": "おすすめ", "ko": "추천", "ar": "مميز", "hi": "फ़ीचर्ड"},

    # Sections
    "Discover": {"es": "Descubre", "fr": "Découvrez", "de": "Entdecken", "pt": "Descubra", "zh": "发现", "ja": "発見する", "ko": "발견하다", "ar": "اكتشف", "hi": "खोजें"},
    "Future": {"es": "Futuro", "fr": "Avenir", "de": "Zukunft", "pt": "Futuro", "zh": "未来", "ja": "未来", "ko": "미래", "ar": "المستقبل", "hi": "भविष्य"},
    "Expert": {"es": "Experto", "fr": "Expert", "de": "Experte", "pt": "Especialista", "zh": "专家", "ja": "専門家", "ko": "전문가", "ar": "خبير", "hi": "विशेषज्ञ"},
    "Insights": {"es": "Perspectivas", "fr": "Analyses", "de": "Einblicke", "pt": "Insights", "zh": "洞察", "ja": "インサイト", "ko": "인사이트", "ar": "رؤى", "hi": "इनसाइट्स"},
    "Updated": {"es": "Actualizado", "fr": "Mis à jour", "de": "Aktualisiert", "pt": "Atualizado", "zh": "更新", "ja": "更新済み", "ko": "업데이트됨", "ar": "محدث", "hi": "अपडेट किया गया"},
    "Selection": {"es": "Selección", "fr": "Sélection", "de": "Auswahl", "pt": "Seleção", "zh": "精选", "ja": "セレクション", "ko": "선택", "ar": "اختيار", "hi": "चयन"},
    "Curated": {"es": "Seleccionado", "fr": "Sélectionné", "de": "Kuratiert", "pt": "Selecionado", "zh": "精选", "ja": "厳選された", "ko": "선별된", "ar": "منسق", "hi": "चयनित"},

    # Noms d'outils AI (ne pas traduire, garder les noms originaux)
    "ChatGPT": {"es": "ChatGPT", "fr": "ChatGPT", "de": "ChatGPT", "pt": "ChatGPT", "zh": "ChatGPT", "ja": "ChatGPT", "ko": "ChatGPT", "ar": "ChatGPT", "hi": "ChatGPT"},
    "Claude": {"es": "Claude", "fr": "Claude", "de": "Claude", "pt": "Claude", "zh": "Claude", "ja": "Claude", "ko": "Claude", "ar": "Claude", "hi": "Claude"},
    "Midjourney": {"es": "Midjourney", "fr": "Midjourney", "de": "Midjourney", "pt": "Midjourney", "zh": "Midjourney", "ja": "Midjourney", "ko": "Midjourney", "ar": "Midjourney", "hi": "Midjourney"},
    "Cursor": {"es": "Cursor", "fr": "Cursor", "de": "Cursor", "pt": "Cursor", "zh": "Cursor", "ja": "Cursor", "ko": "Cursor", "ar": "Cursor", "hi": "Cursor"},
}

def translate_text(text, target_lang):
    """
    Traduire un texte en utilisant le dictionnaire de traductions communes
    Si la traduction n'existe pas, retourner [TO TRANSLATE] + texte original
    """
    # Vérifier si le texte complet existe dans le dictionnaire
    if text in COMMON_TRANSLATIONS:
        return COMMON_TRANSLATIONS[text].get(target_lang, f"[TO TRANSLATE] {text}")

    # Essayer de traduire mot par mot pour les phrases courtes
    words = text.split()
    if len(words) <= 3:
        translated_words = []
        all_found = True

        for word in words:
            if word in COMMON_TRANSLATIONS:
                translated_words.append(COMMON_TRANSLATIONS[word].get(target_lang, word))
            else:
                all_found = False
                break

        if all_found:
            return ' '.join(translated_words)

    # Si aucune traduction trouvée, marquer pour traduction manuelle
    return f"[TO TRANSLATE] {text}"

def auto_translate_keys(input_file):
    """Traduire automatiquement les clés depuis un fichier JSON"""

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ Erreur lecture fichier: {e}")
        return None

    keys = data.get('keys', {})
    total_keys = len(keys)

    print(f"\n{'='*80}")
    print(f"🔄 TRADUCTION AUTOMATIQUE")
    print(f"{'='*80}\n")
    print(f"Fichier source: {input_file}")
    print(f"Nombre de clés: {total_keys}\n")

    translated_count = 0
    manual_count = 0

    for key, translations in keys.items():
        en_text = translations['en']

        # Traduire dans chaque langue
        for lang in ['es', 'fr', 'de', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']:
            translated = translate_text(en_text, lang)
            translations[lang] = translated

            if not translated.startswith('[TO TRANSLATE]'):
                translated_count += 1
            else:
                manual_count += 1

    total_translations = total_keys * 9  # 9 langues cibles
    auto_percentage = (translated_count / total_translations * 100) if total_translations > 0 else 0

    print(f"📊 Résultats:")
    print(f"   - Traductions automatiques: {translated_count}/{total_translations} ({auto_percentage:.1f}%)")
    print(f"   - À traduire manuellement: {manual_count}/{total_translations} ({100-auto_percentage:.1f}%)")
    print()

    # Sauvegarder le fichier traduit
    output_file = input_file.replace('.json', '_translated.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"✅ Fichier traduit sauvegardé: {output_file}\n")

    return data

def generate_i18n_code(data, output_file):
    """Générer le code JavaScript à ajouter dans i18n.js"""

    keys = data.get('keys', {})
    languages = ['en', 'es', 'fr', 'de', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']

    print(f"{'='*80}")
    print(f"📝 GÉNÉRATION DU CODE i18n.js")
    print(f"{'='*80}\n")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("// ==================== NOUVELLES CLÉS À AJOUTER ====================\n")
        f.write("// Ajouter ces clés dans chaque bloc de langue dans js/i18n.js\n\n")

        for lang in languages:
            lang_name = {
                'en': 'ENGLISH',
                'es': 'ESPAÑOL',
                'fr': 'FRANÇAIS',
                'de': 'DEUTSCH',
                'pt': 'PORTUGUÊS',
                'zh': '中文',
                'ja': '日本語',
                'ko': '한국어',
                'ar': 'العربية',
                'hi': 'हिन्दी'
            }[lang]

            f.write(f"// ========== {lang_name} ({lang.upper()}) ==========\n")
            f.write(f"// À ajouter dans le bloc: {lang}: {{\n\n")

            for key, translations in sorted(keys.items()):
                value = translations[lang]
                # Échapper les guillemets
                value = value.replace('"', '\\"')
                f.write(f'"{key}": "{value}",\n')

            f.write("\n\n")

    print(f"✅ Code i18n généré: {output_file}")
    print(f"\nPour l'ajouter à i18n.js:")
    print(f"  1. Ouvrir js/i18n.js")
    print(f"  2. Copier les clés de chaque langue dans les blocs correspondants")
    print(f"  3. Traduire manuellement les entrées marquées [TO TRANSLATE]")
    print()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 translate_keys.py <fichier_keys.json>")
        sys.exit(1)

    input_file = sys.argv[1]
    if not os.path.isabs(input_file):
        input_file = os.path.join(PROJECT_ROOT, input_file)

    if not os.path.exists(input_file):
        print(f"❌ Fichier non trouvé: {input_file}")
        sys.exit(1)

    # Traduire automatiquement
    data = auto_translate_keys(input_file)

    if not data:
        sys.exit(1)

    # Générer le code i18n.js
    output_code_file = input_file.replace('.json', '_i18n_code.js')
    generate_i18n_code(data, output_code_file)

    print(f"{'='*80}")
    print(f"✅ TRADUCTION TERMINÉE")
    print(f"{'='*80}\n")

if __name__ == "__main__":
    main()
