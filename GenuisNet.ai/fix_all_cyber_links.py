#!/usr/bin/env python3
"""
Comprehensive script to link all cybersecurity tools that have reviews.
"""
import re

page_path = "/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/categories/ai-cybersecurity.html"

# Available reviews
reviews = [
    'abnormal-security', 'cisco-securex', 'cortex-xdr', 'crowdstrike',
    'cyberark', 'cylance', 'darktrace', 'fortinet', 'ibm-qradar',
    'lacework', 'microsoft-sentinel', 'okta', 'palo-alto-ngfw',
    'qualys', 'rapid7', 'sentinelone', 'snyk', 'splunk-security',
    'tenable', 'vectra-ai', 'wiz'
]

# Tool name to review file mapping
mappings = {
    'Abnormal Security': 'abnormal-security',
    'Cisco SecureX': 'cisco-securex',
    'Cisco': 'cisco-securex',
    'Palo Alto Cortex': 'cortex-xdr',
    'Cortex XDR': 'cortex-xdr',
    'CrowdStrike': 'crowdstrike',
    'CrowdStrike Falcon': 'crowdstrike',
    'CyberArk': 'cyberark',
    'Cylance': 'cylance',
    'BlackBerry Cylance': 'cylance',
    'Darktrace': 'darktrace',
    'Fortinet': 'fortinet',
    'Fortinet FortiGate': 'fortinet',
    'Fortinet FortiGuard': 'fortinet',
    'IBM QRadar': 'ibm-qradar',
    'Lacework': 'lacework',
    'Microsoft Sentinel': 'microsoft-sentinel',
    'Okta': 'okta',
    'Palo Alto Networks': 'palo-alto-ngfw',
    'Palo Alto NGFW': 'palo-alto-ngfw',
    'Qualys': 'qualys',
    'Rapid7': 'rapid7',
    'SentinelOne': 'sentinelone',
    'Snyk': 'snyk',
    'Splunk': 'splunk-security',
    'Splunk Enterprise Security': 'splunk-security',
    'Tenable': 'tenable',
    'Vectra AI': 'vectra-ai',
    'Vectra': 'vectra-ai',
    'Wiz': 'wiz',
}

# Read file
with open(page_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Track updates
updated_count = 0

# For each tool name, update the link
for tool_name, review_file in sorted(mappings.items(), key=lambda x: len(x[0]), reverse=True):
    # Pattern to find: <a href="#">...any content...<h3>ToolName</h3>
    pattern = r'(<a\s+href=")[^"]*("(?:(?!</a>).)*?<h3>' + re.escape(tool_name) + r'</h3>)'
    replacement = rf'\1../reviews/cybersecurity/{review_file}.html\2'

    new_content, count = re.subn(pattern, replacement, content, flags=re.DOTALL)

    if count > 0:
        content = new_content
        updated_count += count
        print(f"✓ Linked: {tool_name} -> {review_file}.html ({count} occurrence(s))")

# Write updated content
with open(page_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n✓ Total links updated: {updated_count}")

# Check final counts
remaining_hash = content.count('href="#"')
review_links = len(re.findall(r'href="\.\./reviews/cybersecurity/[^"]+\.html"', content))

print(f"✓ Review links now: {review_links}")
print(f"✓ Placeholder '#' links remaining: {remaining_hash}")
