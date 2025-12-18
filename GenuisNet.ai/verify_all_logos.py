#!/usr/bin/env python3
"""Vérification que tous les logos sont présents dans les reviews"""

from pathlib import Path
import re

BASE_DIR = Path(__file__).parent
REVIEWS_DIR = BASE_DIR / "pages" / "reviews"
LOGOS_DIR = BASE_DIR / "assets" / "images" / "logos"

def check_review_has_logo(review_path: Path) -> dict:
    """Vérifie si une page de review a un logo"""
    try:
        with open(review_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Chercher les logos officiels
        has_official_logo = 'assets/images/logos/' in content
        
        # Chercher d'autres chemins de logos
        has_tools_logo = 'assets/images/tools/' in content
        
        # Extraire le chemin du logo
        logo_match = re.search(r'<img[^>]*src="([^"]*(?:logos|tools)[^"]*)"', content)
        logo_path = logo_match.group(1) if logo_match else None
        
        return {
            'path': str(review_path.relative_to(BASE_DIR)),
            'has_official': has_official_logo,
            'has_other': has_tools_logo,
            'logo_path': logo_path,
            'status': '✅' if has_official_logo else ('⚠️' if has_tools_logo else '❌')
        }
    except Exception as e:
        return {
            'path': str(review_path.relative_to(BASE_DIR)),
            'has_official': False,
            'has_other': False,
            'logo_path': None,
            'status': '❌',
            'error': str(e)
        }

print("🔍 Vérification de tous les logos dans les reviews...\n")

all_reviews = list(REVIEWS_DIR.rglob("*.html"))
print(f"📄 {len(all_reviews)} pages de review trouvées\n")

results = []
for review in sorted(all_reviews):
    result = check_review_has_logo(review)
    results.append(result)

# Statistiques
official_count = sum(1 for r in results if r['has_official'])
other_count = sum(1 for r in results if r['has_other'] and not r['has_official'])
missing_count = sum(1 for r in results if not r['has_official'] and not r['has_other'])

print("="*70)
print("📊 RÉSUMÉ DE LA VÉRIFICATION")
print("="*70)
print(f"✅ Pages avec logos officiels (assets/images/logos/): {official_count}/{len(results)}")
print(f"⚠️  Pages avec autres logos (assets/images/tools/):  {other_count}/{len(results)}")
print(f"❌ Pages sans logo:                                   {missing_count}/{len(results)}")
print(f"\n🎯 Taux de logos officiels: {(official_count/len(results)*100):.1f}%")

# Afficher les pages sans logo officiel
if other_count > 0 or missing_count > 0:
    print("\n⚠️  PAGES À VÉRIFIER:")
    print("-"*70)
    for r in results:
        if not r['has_official']:
            print(f"{r['status']} {r['path']}")
            if r['logo_path']:
                print(f"   Logo actuel: {r['logo_path']}")
else:
    print("\n🎉 PARFAIT! Toutes les pages utilisent les logos officiels!")

# Échantillon de vérification
print("\n✨ ÉCHANTILLON DE VÉRIFICATION (10 premières pages):")
print("-"*70)
for r in results[:10]:
    name = Path(r['path']).stem
    print(f"{r['status']} {name:30} → {r['logo_path'] or 'Aucun logo'}")

