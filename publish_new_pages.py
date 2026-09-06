#!/usr/bin/env python3
"""
Publication des 50 nouvelles fiches. A LANCER SEULEMENT :
  1. apres ta relecture et ta validation editoriale
  2. apres la fin du crawl du sitemap en cours

Ce que fait le script :
  - regenere les 50 pages SANS le meta robots noindex
  - ajoute les 50 URLs a docs/sitemap-en.xml (sauvegarde prealable)
  - regenere docs/tools_list.csv / .json
  - signale les 5 nouvelles categories a rattacher a la navigation

Rien n'est ecrit sans --confirm. Par defaut le script fait une simulation.
"""
import argparse
import datetime
import io
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(ROOT, "docs")
SITEMAP = os.path.join(DOCS, "sitemap-en.xml")
SITE = "https://techvernia.com"
TODAY = datetime.date.today().isoformat()

NEW_CATEGORIES = {
    "browsers":  ("AI Browsers", "ai-browsers.html"),
    "local-llm": ("Local LLM Tools", "ai-local-llm.html"),
    "llmops":    ("LLMOps & Evaluation", "ai-llmops.html"),
    "voice":     ("AI Voice Agents", "ai-voice.html"),
    "data":      ("AI Data Infrastructure", "ai-data.html"),   # dossier existant, page categorie absente
}


def load_tools():
    tools = []
    for i in range(1, 21):
        p = os.path.join(ROOT, "tools_data_%02d.py" % i)
        if not os.path.exists(p):
            continue
        ns = {}
        exec(compile(io.open(p, encoding="utf-8").read(), p, "exec"), ns)
        tools.extend(ns["TOOLS"])
    return tools


def add_to_sitemap(tools, confirm):
    xml = io.open(SITEMAP, encoding="utf-8").read()
    entries, skipped = [], []
    for t in tools:
        loc = "%s/pages/reviews/%s/%s.html" % (SITE, t["category"], t["slug"])
        if loc in xml:
            skipped.append(t["slug"])
            continue
        entries.append(
            "<url>\n<loc>%s</loc>\n<lastmod>%s</lastmod>\n"
            "<changefreq>monthly</changefreq>\n<priority>0.7</priority>\n</url>"
            % (loc, TODAY))
    if not entries:
        print("sitemap : rien a ajouter (%d deja presentes)" % len(skipped))
        return 0
    if not confirm:
        print("sitemap : %d URLs seraient ajoutees (simulation)" % len(entries))
        return len(entries)
    shutil.copy2(SITEMAP, SITEMAP + ".bak-" + TODAY)
    new = xml.replace("</urlset>", "\n".join(entries) + "\n</urlset>")
    io.open(SITEMAP, "w", encoding="utf-8", newline="\n").write(new)
    print("sitemap : %d URLs ajoutees (sauvegarde %s.bak-%s)"
          % (len(entries), os.path.basename(SITEMAP), TODAY))
    return len(entries)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--confirm", action="store_true",
                    help="ecrit reellement les changements (sinon simulation)")
    args = ap.parse_args()

    tools = load_tools()
    print("=" * 70)
    print("PUBLICATION DES %d NOUVELLES FICHES  %s" % (len(tools), "" if args.confirm else "(SIMULATION)"))
    print("=" * 70)

    print("\n[1/4] regeneration sans noindex")
    cmd = [sys.executable, "generate_reviews.py"] + (["--publish"] if args.confirm else ["--dry-run"])
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    print("      " + (r.stdout.strip().splitlines() or ["(rien)"])[-1])
    if r.returncode != 0:
        print("      ECHEC : ", r.stdout[-500:], r.stderr[-500:])
        return 1

    print("\n[2/4] sitemap")
    add_to_sitemap(tools, args.confirm)

    print("\n[3/4] inventaire tools_list")
    if args.confirm:
        subprocess.run([sys.executable, "rebuild_tools_list.py"], cwd=ROOT)
    else:
        print("      serait regenere")

    print("\n[4/4] categories a rattacher a la navigation (travail manuel)")
    counts = {}
    for t in tools:
        counts[t["category"]] = counts.get(t["category"], 0) + 1
    for cat, (label, page) in NEW_CATEGORIES.items():
        exists = os.path.exists(os.path.join(DOCS, "pages", "categories", page))
        n = counts.get(cat, 0)
        print("      %-10s %2d fiches  page categorie %s : %s"
              % (cat, n, page, "existe" if exists else "A CREER"))
    print("""
      Ces 5 categories n'ont pas encore de page d'index ni d'entree dans la
      navigation. Tant que ce n'est pas fait, les fiches sont accessibles par
      URL directe et par le sitemap, mais orphelines dans le maillage interne
      — ce qui limite fortement leur potentiel de classement.
""")

    if not args.confirm:
        print("Simulation terminee. Relancer avec --confirm pour appliquer.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
