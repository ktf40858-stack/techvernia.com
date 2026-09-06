#!/usr/bin/env python3
"""
Genere les fiches de review des 50 nouveaux outils AI.

Contraintes respectees (crawl du sitemap en cours) :
  - les pages sortent en <meta name="robots" content="noindex, nofollow">
  - aucune ecriture dans sitemap.xml / sitemap-en.xml
  - aucune modification des pages ni de la navigation existantes
  - rien n'est ajoute aux pages de categorie

Apres validation, `python generate_reviews.py --publish` retire le noindex,
et un second script (a lancer une fois le crawl termine) fera l'ajout au
sitemap et aux categories.

Le contenu de chaque fiche est ecrit a la main dans tools_data_*.py :
aucun paragraphe n'est partage entre deux outils, pour ne pas rejouer le
rejet AdSense pour contenu duplique.
"""
import argparse
import html
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(ROOT, "docs")
GAB = os.path.join(ROOT, "_gabarit")
REVIEWS = os.path.join(DOCS, "pages", "reviews")
LOGOS_FS = os.path.join(DOCS, "assets", "images", "logos")

SITE = "https://techvernia.com"
UP = "../../../"          # profondeur constante : pages/reviews/<cat>/<slug>.html

# --- bibliotheque d'icones SVG (reprise du style neon-icon du site) ---------
ICONS = {
    "shield":   '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>',
    "cube":     '<path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path>',
    "check":    '<path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>',
    "monitor":  '<rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line>',
    "link":     '<path d="M15 7h3a5 5 0 0 1 5 5 5 5 0 0 1-5 5h-3m-6 0H6a5 5 0 0 1-5-5 5 5 0 0 1 5-5h3"></path><line x1="8" y1="12" x2="16" y2="12"></line>',
    "activity": '<polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline>',
    "globe":    '<circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>',
    "terminal": '<polyline points="4 17 10 11 4 5"></polyline><line x1="12" y1="19" x2="20" y2="19"></line>',
    "cpu":      '<rect x="4" y="4" width="16" height="16" rx="2"></rect><rect x="9" y="9" width="6" height="6"></rect><line x1="9" y1="1" x2="9" y2="4"></line><line x1="15" y1="1" x2="15" y2="4"></line><line x1="9" y1="20" x2="9" y2="23"></line><line x1="15" y1="20" x2="15" y2="23"></line>',
    "database": '<ellipse cx="12" cy="5" rx="9" ry="3"></ellipse><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"></path><path d="M3 12c0 1.66 4 3 9 3s9-1.34 9-3"></path>',
    "search":   '<circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line>',
    "mic":      '<path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="23"></line>',
    "zap":      '<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon>',
    "eye":      '<path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle>',
    "layers":   '<polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline>',
    "lock":     '<rect x="3" y="11" width="18" height="11" rx="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path>',
    "users":    '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>',
    "clock":    '<circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline>',
    "image":    '<rect x="3" y="3" width="18" height="18" rx="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline>',
    "book":     '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>',
    "git":      '<circle cx="18" cy="18" r="3"></circle><circle cx="6" cy="6" r="3"></circle><path d="M6 21V9a9 9 0 0 0 9 9"></path>',
    "brain":    '<path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96.44A2.5 2.5 0 0 1 4 17.5v-1A2.5 2.5 0 0 1 2 14a2.5 2.5 0 0 1 1.5-2.29A2.5 2.5 0 0 1 3 9.5 2.5 2.5 0 0 1 5.5 7 2.5 2.5 0 0 1 9.5 2z"></path><path d="M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96.44A2.5 2.5 0 0 0 20 17.5v-1A2.5 2.5 0 0 0 22 14a2.5 2.5 0 0 0-1.5-2.29A2.5 2.5 0 0 0 21 9.5 2.5 2.5 0 0 0 18.5 7 2.5 2.5 0 0 0 14.5 2z"></path>',
}
SVG = ('<svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" '
       'viewBox="0 0 24 24">%s</svg>')


def icon(key):
    return SVG % ICONS.get(key, ICONS["check"])


def e(t):
    """Echappe pour du texte HTML, en laissant passer les entites deja ecrites."""
    return html.escape(t, quote=False).replace("&amp;#", "&#").replace("&amp;mdash;", "&mdash;")


def stars(rating):
    full = int(rating)
    half = (rating - full) >= 0.5
    s = "&#9733;" * full
    if half and full < 5:
        s += "&#9733;"
        full += 1
    s += "&#9734;" * (5 - full)
    return s



# --- resolution des liens "related" ---------------------------------------
_SLUG_INDEX = None


def resolve_related(target_slug, from_category):
    """Retourne le href relatif correct pour une fiche liee.

    Le site lie les fiches d'une meme categorie en relatif simple
    (`slug.html`). Pour une fiche d'une autre categorie il faut remonter
    d'un cran (`../categorie/slug.html`). On resout automatiquement en
    indexant les fiches reellement presentes sur le disque.
    """
    global _SLUG_INDEX
    if _SLUG_INDEX is None:
        _SLUG_INDEX = {}
        for cat in os.listdir(REVIEWS):
            cdir = os.path.join(REVIEWS, cat)
            if not os.path.isdir(cdir):
                continue
            for fn in os.listdir(cdir):
                if fn.endswith(".html"):
                    _SLUG_INDEX.setdefault(fn[:-5], cat)
    cat = _SLUG_INDEX.get(target_slug)
    if cat is None or cat == from_category:
        return target_slug + ".html"          # meme dossier, ou pas encore genere
    return "../%s/%s.html" % (cat, target_slug)


# --- fragments -------------------------------------------------------------
def build_head(t, noindex=True):
    style = io.open(os.path.join(GAB, "style.html"), encoding="utf-8").read()
    robots = ('<meta content="noindex, nofollow" name="robots"/>\n'
              '<!-- NOINDEX : fiche en attente de validation editoriale. '
              'Retire par generate_reviews.py --publish -->\n') if noindex else ""
    schema = build_schema(t)
    return """<!DOCTYPE html>

<html data-theme="dark" lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
{robots}<meta content="{desc}" name="description"/>
<meta content="{kw}" name="keywords"/>
<meta content="TechVernia" name="author"/>
<meta content="{title}" property="og:title"/>
<meta content="{desc}" property="og:description"/>
<meta content="article" property="og:type"/>
<meta content="{site}/pages/reviews/{cat}/{slug}.html" property="og:url"/>
<meta content="{site}/assets/images/logos/{slug}.png" property="og:image"/>
<meta content="summary_large_image" name="twitter:card"/>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8248464433423786"
     crossorigin="anonymous"></script>
<!-- Google Analytics 4 - TechVernia -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-S2YLSEB9VR"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'G-S2YLSEB9VR');
</script>
<!-- End Google Analytics -->

<title>{title}</title>
<link href="{up}css/style.css" rel="stylesheet"/>
<link href="{up}css/responsive.css" rel="stylesheet"/>
<link href="{up}css/guides-reviews.css" rel="stylesheet"/>
<link href="{up}css/animations.css" rel="stylesheet"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&amp;family=Inter:wght@300;400;500;600;700;800&amp;family=JetBrains+Mono:wght@400;500;600&amp;display=swap" rel="stylesheet"/><link href="{up}css/neon-icons.css" rel="stylesheet"/>
{style}
{schema}
</head>
""".format(robots=robots, desc=e(t["meta_desc"]), kw=e(t["meta_keywords"]),
           title=e(t["title"]), site=SITE, cat=t["category"], slug=t["slug"],
           up=UP, style=style, schema=schema)


def build_schema(t):
    review = {
        "@context": "https://schema.org",
        "@type": "Review",
        "itemReviewed": {
            "@type": "SoftwareApplication",
            "name": t["name"],
            "applicationCategory": t["app_category"],
            "operatingSystem": t.get("os", "Web"),
            "url": t["url"],
        },
        "author": {"@type": "Organization", "name": "TechVernia"},
        "publisher": {"@type": "Organization", "name": "TechVernia"},
        "reviewRating": {
            "@type": "Rating",
            "ratingValue": t["rating"],
            "bestRating": 5,
            "worstRating": 1,
        },
        "datePublished": t.get("date", "2026-09-06"),
        "reviewBody": t["overview"][0],
    }
    faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in t["faq"]
        ],
    }
    return ('<script type="application/ld+json">%s</script>\n'
            '<script type="application/ld+json">%s</script>'
            % (json.dumps(review, ensure_ascii=False, indent=1),
               json.dumps(faq, ensure_ascii=False, indent=1)))


def build_body(t):
    o = []
    a = o.append
    # fil d'ariane
    a('<div class="container" style="padding-top: calc(80px + var(--space-lg));">')
    a('<nav style="font-size: var(--text-sm); color: var(--text-tertiary);">')
    a('<a href="%sindex.html" style="color: var(--text-tertiary); text-decoration: none;">Home</a>' % UP)
    a('<span style="margin: 0 var(--space-sm);">/</span>')
    a('<a href="%s" style="color: var(--text-tertiary); text-decoration: none;">%s</a>'
      % (t["cat_href"], e(t["cat_label"])))
    a('<span style="margin: 0 var(--space-sm);">/</span>')
    a('<span style="color: var(--text-primary);">%s Review</span>' % e(t["name"]))
    a('</nav>\n</div>')

    # hero
    a('<header class="review-hero">\n<div class="container">\n<div class="review-hero-content">')
    a('<div class="tool-logo-xl">')
    a('<img alt="%s Logo" src="%sassets/images/logos/%s.png" onerror="this.style.display=\'none\'"/>'
      % (e(t["name"]), UP, t["slug"]))
    a('</div>\n<div class="review-hero-info">')
    a('<h1>%s Review 2026</h1>' % e(t["name"]))
    a('<p class="company">by %s &mdash; %s &nbsp; %s %s</p>'
      % (e(t["company"]), e(t["domain"]), t["flag"], e(t["country"])))
    a('<div class="review-badges">')
    for i, b in enumerate(t["badges"]):
        cls = ["badge badge-popular", "badge badge-new",
               'badge" style="background: rgba(124, 58, 237, 0.1); color: #7C3AED;'][min(i, 2)]
        a('<span class="%s">%s</span>' % (cls, e(b)))
    a('</div>\n</div>')
    a('<div class="rating-box">')
    a('<div class="rating-score">%s</div>' % t["rating"])
    a('<div class="rating-stars">%s</div>' % stars(t["rating"]))
    a('<div class="rating-label">Expert Rating</div>')
    a('</div>\n</div>\n</div>\n</header>')

    # bandeau de stats
    a('<div class="quick-stats">\n<div class="container">\n<div class="quick-stats-grid">')
    for v, l in t["quick_stats"]:
        a('<div class="quick-stat"><div class="quick-stat-value">%s</div>'
          '<div class="quick-stat-label">%s</div></div>' % (e(v), e(l)))
    a('</div>\n</div>\n</div>')

    # contenu
    a('<main class="container">\n<div class="review-content">\n<article class="review-main">')
    a('<div class="test-section-top">')
    a('<h2>Try %s</h2>' % e(t["name"]))
    a('<div class="cta-buttons-top">')
    a('<a class="btn btn-primary" href="%s" rel="nofollow sponsored" target="_blank">Visit %s &rarr;</a>'
      % (t["url"], e(t["name"])))
    a('<a class="btn btn-outline" href="%s" rel="nofollow sponsored" target="_blank">%s</a>'
      % (t["cta2_url"], e(t["cta2_label"])))
    a('</div>\n</div>\n')

    a('<h2 id="overview">Overview</h2>')
    for p in t["overview"]:
        a('<p>%s</p>' % e(p))

    a('\n<h2 id="features">Key Features</h2>\n<div class="features-grid">')
    for ic, ftitle, fdesc in t["features"]:
        a('<div class="feature-card">')
        a('<div class="feature-card-icon">\n%s\n</div>' % icon(ic))
        a('<h4>%s</h4>' % e(ftitle))
        a('<p>%s</p>' % e(fdesc))
        a('</div>')
    a('</div>')

    a('\n<h2 id="pros-cons">Pros &amp; Cons</h2>\n<div class="pros-cons-grid">')
    a('<div class="pros-box">')
    a('<h4>%s Advantages</h4>\n<ul>'
      % (SVG % '<polyline points="20 6 9 17 4 12"></polyline>'))
    for p in t["pros"]:
        a('<li>%s</li>' % e(p))
    a('</ul>\n</div>')
    a('<div class="cons-box">')
    a('<h4>%s Disadvantages</h4>\n<ul>'
      % (SVG % '<line x1="18" x2="6" y1="6" y2="18"></line><line x1="6" x2="18" y1="6" y2="18"></line>'))
    for c in t["cons"]:
        a('<li>%s</li>' % e(c))
    a('</ul>\n</div>\n</div>')

    a('\n<h2 id="pricing">Pricing Plans</h2>\n<table class="pricing-table">')
    a('<thead><tr><th>Plan</th><th>Price</th><th>Key Features</th></tr></thead>\n<tbody>')
    for plan, price, feats in t["pricing"]:
        a('<tr><td class="plan-name">%s</td><td class="price">%s</td><td>%s</td></tr>'
          % (e(plan), e(price), e(feats)))
    a('</tbody>\n</table>')

    a('\n<h2 id="use-cases">Best Use Cases</h2>')
    a('<h3>%s Excels At:</h3>\n<ul>' % e(t["name"]))
    for u in t["excels"]:
        a('<li>%s</li>' % e(u))
    a('</ul>')
    a('<h3>May Not Be Ideal For:</h3>\n<ul>')
    for u in t["not_ideal"]:
        a('<li>%s</li>' % e(u))
    a('</ul>')

    a('\n<h2 id="comparison">How It Compares</h2>')
    for h, p in t["comparisons"]:
        a('<h3>%s</h3>' % e(h))
        a('<p>%s</p>' % e(p))

    a('\n<h2 id="verdict">Final Verdict</h2>\n<div class="verdict-box">')
    a('<h3>Our Recommendation</h3>')
    a('<p>%s</p>' % e(t["verdict"]))
    a('</div>')

    a('\n<h2 id="faq">Frequently Asked Questions</h2>')
    for q, ans in t["faq"]:
        a('<div class="faq-item">')
        a('<div class="faq-question"><span>%s</span><span>+</span></div>' % e(q))
        a('<div class="faq-answer">%s</div>' % e(ans))
        a('</div>')
    a('</article>\n')

    # colonne de droite
    a('<aside class="review-sidebar">')
    a('<div class="sidebar-card">')
    a('<h3>Get %s</h3>\n<div class="cta-buttons">' % e(t["name"]))
    a('<a class="btn btn-primary" href="%s" rel="nofollow sponsored" target="_blank">Visit %s &rarr;</a>'
      % (t["url"], e(t["name"])))
    a('<a class="btn btn-outline" href="%s" rel="nofollow sponsored" target="_blank">%s</a>'
      % (t["cta2_url"], e(t["cta2_label"])))
    a('</div>\n<div class="rating-breakdown">')
    for label, score in t["breakdown"]:
        a('<div class="rating-item"><span class="rating-item-label">%s</span>'
          '<div class="rating-item-bar"><div class="rating-item-fill" style="width: %d%%"></div></div>'
          '<span class="rating-item-score">%s</span></div>'
          % (e(label), int(round(score * 10)), score))
    a('</div>\n</div>')

    a('<div class="sidebar-card">\n<h3>Table of Contents</h3>\n<ul class="toc-list">')
    for href, lab in [("#overview", "Overview"), ("#features", "Key Features"),
                      ("#pros-cons", "Pros &amp; Cons"), ("#pricing", "Pricing"),
                      ("#use-cases", "Use Cases"), ("#comparison", "Comparison"),
                      ("#verdict", "Verdict"), ("#faq", "FAQ")]:
        a('<li><a href="%s">%s</a></li>' % (href, lab))
    a('</ul>\n</div>')

    a('<div class="sidebar-card">\n<h3>Compare With</h3>')
    for rslug, rname, rrating, rtag in t["related"]:
        a('<div class="related-tool">')
        a('<div class="related-tool-logo" style="background: linear-gradient(135deg, #7C3AED, #C084FC);">')
        a('<img alt="%s Logo" src="%sassets/images/logos/%s.png" '
          'style="width: 100%%; height: 100%%; object-fit: contain;" '
          'onerror="this.style.display=\'none\'"/>' % (e(rname), UP, rslug))
        a('</div>\n<div class="related-tool-info">')
        a('<div class="related-tool-name"><a href="%s">%s</a></div>'
          % (resolve_related(rslug, t["category"]), e(rname)))
        a('<div class="related-tool-rating">&#9733; %s - %s</div>' % (rrating, e(rtag)))
        a('</div>\n</div>')
    a('</div>')

    a('<div class="sidebar-card">\n<h3>Quick Info</h3>')
    a('<ul style="list-style: none; padding: 0; font-size: var(--text-sm);">')
    rows = [("Company", t["company"]), ("Founded", t["founded"]),
            ("Headquarters", t["hq"]), ("Country", "%s %s" % (t["flag"], t["country"]))]
    for k, v in rows:
        a('<li style="display: flex; justify-content: space-between; padding: var(--space-sm) 0; '
          'border-bottom: 1px solid var(--border-color);">'
          '<span style="color: var(--text-tertiary);">%s</span>'
          '<span style="font-weight: 500;">%s</span></li>' % (k, e(v)))
    a('<li style="display: flex; justify-content: space-between; padding: var(--space-sm) 0;">'
      '<span style="color: var(--text-tertiary);">Website</span>'
      '<span style="font-weight: 500; color: #7C3AED;">%s</span></li>' % e(t["domain"]))
    a('</ul>\n</div>\n</aside>\n</div>\n</main>')
    return "\n".join(o)


def build_page(t, noindex=True):
    nav = io.open(os.path.join(GAB, "nav.html"), encoding="utf-8").read()
    footer = io.open(os.path.join(GAB, "footer.html"), encoding="utf-8").read()
    # le footer du gabarit pointe vers 3 categories figees : on met celle de la fiche en tete
    footer = footer.replace(
        '<li><a href="../../categories/ai-cybersecurity.html">AI Cybersecurity</a></li>',
        '<li><a href="%s">%s</a></li>' % (t["cat_href"], e(t["cat_label"])))
    return build_head(t, noindex) + nav + "\n" + build_body(t) + "\n" + footer


# --- chargement des donnees ------------------------------------------------
def load_tools():
    tools = []
    for i in range(1, 21):
        mod = "tools_data_%02d" % i
        path = os.path.join(ROOT, mod + ".py")
        if not os.path.exists(path):
            continue
        ns = {}
        exec(compile(io.open(path, encoding="utf-8").read(), path, "exec"), ns)
        tools.extend(ns["TOOLS"])
    return tools


REQUIRED = ["slug", "category", "cat_href", "cat_label", "name", "company", "domain",
            "url", "cta2_url", "cta2_label", "flag", "country", "founded", "hq",
            "rating", "badges", "quick_stats", "title", "meta_desc", "meta_keywords",
            "app_category", "overview", "features", "pros", "cons", "pricing",
            "excels", "not_ideal", "comparisons", "verdict", "faq", "breakdown",
            "related"]


def validate(t):
    errs = []
    for k in REQUIRED:
        if k not in t:
            errs.append("champ manquant : %s" % k)
    if errs:
        return errs
    if len(t["overview"]) < 3:
        errs.append("overview : %d paragraphes (3 minimum)" % len(t["overview"]))
    if len(t["features"]) != 6:
        errs.append("features : %d (6 attendus)" % len(t["features"]))
    if len(t["faq"]) < 4:
        errs.append("faq : %d (4 minimum)" % len(t["faq"]))
    if len(t["quick_stats"]) != 5:
        errs.append("quick_stats : %d (5 attendus)" % len(t["quick_stats"]))
    if len(t["breakdown"]) != 5:
        errs.append("breakdown : %d (5 attendus)" % len(t["breakdown"]))
    if len(t["related"]) != 3:
        errs.append("related : %d (3 attendus)" % len(t["related"]))
    if not os.path.exists(os.path.join(LOGOS_FS, t["slug"] + ".png")):
        errs.append("logo absent : assets/images/logos/%s.png" % t["slug"])
    words = sum(len(p.split()) for p in t["overview"])
    if words < 150:
        errs.append("overview trop court : %d mots" % words)
    return errs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--publish", action="store_true",
                    help="genere sans noindex (a n'utiliser qu'apres validation)")
    ap.add_argument("--only", help="ne generer que ce slug")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    tools = load_tools()
    if args.only:
        tools = [t for t in tools if t["slug"] == args.only]
    if not tools:
        print("aucun outil a generer (tools_data_*.py absents ?)")
        return 1

    written, failed, total_words = 0, [], 0
    for t in tools:
        errs = validate(t)
        if errs:
            failed.append((t.get("slug", "?"), errs))
            continue
        page = build_page(t, noindex=not args.publish)
        outdir = os.path.join(REVIEWS, t["category"])
        out = os.path.join(outdir, t["slug"] + ".html")
        words = len(page.split())
        total_words += words
        if not args.dry_run:
            os.makedirs(outdir, exist_ok=True)
            io.open(out, "w", encoding="utf-8", newline="\n").write(page)
        written += 1
        print("%-22s %-14s %6d o" % (t["slug"], t["category"], len(page)))

    print("\n--- resume ---")
    print("pages generees : %d" % written)
    print("noindex        : %s" % ("non (PUBLIE)" if args.publish else "oui"))
    if failed:
        print("en erreur      : %d" % len(failed))
        for slug, errs in failed:
            print("   %s" % slug)
            for x in errs:
                print("      - %s" % x)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
