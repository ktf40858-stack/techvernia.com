#!/bin/bash
# Téléchargement des vrais logos Palo Alto Networks depuis Credly

echo "Téléchargement des logos officiels Palo Alto Networks..."

# PCNSE (déjà téléchargé)
wget -q --timeout=10 "https://images.credly.com/size/680x680/images/a7179299-0c6e-4327-a27d-ea5853a1ab55/pan_pcnse_digital-badge_sharing-logo-2048x2048.png" -O paloalto-pcnse.png && echo "✓ PCNSE" || echo "✗ PCNSE"

# PCNSA
wget -q --timeout=10 "https://images.credly.com/size/680x680/images/d8ec8dd8-d90c-4216-977f-c76b1f2d6e18/image.png" -O paloalto-pcnsa.png && echo "✓ PCNSA" || echo "✗ PCNSA"

# PCCET  
wget -q --timeout=10 "https://images.credly.com/size/680x680/images/9c7c26c0-8b41-4e1d-8a44-b46ee48a3a90/image.png" -O paloalto-pccet.png && echo "✓ PCCET" || echo "✗ PCCET"

# PCSAE
wget -q --timeout=10 "https://images.credly.com/size/680x680/images/97ca0b3b-85cf-4e3b-85d0-ac2aa92c86d1/image.png" -O paloalto-pcsae.png && echo "✓ PCSAE" || echo "✗ PCSAE"

# PCCSE (Prisma Cloud)
wget -q --timeout=10 "https://images.credly.com/size/680x680/images/2a4063bb-6c00-4908-bc40-fae38b25f8f1/image.png" -O paloalto-pccse.png && echo "✓ PCCSE" || echo "✗ PCCSE"

# PCCSA
wget -q --timeout=10 "https://images.credly.com/size/680x680/images/3c5d55f5-55e3-4c4c-b27b-0c4e176e1832/image.png" -O paloalto-pccsa.png && echo "✓ PCCSA" || echo "✗ PCCSA"

echo ""
echo "Vérification des fichiers téléchargés:"
ls -lh paloalto-*.png | grep -v official | wc -l
