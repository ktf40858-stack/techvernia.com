#!/usr/bin/env python3
"""
Download ALL real logos for ALL categories.
"""

import os
import time
import requests

BASE_DIR = "/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/assets/images/tools"

# Complete list of all tools with their domains
ALL_LOGOS = {
    'image/adobe-firefly': ['adobe.com', 'firefly.adobe.com'],
    'image/canva-ai': ['canva.com'],
    'image/clipdrop': ['clipdrop.co'],
    'image/ideogram': ['ideogram.ai'],
    'image/leonardo-ai': ['leonardo.ai'],
    'image/stable-diffusion': ['stability.ai'],

    'video/pictory': ['pictory.ai'],
    'video/heygen': ['heygen.com'],
    'video/invideo': ['invideo.io'],
    'video/kapwing': ['kapwing.com'],
    'video/lumen5': ['lumen5.com'],
    'video/runway': ['runwayml.com'],
    'video/synthesia': ['synthesia.io'],
    'video/kling-ai': ['klingai.com'],

    'cybersecurity/abnormal-security': ['abnormalsecurity.com'],
    'cybersecurity/cisco-securex': ['cisco.com'],
    'cybersecurity/cortex-xdr': ['paloaltonetworks.com'],
    'cybersecurity/crowdstrike': ['crowdstrike.com'],
    'cybersecurity/cyberark': ['cyberark.com'],
    'cybersecurity/cylance': ['blackberry.com'],
    'cybersecurity/darktrace': ['darktrace.com'],
    'cybersecurity/fortinet': ['fortinet.com'],
    'cybersecurity/ibm-qradar': ['ibm.com'],
    'cybersecurity/lacework': ['lacework.com'],
    'cybersecurity/microsoft-sentinel': ['microsoft.com', 'azure.microsoft.com'],
    'cybersecurity/okta': ['okta.com'],
    'cybersecurity/palo-alto-ngfw': ['paloaltonetworks.com'],
    'cybersecurity/qualys': ['qualys.com'],
    'cybersecurity/rapid7': ['rapid7.com'],
    'cybersecurity/sentinelone': ['sentinelone.com'],
    'cybersecurity/snyk': ['snyk.io'],
    'cybersecurity/splunk-security': ['splunk.com'],
    'cybersecurity/tenable': ['tenable.com'],
    'cybersecurity/vectra-ai': ['vectra.ai'],
    'cybersecurity/wiz': ['wiz.io'],
}

def download_logo(category, tool_name, domains):
    """Try to download logo from multiple sources."""

    output_dir = os.path.join(BASE_DIR, category)
    os.makedirs(output_dir, exist_ok=True)

    print(f"  📥 {tool_name}...", end=" ", flush=True)

    for domain in domains:
        # Try Clearbit first (best quality usually)
        url = f"https://logo.clearbit.com/{domain}"
        output_path = os.path.join(output_dir, f"{tool_name}.png")

        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200 and len(response.content) > 1000:
                with open(output_path, 'wb') as f:
                    f.write(response.content)
                size = os.path.getsize(output_path)
                print(f"✓ ({size:,} bytes)")
                return True
        except:
            pass

    print("✗ Failed")
    return False

# Download all logos
print("🎨 Downloading ALL real logos...\n")

total = len(ALL_LOGOS)
success = 0

for logo_path, domains in ALL_LOGOS.items():
    category, tool = logo_path.split('/')
    if download_logo(category, tool, domains):
        success += 1
    time.sleep(0.5)

print(f"\n{'=' * 70}")
print(f"✅ Downloaded {success}/{total} logos successfully")
print(f"{'=' * 70}")
