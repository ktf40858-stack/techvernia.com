#!/usr/bin/env python3
"""
Seconde passe logos : pour les slugs dont le PNG est basse definition
(< 128 px) ou dans un format non-PNG, va chercher l'apple-touch-icon
ou l'og:image officiel du site de l'editeur, qui sont haute resolution.

Ne remplace le fichier que si la nouvelle image est strictement meilleure.
"""
import os
import re
import struct
import sys
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
LOGOS = os.path.join(ROOT, "docs", "assets", "images", "logos")
HDRS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/122.0 Safari/537.36"}

TARGETS = {
    "opera-neon":   "https://www.opera.com/",
    "skyvern":      "https://www.skyvern.com/",
    "firecrawl":    "https://www.firecrawl.dev/",
    "opencode":     "https://opencode.ai/",
    "jan":          "https://jan.ai/",
    "pinecone":     "https://www.pinecone.io/",
    "weaviate":     "https://weaviate.io/",
    "mem0":         "https://mem0.ai/",
    "profound":     "https://www.tryprofound.com/",
    "goodie-ai":    "https://www.higoodie.com/",
    "llmrefs":      "https://llmrefs.com/",
    "agentforce":   "https://www.salesforce.com/agentforce/",
    "limitless":    "https://www.limitless.ai/",
}

ICON_RE = re.compile(
    r'<link[^>]+rel=["\'][^"\']*(?:apple-touch-icon|icon)[^"\']*["\'][^>]*>', re.I)
HREF_RE = re.compile(r'href=["\']([^"\']+)["\']', re.I)
SIZES_RE = re.compile(r'sizes=["\'](\d+)x\d+["\']', re.I)
OG_RE = re.compile(
    r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', re.I)


def get(url, timeout=20):
    req = urllib.request.Request(url, headers=HDRS)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def png_dims(data):
    """(largeur, hauteur) d'un PNG ou d'un ICO. None si format non reconnu."""
    if data[:8] == b"\x89PNG\r\n\x1a\n" and data[12:16] == b"IHDR":
        w, h = struct.unpack(">II", data[16:24])
        return (w, h)
    if data[:4] == b"\x00\x00\x01\x00":
        return (data[6] or 256, data[7] or 256)
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return (256, 256)
    if data[:5] == b"<?xml" or data[:4] == b"<svg":
        return (1024, 1024)   # vectoriel : toujours mieux
    return None


def png_width(data):
    d = png_dims(data)
    return d[0] if d else None


def is_square(data, tol=0.25):
    """Un logo doit etre grosso modo carre : ecarte les bannieres og:image."""
    d = png_dims(data)
    if not d or d[1] == 0:
        return False
    ratio = d[0] / float(d[1])
    return (1 - tol) <= ratio <= (1 + tol)


def candidates(page_url):
    """Retourne les URLs d'icones du plus grand au plus petit."""
    try:
        html = get(page_url).decode("utf-8", "replace")
    except Exception as e:
        print("   page inaccessible : %s" % e)
        return []
    found = []
    for tag in ICON_RE.findall(html):
        m = HREF_RE.search(tag)
        if not m:
            continue
        size = SIZES_RE.search(tag)
        px = int(size.group(1)) if size else (180 if "apple-touch" in tag.lower() else 64)
        px += 10000   # les <link rel=icon> passent avant tout og:image
        found.append((px, urllib.parse.urljoin(page_url, m.group(1))))
    for m in OG_RE.findall(html):
        found.append((512, urllib.parse.urljoin(page_url, m)))   # og:image : dernier recours
    found.sort(key=lambda x: -x[0])
    return [u for _, u in found]


def current_width(path):
    if not os.path.exists(path):
        return 0
    w = png_width(open(path, "rb").read(64))
    return w or 0


def main():
    only = sys.argv[1:] or None
    upgraded, kept = [], []
    for slug, url in sorted(TARGETS.items()):
        if only and slug not in only:
            continue
        dest = os.path.join(LOGOS, slug + ".png")
        before = current_width(dest)
        print("%-14s (actuel %spx)" % (slug, before or "?"))
        best = None
        for cand in candidates(url)[:6]:
            try:
                data = get(cand)
            except Exception:
                continue
            w = png_width(data[:64])
            if not is_square(data[:64]):
                print("   x %s ignore (non carre)" % cand[:70])
                continue
            if w and w > max(before, 128) and (best is None or w > best[0]):
                best = (w, data, cand)
        if best:
            open(dest, "wb").write(best[1])
            upgraded.append((slug, before, best[0]))
            print("   -> %dpx depuis %s" % (best[0], best[2][:80]))
        else:
            kept.append(slug)
            print("   -> rien de mieux trouve, logo conserve")

    print("\n--- resume ---")
    print("ameliores : %d" % len(upgraded))
    for s, b, a in upgraded:
        print("   %-14s %spx -> %dpx" % (s, b or "?", a))
    print("inchanges : %d  %s" % (len(kept), ", ".join(kept)))


if __name__ == "__main__":
    main()
