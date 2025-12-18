#!/bin/bash
# Crée toutes les pages de certification manquantes en générant du HTML simple

cd "/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/certifications"

# Liste des certifications à créer (celles qui n'existent pas encore)
declare -A CERTS=(
    ["fortinet-nse8"]="NSE 8 - Written Exam|Master Level|Fortinet|#EE3124|NSE8|400"
    ["paloalto-pccet"]="PCCET|Entry-Level Technician|Palo Alto Networks|#FA582D|PCCET|100"
    ["paloalto-pccsa"]="PCCSA|Cybersecurity Associate|Palo Alto Networks|#FA582D|PCCSA|200"
    ["paloalto-pccse"]="PCCSE|Cybersecurity Engineer|Palo Alto Networks|#FA582D|PCCSE|250"
    ["paloalto-pcsae"]="PCSAE|Security Automation Engineer|Palo Alto Networks|#FA582D|PCSAE|250"
    ["microsoft-sc900"]="SC-900|Security Fundamentals|Microsoft|#00A4EF|SC-900|99"
    ["microsoft-sc300"]="SC-300|Identity Administrator|Microsoft|#00A4EF|SC-300|165"
    ["microsoft-sc400"]="SC-400|Information Protection|Microsoft|#00A4EF|SC-400|165"
    ["microsoft-az500"]="AZ-500|Azure Security|Microsoft|#00A4EF|AZ-500|165"
    ["cisco-cyberops"]="CyberOps Associate|Associate Level|Cisco|#1BA0D7|200-201|300"
    ["cisco-ccnp-security"]="CCNP Security|Professional Level|Cisco|#1BA0D7|350-701|400"
    ["cisco-ccie-security"]="CCIE Security|Expert Level|Cisco|#1BA0D7|CCIE|1600"
    ["crowdstrike-ccfr"]="CCFR|Falcon Responder|CrowdStrike|#E01F3D|CCFR|Sales"
    ["crowdstrike-ccfh"]="CCFH|Falcon Hunter|CrowdStrike|#E01F3D|CCFH|Sales"
    ["ibm-qradar-siem"]="QRadar SIEM|Specialist|IBM|#0F62FE|C1000-142|200"
    ["ibm-qradar-analyst"]="QRadar Analyst|Associate|IBM|#0F62FE|C1000-123|200"
    ["cyberark-defender"]="CyberArk Defender|Defender|CyberArk|#0066B1|PAM-DEF|Varies"
    ["cyberark-sentry"]="CyberArk Sentry|Sentry|CyberArk|#0066B1|PAM-SEN|Varies"
    ["cyberark-guardian"]="CyberArk Guardian|Guardian|CyberArk|#0066B1|PAM-CDE|Varies"
    ["okta-professional"]="Okta Professional|Professional|Okta|#007DC1|OCP|Varies"
    ["okta-administrator"]="Okta Administrator|Administrator|Okta|#007DC1|OCA|Varies"
    ["okta-consultant"]="Okta Consultant|Consultant|Okta|#007DC1|OCC|Varies"
    ["okta-developer"]="Okta Developer|Developer|Okta|#007DC1|OCD|Varies"
    ["qualys-vmdr"]="Qualys VMDR|Specialist|Qualys|#ED2E27|VMDR|FREE"
    ["qualys-was"]="Qualys WAS|Specialist|Qualys|#ED2E27|WAS|FREE"
    ["rapid7-insightvm"]="Rapid7 InsightVM|Administrator|Rapid7|#FF6700|InsightVM|FREE"
    ["rapid7-insightidr"]="Rapid7 InsightIDR|Administrator|Rapid7|#FF6700|InsightIDR|FREE"
    ["tenable-nessus"]="Nessus Certified|Professional|Tenable|#00B388|Nessus-Pro|Varies"
    ["darktrace-engineer"]="Darktrace Engineer|Engineer|Darktrace|#E94E1B|DCE|Partner"
    ["sentinelone-core"]="SentinelOne Core|Administrator|SentinelOne|#6A1B9A|S1-Core|Customer"
    ["sentinelone-advanced"]="SentinelOne Advanced|Advanced|SentinelOne|#6A1B9A|S1-Adv|Customer"
    ["sophos-engineer"]="Sophos Engineer|Engineer|Sophos|#00BFFF|SCE|Partner"
    ["sophos-architect"]="Sophos Architect|Architect|Sophos|#00BFFF|SCA|Partner"
    ["trendmicro-professional"]="Trend Micro Pro|Professional|Trend Micro|#D71920|TMCP|Varies"
    ["trendmicro-expert"]="Trend Micro Expert|Expert|Trend Micro|#D71920|TMCE|Varies"
    ["splunk-es-admin"]="Splunk ES Admin|Administrator|Splunk|#FF6B00|SPLK-3003|250"
    ["splunk-soar-dev"]="Splunk SOAR Dev|Developer|Splunk|#FF6B00|SPLK-2003|250"
)

echo "Création des pages de certification manquantes..."
count=0

for cert_id in "${!CERTS[@]}"; do
    if [ ! -f "${cert_id}.html" ]; then
        IFS='|' read -r name level vendor color exam_code cost <<< "${CERTS[$cert_id]}"

        # Note: Le HTML sera créé par Python car trop complexe pour bash
        echo "⏳ ${cert_id} (sera créé par Python)"
        ((count++))
    else
        echo "✓ ${cert_id}.html existe déjà"
    fi
done

echo ""
echo "$count pages à créer"
