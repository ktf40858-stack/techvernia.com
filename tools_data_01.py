# -*- coding: utf-8 -*-
"""Lot 1 - Navigateurs AI (nouvelle categorie browsers/).

Contenu redige a la main, un texte par outil, aucun paragraphe partage.
Faits verifies le 2026-09-06 (voir 50_NOUVEAUX_OUTILS_AI_2026-09.md).

Note : ChatGPT Atlas a ete retire de la liste (produit autonome arrete le
9 aout 2026) et remplace par Gemini in Chrome.
"""

CAT = dict(category="browsers", cat_href="../../categories.html",
           cat_label="AI Browsers", app_category="WebApplication")

TOOLS = [

dict(CAT,
 slug="perplexity-comet", name="Perplexity Comet", company="Perplexity AI",
 domain="perplexity.ai", url="https://www.perplexity.ai/comet",
 cta2_url="https://www.perplexity.ai/comet", cta2_label="Download Free",
 flag="&#127482;&#127480;", country="USA", founded="2022", hq="San Francisco, California, USA",
 rating=4.5, date="2026-09-06",
 badges=["Free", "Agentic Browsing", "Cross-Platform"],
 quick_stats=[("Free", "All Platforms"), ("Agent Mode", "Built In"),
              ("Windows / Mac / iOS / Android", "Availability"),
              ("Aug 2026", "Android Launch"), ("2022", "Founded")],
 title="Perplexity Comet Review 2026: The Free Agentic AI Browser | TechVernia",
 meta_desc="Perplexity Comet review 2026. The free agentic AI browser with built-in "
           "search, tab context and task automation across Windows, macOS, iOS and "
           "Android. Features, limits and honest verdict.",
 meta_keywords="Perplexity Comet review, agentic browser, AI browser, Comet vs Dia, "
               "free AI browser, Perplexity browser",
 overview=[
  "Comet is Perplexity's browser, and it is the product that turned the agentic browser from a "
  "waitlist curiosity into something ordinary people actually run as their daily driver. Perplexity "
  "dropped the paywall in October 2025, then made Comet completely free on every platform in March "
  "2026. In August 2026 it landed on Android, making it the first agentic browser shipping on mobile "
  "rather than promising it.",
  "What separates Comet from a browser with a chatbot bolted on is that the assistant sees your tabs. "
  "Ask it to compare the three product pages you have open, pull the pricing out of a PDF in tab four, "
  "or summarise a thread you have been scrolling for ten minutes, and it works from what is actually "
  "on screen rather than from a fresh web search. Perplexity's search stack does the rest: when the "
  "answer is not in your tabs, it goes and gets it, with citations.",
  "Comet's agent mode handles multi-step tasks — filling a form, working through a checkout, "
  "collecting data across a list of pages. It is genuinely useful and genuinely imperfect: it stalls "
  "on heavy JavaScript apps and on anything behind an aggressive bot check. Treat it as a fast junior "
  "assistant you still supervise, not as unattended automation, and it earns its place.",
 ],
 features=[
  ("globe", "Tab-Aware Assistant",
   "The sidebar assistant reads the tabs you already have open, so questions about your current "
   "research do not require re-pasting content or re-running a search."),
  ("zap", "Agent Mode",
   "Multi-step task execution inside the page: form filling, comparison shopping, extracting a table "
   "across paginated results. You watch it work and can interrupt at any step."),
  ("search", "Perplexity Search Built In",
   "The address bar is an answer engine. Queries return a cited synthesis rather than ten blue links, "
   "with the underlying sources one click away."),
  ("brain", "Research Memory",
   "Comet threads memory through research sessions, so a follow-up question days later still carries "
   "the context of what you were investigating."),
  ("monitor", "True Cross-Platform",
   "Windows, macOS, iOS and Android. The Android release in August 2026 made it the first agentic "
   "browser genuinely available on a phone rather than in preview."),
  ("cube", "Chromium Foundation",
   "Built on Chromium, so Chrome extensions, saved passwords and profile import all work. Migration "
   "is a five-minute job, not a project."),
 ],
 pros=[
  "Completely free on every platform since March 2026",
  "Tab context makes the assistant genuinely useful, not decorative",
  "Perplexity's cited search is the best-in-class part of the package",
  "Chromium base means extensions and profile import just work",
  "Only serious agentic browser with a real mobile release",
  "No account gymnastics: install and use",
 ],
 cons=[
  "Agent mode stalls on JavaScript-heavy apps and bot-protected sites",
  "Sending page content to Perplexity is a privacy trade-off some teams cannot make",
  "Free product from a company still searching for its business model",
  "Assistant quality drops on very long pages",
 ],
 pricing=[
  ("Comet", "Free", "Full browser, assistant and agent mode, all platforms"),
  ("Perplexity Pro", "$20 / month", "Higher model limits, Pro Search, file uploads"),
  ("Perplexity Max", "$200 / month", "Frontier model access, highest limits, early features"),
 ],
 excels=[
  "Research-heavy work where you keep a dozen tabs open",
  "Replacing the search-then-skim-ten-tabs loop with a cited answer",
  "Anyone who wants an agentic browser without paying for it",
  "Mobile users who want the same assistant on a phone",
 ],
 not_ideal=[
  "Organisations where page content cannot leave the device",
  "Unattended automation — the agent needs supervision",
  "Users committed to Safari or Firefox ecosystems",
 ],
 comparisons=[
  ("Perplexity Comet vs Dia",
   "Dia is the better-designed browser and the more privacy-conservative one; Comet is the more "
   "capable researcher and the only one of the two on Android. If design and restraint matter more "
   "than reach, Dia wins. For most people doing research, Comet does more."),
  ("Perplexity Comet vs Gemini in Chrome",
   "Gemini in Chrome has distribution Comet can only dream of, and deeper Google Workspace hooks. "
   "Comet's advantage is that the assistant and the search engine are the same product, so citations "
   "and follow-ups are tighter. Comet is also free where Chrome's better agent features are not."),
 ],
 verdict="Comet is the AI browser to try first, and the fact that it costs nothing makes that an easy "
         "recommendation. The tab-aware assistant is the feature that justifies switching browsers at "
         "all — it removes the copy-paste tax from research work — and Perplexity's cited search is "
         "still the best implementation of answer-engine browsing anyone ships. Agent mode is the "
         "weaker half: impressive when it works, and it does not always work. Install it as your "
         "research browser, keep Chrome around for the banking site that breaks, and revisit agent "
         "mode every few months as it improves.",
 faq=[
  ("Is Perplexity Comet free?",
   "Yes. Perplexity dropped the Comet paywall in October 2025 and made the browser completely free on "
   "all platforms in March 2026. A paid Perplexity Pro or Max subscription raises model limits inside "
   "the assistant but is not required to use the browser."),
  ("Which platforms does Comet run on?",
   "Windows, macOS, iOS and Android. The Android release in August 2026 made Comet the first agentic "
   "browser with a genuine mobile version rather than a preview."),
  ("Can Comet use my Chrome extensions?",
   "Yes. Comet is built on Chromium, so Chrome extensions, bookmarks, saved passwords and profiles "
   "import directly. Most people migrate in a few minutes."),
  ("Is Comet safe to use with sensitive pages?",
   "Be careful. The assistant works by reading page content, which means that content reaches "
   "Perplexity's servers. For regulated data, internal dashboards or anything under NDA, use a "
   "separate browser profile or a different browser entirely."),
 ],
 breakdown=[("Search Quality", 9.4), ("Agent Reliability", 7.2),
            ("Platform Coverage", 9.6), ("Privacy", 6.5), ("Value", 9.8)],
 related=[("dia-browser", "Dia", "4.2", "Design-Led AI Browser"),
          ("gemini-in-chrome", "Gemini in Chrome", "4.4", "Agentic Browsing"),
          ("brave-leo", "Brave Leo", "4.1", "Privacy-First AI")],
),

dict(CAT,
 slug="gemini-in-chrome", name="Gemini in Chrome", company="Google",
 domain="google.com/chrome", url="https://www.google.com/chrome/",
 cta2_url="https://gemini.google/", cta2_label="See Gemini Plans",
 flag="&#127482;&#127480;", country="USA", founded="2008", hq="Mountain View, California, USA",
 rating=4.4, date="2026-09-06",
 badges=["Largest Reach", "Google Integrated", "Agentic Browsing"],
 quick_stats=[("Chrome", "Distribution"), ("Gemini", "Model"),
              ("Workspace", "Native Hooks"), ("Free tier", "Entry Price"),
              ("2008", "Chrome Launch")],
 title="Gemini in Chrome Review 2026: Google's Agentic Browser Play | TechVernia",
 meta_desc="Gemini in Chrome review 2026. Google put its assistant inside the world's "
           "most-used browser: page understanding, agentic tasks and Workspace "
           "integration. Strengths, limits and how it compares to Comet.",
 meta_keywords="Gemini in Chrome review, Chrome AI browser, Google agentic browsing, "
               "Gemini browser, Chrome vs Comet",
 overview=[
  "Google did not build a new browser to compete in the AI browser race. It already had the one "
  "everyone uses, and put Gemini inside it. That is the whole strategic story of Gemini in Chrome, "
  "and it is why the product matters more than its feature list suggests: the competition ships "
  "clever browsers nobody has installed, while Google ships a decent assistant to the browser "
  "already open on most desktops on earth.",
  "In practice Gemini in Chrome reads the page you are on and the tabs around it, answers questions "
  "about them, summarises long documents, and increasingly takes actions on your behalf — the "
  "agentic layer that turns 'explain this checkout page' into 'complete this checkout'. Because it "
  "is Google, the hooks into Gmail, Docs, Drive and Calendar are native rather than bolted on, which "
  "is the single biggest practical advantage over every independent AI browser.",
  "The catch is tiering. The basic assistant is free with a Google account; the genuinely useful "
  "agentic capabilities sit behind Google AI Pro and AI Ultra subscriptions, and Ultra is expensive. "
  "You are also handing Google even more of your browsing context than it already had, which for some "
  "organisations is a straightforward disqualifier.",
 ],
 features=[
  ("globe", "Page and Tab Understanding",
   "Ask about the page you are reading or the set of tabs you have open, and get an answer grounded "
   "in that content rather than a generic web search."),
  ("zap", "Agentic Task Execution",
   "Multi-step actions inside the browser — filling forms, working through flows, collecting data "
   "across pages — on the higher subscription tiers."),
  ("layers", "Native Workspace Integration",
   "Gmail, Docs, Drive and Calendar are first-party context, not connectors. Pulling a document into "
   "a browsing task requires no setup."),
  ("search", "Google Search Grounding",
   "Answers can be grounded in live Search results, which remains the broadest index available to any "
   "AI assistant in a browser."),
  ("users", "Zero Migration Cost",
   "It is Chrome. Your extensions, profiles, passwords and sync are already there — the adoption "
   "friction that sinks rival AI browsers simply does not exist."),
  ("lock", "Enterprise Policy Controls",
   "Chrome Enterprise policy lets IT disable or scope the assistant per organisational unit, which "
   "independent AI browsers generally cannot offer."),
 ],
 pros=[
  "Already installed — no browser migration required",
  "Deepest Workspace and Google Search integration of any AI browser",
  "Enterprise policy controls that rivals do not have",
  "Free tier is genuinely usable for summarising and Q&A",
  "Backed by a company that will not shut it down next quarter",
 ],
 cons=[
  "Best agentic features are gated behind AI Pro and the expensive AI Ultra tier",
  "Hands Google even more browsing context",
  "Feature rollout is staggered by region and account type",
  "Less focused than purpose-built agentic browsers",
 ],
 pricing=[
  ("Chrome", "Free", "Browser plus basic Gemini assistance with a Google account"),
  ("Google AI Pro", "$19.99 / month", "Higher limits and expanded agentic features"),
  ("Google AI Ultra", "$249.99 / month", "Frontier models, highest limits, earliest feature access"),
 ],
 excels=[
  "Teams already standardised on Google Workspace",
  "Organisations that need policy control over an AI assistant",
  "Anyone who wants AI browsing without changing browsers",
  "Users who value stability over novelty",
 ],
 not_ideal=[
  "Privacy-sensitive work where Google is the wrong custodian",
  "Users who want the assistant to be the product rather than a feature",
  "Budget-conscious users needing the agentic tier",
 ],
 comparisons=[
  ("Gemini in Chrome vs Perplexity Comet",
   "Comet is the sharper research tool and it is free; Gemini in Chrome is the one you do not have to "
   "install. For deep multi-source research with citations, Comet still reads better. For everything "
   "that touches Gmail, Docs or Calendar, Chrome wins without a contest."),
  ("Gemini in Chrome vs Brave Leo",
   "Opposite philosophies. Brave Leo minimises what leaves your machine and asks for no account; "
   "Gemini in Chrome maximises context by design. Choose on your privacy posture, not on features."),
 ],
 verdict="Gemini in Chrome is not the most interesting AI browser and it does not need to be. "
         "Distribution is the feature: for the overwhelming majority of users the AI browser they end "
         "up using will be the one already on their machine, and Google has made that one competent. "
         "The Workspace integration is the genuine differentiator and no independent browser can "
         "match it. Where it falls down is pricing honesty — the demos that sell the product are the "
         "agentic features, and those live on paid tiers that climb to $249.99 a month. Use the free "
         "tier, and only pay up if you have measured the agent doing real work for you.",
 faq=[
  ("Is Gemini in Chrome free?",
   "The basic assistant is free with a Google account. The more capable agentic features are part of "
   "the Google AI Pro ($19.99/month) and AI Ultra ($249.99/month) subscriptions."),
  ("Do I need to install a different browser?",
   "No — that is the point. Gemini runs inside Chrome, so extensions, profiles, passwords and sync "
   "carry over because nothing changed."),
  ("Can my company disable it?",
   "Yes. Chrome Enterprise policies let administrators disable or scope the assistant per "
   "organisational unit, which is one of the clearest advantages over independent AI browsers."),
  ("Is this what replaced ChatGPT Atlas?",
   "Not directly, but it is the beneficiary. OpenAI discontinued Atlas as a standalone browser on "
   "9 August 2026 and moved its agentic browsing into the ChatGPT desktop app and a Chrome extension "
   "— which means OpenAI's browser strategy now also runs inside Google's browser."),
 ],
 breakdown=[("Reach and Adoption", 10.0), ("Workspace Integration", 9.5),
            ("Agent Reliability", 7.8), ("Privacy", 5.5), ("Value", 7.0)],
 related=[("perplexity-comet", "Perplexity Comet", "4.5", "Free Agentic Browser"),
          ("brave-leo", "Brave Leo", "4.1", "Privacy-First AI"),
          ("opera-neon", "Opera Neon", "3.9", "Power-User Automation")],
),

dict(CAT,
 slug="opera-neon", name="Opera Neon", company="Opera Software",
 domain="operaneon.com", url="https://www.operaneon.com/",
 cta2_url="https://www.opera.com/neon", cta2_label="See Neon Details",
 flag="&#127475;&#127476;", country="Norway", founded="1995", hq="Oslo, Norway",
 rating=3.9, date="2026-09-06",
 badges=["Power Users", "Automation First", "Subscription"],
 quick_stats=[("$19.90/mo", "Subscription"), ("Automation", "Core Focus"),
              ("Norway", "Vendor Origin"), ("Desktop", "Availability"),
              ("1995", "Opera Founded")],
 title="Opera Neon Review 2026: The Power-User Agentic Browser | TechVernia",
 meta_desc="Opera Neon review 2026. A subscription agentic browser aimed at power "
           "users: friction-free text insertion, task automation and a browser vendor "
           "with 30 years of history. Who it is for and who should skip it.",
 meta_keywords="Opera Neon review, agentic browser, Opera AI browser, Neon pricing, "
               "browser automation",
 overview=[
  "Opera Neon is the odd one out in the AI browser field, and deliberately so. Where Perplexity and "
  "Google chase mass adoption with free tiers, Opera built a $19.90-a-month browser aimed at people "
  "who will actually use automation daily and are willing to pay for it. It is a narrower bet, from "
  "the one vendor in this category that has been shipping browsers since 1995.",
  "The product's strongest quality is friction: there is very little of it. Text insertion, "
  "rewriting, and pulling content between contexts happen without the modal-dialog ceremony that "
  "makes assistants in other browsers feel like a detour. For someone whose day is composing, "
  "editing and moving text between web apps, that adds up faster than a benchmark score suggests.",
  "The weakness is that Neon remains an experimental surface rather than a settled product. Opera has "
  "a track record of shipping ambitious browser concepts and then moving on — the original Opera Neon "
  "concept browser of 2017 being the obvious precedent. Treat it as a genuinely useful tool you "
  "should not build a team workflow around until it has a couple more years behind it.",
 ],
 features=[
  ("zap", "Friction-Free Text Insertion",
   "Generating, rewriting and inserting text happens inline without breaking flow — the single "
   "feature power users cite most often as the reason they keep it."),
  ("terminal", "Task Automation",
   "Multi-step browser tasks can be described and re-run, aimed at repetitive web work rather than "
   "one-off questions."),
  ("globe", "Built-In Browser Fundamentals",
   "Ad blocking, a VPN and workspaces come from Opera's mature browser line rather than being bolted "
   "onto a fresh Chromium fork."),
  ("layers", "Workspace Organisation",
   "Tab management for people who run dozens of tabs across separate contexts, inherited from Opera "
   "One's workspace model."),
  ("cube", "Chromium Compatibility",
   "Chromium underneath means Chrome extensions and standard web app compatibility."),
  ("users", "Independent European Vendor",
   "Not owned by a search engine or a model lab, which is a meaningful positioning difference for "
   "some buyers."),
 ],
 pros=[
  "The least intrusive AI text workflow of any browser in this list",
  "Mature browser fundamentals: ad blocking, VPN, workspaces",
  "A vendor with 30 years of browser engineering behind it",
  "Independent of Google, OpenAI and Perplexity",
  "Subscription model means the product is not monetising your data",
 ],
 cons=[
  "$19.90 a month competes against free products that do most of the same job",
  "Experimental surface — Opera has retired ambitious browser concepts before",
  "Smaller user base means fewer community resources when something breaks",
  "Desktop only",
 ],
 pricing=[
  ("Opera One", "Free", "Standard Opera browser with free AI features"),
  ("Opera Neon", "$19.90 / month", "Agentic browsing, automation, power-user AI workflow"),
 ],
 excels=[
  "Writers and editors who move text between web apps all day",
  "Power users who want automation and will pay to avoid rate limits",
  "Buyers who deliberately want a non-US, non-model-lab vendor",
  "People who already like Opera's workspace model",
 ],
 not_ideal=[
  "Casual users — free alternatives cover the basics",
  "Teams needing a stable, long-term standardised browser",
  "Mobile-first workflows",
 ],
 comparisons=[
  ("Opera Neon vs Perplexity Comet",
   "Comet is free and better at research; Neon is paid and better at doing repetitive text work "
   "without getting in your way. If you mostly read and research, Comet. If you mostly write and "
   "repeat, Neon is worth the trial."),
  ("Opera Neon vs Dia",
   "Both are opinionated, design-conscious browsers charging around $20 a month. Dia is the better "
   "looking and better funded after Atlassian's acquisition of The Browser Company; Neon has the more "
   "mature browser underneath it."),
 ],
 verdict="Opera Neon is a real product with a real audience, and that audience is smaller than Opera "
         "would like. The automation and inline text workflow are genuinely better than what free "
         "competitors ship, and the browser fundamentals underneath are the most mature in this "
         "category. But charging $19.90 a month in a field where Comet is free and Chrome is already "
         "installed is a hard sell that only works if you are automating something daily. Try it for "
         "a month against your actual repetitive tasks. If you cannot name three of them, keep the "
         "money.",
 faq=[
  ("How much does Opera Neon cost?",
   "$19.90 per month. Opera's standard browser, Opera One, remains free with a lighter set of AI "
   "features."),
  ("Is Opera Neon the same as the 2017 Opera Neon concept?",
   "No. Opera reused the name. The 2017 Neon was an experimental concept browser; the 2026 product is "
   "a subscription agentic browser aimed at power users."),
  ("Does Opera Neon support Chrome extensions?",
   "Yes. It is built on Chromium, so standard Chrome extensions and web app compatibility carry over."),
  ("Is there a mobile version?",
   "Neon is a desktop product. Opera ships separate mobile browsers with their own AI features."),
 ],
 breakdown=[("Automation Depth", 8.5), ("Text Workflow", 9.0),
            ("Browser Fundamentals", 8.8), ("Value for Money", 6.0), ("Maturity", 6.5)],
 related=[("dia-browser", "Dia", "4.2", "Design-Led AI Browser"),
          ("perplexity-comet", "Perplexity Comet", "4.5", "Free Agentic Browser"),
          ("brave-leo", "Brave Leo", "4.1", "Privacy-First AI")],
),

dict(CAT,
 slug="dia-browser", name="Dia", company="The Browser Company (Atlassian)",
 domain="diabrowser.com", url="https://www.diabrowser.com/",
 cta2_url="https://www.diabrowser.com/", cta2_label="Download Dia",
 flag="&#127482;&#127480;", country="USA", founded="2019", hq="New York, New York, USA",
 rating=4.2, date="2026-09-06",
 badges=["Best Design", "Tab Memory", "Atlassian-Backed"],
 quick_stats=[("$610M", "Atlassian Deal"), ("Free + Pro", "Pricing"),
              ("Tab-Based", "Memory Model"), ("Arc", "Predecessor"),
              ("2019", "Company Founded")],
 title="Dia Browser Review 2026: The Design-Led AI Browser | TechVernia",
 meta_desc="Dia browser review 2026. The Browser Company's successor to Arc, now "
           "Atlassian-owned: tab-based memory, skills and the best interface design "
           "in the AI browser field. Where it shines and where it is unfinished.",
 meta_keywords="Dia browser review, The Browser Company, Arc successor, AI browser, "
               "Dia vs Comet, Atlassian browser",
 overview=[
  "Dia is what happened after The Browser Company decided Arc had reached the end of its road. Arc "
  "had a devoted following and an interface people wrote love letters about; it also had a ceiling. "
  "Dia is the company's answer to what a browser looks like when the assistant is designed in from "
  "the first sketch rather than added to a sidebar, and it shows — this is comfortably the "
  "best-looking product in the category.",
  "The interesting technical choice is memory. Where rivals attach memory to an account or a chat "
  "thread, Dia builds it around tabs and around what the company calls skills: reusable instructions "
  "you teach the browser once and invoke later. It is a more browser-native idea than a chat window "
  "that happens to live next to your web page, and when it clicks it feels like the right answer to "
  "the whole category.",
  "It is also the least finished product here. Features arrive and change, edges are rough, and "
  "reviewers who use it daily consistently describe it as not yet a safe default. The August 2026 "
  "acquisition of The Browser Company by Atlassian for $610 million cuts both ways: it removes the "
  "funding risk that kills ambitious browsers, and it raises a fair question about whose roadmap Dia "
  "now serves.",
 ],
 features=[
  ("brain", "Tab-Based Memory",
   "Memory is organised around what you have been browsing rather than around a chat history, so "
   "context follows your work instead of your conversation."),
  ("book", "Skills",
   "Teach Dia a repeatable instruction once — a summarising style, an extraction format, a review "
   "checklist — then invoke it by name on any page."),
  ("image", "Best-in-Class Interface",
   "The clearest, calmest design in the AI browser field, inherited from the team that built Arc's "
   "much-loved interface."),
  ("lock", "Conservative by Default",
   "Less page content leaves the machine automatically than in rivals, which reviewers consistently "
   "rate as the safest default posture among mainstream AI browsers."),
  ("layers", "Tab Organisation",
   "The Browser Company's core competence: managing many tabs without the tab strip becoming an "
   "unreadable smear."),
  ("users", "Atlassian Backing",
   "Post-acquisition, the funding question that hangs over independent browsers no longer applies."),
 ],
 pros=[
  "The best interface design in the category, by a clear margin",
  "Tab-based memory and skills are the most browser-native ideas anyone has shipped",
  "Conservative privacy defaults compared with rivals",
  "Free tier is usable; Pro is priced in line with competitors",
  "Atlassian's acquisition removes the funding risk",
 ],
 cons=[
  "Genuinely unfinished — reviewers still do not recommend it as a daily driver",
  "Narrowest platform reach of the major AI browsers",
  "Roadmap direction uncertain under new ownership",
  "Smaller feature set than Comet or Chrome",
 ],
 pricing=[
  ("Dia", "Free", "Browser, assistant and core features"),
  ("Dia Pro", "$20 / month", "Higher model limits and expanded skills"),
 ],
 excels=[
  "Designers and writers who care how their tools feel",
  "Former Arc users looking for where that team went",
  "Users who want AI browsing with conservative data defaults",
  "Anyone evaluating where the category is heading rather than what it does today",
 ],
 not_ideal=[
  "Teams that need a stable, standardised browser now",
  "Users on platforms Dia does not cover",
  "Anyone whose main need is heavy agentic automation",
 ],
 comparisons=[
  ("Dia vs Perplexity Comet",
   "Comet does more and costs nothing; Dia is better designed and more careful with your data. Comet "
   "is the pragmatic choice today. Dia is the one to watch, and the one you will enjoy using more."),
  ("Dia vs Arc",
   "Dia is Arc's successor from the same team, not a competitor to it. The Browser Company wound Arc "
   "down to focus on Dia, which is the source of much of the community's frustration and much of "
   "Dia's design pedigree."),
 ],
 verdict="Dia is the most interesting browser in this category and the hardest to recommend today. "
         "The design is superb, the tab-memory and skills model is the smartest structural idea "
         "anyone has had about AI browsing, and the privacy defaults are the most conservative among "
         "mainstream options. It is also visibly unfinished, and Atlassian's $610 million acquisition "
         "leaves an open question about whose product it becomes. Install it as a second browser, use "
         "it for research and writing, and keep something dependable for the work that has to ship "
         "today. In a year this may well be the recommendation rather than the runner-up.",
 faq=[
  ("Is Dia free?",
   "There is a free tier that covers the browser and core assistant. Dia Pro costs $20 per month for "
   "higher model limits and expanded skills."),
  ("What happened to Arc?",
   "The Browser Company wound Arc down to concentrate on Dia. Arc still runs but is no longer the "
   "team's focus, which is why longtime Arc users have been vocal about the transition."),
  ("Who owns Dia now?",
   "Atlassian. The Browser Company was acquired for $610 million in 2026, which secures Dia's funding "
   "but leaves questions about long-term product direction."),
  ("What are Dia skills?",
   "Reusable instructions you define once and invoke by name on any page — a summarising style, an "
   "extraction format, a review checklist. They are Dia's answer to repeating the same prompt."),
 ],
 breakdown=[("Interface Design", 9.7), ("Memory Model", 8.8),
            ("Privacy Defaults", 8.0), ("Feature Completeness", 6.2), ("Stability", 6.5)],
 related=[("perplexity-comet", "Perplexity Comet", "4.5", "Free Agentic Browser"),
          ("opera-neon", "Opera Neon", "3.9", "Power-User Automation"),
          ("gemini-in-chrome", "Gemini in Chrome", "4.4", "Agentic Browsing")],
),

dict(CAT,
 slug="brave-leo", name="Brave Leo", company="Brave Software",
 domain="brave.com", url="https://brave.com/leo/",
 cta2_url="https://brave.com/download/", cta2_label="Download Brave",
 flag="&#127482;&#127480;", country="USA", founded="2015", hq="San Francisco, California, USA",
 rating=4.1, date="2026-09-06",
 badges=["Privacy First", "No Account", "Free Tier"],
 quick_stats=[("No account", "Required"), ("Free", "Base Tier"),
              ("$14.99/mo", "Premium"), ("Built-in", "Ad Blocking"),
              ("2015", "Founded")],
 title="Brave Leo Review 2026: The Privacy-First AI Browser Assistant | TechVernia",
 meta_desc="Brave Leo review 2026. The AI assistant built into Brave: no account "
           "required, no chat retention by default, and a genuine privacy position "
           "rather than a marketing one. Features, Premium pricing and limits.",
 meta_keywords="Brave Leo review, privacy AI browser, Brave AI assistant, Leo Premium, "
               "private AI browsing",
 overview=[
  "Brave Leo is the AI assistant built into the Brave browser, and it is the only entry in this "
  "category where privacy is the product rather than a compliance page. You do not create an account "
  "to use it. Conversations are not retained to train models by default. Requests are proxied so the "
  "model provider does not see your IP address. For anyone who has read the terms of service on the "
  "alternatives, that list is the whole pitch.",
  "Functionally, Leo does the things you expect: summarise the page, answer questions about it, "
  "rewrite selected text, explain a block of code. It is a competent assistant rather than a "
  "spectacular one, and Brave has been deliberately unhurried about adding the agentic task "
  "execution that Comet and Chrome market heavily. If your yardstick is autonomous multi-step "
  "automation, Leo will disappoint you.",
  "That restraint is defensible. An agent that clicks through pages on your behalf is, by "
  "construction, an agent with broad access to your session, and Brave's user base is the one least "
  "likely to want that trade. Leo is the assistant for people who want AI help without a new "
  "surveillance surface, and it is the best option in that specific bracket.",
 ],
 features=[
  ("lock", "No Account Required",
   "Leo works out of the box with no sign-up, no email and no profile. The only AI browser assistant "
   "in this list where that is true."),
  ("eye", "No Chat Retention by Default",
   "Conversations are not stored to train models. Brave proxies requests so the model provider does "
   "not see your IP address."),
  ("globe", "Page and Video Summarisation",
   "Summarise articles, documents and video transcripts inline, without sending your identity along "
   "with the content."),
  ("shield", "Built on Brave's Shields",
   "Runs inside a browser that blocks trackers and ads by default, so the AI layer is not undermined "
   "by the page around it."),
  ("brain", "Multiple Model Backends",
   "Choose between hosted models, with Premium unlocking stronger frontier models and higher rate "
   "limits."),
  ("cpu", "Bring Your Own Local Model",
   "Leo can be pointed at a locally hosted model, so the conversation never leaves your machine at "
   "all — a genuinely rare capability."),
 ],
 pros=[
  "The only serious AI browser assistant that needs no account",
  "Conversations are not retained for training by default",
  "Can be pointed at a local model for full data control",
  "Free tier is genuinely usable, not a teaser",
  "Sits inside a browser with real tracker and ad blocking",
 ],
 cons=[
  "No meaningful agentic task execution — deliberately",
  "Assistant quality trails Comet and Gemini on hard research questions",
  "Premium at $14.99/month is close to full frontier chatbot pricing",
  "Smaller ecosystem and fewer integrations",
 ],
 pricing=[
  ("Leo", "Free", "Assistant, summarisation and rewriting with rate limits, no account"),
  ("Leo Premium", "$14.99 / month", "Frontier model access, higher rate limits, priority"),
 ],
 excels=[
  "Privacy-conscious users and anyone handling sensitive material",
  "Journalists, researchers and security practitioners",
  "Teams that cannot let page content reach a model vendor unproxied",
  "Users who want to run a local model behind the browser assistant",
 ],
 not_ideal=[
  "Anyone who wants agentic multi-step automation",
  "Users needing deep Workspace or Microsoft 365 integration",
  "Heavy research workflows where Comet's citations win",
 ],
 comparisons=[
  ("Brave Leo vs Perplexity Comet",
   "Comet is the stronger researcher and has agent mode; Leo asks for nothing about you and retains "
   "nothing by default. The comparison is not really about features — it is about whether you are "
   "willing to send page content to a vendor to get better answers."),
  ("Brave Leo vs Gemini in Chrome",
   "Diametrically opposed designs. Gemini maximises context by connecting everything Google knows "
   "about you; Leo minimises it. Both are competent. The choice is a policy decision, not a product "
   "comparison."),
 ],
 verdict="Brave Leo will not win a feature bake-off and is not trying to. It is the assistant for "
         "people whose threat model makes the other options unusable, and in that bracket it has no "
         "real competition: no account, no retention by default, proxied requests, and the option to "
         "point it at a model running on your own hardware. The absence of agentic automation is a "
         "genuine limitation and, given what an agent needs access to, a defensible one. If you work "
         "with material that should not reach a vendor's logs, this is your AI browser. If you want "
         "the browser to do your shopping, it is not.",
 faq=[
  ("Is Brave Leo free?",
   "Yes, with rate limits and no account required. Leo Premium at $14.99 per month adds frontier "
   "model access and higher limits."),
  ("Does Brave Leo store my conversations?",
   "Not by default. Conversations are not retained to train models, and Brave proxies requests so the "
   "model provider does not see your IP address."),
  ("Can Leo run a local model?",
   "Yes. Leo can be configured to use a locally hosted model, which keeps the entire conversation on "
   "your machine. It is one of the few browser assistants that supports this."),
  ("Does Brave Leo have an agent mode?",
   "No meaningful multi-step task automation, and that is deliberate. Brave has been slower than "
   "rivals to ship agentic browsing because an agent acting in your session needs broad access to it."),
 ],
 breakdown=[("Privacy", 9.8), ("Assistant Quality", 7.5),
            ("Local Model Support", 9.0), ("Agentic Features", 4.0), ("Value", 8.5)],
 related=[("perplexity-comet", "Perplexity Comet", "4.5", "Free Agentic Browser"),
          ("dia-browser", "Dia", "4.2", "Design-Led AI Browser"),
          ("gemini-in-chrome", "Gemini in Chrome", "4.4", "Agentic Browsing")],
),

]
