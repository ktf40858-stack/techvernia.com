from pathlib import Path
import subprocess

logos_dir = Path("assets/images/logos")

print("🔍 Vérification de tous les logos...\n")

corrupted = []
valid = 0

for logo_file in sorted(logos_dir.glob("*")):
    if logo_file.is_file():
        result = subprocess.run(['file', str(logo_file)], capture_output=True, text=True)
        file_type = result.stdout
        
        if not any(x in file_type for x in ['PNG', 'SVG', 'JPEG', 'image', 'data']):
            corrupted.append((logo_file.name, file_type.split(':')[1].strip()))
        else:
            valid += 1

print(f"✅ Logos valides: {valid}")
print(f"⚠️  Logos corrompus: {len(corrupted)}\n")

if corrupted:
    print("📋 FICHIERS À CORRIGER:")
    for name, ftype in corrupted:
        print(f"  ⚠️  {name}: {ftype}")

