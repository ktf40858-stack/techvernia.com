#!/usr/bin/env python3
"""Add nav-i18n.js script reference to Customer Service & Support pages"""

import os
import re
import sys

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

CUSTOMER_SERVICE_DIR = 'GenuisNet.ai/pages/reviews/customer-service'

TOOLS = [
    'ada', 'certainly', 'cognigy', 'drift', 'forethought', 'freshdesk-ai',
    'helpshift', 'intercom-fin', 'kustomer', 'liveperson', 'netomi',
    'polyai', 'ultimateai', 'yellowai', 'zendesk-ai'
]

NAV_I18N_SCRIPT = '<script src="../../../js/nav-i18n.js"></script>'

def add_nav_i18n_script(html_file):
    """Add nav-i18n.js script after i18n.js if not already present"""

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if nav-i18n.js is already included
    if 'nav-i18n.js' in content:
        return 'already_exists'

    # Find i18n.js script tag and add nav-i18n.js after it
    i18n_pattern = r'(<script src="../../../js/i18n\.js"></script>)'

    if re.search(i18n_pattern, content):
        # Add nav-i18n.js right after i18n.js
        content = re.sub(
            i18n_pattern,
            r'\1\n    ' + NAV_I18N_SCRIPT,
            content
        )

        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        return 'added'

    return 'not_found'

print("=" * 70)
print("CUSTOMER SERVICE & SUPPORT - ADD NAV I18N SCRIPT")
print("=" * 70)

added = 0
already_exists = 0
failed = 0

for tool in TOOLS:
    html_file = os.path.join(CUSTOMER_SERVICE_DIR, f'{tool}.html')

    if not os.path.exists(html_file):
        print(f"\n❌ {tool}: File not found")
        failed += 1
        continue

    try:
        result = add_nav_i18n_script(html_file)

        if result == 'added':
            print(f"\n✅ {tool}: nav-i18n.js added")
            added += 1
        elif result == 'already_exists':
            print(f"\n✓  {tool}: nav-i18n.js already exists")
            already_exists += 1
        else:
            print(f"\n⚠️  {tool}: i18n.js not found")
            failed += 1

    except Exception as e:
        print(f"\n❌ {tool}: Error - {str(e)}")
        failed += 1

print("\n" + "=" * 70)
print(f"SUMMARY: {added} added, {already_exists} existed, {failed} failed")
print("=" * 70)
