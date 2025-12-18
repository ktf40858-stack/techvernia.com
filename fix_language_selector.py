#!/usr/bin/env python3
"""
Fix the setupLanguageSelector function in i18n.js
"""

print("🔧 Fixing language selector in i18n.js...")

# Read the file
with open('GenuisNet.ai/js/i18n.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Old code
old_code = '''// Setup language selector
function setupLanguageSelector() {
    const langBtn = document.getElementById('lang-btn');
    const langDropdown = document.getElementById('lang-dropdown');
    const langSelector = document.querySelector('.language-selector');

    if (!langBtn || !langDropdown) return;

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
}'''

# New code
new_code = '''// Setup language selector
function setupLanguageSelector() {
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
}'''

# Replace
if old_code in content:
    content = content.replace(old_code, new_code)
    print("✅ Found and replaced setupLanguageSelector")
else:
    print("❌ Could not find the exact code to replace")
    print("Searching for partial match...")
    if "function setupLanguageSelector()" in content:
        print("✅ Function exists in file")
    else:
        print("❌ Function not found")

# Save
with open('GenuisNet.ai/js/i18n.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ File saved!")
