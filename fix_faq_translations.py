#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fix FAQ answer translations in all Translation tool i18n files
"""

import os
import re

# Base directory
base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
js_dir = os.path.join(base_dir, "js")

# All 10 Translation tools
tools = [
    "deepl-pro",
    "google-translate-ai",
    "lilt",
    "lokalise",
    "microsoft-translator",
    "modernmt",
    "phrase",
    "smartling",
    "systran",
    "unbabel"
]

# FAQ answer translations (English -> German)
faq_translations = {
    # Answer 1: Is worth the investment?
    "For most organizations, yes. The AI-powered automation and productivity gains typically provide strong ROI within the first few months. The platform's scalability and extensive features justify the cost for growing teams.":
    "Für die meisten Organisationen ja. Die KI-gestützte Automatisierung und Produktivitätsgewinne liefern in der Regel einen starken ROI innerhalb der ersten Monate. Die Skalierbarkeit und umfangreichen Funktionen der Plattform rechtfertigen die Kosten für wachsende Teams.",

    # Answer 2: How long does implementation take?
    "Most teams can get started within a day. Basic setup takes minutes, while full enterprise deployment with custom integrations typically takes 1-2 weeks with proper planning.":
    "Die meisten Teams können innerhalb eines Tages beginnen. Die grundlegende Einrichtung dauert nur Minuten, während die vollständige Enterprise-Bereitstellung mit benutzerdefinierten Integrationen in der Regel 1-2 Wochen mit ordentlicher Planung dauert.",

    # Answer 3: What integrations are available?
    "integrates with 100+ popular platforms including Slack, Microsoft Teams, Salesforce, Google Workspace, and many more. A robust API enables custom integrations.":
    "integriert sich mit über 100 beliebten Plattformen, darunter Slack, Microsoft Teams, Salesforce, Google Workspace und viele mehr. Eine robuste API ermöglicht benutzerdefinierte Integrationen.",

    # Answer 4: Is my data secure?
    "Yes. uses bank-grade encryption, maintains SOC 2 Type II certification, and is compliant with GDPR, HIPAA, and other major regulations. Data is encrypted at rest and in transit.":
    "Ja. verwendet Bankensicherheit, hält SOC 2 Typ II Zertifizierung aufrecht und ist konform mit GDPR, HIPAA und anderen wichtigen Vorschriften. Daten sind im Ruhezustand und während der Übertragung verschlüsselt.",

    # Answer 5: Can I migrate from another platform?
    "Absolutely. provides migration tools and dedicated support to help you seamlessly transition from competing platforms with minimal downtime.":
    "Auf jeden Fall. bietet Migrationswerkzeuge und dedizierten Support, um Ihnen bei einem nahtlosen Übergang von konkurrierenden Plattformen mit minimaler Ausfallzeit zu helfen.",

    # Answer 6: What kind of support is available?
    "Professional plans include email support with 24-hour response time. Enterprise customers get dedicated account managers, priority support, and SLA guarantees.":
    "Professional-Pläne umfassen E-Mail-Support mit 24-Stunden-Reaktionszeit. Enterprise-Kunden erhalten dedizierte Account-Manager, Priority-Support und SLA-Garantien.",

    # Answer 7: Does offer a free trial?
    "Yes! You can try all Professional features free for 14 days with no credit card required. The free plan is available indefinitely for basic usage.":
    "Ja! Sie können alle Professional-Funktionen 14 Tage kostenlos ohne Kreditkarte testen. Der kostenlose Plan ist unbegrenzt für grundlegende Nutzung verfügbar.",

    # Answer 8: How does AI enhance the platform?
    "The AI engine learns from your usage patterns to suggest optimizations, automate repetitive tasks, predict outcomes, and provide intelligent recommendations that improve over time.":
    "Die KI-Engine lernt aus Ihren Nutzungsmustern, um Optimierungen vorzuschlagen, sich wiederholende Aufgaben zu automatisieren, Ergebnisse vorherzusagen und intelligente Empfehlungen zu geben, die sich im Laufe der Zeit verbessern."
}

def fix_faq_in_file(filepath, tool_key):
    """Fix FAQ translations in a single i18n file"""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Track changes
    changes_made = 0

    # Replace each FAQ answer in the German section
    for english_text, german_text in faq_translations.items():
        # Create the search pattern (in the "de" section)
        # The English text might have tool name placeholder
        pattern = f'": "{re.escape(english_text)}"'

        # Check if this pattern exists in content
        if pattern in content:
            # Replace with German translation
            replacement = f'": "{german_text}"'

            # Only replace in the German section
            # Split content into sections
            de_section_start = content.find('"de": {')

            if de_section_start != -1:
                # Find where German section ends (next closing brace at same level)
                brace_count = 0
                de_section_end = de_section_start
                for i in range(de_section_start, len(content)):
                    if content[i] == '{':
                        brace_count += 1
                    elif content[i] == '}':
                        brace_count -= 1
                        if brace_count == 0:
                            de_section_end = i
                            break

                # Get German section content
                before_de = content[:de_section_start]
                de_section = content[de_section_start:de_section_end+1]
                after_de = content[de_section_end+1:]

                # Replace in German section only
                old_de_section = de_section
                de_section = de_section.replace(pattern, replacement)

                if de_section != old_de_section:
                    changes_made += 1

                # Reconstruct content
                content = before_de + de_section + after_de

    # Write back if changes were made
    if changes_made > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    return changes_made

# Main execution
print("=" * 70)
print("FIXING FAQ TRANSLATIONS IN TRANSLATION TOOLS")
print("=" * 70)
print()

results = []

for tool in tools:
    filepath = os.path.join(js_dir, f"{tool}-i18n.js")

    if not os.path.exists(filepath):
        print(f"{tool}: [SKIP] File not found")
        continue

    print(f"Processing {tool}...")

    try:
        changes = fix_faq_in_file(filepath, tool)
        results.append({
            "tool": tool,
            "status": "SUCCESS",
            "changes": changes
        })
        print(f"  [OK] {changes} FAQ answers translated")
    except Exception as e:
        results.append({
            "tool": tool,
            "status": "FAILED",
            "error": str(e)
        })
        print(f"  [ERROR] {str(e)}")

    print()

# Summary
print("=" * 70)
print("SUMMARY")
print("=" * 70)
print()

success_count = sum(1 for r in results if r["status"] == "SUCCESS")
total_changes = sum(r.get("changes", 0) for r in results if r["status"] == "SUCCESS")

print(f"Tools processed: {success_count}/{len(results)}")
print(f"Total FAQ answers translated: {total_changes}")
print()

if total_changes > 0:
    print("FAQ translations successfully updated!")
else:
    print("No changes needed - FAQ translations already present")

print()
print("=" * 70)
