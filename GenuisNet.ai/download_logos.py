#!/usr/bin/env python3
"""
Télécharger les logos officiels des outils AI
Utilise les APIs publiques et sources officielles pour récupérer les logos
"""

import os
import requests
import time
from pathlib import Path

# Créer le dossier pour les logos
LOGOS_DIR = 'assets/images/logos'
os.makedirs(LOGOS_DIR, exist_ok=True)

# URLs des logos officiels (utilisant des sources publiques)
# Format: 'tool-slug': 'URL du logo'
LOGO_URLS = {
    # Analytics
    'tableau-pulse': 'https://logo.clearbit.com/tableau.com',
    'thoughtspot': 'https://logo.clearbit.com/thoughtspot.com',
    'power-bi-copilot': 'https://logo.clearbit.com/powerbi.microsoft.com',
    'looker-ai': 'https://logo.clearbit.com/looker.com',
    'domo-ai': 'https://logo.clearbit.com/domo.com',
    'qlik-sense-ai': 'https://logo.clearbit.com/qlik.com',
    'sisense-ai': 'https://logo.clearbit.com/sisense.com',
    'alteryx-ai': 'https://logo.clearbit.com/alteryx.com',
    'yellowfin-ai': 'https://logo.clearbit.com/yellowfinbi.com',
    'microstrategy-ai': 'https://logo.clearbit.com/microstrategy.com',
    'mode-analytics': 'https://logo.clearbit.com/mode.com',
    'datarobot': 'https://logo.clearbit.com/datarobot.com',
    'h2oai': 'https://logo.clearbit.com/h2o.ai',

    # Customer Service
    'intercom-fin': 'https://logo.clearbit.com/intercom.com',
    'zendesk-ai': 'https://logo.clearbit.com/zendesk.com',
    'ada': 'https://logo.clearbit.com/ada.cx',
    'drift': 'https://logo.clearbit.com/drift.com',
    'liveperson': 'https://logo.clearbit.com/liveperson.com',
    'freshdesk-ai': 'https://logo.clearbit.com/freshdesk.com',
    'kustomer': 'https://logo.clearbit.com/kustomer.com',
    'ultimateai': 'https://logo.clearbit.com/ultimate.ai',
    'polyai': 'https://logo.clearbit.com/poly.ai',
    'forethought': 'https://logo.clearbit.com/forethought.ai',
    'helpshift': 'https://logo.clearbit.com/helpshift.com',
    'yellowai': 'https://logo.clearbit.com/yellow.ai',
    'netomi': 'https://logo.clearbit.com/netomi.com',
    'certainly': 'https://logo.clearbit.com/certainly.io',
    'cognigy': 'https://logo.clearbit.com/cognigy.com',

    # Education
    'khan-academy-ai': 'https://logo.clearbit.com/khanacademy.org',
    'duolingo-max': 'https://logo.clearbit.com/duolingo.com',
    'coursera-coach': 'https://logo.clearbit.com/coursera.org',
    'century-tech': 'https://logo.clearbit.com/century.tech',
    'gradescope': 'https://logo.clearbit.com/gradescope.com',
    'quizlet-ai': 'https://logo.clearbit.com/quizlet.com',

    # Gaming
    'inworld-ai': 'https://logo.clearbit.com/inworld.ai',
    'scenario': 'https://logo.clearbit.com/scenario.com',
    'ludoai': 'https://logo.clearbit.com/ludo.ai',
    'replika': 'https://logo.clearbit.com/replika.com',

    # HR
    'paradox-olivia': 'https://logo.clearbit.com/paradox.ai',
    'hirevue': 'https://logo.clearbit.com/hirevue.com',
    'pymetrics': 'https://logo.clearbit.com/pymetrics.ai',
    'eightfold-ai': 'https://logo.clearbit.com/eightfold.ai',
    'beamery': 'https://logo.clearbit.com/beamery.com',
    'phenom': 'https://logo.clearbit.com/phenom.com',
    'harver': 'https://logo.clearbit.com/harver.com',
    'textio': 'https://logo.clearbit.com/textio.com',
    'workable-ai': 'https://logo.clearbit.com/workable.com',

    # Legal
    'harvey-ai': 'https://logo.clearbit.com/harvey.ai',
    'cocounsel': 'https://logo.clearbit.com/casetext.com',
    'lawgeex': 'https://logo.clearbit.com/lawgeex.com',
    'luminance': 'https://logo.clearbit.com/luminance.com',
    'casetext': 'https://logo.clearbit.com/casetext.com',
    'everlaw': 'https://logo.clearbit.com/everlaw.com',

    # Quantum
    'ibm-quantum': 'https://logo.clearbit.com/ibm.com',
    'google-cirq': 'https://logo.clearbit.com/google.com',
    'amazon-braket': 'https://logo.clearbit.com/aws.amazon.com',
    'azure-quantum': 'https://logo.clearbit.com/microsoft.com',
    'd-wave-leap': 'https://logo.clearbit.com/dwavesys.com',
    'rigetti-qcs': 'https://logo.clearbit.com/rigetti.com',
    'ionq': 'https://logo.clearbit.com/ionq.com',

    # Research
    'consensus': 'https://logo.clearbit.com/consensus.app',
    'elicit': 'https://logo.clearbit.com/elicit.com',
    'scite': 'https://logo.clearbit.com/scite.ai',
    'scispace': 'https://logo.clearbit.com/typeset.io',
    'researchrabbit': 'https://logo.clearbit.com/researchrabbit.ai',
    'scholarcy': 'https://logo.clearbit.com/scholarcy.com',
    'litmaps': 'https://logo.clearbit.com/litmaps.com',

    # Sales
    'salesforce-einstein-gpt': 'https://logo.clearbit.com/salesforce.com',
    'hubspot-ai': 'https://logo.clearbit.com/hubspot.com',
    'gong': 'https://logo.clearbit.com/gong.io',
    'outreach': 'https://logo.clearbit.com/outreach.io',
    'apolloio': 'https://logo.clearbit.com/apollo.io',
    'peopleai': 'https://logo.clearbit.com/people.ai',
    'clari': 'https://logo.clearbit.com/clari.com',
    'chorusai': 'https://logo.clearbit.com/chorus.ai',
    'conversica': 'https://logo.clearbit.com/conversica.com',
    '6sense': 'https://logo.clearbit.com/6sense.com',
    'lavender': 'https://logo.clearbit.com/lavender.ai',

    # Translation
    'deepl-pro': 'https://logo.clearbit.com/deepl.com',
    'google-translate-ai': 'https://logo.clearbit.com/translate.google.com',
    'microsoft-translator': 'https://logo.clearbit.com/microsoft.com',
    'phrase': 'https://logo.clearbit.com/phrase.com',
    'smartling': 'https://logo.clearbit.com/smartling.com',
    'lokalise': 'https://logo.clearbit.com/lokalise.com',
    'unbabel': 'https://logo.clearbit.com/unbabel.com',
    'lilt': 'https://logo.clearbit.com/lilt.com',
}

def download_logo(tool_slug, url):
    """Télécharger un logo depuis l'URL"""
    try:
        response = requests.get(url, timeout=10, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

        if response.status_code == 200:
            # Sauvegarder le logo
            logo_path = f'{LOGOS_DIR}/{tool_slug}.png'
            with open(logo_path, 'wb') as f:
                f.write(response.content)
            return True
        else:
            return False

    except Exception as e:
        print(f"      ❌ Erreur: {e}")
        return False

def main():
    print("="*70)
    print("📥 TÉLÉCHARGEMENT DES LOGOS OFFICIELS")
    print("="*70)
    print()
    print(f"📁 Dossier de destination: {LOGOS_DIR}")
    print()

    success_count = 0
    failed_count = 0

    for tool_slug, url in LOGO_URLS.items():
        print(f"⏳ {tool_slug}...", end=" ")

        if download_logo(tool_slug, url):
            print(f"✅")
            success_count += 1
        else:
            print(f"❌")
            failed_count += 1

        # Pause pour éviter de surcharger l'API
        time.sleep(0.5)

    print()
    print("="*70)
    print(f"✅ TÉLÉCHARGEMENT TERMINÉ!")
    print(f"   Succès: {success_count}")
    print(f"   Échecs: {failed_count}")
    print(f"   Total: {success_count + failed_count}")
    print("="*70)

if __name__ == '__main__':
    main()
