#!/usr/bin/env python3
"""
Convertit les cert-card DIV en liens cliquables dans les pages de review cybersecurity
"""

import re
from pathlib import Path

# Mapping certification → fichier de page
CERT_LINKS = {
    # Fortinet
    'NSE 4 - FortiGate Security': 'fortinet-nse4.html',
    'NSE 7 - Enterprise Firewall': 'fortinet-nse7.html',
    'NSE 8 - Written Exam': 'fortinet-nse8.html',
    # Palo Alto Networks
    'PCNSA': 'paloalto-pcnsa.html',
    'PCNSE': 'paloalto-pcnse.html',
    'PCCET': 'paloalto-pccet.html',
    'PCCSA': 'paloalto-pccsa.html',
    'PCCSE': 'paloalto-pccse.html',
    'PCSAE': 'paloalto-pcsae.html',
    # Microsoft
    'SC-900: Security Fundamentals': 'microsoft-sc900.html',
    'SC-200: Security Operations Analyst': 'microsoft-sc200.html',
    'SC-300: Identity Administrator': 'microsoft-sc300.html',
    'SC-400: Information Protection': 'microsoft-sc400.html',
    'AZ-500: Azure Security': 'microsoft-az500.html',
    # Cisco
    'CyberOps Associate': 'cisco-cyberops.html',
    'CCNP Security': 'cisco-ccnp-security.html',
    'CCIE Security': 'cisco-ccie-security.html',
    # CrowdStrike
    'CCFA - Falcon Administrator': 'crowdstrike-ccfa.html',
    'CCFR - Falcon Responder': 'crowdstrike-ccfr.html',
    'CCFH - Falcon Hunter': 'crowdstrike-ccfh.html',
    # IBM QRadar
    'QRadar SIEM': 'ibm-qradar-siem.html',
    'QRadar SIEM Specialist': 'ibm-qradar-siem.html',
    'QRadar SIEM V7.4.3 Specialist': 'ibm-qradar-siem.html',
    'QRadar Analyst': 'ibm-qradar-analyst.html',
    'QRadar Associate Analyst': 'ibm-qradar-analyst.html',
    'QRadar SIEM Security Analyst': 'ibm-qradar-analyst.html',
    # CyberArk
    'CyberArk Defender': 'cyberark-defender.html',
    'CyberArk Defender - PAM': 'cyberark-defender.html',
    'CyberArk Sentry': 'cyberark-sentry.html',
    'CyberArk Sentry - PAM': 'cyberark-sentry.html',
    'CyberArk Guardian': 'cyberark-guardian.html',
    'CyberArk Guardian - PAM': 'cyberark-guardian.html',
    'Certified Delivery Engineer': 'cyberark-guardian.html',
    # Okta
    'Okta Professional': 'okta-professional.html',
    'Okta Certified Professional': 'okta-professional.html',
    'Okta Administrator': 'okta-administrator.html',
    'Okta Certified Administrator': 'okta-administrator.html',
    'Okta Consultant': 'okta-consultant.html',
    'Okta Certified Consultant': 'okta-consultant.html',
    'Okta Developer': 'okta-developer.html',
    'Okta Certified Developer': 'okta-developer.html',
    # Qualys
    'Qualys VMDR': 'qualys-vmdr.html',
    'VMDR Specialist': 'qualys-vmdr.html',
    'Qualys VMDR Specialist': 'qualys-vmdr.html',
    'Qualys WAS': 'qualys-was.html',
    'WAS Specialist': 'qualys-was.html',
    'Qualys WAS Specialist': 'qualys-was.html',
    # Rapid7
    'Rapid7 InsightVM': 'rapid7-insightvm.html',
    'InsightVM Administrator': 'rapid7-insightvm.html',
    'Rapid7 InsightVM Certified': 'rapid7-insightvm.html',
    'Rapid7 InsightIDR': 'rapid7-insightidr.html',
    'InsightIDR Administrator': 'rapid7-insightidr.html',
    'Rapid7 InsightIDR Certified': 'rapid7-insightidr.html',
    # Tenable
    'Nessus Certified': 'tenable-nessus.html',
    'Nessus Professional': 'tenable-nessus.html',
    'Nessus Certified Professional': 'tenable-nessus.html',
    # Darktrace
    'Darktrace Engineer': 'darktrace-engineer.html',
    'Darktrace Certified Engineer': 'darktrace-engineer.html',
    # SentinelOne
    'SentinelOne Core': 'sentinelone-core.html',
    'SentinelOne Core Administrator': 'sentinelone-core.html',
    'SentinelOne Advanced': 'sentinelone-advanced.html',
    'SentinelOne Advanced Admin': 'sentinelone-advanced.html',
    # Sophos
    'Sophos Engineer': 'sophos-engineer.html',
    'Sophos Certified Engineer': 'sophos-engineer.html',
    'Sophos Architect': 'sophos-architect.html',
    'Sophos Certified Architect': 'sophos-architect.html',
    # Trend Micro
    'Trend Micro Pro': 'trendmicro-professional.html',
    'Trend Micro Professional': 'trendmicro-professional.html',
    'Trend Micro Certified Professional': 'trendmicro-professional.html',
    'Trend Micro Expert': 'trendmicro-expert.html',
    'Trend Micro Certified Expert': 'trendmicro-expert.html',
    # Splunk
    'Splunk ES Admin': 'splunk-es-admin.html',
    'Splunk Enterprise Security Administrator': 'splunk-es-admin.html',
    'Splunk ES Certified Admin': 'splunk-es-admin.html',
    'Splunk SOAR Dev': 'splunk-soar-dev.html',
    'Splunk SOAR Developer': 'splunk-soar-dev.html',
    'Splunk SOAR Certified Dev': 'splunk-soar-dev.html',
}

def convert_div_to_link(content, cert_name, cert_link):
    """Convertit une cert-card DIV en lien cliquable"""

    # Pattern pour trouver la cert-card spécifique
    # Cherche: <div class="cert-card" ... ><div ...><img ...>...cert_name...</div>
    pattern = r'(<div class="cert-card"[^>]*>)(.*?<h3[^>]*>' + re.escape(cert_name) + r'</h3>.*?)(</div>\s*(?:</div>)?)'

    def replacement(match):
        # Convertir en lien
        opening = match.group(1).replace('<div class="cert-card"', '<a href="../../certifications/' + cert_link + '" class="cert-card"')
        content_inner = match.group(2)

        # Ajouter "View Details →" à la fin si pas déjà présent
        if 'View Details' not in content_inner:
            # Trouver le dernier <div avec exam code
            last_div_match = re.search(r'(<span[^>]*>Exam:[^<]*</span>)\s*(</div>)', content_inner)
            if last_div_match:
                content_inner = content_inner.replace(
                    last_div_match.group(0),
                    last_div_match.group(1) + '\n<span style="color: var(--accent-color); font-size: var(--text-sm); font-weight: 600;">View Details →</span>' + last_div_match.group(2)
                )

        closing = match.group(3).replace('</div>', '</a>', 1)

        return opening + content_inner + closing

    # Appliquer le remplacement
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    return new_content

def process_file(filepath):
    """Traite un fichier HTML"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        changes = 0

        # Pour chaque certification, convertir DIV en lien
        for cert_name, cert_link in CERT_LINKS.items():
            new_content = convert_div_to_link(content, cert_name, cert_link)
            if new_content != content:
                changes += 1
                content = new_content

        # Sauvegarder si modifié
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return changes
        return 0
    except Exception as e:
        print(f"✗ Erreur {filepath}: {e}")
        return 0

# Main
base_path = Path('/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/reviews/cybersecurity')

print("╔═══════════════════════════════════════════════════════════════╗")
print("║  🔗 CONVERSION DES CERTIFICATIONS EN LIENS CLIQUABLES         ║")
print("╚═══════════════════════════════════════════════════════════════╝\n")

html_files = list(base_path.glob('*.html'))
print(f"📁 Fichiers trouvés: {len(html_files)}\n")

modified_count = 0
total_changes = 0

for filepath in html_files:
    changes = process_file(filepath)
    if changes > 0:
        modified_count += 1
        total_changes += changes
        print(f"✓ {filepath.name} ({changes} certifications liées)")

print(f"\n{'═' * 65}")
print(f"✅ CONVERSION TERMINÉE")
print(f"{'═' * 65}")
print(f"Fichiers modifiés: {modified_count}")
print(f"Certifications liées: {total_changes}")
print(f"{'═' * 65}\n")
