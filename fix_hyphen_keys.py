#!/usr/bin/env python3
"""
Correction URGENTE: Corriger les noms de clés IMAGE dans i18n.js
Les clés ont été créées sans tirets mais les HTML utilisent des tirets
"""
import re

print("╔══════════════════════════════════════════════════════════╗")
print("║   CORRECTION DES NOMS DE CLÉS IMAGE (TIRETS MANQUANTS)  ║")
print("╚══════════════════════════════════════════════════════════╝")
print()

# Mapping des noms d'outils : format_sans_tiret → format_avec_tiret
tool_mappings = {
    'adobefirefly': 'adobe-firefly',
    'canvaai': 'canva-ai',
    'dalle3': 'dall-e-3',
    'leonardoai': 'leonardo-ai',
    'stablediffusion': 'stable-diffusion',
}

print("📋 Mappings à appliquer:")
for old, new in tool_mappings.items():
    print(f"  review.{old}.* → review.{new}.*")
print()

# Lire i18n.js
print("📖 Lecture de i18n.js...")
with open('GenuisNet.ai/js/i18n.js', 'r', encoding='utf-8') as f:
    content = f.read()

original_size = len(content)

# Créer backup
backup_file = 'GenuisNet.ai/js/i18n.js.backup-before-hyphen-fix'
with open(backup_file, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"✓ Backup créé: {backup_file}")
print()

# Remplacer chaque mapping dans toutes les langues
total_replacements = 0

for old_name, new_name in tool_mappings.items():
    # Pattern pour capturer "review.{old_name}.
    pattern = rf'"(review)\.({old_name})\.'
    replacement = r'"\1.' + new_name + r'.'

    count = len(re.findall(pattern, content))
    if count > 0:
        content = re.sub(pattern, replacement, content)
        total_replacements += count
        print(f"  ✓ {old_name} → {new_name}: {count} occurrences")
    else:
        print(f"  - {old_name}: Aucune occurrence trouvée")

print()
print(f"📊 Total: {total_replacements} clés renommées")

# Sauvegarder
with open('GenuisNet.ai/js/i18n.js', 'w', encoding='utf-8') as f:
    f.write(content)

new_size = len(content)
print(f"✓ Fichier mis à jour ({original_size} → {new_size} octets)")

# Vérifier syntaxe
print()
print("🔍 Vérification de la syntaxe JavaScript...")
import subprocess
result = subprocess.run(
    ['node', '-c', 'GenuisNet.ai/js/i18n.js'],
    capture_output=True,
    text=True
)

if result.returncode == 0:
    print("✅ Syntaxe JavaScript valide!")
else:
    print(f"❌ Erreur de syntaxe:\n{result.stderr}")
    print("   Restauration du backup...")
    with open(backup_file, 'r', encoding='utf-8') as f:
        original = f.read()
    with open('GenuisNet.ai/js/i18n.js', 'w', encoding='utf-8') as f:
        f.write(original)
    print("   Backup restauré")
    exit(1)

print()
print("="*60)
print("✅ CORRECTION DES TIRETS TERMINÉE!")
print(f"🔧 {total_replacements} clés renommées dans toutes les langues")
print()
print("🧪 TESTER MAINTENANT:")
print("   1. Ouvrir GenuisNet.ai/pages/reviews/image/adobe-firefly.html")
print("   2. Vider le cache (Ctrl+Shift+Del)")
print("   3. Changer en ESPAGNOL")
print("   4. Vérifier que le contenu est traduit")
