#!/usr/bin/env python3
"""
Verifie que les 50 outils existent toujours avant d'ecrire leur fiche.

Motivation : la fiche Sora du site vend encore un produit arrete. On ne
recommence pas. Pour chaque outil : code HTTP, titre de la page d'accueil,
et detection de signaux d'arret (sunset, discontinued, shutting down...).
"""
import re
import ssl
import urllib.error
import urllib.request

HDRS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/122.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"}

SUNSET = re.compile(
    r"(sunset|discontinu|shutting down|shut down|no longer available|"
    r"end of life|deprecat|has been retired|winding down|acquired by)", re.I)
TITLE = re.compile(r"<title[^>]*>(.*?)</title>", re.S | re.I)

URLS = [
    ("perplexity-comet",   "https://www.perplexity.ai/comet"),
    ("chatgpt-atlas",      "https://openai.com/index/introducing-chatgpt-atlas/"),
    ("opera-neon",         "https://www.opera.com/neon"),
    ("dia-browser",        "https://www.diabrowser.com/"),
    ("brave-leo",          "https://brave.com/leo/"),
    ("browser-use",        "https://browser-use.com/"),
    ("skyvern",            "https://www.skyvern.com/"),
    ("browserbase",        "https://www.browserbase.com/"),
    ("firecrawl",          "https://www.firecrawl.dev/"),
    ("opencode",           "https://opencode.ai/"),
    ("openai-codex",       "https://openai.com/codex/"),
    ("google-antigravity", "https://antigravity.google/"),
    ("gemini-cli",         "https://github.com/google-gemini/gemini-cli"),
    ("warp",               "https://www.warp.dev/"),
    ("lm-studio",          "https://lmstudio.ai/"),
    ("jan",                "https://jan.ai/"),
    ("open-webui",         "https://openwebui.com/"),
    ("anythingllm",        "https://anythingllm.com/"),
    ("vllm",               "https://docs.vllm.ai/en/latest/"),
    ("pinecone",           "https://www.pinecone.io/"),
    ("qdrant",             "https://qdrant.tech/"),
    ("weaviate",           "https://weaviate.io/"),
    ("langfuse",           "https://langfuse.com/"),
    ("langsmith",          "https://www.langchain.com/langsmith"),
    ("braintrust",         "https://www.braintrust.dev/"),
    ("mem0",               "https://mem0.ai/"),
    ("letta",              "https://www.letta.com/"),
    ("xbow",               "https://xbow.com/"),
    ("dropzone-ai",        "https://www.dropzone.ai/"),
    ("prophet-security",   "https://www.prophetsecurity.ai/"),
    ("radiant-security",   "https://radiantsecurity.ai/"),
    ("exaforce",           "https://www.exaforce.com/"),
    ("vapi",               "https://vapi.ai/"),
    ("retell-ai",          "https://www.retellai.com/"),
    ("bland-ai",           "https://www.bland.ai/"),
    ("cartesia",           "https://cartesia.ai/"),
    ("profound",           "https://www.tryprofound.com/"),
    ("goodie-ai",          "https://www.higoodie.com/"),
    ("llmrefs",            "https://llmrefs.com/"),
    ("dust",               "https://dust.tt/"),
    ("agentforce",         "https://www.salesforce.com/agentforce/"),
    ("moveworks",          "https://www.moveworks.com/"),
    ("rogo",               "https://www.rogo.ai/"),
    ("hebbia",             "https://www.hebbia.com/"),
    ("nabla",              "https://www.nabla.com/"),
    ("nano-banana",        "https://gemini.google/overview/image-generation/"),
    ("seedream-5",         "https://www.volcengine.com/"),
    ("odyssey",            "https://odyssey.ml/"),
    ("granola",            "https://www.granola.ai/"),
    ("limitless",          "https://www.limitless.ai/"),
]


def check(url):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    req = urllib.request.Request(url, headers=HDRS)
    try:
        with urllib.request.urlopen(req, timeout=25, context=ctx) as r:
            body = r.read(200000).decode("utf-8", "replace")
            code = r.getcode()
            final = r.geturl()
    except urllib.error.HTTPError as ex:
        return ex.code, "", "", []
    except Exception as ex:
        return 0, str(ex)[:40], "", []
    m = TITLE.search(body)
    title = re.sub(r"\s+", " ", m.group(1)).strip()[:60] if m else ""
    flags = sorted(set(x.lower() for x in SUNSET.findall(body)))
    return code, title, final, flags


def main():
    alive, suspect, dead = [], [], []
    for slug, url in URLS:
        code, title, final, flags = check(url)
        redir = ""
        if final and final.rstrip("/") != url.rstrip("/"):
            redir = " -> %s" % final[:60]
        if code == 200 and not flags:
            alive.append(slug)
            state = "OK   "
        elif code == 200:
            suspect.append((slug, flags))
            state = "ATTN "
        else:
            dead.append((slug, code))
            state = "KO   "
        print("%s %-20s %-3s %-45s%s" % (state, slug, code, title, redir))
        if flags:
            print("        signaux : %s" % ", ".join(flags))

    print("\n--- resume ---")
    print("en ligne sans signal : %d" % len(alive))
    print("a verifier a la main : %d  %s" % (len(suspect), ", ".join(s for s, _ in suspect)))
    print("injoignables         : %d  %s" % (len(dead), ", ".join("%s(%s)" % d for d in dead)))


if __name__ == "__main__":
    main()
