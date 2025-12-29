#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vérifie l'état des attributs i18n et scripts dans les HTML cybersecurity
"""

import os
import re

CYBER_DIR = "GenuisNet.ai/pages/reviews/cybersecurity"

# Tous les outils avec i18n généré
TOOLS_WITH_I18N = [
    'cisco-securex', 'cortex-xdr', 'crowdstrike', 'cyberark', 'darktrace',
    'fortinet', 'ibm-qradar', 'microsoft-sentinel', 'palo-alto-ngfw',
    'qualys', 'rapid7', 'sentinelone', 'sophos-interceptx', 'splunk-security',
    'tenable', 'trend-micro-vision-one', 'abnormal-security', 'carbon-black',
    'cylance', 'exabeam', 'lacework', 'mcafee-mvision', 'recorded-future',
    'symantec-endpoint', 'vectra-ai', 'wiz', 'zerofox'
]

def check_html_i18n(tool):
    """Vérifie l'état i18n d'un fichier HTML"""
    html_file = os.path.join(CYBER_DIR, f'{tool}.html')

    if not os.path.exists(html_file):
        return {'exists': False}

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Vérifier la présence du script i18n
    has_tool_script = f'{tool}-i18n.js' in content
    has_main_i18n = 'i18n.js' in content

    # Compter les attributs data-i18n
    data_i18n_count = len(re.findall(r'data-i18n=', content))

    # Vérifier le sélecteur de langue
    has_lang_selector = 'language-selector' in content or 'languageSelector' in content

    return {
        'exists': True,
        'has_tool_script': has_tool_script,
        'has_main_i18n': has_main_i18n,
        'data_i18n_count': data_i18n_count,
        'has_lang_selector': has_lang_selector
    }

def main():
    print("=" * 80)
    print("VERIFICATION I18N DANS LES FICHIERS HTML")
    print("=" * 80)

    complete = []
    missing_scripts = []
    missing_attributes = []
    missing_file = []

    for tool in TOOLS_WITH_I18N:
        status = check_html_i18n(tool)

        if not status['exists']:
            missing_file.append(tool)
            continue

        if status['has_tool_script'] and status['has_main_i18n'] and status['data_i18n_count'] > 30:
            complete.append({'tool': tool, **status})
        elif not status['has_tool_script'] or not status['has_main_i18n']:
            missing_scripts.append({'tool': tool, **status})
        elif status['data_i18n_count'] < 30:
            missing_attributes.append({'tool': tool, **status})

    print(f"\n[OK] COMPLET - Script + Attributs ({len(complete)}):")
    for item in complete:
        selector = "✓" if item['has_lang_selector'] else "✗"
        print(f"  {item['tool']:30s} | {item['data_i18n_count']:3d} attributs | Selector: {selector}")

    print(f"\n[SCRIPTS] Scripts manquants ({len(missing_scripts)}):")
    for item in missing_scripts:
        tool_scr = "✓" if item['has_tool_script'] else "✗"
        main_scr = "✓" if item['has_main_i18n'] else "✗"
        print(f"  {item['tool']:30s} | Tool: {tool_scr} | Main: {main_scr} | {item['data_i18n_count']} attributs")

    print(f"\n[ATTR] Attributs data-i18n manquants ({len(missing_attributes)}):")
    for item in missing_attributes:
        print(f"  {item['tool']:30s} | Seulement {item['data_i18n_count']} attributs")

    if missing_file:
        print(f"\n[FILE] Fichiers HTML manquants ({len(missing_file)}):")
        for tool in missing_file:
            print(f"  {tool}")

    print(f"\n" + "=" * 80)
    print(f"RESUME:")
    print(f"  Complets: {len(complete)}/{len(TOOLS_WITH_I18N)}")
    print(f"  Scripts manquants: {len(missing_scripts)}")
    print(f"  Attributs manquants: {len(missing_attributes)}")
    print(f"  HTML manquants: {len(missing_file)}")
    print("=" * 80)

if __name__ == "__main__":
    main()
