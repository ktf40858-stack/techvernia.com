#!/usr/bin/env python3
"""
Créer des badges Palo Alto Networks au style officiel
Rectangulaires oranges avec le logo officiel Palo Alto
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Couleur officielle Palo Alto Networks
PALOALTO_ORANGE = '#FA582D'

def create_paloalto_badge(cert_code, output_file):
    """
    Crée un badge style Palo Alto Networks officiel
    Format: Rectangle orange avec logo et code certification
    """

    # Dimensions (format carré pour compatibilité)
    width, height = 2048, 2048

    # Créer l'image avec fond orange
    img = Image.new('RGB', (width, height), PALOALTO_ORANGE)
    draw = ImageDraw.Draw(img)

    # Charger les fonts
    try:
        font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 280)
        font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 80)
    except:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # Dessiner "paloalto" en haut (style officiel)
    # Logo simplifié: trois barres parallèles + texte
    bar_width = 80
    bar_spacing = 30
    bar_height = 120
    start_x = 100
    start_y = 200

    # Trois barres blanches inclinées (logo Palo Alto simplifié)
    for i in range(3):
        x = start_x + (i * (bar_width + bar_spacing))
        points = [
            (x, start_y),
            (x + bar_width, start_y - 40),
            (x + bar_width, start_y - 40 + bar_height),
            (x, start_y + bar_height)
        ]
        draw.polygon(points, fill='white')

    # Texte "paloalto"
    company_text = "paloalto"
    bbox = draw.textbbox((0, 0), company_text, font=font_small)
    text_width = bbox[2] - bbox[0]
    text_x = start_x + 300
    text_y = start_y + 20
    draw.text((text_x, text_y), company_text, fill='white', font=font_small)

    # Texte "NETWORKS" (plus petit)
    try:
        font_tiny = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40)
    except:
        font_tiny = font_small

    networks_text = "NETWORKS"
    bbox = draw.textbbox((0, 0), networks_text, font=font_tiny)
    networks_width = bbox[2] - bbox[0]
    draw.text((text_x + 350, text_y + 55), networks_text, fill='white', font=font_tiny)

    # Code de certification au centre (GRAND)
    cert_bbox = draw.textbbox((0, 0), cert_code, font=font_large)
    cert_width = cert_bbox[2] - cert_bbox[0]
    cert_height = cert_bbox[3] - cert_bbox[1]
    cert_x = (width - cert_width) // 2
    cert_y = (height - cert_height) // 2 + 200

    draw.text((cert_x, cert_y), cert_code, fill='white', font=font_large)

    # Sauvegarder
    img.save(output_file, 'PNG', quality=95)
    print(f"✓ {output_file}")

# Créer tous les badges Palo Alto Networks
badges = {
    'paloalto-pcnsa.png': 'PCNSA',
    'paloalto-pccet.png': 'PCCET',
    'paloalto-pccsa.png': 'PCCSA',
    'paloalto-pccse.png': 'PCCSE',
}

print("Création des badges Palo Alto Networks style officiel...\n")

for filename, code in badges.items():
    create_paloalto_badge(code, filename)

print("\n✓ Tous les badges Palo Alto créés!")
print("Note: PCNSE et PCSAE sont déjà téléchargés depuis Credly")
