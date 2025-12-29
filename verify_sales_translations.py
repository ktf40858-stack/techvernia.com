import os
import json
import re

base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
js_dir = os.path.join(base_dir, "js")

tools = [
    "6sense",
    "apolloio",
    "attention",
    "chorusai",
    "clari",
    "conversica",
    "exceedai",
    "gong",
    "hubspot-ai",
    "insidesales",
    "lavender",
    "outreach",
    "peopleai",
    "regieai",
    "salesforce-einstein-gpt",
    "troopsai"
]

def load_i18n_stats(js_file):
    """Charge les statistiques d'un fichier i18n"""
    with open(js_file, 'r', encoding='utf-8') as f:
        content = f.read()

    stats = {}
    languages = ["en", "de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]

    for lang in languages:
        pattern = rf'"{lang}":\s*(\{{[^}}]+(?:\{{[^}}]*\}}[^}}]*)*\}})'
        match = re.search(pattern, content, re.DOTALL)

        if match:
            key_pattern = r'"([^"]+)":'
            matches = re.findall(key_pattern, match.group(1))
            stats[lang] = len(matches)
        else:
            stats[lang] = 0

    return stats

# MAIN
print("=" * 80)
print(" " * 20 + "AI SALES & CRM I18N COMPLETION REPORT")
print("=" * 80)

print("\n" + "-" * 80)
print(f"{'Tool':<30} {'EN':<6} {'DE':<6} {'ES':<6} {'FR':<6} {'PT':<6} {'ZH':<6} {'JA':<6} {'KO':<6} {'AR':<6} {'HI':<6}")
print("-" * 80)

total_stats = {lang: 0 for lang in ["en", "de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]}

for tool in tools:
    js_file = os.path.join(js_dir, f"{tool}-i18n.js")

    if os.path.exists(js_file):
        stats = load_i18n_stats(js_file)

        # Afficher les stats
        print(f"{tool:<30} {stats['en']:<6} {stats['de']:<6} {stats['es']:<6} {stats['fr']:<6} {stats['pt']:<6} {stats['zh']:<6} {stats['ja']:<6} {stats['ko']:<6} {stats['ar']:<6} {stats['hi']:<6}")

        # Ajouter au total
        for lang, count in stats.items():
            total_stats[lang] += count
    else:
        print(f"{tool:<30} FILE NOT FOUND")

print("-" * 80)
print(f"{'TOTAL':<30} {total_stats['en']:<6} {total_stats['de']:<6} {total_stats['es']:<6} {total_stats['fr']:<6} {total_stats['pt']:<6} {total_stats['zh']:<6} {total_stats['ja']:<6} {total_stats['ko']:<6} {total_stats['ar']:<6} {total_stats['hi']:<6}")
print("=" * 80)

# Calculer le pourcentage de complétion
if total_stats['en'] > 0:
    for lang in ["de", "es", "fr", "pt", "zh", "ja", "ko", "ar", "hi"]:
        percentage = (total_stats[lang] / total_stats['en']) * 100
        print(f"{lang.upper()}: {percentage:.1f}% complete")

print("\n" + "=" * 80)
print(" " * 25 + "SUMMARY")
print("=" * 80)
print(f"Total AI Sales & CRM Tools: {len(tools)}")
print(f"Total English Keys: {total_stats['en']}")
print(f"Total Translations per Language: ~{total_stats['de']} (avg)")
print(f"Total Translations Across All Languages: {sum(total_stats.values())}")
print(f"Languages Supported: 10 (EN, DE, ES, FR, PT, ZH, JA, KO, AR, HI)")
print("=" * 80)
