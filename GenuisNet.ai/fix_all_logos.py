#!/usr/bin/env python3
"""
Corrige TOUS les logos à travers le site web
- Mappe correctement les logos téléchargés aux AI
- Utilise des emojis distinctifs pour les AI sans logo
"""

from pathlib import Path
import re

# Mapping exact: nom d'AI -> nom de fichier logo
LOGO_MAPPING = {
    # AI Chatbots - logos téléchargés
    'Gemini': 'gemini.svg',
    'Perplexity AI': 'perplexity-ai.png',
    'Poe': 'poe.svg',
    'HuggingChat': 'huggingchat.svg',
    'DeepSeek': 'deepseek.png',
    'Grok': 'grok.png',
    'Cohere': 'cohere.png',
    'Character.AI': 'characterai.png',

    # AI Writing - logos téléchargés
    'Rytr': 'rytr.png',
    'QuillBot': 'quillbot.png',
    'ProWritingAid': 'prowritingaid.png',
    'Notion AI': 'notion-ai.png',
    'Frase': 'frase.png',

    # AI Coding - logos téléchargés
    'Cursor': 'cursor.png',
    'Tabnine': 'tabnine.png',
    'Codeium': 'codeium.png',
    'Amazon CodeWhisperer': 'amazon-codewhisperer.png',
    'Sourcegraph Cody': 'sourcegraph-cody.svg',
    'AskCodi': 'askcodi.png',

    # AI Image - logos téléchargés
    'Stable Diffusion': 'stable-diffusion.png',
    'Leonardo.ai': 'leonardoai.png',
    'Adobe Firefly': 'adobe-firefly.png',
    'Canva AI': 'canva-ai.svg',
    'DreamStudio': 'dreamstudio.png',
    'Playground AI': 'playground-ai.png',
    'NightCafe': 'nightcafe.png',
    'Artbreeder': 'artbreeder.png',

    # AI Video - logos téléchargés
    'Pika Labs': 'pika-labs.png',
    'HeyGen': 'heygen.png',
    'D-ID': 'd-id.png',
    'Pictory': 'pictory.png',
    'InVideo AI': 'invideo-ai.png',
    'Fliki': 'fliki.png',
    'CapCut': 'capcut.png',

    # AI Audio - logos téléchargés
    'ElevenLabs': 'elevenlabs.png',
    'Play.ht': 'playht.png',
    'Speechify': 'speechify.png',
    'Resemble AI': 'resemble-ai.png',
    'Otter.ai': 'otterai.png',
    'AssemblyAI': 'assemblyai.png',
    'Suno AI': 'suno-ai.png',

    # AI Productivity - logos téléchargés
    'Motion': 'motion.png',
    'ClickUp AI': 'clickup-ai.png',
    'Fireflies.ai': 'firefliesai.png',
    'Taskade': 'taskade.png',
    'SaneBox': 'sanebox.png',

    # AI SEO - logos téléchargés
    'Clearscope': 'clearscope.png',
    'MarketMuse': 'marketmuse.png',
    'NeuronWriter': 'neuronwriter.png',
    'GrowthBar': 'growthbar.png',
    'INK': 'ink.png',
    'RankIQ': 'rankiq.png',
    'WordLift': 'wordlift.png',

    # AI Business - logos téléchargés
    'HubSpot AI': 'hubspot-ai.png',
    'Zoho Zia': 'zoho-zia.png',
    'IBM Watson': 'ibm-watson.png',
    'Tableau AI': 'tableau-ai.png',
    'Power BI AI': 'power-bi-ai.svg',
    'DataRobot': 'datarobot.png',
    'H2O.ai': 'h2oai.png',
    'ThoughtSpot': 'thoughtspot.png',
    'ServiceNow AI': 'servicenow-ai.png',
    'Salesforce Einstein': 'salesforce-einstein.svg',

    # AI Networking - logos téléchargés
    'Cisco DNA Center': 'cisco-dna-center.png',
    'Fortinet FortiAI': 'fortinet-fortiai.png',
    'Dynatrace': 'dynatrace.png',
    'Splunk': 'splunk.png',
    'New Relic AI': 'new-relic-ai.png',
    'ThousandEyes': 'thousandeyes.png',
    'NetBrain': 'netbrain.png',
    'SolarWinds AI': 'solarwinds-ai.png',
    'Datadog': 'datadog.png',

    # AI Cybersecurity - logos téléchargés
    'SentinelOne': 'sentinelone.png',
    'Cybereason': 'cybereason.png',
    'Microsoft Defender AI': 'microsoft-defender-ai.png',
    'Splunk Enterprise Security': 'splunk-enterprise-security.png',
    'Abnormal Security': 'abnormal-security.png',
    'Recorded Future': 'recorded-future.png',
    'ZeroFox': 'zerofox.png',
    'Palo Alto Cortex': 'palo-alto-cortex.png',

    # AI Medical - logos téléchargés
    'IBM Watson Health': 'ibm-watson-health.png',
    'PathAI': 'pathai.png',
    'Paige.AI': 'paigeai.png',
    'Aidoc': 'aidoc.png',
    'HeartFlow': 'heartflow.png',
    'Qure.ai': 'qureai.png',
    'K Health': 'k-health.png',
    'Ada Health': 'ada-health.png',

    # AI Architecture - logos téléchargés
    'Spacemaker': 'spacemaker.png',
    'Hypar': 'hypar.png',
    'Autodesk Forma': 'autodesk-forma.png',
    'Buildots': 'buildots.png',
    'OpenSpace': 'openspace.png',
    'Reconstruct': 'reconstruct.png',
    'Join': 'join.png',
}

# Emojis distinctifs pour les AI sans logo
EMOJI_FALLBACKS = {
    # Chatbots
    'Microsoft Copilot': '🤖',
    'Pi': '🥧',
    'YouChat': '💬',
    'Mistral Chat': '🌬️',

    # Writing
    'Jasper': '✨',
    'Copy.ai': '📝',
    'Writesonic': '🎵',
    'Wordtune': '🎯',
    'Sudowrite': '✍️',
    'Grammarly': '✅',
    'Scalenut': '📈',

    # Coding
    'GitHub Copilot': '👨‍✈️',
    'Replit AI': '🔄',
    'Blackbox AI': '⬛',
    'Phind': '🔍',
    'Bito AI': '🤖',
    'AlphaCode': '🅰️',

    # Image
    'Midjourney': '🎨',
    'DALL-E 3': '🖼️',
    'Ideogram': '💡',
    'Runway ML': '🎬',

    # Video
    'Runway Gen-2': '🎬',
    'Synthesia': '🎥',
    'Descript': '🎙️',
    'Lumen5': '💡',
    'OpusClip': '✂️',

    # Audio
    'Murf AI': '🎤',
    'Descript Overdub': '🎙️',
    'WellSaid Labs': '🗣️',
    'LOVO': '🔊',
    'Krisp': '🔇',

    # Productivity
    'Reclaim AI': '📅',
    'Mem': '🧠',
    'Tactiq': '📝',
    'Clockwise': '🕐',
    'Sunsama': '☀️',
    'Superhuman': '⚡',

    # SEO
    'Surfer SEO': '🏄',
    'LongShot AI': '🎯',
    'SEO.ai': '🔍',

    # Business
    'UiPath': '🤖',
    'Workday AI': '💼',

    # Networking
    'Juniper Mist AI': '🌫️',
    'Aruba AI': '🏝️',
    'Auvik': '🌐',

    # Cybersecurity
    'CrowdStrike Falcon': '🦅',
    'Darktrace': '🕷️',
    'Vectra AI': '🔎',
    'Cylance': '🛡️',

    # Medical
    'Zebra Medical Vision': '🦓',
    'Viz.ai': '🧠',
    'Tempus': '⏱️',
    'Babylon Health': '🏥',

    # Architecture
    'TestFit': '📐',
    'Finch3D': '🐦',
    'Archistar': '🏗️',
    'Augmenta': '🔧',
    'Doxel': '📊',
}

def fix_logos_in_file(file_path):
    """Corrige tous les logos dans un fichier HTML."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        fixed_count = 0

        # Chemin relatif vers les logos
        logo_path = '../../assets/images/logos/'

        # Trouver toutes les cartes tool-card
        card_pattern = r'(<(?:article|a[^>]*) class="tool-card">)(.*?)(</(?:article|a)>)'

        def fix_card_logo(match):
            nonlocal fixed_count
            opening_tag = match.group(1)
            card_content = match.group(2)
            closing_tag = match.group(3)

            # Extraire le nom de l'AI
            h3_match = re.search(r'<h3>([^<]+)</h3>', card_content)
            if not h3_match:
                return match.group(0)

            ai_name = h3_match.group(1).strip()

            # Vérifier si on a un logo ou un emoji pour cette AI
            if ai_name in LOGO_MAPPING:
                logo_file = LOGO_MAPPING[ai_name]
                new_logo = f'<div class="tool-logo">\n                        <img src="{logo_path}{logo_file}" alt="{ai_name}" style="width: 48px; height: 48px; object-fit: contain;">\n                    </div>'
                fixed_count += 1
            elif ai_name in EMOJI_FALLBACKS:
                emoji = EMOJI_FALLBACKS[ai_name]
                new_logo = f'<div class="tool-logo">\n                        <span style="font-size: 32px;">{emoji}</span>\n                    </div>'
            else:
                # Garder emoji par défaut
                new_logo = f'<div class="tool-logo">\n                        <span style="font-size: 32px;">🤖</span>\n                    </div>'

            # Remplacer le logo existant
            new_card_content = re.sub(
                r'<div class="tool-logo">.*?</div>',
                new_logo,
                card_content,
                count=1,
                flags=re.DOTALL
            )

            return opening_tag + new_card_content + closing_tag

        content = re.sub(card_pattern, fix_card_logo, content, flags=re.DOTALL)

        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, fixed_count

        return False, 0

    except Exception as e:
        print(f"   ❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        return False, 0

def main():
    """Programme principal."""
    base_dir = Path('/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/categories')

    print("🎨 CORRECTION DE TOUS LES LOGOS\n")

    categories = ['ai-chatbots', 'ai-writing', 'ai-coding', 'ai-image', 'ai-video',
                  'ai-audio', 'ai-productivity', 'ai-seo', 'ai-business', 'ai-networking',
                  'ai-cybersecurity', 'ai-medical', 'ai-architecture']

    total_fixed = 0
    report = []

    for category in categories:
        file_path = base_dir / f'{category}.html'
        if file_path.exists():
            print(f"📁 {category}")
            success, count = fix_logos_in_file(file_path)
            if success:
                total_fixed += count
                report.append(f"  ✅ {category}: {count} logos corrigés")
                print(f"   ✅ {count} logos corrigés\n")
            else:
                report.append(f"  ℹ️  {category}: Aucune correction")
                print(f"   ℹ️  Aucune correction\n")

    print(f"{'='*60}")
    print(f"🎉 Terminé!")
    print(f"🖼️  Total logos corrigés: {total_fixed}")

    # Sauvegarder le rapport
    with open('/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/RAPPORT_LOGOS.txt', 'w', encoding='utf-8') as f:
        f.write("RAPPORT DE CORRECTION DES LOGOS\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Total logos corrigés: {total_fixed}\n\n")
        f.write("Détails par catégorie:\n")
        for line in report:
            f.write(line + "\n")

    print("\n📄 Rapport sauvegardé dans RAPPORT_LOGOS.txt")

if __name__ == '__main__':
    main()
