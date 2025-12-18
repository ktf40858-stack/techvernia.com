#!/usr/bin/env python3
import re

page_path = "/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/categories/ai-cybersecurity.html"

# Read the file
with open(page_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Manual fixes for specific tools with reviews
fixes = [
    # Fix IBM QRadar (appears twice, one at line 594)
    (r'(<a href=")#(" class="tool-card">.*?<h3>IBM QRadar</h3>)', 
     r'\1../reviews/cybersecurity/ibm-qradar.html\2'),
    
    # Fix Fortinet (wrong link to cylance, should be fortinet)
    (r'(<a href=")../reviews/cybersecurity/cylance\.html(" class="tool-card">.*?<h3>Fortinet FortiGuard</h3>)',
     r'\1../reviews/cybersecurity/fortinet.html\2'),
    
    # Fix remaining tools that have reviews
    (r'(<a href=")#(" class="tool-card">.*?<h3>Microsoft Sentinel</h3>)',
     r'\1../reviews/cybersecurity/microsoft-sentinel.html\2'),
    
    (r'(<a href=")#(" class="tool-card">.*?<h3>Splunk Enterprise Security</h3>)',
     r'\1../reviews/cybersecurity/splunk-security.html\2'),
    
    (r'(<a href=")#(" class="tool-card">.*?<h3>Palo Alto Networks</h3>)',
     r'\1../reviews/cybersecurity/palo-alto-ngfw.html\2'),
    
    (r'(<a href=")#(" class="tool-card">.*?<h3>Fortinet FortiGate</h3>)',
     r'\1../reviews/cybersecurity/fortinet.html\2'),
    
    (r'(<a href=")#(" class="tool-card">.*?<h3>CyberArk</h3>)',
     r'\1../reviews/cybersecurity/cyberark.html\2'),
    
    (r'(<a href=")#(" class="tool-card">.*?<h3>Okta</h3>)',
     r'\1../reviews/cybersecurity/okta.html\2'),
    
    (r'(<a href=")#(" class="tool-card">.*?<h3>Wiz</h3>)',
     r'\1../reviews/cybersecurity/wiz.html\2'),
    
    (r'(<a href=")#(" class="tool-card">.*?<h3>Snyk</h3>)',
     r'\1../reviews/cybersecurity/snyk.html\2'),
    
    (r'(<a href=")#(" class="tool-card">.*?<h3>Lacework</h3>)',
     r'\1../reviews/cybersecurity/lacework.html\2'),
    
    (r'(<a href=")#(" class="tool-card">.*?<h3>Tenable</h3>)',
     r'\1../reviews/cybersecurity/tenable.html\2'),
    
    (r'(<a href=")#(" class="tool-card">.*?<h3>Qualys</h3>)',
     r'\1../reviews/cybersecurity/qualys.html\2'),
    
    (r'(<a href=")#(" class="tool-card">.*?<h3>Rapid7</h3>)',
     r'\1../reviews/cybersecurity/rapid7.html\2'),
    
    (r'(<a href=")#(" class="tool-card">.*?<h3>Cisco SecureX</h3>)',
     r'\1../reviews/cybersecurity/cisco-securex.html\2'),
]

updated = 0
for pattern, replacement in fixes:
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    if new_content != content:
        content = new_content
        updated += 1
        print(f"✓ Fixed link")

# Write back
with open(page_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n✓ Total fixes applied: {updated}")
