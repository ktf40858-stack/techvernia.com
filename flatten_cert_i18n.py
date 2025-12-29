"""
Script to flatten nested i18n objects to dot-notation flat keys
for certification JavaScript files.
"""

import re
import json

def flatten_dict(nested_dict, parent_key='', separator='.'):
    """
    Flatten a nested dictionary into dot-notation keys.
    """
    items = []
    for key, value in nested_dict.items():
        new_key = f"{parent_key}{separator}{key}" if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, separator=separator).items())
        else:
            items.append((new_key, value))
    return dict(items)

def extract_nested_structure(content, lang_code):
    """
    Extract the nested structure for a specific language from the JS file.
    Returns a dictionary representation.
    """
    # Find the language block
    pattern = rf'{lang_code}:\s*\{{([^}}]+(?:\{{[^}}]*\}}[^}}]*)*)\}}'
    match = re.search(pattern, content, re.DOTALL)

    if not match:
        return None

    lang_block = match.group(1)

    # Parse the nested structure manually
    result = {}

    # Extract nav section
    nav_match = re.search(r'nav:\s*\{\s*back_to_review:\s*"([^"]*)"', lang_block)
    if nav_match:
        result['nav.back_to_review'] = nav_match.group(1)

    # Extract cert section with nested properties
    cert_pattern = r'cert:\s*\{([^}]+(?:\{[^}]*\}[^}]*)*)\}'
    cert_match = re.search(cert_pattern, lang_block, re.DOTALL)

    if cert_match:
        cert_block = cert_match.group(1)

        # Find nested cert type (e.g., jncip, jncis, ansible, etc.)
        nested_cert_pattern = r'(\w+):\s*\{([^}]+)\}'
        nested_cert_match = re.search(nested_cert_pattern, cert_block, re.DOTALL)

        if nested_cert_match:
            cert_type = nested_cert_match.group(1)
            nested_props = nested_cert_match.group(2)

            # Extract all properties from the nested cert object
            prop_pattern = r'(\w+):\s*"([^"]*)"'
            for prop_match in re.finditer(prop_pattern, nested_props):
                prop_name = prop_match.group(1)
                prop_value = prop_match.group(2)
                result[f'cert.{cert_type}.{prop_name}'] = prop_value

        # Extract direct cert properties
        direct_props = re.sub(r'\w+:\s*\{[^}]+\}', '', cert_block)
        prop_pattern = r'(\w+):\s*"([^"]*)"'
        for prop_match in re.finditer(prop_pattern, direct_props):
            prop_name = prop_match.group(1)
            prop_value = prop_match.group(2)
            result[f'cert.{prop_name}'] = prop_value

    # Extract footer section
    footer_pattern = r'footer:\s*\{\s*copyright:\s*"([^"]*)"\s*,\s*trademark:\s*"([^"]*)"\s*\}'
    footer_match = re.search(footer_pattern, lang_block, re.DOTALL)

    if footer_match:
        result['footer.copyright'] = footer_match.group(1)
        result['footer.trademark'] = footer_match.group(2)

    return result

def generate_flat_lang_block(flat_dict, indent='    '):
    """
    Generate a formatted language block with flat keys.
    """
    lines = []
    for key, value in sorted(flat_dict.items()):
        # Escape quotes in value
        escaped_value = value.replace('"', '\\"')
        lines.append(f'{indent}"{key}": "{escaped_value}"')
    return ',\n'.join(lines)

def process_file(file_path, variable_name):
    """
    Process a single i18n file to convert from nested to flat structure.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract language blocks
    languages = ['en', 'fr', 'de', 'es', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']

    new_content_parts = []
    new_content_parts.append(f"// {file_path.split('/')[-1].split('.')[0].replace('-', ' ').title()} i18n")
    new_content_parts.append(f"window.{variable_name} = {{")

    for lang in languages:
        flat_dict = extract_nested_structure(content, lang)
        if flat_dict:
            new_content_parts.append(f"  {lang}: {{")
            new_content_parts.append(generate_flat_lang_block(flat_dict, '    '))
            new_content_parts.append("  }" + ("," if lang != 'hi' else ""))

    new_content_parts.append("};")
    new_content_parts.append("")  # Empty line at end

    return '\n'.join(new_content_parts)

# File configurations
files_to_process = [
    ('C:/Users/Freddy/Desktop/GeniusNet.ai/GenuisNet.ai/js/jncip-mistai-i18n.js', 'jncipMistaiTranslations'),
    ('C:/Users/Freddy/Desktop/GeniusNet.ai/GenuisNet.ai/js/jncis-mistai-wireless-i18n.js', 'jncisMistaiWirelessTranslations'),
    ('C:/Users/Freddy/Desktop/GeniusNet.ai/GenuisNet.ai/js/ansible-automation-i18n.js', 'ansibleAutomationTranslations'),
    ('C:/Users/Freddy/Desktop/GeniusNet.ai/GenuisNet.ai/js/ansible-advanced-i18n.js', 'ansibleAdvancedTranslations'),
    ('C:/Users/Freddy/Desktop/GeniusNet.ai/GenuisNet.ai/js/terraform-associate-i18n.js', 'terraformAssociateTranslations'),
    ('C:/Users/Freddy/Desktop/GeniusNet.ai/GenuisNet.ai/js/terraform-professional-i18n.js', 'terraformProfessionalTranslations'),
    ('C:/Users/Freddy/Desktop/GeniusNet.ai/GenuisNet.ai/js/zabbix-specialist-i18n.js', 'zabbixSpecialistTranslations'),
    ('C:/Users/Freddy/Desktop/GeniusNet.ai/GenuisNet.ai/js/zabbix-professional-i18n.js', 'zabbixProfessionalTranslations'),
    ('C:/Users/Freddy/Desktop/GeniusNet.ai/GenuisNet.ai/js/zabbix-expert-i18n.js', 'zabbixExpertTranslations'),
    ('C:/Users/Freddy/Desktop/GeniusNet.ai/GenuisNet.ai/js/rhce-i18n.js', 'rhceTranslations'),
]

print("Processing certification i18n files...")
print("=" * 60)

for file_path, var_name in files_to_process:
    print(f"\nProcessing: {file_path.split('/')[-1]}")
    try:
        new_content = process_file(file_path, var_name)
        # Write backup
        with open(file_path + '.backup', 'w', encoding='utf-8') as f:
            with open(file_path, 'r', encoding='utf-8') as orig:
                f.write(orig.read())
        print(f"  ✓ Backup created: {file_path}.backup")

        # Write new content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  ✓ File converted to flat keys")
    except Exception as e:
        print(f"  ✗ Error: {e}")

print("\n" + "=" * 60)
print("Processing complete!")
print("\nAll files have been converted from nested objects to flat keys.")
print("Backup files (.backup) have been created for each file.")
