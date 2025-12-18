#!/usr/bin/env python3
"""
Script pour mettre à jour tous les logos dans les pages de review
en utilisant les logos officiels disponibles dans assets/images/logos/
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple

# Chemins de base
BASE_DIR = Path(__file__).parent
REVIEWS_DIR = BASE_DIR / "pages" / "reviews"
LOGOS_DIR = BASE_DIR / "assets" / "images" / "logos"

def get_available_logos() -> Dict[str, str]:
    """
    Récupère tous les logos officiels disponibles
    Retourne un dict: {nom_fichier_sans_ext: chemin_relatif}
    """
    logos = {}
    if not LOGOS_DIR.exists():
        print(f"❌ Dossier logos introuvable: {LOGOS_DIR}")
        return logos

    for logo_file in LOGOS_DIR.glob("*"):
        if logo_file.suffix.lower() in ['.png', '.svg', '.jpg', '.jpeg']:
            # Nom sans extension
            name = logo_file.stem
            logos[name] = str(logo_file.relative_to(BASE_DIR))

    print(f"✅ {len(logos)} logos officiels trouvés")
    return logos

def extract_tool_name_from_review(html_path: Path) -> str:
    """
    Extrait le nom de l'outil depuis le nom du fichier
    """
    return html_path.stem

def find_logo_match(tool_name: str, available_logos: Dict[str, str]) -> str:
    """
    Trouve le logo correspondant au nom de l'outil
    Gère les variations de nommage
    """
    # Mapping manuel pour les cas spéciaux
    manual_mapping = {
        'cylance': 'cylance-new',
        'palo-alto-ngfw': 'palo-alto',
        'cortex-xdr': 'palo-alto-cortex',
        'splunk-security': 'splunk-enterprise-security',
        'microsoft-sentinel': 'microsoft-defender-ai',
        'codewhisperer': 'amazon-codewhisperer',
        'github-copilot': 'copilot',
        'looker-ai': 'looker',
        'dall-e-3': 'stable-diffusion',  # Placeholder si pas de logo DALL-E
        'deepseek-coder': 'deepseek',
        'sentinelone': 'sentinelone-new',
        'salesforce-einstein-gpt': 'salesforce-einstein',
    }

    # Normalisation du nom
    tool_normalized = tool_name.lower().replace(" ", "-").replace("_", "-")

    # Vérifier le mapping manuel d'abord
    if tool_normalized in manual_mapping:
        mapped_name = manual_mapping[tool_normalized]
        if mapped_name in available_logos:
            return available_logos[mapped_name]

    # Correspondances exactes
    if tool_normalized in available_logos:
        return available_logos[tool_normalized]

    # Correspondances avec variations
    variations = [
        tool_normalized.replace("-ai", ""),
        f"{tool_normalized}-ai",
        tool_normalized.replace("-", ""),
        tool_normalized.replace("-", "_"),
    ]

    for var in variations:
        if var in available_logos:
            return available_logos[var]

    return None

def get_relative_path_from_review(review_path: Path, logo_path: str) -> str:
    """
    Calcule le chemin relatif depuis une page de review vers le logo
    """
    # Compter le nombre de niveaux de dossiers
    # Ex: pages/reviews/chatbots/chatgpt.html -> 3 niveaux
    depth = len(review_path.relative_to(REVIEWS_DIR).parts)
    prefix = "../" * depth
    return f"{prefix}{logo_path}"

def update_logo_in_review(review_path: Path, logo_rel_path: str) -> bool:
    """
    Met à jour le logo dans une page de review
    Gère les deux formats: tool-logo-xl et review-logo
    """
    try:
        with open(review_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        updated = False

        # Pattern 1: tool-logo-xl
        # <div class="tool-logo-xl">
        #     <img alt="..." src="..."/>
        # </div>
        pattern1 = r'(<div class="tool-logo-xl">)\s*(<img[^>]*?src=")([^"]+)("[^>]*/>)'

        def replace_logo_xl(match):
            nonlocal updated
            div_open = match.group(1)
            img_start = match.group(2)
            old_src = match.group(3)
            img_end = match.group(4)

            # Remplacer uniquement si ce n'est pas déjà le bon chemin
            if 'assets/images/logos/' not in old_src:
                updated = True
                new_src = logo_rel_path
                return f'{div_open}\n<img alt="{review_path.stem.title()} Logo" src="{new_src}"{img_end[:-2]}/>'
            return match.group(0)

        content = re.sub(pattern1, replace_logo_xl, content)

        # Pattern 2: review-logo
        # <div class="review-logo">
        #     <img alt="..." src="..."/>
        # </div>
        pattern2 = r'(<div class="review-logo">)\s*(<img[^>]*?src=")([^"]+)("[^>]*/>)'

        def replace_review_logo(match):
            nonlocal updated
            div_open = match.group(1)
            img_start = match.group(2)
            old_src = match.group(3)
            img_end = match.group(4)

            # Remplacer uniquement si ce n'est pas déjà le bon chemin
            if 'assets/images/logos/' not in old_src:
                updated = True
                new_src = logo_rel_path
                return f'{div_open}\n<img alt="{review_path.stem.title()} Logo" src="{new_src}"{img_end[:-2]}/>'
            return match.group(0)

        content = re.sub(pattern2, replace_review_logo, content)

        # Pattern 3: div sans img (juste du texte comme "OK")
        # <div class="review-logo">OK</div> ou <div class="tool-logo-xl">ChatGPT</div>
        pattern3 = r'(<div class="(?:review-logo|tool-logo-xl)">)(?!<img)([^<]+)(</div>)'

        def add_missing_logo(match):
            nonlocal updated
            div_open = match.group(1)
            text_content = match.group(2).strip()
            div_close = match.group(3)

            # Ajouter l'image
            updated = True
            tool_name = review_path.stem.replace('_', '-').lower()
            return f'{div_open}\n<img alt="{tool_name.title()} Logo" src="{logo_rel_path}"/>\n{div_close}'

        content = re.sub(pattern3, add_missing_logo, content)

        # Si le contenu a changé, sauvegarder
        if updated:
            with open(review_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True

        return False

    except Exception as e:
        print(f"❌ Erreur lors de la mise à jour de {review_path}: {e}")
        return False

def main():
    print("🚀 Début de la mise à jour des logos dans les reviews...\n")

    # 1. Récupérer tous les logos disponibles
    available_logos = get_available_logos()

    if not available_logos:
        print("❌ Aucun logo disponible, arrêt du script.")
        return

    # 2. Parcourir toutes les pages de review
    review_files = list(REVIEWS_DIR.rglob("*.html"))
    print(f"📄 {len(review_files)} pages de review trouvées\n")

    stats = {
        'updated': 0,
        'not_found': 0,
        'already_ok': 0,
        'errors': 0
    }

    not_found_list = []

    for review_path in sorted(review_files):
        tool_name = extract_tool_name_from_review(review_path)

        # Trouver le logo correspondant
        logo_path = find_logo_match(tool_name, available_logos)

        if not logo_path:
            stats['not_found'] += 1
            not_found_list.append(tool_name)
            print(f"⚠️  Logo non trouvé: {tool_name} ({review_path.relative_to(BASE_DIR)})")
            continue

        # Calculer le chemin relatif
        logo_rel_path = get_relative_path_from_review(review_path, logo_path)

        # Mettre à jour le fichier
        if update_logo_in_review(review_path, logo_rel_path):
            stats['updated'] += 1
            print(f"✅ Mis à jour: {tool_name} -> {logo_path}")
        else:
            stats['already_ok'] += 1

    # Résumé
    print("\n" + "="*60)
    print("📊 RÉSUMÉ")
    print("="*60)
    print(f"✅ Logos mis à jour: {stats['updated']}")
    print(f"✓  Déjà à jour: {stats['already_ok']}")
    print(f"⚠️  Logos non trouvés: {stats['not_found']}")
    print(f"❌ Erreurs: {stats['errors']}")
    print(f"\n📋 Total pages traitées: {len(review_files)}")

    if not_found_list:
        print(f"\n⚠️  Outils sans logo officiel ({len(not_found_list)}):")
        for tool in sorted(set(not_found_list)):
            print(f"   - {tool}")

    print("\n✨ Terminé!")

if __name__ == "__main__":
    main()
