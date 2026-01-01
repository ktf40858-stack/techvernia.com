#!/usr/bin/env python3
"""
Générateur de screenshots de terminal stylisés pour les outils networking
"""

from PIL import Image, ImageDraw, ImageFont
import textwrap

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


# TERRAFORM SCREENSHOT
terraform_content = [
    ("$ terraform plan", 'prompt'),
    ("", 'text'),
    ("Terraform used the selected providers to generate the following execution", 'text'),
    ("plan. Resource actions are indicated with the following symbols:", 'text'),
    ("  + create", 'green'),
    ("  ~ update in-place", 'yellow'),
    ("  - destroy", 'red'),
    ("", 'text'),
    ("Terraform will perform the following actions:", 'text'),
    ("", 'text'),
    ("  # aws_vpc.main will be created", 'green'),
    ("  + resource \"aws_vpc\" \"main\" {", 'text'),
    ("      + cidr_block                       = \"10.0.0.0/16\"", 'blue'),
    ("      + enable_dns_hostnames             = true", 'blue'),
    ("      + enable_dns_support               = true", 'blue'),
    ("      + id                               = (known after apply)", 'gray'),
    ("      + instance_tenancy                 = \"default\"", 'blue'),
    ("    }", 'text'),
    ("", 'text'),
    ("  # aws_subnet.public[0] will be created", 'green'),
    ("  + resource \"aws_subnet\" \"public\" {", 'text'),
    ("      + availability_zone               = \"us-east-1a\"", 'blue'),
    ("      + cidr_block                      = \"10.0.1.0/24\"", 'blue'),
    ("      + vpc_id                          = (known after apply)", 'gray'),
    ("    }", 'text'),
    ("", 'text'),
    ("Plan: 2 to add, 0 to change, 0 to destroy.", 'green'),
]

# ANSIBLE SCREENSHOT
ansible_content = [
    ("$ ansible-playbook -i inventory deploy-web.yml", 'prompt'),
    ("", 'text'),
    ("PLAY [Deploy Web Application] *********************************************", 'purple'),
    ("", 'text'),
    ("TASK [Gathering Facts] ****************************************************", 'blue'),
    ("ok: [web-server-1]", 'green'),
    ("ok: [web-server-2]", 'green'),
    ("", 'text'),
    ("TASK [Install Nginx] ******************************************************", 'blue'),
    ("changed: [web-server-1]", 'yellow'),
    ("changed: [web-server-2]", 'yellow'),
    ("", 'text'),
    ("TASK [Copy application files] *********************************************", 'blue'),
    ("ok: [web-server-1]", 'green'),
    ("changed: [web-server-2]", 'yellow'),
    ("", 'text'),
    ("TASK [Start Nginx service] ************************************************", 'blue'),
    ("ok: [web-server-1]", 'green'),
    ("ok: [web-server-2]", 'green'),
    ("", 'text'),
    ("PLAY RECAP ****************************************************************", 'purple'),
    ("web-server-1     : ok=4    changed=1    unreachable=0    failed=0", 'green'),
    ("web-server-2     : ok=4    changed=2    unreachable=0    failed=0", 'green'),
]

# ZABBIX SCREENSHOT
zabbix_content = [
    ("$ zabbix_get -s 192.168.1.10 -k system.cpu.load[percpu,avg1]", 'prompt'),
    ("0.45", 'green'),
    ("", 'text'),
    ("$ zabbix_sender -z zabbix.example.com -s \"Web Server\" -k ping -o 1", 'prompt'),
    ("info from server: \"processed: 1; failed: 0; total: 1; seconds spent: 0.000123\"", 'blue'),
    ("sent: 1; skipped: 0; total: 1", 'green'),
    ("", 'text'),
    ("=== Active Alerts ===", 'yellow'),
    ("", 'text'),
    ("[CRITICAL] High CPU usage on web-server-1 (95%)", 'red'),
    ("[WARNING]  Disk space low on db-server-1 (85%)", 'yellow'),
    ("[INFO]     Network latency increased on router-core (45ms)", 'blue'),
    ("", 'text'),
    ("=== Network Performance ===", 'yellow'),
    ("", 'text'),
    ("Interface eth0:", 'text'),
    ("  ├─ In:  1.2 Gbps", 'green'),
    ("  ├─ Out: 850 Mbps", 'green'),
    ("  └─ Errors: 0", 'green'),
    ("", 'text'),
    ("Monitored hosts: 247 | Problems: 2 | Avg response: 12ms", 'blue'),
]

if __name__ == "__main__":
    print("Génération des screenshots de terminal...")

    create_terminal_screenshot(
        terraform_content,
        "terraform.png",
        title="Terraform - Infrastructure as Code"
    )

    create_terminal_screenshot(
        ansible_content,
        "ansible.png",
        title="Ansible AWX - Automation Playbook"
    )

    create_terminal_screenshot(
        zabbix_content,
        "zabbix.png",
        title="Zabbix - Network Monitoring"
    )

    print("\n✓ Tous les screenshots ont été créés!")
