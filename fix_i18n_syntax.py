#!/usr/bin/env python3
"""
Fix the syntax error in i18n.js by adding missing translations declaration
"""

print("🔧 Fixing i18n.js syntax error...")

# Read the file
with open('GenuisNet.ai/js/i18n.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Check if it already starts with const translations
if content.strip().startswith('const translations'):
    print("✅ File already has translations declaration")
else:
    print("❌ Missing translations declaration, adding it...")

    # Add const translations = { at the beginning
    new_content = "const translations = {\n" + content

    # Find the last occurrence of setupLanguageSelector function and add closing brace before it
    # We need to find where the translations object should close

    # Better approach: find where the functions start (after all language sections)
    import re

    # Find the line with "function initI18n"
    match = re.search(r'\nfunction initI18n\(\)', new_content)
    if match:
        pos = match.start()
        # Add closing brace and semicolon before the functions
        new_content = new_content[:pos] + "\n};\n" + new_content[pos:]
        print("✅ Added closing brace for translations object")
    else:
        print("❌ Could not find where to close translations object")

    # Save
    with open('GenuisNet.ai/js/i18n.js', 'w', encoding='utf-8') as f:
        f.write(new_content)

    print("✅ File saved!")

print("Done!")
