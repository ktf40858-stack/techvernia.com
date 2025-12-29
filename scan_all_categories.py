#!/usr/bin/env python3
import sys, io, os, glob

if sys.platform=='win32':
    sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

categories = [
    'analytics', 'architecture', 'audio', 'business', 'chatbots', 'coding',
    'customer-service', 'cybersecurity', 'education', 'gaming', 'hr', 'image',
    'legal', 'medical', 'networking', 'productivity', 'quantum', 'research',
    'sales', 'seo', 'translation', 'video', 'writing'
]

print("📊 SCAN COMPLET DE TOUTES LES CATÉGORIES")
print("=" * 100)

total_tools = 0
categories_data = []

for category in categories:
    html_files = glob.glob(f'GenuisNet.ai/pages/reviews/{category}/*.html')
    js_files = glob.glob(f'GenuisNet.ai/js/*-i18n.js')

    # Compter combien d'outils ont des fichiers i18n
    tools_with_i18n = 0
    for html_file in html_files:
        tool_name = os.path.basename(html_file).replace('.html', '')
        i18n_file = f'GenuisNet.ai/js/{tool_name}-i18n.js'
        if os.path.exists(i18n_file):
            # Vérifier s'il a le code d'application
            with open(i18n_file, 'r', encoding='utf-8') as f:
                content = f.read()
                if 'function apply' in content and 'languageChanged' in content:
                    tools_with_i18n += 1

    count = len(html_files)
    total_tools += count

    categories_data.append({
        'name': category,
        'count': count,
        'with_i18n': tools_with_i18n
    })

# Afficher par ordre de nombre d'outils
categories_data.sort(key=lambda x: x['count'], reverse=True)

print(f"{'Catégorie':<20} {'Outils':<10} {'i18n Complets':<15} {'Statut'}")
print("-" * 100)

for cat_data in categories_data:
    name = cat_data['name']
    count = cat_data['count']
    with_i18n = cat_data['with_i18n']

    if with_i18n == count:
        status = "✅ 100%"
    elif with_i18n > 0:
        percent = int(100 * with_i18n / count)
        status = f"⚠️  {percent}%"
    else:
        status = "❌ 0%"

    print(f"{name:<20} {count:<10} {with_i18n}/{count:<12} {status}")

print("-" * 100)
print(f"{'TOTAL:':<20} {total_tools:<10}")
print()

# Compter combien il faut faire
hr_done = next((c for c in categories_data if c['name'] == 'hr'), {})
if hr_done:
    print(f"✅ HR: {hr_done['count']} outils complétés")

remaining = sum(c['count'] - c['with_i18n'] for c in categories_data if c['name'] != 'hr')
print(f"📋 Restant: {remaining} outils à traiter")
print(f"📦 Total avec HR: {total_tools} outils")
