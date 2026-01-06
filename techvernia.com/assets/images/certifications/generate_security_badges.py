#!/usr/bin/env python3
"""
Générateur de badges de certification pour cybersécurité
Format professionnel avec logos et couleurs de marque
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Couleurs des marques
BRAND_COLORS = {
    'fortinet': '#EE3124',
    'paloalto': '#FA582D',
    'microsoft': '#00A4EF',
    'cisco': '#1BA0D7',
    'crowdstrike': '#E01F3D',
    'ibm': '#0F62FE',
    'cyberark': '#0066B1',
    'okta': '#007DC1',
    'qualys': '#ED2E27',
    'rapid7': '#FF6700',
    'tenable': '#00B388',
    'darktrace': '#E94E1B',
    'sentinelone': '#6A1B9A',
    'sophos': '#00BFFF',
    'trendmicro': '#D71920',
    'splunk': '#FF6B00',
}

def create_cert_badge(cert_name, brand_color, filename, level="Professional"):
    """
    Crée un badge de certification circulaire professionnel

    Args:
        cert_name: Nom de la certification
        brand_color: Couleur de la marque (hex)
        filename: Nom du fichier de sortie
        level: Niveau de la certification
    """
    size = 400
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Cercle extérieur (bordure)
    draw.ellipse([10, 10, size-10, size-10], fill=brand_color)

    # Cercle intérieur blanc
    draw.ellipse([25, 25, size-25, size-25], fill='white')

    # Cercle central coloré
    draw.ellipse([60, 60, size-60, size-60], fill=brand_color)

    # Étoile/Badge au centre
    center = size // 2
    star_size = 80

    # Dessiner un badge simplifié
    badge_points = []
    for i in range(8):
        angle = i * 45
        import math
        if i % 2 == 0:
            r = star_size
        else:
            r = star_size * 0.5
        x = center + r * math.cos(math.radians(angle - 90))
        y = center + r * math.sin(math.radians(angle - 90))
        badge_points.append((x, y))

    draw.polygon(badge_points, fill='white', outline='white')

    # Texte sur le cercle
    try:
        font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
        font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
    except:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # Texte du nom (en haut)
    name_lines = cert_name.split('\n')
    y_offset = 50
    for line in name_lines:
        bbox = draw.textbbox((0, 0), line, font=font_large)
        text_width = bbox[2] - bbox[0]
        draw.text((center - text_width // 2, y_offset), line, fill='white', font=font_large)
        y_offset += 45

    # Niveau (en bas)
    bbox = draw.textbbox((0, 0), level, font=font_small)
    text_width = bbox[2] - bbox[0]
    draw.text((center - text_width // 2, size - 80), level, fill='white', font=font_small)

    # Badge "Certified"
    certified_text = "CERTIFIED"
    bbox = draw.textbbox((0, 0), certified_text, font=font_small)
    text_width = bbox[2] - bbox[0]
    draw.text((center - text_width // 2, size - 110), certified_text, fill=brand_color, font=font_small)

    # Sauvegarder
    img.save(filename, 'PNG')
    print(f"✓ {filename}")

# Créer tous les badges
print("Génération des badges de certification cybersecurity...\n")

# Fortinet NSE
create_cert_badge("NSE 4", BRAND_COLORS['fortinet'], "fortinet-nse4.png", "Professional")
create_cert_badge("NSE 7", BRAND_COLORS['fortinet'], "fortinet-nse7.png", "Expert")
create_cert_badge("NSE 8", BRAND_COLORS['fortinet'], "fortinet-nse8.png", "Master")

# Palo Alto Networks
create_cert_badge("PCNSA", BRAND_COLORS['paloalto'], "paloalto-pcnsa.png", "Administrator")
create_cert_badge("PCNSE", BRAND_COLORS['paloalto'], "paloalto-pcnse.png", "Engineer")
create_cert_badge("PCCSA", BRAND_COLORS['paloalto'], "paloalto-pccsa.png", "Associate")
create_cert_badge("PCCSE", BRAND_COLORS['paloalto'], "paloalto-pccse.png", "Engineer")
create_cert_badge("PCSAE", BRAND_COLORS['paloalto'], "paloalto-pcsae.png", "Automation")
create_cert_badge("PCCET", BRAND_COLORS['paloalto'], "paloalto-pccet.png", "Entry Level")

# Microsoft Security
create_cert_badge("SC-200", BRAND_COLORS['microsoft'], "microsoft-sc200.png", "Security Analyst")
create_cert_badge("SC-300", BRAND_COLORS['microsoft'], "microsoft-sc300.png", "Identity Admin")
create_cert_badge("SC-400", BRAND_COLORS['microsoft'], "microsoft-sc400.png", "Info Protection")
create_cert_badge("SC-900", BRAND_COLORS['microsoft'], "microsoft-sc900.png", "Fundamentals")
create_cert_badge("AZ-500", BRAND_COLORS['microsoft'], "microsoft-az500.png", "Azure Security")
create_cert_badge("MS-500", BRAND_COLORS['microsoft'], "microsoft-ms500.png", "M365 Security")

# Cisco Security
create_cert_badge("CyberOps\nAssociate", BRAND_COLORS['cisco'], "cisco-cyberops.png", "Associate")
create_cert_badge("CCNP\nSecurity", BRAND_COLORS['cisco'], "cisco-ccnp-security.png", "Professional")
create_cert_badge("CCIE\nSecurity", BRAND_COLORS['cisco'], "cisco-ccie-security.png", "Expert")

# CrowdStrike
create_cert_badge("CCFA", BRAND_COLORS['crowdstrike'], "crowdstrike-ccfa.png", "Administrator")
create_cert_badge("CCFR", BRAND_COLORS['crowdstrike'], "crowdstrike-ccfr.png", "Responder")
create_cert_badge("CCFH", BRAND_COLORS['crowdstrike'], "crowdstrike-ccfh.png", "Hunter")

# IBM QRadar
create_cert_badge("QRadar\nSIEM", BRAND_COLORS['ibm'], "ibm-qradar-siem.png", "Specialist")
create_cert_badge("QRadar\nAnalyst", BRAND_COLORS['ibm'], "ibm-qradar-analyst.png", "Associate")

# CyberArk
create_cert_badge("CyberArk\nDefender", BRAND_COLORS['cyberark'], "cyberark-defender.png", "Defender")
create_cert_badge("CyberArk\nSentry", BRAND_COLORS['cyberark'], "cyberark-sentry.png", "Sentry")
create_cert_badge("CyberArk\nGuardian", BRAND_COLORS['cyberark'], "cyberark-guardian.png", "Guardian")
create_cert_badge("CyberArk\nTrustee", BRAND_COLORS['cyberark'], "cyberark-trustee.png", "Trustee")

# Okta
create_cert_badge("Okta\nProfessional", BRAND_COLORS['okta'], "okta-professional.png", "Professional")
create_cert_badge("Okta\nAdmin", BRAND_COLORS['okta'], "okta-administrator.png", "Administrator")
create_cert_badge("Okta\nConsultant", BRAND_COLORS['okta'], "okta-consultant.png", "Consultant")
create_cert_badge("Okta\nDeveloper", BRAND_COLORS['okta'], "okta-developer.png", "Developer")

# Qualys
create_cert_badge("Qualys\nVMDR", BRAND_COLORS['qualys'], "qualys-vmdr.png", "Specialist")
create_cert_badge("Qualys\nWAS", BRAND_COLORS['qualys'], "qualys-was.png", "Specialist")

# Rapid7
create_cert_badge("Rapid7\nInsightVM", BRAND_COLORS['rapid7'], "rapid7-insightvm.png", "Administrator")
create_cert_badge("Rapid7\nInsightIDR", BRAND_COLORS['rapid7'], "rapid7-insightidr.png", "Administrator")

# Tenable
create_cert_badge("Nessus\nCertified", BRAND_COLORS['tenable'], "tenable-nessus.png", "Specialist")

# Darktrace
create_cert_badge("Darktrace\nEngineer", BRAND_COLORS['darktrace'], "darktrace-engineer.png", "Engineer")

# SentinelOne
create_cert_badge("SentinelOne\nCore Admin", BRAND_COLORS['sentinelone'], "sentinelone-core.png", "Administrator")
create_cert_badge("SentinelOne\nAdvanced", BRAND_COLORS['sentinelone'], "sentinelone-advanced.png", "Advanced")

# Sophos
create_cert_badge("Sophos\nEngineer", BRAND_COLORS['sophos'], "sophos-engineer.png", "Engineer")
create_cert_badge("Sophos\nArchitect", BRAND_COLORS['sophos'], "sophos-architect.png", "Architect")

# Trend Micro
create_cert_badge("Trend Micro\nProfessional", BRAND_COLORS['trendmicro'], "trendmicro-professional.png", "Professional")
create_cert_badge("Trend Micro\nExpert", BRAND_COLORS['trendmicro'], "trendmicro-expert.png", "Expert")

# Splunk (si manquant)
create_cert_badge("Splunk\nES Admin", BRAND_COLORS['splunk'], "splunk-es-admin.png", "Administrator")
create_cert_badge("Splunk\nSOAR Dev", BRAND_COLORS['splunk'], "splunk-soar-dev.png", "Developer")

print("\n✓ Tous les badges générés avec succès!")
