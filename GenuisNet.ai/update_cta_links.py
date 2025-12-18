#!/usr/bin/env python3
"""
Mettre à jour les liens CTA "Try for Free" avec les vraies URLs des outils AI
"""

import os
import re
from bs4 import BeautifulSoup

# URLs réelles des outils AI par catégorie
TOOL_URLS = {
    'analytics': {
        'tableau-pulse': 'https://www.tableau.com/products/pulse',
        'thoughtspot': 'https://www.thoughtspot.com/trial',
        'power-bi-copilot': 'https://powerbi.microsoft.com/try',
        'looker-ai': 'https://cloud.google.com/looker/docs/ai',
        'domo-ai': 'https://www.domo.com/trial',
        'qlik-sense-ai': 'https://www.qlik.com/us/trial/qlik-sense',
        'sisense-ai': 'https://www.sisense.com/get-sisense/',
        'alteryx-ai': 'https://www.alteryx.com/trial',
        'yellowfin-ai': 'https://www.yellowfinbi.com/trial',
        'microstrategy-ai': 'https://www.microstrategy.com/en/trial',
        'mode-analytics': 'https://mode.com/get-started/',
        'datarobot': 'https://www.datarobot.com/trial/',
        'h2oai': 'https://h2o.ai/platform/ai-cloud/make/',
        'prophet-meta': 'https://facebook.github.io/prophet/',
        'amazon-quicksight-q': 'https://aws.amazon.com/quicksight/q/'
    },
    'customer-service': {
        'intercom-fin': 'https://www.intercom.com/fin',
        'zendesk-ai': 'https://www.zendesk.com/register/',
        'ada': 'https://www.ada.cx/request-demo',
        'drift': 'https://www.drift.com/get-started/',
        'liveperson': 'https://www.liveperson.com/trial/',
        'freshdesk-ai': 'https://freshdesk.com/signup',
        'kustomer': 'https://www.kustomer.com/demo/',
        'ultimateai': 'https://www.ultimate.ai/demo',
        'polyai': 'https://poly.ai/request-demo/',
        'forethought': 'https://forethought.ai/demo',
        'helpshift': 'https://www.helpshift.com/request-demo/',
        'yellowai': 'https://yellow.ai/request-demo/',
        'netomi': 'https://www.netomi.com/request-demo',
        'certainly': 'https://certainly.io/book-demo/',
        'cognigy': 'https://www.cognigy.com/trial'
    },
    'education': {
        'khan-academy-ai': 'https://www.khanacademy.org/khan-labs',
        'duolingo-max': 'https://www.duolingo.com/max',
        'coursera-coach': 'https://www.coursera.org/',
        'century-tech': 'https://www.century.tech/request-demo/',
        'squirrel-ai': 'https://squirrelai.com/',
        'carnegie-learning': 'https://www.carnegielearning.com/request-demo/',
        'gradescope': 'https://www.gradescope.com/',
        'socratic-by-google': 'https://socratic.org/',
        'quizlet-ai': 'https://quizlet.com/labs/qchat',
        'cognii': 'https://www.cognii.com/request-demo/',
        'thinkster-math': 'https://hellothinkster.com/signup',
        'aleks': 'https://www.aleks.com/',
        'knewton-alta': 'https://www.knewton.com/alta/',
        'querium': 'https://www.querium.com/'
    },
    'gaming': {
        'inworld-ai': 'https://www.inworld.ai/get-started',
        'scenario': 'https://www.scenario.com/',
        'ludoai': 'https://ludo.ai/',
        'latitude-ai-dungeon': 'https://play.aidungeon.com/',
        'promethean-ai': 'https://www.prometheanai.com/',
        'rosebud-ai': 'https://www.rosebud.ai/',
        'hidden-door': 'https://www.hiddendoor.co/',
        'charismaai': 'https://charisma.ai/',
        'rct-ai': 'https://www.rct.ai/',
        'artomatix': 'https://www.artomatix.com/',
        'replika': 'https://replika.com/'
    },
    'hr': {
        'paradox-olivia': 'https://www.paradox.ai/request-demo',
        'hirevue': 'https://www.hirevue.com/request-demo',
        'pymetrics': 'https://www.pymetrics.ai/request-demo/',
        'eightfold-ai': 'https://eightfold.ai/request-demo/',
        'beamery': 'https://beamery.com/request-demo/',
        'phenom': 'https://www.phenom.com/demo',
        'seekout': 'https://seekout.com/request-demo/',
        'harver': 'https://harver.com/request-demo/',
        'textio': 'https://textio.com/products/hire',
        'fetcher': 'https://fetcher.ai/demo/',
        'humanly': 'https://humanly.io/demo',
        'sense': 'https://www.sense.com/request-demo',
        'findem': 'https://www.findem.ai/demo/',
        'workable-ai': 'https://www.workable.com/signup'
    },
    'legal': {
        'harvey-ai': 'https://www.harvey.ai/contact',
        'cocounsel': 'https://casetext.com/cocounsel',
        'lawgeex': 'https://www.lawgeex.com/demo/',
        'luminance': 'https://www.luminance.com/request-demo.html',
        'kira-systems': 'https://kirasystems.com/request-demo/',
        'ross-intelligence': 'https://www.rossintelligence.com/',
        'casetext': 'https://casetext.com/sign-up',
        'lex-machina': 'https://lexmachina.com/request-demo/',
        'blue-j-legal': 'https://www.bluejlegal.com/request-demo/',
        'everlaw': 'https://www.everlaw.com/request-a-demo/',
        'primer': 'https://primer.ai/contact/',
        'ravel-law': 'https://www.ravellaw.com/'
    },
    'quantum': {
        'ibm-quantum': 'https://quantum-computing.ibm.com/',
        'google-cirq': 'https://quantumai.google/cirq',
        'amazon-braket': 'https://aws.amazon.com/braket/',
        'azure-quantum': 'https://azure.microsoft.com/en-us/products/quantum',
        'd-wave-leap': 'https://cloud.dwavesys.com/leap/signup/',
        'rigetti-qcs': 'https://www.rigetti.com/get-started',
        'xanadu-pennylane': 'https://pennylane.ai/',
        'ionq': 'https://ionq.com/get-started'
    },
    'research': {
        'consensus': 'https://consensus.app/',
        'elicit': 'https://elicit.com/',
        'scite': 'https://scite.ai/',
        'scispace': 'https://typeset.io/',
        'researchrabbit': 'https://www.researchrabbit.ai/',
        'semantic-scholar': 'https://www.semanticscholar.org/',
        'irisai': 'https://iris.ai/',
        'scholarcy': 'https://www.scholarcy.com/',
        'litmaps': 'https://www.litmaps.com/',
        'connected-papers': 'https://www.connectedpapers.com/',
        'perplexity-research': 'https://www.perplexity.ai/',
        'undermind': 'https://www.undermind.ai/'
    },
    'sales': {
        'salesforce-einstein-gpt': 'https://www.salesforce.com/form/einstein/gpt/',
        'hubspot-ai': 'https://www.hubspot.com/products/artificial-intelligence',
        'gong': 'https://www.gong.io/demo/',
        'outreach': 'https://www.outreach.io/demo',
        'apolloio': 'https://www.apollo.io/',
        'peopleai': 'https://people.ai/request-demo/',
        'clari': 'https://www.clari.com/demo/',
        'chorusai': 'https://www.chorus.ai/demo',
        'conversica': 'https://www.conversica.com/demo/',
        'exceedai': 'https://exceed.ai/request-demo/',
        '6sense': 'https://6sense.com/request-a-demo/',
        'insidesales': 'https://www.insidesales.com/demo/',
        'troopsai': 'https://troops.ai/demo',
        'attention': 'https://www.attention.tech/',
        'lavender': 'https://www.lavender.ai/',
        'regieai': 'https://www.regie.ai/demo'
    },
    'translation': {
        'deepl-pro': 'https://www.deepl.com/pro',
        'google-translate-ai': 'https://cloud.google.com/translate',
        'microsoft-translator': 'https://azure.microsoft.com/en-us/products/ai-services/ai-translator',
        'phrase': 'https://phrase.com/demo/',
        'smartling': 'https://www.smartling.com/demo/',
        'lokalise': 'https://lokalise.com/signup',
        'systran': 'https://www.systransoft.com/trial/',
        'unbabel': 'https://unbabel.com/request-demo/',
        'lilt': 'https://lilt.com/demo',
        'modernmt': 'https://www.modernmt.com/trial/'
    }
}

def update_cta_link(file_path, category, tool_slug):
    """Mettre à jour le lien CTA avec l'URL réelle"""

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Obtenir l'URL de l'outil
        tool_url = TOOL_URLS.get(category, {}).get(tool_slug, '#')

        if tool_url == '#':
            print(f"      ⚠️  URL non trouvée pour {tool_slug}")
            return False

        # Remplacer le lien # par l'URL réelle dans le CTA
        # Chercher: <a class="btn btn-white" href="#"
        # Remplacer par: <a class="btn btn-white" href="URL réelle"

        soup = BeautifulSoup(content, 'html.parser')

        # Trouver le bouton CTA principal dans la section cta-top-section
        cta_section = soup.find('div', class_='cta-top-section')
        if cta_section:
            # Trouver le premier bouton (Try for Free)
            btn_white = cta_section.find('a', class_='btn-white')
            if btn_white:
                btn_white['href'] = tool_url
                btn_white['target'] = '_blank'
                btn_white['rel'] = 'noopener noreferrer'

        # Sauvegarder
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))

        return True

    except Exception as e:
        print(f"      ❌ Erreur: {e}")
        return False

def update_all_cta_links():
    """Mettre à jour tous les liens CTA"""

    print("="*70)
    print("🔗 MISE À JOUR DES LIENS CTA VERS LES PAGES D'ESSAI")
    print("="*70)
    print()

    total_updated = 0

    for category, tools in TOOL_URLS.items():
        print(f"\n📁 {category.upper()}")

        category_dir = f'pages/reviews/{category}'

        if not os.path.exists(category_dir):
            print(f"   ⚠️  Dossier non trouvé: {category_dir}")
            continue

        for tool_slug, url in tools.items():
            file_path = f'{category_dir}/{tool_slug}.html'

            if not os.path.exists(file_path):
                print(f"   ⚠️  Fichier non trouvé: {tool_slug}.html")
                continue

            if update_cta_link(file_path, category, tool_slug):
                print(f"   ✅ {tool_slug}.html → {url}")
                total_updated += 1

    print()
    print("="*70)
    print(f"✅ LIENS MIS À JOUR!")
    print(f"   Pages mises à jour: {total_updated}")
    print("="*70)

if __name__ == '__main__':
    update_all_cta_links()
