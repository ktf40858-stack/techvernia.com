#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script d'analyse du support multilingue pour la catégorie AI Translation & Localization
"""

import os
import json
import re
from pathlib import Path
from collections import defaultdict

class TranslationI18nAnalyzer:
    def __init__(self, base_path):
        self.base_path = Path(base_path)
        self.translation_tools = [
            'deepl-pro',
            'google-translate-ai',
            'lilt',
            'lokalise',
            'microsoft-translator',
            'modernmt',
            'phrase',
            'smartling',
            'systran',
            'unbabel'
        ]
        self.languages = {
            'en': 'English',
            'fr': 'Français',
            'de': 'Deutsch',
            'es': 'Español',
            'pt': 'Português',
            'zh': '中文',
            'ja': '日本語',
            'ko': '한국어',
            'ar': 'العربية',
            'hi': 'हिन्दी'
        }

    def analyze_i18n_file(self, tool_name):
        """Analyse un fichier i18n pour un outil spécifique"""
        i18n_path = self.base_path / 'GenuisNet.ai' / 'js' / f'{tool_name}-i18n.js'

        if not i18n_path.exists():
            return {
                'exists': False,
                'languages': [],
                'total_keys': 0,
                'file_size': 0
            }

        with open(i18n_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extraire les langues
        lang_pattern = r'"([a-z]{2})":\s*\{'
        found_languages = re.findall(lang_pattern, content)

        # Compter les clés pour la langue anglaise
        en_keys = re.findall(r'"review\.' + tool_name.replace('-', r'[-\.]') + r'[^"]*":', content)

        return {
            'exists': True,
            'languages': found_languages,
            'total_keys': len(en_keys),
            'file_size': len(content),
            'line_count': content.count('\n')
        }

    def analyze_html_file(self, tool_name):
        """Analyse un fichier HTML pour vérifier l'intégration i18n"""
        html_path = self.base_path / 'GenuisNet.ai' / 'pages' / 'reviews' / 'translation' / f'{tool_name}.html'

        if not html_path.exists():
            return {
                'exists': False,
                'has_i18n_script': False,
                'has_lang_selector': False,
                'has_data_i18n': False
            }

        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Vérifier la présence du script i18n
        has_i18n_script = f'{tool_name}-i18n.js' in content

        # Vérifier la présence du sélecteur de langue
        has_lang_selector = 'language-selector' in content or 'lang-selector' in content

        # Vérifier la présence d'attributs data-i18n
        has_data_i18n = 'data-i18n=' in content

        # Compter les éléments data-i18n
        data_i18n_count = len(re.findall(r'data-i18n="[^"]*"', content))

        return {
            'exists': True,
            'has_i18n_script': has_i18n_script,
            'has_lang_selector': has_lang_selector,
            'has_data_i18n': has_data_i18n,
            'data_i18n_count': data_i18n_count,
            'file_size': len(content)
        }

    def generate_report(self):
        """Génère un rapport complet de l'analyse"""
        print("="*80)
        print("RAPPORT MULTILINGUE - CATÉGORIE AI TRANSLATION & LOCALIZATION")
        print("="*80)
        print()

        print("📊 VUE D'ENSEMBLE")
        print("-" * 80)
        print(f"Nombre total d'outils: {len(self.translation_tools)}")
        print(f"Langues supportées: {len(self.languages)}")
        print(f"Langues: {', '.join([f'{code} ({name})' for code, name in self.languages.items()])}")
        print()

        print("="*80)
        print("📁 ANALYSE DÉTAILLÉE PAR OUTIL")
        print("="*80)
        print()

        summary = {
            'total_tools': len(self.translation_tools),
            'i18n_complete': 0,
            'html_complete': 0,
            'fully_integrated': 0,
            'missing_i18n': [],
            'missing_integration': []
        }

        for tool in self.translation_tools:
            print(f"🔧 {tool.upper()}")
            print("-" * 80)

            # Analyser le fichier i18n
            i18n_info = self.analyze_i18n_file(tool)
            print(f"  Fichier i18n:")
            if i18n_info['exists']:
                print(f"    ✅ Existe: Oui")
                print(f"    📝 Lignes: {i18n_info['line_count']}")
                print(f"    🔑 Clés de traduction: {i18n_info['total_keys']}")
                print(f"    🌍 Langues: {len(i18n_info['languages'])}/{len(self.languages)}")

                missing_langs = set(self.languages.keys()) - set(i18n_info['languages'])
                if missing_langs:
                    print(f"    ⚠️  Langues manquantes: {', '.join(missing_langs)}")
                else:
                    print(f"    ✅ Toutes les langues présentes!")
                    summary['i18n_complete'] += 1
            else:
                print(f"    ❌ Existe: Non")
                summary['missing_i18n'].append(tool)

            # Analyser le fichier HTML
            html_info = self.analyze_html_file(tool)
            print(f"\n  Fichier HTML:")
            if html_info['exists']:
                print(f"    ✅ Existe: Oui")
                print(f"    📜 Script i18n chargé: {'✅ Oui' if html_info['has_i18n_script'] else '❌ Non'}")
                print(f"    🌐 Sélecteur de langue: {'✅ Oui' if html_info['has_lang_selector'] else '❌ Non'}")
                print(f"    🏷️  Attributs data-i18n: {'✅ Oui' if html_info['has_data_i18n'] else '❌ Non'}")
                print(f"    📊 Nombre de data-i18n: {html_info['data_i18n_count']}")

                if html_info['has_i18n_script'] and html_info['has_lang_selector'] and html_info['has_data_i18n']:
                    print(f"    ✅ Intégration complète!")
                    summary['html_complete'] += 1
                else:
                    summary['missing_integration'].append(tool)
            else:
                print(f"    ❌ Existe: Non")

            # Vérifier si l'outil est complètement intégré
            if (i18n_info['exists'] and
                len(i18n_info['languages']) == len(self.languages) and
                html_info['exists'] and
                html_info['has_i18n_script'] and
                html_info['has_lang_selector'] and
                html_info['has_data_i18n']):
                print(f"\n  🎉 STATUT: COMPLÈTEMENT MULTILINGUE ✅")
                summary['fully_integrated'] += 1
            else:
                print(f"\n  ⚠️  STATUT: INTÉGRATION PARTIELLE")

            print()

        print("="*80)
        print("📈 RÉSUMÉ STATISTIQUE")
        print("="*80)
        print()
        print(f"✅ Outils avec fichiers i18n complets: {summary['i18n_complete']}/{summary['total_tools']} ({summary['i18n_complete']/summary['total_tools']*100:.1f}%)")
        print(f"✅ Outils avec HTML intégré: {summary['html_complete']}/{summary['total_tools']} ({summary['html_complete']/summary['total_tools']*100:.1f}%)")
        print(f"🎉 Outils complètement multilingues: {summary['fully_integrated']}/{summary['total_tools']} ({summary['fully_integrated']/summary['total_tools']*100:.1f}%)")
        print()

        if summary['missing_i18n']:
            print(f"⚠️  Fichiers i18n manquants: {', '.join(summary['missing_i18n'])}")

        if summary['missing_integration']:
            print(f"⚠️  Intégration HTML incomplète: {', '.join(summary['missing_integration'])}")
        print()

        print("="*80)
        print("🎯 RECOMMANDATIONS")
        print("="*80)
        print()

        if summary['fully_integrated'] == summary['total_tools']:
            print("✅ Excellente nouvelle! Tous les outils de traduction sont complètement multilingues.")
            print("✅ La catégorie AI Translation & Localization est prête pour un déploiement international.")
        else:
            print("📋 Actions recommandées:")
            if summary['missing_i18n']:
                print(f"   1. Créer les fichiers i18n manquants pour: {', '.join(summary['missing_i18n'])}")
            if summary['missing_integration']:
                print(f"   2. Compléter l'intégration HTML pour: {', '.join(summary['missing_integration'])}")

        print()
        print("="*80)
        print("🌍 SUPPORT LINGUISTIQUE DÉTAILLÉ")
        print("="*80)
        print()

        # Tableau récapitulatif par langue
        print(f"{'Langue':<15} {'Code':<6} {'Outils supportés':<20} {'Pourcentage'}")
        print("-" * 80)

        for lang_code, lang_name in self.languages.items():
            tools_with_lang = 0
            for tool in self.translation_tools:
                i18n_info = self.analyze_i18n_file(tool)
                if i18n_info['exists'] and lang_code in i18n_info['languages']:
                    tools_with_lang += 1

            percentage = tools_with_lang / len(self.translation_tools) * 100
            bar = '█' * int(percentage / 5)
            print(f"{lang_name:<15} {lang_code:<6} {tools_with_lang:>2}/{len(self.translation_tools):<15} {percentage:>6.1f}% {bar}")

        print()
        print("="*80)
        print("📝 NOTES TECHNIQUES")
        print("="*80)
        print()
        print("Structure des fichiers i18n:")
        print("  - Format: JavaScript (const translations = {...})")
        print("  - Taille moyenne: ~1256 lignes par fichier")
        print("  - Clés: Nommées selon le pattern 'review.{tool-name}.{section}.{element}'")
        print()
        print("Intégration HTML:")
        print("  - Script i18n: Chargé via <script src='../../../js/{tool-name}-i18n.js'>")
        print("  - Sélecteur de langue: Présent dans la navigation")
        print("  - Attributs: data-i18n appliqués aux éléments traduisibles")
        print()

        return summary

def main():
    import sys
    import io

    # Fix Windows console encoding
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    base_path = Path(__file__).parent
    analyzer = TranslationI18nAnalyzer(base_path)
    summary = analyzer.generate_report()

    print("="*80)
    print("Analyse terminée avec succès! ✅")
    print("="*80)

if __name__ == "__main__":
    main()
