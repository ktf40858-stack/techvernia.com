#!/usr/bin/env python3
"""
Fix the setupLanguageSelector function in i18n.js properly
"""
import re

print("🔧 Fixing language selector properly in i18n.js...")

# Read the file
with open('GenuisNet.ai/js/i18n.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace the entire function
pattern = r'function setupLanguageSelector\(\) \{.*?\n\}\n\n// Update language selector display'

replacement = '''function setupLanguageSelector() {
    const langBtn = document.getElementById('lang-btn');
    const langDropdown = document.getElementById('lang-dropdown');
    const langSelector = document.querySelector('.language-selector');

    if (!langBtn || !langDropdown || !langSelector) {
        console.warn('⚠️ Language selector elements not found');
        return;
    }

    langBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        langSelector.classList.toggle('active');
    });

    document.addEventListener('click', () => {
        langSelector.classList.remove('active');
    });

    langDropdown.querySelectorAll('.lang-option').forEach(option => {
        option.addEventListener('click', () => {
            const lang = option.getAttribute('data-lang');
            setLanguage(lang);
            langSelector.classList.remove('active');
        });
    });

    console.log('✅ Language selector initialized');
}

// Update language selector display'''

# Replace using regex with DOTALL flag
new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

if new_content != content:
    print("✅ Function replaced successfully")
    with open('GenuisNet.ai/js/i18n.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("✅ File saved!")
else:
    print("❌ Could not find or replace the function")
    print("Trying alternative method...")

    # Alternative: find the broken function and fix it
    # Remove all the misplaced console.log statements
    content = re.sub(r'\n\s+console\.log\(\'✅ Language selector initialized\'\);(?=\s+option\.addEventListener)', '', content)
    content = re.sub(r'\n\s+console\.log\(\'✅ Language selector initialized\'\);(?=\s+const lang)', '', content)
    content = re.sub(r'\n\s+console\.log\(\'✅ Language selector initialized\'\);(?=\s+setLanguage)', '', content)
    content = re.sub(r'\n\s+console\.log\(\'✅ Language selector initialized\'\);(?=\s+langSelector\.classList)', '', content)

    # Add it once at the end of the function
    pattern2 = r'(langDropdown\.querySelectorAll\(\'\.lang-option\'\)\.forEach\(option => \{.*?}\);)\n(\s+)\}'
    replacement2 = r'\1\n\n\2console.log(\'✅ Language selector initialized\');\n\2}'
    content = re.sub(pattern2, replacement2, content, flags=re.DOTALL)

    with open('GenuisNet.ai/js/i18n.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print("✅ Cleaned up misplaced console.log statements!")

print("Done!")
