#!/usr/bin/env python3
"""
Bulk download ALL logos from Brandfetch.com
This uses the Brandfetch API to get high-quality official logos.
"""

import os
import requests
import time
import json

BASE_DIR = "/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/assets/images/tools"

# All tools with their Brandfetch domains
BRANDFETCH_TOOLS = {
    # WRITING
    'writing/grammarly': 'grammarly.com',
    'writing/copyai': 'copy.ai',
    'writing/jasper-ai': 'jasper.ai',
    'writing/quillbot': 'quillbot.com',
    'writing/rytr': 'rytr.me',
    'writing/wordtune': 'wordtune.com',
    'writing/writesonic': 'writesonic.com',

    # IMAGE
    'image/adobe-firefly': 'adobe.com',
    'image/canva-ai': 'canva.com',
    'image/clipdrop': 'clipdrop.co',
    'image/dall-e-3': 'openai.com',
    'image/ideogram': 'ideogram.ai',
    'image/leonardo-ai': 'leonardo.ai',
    'image/midjourney': 'midjourney.com',
    'image/stable-diffusion': 'stability.ai',

    # VIDEO
    'video/heygen': 'heygen.com',
    'video/invideo': 'invideo.io',
    'video/kapwing': 'kapwing.com',
    'video/kling-ai': 'klingai.com',
    'video/lumen5': 'lumen5.com',
    'video/pictory': 'pictory.ai',
    'video/runway': 'runwayml.com',
    'video/synthesia': 'synthesia.io',

    # AUDIO
    'audio/descript': 'descript.com',
    'audio/elevenlabs': 'elevenlabs.io',
    'audio/murf-ai': 'murf.ai',
    'audio/playht': 'play.ht',
    'audio/resemble-ai': 'resemble.ai',
    'audio/speechify': 'speechify.com',
    'audio/suno-ai': 'suno.com',
    'audio/udio': 'udio.com',

    # CODING
    'coding/codeium': 'codeium.com',
    'coding/codewhisperer': 'aws.amazon.com',
    'coding/cursor': 'cursor.sh',
    'coding/deepseek-coder': 'deepseek.com',
    'coding/github-copilot': 'github.com',
    'coding/replit': 'replit.com',
    'coding/tabnine': 'tabnine.com',
    'coding/windsurf': 'codeium.com',

    # PRODUCTIVITY
    'productivity/clickup-ai': 'clickup.com',
    'productivity/firefliesai': 'fireflies.ai',
    'productivity/mem-ai': 'mem.ai',
    'productivity/motion': 'usemotion.com',
    'productivity/notion-ai': 'notion.so',
    'productivity/otterai': 'otter.ai',
    'productivity/reclaim-ai': 'reclaim.ai',
    'productivity/zapier': 'zapier.com',

    # SEO
    'seo/ahrefs': 'ahrefs.com',
    'seo/clearscope': 'clearscope.io',
    'seo/frase': 'frase.io',
    'seo/marketmuse': 'marketmuse.com',
    'seo/neuronwriter': 'neuronwriter.com',
    'seo/scalenut': 'scalenut.com',
    'seo/semrush': 'semrush.com',
    'seo/surfer-seo': 'surferseo.com',

    # BUSINESS
    'business/chorusai': 'chorus.ai',
    'business/conversica': 'conversica.com',
    'business/drift': 'drift.com',
    'business/gong': 'gong.io',
    'business/hubspot-ai': 'hubspot.com',
    'business/looker': 'looker.com',
    'business/salesforce-einstein': 'salesforce.com',
    'business/tableau': 'tableau.com',

    # CYBERSECURITY
    'cybersecurity/abnormal-security': 'abnormalsecurity.com',
    'cybersecurity/cisco-securex': 'cisco.com',
    'cybersecurity/cortex-xdr': 'paloaltonetworks.com',
    'cybersecurity/crowdstrike': 'crowdstrike.com',
    'cybersecurity/cyberark': 'cyberark.com',
    'cybersecurity/cylance': 'blackberry.com',
    'cybersecurity/darktrace': 'darktrace.com',
    'cybersecurity/fortinet': 'fortinet.com',
    'cybersecurity/ibm-qradar': 'ibm.com',
    'cybersecurity/lacework': 'lacework.com',
    'cybersecurity/microsoft-sentinel': 'microsoft.com',
    'cybersecurity/okta': 'okta.com',
    'cybersecurity/palo-alto-ngfw': 'paloaltonetworks.com',
    'cybersecurity/qualys': 'qualys.com',
    'cybersecurity/rapid7': 'rapid7.com',
    'cybersecurity/sentinelone': 'sentinelone.com',
    'cybersecurity/snyk': 'snyk.io',
    'cybersecurity/splunk-security': 'splunk.com',
    'cybersecurity/tenable': 'tenable.com',
    'cybersecurity/vectra-ai': 'vectra.ai',
    'cybersecurity/wiz': 'wiz.io',

    # ARCHITECTURE
    'architecture/finch3d': 'finch3d.com',
    'architecture/maket-ai': 'maket.ai',
    'architecture/arko-ai': 'arko.ai',
    'architecture/testfit': 'testfit.io',
    'architecture/spacemaker-ai': 'spacemakerai.com',
    'architecture/hypar': 'hypar.io',
    'architecture/veras-ai': 'veras.ai',
    'architecture/gendo-ai': 'gendo.ai',

    # MEDICAL
    'medical/aidoc': 'aidoc.com',
    'medical/butterfly-iq': 'butterflynetwork.com',
    'medical/nuance-dragon': 'nuance.com',
    'medical/paige-ai': 'paige.ai',
    'medical/pathai': 'pathai.com',
    'medical/tempus': 'tempus.com',
    'medical/viz-ai': 'viz.ai',
    'medical/zebra-medical': 'zebra-med.com',
}

def download_from_brandfetch(domain, output_path):
    """Download logo from Brandfetch API."""
    try:
        # Brandfetch API v2 endpoint
        url = f"https://api.brandfetch.io/v2/brands/{domain}"

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

        response = requests.get(url, headers=headers, timeout=15)

        if response.status_code == 200:
            data = response.json()

            # Try to get SVG logo first
            if 'logos' in data and len(data['logos']) > 0:
                logo = data['logos'][0]

                # Find SVG format
                svg_url = None
                png_url = None

                if 'formats' in logo:
                    for format_item in logo['formats']:
                        if format_item.get('format') == 'svg':
                            svg_url = format_item.get('src')
                        elif format_item.get('format') == 'png':
                            png_url = format_item.get('src')

                # Download SVG or PNG
                logo_url = svg_url or png_url
                if logo_url:
                    logo_response = requests.get(logo_url, timeout=10)
                    if logo_response.status_code == 200 and len(logo_response.content) > 1000:
                        # Determine extension
                        ext = 'svg' if svg_url else 'png'
                        final_path = output_path.replace('.png', f'.{ext}')

                        with open(final_path, 'wb') as f:
                            f.write(logo_response.content)
                        return True, len(logo_response.content)

    except Exception as e:
        pass

    return False, 0

def main():
    print("🎨 Brandfetch Bulk Logo Downloader")
    print("=" * 70)
    print("Downloading ALL official logos from Brandfetch.com API...")
    print("=" * 70 + "\n")

    total = len(BRANDFETCH_TOOLS)
    success = 0
    failed = []

    for tool_path, domain in BRANDFETCH_TOOLS.items():
        category, tool_name = tool_path.split('/')

        output_dir = os.path.join(BASE_DIR, category)
        os.makedirs(output_dir, exist_ok=True)

        output_path = os.path.join(output_dir, f"{tool_name}.png")

        print(f"📥 {tool_name:<25} ({domain})...", end=" ", flush=True)

        result, size = download_from_brandfetch(domain, output_path)

        if result:
            print(f"✓ ({size:,} bytes)")
            success += 1
        else:
            print("✗ Failed")
            failed.append(f"{category}/{tool_name} ({domain})")

        time.sleep(1)  # Be respectful to Brandfetch API

    print("\n" + "=" * 70)
    print(f"📊 RESULTS")
    print("=" * 70)
    print(f"✅ Successfully downloaded: {success}/{total} logos")
    print(f"❌ Failed: {len(failed)} logos")

    if failed:
        print(f"\n⚠️  Failed logos:")
        for item in failed:
            print(f"   • {item}")

    print("\nRun 'python3 verify_tool_logos.py' to verify all logos!")

if __name__ == "__main__":
    main()
