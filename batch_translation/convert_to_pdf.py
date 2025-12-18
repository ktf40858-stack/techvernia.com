#!/usr/bin/env python3
"""
Convertit le fichier HTML en PDF en utilisant le navigateur
"""
import subprocess
import os
from pathlib import Path

html_file = Path(__file__).parent / "GUIDE_TRADUCTION_ESPAGNOL.html"
pdf_file = Path(__file__).parent / "GUIDE_TRADUCTION_ESPAGNOL.pdf"

print("🔄 Conversion HTML → PDF en cours...")
print(f"📄 Source: {html_file}")
print(f"📄 Destination: {pdf_file}")
print()

# Ouvrir Firefox et imprimer en PDF
print("📖 Ouverture du fichier HTML dans Firefox...")
print()
print("=" * 70)
print("INSTRUCTIONS:")
print("=" * 70)
print("1. Firefox va s'ouvrir avec le guide de traduction")
print("2. Appuyez sur Ctrl+P (ou Cmd+P sur Mac)")
print("3. Sélectionnez 'Enregistrer en PDF' comme imprimante")
print("4. Cliquez sur 'Enregistrer'")
print("5. Sauvegardez le PDF dans le dossier:")
print(f"   {pdf_file.parent}")
print("6. Nommez le fichier: GUIDE_TRADUCTION_ESPAGNOL.pdf")
print("=" * 70)
print()

# Ouvrir dans Firefox
subprocess.run(['firefox', str(html_file)])
