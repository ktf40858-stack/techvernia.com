#!/usr/bin/env python3
"""
Générateur de screenshot de terminal Cisco CLI
"""

from PIL import Image, ImageDraw, ImageFont

# Couleurs du thème dark terminal
COLORS = {
    'bg': '#1e1e1e',
    'text': '#d4d4d4',
    'green': '#4ec9b0',
    'blue': '#569cd6',
    'yellow': '#dcdcaa',
    'orange': '#ce9178',
    'purple': '#c586c0',
    'red': '#f48771',
    'gray': '#808080',
    'prompt': '#00ff00',
    'cisco_blue': '#0099cc',
}

def create_terminal_screenshot(content_lines, filename, width=1200, title="Terminal"):
    """
    Crée un screenshot de terminal stylisé

    Args:
        content_lines: Liste de tuples (texte, couleur)
        filename: Nom du fichier de sortie
        width: Largeur de l'image
        title: Titre de la fenêtre
    """
    # Calcul de la hauteur
    line_height = 24
    padding = 40
    title_bar_height = 40
    height = title_bar_height + (len(content_lines) * line_height) + (padding * 2)

    # Créer l'image
    img = Image.new('RGB', (width, height), COLORS['bg'])
    draw = ImageDraw.Draw(img)

    # Dessiner la barre de titre (style macOS)
    draw.rectangle([(0, 0), (width, title_bar_height)], fill='#2d2d2d')

    # Boutons macOS
    button_y = title_bar_height // 2
    draw.ellipse([(15, button_y - 6), (27, button_y + 6)], fill='#ff5f56')
    draw.ellipse([(35, button_y - 6), (47, button_y + 6)], fill='#ffbd2e')
    draw.ellipse([(55, button_y - 6), (67, button_y + 6)], fill='#27c93f')

    # Titre
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf", 14)
    except:
        title_font = ImageFont.load_default()

    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    draw.text((width // 2 - title_width // 2, 12), title, fill='#999', font=title_font)

    # Dessiner le contenu
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 14)
    except:
        font = ImageFont.load_default()

    y = title_bar_height + padding
    for line, color in content_lines:
        draw.text((padding, y), line, fill=COLORS.get(color, COLORS['text']), font=font)
        y += line_height

    # Sauvegarder
    img.save(filename)
    print(f"✓ Créé: {filename}")


# CISCO CLI SCREENSHOT
cisco_cli_content = [
    ("Router>enable", 'prompt'),
    ("Router#configure terminal", 'prompt'),
    ("Enter configuration commands, one per line. End with CNTL/Z.", 'gray'),
    ("", 'text'),
    ("Router(config)#hostname DNA-Center-Core", 'cisco_blue'),
    ("DNA-Center-Core(config)#", 'cisco_blue'),
    ("", 'text'),
    ("DNA-Center-Core(config)#interface GigabitEthernet0/0/1", 'cisco_blue'),
    ("DNA-Center-Core(config-if)#description ** Uplink to Distribution **", 'cisco_blue'),
    ("DNA-Center-Core(config-if)#ip address 10.1.1.1 255.255.255.0", 'cisco_blue'),
    ("DNA-Center-Core(config-if)#no shutdown", 'cisco_blue'),
    ("", 'text'),
    ("%LINK-5-CHANGED: Interface GigabitEthernet0/0/1, changed state to up", 'green'),
    ("%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/0/1,", 'green'),
    ("changed state to up", 'green'),
    ("", 'text'),
    ("DNA-Center-Core(config-if)#exit", 'cisco_blue'),
    ("DNA-Center-Core(config)#", 'cisco_blue'),
    ("", 'text'),
    ("DNA-Center-Core(config)#ip routing", 'cisco_blue'),
    ("DNA-Center-Core(config)#router ospf 1", 'cisco_blue'),
    ("DNA-Center-Core(config-router)#network 10.1.1.0 0.0.0.255 area 0", 'cisco_blue'),
    ("DNA-Center-Core(config-router)#exit", 'cisco_blue'),
    ("", 'text'),
    ("DNA-Center-Core(config)#end", 'cisco_blue'),
    ("DNA-Center-Core#", 'cisco_blue'),
    ("", 'text'),
    ("%SYS-5-CONFIG_I: Configured from console by console", 'yellow'),
    ("", 'text'),
    ("DNA-Center-Core#show ip interface brief", 'prompt'),
    ("Interface              IP-Address      OK? Method Status                Protocol", 'text'),
    ("GigabitEthernet0/0/0   unassigned      YES unset  administratively down down", 'gray'),
    ("GigabitEthernet0/0/1   10.1.1.1        YES manual up                    up", 'green'),
    ("GigabitEthernet0/0/2   unassigned      YES unset  administratively down down", 'gray'),
    ("Vlan1                  unassigned      YES unset  administratively down down", 'gray'),
    ("", 'text'),
    ("DNA-Center-Core#show running-config | include hostname", 'prompt'),
    ("hostname DNA-Center-Core", 'cisco_blue'),
    ("", 'text'),
    ("DNA-Center-Core#", 'cisco_blue'),
]

if __name__ == "__main__":
    print("Génération du screenshot Cisco CLI...")

    create_terminal_screenshot(
        cisco_cli_content,
        "cisco-ai.png",
        title="Cisco DNA Center - CLI Configuration"
    )

    print("\n✓ Screenshot Cisco CLI créé!")
