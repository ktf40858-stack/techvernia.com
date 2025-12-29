"""
Create temporary i18n files for Cybersecurity tools
These allow pages to load without errors while waiting for translations
"""
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

def create_temp_i18n_file(tool_name):
    """Create a temporary i18n file with empty translations"""

    js_file = f"GenuisNet.ai/js/{tool_name}-i18n.js"

    # Check if file already exists
    if os.path.exists(js_file):
        return 'already_exists'

    # Create variable name (convert hyphens to underscores)
    var_name = tool_name.replace('-', '_')
    func_name = tool_name.replace('-', '_').title().replace('_', '')

    # Create temporary file with empty translations
    content = f"""// Temporary {tool_name} i18n file
// This will be replaced with full translations once agents complete

const {var_name}_translations = {{
    // Translations will be added here
}};

function get{func_name}Translation(key, lang) {{
    if ({var_name}_translations[lang] && {var_name}_translations[lang][key]) {{
        return {var_name}_translations[lang][key];
    }}
    return null;
}}

function apply{func_name}Translations(lang) {{
    console.log('🔄 {tool_name} translations loading... (waiting for agents to complete)');
    // Translations will be applied once available
}}

window.addEventListener('languageChanged', (e) => {{
    const lang = e.detail.language;
    setTimeout(() => apply{func_name}Translations(lang), 200);
}});

console.log('⏳ {tool_name} i18n loaded (temporary - awaiting translations)');
"""

    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(content)

    return True

# Main processing
print("\n" + "=" * 60)
print("CREATE TEMPORARY I18N FILES")
print("=" * 60)

created = 0
existed = 0

for tool in TOOLS:
    result = create_temp_i18n_file(tool)

    if result == True:
        print(f"{tool}: [OK] Temporary file created")
        created += 1
    elif result == 'already_exists':
        print(f"{tool}: [SKIP] File already exists")
        existed += 1

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"Created: {created}")
print(f"Already existed: {existed}")
print("\n" + "=" * 60)
print("Temporary i18n files created!")
print("These will be replaced with full translations once agents complete.")
print("=" * 60)
