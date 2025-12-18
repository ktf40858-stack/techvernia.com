#!/usr/bin/env python3
"""
1. Supprime les doublons (garde les full reviews, supprime les cartes simples)
2. Télécharge les logos réels pour chaque AI
3. Implémente les logos dans le HTML
"""

from pathlib import Path
import re
import requests
from urllib.parse import quote
import time

# Mapping des noms d'AI vers leurs URLs de logo officiels
LOGO_URLS = {
    # AI Chatbots
    'Gemini': 'https://www.gstatic.com/lamda/images/gemini_sparkle_v002_d4735304ff6292a690345.svg',
    'Microsoft Copilot': 'https://www.microsoft.com/en-us/microsoft-365/blog/wp-content/uploads/sites/2/2023/03/Copilot_Icon.png',
    'Perplexity AI': 'https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/perplexity-ai-icon.png',
    'Poe': 'https://psc2.cf2.poecdn.net/favicon.svg',
    'Character.AI': 'https://characterai.io/favicon.svg',
    'Pi': 'https://pi.ai/assets/img/brand/pi-logo.svg',
    'HuggingChat': 'https://huggingface.co/front/assets/huggingface_logo.svg',
    'YouChat': 'https://you.com/favicon.ico',
    'Mistral Chat': 'https://mistral.ai/images/logo_hubc88c4ece131b91c7cb753f40e9e1cc5_2589_256x0_resize_q97_h2_lanczos_3.webp',
    'DeepSeek': 'https://chat.deepseek.com/favicon.ico',
    'Grok': 'https://grok.x.ai/favicon.ico',
    'Cohere': 'https://cohere.com/favicon.ico',

    # AI Writing
    'Jasper': 'https://www.jasper.ai/favicon.ico',
    'Copy.ai': 'https://www.copy.ai/favicon.ico',
    'Writesonic': 'https://writesonic.com/favicon.ico',
    'Rytr': 'https://rytr.me/favicon.ico',
    'Grammarly': 'https://static.grammarly.com/assets/files/63da64a39c408c019e296df7f0f18977/grammarly-favicon.svg',
    'QuillBot': 'https://quillbot.com/favicon.ico',
    'Wordtune': 'https://www.wordtune.com/favicon.ico',
    'Sudowrite': 'https://www.sudowrite.com/favicon.ico',
    'ProWritingAid': 'https://prowritingaid.com/favicon.ico',
    'Notion AI': 'https://www.notion.so/images/favicon.ico',
    'Scalenut': 'https://www.scalenut.com/favicon.ico',
    'Frase': 'https://www.frase.io/wp-content/uploads/2021/04/frase-favicon.png',

    # AI Coding
    'GitHub Copilot': 'https://github.githubassets.com/assets/copilot-128x128-1.png',
    'Cursor': 'https://www.cursor.so/favicon.ico',
    'Tabnine': 'https://www.tabnine.com/favicon.ico',
    'Codeium': 'https://codeium.com/favicon.ico',
    'Amazon CodeWhisperer': 'https://d1.awsstatic.com/logos/aws-logo-lockups/poweredbyaws/PB_AWS_logo_RGB_REV_SQ.8c88ac215fe4e441dc42865dd6962ed4f444a90d.png',
    'Replit AI': 'https://replit.com/public/images/favicon.ico',
    'Sourcegraph Cody': 'https://sourcegraph.com/.assets/img/sourcegraph-mark.svg',
    'AskCodi': 'https://www.askcodi.com/favicon.ico',
    'Blackbox AI': 'https://www.blackbox.ai/favicon.ico',
    'Phind': 'https://www.phind.com/images/favicon.png',
    'Bito AI': 'https://bito.ai/wp-content/uploads/2023/03/bito-favicon.png',
    'AlphaCode': 'https://storage.googleapis.com/deepmind-media/research/alphacode/AlphaCode-logo.svg',

    # AI Image
    'Midjourney': 'https://cdn.midjourney.com/favicon.ico',
    'DALL-E 3': 'https://openai.com/favicon.ico',
    'Stable Diffusion': 'https://stability.ai/favicon.ico',
    'Leonardo.ai': 'https://leonardo.ai/favicon.ico',
    'Ideogram': 'https://ideogram.ai/favicon.ico',
    'Adobe Firefly': 'https://www.adobe.com/favicon.ico',
    'Canva AI': 'https://static.canva.com/web/images/8439b51bb7a19f6e65ce1064bc37c197.svg',
    'Runway ML': 'https://runwayml.com/favicon.ico',
    'DreamStudio': 'https://dreamstudio.ai/favicon.ico',
    'Playground AI': 'https://playground.com/favicon.ico',
    'NightCafe': 'https://creator.nightcafe.studio/favicon.ico',
    'Artbreeder': 'https://www.artbreeder.com/favicon.ico',

    # AI Video
    'Runway Gen-2': 'https://runwayml.com/favicon.ico',
    'Pika Labs': 'https://pika.art/favicon.ico',
    'Synthesia': 'https://www.synthesia.io/favicon.ico',
    'HeyGen': 'https://www.heygen.com/favicon.ico',
    'D-ID': 'https://www.d-id.com/favicon.ico',
    'Descript': 'https://www.descript.com/favicon.ico',
    'Pictory': 'https://pictory.ai/favicon.ico',
    'InVideo AI': 'https://invideo.io/favicon.ico',
    'Fliki': 'https://fliki.ai/favicon.ico',
    'Lumen5': 'https://lumen5.com/favicon.ico',
    'OpusClip': 'https://www.opus.pro/favicon.ico',
    'CapCut': 'https://www.capcut.com/favicon.ico',

    # AI Audio
    'ElevenLabs': 'https://elevenlabs.io/favicon.ico',
    'Murf AI': 'https://murf.ai/favicon.ico',
    'Play.ht': 'https://play.ht/favicon.ico',
    'Speechify': 'https://speechify.com/favicon.ico',
    'Descript Overdub': 'https://www.descript.com/favicon.ico',
    'Resemble AI': 'https://www.resemble.ai/favicon.ico',
    'WellSaid Labs': 'https://wellsaidlabs.com/favicon.ico',
    'LOVO': 'https://lovo.ai/favicon.ico',
    'Krisp': 'https://krisp.ai/favicon.ico',
    'Otter.ai': 'https://otter.ai/favicon.ico',
    'AssemblyAI': 'https://www.assemblyai.com/favicon.ico',
    'Suno AI': 'https://suno.ai/favicon.ico',

    # AI Productivity
    'Motion': 'https://www.usemotion.com/favicon.ico',
    'Reclaim AI': 'https://reclaim.ai/favicon.ico',
    'ClickUp AI': 'https://clickup.com/favicon.ico',
    'Mem': 'https://get.mem.ai/favicon.ico',
    'Fireflies.ai': 'https://fireflies.ai/favicon.ico',
    'Tactiq': 'https://tactiq.io/favicon.ico',
    'Clockwise': 'https://www.getclockwise.com/favicon.ico',
    'Sunsama': 'https://www.sunsama.com/favicon.ico',
    'Taskade': 'https://www.taskade.com/favicon.ico',
    'Superhuman': 'https://superhuman.com/favicon.ico',
    'SaneBox': 'https://www.sanebox.com/favicon.ico',

    # AI SEO
    'Surfer SEO': 'https://surferseo.com/favicon.ico',
    'Clearscope': 'https://www.clearscope.io/favicon.ico',
    'MarketMuse': 'https://www.marketmuse.com/favicon.ico',
    'NeuronWriter': 'https://www.neuronwriter.com/favicon.ico',
    'LongShot AI': 'https://www.longshot.ai/favicon.ico',
    'GrowthBar': 'https://www.growthbarseo.com/favicon.ico',
    'INK': 'https://inkforall.com/favicon.ico',
    'SEO.ai': 'https://seo.ai/favicon.ico',
    'RankIQ': 'https://www.rankiq.com/favicon.ico',
    'WordLift': 'https://wordlift.io/favicon.ico',

    # AI Business
    'Salesforce Einstein': 'https://www.salesforce.com/etc/designs/sfdc-www/images/favicon.ico',
    'HubSpot AI': 'https://www.hubspot.com/favicon.ico',
    'Zoho Zia': 'https://www.zoho.com/favicon.ico',
    'IBM Watson': 'https://www.ibm.com/favicon.ico',
    'Tableau AI': 'https://www.tableau.com/favicon.ico',
    'Power BI AI': 'https://powerbi.microsoft.com/pictures/application-logos/svg/powerbi.svg',
    'DataRobot': 'https://www.datarobot.com/favicon.ico',
    'H2O.ai': 'https://h2o.ai/favicon.ico',
    'UiPath': 'https://www.uipath.com/hs-fs/hubfs/favicon.png',
    'ThoughtSpot': 'https://www.thoughtspot.com/favicon.ico',
    'Workday AI': 'https://www.workday.com/content/dam/web/images/icons/wd-favicon.ico',
    'ServiceNow AI': 'https://www.servicenow.com/etc/designs/servicenow/favicon.ico',

    # AI Networking
    'Cisco DNA Center': 'https://www.cisco.com/favicon.ico',
    'Juniper Mist AI': 'https://www.juniper.net/etc/designs/juniper/favicon.ico',
    'Aruba AI': 'https://www.arubanetworks.com/favicon.ico',
    'Fortinet FortiAI': 'https://www.fortinet.com/etc/designs/fortinet/favicon.ico',
    'Dynatrace': 'https://www.dynatrace.com/favicon.ico',
    'Datadog': 'https://static.datadoghq.com/static/images/logos/dogshell_av.png',
    'Splunk': 'https://www.splunk.com/content/dam/splunk2/images/icons/favicons/favicon.ico',
    'New Relic AI': 'https://newrelic.com/favicon.ico',
    'ThousandEyes': 'https://www.thousandeyes.com/favicon.ico',
    'NetBrain': 'https://www.netbraintech.com/favicon.ico',
    'SolarWinds AI': 'https://www.solarwinds.com/favicon.ico',
    'Auvik': 'https://www.auvik.com/wp-content/themes/auvik2018/assets/img/favicons/favicon.ico',

    # AI Cybersecurity
    'CrowdStrike Falcon': 'https://www.crowdstrike.com/favicon.ico',
    'Darktrace': 'https://www.darktrace.com/favicon.ico',
    'SentinelOne': 'https://www.sentinelone.com/favicon.ico',
    'Palo Alto Cortex': 'https://www.paloaltonetworks.com/etc/designs/pan-corp/images/favicons/favicon.ico',
    'Vectra AI': 'https://www.vectra.ai/favicon.ico',
    'Cybereason': 'https://www.cybereason.com/favicon.ico',
    'Cylance': 'https://www.blackberry.com/content/dam/bbcomv4/blackberry-com/images/icons/favicon.ico',
    'Microsoft Defender AI': 'https://www.microsoft.com/favicon.ico',
    'Splunk Enterprise Security': 'https://www.splunk.com/content/dam/splunk2/images/icons/favicons/favicon.ico',
    'Abnormal Security': 'https://abnormalsecurity.com/favicon.ico',
    'Recorded Future': 'https://www.recordedfuture.com/favicon.ico',
    'ZeroFox': 'https://www.zerofox.com/favicon.ico',

    # AI Medical
    'IBM Watson Health': 'https://www.ibm.com/favicon.ico',
    'PathAI': 'https://www.pathai.com/favicon.ico',
    'Zebra Medical Vision': 'https://www.zebra-med.com/favicon.ico',
    'Viz.ai': 'https://www.viz.ai/favicon.ico',
    'Tempus': 'https://www.tempus.com/favicon.ico',
    'Paige.AI': 'https://paige.ai/favicon.ico',
    'Aidoc': 'https://www.aidoc.com/favicon.ico',
    'HeartFlow': 'https://www.heartflow.com/favicon.ico',
    'Qure.ai': 'https://qure.ai/favicon.ico',
    'K Health': 'https://www.khealth.com/favicon.ico',
    'Ada Health': 'https://ada.com/favicon.ico',
    'Babylon Health': 'https://www.babylonhealth.com/favicon.ico',

    # AI Architecture
    'Spacemaker': 'https://www.spacemakerai.com/favicon.ico',
    'TestFit': 'https://testfit.io/favicon.ico',
    'Finch3D': 'https://www.finch3d.com/favicon.ico',
    'Hypar': 'https://hypar.io/favicon.ico',
    'Autodesk Forma': 'https://www.autodesk.com/favicon.ico',
    'Archistar': 'https://archistar.ai/favicon.ico',
    'Augmenta': 'https://www.augmenta.ai/favicon.ico',
    'Buildots': 'https://buildots.com/favicon.ico',
    'OpenSpace': 'https://www.openspace.ai/favicon.ico',
    'Doxel': 'https://www.doxel.ai/favicon.ico',
    'Reconstruct': 'https://reconstructinc.com/favicon.ico',
    'Join': 'https://www.join.build/favicon.ico',
}

def remove_duplicate_simple_cards(file_path, category_key):
    """Supprime les cartes simples en double (garde les full reviews)."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Trouver tous les noms dans les cartes full review
        full_review_names = set()
        full_review_pattern = r'<article class="tool-card-full">.*?<h3>([^<]+)</h3>'
        for match in re.finditer(full_review_pattern, content, re.DOTALL):
            full_review_names.add(match.group(1).strip())

        if not full_review_names:
            print(f"   ℹ️  Pas de full reviews dans cette catégorie")
            return False, 0

        # Supprimer les cartes simples avec les mêmes noms
        removed_count = 0
        for name in full_review_names:
            # Pattern pour carte simple <article> ou <a>
            simple_card_pattern = rf'<(article|a[^>]*) class="tool-card">.*?<h3>{re.escape(name)}</h3>.*?</\1>'

            matches = list(re.finditer(simple_card_pattern, content, re.DOTALL))
            if len(matches) > 1:
                # Garder seulement la première occurrence (qui devrait être après la full review)
                # Supprimer toutes sauf la première
                for match in matches[1:]:
                    content = content.replace(match.group(0), '')
                    removed_count += 1
                    print(f"   🗑️  Supprimé doublon: {name}")

        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, removed_count

        return False, 0

    except Exception as e:
        print(f"   ❌ Erreur: {e}")
        return False, 0

def download_logo(name, url, save_dir):
    """Télécharge un logo."""
    try:
        # Créer un nom de fichier sûr
        safe_name = re.sub(r'[^\w\s-]', '', name.lower())
        safe_name = re.sub(r'[-\s]+', '-', safe_name)

        # Déterminer l'extension
        ext = '.svg' if url.endswith('.svg') else '.png'
        filename = f"{safe_name}{ext}"
        filepath = save_dir / filename

        # Télécharger
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        with open(filepath, 'wb') as f:
            f.write(response.content)

        return filename, True

    except Exception as e:
        print(f"      ⚠️  Échec téléchargement {name}: {e}")
        return None, False

def main():
    """Programme principal."""
    base_dir = Path('/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/categories')

    print("🗑️  ÉTAPE 1: Suppression des doublons...\n")

    total_removed = 0
    categories = ['ai-chatbots', 'ai-writing', 'ai-coding', 'ai-image', 'ai-video',
                  'ai-audio', 'ai-productivity', 'ai-seo', 'ai-business', 'ai-networking',
                  'ai-cybersecurity', 'ai-medical', 'ai-architecture']

    for category in categories:
        file_path = base_dir / f'{category}.html'
        if file_path.exists():
            print(f"📁 {category}")
            success, count = remove_duplicate_simple_cards(file_path, category)
            if success and count > 0:
                total_removed += count
                print(f"   ✅ {count} doublon(s) supprimé(s)\n")
            else:
                print(f"   ✓ Aucun doublon\n")

    print(f"{'='*60}")
    print(f"✅ Doublons supprimés: {total_removed}")
    print(f"\n📥 ÉTAPE 2: Téléchargement des logos...\n")

    # Créer le dossier logos s'il n'existe pas
    logos_dir = Path('/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/assets/images/logos')
    logos_dir.mkdir(parents=True, exist_ok=True)

    downloaded = 0
    failed = 0

    for name, url in LOGO_URLS.items():
        print(f"  {name}...", end=' ')
        filename, success = download_logo(name, url, logos_dir)
        if success:
            print(f"✅ {filename}")
            downloaded += 1
        else:
            print(f"❌")
            failed += 1
        time.sleep(0.5)  # Éviter de surcharger les serveurs

    print(f"\n{'='*60}")
    print(f"🎉 Terminé!")
    print(f"📊 Logos téléchargés: {downloaded}")
    print(f"⚠️  Échecs: {failed}")
    print(f"\n⏭️  ÉTAPE 3: Implémentation des logos dans le HTML (à faire ensuite)")

if __name__ == '__main__':
    main()
