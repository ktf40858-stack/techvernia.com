import os

files = [
    "ada.html", "certainly.html", "cognigy.html", "drift.html",
    "forethought.html", "freshdesk-ai.html", "helpshift.html",
    "kustomer.html", "liveperson.html", "netomi.html",
    "polyai.html", "ultimateai.html", "yellowai.html", "zendesk-ai.html"
]

old_navbar = '''<ul class="nav-menu" id="nav-menu">
<li class="nav-item"><a class="nav-link active" data-i18n="nav.home" href="../../../index.html">Home</a></li>
<li class="nav-item"><a class="nav-link active" href="../../categories/ai-customer-service.html">Categories</a></li>
<li class="nav-item"><a class="nav-link" href="../../guides.html"><span data-i18n="nav.guides">Guides</span></a></li>
<li class="nav-item"><a class="nav-link" href="../../comparisons.html"><span data-i18n="nav.compare">Compare</span></a></li>
<li class="nav-item"><a class="nav-link" href="../../about.html"><span data-i18n="nav.about">About</span></a></li>
</ul>'''

new_navbar = '''<ul class="nav-menu" id="nav-menu">
<li class="nav-item"><a class="nav-link" href="../../../index.html"><span data-i18n="nav.home">Home</span></a></li>
<li class="nav-item"><a class="nav-link active" href="../../categories/ai-customer-service.html"><span data-i18n="nav.categories">Categories</span></a></li>
<li class="nav-item"><a class="nav-link" href="../../guides.html"><span data-i18n="nav.guides">Guides</span></a></li>
<li class="nav-item"><a class="nav-link" href="../../comparisons.html"><span data-i18n="nav.compare">Compare</span></a></li>
<li class="nav-item"><a class="nav-link" href="../../blog.html"><span data-i18n="nav.blog">Blog</span></a></li>
<li class="nav-item"><a class="nav-link" href="../../about.html"><span data-i18n="nav.about">About</span></a></li>
<li class="nav-item"><a class="nav-link" href="../../contact.html"><span data-i18n="nav.contact">Contact</span></a></li>
</ul>'''

base_dir = r"C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\pages\reviews\customer-service"

for filename in files:
    filepath = os.path.join(base_dir, filename)
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if old_navbar in content:
            content = content.replace(old_navbar, new_navbar)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[OK] Updated {filename}")
        else:
            print(f"[SKIP] Navbar not found in {filename}")
    except Exception as e:
        print(f"[ERROR] Error with {filename}: {e}")

print("\n[DONE] Updated all navbars.")
