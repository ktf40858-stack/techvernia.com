import os
import json
import re

base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
cs_batch_dir = os.path.join(base_dir, "pages", "reviews", "customer-service")
edu_batch_dir = os.path.join(base_dir, "pages", "reviews", "education")
js_dir = os.path.join(base_dir, "js")

# Utiliser Ada comme référence (fichier Customer Service complet)
reference_tool = "ada"

edu_tools = [
    "aleks", "carnegie-learning", "century-tech", "cognii",
    "coursera-coach", "duolingo-max", "gradescope", "khan-academy-ai",
    "knewton-alta", "querium", "quizlet-ai", "socratic-by-google",
    "squirrel-ai", "thinkster-math"
]

# Adaptations à faire pour Education
adaptations = {
    "customer service": "education",
    "customer-service": "education",
    "service al cliente": "educación",
    "servicio al cliente": "educación",
    "atención al cliente": "educación",
    "service client": "éducation",
    "Servizio clienti": "istruzione",
    "Kundenservice": "Bildung",
    "Kundendienst": "Bildung",
    "atendimento ao cliente": "educação",
    "客户服务": "教育",
    "カスタマーサービス": "教育",
    "고객 서비스": "교육",
    "خدمة العملاء": "التعليم",
    "ग्राहक सेवा": "शिक्षा",

    "modern businesses": "modern educational institutions",
    "empresas modernas": "instituciones educativas modernas",
    "entreprises modernes": "établissements éducatifs modernes",
    "moderne Unternehmen": "moderne Bildungseinrichtungen",
    "empresas modernas": "instituições educacionais modernas",
    "现代企业": "现代教育机构",
    "現代の企業": "現代の教育機関",
    "현대 기업": "현대 교육 기관",
    "الشركات الحديثة": "المؤسسات التعليمية الحديثة",
    "आधुनिक व्यवसाय": "आधुनिक शैक्षणिक संस्थान",

    "organizations": "educational institutions",
    "organizaciones": "instituciones educativas",
    "organisations": "établissements éducatifs",
    "Organisationen": "Bildungseinrichtungen",
    "organizações": "instituições educacionais",
    "组织": "教育机构",
    "組織": "教育機関",
    "조직": "교육 기관",
    "المنظمات": "المؤسسات التعليمية",
    "संगठन": "शैक्षणिक संस्थान"
}

def adapt_text(text):
    """Adapte un texte de Customer Service pour Education"""
    adapted = text
    for old, new in adaptations.items():
        # Remplacement case-insensitive mais préservant la casse du remplacement
        adapted = re.sub(re.escape(old), new, adapted, flags=re.IGNORECASE)
    return adapted

def load_reference_translations():
    """Charge toutes les traductions de référence depuis Ada (Customer Service)"""
    all_translations = {}
    languages = ["de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]

    for batch_num in range(1, 4):
        batch_file = os.path.join(cs_batch_dir, f"{reference_tool}-batch{batch_num}.json")
        if os.path.exists(batch_file):
            with open(batch_file, 'r', encoding='utf-8') as f:
                batch_data = json.load(f)
                for lang in languages:
                    if lang not in all_translations:
                        all_translations[lang] = {}
                    if lang in batch_data:
                        all_translations[lang].update(batch_data[lang])

    return all_translations

def tool_to_camel(tool):
    parts = tool.split('-')
    return parts[0] + ''.join(p.capitalize() for p in parts[1:])

def tool_to_title(tool):
    return ' '.join(p.capitalize() for p in tool.split('-'))

def update_education_tool(edu_tool, reference_translations):
    """Met à jour un outil Education avec les traductions adaptées"""
    js_file = os.path.join(js_dir, f"{edu_tool}-i18n.js")

    if not os.path.exists(js_file):
        return

    # Lire le fichier i18n actuel
    with open(js_file, 'r', encoding='utf-8') as f:
        content = f.read()

    edu_tool_display = tool_to_title(edu_tool)
    ada_display = "Ada"

    # Pour chaque langue
    languages = ["de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]

    for lang in languages:
        if lang not in reference_translations:
            continue

        # Pour chaque clé de référence
        for ada_key, ada_value in reference_translations[lang].items():
            # Convertir la clé Ada en clé pour l'outil Education
            # review.ada.xxx -> review.edu-tool.xxx
            edu_key = ada_key.replace("review.ada.", f"review.{edu_tool}.")

            # Adapter le texte pour Education
            adapted_value = adapt_text(ada_value)
            # Remplacer Ada par le nom de l'outil Education
            adapted_value = adapted_value.replace(ada_display, edu_tool_display)

            # Trouver et remplacer dans le contenu
            # Chercher la clé existante (qui peut avoir du texte anglais)
            pattern = rf'"{re.escape(edu_key)}":\s*"[^"]*"'

            def replacer(match):
                return f'"{edu_key}": "{adapted_value}"'

            content = re.sub(pattern, replacer, content)

    # Sauvegarder
    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  [OK] {edu_tool} updated with adapted translations")

# MAIN EXECUTION
print("=" * 70)
print("ADAPTING CUSTOMER SERVICE TRANSLATIONS FOR EDUCATION TOOLS")
print("=" * 70)

print(f"\n[1/2] Loading reference translations from {reference_tool}...")
reference_translations = load_reference_translations()
print(f"  [OK] Loaded {sum(len(v) for v in reference_translations.values())} translations")

print(f"\n[2/2] Updating Education tools...")
for edu_tool in edu_tools:
    update_education_tool(edu_tool, reference_translations)

print("\n" + "=" * 70)
print("[COMPLETE] All Education tools updated with professional translations!")
print("=" * 70)
