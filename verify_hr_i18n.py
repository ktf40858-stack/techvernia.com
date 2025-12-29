#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HR I18N Verification Script
Vérifie que tous les fichiers i18n HR sont complets et corrects
"""

import os
import json
import re

HR_TOOLS = [
    'beamery', 'eightfold-ai', 'fetcher', 'findem', 'harver',
    'hirevue', 'humanly', 'paradox-olivia', 'phenom', 'pymetrics',
    'seekout', 'sense', 'textio', 'workable-ai'
]

LANGUAGES = ['en', 'fr', 'de', 'es', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']

def verify_file(filepath, tool_name):
    """Vérifie un fichier i18n"""
    errors = []
    warnings = []

    if not os.path.exists(filepath):
        errors.append(f"File does not exist: {filepath}")
        return errors, warnings

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Vérifier que toutes les langues sont présentes
    for lang in LANGUAGES:
        if f'"{lang}":' not in content:
            errors.append(f"Missing language: {lang}")

    # Vérifier qu'il n'y a pas de texte en anglais dans les autres langues
    # (sauf pour les clés qui sont censées être en anglais)
    for lang in ['fr', 'de', 'es', 'pt']:
        # Extraire la section de cette langue
        pattern = f'"{lang}":\\s*{{([^}}]+)}}'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            lang_section = match.group(1)
            # Compter les lignes en anglais (heuristique simple)
            english_phrases = [
                'is a powerful',
                'The platform leverages',
                'Advanced features',
                'Powerful AI capabilities'
            ]
            for phrase in english_phrases:
                if phrase in lang_section:
                    warnings.append(f"{lang}: Contains English phrase '{phrase}'")

    # Vérifier la taille du fichier
    size = len(content)
    if size < 50000:
        warnings.append(f"File seems small ({size} chars), may be incomplete")

    # Vérifier la structure JavaScript
    if 'const ' not in content or 'Translations = {' not in content:
        errors.append("Invalid JavaScript structure")

    return errors, warnings

def main():
    """Vérifie tous les fichiers HR i18n"""
    base_path = 'GenuisNet.ai/js'

    print("=" * 70)
    print("HR I18N VERIFICATION REPORT")
    print("=" * 70)
    print()

    total_errors = 0
    total_warnings = 0
    all_ok = []
    has_issues = []

    for tool in HR_TOOLS:
        filename = f"{tool}-i18n.js"
        filepath = os.path.join(base_path, filename)

        errors, warnings = verify_file(filepath, tool)

        if errors:
            total_errors += len(errors)
            has_issues.append(tool)
            print(f"[ERROR] {filename}")
            for error in errors:
                print(f"  - {error}")
        elif warnings:
            total_warnings += len(warnings)
            has_issues.append(tool)
            print(f"[WARNING] {filename}")
            for warning in warnings:
                print(f"  - {warning}")
        else:
            all_ok.append(tool)
            print(f"[OK] {filename}")

        print()

    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Total files checked: {len(HR_TOOLS)}")
    print(f"Files OK: {len(all_ok)}")
    print(f"Files with issues: {len(has_issues)}")
    print(f"Total errors: {total_errors}")
    print(f"Total warnings: {total_warnings}")
    print()

    if all_ok:
        print("Files OK:")
        for tool in all_ok:
            print(f"  - {tool}")
        print()

    if has_issues:
        print("Files with issues:")
        for tool in has_issues:
            print(f"  - {tool}")
        print()

    if total_errors == 0:
        print("[SUCCESS] All HR i18n files are valid!")
    else:
        print(f"[FAILED] {total_errors} errors found")

    print("=" * 70)

if __name__ == "__main__":
    main()
