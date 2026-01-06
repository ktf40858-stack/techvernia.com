#!/usr/bin/env python3
"""
Générateur de screenshot de terminal Juniper CLI (Junos OS)
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
    'juniper_green': '#84bd00',
    'juniper_blue': '#00a9e0',
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


# JUNIPER CLI SCREENSHOT (Junos OS)
juniper_cli_content = [
    ("admin@mist-ai-switch> configure", 'prompt'),
    ("Entering configuration mode", 'gray'),
    ("", 'text'),
    ("[edit]", 'yellow'),
    ("admin@mist-ai-switch# set system host-name mist-campus-core", 'juniper_green'),
    ("", 'text'),
    ("[edit]", 'yellow'),
    ("admin@mist-ai-switch# set interfaces ge-0/0/0 description \"Uplink to Core\"", 'juniper_green'),
    ("", 'text'),
    ("[edit]", 'yellow'),
    ("admin@mist-ai-switch# set interfaces ge-0/0/0 unit 0 family inet address 10.1.1.1/24", 'juniper_green'),
    ("", 'text'),
    ("[edit]", 'yellow'),
    ("admin@mist-ai-switch# set protocols ospf area 0.0.0.0 interface ge-0/0/0.0", 'juniper_green'),
    ("", 'text'),
    ("[edit]", 'yellow'),
    ("admin@mist-ai-switch# set routing-options static route 0.0.0.0/0 next-hop 10.1.1.254", 'juniper_green'),
    ("", 'text'),
    ("[edit]", 'yellow'),
    ("admin@mist-ai-switch# show | compare", 'juniper_blue'),
    ("[edit system]", 'text'),
    ("+   host-name mist-campus-core;", 'green'),
    ("[edit interfaces ge-0/0/0]", 'text'),
    ("+   description \"Uplink to Core\";", 'green'),
    ("+   unit 0 {", 'green'),
    ("+       family inet {", 'green'),
    ("+           address 10.1.1.1/24;", 'green'),
    ("+       }", 'green'),
    ("+   }", 'green'),
    ("[edit protocols ospf area 0.0.0.0]", 'text'),
    ("+   interface ge-0/0/0.0;", 'green'),
    ("[edit routing-options]", 'text'),
    ("+   static {", 'green'),
    ("+       route 0.0.0.0/0 next-hop 10.1.1.254;", 'green'),
    ("+   }", 'green'),
    ("", 'text'),
    ("[edit]", 'yellow'),
    ("admin@mist-ai-switch# commit check", 'juniper_blue'),
    ("configuration check succeeds", 'green'),
    ("", 'text'),
    ("[edit]", 'yellow'),
    ("admin@mist-ai-switch# commit", 'juniper_blue'),
    ("commit complete", 'green'),
    ("", 'text'),
    ("[edit]", 'yellow'),
    ("admin@mist-ai-switch# exit", 'juniper_blue'),
    ("Exiting configuration mode", 'gray'),
    ("", 'text'),
    ("admin@mist-ai-switch> show interfaces terse | match ge-0/0/0", 'prompt'),
    ("ge-0/0/0                up    up", 'green'),
    ("ge-0/0/0.0              up    up   inet     10.1.1.1/24", 'green'),
    ("", 'text'),
    ("admin@mist-ai-switch> show ospf neighbor", 'prompt'),
    ("Address          Interface              State     ID               Pri  Dead", 'text'),
    ("10.1.1.2         ge-0/0/0.0             Full      192.168.1.1      128    37", 'green'),
    ("", 'text'),
    ("admin@mist-ai-switch>", 'prompt'),
]

if __name__ == "__main__":
    print("Génération du screenshot Juniper CLI...")

    create_terminal_screenshot(
        juniper_cli_content,
        "juniper-mist.png",
        title="Juniper Mist AI - Junos CLI Configuration"
    )

    print("\n✓ Screenshot Juniper CLI créé!")
