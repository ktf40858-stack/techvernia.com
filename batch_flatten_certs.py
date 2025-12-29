"""
Batch conversion script to flatten nested i18n structures to dot-notation flat keys
for all remaining certification JavaScript files.
"""

import os
import re

# Base directory
BASE_DIR = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\js"

# Files already completed
COMPLETED = ["jncip-mistai-i18n.js"]

# Files to process (from user's request)
FILES_TO_PROCESS = [
    "jncis-mistai-wireless-i18n.js",
    "ansible-automation-i18n.js",
    "ansible-advanced-i18n.js",
    "terraform-associate-i18n.js",
    "terraform-professional-i18n.js",
    "zabbix-specialist-i18n.js",
    "zabbix-professional-i18n.js",
    "zabbix-expert-i18n.js",
    "rhce-i18n.js"
]

def convert_nested_to_flat(nested_structure):
    """
    Convert nested JavaScript object to flat dot-notation keys.
    Input: String containing the nested object (one language block)
    Output: Dictionary with flat keys
    """
    result = {}

    # Remove comments and normalize
    content = re.sub(r'//.*?\n', '\n', nested_structure)

    # Extract nav.back_to_review
    nav_match = re.search(r'nav:\s*\{\s*back_to_review:\s*"([^"]*)"', content)
    if nav_match:
        result['nav.back_to_review'] = nav_match.group(1)

    # Extract nested cert object (cert.CERTTYPE.*)
    cert_nested_pattern = r'(\w+):\s*\{([^}]+)\}'
    cert_block_match = re.search(r'cert:\s*\{(.*?)\n\s*\},?\s*footer:', content, re.DOTALL)

    if cert_block_match:
        cert_content = cert_block_match.group(1)

        # Find the nested certification type (e.g., jncis, ansible, terraform, etc.)
        nested_match = re.search(r'(\w+):\s*\{([^}]+(?:\{[^}]*\}[^}]*)*)\}', cert_content, re.DOTALL)

        if nested_match:
            cert_type = nested_match.group(1)
            nested_props = nested_match.group(2)

            # Extract properties from nested object
            prop_pattern = r'(\w+):\s*"([^"]*)"'
            for match in re.finditer(prop_pattern, nested_props):
                prop_name = match.group(1)
                prop_value = match.group(2)
                result[f'cert.{cert_type}.{prop_name}'] = prop_value

        # Extract direct cert properties (overview, key_topics, etc.)
        # Remove nested cert object first
        direct_cert = re.sub(r'\w+:\s*\{[^}]+(?:\{[^}]*\}[^}]*)*\}', '', cert_content)

        prop_pattern = r'(\w+):\s*"([^"]*)"'
        for match in re.finditer(prop_pattern, direct_cert):
            prop_name = match.group(1)
            prop_value = match.group(2)
            result[f'cert.{prop_name}'] = prop_value

    # Extract footer
    footer_match = re.search(r'footer:\s*\{\s*copyright:\s*"([^"]*)"\s*,\s*trademark:\s*"([^"]*)"\s*\}', content, re.DOTALL)
    if footer_match:
        result['footer.copyright'] = footer_match.group(1)
        result['footer.trademark'] = footer_match.group(2)

    return result

def format_flat_object(flat_dict, indent='    '):
    """Format flat dictionary as JavaScript object with sorted keys."""
    lines = []
    for key in sorted(flat_dict.keys()):
        value = flat_dict[key].replace('"', '\\"')  # Escape quotes
        lines.append(f'{indent}"{key}": "{value}"')
    return ',\n'.join(lines)

def process_file(file_path):
    """Process a single file to convert nested to flat structure."""
    print(f"\nProcessing: {os.path.basename(file_path)}")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract variable name from first line
        var_match = re.search(r'window\.(\w+)\s*=', content)
        if not var_match:
            print(f"  ERROR: Could not find window variable name")
            return False

        var_name = var_match.group(1)

        # Extract comment from first line
        comment_match = re.search(r'^//\s*(.+)', content)
        comment = comment_match.group(1) if comment_match else f"{os.path.basename(file_path)} i18n"

        # Process each language
        languages = ['en', 'fr', 'de', 'es', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']
        lang_blocks = {}

        for lang in languages:
            # Extract language block
            pattern = rf'{lang}:\s*\{{(.*?)^\s*\}}(?:,|\s*\}})'
            match = re.search(pattern, content, re.MULTILINE | re.DOTALL)

            if match:
                lang_content = match.group(1)
                flat_dict = convert_nested_to_flat(lang_content)
                lang_blocks[lang] = flat_dict
            else:
                print(f"  WARNING: Could not extract {lang} block")
                return False

        # Generate new file content
        new_lines = [f"// {comment}"]
        new_lines.append(f"window.{var_name} = {{")

        for i, lang in enumerate(languages):
            if lang in lang_blocks:
                new_lines.append(f"  {lang}: {{")
                new_lines.append(format_flat_object(lang_blocks[lang]))
                new_lines.append("  }" + ("" if i == len(languages) - 1 else ","))

        new_lines.append("};")
        new_lines.append("")  # Empty line at end

        new_content = '\n'.join(new_lines)

        # Create backup
        backup_path = file_path + '.backup'
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  [OK] Backup created: {os.path.basename(backup_path)}")

        # Write new content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  [OK] File converted to flat keys")

        return True

    except Exception as e:
        print(f"  [ERROR] {str(e)}")
        return False

def main():
    """Main function to process all files."""
    print("=" * 70)
    print("BATCH CERTIFICATION I18N FLATTENING SCRIPT")
    print("=" * 70)
    print(f"\nProcessing {len(FILES_TO_PROCESS)} files...")

    success_count = 0
    fail_count = 0

    for filename in FILES_TO_PROCESS:
        file_path = os.path.join(BASE_DIR, filename)

        if not os.path.exists(file_path):
            print(f"\n[SKIP] File not found: {filename}")
            fail_count += 1
            continue

        if process_file(file_path):
            success_count += 1
        else:
            fail_count += 1

    print("\n" + "=" * 70)
    print(f"SUMMARY: {success_count} successful, {fail_count} failed")
    print("=" * 70)

if __name__ == "__main__":
    main()
