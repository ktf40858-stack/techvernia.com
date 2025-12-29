import os
import re

js_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\js"

translation_tools = {
    "deepl-pro": {"name": "DeepL Pro", "key_part": "deepl.pro"},
    "google-translate-ai": {"name": "Google Translate AI", "key_part": "google.translate.ai"},
    "lilt": {"name": "Lilt", "key_part": "lilt"},
    "lokalise": {"name": "Lokalise", "key_part": "lokalise"},
    "microsoft-translator": {"name": "Microsoft Translator", "key_part": "microsoft.translator"},
    "modernmt": {"name": "ModernMT", "key_part": "modernmt"},
    "phrase": {"name": "Phrase", "key_part": "phrase"},
    "smartling": {"name": "Smartling", "key_part": "smartling"},
    "systran": {"name": "SYSTRAN", "key_part": "systran"},
    "unbabel": {"name": "Unbabel", "key_part": "unbabel"}
}

# German translations for use cases
de_translations_template = {
    "{key_part}.excels.for": "{name} eignet sich hervorragend für:",
    "enterprise.teams.large.organizations.requiring": "Enterprise-Teams: Große Organisationen, die skalierbare Übersetzungslösungen mit erweiterten Funktionen benötigen",
    "growing.startups.fast-moving.companies.that": "Wachsende Startups: Schnelllebige Unternehmen, die flexible KI-gestützte Automatisierung benötigen",
    "remote.teams.distributed.teams.requiring": "Remote-Teams: Verteilte Teams, die Echtzeit-Zusammenarbeit und Kommunikation benötigen",
    "data-driven.organizations.companies.leveraging.analytics": "Datengesteuerte Organisationen: Unternehmen, die Analysen für strategische Entscheidungen nutzen",
    "compliance-heavy.industries.regulated.sectors.requiring": "Compliance-intensive Branchen: Regulierte Sektoren, die Enterprise-Sicherheit und Compliance benötigen",
    "may.not.be.ideal.for": "Möglicherweise nicht ideal für:",
    "very.small.businesses.with.minimal": "Sehr kleine Unternehmen mit minimalen Übersetzungsbedürfnissen",
    "organizations.requiring.extensive.offline.functionality": "Organisationen, die umfangreiche Offline-Funktionalität benötigen",
    "teams.with.very.limited.technical": "Teams mit sehr begrenzter technischer Expertise",
}

def add_use_case_translations_to_german(tool_key, tool_info):
    """Add or update German translations for use cases"""

    js_file = os.path.join(js_dir, f"{tool_key}-i18n.js")
    tool_name = tool_info["name"]
    key_part = tool_info["key_part"]

    if not os.path.exists(js_file):
        return False

    with open(js_file, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    modified = False

    # Build translations with tool-specific values
    de_translations = {}
    for key_suffix, translation in de_translations_template.items():
        # Replace {key_part} and {name} placeholders
        actual_key = key_suffix.replace("{key_part}", key_part)
        actual_translation = translation.replace("{name}", tool_name)
        de_translations[actual_key] = actual_translation

    # Find German section
    de_pattern = r'  "de":\s*\{'
    de_match = re.search(de_pattern, content)

    if not de_match:
        print(f"    [!] German section not found")
        return False

    # For each translation, find and replace or add
    for key_suffix, translation in de_translations.items():
        full_key = f"review.{tool_key}.{key_suffix}"

        # Try to find this key in the content
        key_pattern = rf'("{re.escape(full_key)}":\s*)"[^"]*"'
        key_match = re.search(key_pattern, content)

        if key_match:
            # Key exists, replace the value
            replacement = f'{key_match.group(1)}"{translation}"'
            content, count = re.subn(key_pattern, replacement, content)
            if count > 0:
                modified = True
        else:
            # Key doesn't exist, add it to German section
            insert_pos = de_match.end() + 1  # After the opening brace and newline
            new_line = f'    "{full_key}": "{translation}",\n'
            content = content[:insert_pos] + new_line + content[insert_pos:]
            modified = True

    if modified and content != original_content:
        with open(js_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  [+] German use case translations added/updated")
        return True

    return False

print("=" * 70)
print("ADDING PROPER GERMAN USE CASE TRANSLATIONS")
print("=" * 70)

fixed_count = 0

for tool_key, tool_info in translation_tools.items():
    print(f"\n{tool_info['name']}:")
    if add_use_case_translations_to_german(tool_key, tool_info):
        fixed_count += 1
    else:
        print(f"  [OK] Already complete")

print("\n" + "=" * 70)
print(f"COMPLETE: {fixed_count}/10 tools updated")
print("=" * 70)
print("\nGerman use case translations now complete!")
print("=" * 70)
