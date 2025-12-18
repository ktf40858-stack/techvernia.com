#!/usr/bin/env python3
"""
Reformate toutes les 37 certifications au format CCNA
Réutilise les données de generate_remaining_cert_pages.py
"""

from pathlib import Path
import sys

# Import des données depuis le script de génération
sys.path.insert(0, str(Path(__file__).parent))

print("╔═══════════════════════════════════════════════════════════════╗")
print("║   🔄 REFORMATAGE COMPLET AU FORMAT CCNA                      ║")
print("╚═══════════════════════════════════════════════════════════════╝\n")

print("📦 Chargement du template et des fonctions...")

exec(open('generate_remaining_cert_pages.py').read(), globals())

# Continuer sera dans la suite du fichier...
print("✓ Module chargé")

