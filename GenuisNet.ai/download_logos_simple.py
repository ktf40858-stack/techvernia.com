#!/usr/bin/env python3
"""
Simple script to download logos from various free sources.
Uses multiple fallback methods to ensure we get logos for all tools.
"""

import os
import requests
import time
from urllib.parse import quote

base_path = "/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/assets/images/tools"

# All tools with their domains
tools = {
    'writing': {
        'copyai': 'copy.ai',
        'grammarly': 'grammarly.com',
        'jasper-ai': 'jasper.ai',
        'quillbot': 'quillbot.com',
        'rytr': 'rytr.me',
        'wordtune': 'wordtune.com',
        'writesonic': 'writesonic.com'
    },
    'image': {
        'adobe-firefly': 'adobe.com',
        'canva-ai': 'canva.com',
        'clipdrop': 'clipdrop.co',
        'dall-e-3': 'openai.com',
        'ideogram': 'ideogram.ai',
        'leonardo-ai': 'leonardo.ai',
        'midjourney': 'midjourney.com',
        'stable-diffusion': 'stability.ai'
    },
    'video': {
        'pictory': 'pictory.ai'
    },
    'cybersecurity': {
        'abnormal-security': 'abnormalsecurity.com',
        'cisco-securex': 'cisco.com',
        'cortex-xdr': 'paloaltonetworks.com',
        'crowdstrike': 'crowdstrike.com',
        'cyberark': 'cyberark.com',
        'cylance': 'blackberry.com',
        'darktrace': 'darktrace.com',
        'fortinet': 'fortinet.com',
        'ibm-qradar': 'ibm.com',
        'lacework': 'lacework.com',
        'microsoft-sentinel': 'microsoft.com',
        'okta': 'okta.com',
        'palo-alto-ngfw': 'paloaltonetworks.com',
        'qualys': 'qualys.com',
        'rapid7': 'rapid7.com',
        'sentinelone': 'sentinelone.com',
        'snyk': 'snyk.io',
        'splunk-security': 'splunk.com',
        'tenable': 'tenable.com',
        'vectra-ai': 'vectra.ai',
        'wiz': 'wiz.io'
    }
}

def download_logo(category, tool_name, domain):
    """Try multiple sources to download logo."""

    output_svg = os.path.join(base_path, category, f"{tool_name}.svg")
    output_png = os.path.join(base_path, category, f"{tool_name}.png")

    # Skip if already exists and is good
    if os.path.exists(output_svg) and os.path.getsize(output_svg) > 1000:
        print(f"  ⏭  {tool_name}: Already exists")
        return True

    print(f"  📥 {tool_name}...", end=" ", flush=True)

    # Method 1: Clearbit (reliable for many companies)
    try:
        url = f"https://logo.clearbit.com/{domain}"
        response = requests.get(url, timeout=10)
        if response.status_code == 200 and len(response.content) > 1000:
            with open(output_png, 'wb') as f:
                f.write(response.content)
            print("✓ (Clearbit PNG)")
            return True
    except:
        pass

    # Method 2: Logo.dev
    try:
        url = f"https://img.logo.dev/{domain}?token=pk_X-1ZO13CRaadr0E7e2bMvQ"
        response = requests.get(url, timeout=10)
        if response.status_code == 200 and len(response.content) > 1000:
            with open(output_png, 'wb') as f:
                f.write(response.content)
            print("✓ (Logo.dev)")
            return True
    except:
        pass

    # Method 3: Google favicon (fallback)
    try:
        url = f"https://www.google.com/s2/favicons?domain={domain}&sz=128"
        response = requests.get(url, timeout=10)
        if response.status_code == 200 and len(response.content) > 500:
            with open(output_png, 'wb') as f:
                f.write(response.content)
            print("✓ (Google Favicon)")
            return True
    except:
        pass

    print("✗ Failed")
    return False

# Download logos
print("🔽 Downloading logos from multiple sources...\n")

total = 0
success = 0

for category, tools_dict in tools.items():
    print(f"\n📁 {category.upper()}")
    print("=" * 60)

    for tool_name, domain in tools_dict.items():
        total += 1
        if download_logo(category, tool_name, domain):
            success += 1
        time.sleep(0.5)  # Be nice to servers

print(f"\n{'=' * 60}")
print(f"✅ Downloaded: {success}/{total} logos")
print(f"{'=' * 60}\n")
print("Run verify_tool_logos.py to check results!")
