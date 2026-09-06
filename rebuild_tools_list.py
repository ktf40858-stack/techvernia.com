#!/usr/bin/env python3
"""
Regenere docs/tools_list.csv et docs/tools_list.json a partir de l'etat reel
de docs/pages/reviews/. L'ancien fichier etait fige a 253 entrees alors que
le site en compte 472+.

Ne touche ni au sitemap, ni aux pages : c'est un artefact de build.
"""
import csv
import json
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(ROOT, "docs")
REVIEWS = os.path.join(DOCS, "pages", "reviews")
LOGOS = os.path.join(DOCS, "assets", "images", "logos")
SHOTS = os.path.join(DOCS, "images", "screenshots")

TITLE_RE = re.compile(r"<title>(.*?)</title>", re.S | re.I)
CANON_RE = re.compile(r'rel="canonical"[^>]*href="([^"]+)"', re.I)
NOINDEX_RE = re.compile(r'name="robots"[^>]*content="[^"]*noindex', re.I)


def logo_for(slug):
    if not os.path.isdir(LOGOS):
        return ""
    for ext in ("png", "svg", "jpg", "webp", "avif", "ico"):
        p = os.path.join(LOGOS, slug + "." + ext)
        if os.path.exists(p):
            return "assets/images/logos/%s.%s" % (slug, ext)
    return ""


def screenshot_for(cat, slug):
    for ext in ("png", "jpg", "webp"):
        p = os.path.join(SHOTS, cat, slug + "." + ext)
        if os.path.exists(p):
            return "images/screenshots/%s/%s.%s" % (cat, slug, ext)
    return ""


rows = []
for cat in sorted(os.listdir(REVIEWS)):
    cdir = os.path.join(REVIEWS, cat)
    if not os.path.isdir(cdir):
        continue
    for fn in sorted(os.listdir(cdir)):
        if not fn.endswith(".html"):
            continue
        slug = fn[:-5]
        path = os.path.join(cdir, fn)
        try:
            html = open(path, encoding="utf-8", errors="replace").read()
        except OSError:
            html = ""
        m = TITLE_RE.search(html)
        title = re.sub(r"\s+", " ", m.group(1)).strip() if m else ""
        logo = logo_for(slug)
        shot = screenshot_for(cat, slug)
        rows.append({
            "name": slug,
            "category": cat,
            "title": title,
            "html_file": "pages/reviews/%s/%s" % (cat, fn),
            "logo": logo,
            "logo_exists": bool(logo),
            "screenshot_exists": bool(shot),
            "screenshot_path": shot,
            "noindex": bool(NOINDEX_RE.search(html)),
            "canonical": (CANON_RE.search(html).group(1) if CANON_RE.search(html) else ""),
            "bytes": os.path.getsize(path),
        })

fields = ["name", "category", "title", "html_file", "logo", "logo_exists",
          "screenshot_exists", "screenshot_path", "noindex", "canonical", "bytes"]

with open(os.path.join(DOCS, "tools_list.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(rows)

with open(os.path.join(DOCS, "tools_list.json"), "w", encoding="utf-8") as f:
    json.dump(rows, f, indent=2, ensure_ascii=False)

cats = {}
for r in rows:
    cats[r["category"]] = cats.get(r["category"], 0) + 1

print("fiches indexees      : %d" % len(rows))
print("avec logo            : %d" % sum(1 for r in rows if r["logo_exists"]))
print("sans logo            : %d" % sum(1 for r in rows if not r["logo_exists"]))
print("en noindex           : %d" % sum(1 for r in rows if r["noindex"]))
print("categories           : %d" % len(cats))
for c in sorted(cats):
    print("   %-18s %3d" % (c, cats[c]))
