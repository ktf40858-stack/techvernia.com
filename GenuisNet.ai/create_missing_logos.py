#!/usr/bin/env python3
"""
Create all missing tool logos with brand-appropriate designs.
"""

import os

base_path = "/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai"

# Define missing logos with their brand colors
missing_logos = {
    # Writing tools
    'writing/copyai': {'color1': '#10B981', 'color2': '#059669', 'letter': 'C'},
    'writing/grammarly': {'color1': '#15C39A', 'color2': '#0D9470', 'letter': 'G'},
    'writing/quillbot': {'color1': '#00B67A', 'color2': '#008C5E', 'letter': 'Q'},
    'writing/rytr': {'color1': '#7C3AED', 'color2': '#6D28D9', 'letter': 'R'},
    'writing/wordtune': {'color1': '#0052CC', 'color2': '#003D99', 'letter': 'W'},
    'writing/writesonic': {'color1': '#8B5CF6', 'color2': '#7C3AED', 'letter': 'W'},

    # Image tools
    'image/adobe-firefly': {'color1': '#FF0000', 'color2': '#CC0000', 'letter': 'Ff'},
    'image/canva-ai': {'color1': '#00C4CC', 'color2': '#00A0B0', 'letter': 'C'},
    'image/clipdrop': {'color1': '#FF6B6B', 'color2': '#EE5A52', 'letter': 'CD'},
    'image/ideogram': {'color1': '#8B5CF6', 'color2': '#7C3AED', 'letter': 'I'},
    'image/leonardo-ai': {'color1': '#FF6B35', 'color2': '#F7931E', 'letter': 'L'},
    'image/stable-diffusion': {'color1': '#000000', 'color2': '#1F1F1F', 'letter': 'SD'},

    # Video tools
    'video/pictory': {'color1': '#FF6B35', 'color2': '#F7931E', 'letter': 'P'},

    # Cybersecurity tools
    'cybersecurity/abnormal-security': {'color1': '#FF0000', 'color2': '#CC0000', 'letter': 'A'},
    'cybersecurity/cisco-securex': {'color1': '#049FD9', 'color2': '#00BCEB', 'letter': 'C'},
    'cybersecurity/cortex-xdr': {'color1': '#FA582D', 'color2': '#FF6B35', 'letter': 'X'},
    'cybersecurity/crowdstrike': {'color1': '#E01F3D', 'color2': '#C41230', 'letter': 'CS'},
    'cybersecurity/cyberark': {'color1': '#0066CC', 'color2': '#0052A3', 'letter': 'CA'},
    'cybersecurity/cylance': {'color1': '#00A94F', 'color2': '#008C40', 'letter': 'C'},
    'cybersecurity/darktrace': {'color1': '#E74C3C', 'color2': '#C0392B', 'letter': 'DT'},
    'cybersecurity/fortinet': {'color1': '#EE3124', 'color2': '#C41E3A', 'letter': 'F'},
    'cybersecurity/ibm-qradar': {'color1': '#0F62FE', 'color2': '#0043CE', 'letter': 'Q'},
    'cybersecurity/lacework': {'color1': '#00C7B7', 'color2': '#00A896', 'letter': 'L'},
    'cybersecurity/microsoft-sentinel': {'color1': '#0078D4', 'color2': '#005A9E', 'letter': 'MS'},
    'cybersecurity/okta': {'color1': '#007DC1', 'color2': '#005E93', 'letter': 'O'},
    'cybersecurity/palo-alto-ngfw': {'color1': '#FA582D', 'color2': '#FF6B35', 'letter': 'PA'},
    'cybersecurity/qualys': {'color1': '#ED1C24', 'color2': '#C41230', 'letter': 'Q'},
    'cybersecurity/rapid7': {'color1': '#FF6B35', 'color2': '#F7931E', 'letter': 'R7'},
    'cybersecurity/sentinelone': {'color1': '#6A1B9A', 'color2': '#4A148C', 'letter': 'S1'},
    'cybersecurity/snyk': {'color1': '#4C4A73', 'color2': '#383646', 'letter': 'S'},
    'cybersecurity/splunk-security': {'color1': '#000000', 'color2': '#1A1A1A', 'letter': 'SP'},
    'cybersecurity/tenable': {'color1': '#00A7E5', 'color2': '#0086BA', 'letter': 'T'},
    'cybersecurity/vectra-ai': {'color1': '#FF6B35', 'color2': '#F7931E', 'letter': 'V'},
    'cybersecurity/wiz': {'color1': '#8B5CF6', 'color2': '#7C3AED', 'letter': 'W'},
}

def create_logo_svg(letter, color1, color2):
    """Generate SVG logo with gradient background and letter."""
    return f'''<svg width="200" height="200" viewBox="0 0 200 200" fill="none" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:{color1};stop-opacity:1" />
            <stop offset="100%" style="stop-color:{color2};stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect width="200" height="200" rx="20" fill="url(#grad)"/>
    <text x="100" y="130" font-family="Arial, sans-serif" font-size="80" font-weight="700" fill="#FFFFFF" text-anchor="middle">{letter}</text>
</svg>'''

# Create logos
print("🎨 Creating missing tool logos...\n")

created_count = 0

for path, config in missing_logos.items():
    category, filename = path.split('/')
    logo_dir = os.path.join(base_path, f"assets/images/tools/{category}")

    # Create directory if it doesn't exist
    os.makedirs(logo_dir, exist_ok=True)

    logo_path = os.path.join(logo_dir, f"{filename}.svg")

    svg_content = create_logo_svg(config['letter'], config['color1'], config['color2'])

    with open(logo_path, 'w', encoding='utf-8') as f:
        f.write(svg_content)

    created_count += 1
    print(f"✓ Created: {path}.svg")

# Fix invalid logos
invalid_logos = {
    'seo/clearscope': {'color1': '#3B82F6', 'color2': '#2563EB', 'letter': 'C'},
    'architecture/veras-ai': {'color1': '#0EA5E9', 'color2': '#0284C7', 'letter': 'V'},
    'medical/zebra-medical': {'color1': '#8B5CF6', 'color2': '#7C3AED', 'letter': 'Z'},
}

print(f"\n🔧 Fixing invalid logos...\n")

for path, config in invalid_logos.items():
    category, filename = path.split('/')
    logo_path = os.path.join(base_path, f"assets/images/tools/{category}/{filename}.svg")

    svg_content = create_logo_svg(config['letter'], config['color1'], config['color2'])

    with open(logo_path, 'w', encoding='utf-8') as f:
        f.write(svg_content)

    created_count += 1
    print(f"✓ Fixed: {path}.svg")

print(f"\n✅ Process complete!")
print(f"📊 Created/Fixed {created_count} logo files")
