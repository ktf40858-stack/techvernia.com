# -*- coding: utf-8 -*-
"""Lot 2 - Agents computer-use (agents/) et agents de code (coding/)."""

AG = dict(category="agents", cat_href="../../categories/ai-agents.html",
          cat_label="AI Agents", app_category="DeveloperApplication")
CO = dict(category="coding", cat_href="../../categories/ai-coding.html",
          cat_label="AI Coding", app_category="DeveloperApplication")

TOOLS = [

dict(AG,
 slug="browser-use", name="Browser Use", company="Browser Use",
 domain="browser-use.com", url="https://browser-use.com/",
 cta2_url="https://github.com/browser-use/browser-use", cta2_label="View on GitHub",
 flag="&#127482;&#127480;", country="USA", founded="2024", hq="San Francisco, California, USA",
 rating=4.6, date="2026-09-06",
 badges=["Open Source", "89.1% WebVoyager", "95K Stars"],
 quick_stats=[("89.1%", "WebVoyager"), ("95,000+", "GitHub Stars"),
              ("Python", "Language"), ("MIT-style", "Open Source"), ("2024", "Founded")],
 title="Browser Use Review 2026: The Open-Source Browser Agent Standard | TechVernia",
 meta_desc="Browser Use review 2026. The open-source browser automation framework with "
           "a state-of-the-art 89.1% WebVoyager score and 95,000+ GitHub stars. "
           "Architecture, limits and how it compares to Skyvern and Browserbase.",
 meta_keywords="Browser Use review, browser agent, WebVoyager benchmark, open source "
               "browser automation, Python browser agent",
 overview=[
  "Browser Use is the library that made natural-language browser automation a normal thing to build "
  "with. You describe what you want done — log into this dashboard, pull the last thirty invoices, "
  "put them in a CSV — and the agent drives a real browser to do it, reasoning about the page rather "
  "than replaying a brittle selector script that breaks the next time a designer moves a button.",
  "It is the performance leader among open-source browser agents, with a state-of-the-art 89.1% "
  "success rate on the WebVoyager benchmark, and the adoption to match: over 95,000 GitHub stars "
  "makes it the de-facto standard developers reach for first. That matters more than the benchmark "
  "gap over rivals, because it means the examples, the Stack Overflow answers and the integrations "
  "already exist when you get stuck.",
  "Architecturally it is a framework, not a service. You supply the model API key, you decide where "
  "the browser runs, you own the infrastructure bill. In production most teams pair it with managed "
  "browser infrastructure — Browserbase being the common choice — so Browser Use handles the agent "
  "logic while someone else handles sessions, proxies and the fleet of headless Chromes.",
 ],
 features=[
  ("terminal", "Natural-Language Task Definition",
   "Describe the goal in plain English instead of writing selectors. The agent reasons about the "
   "rendered page, so layout changes do not break the automation."),
  ("git", "Fully Open Source",
   "The complete agent loop is inspectable and forkable. No black box between your prompt and the "
   "clicks it produces — which matters when it does something unexpected."),
  ("brain", "Bring Your Own Model",
   "Works with OpenAI, Anthropic, Google and local models. You control cost, latency and where the "
   "reasoning happens."),
  ("activity", "State-of-the-Art Benchmark Results",
   "89.1% on WebVoyager, the highest published score among open-source browser agents and "
   "competitive with commercial products."),
  ("layers", "Composable with Managed Infrastructure",
   "Pairs cleanly with Browserbase or self-hosted browser fleets. The library does agent logic and "
   "leaves session management to whatever you already run."),
  ("cube", "Python-Native",
   "Ships as a Python library, so it drops into existing data pipelines, schedulers and backend "
   "services without a new runtime."),
 ],
 pros=[
  "Highest published WebVoyager score of any open-source browser agent",
  "95,000+ stars means the ecosystem answers most questions for you",
  "No vendor lock-in — your model keys, your infrastructure",
  "Resilient to layout changes that break selector-based scripts",
  "Free to run beyond model and compute costs",
 ],
 cons=[
  "You own the infrastructure: browsers, proxies, retries, scaling",
  "Model costs on long tasks add up quickly and are easy to under-budget",
  "Non-deterministic by nature — needs verification steps in production",
  "Bot detection on protected sites remains an unsolved problem",
 ],
 pricing=[
  ("Open Source", "Free", "Full framework, self-hosted, you pay only model and compute"),
  ("Cloud", "Usage-based", "Hosted runs without managing browser infrastructure yourself"),
 ],
 excels=[
  "Automating internal tools and dashboards that have no API",
  "Data collection across sites where the layout changes often",
  "Teams that need to inspect and modify the agent loop",
  "Prototyping automations before committing to a commercial platform",
 ],
 not_ideal=[
  "Teams without engineering capacity to run browser infrastructure",
  "Workflows requiring deterministic, audited, repeatable execution",
  "Targets with aggressive bot protection",
 ],
 comparisons=[
  ("Browser Use vs Skyvern",
   "Browser Use leads overall at 89.1% WebVoyager against Skyvern's 85.85%, but Skyvern is measurably "
   "better on form-filling specifically and ships more enterprise scaffolding. Pick Browser Use for "
   "general automation and community depth, Skyvern for high-volume form workflows."),
  ("Browser Use vs Browserbase",
   "They are not competitors — they are layers. Browser Use is the agent logic; Browserbase is the "
   "managed browser infrastructure it runs on. The common 2026 production stack is both together "
   "plus your own model key."),
 ],
 verdict="Browser Use is the correct default for anyone building browser automation in 2026. The "
         "benchmark lead is real but the adoption is the stronger argument: at 95,000 stars, the "
         "problem you hit at 2am has almost certainly been hit and documented by someone else. Go in "
         "clear-eyed about the two costs nobody budgets for — model spend on long-running tasks, and "
         "the engineering time to run browsers reliably at scale. Pair it with managed infrastructure "
         "rather than building a headless Chrome fleet yourself, and add verification steps to "
         "anything that touches production data.",
 faq=[
  ("Is Browser Use free?",
   "The framework is open source and free. You pay for the model API calls the agent makes and for "
   "the compute running the browsers. A hosted cloud option exists for teams that do not want to "
   "manage infrastructure."),
  ("What is the WebVoyager benchmark?",
   "A standard test suite for browser agents measuring end-to-end task success on real websites. "
   "Browser Use's 89.1% is the highest published open-source result; Skyvern follows at 85.85%."),
  ("Which models does it work with?",
   "OpenAI, Anthropic, Google and local models. You supply the key, which means you control cost and "
   "can keep reasoning on your own hardware if required."),
  ("Can it get past bot detection?",
   "Not reliably, and no honest vendor claims otherwise. Sites with aggressive bot protection remain "
   "the hard limit for every browser agent in this category."),
 ],
 breakdown=[("Task Success Rate", 8.9), ("Community and Docs", 9.5),
            ("Flexibility", 9.3), ("Ease of Deployment", 6.8), ("Value", 9.4)],
 related=[("skyvern", "Skyvern", "4.4", "Form-Filling Specialist"),
          ("browserbase", "Browserbase", "4.5", "Browser Infrastructure"),
          ("firecrawl", "Firecrawl", "4.6", "Web-to-LLM Context API")],
),

dict(AG,
 slug="skyvern", name="Skyvern", company="Skyvern",
 domain="skyvern.com", url="https://www.skyvern.com/",
 cta2_url="https://github.com/Skyvern-AI/skyvern", cta2_label="View on GitHub",
 flag="&#127482;&#127480;", country="USA", founded="2024", hq="San Francisco, California, USA",
 rating=4.4, date="2026-09-06",
 badges=["Form Automation", "$17.5M Raised", "Computer Vision"],
 quick_stats=[("85.85%", "WebVoyager"), ("$17.5M", "Funding"),
              ("Vision + LLM", "Approach"), ("Enterprise", "Focus"), ("2024", "Founded")],
 title="Skyvern Review 2026: Vision-Based Browser Automation for Forms | TechVernia",
 meta_desc="Skyvern review 2026. Browser automation combining LLMs and computer vision, "
           "scoring 85.85% on WebVoyager and leading on form-filling. Enterprise "
           "procurement use cases, pricing and honest limits.",
 meta_keywords="Skyvern review, browser automation, form filling automation, computer "
               "vision agent, Skyvern vs Browser Use",
 overview=[
  "Skyvern takes a different route to the same destination as other browser agents: instead of "
  "reasoning purely over the DOM, it combines large language models with computer vision, looking at "
  "the rendered page the way a person does. That choice pays off precisely where DOM-based agents "
  "struggle — forms built by enterprise software vendors, where field labels, hidden inputs and "
  "custom widgets make the underlying markup close to unreadable.",
  "The results back the design. Skyvern scores 85.85% on WebVoyager, slightly behind Browser Use "
  "overall, but it is the best-performing agent specifically on form-filling tasks. That specificity "
  "is the business: the company reports enterprise customers running thousands of procurement "
  "automations per week, which is a category of work that is high-volume, form-shaped and expensive "
  "to staff.",
  "Skyvern raised $17.5 million and is open source with a commercial cloud on top, which is the "
  "familiar and sensible pattern in this space. You can read the code, run it yourself, and buy the "
  "managed version when running browser fleets stops being interesting.",
 ],
 features=[
  ("eye", "Vision-Plus-LLM Page Understanding",
   "Reads the rendered page visually rather than relying on DOM structure, which is why it survives "
   "the badly-built enterprise forms that defeat selector-based tools."),
  ("check", "Best-in-Class Form Filling",
   "The leading agent on form-completion tasks specifically, which is the highest-volume category of "
   "real-world browser automation."),
  ("layers", "Workflow Chaining",
   "Multi-step workflows that pass state between stages, aimed at end-to-end business processes "
   "rather than single tasks."),
  ("git", "Open Source Core",
   "The engine is open source and self-hostable, with a commercial cloud for teams that would rather "
   "not operate it."),
  ("users", "Enterprise Procurement Focus",
   "Documented deployments running thousands of procurement automations per week — a narrow but "
   "genuinely proven use case."),
  ("terminal", "API and Scheduling",
   "Trigger runs from your own systems and schedule recurring workflows, rather than driving "
   "everything from a notebook."),
 ],
 pros=[
  "Best available agent for form-heavy automation",
  "Vision-based approach survives markup that breaks DOM agents",
  "Open source core with a commercial cloud when you want it",
  "Proven at enterprise volume, not just in demos",
  "$17.5M funding gives reasonable continuity confidence",
 ],
 cons=[
  "Lower overall WebVoyager score than Browser Use",
  "Vision inference costs more per step than DOM-only approaches",
  "Smaller community than Browser Use, so fewer worked examples",
  "Narrower general-purpose appeal outside form workflows",
 ],
 pricing=[
  ("Open Source", "Free", "Self-hosted engine, you provide models and infrastructure"),
  ("Cloud Starter", "Usage-based", "Managed runs, scheduling, hosted browsers"),
  ("Enterprise", "Custom", "Volume automation, support, deployment assistance"),
 ],
 excels=[
  "Procurement, onboarding and any high-volume form workflow",
  "Legacy enterprise web apps with unreadable markup",
  "Processes where a human currently retypes data between systems",
  "Teams wanting open source with a commercial escape hatch",
 ],
 not_ideal=[
  "General-purpose browsing and research tasks",
  "Cost-sensitive workloads where vision inference is too expensive",
  "Teams that need the largest possible community",
 ],
 comparisons=[
  ("Skyvern vs Browser Use",
   "Browser Use wins on general tasks and community size; Skyvern wins on forms and ships more "
   "enterprise scaffolding. If your automation is mostly filling things in, Skyvern is the better "
   "tool despite the lower headline benchmark."),
  ("Skyvern vs UiPath",
   "UiPath is mature RPA with governance, audit trails and an army of implementation partners. "
   "Skyvern is dramatically cheaper to start and does not break when a page layout changes. Large "
   "regulated enterprises will still choose UiPath; teams automating a specific painful process "
   "should look at Skyvern first."),
 ],
 verdict="Skyvern is the specialist worth knowing about. Chasing Browser Use on the general benchmark "
         "would be the wrong read: the vision-based approach exists to solve enterprise forms, and on "
         "that specific job it is the best thing available. If your automation problem is people "
         "retyping data into a vendor portal thousands of times a month, this is the tool to trial, "
         "and the open-source core means the trial costs you engineering time rather than a contract. "
         "For general browsing automation, Browser Use remains the better default.",
 faq=[
  ("How does Skyvern differ from Browser Use?",
   "Skyvern uses computer vision alongside the language model to read the rendered page, where "
   "Browser Use reasons primarily over the DOM. That makes Skyvern stronger on badly-built enterprise "
   "forms and Browser Use stronger on general tasks."),
  ("Is Skyvern open source?",
   "Yes, the core engine is open source and self-hostable. A commercial cloud offering adds managed "
   "browsers, scheduling and support."),
  ("What is Skyvern actually used for in production?",
   "Predominantly high-volume form workflows. The company reports enterprise customers running "
   "thousands of procurement automations per week."),
  ("Is vision-based automation more expensive?",
   "Yes. Sending page screenshots to a vision model costs more per step than DOM-only reasoning. The "
   "trade is reliability on pages where DOM approaches simply fail."),
 ],
 breakdown=[("Form Automation", 9.5), ("General Task Success", 8.6),
            ("Enterprise Readiness", 8.4), ("Cost Efficiency", 6.8), ("Community", 7.5)],
 related=[("browser-use", "Browser Use", "4.6", "Open-Source Browser Agent"),
          ("browserbase", "Browserbase", "4.5", "Browser Infrastructure"),
          ("uipath", "UiPath", "4.5", "Enterprise RPA")],
),

dict(AG,
 slug="browserbase", name="Browserbase", company="Browserbase",
 domain="browserbase.com", url="https://www.browserbase.com/",
 cta2_url="https://www.browserbase.com/pricing", cta2_label="See Pricing",
 flag="&#127482;&#127480;", country="USA", founded="2024", hq="San Francisco, California, USA",
 rating=4.5, date="2026-09-06",
 badges=["Infrastructure", "$300M Valuation", "Managed Sessions"],
 quick_stats=[("$40M", "Raised"), ("$300M", "Valuation"),
              ("Managed", "Browser Fleet"), ("Stagehand", "Own Framework"), ("2024", "Founded")],
 title="Browserbase Review 2026: Managed Browser Infrastructure for AI Agents | TechVernia",
 meta_desc="Browserbase review 2026. The managed headless browser infrastructure behind "
           "much of the agent economy: sessions, proxies, recordings, Agent runs and a "
           "model gateway. Pricing, architecture and when you actually need it.",
 meta_keywords="Browserbase review, headless browser infrastructure, browser agent "
               "hosting, Stagehand, managed Playwright",
 overview=[
  "Browserbase sells the least glamorous and most necessary part of the browser-agent stack: "
  "somewhere for the browsers to actually run. Anyone who has tried to operate a fleet of headless "
  "Chrome instances in production knows the shape of the problem — memory leaks, zombie processes, "
  "proxy rotation, session persistence, and the debugging nightmare of a failure you cannot see. "
  "Browserbase runs that fleet so you do not have to.",
  "The product gives you sessions with persistent profiles and cookies, residential and datacenter "
  "proxies, and full recordings of every run — which turns the worst part of agent debugging, "
  "'why did it click there', into something you can watch. In 2026 the platform expanded beyond raw "
  "infrastructure into Agent runs, a Runtime for deploying agents on Browserbase's own machines, and "
  "a Model Gateway, moving it up the stack toward being a platform rather than a utility.",
  "The company raised $40 million at a $300 million valuation, and it maintains Stagehand, its own "
  "open-source agent framework. In practice the common production pattern in 2026 is agent logic "
  "from Browser Use or Stagehand, sessions from Browserbase, and your own model key.",
 ],
 features=[
  ("cube", "Managed Headless Browser Sessions",
   "Browsers that start fast, stay alive as long as you need and get cleaned up properly — the "
   "infrastructure problem that eats weeks of engineering time when self-hosted."),
  ("lock", "Persistent Profiles and Cookies",
   "Sessions retain login state between runs, which is what makes recurring automation against "
   "authenticated dashboards practical."),
  ("globe", "Proxy Management",
   "Residential and datacenter proxies with rotation, handled at the platform level rather than "
   "wired in by hand."),
  ("eye", "Full Session Recordings",
   "Watch exactly what the agent saw and did. This turns opaque agent failures into ordinary "
   "debugging."),
  ("zap", "Agent Runs and Runtime",
   "Deploy and execute agents on Browserbase infrastructure rather than only borrowing its browsers."),
  ("git", "Stagehand Framework",
   "The company maintains its own open-source agent framework, so you can adopt the whole stack or "
   "just the infrastructure layer."),
 ],
 pros=[
  "Removes the single hardest operational problem in browser automation",
  "Session recordings make agent debugging tractable",
  "Persistent profiles enable recurring authenticated workflows",
  "Framework-agnostic — works with Browser Use, Playwright or Stagehand",
  "Well funded at $40M and a $300M valuation",
 ],
 cons=[
  "Usage-based pricing gets expensive at high volume versus self-hosting",
  "Another vendor in the critical path of your automation",
  "Sending authenticated sessions to a third party is a real risk decision",
  "Overkill for small, occasional automation jobs",
 ],
 pricing=[
  ("Free", "$0", "Limited browser hours for evaluation"),
  ("Developer", "From $39 / month", "Concurrent sessions, proxies, recordings"),
  ("Scale", "Usage-based", "Higher concurrency, residential proxies, priority support"),
  ("Enterprise", "Custom", "Dedicated capacity, SLAs, compliance review"),
 ],
 excels=[
  "Production browser agents that must run reliably and unattended",
  "Recurring automation against authenticated dashboards",
  "Teams who would rather ship agent logic than operate Chrome",
  "Debugging agent behaviour that fails only in production",
 ],
 not_ideal=[
  "Occasional local scripts where a local browser is fine",
  "Very high volume where self-hosting is genuinely cheaper",
  "Workflows where session credentials cannot leave your infrastructure",
 ],
 comparisons=[
  ("Browserbase vs self-hosting Playwright",
   "Self-hosting is cheaper per run and dramatically more expensive per engineer-hour. Browserbase is "
   "worth it until your volume is large enough that a dedicated infrastructure engineer costs less "
   "than the bill — a threshold most teams never reach."),
  ("Browserbase vs Firecrawl",
   "Different jobs. Firecrawl turns pages into clean structured content for a model to read; "
   "Browserbase gives an agent a real browser to act in. Reading versus doing. Many stacks use both."),
 ],
 verdict="Browserbase solves a problem that is boring right up until it takes down your automation at "
         "3am. Managed sessions with persistent profiles and full recordings remove most of the "
         "operational pain of running browser agents, and the recordings alone justify the price the "
         "first time you debug an agent that only misbehaves in production. Watch two things: the "
         "usage-based bill, which surprises teams as volume grows, and the security question of "
         "authenticated sessions living on someone else's infrastructure. For most teams building "
         "browser agents in 2026, this is the right layer to buy rather than build.",
 faq=[
  ("What does Browserbase actually do?",
   "It runs headless browsers as a managed service — sessions, persistent profiles, proxies and "
   "recordings — so you can build browser agents without operating a Chrome fleet yourself."),
  ("Does it replace Browser Use or Skyvern?",
   "No. Those are agent frameworks; Browserbase is the infrastructure they run on. The standard 2026 "
   "production stack combines an agent framework, Browserbase sessions and your own model key."),
  ("What is Stagehand?",
   "Browserbase's own open-source browser agent framework. You can use it with Browserbase or use "
   "Browserbase with a different framework — the infrastructure is framework-agnostic."),
  ("Is it safe to run authenticated sessions there?",
   "It is a genuine risk decision. Persistent profiles mean login state lives on Browserbase "
   "infrastructure. For regulated data or high-value accounts, review it properly before deploying."),
 ],
 breakdown=[("Reliability", 9.2), ("Debugging Tools", 9.4),
            ("Framework Flexibility", 9.0), ("Cost at Scale", 6.5), ("Security Posture", 7.2)],
 related=[("browser-use", "Browser Use", "4.6", "Open-Source Browser Agent"),
          ("skyvern", "Skyvern", "4.4", "Form-Filling Specialist"),
          ("firecrawl", "Firecrawl", "4.6", "Web-to-LLM Context API")],
),

dict(AG,
 slug="firecrawl", name="Firecrawl", company="Firecrawl (Mendable)",
 domain="firecrawl.dev", url="https://www.firecrawl.dev/",
 cta2_url="https://www.firecrawl.dev/pricing", cta2_label="See Pricing",
 flag="&#127482;&#127480;", country="USA", founded="2023", hq="San Francisco, California, USA",
 rating=4.6, date="2026-09-06",
 badges=["Web to LLM", "Developer Favourite", "Open Source"],
 quick_stats=[("Markdown", "Output Format"), ("Crawl + Scrape", "Core API"),
              ("Open Source", "Self-Hostable"), ("Mendable", "Same Team"), ("2023", "Founded")],
 title="Firecrawl Review 2026: The Web-to-LLM Context API | TechVernia",
 meta_desc="Firecrawl review 2026. The API that turns any website into clean, "
           "LLM-ready markdown or structured JSON. Crawling, scraping, extraction, "
           "pricing and how it fits a RAG or agent stack.",
 meta_keywords="Firecrawl review, web scraping API, LLM context, RAG data pipeline, "
               "website to markdown, Firecrawl pricing",
 overview=[
  "Firecrawl exists because feeding the web to a language model is far more annoying than it sounds. "
  "Raw HTML is full of navigation, cookie banners, tracking scripts and boilerplate; half the modern "
  "web renders client-side and returns nothing useful to a naive fetch. Firecrawl handles the "
  "JavaScript rendering, strips the noise and hands back clean markdown or structured JSON that a "
  "model can actually use.",
  "The API covers the three shapes of the problem: scrape a single page, crawl a whole site "
  "respecting its structure, or extract specific fields against a schema you define. That last mode "
  "is the one that quietly replaces a lot of bespoke parsing code — you describe the fields you want "
  "and get typed data back rather than writing selectors that rot.",
  "It has become the default ingestion layer for RAG pipelines and agent stacks, from the team that "
  "previously built Mendable, one of the first commercial chat-with-your-data products. It is open "
  "source and self-hostable, with a managed API for people who do not want to run crawlers, and it "
  "is heavily used as an MCP server so coding agents can pull live documentation.",
 ],
 features=[
  ("globe", "JavaScript-Rendered Scraping",
   "Renders client-side pages before extracting, so single-page applications return real content "
   "instead of an empty shell."),
  ("book", "Clean Markdown Output",
   "Strips navigation, ads and boilerplate and returns readable markdown — the format models handle "
   "best and the one that keeps token costs sane."),
  ("layers", "Whole-Site Crawling",
   "Crawl a documentation site or knowledge base respecting sitemaps and depth limits, in one call "
   "rather than an orchestration project."),
  ("search", "Schema-Based Extraction",
   "Define the fields you want and get typed JSON back. Replaces a surprising amount of hand-written "
   "and constantly-breaking parsing code."),
  ("git", "Open Source and Self-Hostable",
   "Run it on your own infrastructure when data cannot leave your network, or use the managed API "
   "when it can."),
  ("link", "MCP Server",
   "Exposed over the Model Context Protocol, so coding agents and assistants can pull live web "
   "content as a native tool."),
 ],
 pros=[
  "Removes the entire messy layer between the web and a working RAG pipeline",
  "Handles JavaScript-rendered sites that naive scrapers cannot",
  "Schema extraction eliminates a lot of brittle parsing code",
  "Open source, so self-hosting is a genuine option",
  "First-class MCP support fits the 2026 agent stack",
 ],
 cons=[
  "Credit-based pricing is hard to forecast for large crawls",
  "Cannot bypass aggressive bot protection — nobody legitimately can",
  "Extraction quality drops on unusual or deeply nested layouts",
  "You still own the legal and ethical questions about what you crawl",
 ],
 pricing=[
  ("Free", "$0", "Limited monthly credits for evaluation"),
  ("Hobby", "From $16 / month", "Higher credit allowance, standard rate limits"),
  ("Standard", "From $83 / month", "Production volume, concurrency, priority"),
  ("Enterprise", "Custom", "Volume pricing, SLAs, self-hosted support"),
 ],
 excels=[
  "Building RAG pipelines over documentation and knowledge bases",
  "Giving coding agents live access to current library documentation",
  "Turning competitor or market pages into structured data",
  "Replacing hand-written scrapers that break every few weeks",
 ],
 not_ideal=[
  "Sites with strong bot protection",
  "Very large crawls where credit pricing beats self-hosting",
  "Use cases where crawling raises copyright or terms-of-service problems",
 ],
 comparisons=[
  ("Firecrawl vs Browser Use",
   "Firecrawl reads the web; Browser Use acts on it. If you need content in a model's context, "
   "Firecrawl is faster, cheaper and more reliable. If you need something clicked, filled or "
   "submitted, you need an agent."),
  ("Firecrawl vs building your own scraper",
   "Your own scraper is free until you count the maintenance. Firecrawl's real value is that "
   "JavaScript rendering, retries, rate limiting and markdown cleanup are someone else's problem "
   "forever. Self-host it if the bill grows — the code is open."),
 ],
 verdict="Firecrawl is one of the few tools in this list that pays for itself in the first afternoon. "
         "The gap between 'I have a URL' and 'I have clean text a model can reason about' is where an "
         "enormous amount of engineering time disappears, and Firecrawl closes it with one API call. "
         "Schema-based extraction is the underrated feature — it quietly deletes the brittle parsing "
         "layer most teams maintain by hand. Watch the credit consumption on large crawls, and "
         "remember that being able to crawl something is not the same as being allowed to.",
 faq=[
  ("What does Firecrawl return?",
   "Clean markdown by default, or structured JSON when you supply a schema. Both are formats language "
   "models handle well, unlike raw HTML."),
  ("Can Firecrawl handle JavaScript-heavy sites?",
   "Yes. It renders pages before extraction, so single-page applications return real content rather "
   "than an empty shell."),
  ("Is Firecrawl open source?",
   "Yes, and self-hostable. The managed API exists for teams that would rather not operate crawling "
   "infrastructure, but running it yourself is a supported path."),
  ("How does Firecrawl pricing work?",
   "Credit-based, with a free tier for evaluation and paid tiers from around $16 per month. Large "
   "crawls consume credits quickly, so model the cost before pointing it at an entire site."),
 ],
 breakdown=[("Extraction Quality", 9.2), ("Ease of Integration", 9.6),
            ("JavaScript Handling", 9.0), ("Cost Predictability", 7.0), ("Openness", 9.3)],
 related=[("browser-use", "Browser Use", "4.6", "Open-Source Browser Agent"),
          ("browserbase", "Browserbase", "4.5", "Browser Infrastructure"),
          ("langchain", "LangChain", "4.4", "Agent Framework")],
),

dict(CO,
 slug="opencode", name="OpenCode", company="SST",
 domain="opencode.ai", url="https://opencode.ai/",
 cta2_url="https://github.com/sst/opencode", cta2_label="View on GitHub",
 flag="&#127482;&#127480;", country="USA", founded="2024", hq="Distributed / remote",
 rating=4.6, date="2026-09-06",
 badges=["Open Source", "120K Stars", "Bring Your Own Model"],
 quick_stats=[("120,000+", "GitHub Stars"), ("Terminal", "Interface"),
              ("Any Model", "Provider"), ("Zen", "Usage Plans"), ("2024", "First Release")],
 title="OpenCode Review 2026: The Open-Source Coding Agent | TechVernia",
 meta_desc="OpenCode review 2026. The open-source terminal coding agent that hit "
           "120,000 GitHub stars by letting developers bring their own model and API "
           "key. Architecture, Zen plans and how it compares to Claude Code and Cursor.",
 meta_keywords="OpenCode review, open source coding agent, terminal AI coding, "
               "OpenCode vs Claude Code, bring your own model",
 overview=[
  "OpenCode is the coding agent that grew fastest in 2026 by refusing the industry's default bargain. "
  "Every commercial agent ties you to its vendor's models; OpenCode ships the agent and lets you "
  "bring your own key — Claude, GPT, Gemini, or a model running on your own hardware. For teams with "
  "existing model contracts, procurement constraints, or simply a preference for not being resold "
  "inference at a markup, that is the entire argument.",
  "It reached over 120,000 GitHub stars, which puts it among the most-starred developer tools of the "
  "year, and the growth is not purely ideological. It runs in the terminal, which means it works over "
  "SSH, inside containers, on a build server and in every editor at once, rather than being a feature "
  "of one IDE. Developers who live in tmux rather than in a GUI found something built for them.",
  "The commercial layer arrived without breaking the free core: Zen usage-based plans for people who "
  "would rather buy credits than manage provider keys. The project is maintained by SST, and the "
  "governance question that follows every fast-growing open-source developer tool — what happens when "
  "the commercial layer and the free core disagree — is worth watching rather than worrying about "
  "yet.",
 ],
 features=[
  ("terminal", "Terminal-Native",
   "Runs where developers already work. Works over SSH, in containers and on remote build machines, "
   "with no dependency on a particular editor."),
  ("brain", "Bring Your Own Model",
   "Point it at Claude, GPT, Gemini or a locally hosted model. You control the cost, the provider "
   "and where your code is sent."),
  ("git", "Fully Open Source",
   "The agent loop is auditable, which matters for organisations that must know what leaves their "
   "network and why."),
  ("layers", "Multi-File Codebase Work",
   "Plans and executes changes across many files, rather than completing the line you are typing."),
  ("zap", "Zen Usage Plans",
   "Optional paid credits for teams that would rather not manage provider keys and rate limits "
   "themselves."),
  ("lock", "Self-Hostable End to End",
   "Combined with a local model, code never leaves your infrastructure — a genuinely rare property "
   "among capable coding agents."),
 ],
 pros=[
  "No vendor lock-in: your model, your key, your data path",
  "120,000+ stars means a very active ecosystem and fast bug fixes",
  "Terminal-native, so it works over SSH and in CI where GUI tools cannot",
  "Free core, with optional paid credits rather than a paywall",
  "Can run fully offline against a local model",
 ],
 cons=[
  "You manage model keys, rate limits and cost yourself",
  "No integrated GUI — a real barrier for editor-centric developers",
  "Quality depends entirely on which model you point it at",
  "Governance of the free core versus the commercial layer is unproven",
 ],
 pricing=[
  ("Open Source", "Free", "Full agent, bring your own model API key"),
  ("Zen", "Usage-based", "Prepaid credits, no provider key management"),
 ],
 excels=[
  "Teams with existing model contracts or procurement constraints",
  "Remote development over SSH and inside containers",
  "Regulated environments needing a fully self-hosted coding agent",
  "Developers who want to read the agent loop they are running",
 ],
 not_ideal=[
  "Developers who want a polished GUI experience",
  "Teams that want one vendor to call when something breaks",
  "Anyone unwilling to manage model costs",
 ],
 comparisons=[
  ("OpenCode vs Claude Code",
   "Claude Code is the stronger out-of-the-box agent, tuned end to end against Anthropic's models and "
   "backed by a vendor. OpenCode trades that polish for freedom: any model, any environment, full "
   "source. Teams that must control the data path or already buy inference elsewhere pick OpenCode."),
  ("OpenCode vs Cursor",
   "Cursor is an editor with an agent inside it; OpenCode is an agent with no opinion about your "
   "editor. If you work in a GUI, Cursor is more comfortable. If you work over SSH or across many "
   "machines, Cursor cannot follow you there."),
 ],
 verdict="OpenCode earned its 120,000 stars on a straightforward proposition: the coding agent should "
         "not decide which model you use or where your code goes. Terminal-native execution makes it "
         "the only serious option for a lot of real environments — remote servers, containers, "
         "air-gapped networks — and the ability to run it against a local model is a genuine "
         "differentiator for regulated work. It is less polished than the commercial agents and you "
         "carry the cost management yourself. If you value control over convenience, this is the "
         "coding agent to adopt; if you want it to just work on day one, buy one instead.",
 faq=[
  ("Is OpenCode free?",
   "The agent is open source and free. You supply your own model API key and pay that provider "
   "directly. Optional Zen plans sell prepaid credits for teams that prefer not to manage keys."),
  ("Which models does OpenCode support?",
   "Claude, GPT, Gemini and locally hosted models. Choosing a weaker model produces a weaker agent, "
   "so model choice matters more here than with vendor-tied tools."),
  ("Does OpenCode work without an internet connection?",
   "Yes, if you point it at a locally hosted model. That combination keeps code entirely inside your "
   "own infrastructure, which is why it appears in regulated environments."),
  ("Who maintains OpenCode?",
   "SST maintains the project. The core remains open source alongside the commercial Zen plans."),
 ],
 breakdown=[("Model Flexibility", 9.8), ("Codebase Understanding", 8.4),
            ("Environment Coverage", 9.5), ("Polish", 7.0), ("Value", 9.5)],
 related=[("cursor", "Cursor", "4.7", "AI-First Code Editor"),
          ("github-copilot", "GitHub Copilot", "4.6", "IDE Coding Assistant"),
          ("openai-codex", "OpenAI Codex", "4.4", "OpenAI Coding Agent")],
),

]
