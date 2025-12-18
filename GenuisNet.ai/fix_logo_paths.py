#!/usr/bin/env python3
"""Corrige les chemins relatifs des logos"""

from pathlib import Path
import re

BASE_DIR = Path(__file__).parent
REVIEWS_DIR = BASE_DIR / "pages" / "reviews"

def fix_logo_paths(file_path: Path):
    """Corrige le chemin relatif vers le logo"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Calculer le bon nombre de ../
        # pages/reviews/chatbots/file.html -> 3 niveaux
        depth = len(file_path.relative_to(BASE_DIR).parts) - 1
        correct_prefix = "../" * depth
        
        # Remplacer les mauvais chemins
        # Pattern: src="../../assets/images/logos/ ou src="../../../assets/images/logos/
        pattern = r'src="(\.\./)+(assets/images/logos/[^"]+)"'
        
        def replace_path(match):
            asset_path = match.group(2)
            return f'src="{correct_prefix}{asset_path}"'
        
        content = re.sub(pattern, replace_path, content)
        
        if content != original:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
        
    except Exception as e:
        print(f"❌ Erreur {file_path}: {e}")
        return False

print("🔧 Correction des chemins de logos...\n")

fixed = 0
for html_file in REVIEWS_DIR.rglob("*.html"):
    if fix_logo_paths(html_file):
        print(f"✅ {html_file.relative_to(BASE_DIR)}")
        fixed += 1

print(f"\n📊 {fixed} fichiers corrigés")

