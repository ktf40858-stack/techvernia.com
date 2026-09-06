#!/usr/bin/env python3
"""
Telecharge le logo officiel des 50 nouveaux outils dans
docs/assets/images/logos/{slug}.png (convention respectee par 472/472 fiches).

Chaine de repli : Clearbit -> Google favicon 256 -> DuckDuckGo icons.
N'ecrase jamais un logo existant. Ne touche a aucune page du site.
"""
import os
import sys
import time
import urllib.request
import urllib.error

ROOT = os.path.dirname(os.path.abspath(__file__))
LOGOS = os.path.join(ROOT, "docs", "assets", "images", "logos")

# slug -> domaine officiel
TOOLS = {
    # navigateurs AI
    "perplexity-comet":   "perplexity.ai",
    "chatgpt-atlas":      "openai.com",
    "opera-neon":         "opera.com",
    "dia-browser":        "diabrowser.com",
    "brave-leo":          "brave.com",
    # computer-use / scraping
    "browser-use":        "browser-use.com",
    "skyvern":            "skyvern.com",
    "browserbase":        "browserbase.com",
    "firecrawl":          "firecrawl.dev",
    # agents de code
    "opencode":           "opencode.ai",
    "openai-codex":       "openai.com",
    "google-antigravity": "antigravity.google",
    "gemini-cli":         "google.com",
    "warp":               "warp.dev",
    # LLM local
    "lm-studio":          "lmstudio.ai",
    "jan":                "jan.ai",
    "open-webui":         "openwebui.com",
    "anythingllm":        "anythingllm.com",
    "vllm":               "vllm.ai",
    # vector DB
    "pinecone":           "pinecone.io",
    "qdrant":             "qdrant.tech",
    "weaviate":           "weaviate.io",
    # LLMOps
    "langfuse":           "langfuse.com",
    "langsmith":          "langchain.com",
    "braintrust":         "braintrust.dev",
    # memoire d'agents
    "mem0":               "mem0.ai",
    "letta":              "letta.com",
    # SOC agentique
    "xbow":               "xbow.com",
    "dropzone-ai":        "dropzone.ai",
    "prophet-security":   "prophetsecurity.ai",
    "radiant-security":   "radiantsecurity.ai",
    "exaforce":           "exaforce.com",
    # agents vocaux
    "vapi":               "vapi.ai",
    "retell-ai":          "retellai.com",
    "bland-ai":           "bland.ai",
    "cartesia":           "cartesia.ai",
    # GEO
    "profound":           "tryprofound.com",
    "goodie-ai":          "higoodie.com",
    "llmrefs":            "llmrefs.com",
    # agents entreprise
    "dust":               "dust.tt",
    "agentforce":         "salesforce.com",
    "moveworks":          "moveworks.com",
    # verticales
    "rogo":               "rogo.ai",
    "hebbia":             "hebbia.ai",
    "nabla":              "nabla.com",
    # image / world models
    "nano-banana":        "deepmind.google",
    "seedream-5":         "bytedance.com",
    "odyssey":            "odyssey.ml",
    # productivite
    "granola":            "granola.ai",
    "limitless":          "limitless.ai",
}

SOURCES = [
    ("clearbit",   "https://logo.clearbit.com/{d}?size=256"),
    ("google",     "https://www.google.com/s2/favicons?domain={d}&sz=256"),
    ("duckduckgo", "https://icons.duckduckgo.com/ip3/{d}.ico"),
]

HDRS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) TechVerniaLogoBot/1.0"}
MIN_BYTES = 500  # en dessous : favicon generique / placeholder


def fetch(url):
    req = urllib.request.Request(url, headers=HDRS)
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.read()


def main():
    os.makedirs(LOGOS, exist_ok=True)
    ok, skipped, failed = [], [], []
    only = sys.argv[1:] or None

    for slug, domain in sorted(TOOLS.items()):
        if only and slug not in only:
            continue
        dest = os.path.join(LOGOS, slug + ".png")
        if os.path.exists(dest) and os.path.getsize(dest) > MIN_BYTES:
            skipped.append(slug)
            print("=  %-20s deja present (%d o)" % (slug, os.path.getsize(dest)))
            continue

        got = None
        for name, tpl in SOURCES:
            try:
                data = fetch(tpl.format(d=domain))
                if data and len(data) > MIN_BYTES:
                    got = (name, data)
                    break
            except Exception:
                pass
            time.sleep(0.3)

        if got:
            open(dest, "wb").write(got[1])
            ok.append(slug)
            print("OK %-20s %-22s %-10s %d o" % (slug, domain, got[0], len(got[1])))
        else:
            failed.append((slug, domain))
            print("KO %-20s %-22s aucune source" % (slug, domain))

    print("\n--- resume ---")
    print("telecharges : %d" % len(ok))
    print("deja la     : %d" % len(skipped))
    print("echecs      : %d" % len(failed))
    for slug, dom in failed:
        print("   a corriger : %s (%s)" % (slug, dom))


if __name__ == "__main__":
    main()
