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

def fix_i18n_keys(tool_key, tool_name):
    """Corrige les clés mal formées dans le fichier i18n.js"""
    js_file = os.path.join(js_dir, f"{tool_key}-i18n.js")

    with open(js_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remplacements de clés spécifiques
    replacements = {
        # Ces clés contiennent encore "salesforce.einstein.gpt" au lieu du nom de l'outil
        f'"review.{tool_key}.salesforce.einstein.gpt.is.a"': f'"review.{tool_key}.{tool_key}.is.a.powerful.feature-rich"',
        f'"review.{tool_key}.salesforce.einstein.gpt.offers.flexible"': f'"review.{tool_key}.{tool_key}.offers.flexible.pricing.plans"',
        f'"review.{tool_key}.salesforce.einstein.gpt.excels.for"': f'"review.{tool_key}.{tool_key}.excels.for"',
        f'"review.{tool_key}.salesforce.einstein.gpt.vs.competitors"': f'"review.{tool_key}.{tool_key}.vs.competitors"',
        f'"review.{tool_key}.salesforce.einstein.gpt.integrates.with"': f'"review.{tool_key}.{tool_key}.integrates.with.100.popular"',
        f'"review.{tool_key}.faq.is.salesforce.einstein.gpt.worth.the.investment"': f'"review.{tool_key}.faq.is.{tool_key}.worth.the.investment"',
        f'"review.{tool_key}.faq.does.salesforce.einstein.gpt.offer.a.free.trial"': f'"review.{tool_key}.faq.does.{tool_key}.offer.a.free.trial"',

        # Clés manquantes dans le HTML
        f'"review.{tool_key}.explore.salesforce.einstein.gpts.interface"': f'"review.{tool_key}.explore.{tool_key}s.interface"',
        f'"review.{tool_key}.yes.salesforce.einstein.gpt.uses"': f'"review.{tool_key}.yes.{tool_key}.uses.bank-grade.encryption"',
        f'"review.{tool_key}.absolutely.salesforce.einstein.gpt.provides"': f'"review.{tool_key}.absolutely.{tool_key}.provides.migration.tools"',

        # Ajouter les clés manquantes spécifiques
        f'"review.{tool_key}.consensus.is.a.leading.ai-powered"': f'"review.{tool_key}.{tool_key}.is.a.leading.ai-powered"',
        f'"review.{tool_key}.consensus.offers.flexible.pricing.plans"': f'"review.{tool_key}.{tool_key}.offers.flexible.pricing.plans"',
        f'"review.{tool_key}.consensus.excels.for"': f'"review.{tool_key}.{tool_key}.excels.for"',
        f'"review.{tool_key}.consensus.vs.competitors"': f'"review.{tool_key}.{tool_key}.vs.competitors"',
        f'"review.{tool_key}.consensus.integrates.with.100.popular"': f'"review.{tool_key}.{tool_key}.integrates.with.100.popular"',
        f'"review.{tool_key}.yes.consensus.uses.bank-grade.encryption"': f'"review.{tool_key}.yes.{tool_key}.uses.bank-grade.encryption"',
        f'"review.{tool_key}.absolutely.consensus.provides.migration.tools"': f'"review.{tool_key}.absolutely.{tool_key}.provides.migration.tools"',
        f'"review.{tool_key}.consensus.is.a.powerful.feature-rich"': f'"review.{tool_key}.{tool_key}.is.a.powerful.feature-rich"',
        f'"review.{tool_key}.try.consensus.today.and.experience"': f'"review.{tool_key}.try.{tool_key}.today.and.experience"',
        f'"review.{tool_key}.try.consensus.free"': f'"review.{tool_key}.try.{tool_key}.free"',
        f'"review.{tool_key}.explore.consensuss.interface"': f'"review.{tool_key}.explore.{tool_key}s.interface"',
    }

    # Appliquer les remplacements
    for old_key, new_key in replacements.items():
        content = content.replace(old_key, new_key)

    # Écrire le fichier corrigé
    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(content)

    return True

print("=" * 70)
print("FIXING RESEARCH I18N KEYS TO MATCH HTML")
print("=" * 70)

count = 0
for tool_key, tool_name in research_tools.items():
    if fix_i18n_keys(tool_key, tool_name):
        print(f"{tool_name}: [OK] Fixed keys")
        count += 1
    else:
        print(f"{tool_name}: [ERROR] Failed")

print("\n" + "=" * 70)
print(f"[COMPLETE] Fixed keys in {count}/{len(research_tools)} tools")
print("=" * 70)
