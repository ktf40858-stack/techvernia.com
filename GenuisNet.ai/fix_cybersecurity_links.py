#!/usr/bin/env python3
"""
Script to fix cybersecurity tool links to point to actual review pages.
"""

import os
import re

base_path = "/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai"
reviews_dir = os.path.join(base_path, "pages/reviews/cybersecurity")
page_path = os.path.join(base_path, "pages/categories/ai-cybersecurity.html")

# Get list of available reviews (without .html extension)
available_reviews = []
if os.path.exists(reviews_dir):
    for filename in os.listdir(reviews_dir):
        if filename.endswith('.html'):
            available_reviews.append(filename.replace('.html', ''))

print(f"Found {len(available_reviews)} cybersecurity reviews:")
for review in sorted(available_reviews):
    print(f"  - {review}")

# Mapping of tool names in the page to review file names
tool_mappings = {
    'CrowdStrike Falcon': 'crowdstrike',
    'CrowdStrike': 'crowdstrike',
    'Darktrace': 'darktrace',
    'SentinelOne': 'sentinelone',
    'Palo Alto Cortex': 'cortex-xdr',
    'Cortex XDR': 'cortex-xdr',
    'Vectra AI': 'vectra-ai',
    'Cylance': 'cylance',
    'Microsoft Sentinel': 'microsoft-sentinel',
    'Splunk': 'splunk-security',
    'Splunk Enterprise Security': 'splunk-security',
    'IBM QRadar': 'ibm-qradar',
    'Fortinet FortiGate': 'fortinet',
    'Fortinet': 'fortinet',
    'Palo Alto Networks': 'palo-alto-ngfw',
    'Palo Alto NGFW': 'palo-alto-ngfw',
    'Cisco SecureX': 'cisco-securex',
    'CyberArk': 'cyberark',
    'Okta': 'okta',
    'Wiz': 'wiz',
    'Snyk': 'snyk',
    'Lacework': 'lacework',
    'Tenable': 'tenable',
    'Qualys': 'qualys',
    'Rapid7': 'rapid7',
    'Abnormal Security': 'abnormal-security',
}

# Read the page
with open(page_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace links
updated_count = 0
for tool_name, review_file in tool_mappings.items():
    if review_file in available_reviews:
        # Pattern: <a href="#">... <h3>Tool Name</h3>
        pattern = f'(<a href=")[^"]*(".*?<h3>{re.escape(tool_name)}</h3>)'
        replacement = f'\\1../reviews/cybersecurity/{review_file}.html\\2'

        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

        if new_content != content:
            content = new_content
            updated_count += 1
            print(f"✓ Updated link for: {tool_name} -> {review_file}.html")

# Write the updated content
with open(page_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n✓ Total links updated: {updated_count}")
print(f"✓ File updated: ai-cybersecurity.html")
