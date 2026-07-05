import os, re

BASE = r"C:\Users\Freddy\Desktop\techvernia.com\docs\pages\reviews"

TOOLS = [
    (1,  "Claude Code",          "chatbots/claude-code.html",               "claude.com"),
    (2,  "Meta Llama 4",         "chatbots/meta-llama-4.html",              "meta.ai"),
    (3,  "Google Gemma 4",       "chatbots/google-gemma-4.html",            "ai.google.dev"),
    (4,  "Groq",                 "chatbots/groq.html",                       "groq.com"),
    (5,  "Replicate",            "chatbots/replicate.html",                  "replicate.com"),
    (6,  "Ollama",               "chatbots/ollama.html",                     "ollama.com"),
    (7,  "Watsonx.ai",           "chatbots/watsonx-ai.html",                "ibm.com"),
    (8,  "Perplexity DR",        "chatbots/perplexity-deep-research.html",   "perplexity.ai"),
    (9,  "Manus AI",             "chatbots/manus-ai.html",                  "manus.im"),
    (10, "Genspark",             "chatbots/genspark.html",                   "genspark.ai"),
    (11, "Cline",                "coding/cline.html",                        "cline.bot"),
    (12, "Devin",                "coding/devin.html",                        "cognition.ai"),
    (13, "OpenAI Agents SDK",    "coding/openai-agents-sdk.html",           "openai.com"),
    (14, "Aider",                "coding/aider.html",                        "aider.chat"),
    (15, "Magic Patterns",       "coding/magic-patterns.html",               "magicpatterns.com"),
    (16, "OpenAI Operator",      "coding/openai-operator.html",             "openai.com"),
    (17, "Koala Writer",         "writing/koala-writer.html",                "koalaai.com"),
    (18, "Blaze AI",             "writing/blaze-ai.html",                    "blaze.ai"),
    (19, "Lately AI",            "writing/lately-ai.html",                   "lately.ai"),
    (20, "Undetectable AI",      "writing/undetectable-ai.html",            "undetectable.ai"),
    (21, "DALL-E 4",             "image/dall-e-4.html",                      "openai.com"),
    (22, "Google Imagen 4",      "image/google-imagen-4.html",              "gemini.google.com"),
    (23, "Napkin AI",            "image/napkin-ai.html",                    "napkin.ai"),
    (24, "Khroma",               "image/khroma.html",                        "khroma.co"),
    (25, "Adobe Express AI",     "image/adobe-express-ai.html",             "adobe.com"),
    (26, "Bannerbear",           "image/bannerbear.html",                    "bannerbear.com"),
    (27, "Designs.ai",           "image/designs-ai.html",                   "designs.ai"),
    (28, "Sora",                 "video/sora.html",                          "openai.com"),
    (29, "Veo 3",                "video/veo-3.html",                        "deepmind.google"),
    (30, "Seedance",             "video/seedance.html",                      "seedance.ai"),
    (31, "Hailuo AI",            "video/hailuo-ai.html",                    "hailuoai.video"),
    (32, "Captions.ai",          "video/captions-ai.html",                  "captions.ai"),
    (33, "Topaz Video AI",       "video/topaz-video-ai.html",               "topazlabs.com"),
    (34, "Invideo AI",           "video/invideo.html",                      "invideo.io"),
    (35, "ElevenMusic",          "audio/elevenmusic.html",                  "elevenlabs.io"),
    (36, "Adobe Podcast",        "audio/adobe-podcast-enhance.html",        "adobe.com"),
    (37, "Murf AI",              "audio/murf-ai.html",                      "murf.ai"),
    (38, "PlayHT",               "audio/playht.html",                        "play.ht"),
    (39, "CrewAI",               "agents/crewai.html",                       "crewai.com"),
    (40, "AutoGen",              "agents/autogen.html",                      "microsoft.github.io"),
    (41, "LangChain",            "agents/langchain.html",                   "langchain.com"),
    (42, "n8n",                  "agents/n8n.html",                         "n8n.io"),
    (43, "Make",                 "agents/make.html",                        "make.com"),
    (44, "Gumloop",              "agents/gumloop.html",                     "gumloop.com"),
    (45, "Copilot Studio",       "agents/copilot-studio.html",              "microsoft.com"),
    (46, "UiPath",               "agents/uipath.html",                      "uipath.com"),
    (47, "Dify",                 "agents/dify.html",                        "dify.ai"),
    (48, "Flowise",              "agents/flowise.html",                     "flowiseai.com"),
    (49, "LlamaIndex",           "agents/llamaindex.html",                  "llamaindex.ai"),
    (50, "Nemo Guardrails",      "agents/nemo-guardrails.html",             "github.com"),
    (51, "OpenBox",              "agents/openbox.html",                     "openbox.ai"),
    (60, "tldv",                 "meetings/tldv.html",                      "tldv.io"),
    (61, "Fellow",               "meetings/fellow.html",                    "fellow.app"),
    (62, "Read AI",              "meetings/read-ai.html",                   "read.ai"),
    (68, "Predis.ai",            "marketing/predis.html",                   "predis.ai"),
    (69, "AdCreative.ai",        "marketing/adcreative.html",               "adcreative.ai"),
    (70, "Hootsuite OwlyWriter", "marketing/hootsuite-owlywriter.html",     "hootsuite.com"),
    (71, "Buffer AI",            "marketing/buffer-ai.html",                "buffer.com"),
    (72, "Pencil",               "marketing/pencil.html",                   "trypencil.com"),
    (73, "Muze AI",              "marketing/muze-ai.html",                  "muzecmo.com"),
    (74, "Klaviyo AI",           "marketing/klaviyo.html",                  "klaviyo.com"),
    (78, "Figma AI",             "design/figma-ai.html",                    "figma.com"),
    (79, "Google Stitch",        "design/google-stitch.html",               "withgoogle.com"),
    (80, "Uizard",               "design/uizard.html",                      "uizard.io"),
    (81, "Framer AI",            "design/framer.html",                      "framer.com"),
    (87, "Pitch",                "presentations/pitch.html",                "pitch.com"),
    (88, "Tome",                 "presentations/tome.html",                  "tome.app"),
    (89, "Presentations.AI",     "presentations/presentations-ai.html",     "presentations.ai"),
    (92, "Clio Duo",             "legal/clio-duo.html",                     "clio.com"),
    (93, "ContractPodAi",        "legal/contractpodai.html",                "contractpodai.com"),
    (94, "Workiva AI",           "legal/workiva-ai.html",                   "workiva.com"),
    (95, "Leena AI",             "hr/leena-ai.html",                        "leena.ai"),
    (96, "Gloat",                "hr/gloat.html",                           "gloat.com"),
    (97, "Glide",                "specialized/glide.html",                  "glideapps.com"),
    (98, "MCPCore",              "specialized/mcpcore.html",                "mcpcore.ai"),
    (99, "Perplexity Pages",     "specialized/perplexity-pages.html",       "perplexity.ai"),
    (100,"World Labs",           "specialized/world-labs.html",             "worldlabs.ai"),
]

SKIP_DOMAINS = {
    'techvernia.com','googleapis.com','gstatic.com',
    'googletagmanager.com','pagead2.googlesyndication.com',
    'linkedin.com','schema.org','fonts.google','w3.org'
}

missing_file = []
no_link = []
ok = []

for num, name, rel_path, expected_domain in TOOLS:
    rel_path = rel_path.replace('/', os.sep)
    full_path = os.path.join(BASE, rel_path)
    if not os.path.exists(full_path):
        missing_file.append((num, name, rel_path))
        continue
    content = open(full_path, encoding='utf-8', errors='ignore').read()
    if expected_domain in content:
        ok.append((num, name, expected_domain))
    else:
        links = re.findall(r'href="(https?://[^"]+)"', content)
        ext = [l for l in links if not any(s in l for s in SKIP_DOMAINS)]
        domains = list(dict.fromkeys(re.findall(r'https?://(?:www\.)?([^/"?]+)', ' '.join(ext))))
        no_link.append((num, name, expected_domain, domains[:5]))

print("=" * 65)
print(f"CHECKED: {len(TOOLS)} | OK: {len(ok)} | MISSING FILE: {len(missing_file)} | LINK ISSUE: {len(no_link)}")
print("=" * 65)

if missing_file:
    print("\n--- FILE MISSING (not yet implemented) ---")
    for num, name, path in missing_file:
        print(f"  #{num:02d} {name}")

if no_link:
    print("\n--- LINK ISSUE (expected domain not found) ---")
    for num, name, expected, found in no_link:
        print(f"  #{num:02d} {name}: expected '{expected}' | actual: {found}")

if ok:
    print(f"\n--- OK ({len(ok)} tools) ---")
    for num, name, domain in ok:
        print(f"  #{num:02d} {name}: {domain} OK")

