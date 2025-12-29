import os
import re

base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai"
sales_dir = os.path.join(base_dir, "pages", "reviews", "sales")

tools = [
    "6sense",
    "apolloio",
    "attention",
    "chorusai",
    "clari",
    "conversica",
    "exceedai",
    "gong",
    "hubspot-ai",
    "insidesales",
    "lavender",
    "outreach",
    "peopleai",
    "regieai",
    "salesforce-einstein-gpt",
    "troopsai"
]

# HTML du sélecteur de langue à ajouter
language_selector_html = '''<div class="language-selector">
<button class="language-btn" id="language-btn">
<svg class="icon" fill="none" height="20" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="20">
<circle cx="12" cy="12" r="10"></circle>
<line x1="2" x2="22" y1="12" y2="12"></line>
<path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
</svg>
<span id="current-language">EN</span>
<svg class="chevron" fill="none" height="16" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="16">
<polyline points="6 9 12 15 18 9"></polyline>
</svg>
</button>
<div class="language-dropdown" id="language-dropdown">
<div class="language-option" data-lang="en">
<span class="flag">🇬🇧</span>
<span>English</span>
</div>
<div class="language-option" data-lang="de">
<span class="flag">🇩🇪</span>
<span>Deutsch</span>
</div>
<div class="language-option" data-lang="es">
<span class="flag">🇪🇸</span>
<span>Español</span>
</div>
<div class="language-option" data-lang="fr">
<span class="flag">🇫🇷</span>
<span>Français</span>
</div>
<div class="language-option" data-lang="pt">
<span class="flag">🇵🇹</span>
<span>Português</span>
</div>
<div class="language-option" data-lang="zh">
<span class="flag">🇨🇳</span>
<span>中文</span>
</div>
<div class="language-option" data-lang="ja">
<span class="flag">🇯🇵</span>
<span>日本語</span>
</div>
<div class="language-option" data-lang="ko">
<span class="flag">🇰🇷</span>
<span>한국어</span>
</div>
<div class="language-option" data-lang="ar">
<span class="flag">🇸🇦</span>
<span>العربية</span>
</div>
<div class="language-option" data-lang="hi">
<span class="flag">🇮🇳</span>
<span>हिन्दी</span>
</div>
</div>
</div>'''

def add_language_selector(html_file, tool):
    """Ajoute le sélecteur de langue et le script i18n au fichier HTML"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False

    # Vérifier si le sélecteur de langue existe déjà
    if 'language-selector' not in content:
        # Trouver la position après </ul> de la nav-menu
        pattern = r'(</ul>\s*</div>\s*</nav>)'
        match = re.search(pattern, content)

        if match:
            # Insérer le sélecteur avant </div></nav>
            insertion_point = match.start()
            content = content[:insertion_point] + language_selector_html + '\n' + content[insertion_point:]
            modified = True
            print(f"  [+] Added language selector")
        else:
            print(f"  [!] Could not find nav-menu closing tag")

    # Vérifier si le script i18n de l'outil existe
    if f'{tool}-i18n.js' not in content:
        # Trouver la ligne avec i18n.js
        pattern = r'(<script src="../../../js/i18n\.js"></script>)'
        match = re.search(pattern, content)

        if match:
            # Insérer le script de l'outil après i18n.js
            insertion_point = match.end()
            new_script = f'\n<script src="../../../js/{tool}-i18n.js"></script>'
            content = content[:insertion_point] + new_script + content[insertion_point:]
            modified = True
            print(f"  [+] Added {tool}-i18n.js script")
        else:
            print(f"  [!] Could not find i18n.js script tag")

    if modified:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    else:
        print(f"  [OK] Already has language selector and script")
        return False

# MAIN
print("=" * 70)
print("ADDING LANGUAGE SELECTOR & I18N SCRIPTS TO SALES TOOLS")
print("=" * 70)

total_modified = 0
for tool in tools:
    html_file = os.path.join(sales_dir, f"{tool}.html")

    if os.path.exists(html_file):
        print(f"\n{tool}.html:")
        if add_language_selector(html_file, tool):
            total_modified += 1
    else:
        print(f"\n{tool}.html: [SKIP] File not found")

print("\n" + "=" * 70)
print(f"[COMPLETE] Modified {total_modified} files")
print("=" * 70)
