#!/usr/bin/env python3
"""
TechVernia - Générateur de Pages Multilingues
==============================================
Génère automatiquement des pages HTML statiques pour 10 langues
en utilisant les traductions i18n.js existantes.

Langues supportées: EN, FR, ES, DE, PT, ZH, JA, KO, AR, HI
"""

import os
import re
import json
import shutil
from pathlib import Path
from datetime import datetime
from html.parser import HTMLParser
import unicodedata

# Configuration
DOCS_DIR = Path("docs")
LANGUAGES = {
    'en': {'name': 'English', 'flag': '🇬🇧', 'dir': 'ltr'},
    'fr': {'name': 'Français', 'flag': '🇫🇷', 'dir': 'ltr'},
    'es': {'name': 'Español', 'flag': '🇪🇸', 'dir': 'ltr'},
    'de': {'name': 'Deutsch', 'flag': '🇩🇪', 'dir': 'ltr'},
    'pt': {'name': 'Português', 'flag': '🇵🇹', 'dir': 'ltr'},
    'zh': {'name': '中文', 'flag': '🇨🇳', 'dir': 'ltr'},
    'ja': {'name': '日本語', 'flag': '🇯🇵', 'dir': 'ltr'},
    'ko': {'name': '한국어', 'flag': '🇰🇷', 'dir': 'ltr'},
    'ar': {'name': 'العربية', 'flag': '🇸🇦', 'dir': 'rtl'},
    'hi': {'name': 'हिंदी', 'flag': '🇮🇳', 'dir': 'ltr'},
}

# Fichiers à exclure
EXCLUDED_FILES = [
    'home_hero_enhanced.html',
    'demo-logo.html',
    'exemple-icones-moderne.html',
    'logo-preview.html',
    'test_chatgpt_i18n.html',
    'verify_space_grotesk.html',
    'voir-logo.html',
]

# Dossiers à exclure
EXCLUDED_DIRS = [
    'tmpclaude-',
    'backup_',
]

class I18nParser:
    """Parse les fichiers i18n.js et extrait les traductions"""

    def __init__(self, i18n_file):
        self.translations = {}
        self.parse_i18n_file(i18n_file)

    def parse_i18n_file(self, file_path):
        """Parse le fichier i18n.js JavaScript"""
        print(f"📖 Lecture de {file_path}...")

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extraire l'objet translations
            # On cherche: const translations = { ... };
            match = re.search(r'const\s+translations\s*=\s*(\{[\s\S]*?\});', content)
            if not match:
                print(f"⚠️  Impossible de trouver 'const translations' dans {file_path}")
                return

            js_object = match.group(1)

            # Parser chaque langue
            for lang_code in LANGUAGES.keys():
                lang_match = re.search(
                    rf'{lang_code}\s*:\s*\{{([\s\S]*?)\n\s*\}},?\s*(?://|en:|fr:|es:|de:|pt:|zh:|ja:|ko:|ar:|hi:|$)',
                    js_object
                )

                if lang_match:
                    lang_content = lang_match.group(1)
                    self.translations[lang_code] = self.parse_language_object(lang_content)
                    print(f"  ✓ {lang_code.upper()}: {len(self.translations[lang_code])} clés")
                else:
                    print(f"  ✗ {lang_code.upper()}: non trouvé")

        except Exception as e:
            print(f"❌ Erreur lors de la lecture de {file_path}: {e}")

    def parse_language_object(self, content):
        """Parse le contenu d'une langue et extrait les paires clé-valeur"""
        translations = {}

        # Pattern pour capturer "key": "value"
        pattern = r'"([^"]+)":\s*"((?:[^"\\]|\\.)*)"\s*,?'
        matches = re.findall(pattern, content)

        for key, value in matches:
            # Nettoyer les échappements
            value = value.replace('\\"', '"').replace('\\n', '\n').replace('\\\'', "'")
            translations[key] = value

        return translations

    def get_translation(self, lang, key, default=""):
        """Récupère une traduction"""
        return self.translations.get(lang, {}).get(key, default)


class HTMLMultilingualGenerator:
    """Génère les pages HTML multilingues"""

    def __init__(self, i18n_parser):
        self.i18n = i18n_parser
        self.processed_files = []
        self.generated_files = []

    def should_process_file(self, file_path):
        """Vérifie si le fichier doit être traité"""
        file_name = file_path.name

        # Exclure les fichiers spécifiques
        if file_name in EXCLUDED_FILES:
            return False

        # Exclure les dossiers temporaires
        for excluded_dir in EXCLUDED_DIRS:
            if excluded_dir in str(file_path):
                return False

        # Exclure les fichiers déjà dans des dossiers de langue
        for lang in LANGUAGES.keys():
            if f"/{lang}/" in str(file_path).replace('\\', '/'):
                return False

        return True

    def get_relative_path_depth(self, file_path):
        """Calcule la profondeur relative du fichier"""
        rel_path = file_path.relative_to(DOCS_DIR)
        return len(rel_path.parts) - 1

    def adjust_paths_for_depth(self, html_content, depth):
        """Ajuste les chemins relatifs selon la profondeur"""
        if depth == 0:
            # À la racine, ajouter un niveau
            html_content = re.sub(r'href="(?!http|#|/)', r'href="../', html_content)
            html_content = re.sub(r'src="(?!http|#|/)', r'src="../', html_content)
        elif depth > 0:
            # Déjà dans un sous-dossier, pas besoin d'ajustement majeur
            pass

        return html_content

    def translate_html_content(self, html_content, lang_code):
        """Traduit le contenu HTML en remplaçant les attributs data-i18n"""

        # Traduire les éléments avec data-i18n
        def replace_data_i18n(match):
            full_tag = match.group(0)
            i18n_key = match.group(1)

            # Récupérer la traduction
            translation = self.i18n.get_translation(lang_code, i18n_key)

            if not translation:
                # Pas de traduction, garder l'original
                return full_tag

            # Remplacer le contenu entre les balises
            # Pattern: <tag ...>contenu</tag>
            tag_pattern = r'(<[^>]+>)(.*?)(</[^>]+>)'
            tag_match = re.search(tag_pattern, full_tag, re.DOTALL)

            if tag_match:
                opening = tag_match.group(1)
                closing = tag_match.group(3)
                return f"{opening}{translation}{closing}"

            return full_tag

        # Remplacer tous les éléments avec data-i18n
        html_content = re.sub(
            r'<[^>]+data-i18n="([^"]+)"[^>]*>.*?</[^>]+>',
            replace_data_i18n,
            html_content,
            flags=re.DOTALL
        )

        return html_content

    def add_hreflang_tags(self, html_content, file_path):
        """Ajoute les balises hreflang au HTML"""

        # Supprimer d'abord les anciennes balises hreflang (si présentes)
        # Pattern pour détecter les blocs de balises hreflang existantes
        hreflang_pattern = r'<!-- Balises hreflang pour SEO multilingue -->.*?(?=</head>|<link(?! rel="alternate" hreflang)|<script|<style)'
        html_content = re.sub(hreflang_pattern, '', html_content, flags=re.DOTALL)

        # Supprimer aussi les balises individuelles hreflang qui pourraient rester
        html_content = re.sub(r'<link[^>]*rel="alternate"[^>]*hreflang="[^"]*"[^>]*/?>\n?', '', html_content)

        # Calculer l'URL relative
        rel_path = file_path.relative_to(DOCS_DIR)
        url_path = str(rel_path).replace('\\', '/')

        # Construire les balises hreflang
        hreflang_tags = []
        hreflang_tags.append('    <!-- Balises hreflang pour SEO multilingue -->')

        # Langue par défaut (x-default = EN)
        base_url = f"https://techvernia.com/{url_path}"
        hreflang_tags.append(f'    <link rel="alternate" hreflang="x-default" href="{base_url}" />')

        # Toutes les langues
        for lang in LANGUAGES.keys():
            if lang == 'en':
                lang_url = base_url
            else:
                lang_url = f"https://techvernia.com/{lang}/{url_path}"

            hreflang_tags.append(f'    <link rel="alternate" hreflang="{lang}" href="{lang_url}" />')

        hreflang_html = '\n'.join(hreflang_tags)

        # Insérer dans le <head>, juste avant </head>
        html_content = html_content.replace('</head>', f'{hreflang_html}\n</head>')

        return html_content

    def update_lang_attribute(self, html_content, lang_code):
        """Met à jour l'attribut lang dans la balise <html>"""
        html_content = re.sub(
            r'<html([^>]*)lang="[^"]*"',
            rf'<html\1lang="{lang_code}"',
            html_content
        )

        # Ajouter dir="rtl" pour l'arabe
        if lang_code == 'ar':
            html_content = re.sub(
                r'<html([^>]*)>',
                r'<html\1 dir="rtl">',
                html_content
            )

        return html_content

    def generate_multilingual_page(self, source_file, lang_code):
        """Génère une page HTML traduite pour une langue spécifique"""

        try:
            # Lire le fichier source
            with open(source_file, 'r', encoding='utf-8') as f:
                html_content = f.read()

            # Calculer le chemin de destination
            rel_path = source_file.relative_to(DOCS_DIR)

            if lang_code == 'en':
                # Garder l'original pour l'anglais
                dest_file = source_file
            else:
                # Créer dans le dossier de langue
                dest_dir = DOCS_DIR / lang_code / rel_path.parent
                dest_dir.mkdir(parents=True, exist_ok=True)
                dest_file = dest_dir / rel_path.name

            # Traduire le contenu
            html_content = self.translate_html_content(html_content, lang_code)

            # Mettre à jour l'attribut lang
            html_content = self.update_lang_attribute(html_content, lang_code)

            # Ajouter les balises hreflang
            html_content = self.add_hreflang_tags(html_content, source_file)

            # Ajuster les chemins si nécessaire (pour les langues != EN)
            if lang_code != 'en':
                depth = self.get_relative_path_depth(source_file)
                html_content = self.adjust_paths_for_depth(html_content, depth)

            # Écrire le fichier traduit
            with open(dest_file, 'w', encoding='utf-8') as f:
                f.write(html_content)

            self.generated_files.append(str(dest_file))
            return dest_file

        except Exception as e:
            print(f"❌ Erreur lors de la génération de {source_file} en {lang_code}: {e}")
            return None

    def process_all_html_files(self):
        """Traite tous les fichiers HTML du site"""
        print("\n🔄 Recherche des fichiers HTML...")

        # Trouver tous les fichiers HTML
        html_files = list(DOCS_DIR.rglob("*.html"))
        html_files = [f for f in html_files if self.should_process_file(f)]

        print(f"📄 {len(html_files)} fichiers HTML à traiter\n")

        total_generated = 0

        for html_file in html_files:
            rel_path = html_file.relative_to(DOCS_DIR)
            print(f"🔨 Traitement: {rel_path}")

            # Générer pour chaque langue
            for lang_code in LANGUAGES.keys():
                dest_file = self.generate_multilingual_page(html_file, lang_code)
                if dest_file:
                    total_generated += 1

            self.processed_files.append(str(html_file))
            print(f"  ✓ {len(LANGUAGES)} versions générées\n")

        print(f"\n✅ Génération terminée!")
        print(f"   📄 Fichiers sources traités: {len(self.processed_files)}")
        print(f"   🌍 Pages générées: {total_generated}")
        print(f"   📊 Total: {len(self.processed_files)} × {len(LANGUAGES)} = {total_generated} pages")


class SitemapGenerator:
    """Génère le sitemap.xml multilingue"""

    def __init__(self, generator):
        self.generator = generator

    def generate_sitemap(self):
        """Génère le sitemap avec toutes les URLs multilingues"""
        print("\n🗺️  Génération du sitemap.xml...")

        sitemap_file = DOCS_DIR / "sitemap.xml"
        today = datetime.now().strftime('%Y-%m-%d')

        # En-tête XML
        xml_lines = [
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
            '        xmlns:xhtml="http://www.w3.org/1999/xhtml">',
        ]

        # Pour chaque fichier traité
        processed_files_unique = set(self.generator.processed_files)

        for file_path_str in sorted(processed_files_unique):
            file_path = Path(file_path_str)
            rel_path = file_path.relative_to(DOCS_DIR)
            url_path = str(rel_path).replace('\\', '/')

            # Déterminer la priorité
            if url_path == 'index.html':
                priority = '1.0'
            elif 'categories' in url_path or 'reviews' in url_path:
                priority = '0.8'
            else:
                priority = '0.6'

            # Pour chaque langue
            for lang_code in LANGUAGES.keys():
                if lang_code == 'en':
                    full_url = f"https://techvernia.com/{url_path}"
                else:
                    full_url = f"https://techvernia.com/{lang_code}/{url_path}"

                xml_lines.append('  <url>')
                xml_lines.append(f'    <loc>{full_url}</loc>')
                xml_lines.append(f'    <lastmod>{today}</lastmod>')
                xml_lines.append('    <changefreq>weekly</changefreq>')
                xml_lines.append(f'    <priority>{priority}</priority>')

                # Ajouter les liens hreflang alternates
                for alt_lang in LANGUAGES.keys():
                    if alt_lang == 'en':
                        alt_url = f"https://techvernia.com/{url_path}"
                    else:
                        alt_url = f"https://techvernia.com/{alt_lang}/{url_path}"

                    xml_lines.append(f'    <xhtml:link rel="alternate" hreflang="{alt_lang}" href="{alt_url}"/>')

                xml_lines.append('  </url>')

        xml_lines.append('</urlset>')

        # Écrire le sitemap
        sitemap_content = '\n'.join(xml_lines)
        with open(sitemap_file, 'w', encoding='utf-8') as f:
            f.write(sitemap_content)

        total_urls = len(processed_files_unique) * len(LANGUAGES)
        print(f"✅ Sitemap généré: {total_urls} URLs")
        print(f"   📍 Fichier: {sitemap_file}")


def main():
    """Fonction principale"""
    # Configurer l'encodage pour Windows
    import sys
    if sys.platform == 'win32':
        sys.stdout.reconfigure(encoding='utf-8')

    print("=" * 60)
    print("🌍 TechVernia - Générateur de Pages Multilingues")
    print("=" * 60)
    langs_list = ', '.join([f'{code.upper()} ({LANGUAGES[code]["name"]})' for code in LANGUAGES.keys()])
    print(f"\nLangues supportées: {langs_list}")
    print(f"Répertoire: {DOCS_DIR.absolute()}\n")

    # 1. Parser les traductions i18n.js
    i18n_file = DOCS_DIR / "js" / "i18n.js"
    if not i18n_file.exists():
        print(f"❌ Fichier i18n.js introuvable: {i18n_file}")
        return

    i18n_parser = I18nParser(i18n_file)

    if not i18n_parser.translations:
        print("❌ Aucune traduction trouvée dans i18n.js")
        return

    # 2. Générer les pages multilingues
    generator = HTMLMultilingualGenerator(i18n_parser)
    generator.process_all_html_files()

    # 3. Générer le sitemap
    sitemap_gen = SitemapGenerator(generator)
    sitemap_gen.generate_sitemap()

    print("\n" + "=" * 60)
    print("✅ GÉNÉRATION TERMINÉE AVEC SUCCÈS!")
    print("=" * 60)
    print(f"\n📊 Statistiques:")
    print(f"   • Fichiers sources: {len(generator.processed_files)}")
    print(f"   • Pages générées: {len(generator.generated_files)}")
    print(f"   • Langues: {len(LANGUAGES)}")
    print(f"   • URLs dans sitemap: {len(generator.processed_files) * len(LANGUAGES)}")

    print(f"\n📁 Structure créée:")
    for lang_code, lang_info in LANGUAGES.items():
        if lang_code != 'en':
            lang_dir = DOCS_DIR / lang_code
            if lang_dir.exists():
                file_count = len(list(lang_dir.rglob("*.html")))
                print(f"   • {lang_info['flag']} {lang_code.upper()}/: {file_count} fichiers")

    print(f"\n🚀 Prochaines étapes:")
    print(f"   1. Vérifier quelques pages générées manuellement")
    print(f"   2. Tester sur navigateur (http://localhost:8000 ou file://)")
    print(f"   3. Soumettre le nouveau sitemap.xml à Google Search Console")
    print(f"   4. Attendre l'indexation (2-7 jours)")
    print(f"   5. Push sur GitHub quand tout est validé")

    print("\n✨ Votre site est maintenant multilingue et prêt pour le SEO mondial!")


if __name__ == "__main__":
    main()
