#!/usr/bin/env python3
"""
Add a debug script at the end of adobe-firefly.html to test language selector
"""

print("🔧 Adding debug script to adobe-firefly.html...")

# Read the file
with open('GenuisNet.ai/pages/reviews/image/adobe-firefly.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Check if debug script already exists
if '<!-- DEBUG LANGUAGE SELECTOR -->' in content:
    print("⚠️ Debug script already exists, removing old one...")
    # Remove old debug script
    import re
    content = re.sub(r'<!-- DEBUG LANGUAGE SELECTOR -->.*?<!-- END DEBUG -->', '', content, flags=re.DOTALL)

# Debug script to add
debug_script = '''
<!-- DEBUG LANGUAGE SELECTOR -->
<script>
console.log('🔍 DEBUG: Script de diagnostic chargé');

// Wait for DOM to be ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', runDiagnostics);
} else {
    runDiagnostics();
}

function runDiagnostics() {
    console.log('🔍 DEBUG: DOM prêt, lancement diagnostics...');

    // Check if elements exist
    const langBtn = document.getElementById('lang-btn');
    const langDropdown = document.getElementById('lang-dropdown');
    const langSelector = document.querySelector('.language-selector');

    console.log('🔍 DEBUG: langBtn =', langBtn);
    console.log('🔍 DEBUG: langDropdown =', langDropdown);
    console.log('🔍 DEBUG: langSelector =', langSelector);

    if (!langBtn) {
        console.error('❌ lang-btn NOT FOUND!');
        return;
    }
    if (!langDropdown) {
        console.error('❌ lang-dropdown NOT FOUND!');
        return;
    }
    if (!langSelector) {
        console.error('❌ language-selector NOT FOUND!');
        return;
    }

    console.log('✅ All elements found!');

    // Check if i18n is loaded
    console.log('🔍 DEBUG: window.i18n =', window.i18n);

    // Add manual click handler for testing
    console.log('🔍 DEBUG: Adding manual click handler...');
    langBtn.addEventListener('click', function(e) {
        console.log('🔍 DEBUG: BOUTON CLIQUÉ!');
        e.stopPropagation();
        langSelector.classList.toggle('active');
        const isActive = langSelector.classList.contains('active');
        console.log('🔍 DEBUG: Menu est maintenant:', isActive ? 'OUVERT' : 'FERMÉ');
    });

    console.log('✅ Manual handler added!');
}
</script>
<!-- END DEBUG -->
'''

# Add debug script before </body>
if '</body>' in content:
    content = content.replace('</body>', debug_script + '\n</body>')
    print("✅ Debug script added")
else:
    print("❌ Could not find </body> tag")

# Save
with open('GenuisNet.ai/pages/reviews/image/adobe-firefly.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ File saved!")
print("\nOuvrez adobe-firefly.html et regardez la console (F12) pour voir les logs de diagnostic.")
