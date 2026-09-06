#!/usr/bin/env python3
"""
Controle qualite des 50 nouvelles fiches avant validation editoriale.

Verifie : noindex actif, absence du sitemap, JSON-LD valide, liens internes
resolus, logos presents, et surtout absence de contenu duplique entre fiches
(le rejet AdSense de mai portait sur du contenu duplique).
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(ROOT, "docs")
REVIEWS = os.path.join(DOCS, "pages", "reviews")
LOGOS = os.path.join(DOCS, "assets", "images", "logos")

sys.path.insert(0, ROOT)


def load_slugs():
    tools = []
    for i in range(1, 21):
        p = os.path.join(ROOT, "tools_data_%02d.py" % i)
        if not os.path.exists(p):
            continue
        ns = {}
        exec(compile(io.open(p, encoding="utf-8").read(), p, "exec"), ns)
        tools.extend(ns["TOOLS"])
    return tools


LD = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)
REL = re.compile(r'class="related-tool-name"><a href="((?:\.\./)?[a-z0-9-]+(?:/[a-z0-9-]+)?)\.html"')
IMG = re.compile(r'src="\.\./\.\./\.\./assets/images/logos/([a-z0-9-]+)\.png"')
PARA = re.compile(r"<p>(.{80,})</p>")

tools = load_slugs()
errors, warnings = [], []

# sitemap : les nouvelles pages ne doivent PAS y etre pendant le crawl
sitemap = ""
for f in ("sitemap.xml", "sitemap-en.xml"):
    p = os.path.join(DOCS, f)
    if os.path.exists(p):
        sitemap += io.open(p, encoding="utf-8", errors="replace").read()

paragraphs = {}
total_words = 0

for t in tools:
    path = os.path.join(REVIEWS, t["category"], t["slug"] + ".html")
    name = "%s/%s" % (t["category"], t["slug"])
    if not os.path.exists(path):
        errors.append("%s : fichier absent" % name)
        continue
    html = io.open(path, encoding="utf-8").read()
    total_words += len(re.sub(r"<[^>]+>", " ", html).split())

    if 'content="noindex, nofollow" name="robots"' not in html:
        errors.append("%s : noindex ABSENT" % name)
    if "/%s/%s.html" % (t["category"], t["slug"]) in sitemap:
        errors.append("%s : present dans le sitemap pendant le crawl" % name)

    for block in LD.findall(html):
        try:
            json.loads(block)
        except ValueError as ex:
            errors.append("%s : JSON-LD invalide (%s)" % (name, ex))

    d = os.path.dirname(path)
    for rel in REL.findall(html):
        if not os.path.exists(os.path.normpath(os.path.join(d, rel + ".html"))):
            errors.append("%s : lien related casse -> %s.html" % (name, rel))

    for logo in set(IMG.findall(html)):
        if not os.path.exists(os.path.join(LOGOS, logo + ".png")):
            warnings.append("%s : logo manquant -> %s.png" % (name, logo))

    if not os.path.exists(os.path.join(LOGOS, t["slug"] + ".png")):
        errors.append("%s : logo principal absent" % name)

    for para in PARA.findall(html):
        key = re.sub(r"\s+", " ", para).strip()[:120]
        paragraphs.setdefault(key, []).append(name)

dupes = {k: v for k, v in paragraphs.items() if len(set(v)) > 1}

print("=" * 70)
print("CONTROLE DES 50 NOUVELLES FICHES")
print("=" * 70)
print("fiches verifiees        : %d" % len(tools))
print("mots totaux (rendu)     : ~%d" % total_words)
print("moyenne par fiche       : ~%d mots" % (total_words // max(len(tools), 1)))
print("paragraphes uniques     : %d" % len(paragraphs))
print("paragraphes partages    : %d" % len(dupes))
print()
if dupes:
    print("!! CONTENU DUPLIQUE entre fiches :")
    for k, v in list(dupes.items())[:10]:
        print("   %s ... -> %s" % (k[:70], ", ".join(sorted(set(v)))))
    print()
print("erreurs bloquantes      : %d" % len(errors))
for e in errors[:30]:
    print("   KO  %s" % e)
print("avertissements          : %d" % len(warnings))
for w in warnings[:15]:
    print("   --  %s" % w)
print()
print("VERDICT : %s" % ("PRET POUR RELECTURE" if not errors and not dupes
                        else "CORRECTIONS NECESSAIRES"))
sys.exit(1 if (errors or dupes) else 0)
