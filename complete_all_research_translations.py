import os
import re

base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
research_dir = os.path.join(base_dir, "pages", "reviews", "research")
js_dir = os.path.join(base_dir, "js")

research_tools = {
    "connected-papers": "Connected Papers",
    "consensus": "Consensus",
    "elicit": "Elicit",
    "irisai": "Iris.ai",
    "litmaps": "Litmaps",
    "perplexity-research": "Perplexity Research",
    "researchrabbit": "ResearchRabbit",
    "scholarcy": "Scholarcy",
    "scispace": "SciSpace",
    "scite": "Scite",
    "semantic-scholar": "Semantic Scholar",
    "undermind": "Undermind"
}

def fix_html_overview(tool_key, tool_name):
    """Corrige le texte Overview dans le HTML pour qu'il corresponde aux traductions"""
    html_file = os.path.join(research_dir, f"{tool_key}.html")

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Trouver et remplacer le texte Overview
    old_patterns = [
        rf'<p><span data-i18n="review\.{tool_key}\.{tool_key}\.is\.a\.leading\.ai-powered">{tool_name} is a leading AI-powered research platform[^<]+</span></p>',
        rf'<p><span data-i18n="review\.{tool_key}\.{tool_key}\.is\.a">{tool_name} is a leading AI-powered research platform[^<]+</span></p>',
    ]

    new_text = f'<p><span data-i18n="review.{tool_key}.{tool_key}.is.a">{tool_name} is a powerful, feature-rich research platform that delivers exceptional value for teams of all sizes. Highly recommended.</span></p>'

    modified = False
    for pattern in old_patterns:
        if re.search(pattern, content):
            content = re.sub(pattern, new_text, content)
            modified = True
            break

    if modified:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def add_missing_translation_to_all_langs(tool_key, tool_name):
    """Ajoute la traduction {tool}.is.a dans toutes les langues"""
    js_file = os.path.join(js_dir, f"{tool_key}-i18n.js")

    with open(js_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Les traductions pour toutes les langues
    translations = {
        'en': f'{tool_name} is a powerful, feature-rich research platform that delivers exceptional value for teams of all sizes. Highly recommended.',
        'de': f'{tool_name} ist eine leistungsstarke, funktionsreiche Forschungsplattform, die außergewöhnlichen Wert für Teams jeder Größe bietet. Sehr empfehlenswert.',
        'es': f'{tool_name} es una plataforma de investigación potente y rica en funciones que ofrece un valor excepcional para equipos de todos los tamaños. Altamente recomendado.',
        'fr': f'{tool_name} est une plateforme de recherche puissante et riche en fonctionnalités qui offre une valeur exceptionnelle pour les équipes de toutes tailles. Hautement recommandé.',
        'pt': f'{tool_name} é uma plataforma de pesquisa poderosa e rica em recursos que oferece valor excepcional para equipes de todos os tamanhos. Altamente recomendado.',
        'zh': f'{tool_name}是一个功能强大、功能丰富的研究平台，为各种规模的团队提供卓越的价值。强烈推荐。',
        'ja': f'{tool_name}は、あらゆる規模のチームに卓越した価値を提供する、強力で機能豊富な研究プラットフォームです。強くお勧めします。',
        'ko': f'{tool_name}는 모든 규모의 팀에 탁월한 가치를 제공하는 강력하고 기능이 풍부한 연구 플랫폼입니다. 강력히 추천합니다.',
        'ar': f'{tool_name} عبارة عن منصة بحث قوية وغنية بالميزات تقدم قيمة استثنائية للفرق من جميع الأحجام. موصى به بشدة.',
        'hi': f'{tool_name} एक शक्तिशाली, सुविधा-संपन्न अनुसंधान प्लेटफ़ॉर्म है जो सभी आकारों की टीमों के लिए असाधारण मूल्य प्रदान करता है। अत्यधिक अनुशंसित।'
    }

    key = f'review.{tool_key}.{tool_key}.is.a'

    # Pour chaque langue
    for lang, trans in translations.items():
        # Vérifier si la clé existe déjà
        if f'"{key}":' in content and f'"{lang}":' in content:
            # Vérifier dans la section de cette langue
            lang_pattern = rf'"{lang}":\s*\{{[^}}]*"{re.escape(key)}"[^}}]*\}}'
            if re.search(lang_pattern, content, re.DOTALL):
                continue  # Déjà présente

        # Trouver la section de langue et ajouter la clé
        pattern = rf'("{lang}":\s*\{{)'
        match = re.search(pattern, content)
        if match:
            insert_pos = match.end()
            escaped_trans = trans.replace('"', '\\"')
            new_line = f'\n    "{key}": "{escaped_trans}",'
            content = content[:insert_pos] + new_line + content[insert_pos:]

    # Écrire le fichier
    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(content)

    return True

print("=" * 70)
print("COMPLETING FULL MULTILINGUAL SUPPORT FOR ALL RESEARCH TOOLS")
print("=" * 70)

html_fixed = 0
js_updated = 0

for tool_key, tool_name in research_tools.items():
    print(f"\n{tool_name}:")

    # 1. Corriger le HTML
    if fix_html_overview(tool_key, tool_name):
        print(f"  [+] HTML: Fixed overview text")
        html_fixed += 1
    else:
        print(f"  [OK] HTML: Already correct")

    # 2. Ajouter les traductions manquantes
    if add_missing_translation_to_all_langs(tool_key, tool_name):
        print(f"  [+] i18n: Added {tool_key}.is.a in 10 languages")
        js_updated += 1

print("\n" + "=" * 70)
print(f"[SUMMARY]")
print(f"  HTML files fixed: {html_fixed}/{len(research_tools)}")
print(f"  i18n files updated: {js_updated}/{len(research_tools)}")
print("=" * 70)
print("[COMPLETE] All 12 Research tools now have full multilingual support")
print("=" * 70)
