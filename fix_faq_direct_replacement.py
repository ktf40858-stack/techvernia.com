#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fix FAQ translations using direct string replacement
"""

import os

# Base directory
base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
js_dir = os.path.join(base_dir, "js")

# All 10 Translation tools with their names
tools = {
    "deepl-pro": "DeepL Pro",
    "google-translate-ai": "Google Translate AI",
    "lilt": "Lilt",
    "lokalise": "Lokalise",
    "microsoft-translator": "Microsoft Translator",
    "modernmt": "ModernMT",
    "phrase": "Phrase",
    "smartling": "Smartling",
    "systran": "SYSTRAN",
    "unbabel": "Unbabel"
}

def create_faq_replacements(tool_name):
    """Create FAQ replacement pairs for a specific tool"""

    replacements = []

    # FAQ Questions - English to German
    replacements.append((
        f'"Is {tool_name} worth the investment?"',
        f'"Lohnt sich die Investition in {tool_name}?"'
    ))

    replacements.append((
        '"How long does implementation take?"',
        '"Wie lange dauert die Implementierung?"'
    ))

    replacements.append((
        '"What integrations are available?"',
        '"Welche Integrationen sind verfügbar?"'
    ))

    replacements.append((
        '"Is my data secure?"',
        '"Sind meine Daten sicher?"'
    ))

    replacements.append((
        '"Can I migrate from another platform?"',
        '"Kann ich von einer anderen Plattform migrieren?"'
    ))

    replacements.append((
        '"What kind of support is available?"',
        '"Welche Art von Support ist verfügbar?"'
    ))

    replacements.append((
        f'"Does {tool_name} offer a free trial?"',
        f'"Bietet {tool_name} eine kostenlose Testversion an?"'
    ))

    replacements.append((
        '"How does AI enhance the platform?"',
        '"Wie verbessert KI die Plattform?"'
    ))

    # FAQ Answers - English to German
    replacements.append((
        '"For most organizations, yes. The AI-powered automation and productivity gains typically provide strong ROI within the first few months. The platform\'s scalability and extensive features justify the cost for growing teams."',
        '"Für die meisten Organisationen ja. Die KI-gestützte Automatisierung und Produktivitätsgewinne liefern in der Regel einen starken ROI innerhalb der ersten Monate. Die Skalierbarkeit und umfangreichen Funktionen der Plattform rechtfertigen die Kosten für wachsende Teams."'
    ))

    replacements.append((
        '"Most teams can get started within a day. Basic setup takes minutes, while full enterprise deployment with custom integrations typically takes 1-2 weeks with proper planning."',
        '"Die meisten Teams können innerhalb eines Tages beginnen. Die grundlegende Einrichtung dauert nur Minuten, während die vollständige Enterprise-Bereitstellung mit benutzerdefinierten Integrationen in der Regel 1-2 Wochen mit ordentlicher Planung dauert."'
    ))

    replacements.append((
        f'"{tool_name} integrates with 100+ popular platforms including Slack, Microsoft Teams, Salesforce, Google Workspace, and many more. A robust API enables custom integrations."',
        f'"{tool_name} integriert sich mit über 100 beliebten Plattformen, darunter Slack, Microsoft Teams, Salesforce, Google Workspace und viele mehr. Eine robuste API ermöglicht benutzerdefinierte Integrationen."'
    ))

    replacements.append((
        f'"Yes. {tool_name} uses bank-grade encryption, maintains SOC 2 Type II certification, and is compliant with GDPR, HIPAA, and other major regulations. Data is encrypted at rest and in transit."',
        f'"Ja. {tool_name} verwendet Bankensicherheit, hält SOC 2 Typ II Zertifizierung aufrecht und ist konform mit GDPR, HIPAA und anderen wichtigen Vorschriften. Daten sind im Ruhezustand und während der Übertragung verschlüsselt."'
    ))

    replacements.append((
        f'"Absolutely. {tool_name} provides migration tools and dedicated support to help you seamlessly transition from competing platforms with minimal downtime."',
        f'"Auf jeden Fall. {tool_name} bietet Migrationswerkzeuge und dedizierten Support, um Ihnen bei einem nahtlosen Übergang von konkurrierenden Plattformen mit minimaler Ausfallzeit zu helfen."'
    ))

    replacements.append((
        '"Professional plans include email support with 24-hour response time. Enterprise customers get dedicated account managers, priority support, and SLA guarantees."',
        '"Professional-Pläne umfassen E-Mail-Support mit 24-Stunden-Reaktionszeit. Enterprise-Kunden erhalten dedizierte Account-Manager, Priority-Support und SLA-Garantien."'
    ))

    replacements.append((
        '"Yes! You can try all Professional features free for 14 days with no credit card required. The free plan is available indefinitely for basic usage."',
        '"Ja! Sie können alle Professional-Funktionen 14 Tage kostenlos ohne Kreditkarte testen. Der kostenlose Plan ist unbegrenzt für grundlegende Nutzung verfügbar."'
    ))

    replacements.append((
        '"The AI engine learns from your usage patterns to suggest optimizations, automate repetitive tasks, predict outcomes, and provide intelligent recommendations that improve over time."',
        '"Die KI-Engine lernt aus Ihren Nutzungsmustern, um Optimierungen vorzuschlagen, sich wiederholende Aufgaben zu automatisieren, Ergebnisse vorherzusagen und intelligente Empfehlungen zu geben, die sich im Laufe der Zeit verbessern."'
    ))

    return replacements

def fix_faq_in_file(filepath, tool_key, tool_name):
    """Fix FAQ translations in a single i18n file using direct replacement"""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the German section
    de_start = content.find('"de": {')
    if de_start == -1:
        return 0

    # Find the end of the German section
    brace_count = 0
    de_end = de_start
    for i in range(de_start, len(content)):
        if content[i] == '{':
            brace_count += 1
        elif content[i] == '}':
            brace_count -= 1
            if brace_count == 0:
                de_end = i
                break

    # Extract sections
    before_de = content[:de_start]
    de_section = content[de_start:de_end+1]
    after_de = content[de_end+1:]

    # Get replacements for this tool
    replacements = create_faq_replacements(tool_name)

    # Apply replacements in German section only
    changes_made = 0
    for old_text, new_text in replacements:
        if old_text in de_section:
            de_section = de_section.replace(old_text, new_text)
            changes_made += 1

    # Reconstruct file
    new_content = before_de + de_section + after_de

    # Write if changes were made
    if changes_made > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return changes_made

# Main execution
print("=" * 70)
print("FIXING FAQ TRANSLATIONS WITH DIRECT REPLACEMENT")
print("=" * 70)
print()

results = []

for tool_key, tool_name in tools.items():
    filepath = os.path.join(js_dir, f"{tool_key}-i18n.js")

    if not os.path.exists(filepath):
        print(f"{tool_name}: [SKIP] File not found")
        continue

    print(f"Processing {tool_name}...")

    try:
        changes = fix_faq_in_file(filepath, tool_key, tool_name)
        results.append({
            "tool": tool_name,
            "status": "SUCCESS",
            "changes": changes
        })
        print(f"  [OK] {changes} FAQ items translated")
    except Exception as e:
        results.append({
            "tool": tool_name,
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
print(f"Total FAQ items translated: {total_changes}")
print()

if total_changes > 0:
    print("[SUCCESS] FAQ translations updated!")
else:
    print("[INFO] No changes needed")

print()
print("=" * 70)
