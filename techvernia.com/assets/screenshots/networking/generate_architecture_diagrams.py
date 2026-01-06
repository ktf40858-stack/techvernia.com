#!/usr/bin/env python3
"""
Générateur de diagrammes d'architecture pour les outils networking
"""

from PIL import Image, ImageDraw, ImageFont
import math

# Couleurs
COLORS = {
    'bg': '#0d1117',
    'card_bg': '#161b22',
    'border': '#30363d',
    'text': '#c9d1d9',
    'primary': '#58a6ff',
    'success': '#3fb950',
    'warning': '#d29922',
    'purple': '#bc8cff',
    'red': '#f85149',
    'cyan': '#39d0d8',
}

def draw_rounded_rect(draw, xy, radius, fill, outline=None, width=2):
    """Dessine un rectangle avec coins arrondis"""
    x1, y1, x2, y2 = xy
    draw.rectangle([x1 + radius, y1, x2 - radius, y2], fill=fill, outline=outline, width=width)
    draw.rectangle([x1, y1 + radius, x2, y2 - radius], fill=fill, outline=outline, width=width)

    # Coins
    draw.pieslice([x1, y1, x1 + radius * 2, y1 + radius * 2], 180, 270, fill=fill, outline=outline, width=width)
    draw.pieslice([x2 - radius * 2, y1, x2, y1 + radius * 2], 270, 360, fill=fill, outline=outline, width=width)
    draw.pieslice([x1, y2 - radius * 2, x1 + radius * 2, y2], 90, 180, fill=fill, outline=outline, width=width)
    draw.pieslice([x2 - radius * 2, y2 - radius * 2, x2, y2], 0, 90, fill=fill, outline=outline, width=width)

def draw_node(draw, x, y, width, height, title, subtitle, color, font, small_font):
    """Dessine un nœud de diagramme"""
    draw_rounded_rect(draw, [x, y, x + width, y + height], 10,
                      fill=COLORS['card_bg'], outline=color, width=3)

    # Titre
    title_bbox = draw.textbbox((0, 0), title, font=font)
    title_width = title_bbox[2] - title_bbox[0]
    draw.text((x + width//2 - title_width//2, y + 15), title, fill=color, font=font)

    # Sous-titre
    if subtitle:
        sub_bbox = draw.textbbox((0, 0), subtitle, font=small_font)
        sub_width = sub_bbox[2] - sub_bbox[0]
        draw.text((x + width//2 - sub_width//2, y + 40), subtitle, fill=COLORS['text'], font=small_font)

def draw_arrow(draw, x1, y1, x2, y2, color, label=None, font=None):
    """Dessine une flèche entre deux points"""
    draw.line([x1, y1, x2, y2], fill=color, width=3)

    # Tête de flèche
    angle = math.atan2(y2 - y1, x2 - x1)
    arrow_size = 12

    left_x = x2 - arrow_size * math.cos(angle - math.pi/6)
    left_y = y2 - arrow_size * math.sin(angle - math.pi/6)
    right_x = x2 - arrow_size * math.cos(angle + math.pi/6)
    right_y = y2 - arrow_size * math.sin(angle + math.pi/6)

    draw.polygon([x2, y2, left_x, left_y, right_x, right_y], fill=color)

    # Label
    if label and font:
        mid_x, mid_y = (x1 + x2) // 2, (y1 + y2) // 2
        label_bbox = draw.textbbox((0, 0), label, font=font)
        label_width = label_bbox[2] - label_bbox[0]
        draw.rectangle([mid_x - label_width//2 - 5, mid_y - 15,
                       mid_x + label_width//2 + 5, mid_y + 5],
                      fill=COLORS['bg'])
        draw.text((mid_x - label_width//2, mid_y - 12), label, fill=color, font=font)

# DATADOG ARCHITECTURE DIAGRAM
def create_datadog_diagram():
    width, height = 1400, 800
    img = Image.new('RGB', (width, height), COLORS['bg'])
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)
        small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
        tiny_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)
    except:
        font = small_font = tiny_font = ImageFont.load_default()

    # Titre
    title = "Datadog - Unified Observability Platform"
    title_bbox = draw.textbbox((0, 0), title, font=font)
    title_width = title_bbox[2] - title_bbox[0]
    draw.text((width//2 - title_width//2, 30), title, fill=COLORS['primary'], font=font)

    # Infrastructure Layer
    draw.text((50, 100), "Infrastructure", fill=COLORS['text'], font=small_font)
    draw_node(draw, 50, 130, 180, 80, "AWS", "EC2, RDS, S3", COLORS['warning'], font, tiny_font)
    draw_node(draw, 250, 130, 180, 80, "Azure", "VMs, AKS", COLORS['cyan'], font, tiny_font)
    draw_node(draw, 450, 130, 180, 80, "Kubernetes", "Pods, Services", COLORS['success'], font, tiny_font)

    # Datadog Agent Layer
    draw.text((50, 250), "Datadog Agents", fill=COLORS['text'], font=small_font)
    draw_node(draw, 50, 280, 580, 80, "Datadog Agent", "Metrics, Traces, Logs Collection", COLORS['purple'], font, tiny_font)

    # Datadog Platform
    draw.text((50, 400), "Datadog Cloud Platform", fill=COLORS['text'], font=small_font)
    draw_node(draw, 50, 430, 180, 80, "APM", "Distributed Tracing", COLORS['primary'], font, tiny_font)
    draw_node(draw, 250, 430, 180, 80, "Logs", "Log Management", COLORS['primary'], font, tiny_font)
    draw_node(draw, 450, 430, 180, 80, "NPM", "Network Monitoring", COLORS['primary'], font, tiny_font)

    # Watchdog AI
    draw_node(draw, 680, 280, 200, 230, "Watchdog AI", "Anomaly Detection", COLORS['red'], font, tiny_font)
    draw.text((720, 320), "• Auto-detects", fill=COLORS['text'], font=tiny_font)
    draw.text((720, 345), "  anomalies", fill=COLORS['text'], font=tiny_font)
    draw.text((720, 370), "• Root cause", fill=COLORS['text'], font=tiny_font)
    draw.text((720, 395), "  analysis", fill=COLORS['text'], font=tiny_font)
    draw.text((720, 420), "• Smart alerts", fill=COLORS['text'], font=tiny_font)

    # Dashboards & Alerts
    draw_node(draw, 250, 570, 380, 80, "Dashboards & Alerts", "Visualization & Notifications", COLORS['success'], font, tiny_font)

    # Arrows
    draw_arrow(draw, 140, 210, 140, 280, COLORS['primary'], "metrics", tiny_font)
    draw_arrow(draw, 340, 210, 340, 280, COLORS['primary'], "traces", tiny_font)
    draw_arrow(draw, 540, 210, 540, 280, COLORS['primary'], "logs", tiny_font)

    draw_arrow(draw, 140, 360, 140, 430, COLORS['primary'])
    draw_arrow(draw, 340, 360, 340, 430, COLORS['primary'])
    draw_arrow(draw, 540, 360, 540, 430, COLORS['primary'])

    draw_arrow(draw, 440, 510, 440, 570, COLORS['success'])

    # Watchdog connections
    draw_arrow(draw, 630, 320, 680, 320, COLORS['red'])
    draw_arrow(draw, 780, 510, 630, 600, COLORS['red'], "alerts", tiny_font)

    img.save("datadog-architecture.png")
    print("✓ Créé: datadog-architecture.png")

# CISCO DNA CENTER DIAGRAM
def create_cisco_diagram():
    width, height = 1400, 800
    img = Image.new('RGB', (width, height), COLORS['bg'])
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)
        small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
        tiny_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)
    except:
        font = small_font = tiny_font = ImageFont.load_default()

    # Titre
    title = "Cisco DNA Center - Intent-Based Networking"
    title_bbox = draw.textbbox((0, 0), title, font=font)
    title_width = title_bbox[2] - title_bbox[0]
    draw.text((width//2 - title_width//2, 30), title, fill=COLORS['cyan'], font=font)

    # DNA Center Platform
    draw_node(draw, 500, 100, 400, 100, "Cisco DNA Center", "Network Controller & Analytics", COLORS['cyan'], font, tiny_font)

    # Intent-Based Networking
    draw.text((450, 230), "Intent-Based Network Control", fill=COLORS['text'], font=small_font)
    draw_node(draw, 200, 260, 200, 80, "Assurance", "AI Analytics", COLORS['success'], font, tiny_font)
    draw_node(draw, 450, 260, 200, 80, "Automation", "Zero Touch", COLORS['warning'], font, tiny_font)
    draw_node(draw, 700, 260, 200, 80, "Policy", "Intent Engine", COLORS['purple'], font, tiny_font)
    draw_node(draw, 950, 260, 200, 80, "Security", "Encrypted Traffic", COLORS['red'], font, tiny_font)

    # Network Infrastructure
    draw.text((50, 400), "Network Infrastructure", fill=COLORS['text'], font=small_font)
    draw_node(draw, 50, 430, 180, 80, "Campus", "Catalyst Switches", COLORS['primary'], font, tiny_font)
    draw_node(draw, 260, 430, 180, 80, "Data Center", "Nexus Switches", COLORS['primary'], font, tiny_font)
    draw_node(draw, 470, 430, 180, 80, "WAN", "SD-WAN", COLORS['primary'], font, tiny_font)
    draw_node(draw, 680, 430, 180, 80, "Wireless", "Access Points", COLORS['primary'], font, tiny_font)
    draw_node(draw, 890, 430, 180, 80, "IoT", "Connected Devices", COLORS['primary'], font, tiny_font)

    # Telemetry
    draw_node(draw, 350, 570, 700, 80, "Network Telemetry & AI Insights", "Real-time monitoring and predictive analysis", COLORS['success'], font, tiny_font)

    # Arrows
    draw_arrow(draw, 600, 200, 300, 260, COLORS['cyan'])
    draw_arrow(draw, 700, 200, 550, 260, COLORS['cyan'])
    draw_arrow(draw, 800, 200, 800, 260, COLORS['cyan'])
    draw_arrow(draw, 900, 200, 1050, 260, COLORS['cyan'])

    draw_arrow(draw, 140, 510, 500, 570, COLORS['primary'])
    draw_arrow(draw, 350, 510, 550, 570, COLORS['primary'])
    draw_arrow(draw, 560, 510, 650, 570, COLORS['primary'])
    draw_arrow(draw, 770, 510, 750, 570, COLORS['primary'])
    draw_arrow(draw, 980, 510, 850, 570, COLORS['primary'])

    # Feedback loop
    draw_arrow(draw, 1050, 600, 1200, 300, COLORS['success'], "feedback", tiny_font)
    draw_arrow(draw, 1200, 200, 900, 150, COLORS['success'])

    img.save("cisco-architecture.png")
    print("✓ Créé: cisco-architecture.png")

# PRTG DIAGRAM
def create_prtg_diagram():
    width, height = 1400, 700
    img = Image.new('RGB', (width, height), COLORS['bg'])
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)
        small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
        tiny_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)
    except:
        font = small_font = tiny_font = ImageFont.load_default()

    # Titre
    title = "PRTG Network Monitor - All-in-One Monitoring"
    title_bbox = draw.textbbox((0, 0), title, font=font)
    title_width = title_bbox[2] - title_bbox[0]
    draw.text((width//2 - title_width//2, 30), title, fill=COLORS['warning'], font=font)

    # PRTG Core Server
    draw_node(draw, 550, 100, 300, 100, "PRTG Core Server", "Central Monitoring Engine", COLORS['warning'], font, tiny_font)

    # Monitoring Methods
    draw.text((50, 250), "Monitoring Technologies", fill=COLORS['text'], font=small_font)
    draw_node(draw, 50, 280, 150, 80, "SNMP", "v1/v2c/v3", COLORS['primary'], font, tiny_font)
    draw_node(draw, 230, 280, 150, 80, "WMI", "Windows", COLORS['primary'], font, tiny_font)
    draw_node(draw, 410, 280, 150, 80, "NetFlow", "Traffic Analysis", COLORS['primary'], font, tiny_font)
    draw_node(draw, 590, 280, 150, 80, "Packet Sniffing", "Deep Inspection", COLORS['primary'], font, tiny_font)
    draw_node(draw, 770, 280, 150, 80, "HTTP/HTTPS", "Web Services", COLORS['primary'], font, tiny_font)
    draw_node(draw, 950, 280, 150, 80, "SSH/Telnet", "Custom Scripts", COLORS['primary'], font, tiny_font)
    draw_node(draw, 1130, 280, 150, 80, "IPMI", "Hardware", COLORS['primary'], font, tiny_font)

    # Monitored Devices
    draw.text((50, 420), "Monitored Infrastructure", fill=COLORS['text'], font=small_font)
    draw_node(draw, 100, 450, 200, 80, "Network Devices", "Switches, Routers", COLORS['success'], font, tiny_font)
    draw_node(draw, 350, 450, 200, 80, "Servers", "Windows, Linux", COLORS['success'], font, tiny_font)
    draw_node(draw, 600, 450, 200, 80, "Applications", "Databases, Web", COLORS['success'], font, tiny_font)
    draw_node(draw, 850, 450, 200, 80, "Virtual", "VMware, Hyper-V", COLORS['success'], font, tiny_font)
    draw_node(draw, 1100, 450, 200, 80, "Cloud", "AWS, Azure", COLORS['success'], font, tiny_font)

    # Alerts & Reporting
    draw_node(draw, 450, 580, 500, 80, "Dashboards, Maps & Alerts", "Real-time visualization and notifications", COLORS['red'], font, tiny_font)

    # Arrows
    for i, x in enumerate([125, 305, 485, 665, 845, 1025, 1205]):
        draw_arrow(draw, x, 360, 700, 200, COLORS['primary'])

    draw_arrow(draw, 200, 530, 600, 580, COLORS['success'])
    draw_arrow(draw, 450, 530, 650, 580, COLORS['success'])
    draw_arrow(draw, 700, 530, 700, 580, COLORS['success'])
    draw_arrow(draw, 950, 530, 750, 580, COLORS['success'])
    draw_arrow(draw, 1200, 530, 800, 580, COLORS['success'])

    img.save("prtg-architecture.png")
    print("✓ Créé: prtg-architecture.png")

if __name__ == "__main__":
    print("Génération des diagrammes d'architecture...")

    create_datadog_diagram()
    create_cisco_diagram()
    create_prtg_diagram()

    print("\n✓ Tous les diagrammes ont été créés!")
