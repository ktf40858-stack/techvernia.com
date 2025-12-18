#!/usr/bin/env python3
"""Trouve et corrige tous les logos corrompus"""

from pathlib import Path
import subprocess
import shutil

BASE_DIR = Path(__file__).parent
LOGOS_DIR = BASE_DIR / "assets" / "images" / "logos"
TOOLS_DIR = BASE_DIR / "assets" / "images" / "tools"

print("🔍 Recherche de logos corrompus...\n")

corrupted = []
fixed = []

# Vérifier tous les logos
for logo_file in sorted(LOGOS_DIR.glob("*")):
    if logo_file.is_file():
        result = subprocess.run(['file', str(logo_file)], capture_output=True, text=True)
        file_type = result.stdout
        
        # Si c'est un fichier HTML ou vide au lieu d'une image
        if 'HTML' in file_type or 'empty' in file_type or 'ASCII text' in file_type and 'SVG' not in file_type:
            corrupted.append(logo_file)
            print(f"❌ Corrompu: {logo_file.name}")
            print(f"   Type: {file_type.split(':')[1].strip()[:60]}")
            
            # Chercher une version correcte dans tools/
            tool_name = logo_file.stem
            
            # Chercher dans toutes les sous-catégories de tools/
            found = False
            for tools_subdir in TOOLS_DIR.glob("*"):
                if tools_subdir.is_dir():
                    # Chercher SVG d'abord, puis PNG
                    for ext in ['.svg', '.png', '.jpg']:
                        source = tools_subdir / f"{tool_name}{ext}"
                        if source.exists():
                            # Vérifier que c'est vraiment une image
                            check = subprocess.run(['file', str(source)], 
                                                  capture_output=True, text=True)
                            if any(x in check.stdout for x in ['PNG', 'JPEG', 'SVG', 'image']):
                                # Copier
                                shutil.copy(source, LOGOS_DIR / f"{tool_name}{ext}")
                                print(f"   ✅ Corrigé depuis: {source.relative_to(BASE_DIR)}")
                                fixed.append(tool_name)
                                found = True
                                break
                if found:
                    break
            
            if not found:
                print(f"   ⚠️  Aucun remplacement trouvé")
            print()

print("="*70)
print("📊 RÉSUMÉ")
print("="*70)
print(f"❌ Logos corrompus trouvés: {len(corrupted)}")
print(f"✅ Logos corrigés: {len(fixed)}")
print(f"⚠️  Non corrigés: {len(corrupted) - len(fixed)}")

if fixed:
    print(f"\n✅ Logos corrigés:")
    for name in fixed:
        print(f"   - {name}")

print("\n✨ Terminé!")

