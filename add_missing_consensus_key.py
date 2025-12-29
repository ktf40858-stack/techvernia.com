import os
import re

js_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\js"

# Les traductions à ajouter
missing_translations = {
    "en": "Consensus is a powerful, feature-rich research platform that delivers exceptional value for teams of all sizes. Highly recommended.",
    "de": "Consensus ist eine leistungsstarke, funktionsreiche Forschungsplattform, die außergewöhnlichen Wert für Teams jeder Größe bietet. Sehr empfehlenswert.",
    "es": "Consensus es una plataforma de investigación potente y rica en funciones que ofrece un valor excepcional para equipos de todos los tamaños. Altamente recomendado.",
    "fr": "Consensus est une plateforme de recherche puissante et riche en fonctionnalités qui offre une valeur exceptionnelle pour les équipes de toutes tailles. Hautement recommandé.",
    "pt": "Consensus é uma plataforma de pesquisa poderosa e rica em recursos que oferece valor excepcional para equipes de todos os tamanhos. Altamente recomendado.",
    "zh": "Consensus是一个功能强大、功能丰富的研究平台，为各种规模的团队提供卓越的价值。强烈推荐。",
    "ja": "Consensusは、あらゆる規模のチームに卓越した価値を提供する、強力で機能豊富な研究プラットフォームです。強くお勧めします。",
    "ko": "Consensus는 모든 규모의 팀에 탁월한 가치를 제공하는 강력하고 기능이 풍부한 연구 플랫폼입니다. 강력히 추천합니다.",
    "ar": "Consensus عبارة عن منصة بحث قوية وغنية بالميزات تقدم قيمة استثنائية للفرق من جميع الأحجام. موصى به بشدة.",
    "hi": "Consensus एक शक्तिशाली, सुविधा-संपन्न अनुसंधान प्लेटफ़ॉर्म है जो सभी आकारों की टीमों के लिए असाधारण मूल्य प्रदान करता है। अत्यधिक अनुशंसित।"
}

def add_missing_key():
    js_file = os.path.join(js_dir, "consensus-i18n.js")

    with open(js_file, 'r', encoding='utf-8') as f:
        content = f.read()

    key = "review.consensus.consensus.is.a"

    # Pour chaque langue
    for lang, translation in missing_translations.items():
        # Vérifier si la clé existe déjà
        if f'"{key}":' in content:
            print(f"  [{lang}] Key already exists, skipping")
            continue

        # Trouver la section de langue
        pattern = rf'"{lang}":\s*\{{([^}}]*(?:\{{[^}}]*\}}[^}}]*)*)\}}'
        match = re.search(pattern, content, re.DOTALL)

        if match:
            lang_section = match.group(1)

            # Ajouter la nouvelle clé
            escaped_value = translation.replace('"', '\\"')
            new_item = f'    "{key}": "{escaped_value}",\n'

            # Ajouter au début de la section (après le premier {)
            lang_section_start = content.find(match.group(1))
            # Trouver le premier newline après {
            insert_pos = content.find('\n', content.find(f'"{lang}"'))
            if insert_pos > 0:
                content = content[:insert_pos + 1] + new_item + content[insert_pos + 1:]

            print(f"  [{lang}] Added translation")

    # Écrire
    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(content)

    return True

print("=" * 70)
print("ADDING MISSING consensus.is.a KEY TO consensus-i18n.js")
print("=" * 70)

if add_missing_key():
    print("\n[OK] Added missing translations")

print("=" * 70)
