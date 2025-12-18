#!/usr/bin/env python3
"""
Script pour ajouter automatiquement les attributs data-i18n manquants
dans les fichiers HTML des reviews de chatbots
"""
import sys
import re
from bs4 import BeautifulSoup
from pathlib import Path

def slugify(text):
    """Convertit un texte en clé i18n (slug)"""
    # Enlever les caractères spéciaux et mettre en minuscules
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'\s+', '.', text.strip())
    text = re.sub(r'-+', '.', text)
    # Limiter la longueur
    words = text.split('.')
    if len(words) > 5:
        words = words[:5]
    return '.'.join(words)

def has_data_i18n(element):
    """Vérifie si l'élément ou ses enfants ont déjà data-i18n"""
    if element.get('data-i18n'):
        return True
    # Vérifier les enfants span avec data-i18n
    for child in element.find_all('span', {'data-i18n': True}, recursive=False):
        return True
    return False

def wrap_text_with_i18n(soup, element, key, tool_name):
    """Entoure le texte d'un élément avec <span data-i18n>"""
    # Si l'élément a déjà un data-i18n, ne rien faire
    if has_data_i18n(element):
        return False

    # Récupérer le texte direct (sans les enfants)
    text = element.get_text(strip=True)

    # Ignorer si vide ou trop long
    if not text or len(text) > 300:
        return False

    # Créer un nouveau span avec data-i18n
    new_span = soup.new_tag('span')
    new_span['data-i18n'] = f"review.{tool_name}.{key}"
    new_span.string = text

    # Remplacer le contenu de l'élément
    element.clear()
    element.append(new_span)

    return True

def process_html(html_file, tool_name, dry_run=False):
    """Traite un fichier HTML pour ajouter les data-i18n manquants"""

    print(f"\n{'='*60}")
    print(f"🔍 ANALYSE: {html_file}")
    print(f"{'='*60}\n")

    # Lire le fichier HTML
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    # Compteurs
    stats = {
        'h4_added': 0,
        'li_added': 0,
        'td_added': 0,
        'button_added': 0,
        'total_existing': len(soup.find_all(attrs={'data-i18n': True}))
    }

    # 1. Traiter les titres <h4> dans les feature cards
    print("📌 Traitement des titres <h4>...")
    h4_elements = soup.find_all('h4')
    for idx, h4 in enumerate(h4_elements):
        if not has_data_i18n(h4):
            text = h4.get_text(strip=True)
            slug = slugify(text)
            key = f"feature.{slug}.title"
            if wrap_text_with_i18n(soup, h4, key, tool_name):
                stats['h4_added'] += 1
                print(f"  ✓ h4 #{idx+1}: {text[:50]}...")

    # 2. Traiter les éléments de liste <li> (pros/cons)
    print("\n📌 Traitement des listes <li>...")
    li_elements = soup.find_all('li')
    pro_count = 1
    con_count = 1
    for li in li_elements:
        if not has_data_i18n(li):
            text = li.get_text(strip=True)
            # Déterminer si c'est un pro ou un con
            parent_section = li.find_parent(['div', 'section'])
            if parent_section:
                section_text = parent_section.get_text()
                if 'disadvantage' in section_text.lower() or 'cons' in section_text.lower():
                    key = f"con.{con_count}"
                    con_count += 1
                else:
                    key = f"pro.{pro_count}"
                    pro_count += 1
            else:
                key = f"list.item.{li_elements.index(li) + 1}"

            if wrap_text_with_i18n(soup, li, key, tool_name):
                stats['li_added'] += 1
                print(f"  ✓ li: {text[:50]}...")

    # 3. Traiter les cellules de tableau <td>
    print("\n📌 Traitement des tableaux <td>...")
    td_elements = soup.find_all('td')
    for idx, td in enumerate(td_elements):
        if not has_data_i18n(td):
            text = td.get_text(strip=True)
            if text:
                slug = slugify(text)
                key = f"table.{slug}"
                if wrap_text_with_i18n(soup, td, key, tool_name):
                    stats['td_added'] += 1
                    print(f"  ✓ td #{idx+1}: {text[:50]}...")

    # 4. Traiter les boutons sans data-i18n
    print("\n📌 Traitement des boutons <a class='btn'>...")
    button_elements = soup.find_all('a', class_=re.compile('btn'))
    for btn in button_elements:
        if not has_data_i18n(btn):
            text = btn.get_text(strip=True)
            slug = slugify(text)
            key = f"button.{slug}"
            if wrap_text_with_i18n(soup, btn, key, tool_name):
                stats['button_added'] += 1
                print(f"  ✓ button: {text[:50]}...")

    # Statistiques finales
    total_added = stats['h4_added'] + stats['li_added'] + stats['td_added'] + stats['button_added']
    total_after = stats['total_existing'] + total_added

    print(f"\n{'='*60}")
    print(f"📊 STATISTIQUES")
    print(f"{'='*60}")
    print(f"  Éléments data-i18n existants: {stats['total_existing']}")
    print(f"  Titres <h4> ajoutés:          {stats['h4_added']}")
    print(f"  Listes <li> ajoutées:         {stats['li_added']}")
    print(f"  Tableaux <td> ajoutés:        {stats['td_added']}")
    print(f"  Boutons ajoutés:              {stats['button_added']}")
    print(f"  {'─'*60}")
    print(f"  TOTAL AJOUTÉ:                 {total_added}")
    print(f"  TOTAL APRÈS TRAITEMENT:       {total_after}")
    print(f"{'='*60}\n")

    # Sauvegarder le fichier modifié
    if not dry_run and total_added > 0:
        # Backup de l'original
        backup_file = html_file.replace('.html', '.backup.html')
        with open(backup_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"💾 Backup sauvegardé: {backup_file}")

        # Sauvegarder le nouveau fichier
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"✅ Fichier mis à jour: {html_file}\n")
    elif dry_run:
        print("⚠️  MODE DRY-RUN: Aucune modification sauvegardée\n")
    else:
        print("ℹ️  Aucune modification nécessaire\n")

    return stats

def main():
    """Fonction principale"""
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python3 add_missing_i18n.py <tool_name> [--dry-run]")
        print("")
        print("Exemples:")
        print("  python3 add_missing_i18n.py claude")
        print("  python3 add_missing_i18n.py gemini --dry-run")
        print("")
        print("Options:")
        print("  --dry-run    Analyser sans modifier les fichiers")
        sys.exit(1)

    tool_name = sys.argv[1].lower()
    dry_run = '--dry-run' in sys.argv

    html_file = f'GenuisNet.ai/pages/reviews/chatbots/{tool_name}.html'

    if not Path(html_file).exists():
        print(f"❌ Erreur: Fichier non trouvé: {html_file}")
        sys.exit(1)

    if dry_run:
        print("\n⚠️  MODE DRY-RUN ACTIVÉ - Aucune modification ne sera sauvegardée\n")

    stats = process_html(html_file, tool_name, dry_run)

    if not dry_run:
        print("✨ TERMINÉ!")
        print(f"\n🚀 Prochaine étape:")
        print(f"   source venv/bin/activate")
        print(f"   python3 process_tool.py {tool_name}")

if __name__ == '__main__':
    main()
