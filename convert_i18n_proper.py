"""
Proper conversion script to flatten nested i18n structures to dot-notation flat keys.
Manually extracts all keys from nested structure.
"""

import os
import re
import json

BASE_DIR = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\js"

def extract_language_block(content, lang_code):
    """Extract a complete language block including all nested structures."""
    # Find the language block with proper nesting handling
    pattern = rf'{lang_code}:\s*\{{'
    start = content.find(f'{lang_code}:')

    if start == -1:
        return None

    # Find the opening brace
    brace_start = content.find('{', start)
    if brace_start == -1:
        return None

    # Track braces to find the matching closing brace
    brace_count = 1
    pos = brace_start + 1

    while pos < len(content) and brace_count > 0:
        if content[pos] == '{':
            brace_count += 1
        elif content[pos] == '}':
            brace_count -= 1
        pos += 1

    if brace_count != 0:
        return None

    return content[brace_start+1:pos-1]

def parse_object_recursive(content, prefix=''):
    """Recursively parse JavaScript object notation to flat keys."""
    result = {}

    # Remove comments
    content = re.sub(r'//.*?\n', '\n', content)

    # Find all key-value pairs at this level
    # Match: key: "value" or key: { ... }
    pattern = r'(\w+):\s*(?:"([^"]*)"|(\{))'

    pos = 0
    while pos < len(content):
        match = re.search(pattern, content[pos:])
        if not match:
            break

        key = match.group(1)
        value = match.group(2)
        is_object = match.group(3)

        full_key = f"{prefix}.{key}" if prefix else key

        if value is not None:
            # It's a string value
            result[full_key] = value
            pos += match.end()
        elif is_object:
            # It's a nested object
            obj_start = pos + match.start() + len(match.group(0)) - 1

            # Find the matching closing brace
            brace_count = 1
            obj_pos = obj_start + 1

            while obj_pos < len(content) and brace_count > 0:
                if content[obj_pos] == '{':
                    brace_count += 1
                elif content[obj_pos] == '}':
                    brace_count -= 1
                obj_pos += 1

            nested_content = content[obj_start+1:obj_pos-1]
            nested_result = parse_object_recursive(nested_content, full_key)
            result.update(nested_result)

            pos = obj_pos
        else:
            pos += match.end()

    return result

def convert_file(file_path):
    """Convert a single file from nested to flat keys."""
    print(f"\nConverting: {os.path.basename(file_path)}")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()

        # Extract variable name and comment
        var_match = re.search(r'window\.(\w+)\s*=', original_content)
        comment_match = re.search(r'^//\s*(.+)', original_content)

        if not var_match:
            print(f"  [ERROR] Could not find window variable")
            return False

        var_name = var_match.group(1)
        comment = comment_match.group(1) if comment_match else "i18n"

        # Process each language
        languages = ['en', 'fr', 'de', 'es', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']
        lang_data = {}

        for lang in languages:
            lang_block = extract_language_block(original_content, lang)
            if lang_block:
                flat_data = parse_object_recursive(lang_block)
                lang_data[lang] = flat_data
            else:
                print(f"  [WARN] Could not extract {lang} block")

        if not lang_data:
            print(f"  [ERROR] No language data extracted")
            return False

        # Build new content
        lines = [f"// {comment}"]
        lines.append(f"window.{var_name} = {{")

        for i, lang in enumerate(languages):
            if lang in lang_data:
                lines.append(f"  {lang}: {{")

                # Sort keys and format
                sorted_keys = sorted(lang_data[lang].keys())
                for j, key in enumerate(sorted_keys):
                    value = lang_data[lang][key].replace('"', '\\"')
                    comma = "," if j < len(sorted_keys) - 1 else ""
                    lines.append(f'    "{key}": "{value}"{comma}')

                comma = "," if i < len(languages) - 1 else ""
                lines.append(f"  }}{comma}")

        lines.append("};")
        lines.append("")

        new_content = '\n'.join(lines)

        # Write the file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"  [OK] Converted successfully ({len(lang_data)} languages)")
        return True

    except Exception as e:
        print(f"  [ERROR] {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Main function."""
    files = [
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

    print("="*70)
    print("PROPER I18N FLATTENING SCRIPT")
    print("="*70)

    success = 0
    fail = 0

    for filename in files:
        file_path = os.path.join(BASE_DIR, filename)
        if os.path.exists(file_path):
            if convert_file(file_path):
                success += 1
            else:
                fail += 1
        else:
            print(f"\n[SKIP] File not found: {filename}")
            fail += 1

    print("\n" + "="*70)
    print(f"SUMMARY: {success} successful, {fail} failed")
    print("="*70)

if __name__ == "__main__":
    main()
