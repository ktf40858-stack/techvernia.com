"""
Add tool-specific i18n script tags to Cybersecurity HTML files
"""
import re
import os

# All 30 Cybersecurity tools
TOOLS = [
    'abnormal-security', 'carbon-black', 'cisco-securex', 'cortex-xdr',
    'crowdstrike', 'cyberark', 'cybereason', 'cylance', 'darktrace',
    'exabeam', 'fortinet', 'ibm-qradar', 'lacework', 'mcafee-mvision',
    'microsoft-sentinel', 'okta', 'palo-alto-ngfw', 'qualys', 'rapid7',
    'recorded-future', 'sentinelone', 'snyk', 'sophos-interceptx',
    'splunk-security', 'symantec-endpoint', 'tenable',
    'trend-micro-vision-one', 'vectra-ai', 'wiz', 'zerofox'
]

def add_tool_i18n_script(tool_name):
    """Add tool-specific i18n script before i18n.js"""
    html_path = f"GenuisNet.ai/pages/reviews/cybersecurity/{tool_name}.html"

    if not os.path.exists(html_path):
        return False

    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Check if tool i18n script already exists
    if f'{tool_name}-i18n.js' in html:
        return 'already_exists'

    # Find <script src="../../../js/i18n.js"></script>
    # Insert tool-specific i18n script before it
    pattern = r'(<script src="../../../js/)i18n\.js"></script>'

    if re.search(pattern, html):
        # Insert tool-specific script before i18n.js
        replacement = rf'\1{tool_name}-i18n.js"></script>\n    <script src="../../../js/i18n.js"></script>'
        modified_html = re.sub(pattern, replacement, html)

        # Save modified HTML
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(modified_html)

        return True
    else:
        return False

# Main processing
print("\n" + "=" * 60)
print("ADD TOOL-SPECIFIC I18N SCRIPTS")
print("=" * 60)

added = 0
existed = 0
failed = 0

for tool in TOOLS:
    result = add_tool_i18n_script(tool)

    if result == True:
        print(f"{tool}: [OK] Script added")
        added += 1
    elif result == 'already_exists':
        print(f"{tool}: [SKIP] Script already exists")
        existed += 1
    else:
        print(f"{tool}: [FAIL] Could not add script")
        failed += 1

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"Added: {added}")
print(f"Already existed: {existed}")
print(f"Failed: {failed}")
print("=" * 60)
