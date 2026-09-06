# -*- coding: utf-8 -*-
"""Lot 7 - Agents vocaux (voice/) et visibilite dans les moteurs AI / GEO (seo/)."""

VO = dict(category="voice", cat_href="../../categories.html",
          cat_label="AI Voice Agents", app_category="BusinessApplication")
SE = dict(category="seo", cat_href="../../categories/ai-seo.html",
          cat_label="AI SEO Tools", app_category="BusinessApplication")

TOOLS = [

dict(VO,
 slug="retell-ai", name="Retell AI", company="Retell AI",
 domain="retellai.com", url="https://www.retellai.com/",
 cta2_url="https://dashboard.retellai.com/", cta2_label="Start Free",
 flag="&#127482;&#127480;", country="USA", founded="2023", hq="San Francisco, California, USA",
 rating=4.5, date="2026-09-06",
 badges=["Best All-Round", "$0.07/min", "HIPAA"],
 quick_stats=[("$0.07/min", "Entry Price"), ("580-620ms", "Measured Latency"),
              ("HIPAA", "Compliance"), ("No-code + SDK", "Both"), ("2023", "Founded")],
 title="Retell AI Review 2026: Production Voice Agents Without the Assembly | TechVernia",
 meta_desc="Retell AI review 2026. The best all-round voice AI platform: a no-code "
           "builder plus a developer SDK, HIPAA compliance and transparent pricing "
           "from $0.07 per minute. Latency, limits and how it compares to Vapi.",
 meta_keywords="Retell AI review, voice AI platform, AI phone agent, no-code voice "
               "agent, Retell vs Vapi, HIPAA voice AI",
 overview=[
  "Retell AI occupies the position most buyers actually want: capable enough for production, simple "
  "enough to ship this month. It pairs a no-code agent builder with a real developer SDK, which "
  "means an operations lead can build and iterate on the conversation flow while engineering handles "
  "the integrations — rather than every change queuing behind a developer.",
  "The numbers hold up. Independent testing across large call samples put Retell in the 580 to 620 "
  "millisecond range, comfortably inside the threshold where conversations stay natural, and pricing "
  "starts at $0.07 per minute with unusual transparency for this category. HIPAA compliance is "
  "available, which quietly matters a great deal — healthcare is one of the largest genuine markets "
  "for voice agents and most platforms cannot serve it.",
  "The trade-off against Vapi is control. Retell makes more decisions for you, which is exactly why "
  "it is faster to deploy and exactly why a team with unusual latency or provider requirements will "
  "eventually feel constrained. For the large majority of use cases — appointment booking, call "
  "qualification, support triage, reminders — those decisions are the right ones.",
 ],
 features=[
  ("monitor", "No-Code Builder with Developer SDK",
   "Non-engineers build and iterate conversation flows while engineering owns the integrations — the "
   "division of labour that keeps voice projects moving."),
  ("zap", "Consistent Sub-620ms Latency",
   "Measured at 580 to 620 milliseconds across large call samples, inside the range where callers do "
   "not start talking over the agent."),
  ("shield", "HIPAA Compliance",
   "Available compliance for healthcare deployments, which is one of the largest real markets for "
   "voice agents and one most platforms cannot enter."),
  ("terminal", "Function Calling",
   "Agents call your systems mid-call to check availability, look up accounts or book appointments, "
   "which is what makes them useful rather than conversational."),
  ("link", "Telephony and Integrations",
   "Phone numbers, call routing and integrations with common CRM and scheduling tools included."),
  ("activity", "Transparent Per-Minute Pricing",
   "Published rates from $0.07 per minute, which is rarer in this category than it should be."),
 ],
 pros=[
  "Best balance of capability and time to deploy in the category",
  "No-code plus SDK suits how teams actually divide voice work",
  "Transparent pricing rather than mandatory sales calls",
  "HIPAA compliance opens healthcare use cases",
  "Latency consistently inside the natural-conversation threshold",
 ],
 cons=[
  "Less configurable than Vapi for unusual requirements",
  "Per-minute costs climb at high outbound volume versus Bland",
  "Provider choices are more constrained by design",
  "Complex multi-agent flows hit the builder's limits",
 ],
 pricing=[
  ("Pay as you go", "From $0.07 / minute", "Full platform, no minimum commitment"),
  ("Volume", "Custom", "Discounted rates at scale"),
  ("Enterprise", "Custom", "HIPAA, dedicated support, compliance review"),
 ],
 excels=[
  "Appointment booking, reminders and call qualification",
  "Healthcare deployments requiring HIPAA",
  "Teams needing production voice agents in weeks not quarters",
  "Organisations where non-engineers must own the conversation design",
 ],
 not_ideal=[
  "Very high volume outbound where per-minute cost dominates",
  "Teams with unusual latency or provider requirements",
  "Highly complex multi-agent conversation architectures",
 ],
 comparisons=[
  ("Retell AI vs Vapi",
   "Vapi exposes every layer and expects engineering ownership; Retell makes sensible defaults and "
   "ships faster. If voice is your product, Vapi. If voice solves a business problem, Retell is "
   "almost certainly the better use of your time."),
  ("Retell AI vs Bland AI",
   "Bland is meaningfully cheaper at high outbound volume and built for that specific shape of work. "
   "Retell is the better general platform with compliance coverage Bland does not match. Volume "
   "economics decide it."),
 ],
 verdict="Retell AI is the voice platform to start with unless you have a specific reason not to. It "
         "gets the important things right — latency inside the natural-conversation threshold, "
         "transparent pricing, HIPAA availability — and it structures the work so conversation design "
         "and engineering can proceed in parallel rather than in series. You will outgrow it if voice "
         "becomes your core product or if outbound volume makes per-minute cost the dominant factor. "
         "For everyone else, it is the shortest credible path from idea to a phone agent that works.",
 faq=[
  ("How much does Retell AI cost?",
   "From $0.07 per minute on pay-as-you-go, with volume discounts and custom enterprise pricing. "
   "Published rates rather than a mandatory sales conversation."),
  ("Is Retell AI HIPAA compliant?",
   "HIPAA compliance is available, which makes it one of the few voice platforms usable for "
   "healthcare deployments."),
  ("Do I need developers to use it?",
   "Not for conversation design — the no-code builder covers that. You will want engineering for "
   "integrations with your own systems, which is what the SDK is for."),
  ("What latency does it achieve?",
   "Around 580 to 620 milliseconds in independent testing across large call samples, inside the range "
   "where conversations stay natural."),
 ],
 breakdown=[("Time to Deploy", 9.5), ("Latency", 8.8),
            ("Compliance", 9.0), ("Configurability", 7.5), ("Value", 8.8)],
 related=[("vapi", "Vapi", "4.6", "Developer Voice Platform"),
          ("bland-ai", "Bland AI", "4.3", "High-Volume Outbound"),
          ("cartesia", "Cartesia", "4.5", "Real-Time Voice Models")],
),

dict(VO,
 slug="bland-ai", name="Bland AI", company="Bland AI",
 domain="bland.ai", url="https://www.bland.ai/",
 cta2_url="https://app.bland.ai/", cta2_label="Start Building",
 flag="&#127482;&#127480;", country="USA", founded="2023", hq="San Francisco, California, USA",
 rating=4.3, date="2026-09-06",
 badges=["High Volume", "$0.09/min All-In", "Co-Located Inference"],
 quick_stats=[("$0.09/min", "All-In Price"), ("30-50%", "Cheaper at Volume"),
              ("Co-located", "Inference"), ("Outbound", "Primary Use"), ("2023", "Founded")],
 title="Bland AI Review 2026: Voice Agents Built for Outbound Volume | TechVernia",
 meta_desc="Bland AI review 2026. Engineer-built voice AI with co-located inference and "
           "all-in pricing at $0.09 per minute, 30-50% cheaper than rivals at high "
           "outbound volume. Latency reality, use cases and honest limits.",
 meta_keywords="Bland AI review, outbound voice AI, AI cold calling, voice agent "
               "pricing, Bland vs Vapi, high volume voice automation",
 overview=[
  "Bland AI is built by engineers for engineers, and its architectural choices all point the same "
  "direction: run the whole pipeline yourself, co-located, rather than stitching together third-party "
  "providers across the network. Aggressive audio buffering, predictive turn-taking and co-located "
  "inference are the specific techniques, and the goal is removing the network hops that add latency "
  "and cost in a multi-vendor stack.",
  "The commercial consequence is the real story: $0.09 per minute all-in, which comes out 30 to 50 "
  "per cent cheaper than Vapi or Retell once you have paid for their model, voice and telephony "
  "providers separately. At a thousand calls a day that difference is the entire business case, and "
  "it is why Bland shows up in high-volume outbound operations rather than in one-off support "
  "deflection projects.",
  "Be careful with the latency claims, because published figures disagree. Bland's own architecture "
  "targets 400 to 700 milliseconds end to end, while independent testing across large samples "
  "measured closer to 800 milliseconds on average. Both can be true depending on configuration and "
  "call type — but 800 milliseconds is the threshold where callers start talking over the agent, so "
  "test with your own scripts before committing volume.",
 ],
 features=[
  ("cpu", "Co-Located Inference",
   "Model, speech and telephony run together rather than across third-party network hops, which is "
   "where multi-vendor stacks lose both latency and margin."),
  ("zap", "Predictive Turn-Taking",
   "Anticipates when the caller has finished speaking rather than waiting on silence detection, which "
   "is what makes a conversation feel unhurried."),
  ("activity", "All-In Per-Minute Pricing",
   "$0.09 per minute covers the whole stack — no separate model, voice and telephony bills to "
   "reconcile."),
  ("layers", "Built for Outbound Campaigns",
   "Designed around high-volume outbound rather than adapted to it, which shows in the campaign and "
   "concurrency tooling."),
  ("terminal", "Developer-First API",
   "An API built for engineers integrating voice into a larger system rather than a no-code builder."),
  ("lock", "Self-Contained Infrastructure",
   "Fewer third parties in the call path, which simplifies both the latency picture and the data "
   "protection review."),
 ],
 pros=[
  "Substantially cheapest at high outbound volume — 30-50% below rivals all-in",
  "Single all-in price rather than four bills to reconcile",
  "Co-located architecture removes network hops from the call path",
  "Purpose-built for outbound campaigns rather than retrofitted",
  "Fewer third parties in the data path simplifies compliance review",
 ],
 cons=[
  "Independent latency measurements are less flattering than the architecture claims",
  "Developer-first: no meaningful no-code path",
  "Less provider flexibility than Vapi by design",
  "High-volume outbound calling carries real regulatory exposure",
 ],
 pricing=[
  ("Pay as you go", "$0.09 / minute", "All-in: model, voice and telephony included"),
  ("Enterprise", "Custom", "Volume rates, dedicated capacity, support"),
 ],
 excels=[
  "High-volume outbound calling where per-minute cost dominates",
  "Teams that want one bill instead of four",
  "Engineering-led deployments integrating voice into a larger system",
  "Campaigns where concurrency matters more than configurability",
 ],
 not_ideal=[
  "Low-volume use where the price advantage is irrelevant",
  "Teams needing a no-code builder",
  "Latency-critical applications until you have tested with your own scripts",
 ],
 comparisons=[
  ("Bland AI vs Retell AI",
   "Retell is the better general platform with compliance coverage and a no-code builder; Bland is "
   "materially cheaper at volume. Below a few hundred calls a day the difference is noise. Above "
   "that, it becomes the deciding factor."),
  ("Bland AI vs Vapi",
   "Vapi lets you choose every provider and tune the pipeline; Bland runs its own stack and passes "
   "the savings on. Flexibility versus economics, and the right answer depends entirely on your "
   "call volume."),
 ],
 verdict="Bland AI is the correct choice when outbound volume makes per-minute cost the deciding "
         "factor, and it is a defensible architecture rather than a discount. Running the pipeline "
         "co-located removes network hops that a multi-vendor stack cannot avoid, and one all-in "
         "price beats reconciling four bills. Two cautions: independent latency measurements are "
         "less flattering than the architectural claims, so test with your own scripts before "
         "committing; and high-volume outbound calling carries regulatory exposure that has nothing "
         "to do with the technology and everything to do with how you use it.",
 faq=[
  ("How much does Bland AI cost?",
   "$0.09 per minute all-in, covering model, voice and telephony. That works out 30 to 50 per cent "
   "below competitors once their separate provider costs are included."),
  ("What latency does Bland achieve?",
   "The architecture targets 400 to 700 milliseconds end to end, though independent testing measured "
   "closer to 800 milliseconds on average. Test with your own scripts, because 800ms is where callers "
   "begin talking over the agent."),
  ("Is there a no-code builder?",
   "No meaningful one. Bland is developer-first, built around an API for engineers integrating voice "
   "into a larger system."),
  ("What does co-located inference mean?",
   "The model, speech processing and telephony run together rather than across separate third-party "
   "services, removing network hops that add both latency and cost."),
 ],
 breakdown=[("Cost at Volume", 9.7), ("Architecture", 8.8),
            ("Latency Consistency", 7.2), ("Ease of Adoption", 6.8), ("Flexibility", 7.0)],
 related=[("vapi", "Vapi", "4.6", "Developer Voice Platform"),
          ("retell-ai", "Retell AI", "4.5", "Production Voice Agents"),
          ("cartesia", "Cartesia", "4.5", "Real-Time Voice Models")],
),

dict(VO,
 slug="cartesia", name="Cartesia", company="Cartesia",
 domain="cartesia.ai", url="https://www.cartesia.ai/",
 cta2_url="https://play.cartesia.ai/", cta2_label="Try the Playground",
 flag="&#127482;&#127480;", country="USA", founded="2023", hq="San Francisco, California, USA",
 rating=4.5, date="2026-09-06",
 badges=["Real-Time Voice", "State Space Models", "Infrastructure Layer"],
 quick_stats=[("Real-time", "Streaming TTS"), ("SSM", "Architecture"),
              ("API", "Delivery"), ("Voice cloning", "Supported"), ("2023", "Founded")],
 title="Cartesia Review 2026: Real-Time Voice Models for Agent Stacks | TechVernia",
 meta_desc="Cartesia review 2026. The low-latency speech model provider behind many "
           "voice agent stacks, built on state space model research. What it does, "
           "where it sits in the pipeline and how it compares to ElevenLabs.",
 meta_keywords="Cartesia review, real-time text to speech, low latency TTS, voice AI "
               "infrastructure, Cartesia vs ElevenLabs, streaming speech synthesis",
 overview=[
  "Cartesia is a component rather than a product, and understanding that is the whole review. It "
  "supplies the speech layer inside voice agent stacks — the part that turns the model's text into "
  "audio — and it competes on the one axis that matters most in a live conversation: how quickly the "
  "first audio arrives and how steadily it streams after that.",
  "The technical foundation is state space model research, an architecture designed for efficient "
  "sequential processing, which is a better structural fit for streaming audio than approaches "
  "adapted from batch generation. The practical result is speech that begins almost immediately and "
  "continues smoothly, which is what stops a voice agent sounding like it is thinking between "
  "sentences.",
  "You will usually meet Cartesia as an option inside another platform rather than as something you "
  "adopt directly — it appears in the provider lists for Vapi and similar stacks. That positioning is "
  "deliberate and sensible: it is infrastructure that voice platforms build on, and the right way to "
  "evaluate it is to A/B it against alternatives inside whatever platform you are already using.",
 ],
 features=[
  ("zap", "Very Low Time-to-First-Audio",
   "Speech begins almost immediately rather than after a generation pause, which is what determines "
   "whether an agent sounds responsive."),
  ("cpu", "State Space Model Architecture",
   "Built on research designed for efficient sequential processing, a better structural fit for "
   "streaming audio than adapted batch models."),
  ("mic", "Voice Cloning",
   "Custom voices from reference audio, for products that need a consistent brand voice across "
   "every call."),
  ("activity", "Steady Streaming",
   "Consistent audio delivery without the mid-sentence stalls that make agents feel broken."),
  ("link", "API-First Delivery",
   "Designed to be integrated into a voice pipeline rather than used as a standalone application."),
  ("globe", "Multilingual Support",
   "Multiple languages from the same infrastructure, so a multi-market deployment does not need "
   "several providers."),
 ],
 pros=[
  "Among the fastest time-to-first-audio available, which is the metric that decides voice UX",
  "Architecture genuinely designed for streaming rather than adapted to it",
  "Available inside the major voice agent platforms as a drop-in option",
  "Voice cloning for consistent brand identity",
  "Competitive pricing against premium speech providers",
 ],
 cons=[
  "Not a complete product — you need a platform around it",
  "Voice expressiveness trails ElevenLabs on the most demanding content",
  "Smaller voice library than the established leaders",
  "Evaluating it properly requires A/B testing inside your own stack",
 ],
 pricing=[
  ("Free", "$0", "Evaluation credits for testing"),
  ("Pro", "Subscription", "Production character allowance with commercial rights"),
  ("Scale", "Usage-based", "Volume pricing for high-throughput deployments"),
  ("Enterprise", "Custom", "Dedicated capacity, SLAs, support"),
 ],
 excels=[
  "Live voice agents where latency determines whether the product works",
  "Teams already on Vapi or a similar platform choosing a speech provider",
  "Products needing a consistent cloned brand voice at volume",
  "Multilingual voice deployments from one provider",
 ],
 not_ideal=[
  "Narration and audiobook work where expressiveness beats latency",
  "Teams wanting a complete voice agent product rather than a component",
  "Use cases needing the largest possible stock voice library",
 ],
 comparisons=[
  ("Cartesia vs ElevenLabs",
   "ElevenLabs leads on voice quality, expressiveness and library size; Cartesia optimises for "
   "real-time latency. For narration, ElevenLabs. For a live agent where a caller is waiting, "
   "Cartesia's speed is frequently the better trade."),
  ("Cartesia vs using a platform default",
   "Most voice platforms ship a default speech provider that is adequate. Swapping in Cartesia is "
   "usually a configuration change, which makes A/B testing cheap — and the difference in perceived "
   "responsiveness is often larger than teams expect."),
 ],
 verdict="Cartesia is the speech layer to test when your voice agent feels slightly slow and you "
         "cannot work out why. Time-to-first-audio is the single most under-appreciated metric in "
         "voice UX — callers forgive an imperfect voice far more readily than a pause before it "
         "starts — and Cartesia's streaming-first architecture targets exactly that. It is a "
         "component, not a product, so evaluate it by swapping it into the platform you already use "
         "and listening to the difference. For narration work, ElevenLabs remains the better choice.",
 faq=[
  ("Is Cartesia a complete voice agent platform?",
   "No. It supplies the speech layer. You use it inside a platform such as Vapi, or in your own "
   "pipeline, rather than as a standalone product."),
  ("How does it compare to ElevenLabs?",
   "ElevenLabs leads on expressiveness and voice library size; Cartesia optimises for real-time "
   "latency. Live agents usually benefit more from speed, narration from expressiveness."),
  ("What are state space models?",
   "An architecture designed for efficient sequential processing, which suits streaming audio better "
   "than approaches adapted from batch generation — the technical basis for Cartesia's latency."),
  ("Can I clone a voice?",
   "Yes, from reference audio, which is how products maintain a consistent brand voice across large "
   "call volumes."),
 ],
 breakdown=[("Latency", 9.7), ("Streaming Consistency", 9.4),
            ("Voice Quality", 8.5), ("Library Breadth", 7.5), ("Integration Ease", 9.0)],
 related=[("vapi", "Vapi", "4.6", "Developer Voice Platform"),
          ("retell-ai", "Retell AI", "4.5", "Production Voice Agents"),
          ("elevenlabs", "ElevenLabs", "4.8", "AI Voice Generation")],
),

dict(SE,
 slug="profound", name="Profound", company="Profound",
 domain="tryprofound.com", url="https://www.tryprofound.com/",
 cta2_url="https://www.tryprofound.com/", cta2_label="Request a Demo",
 flag="&#127482;&#127480;", country="USA", founded="2023", hq="New York, New York, USA",
 rating=4.5, date="2026-09-06",
 badges=["Enterprise GEO", "$1B Valuation", "Citation Analytics"],
 quick_stats=[("$96M", "Series C"), ("$1B", "Valuation"),
              ("Feb 2026", "Latest Round"), ("Multi-engine", "Coverage"), ("2023", "Founded")],
 title="Profound Review 2026: Enterprise AI Search Visibility Analytics | TechVernia",
 meta_desc="Profound review 2026. The enterprise generative engine optimisation "
           "platform that raised $96M at a $1B valuation: brand citation tracking, "
           "source page analysis and competitor comparison across AI engines.",
 meta_keywords="Profound review, generative engine optimization, GEO tools, AI search "
               "visibility, brand citation tracking, AEO platform",
 overview=[
  "Search changed shape and most brands cannot see it happening. When a customer asks ChatGPT or "
  "Perplexity which product to buy, the answer either mentions you or it does not, and there is no "
  "Search Console telling you which. Profound built the measurement layer for that blind spot, and "
  "the market agreed emphatically: a $96 million Series C in February 2026 at a $1 billion "
  "valuation.",
  "The platform tracks how brands appear across AI engines — citation frequency, sentiment, share of "
  "voice against competitors — and, most usefully, which specific source pages the engines pull from "
  "when they answer. That last capability is what makes it actionable rather than merely "
  "informative. Knowing you are absent from AI answers is depressing; knowing that a competitor's "
  "comparison page is the source being cited tells you what to write.",
  "It is priced and built for enterprises, which is a fair reflection of who has the budget and the "
  "content operation to act on the findings. Smaller teams will find the analytical depth exceeds "
  "what they can realistically respond to, and lighter tools cover the basic question of whether you "
  "are being mentioned at all.",
 ],
 features=[
  ("search", "Multi-Engine Citation Tracking",
   "Monitors brand mentions and citations across the major AI answer engines rather than a single "
   "platform."),
  ("book", "Source Page Attribution",
   "Identifies which specific pages engines cite when answering, which converts measurement into a "
   "content plan."),
  ("users", "Competitive Share of Voice",
   "Compares your citation frequency against competitors on the prompts that matter commercially."),
  ("activity", "Sentiment Analysis",
   "Tracks not only whether you are mentioned but how — being cited as the expensive option is "
   "different from being cited as the leader."),
  ("layers", "Prompt-Level Reporting",
   "Visibility broken down by the actual questions buyers ask rather than by keyword volume."),
  ("check", "Crawler Activity Visibility",
   "Insight into AI crawler behaviour on your site, which is the upstream half of the problem."),
 ],
 pros=[
  "The most complete AI search visibility measurement available",
  "Source page attribution makes findings directly actionable",
  "Multi-engine coverage rather than one platform",
  "Strong funding and enterprise validation reduce vendor risk",
  "Sentiment tracking catches the mentions that hurt",
 ],
 cons=[
  "Enterprise pricing excludes small and mid-sized teams",
  "Requires a content operation capable of acting on the insight",
  "The category is young and best practice is still being established",
  "Measurement is not optimisation — the work still has to be done",
 ],
 pricing=[
  ("Enterprise", "Custom", "Priced on brand coverage, prompt volume and engine breadth"),
 ],
 excels=[
  "Enterprise brands where AI search visibility affects revenue",
  "Understanding which content AI engines actually cite",
  "Competitive intelligence on share of voice in AI answers",
  "Justifying content investment with measurable AI visibility data",
 ],
 not_ideal=[
  "Small businesses and independent publishers",
  "Teams without the capacity to produce content in response",
  "Anyone wanting a simple yes-or-no answer on brand mentions",
 ],
 comparisons=[
  ("Profound vs Goodie AI",
   "Profound is the enterprise measurement platform with the deepest analytics; Goodie bundles "
   "monitoring with optimisation tooling and content generation. Profound tells you more; Goodie "
   "helps you do more."),
  ("Profound vs traditional SEO tools",
   "Ahrefs and Semrush measure a search model that is losing share — Gartner's forecast of a 25 per "
   "cent decline in traditional search volume by 2026 has broadly materialised. They remain "
   "necessary; they are no longer sufficient."),
 ],
 verdict="Profound is the serious tool in the most important new SEO category, and the funding "
         "reflects genuine enterprise demand rather than hype. Source page attribution is the feature "
         "that matters: it turns AI visibility from an anxiety into a content brief. The honest "
         "caveats are that it measures rather than fixes, and that enterprise pricing puts it out of "
         "reach for the smaller publishers who are arguably losing the most traffic to AI answers. "
         "If you have the budget and a content team, this is where to start. If not, LLMrefs covers "
         "the basic question for a fraction of the cost.",
 faq=[
  ("What is generative engine optimisation?",
   "Structuring content and brand presence so AI systems like ChatGPT, Perplexity and Google's AI "
   "Overviews cite and recommend you in their answers — the discipline replacing a substantial share "
   "of traditional SEO."),
  ("How much did Profound raise?",
   "A $96 million Series C in February 2026 at a $1 billion valuation, making it the best-funded "
   "company in the GEO category."),
  ("Does Profound optimise my content?",
   "It measures and diagnoses — including which source pages engines cite — but the content work "
   "remains yours. That is why it suits organisations with an existing content operation."),
  ("Is there a version for small businesses?",
   "Not really. Profound is enterprise-priced. Smaller teams should look at LLMrefs or Goodie AI for "
   "the core visibility question."),
 ],
 breakdown=[("Measurement Depth", 9.6), ("Actionability", 9.0),
            ("Engine Coverage", 9.2), ("Accessibility", 5.0), ("Vendor Strength", 9.4)],
 related=[("goodie-ai", "Goodie AI", "4.2", "AEO Platform"),
          ("llmrefs", "LLMrefs", "4.1", "AI Search Tracking"),
          ("athenahq", "AthenaHQ", "4.3", "Automated GEO")],
),

dict(SE,
 slug="goodie-ai", name="Goodie AI", company="Goodie AI",
 domain="higoodie.com", url="https://higoodie.com/",
 cta2_url="https://higoodie.com/", cta2_label="Get Started",
 flag="&#127482;&#127480;", country="USA", founded="2024", hq="United States",
 rating=4.2, date="2026-09-06",
 badges=["Monitor + Optimise", "AEO Writer", "Topic Explorer"],
 quick_stats=[("Monitoring", "AI Visibility"), ("Optimisation Hub", "Schema + Semantics"),
              ("Topic Explorer", "Gap Analysis"), ("AEO Writer", "Content"),
              ("2024", "Founded")],
 title="Goodie AI Review 2026: Answer Engine Optimisation End to End | TechVernia",
 meta_desc="Goodie AI review 2026. An AEO platform that both measures AI search "
           "visibility and helps fix it: monitoring, schema and semantic optimisation, "
           "content gap analysis and an AEO content writer.",
 meta_keywords="Goodie AI review, answer engine optimization, AEO platform, AI search "
               "visibility, GEO tools, AI content optimization",
 overview=[
  "Goodie AI's positioning is straightforward and sensible: measuring your absence from AI answers is "
  "only half a product, so it bundles the doing with the measuring. The platform pairs AI visibility "
  "monitoring with an optimisation hub that suggests schema markup and semantic content changes, a "
  "topic explorer for finding gaps, and an AEO content writer for producing the material.",
  "That end-to-end shape is the right answer for teams without a large content operation. An "
  "enterprise with fifteen content people can take a diagnostic report and act on it; a marketing "
  "team of three needs the tool to close more of the loop. Goodie is built for the second case, and "
  "the topic explorer in particular is well aimed — identifying which questions in your category you "
  "have no content for is a more useful starting point than a citation count.",
  "The trade-off is depth. Profound's analytics go considerably further, particularly on source page "
  "attribution and competitive share of voice, and a platform spreading itself across monitoring, "
  "optimisation and generation will not match a specialist on any single axis. Content generated by "
  "an AEO writer also needs editing before publication — the AdSense and search quality risks of "
  "publishing unedited generated content are real and well documented.",
 ],
 features=[
  ("eye", "AI Visibility Monitoring",
   "Tracks brand presence across AI platforms so you can see whether you are being cited at all."),
  ("layers", "Optimisation Hub",
   "Suggests schema markup and semantic content changes that make pages easier for engines to parse "
   "and cite."),
  ("search", "Topic Explorer",
   "Finds the questions in your category you have no content for, which is a more actionable starting "
   "point than a raw visibility score."),
  ("book", "AEO Content Writer",
   "Generates content structured for answer engines — a starting draft rather than a publishable "
   "article."),
  ("activity", "Sentiment and Presence Tracking",
   "Monitors how your brand is characterised in AI answers, not only whether it appears."),
  ("check", "Schema and Entity Tagging",
   "Structured data improvements applied systematically rather than page by page."),
 ],
 pros=[
  "Closes the loop from measurement to content, unlike pure analytics tools",
  "Topic explorer surfaces genuinely actionable content gaps",
  "More accessible pricing than enterprise GEO platforms",
  "Schema and entity tagging improve machine readability at scale",
  "Suits small marketing teams without a content department",
 ],
 cons=[
  "Analytics depth trails Profound significantly",
  "Generated content requires real editing before publishing",
  "Younger vendor in a category still defining best practice",
  "Breadth across four functions costs depth in each",
 ],
 pricing=[
  ("Starter", "Subscription", "Visibility monitoring for a single brand"),
  ("Growth", "Subscription", "Optimisation hub, topic explorer, content generation"),
  ("Enterprise", "Custom", "Multi-brand coverage, integrations, support"),
 ],
 excels=[
  "Small marketing teams needing tooling that does more than diagnose",
  "Finding content gaps in your category systematically",
  "Improving structured data across a large content library",
  "Getting started with AEO without an enterprise budget",
 ],
 not_ideal=[
  "Enterprises needing the deepest competitive analytics",
  "Teams that will publish generated content without editing it",
  "Organisations with a strong content team who only need measurement",
 ],
 comparisons=[
  ("Goodie AI vs Profound",
   "Profound measures more deeply and costs considerably more; Goodie measures adequately and helps "
   "you act. If you have a content team, Profound's depth pays off. If you are the content team, "
   "Goodie's breadth is worth more."),
  ("Goodie AI vs AthenaHQ",
   "Both combine measurement with automated on-page optimisation and both target the same gap. "
   "AthenaHQ leans harder on automated schema and entity tagging across large libraries; Goodie puts "
   "more weight on content discovery and generation."),
 ],
 verdict="Goodie AI is the practical AEO platform for teams that have to do the work themselves. "
         "Bundling monitoring with optimisation and content generation is the right shape for a small "
         "marketing function, and the topic explorer is the component most likely to earn its keep — "
         "knowing which questions you have no answer for beats knowing your citation count. Treat the "
         "content writer as a drafting aid rather than a publishing pipeline; unedited generated "
         "content carries genuine search quality and monetisation risk. For deeper analytics with a "
         "real budget behind it, Profound is the stronger tool.",
 faq=[
  ("What is the difference between AEO and GEO?",
   "Answer engine optimisation focuses on becoming the source for direct answers — featured snippets, "
   "AI Overviews. Generative engine optimisation is broader, aiming to influence what an AI engine "
   "says about you overall. In practice the terms overlap heavily."),
  ("Can I publish the content it generates directly?",
   "You should not. Generated content needs editing for accuracy and quality before publication — "
   "unedited AI content carries real search quality and ad monetisation risk."),
  ("How does it compare to Profound?",
   "Profound has substantially deeper analytics and enterprise pricing to match; Goodie is more "
   "accessible and helps you act on findings rather than only reporting them."),
  ("What does the topic explorer do?",
   "Identifies questions being asked in your category that your content does not answer, which is "
   "usually the most actionable output the platform produces."),
 ],
 breakdown=[("Actionability", 9.0), ("Analytics Depth", 7.5),
            ("Content Tooling", 8.2), ("Accessibility", 8.8), ("Vendor Maturity", 6.8)],
 related=[("profound", "Profound", "4.5", "Enterprise GEO Analytics"),
          ("athenahq", "AthenaHQ", "4.3", "Automated GEO"),
          ("llmrefs", "LLMrefs", "4.1", "AI Search Tracking")],
),

dict(SE,
 slug="llmrefs", name="LLMrefs", company="LLMrefs",
 domain="llmrefs.com", url="https://llmrefs.com/",
 cta2_url="https://llmrefs.com/", cta2_label="Track Your Brand",
 flag="&#127482;&#127480;", country="USA", founded="2024", hq="United States",
 rating=4.1, date="2026-09-06",
 badges=["Affordable", "Rank Tracking", "Independent Friendly"],
 quick_stats=[("Rank tracking", "For AI Answers"), ("Multi-engine", "Coverage"),
              ("Self-serve", "Onboarding"), ("Accessible", "Pricing"), ("2024", "Founded")],
 title="LLMrefs Review 2026: Affordable AI Search Rank Tracking | TechVernia",
 meta_desc="LLMrefs review 2026. Generative AI search analytics for independents and "
           "small teams: track whether ChatGPT, Perplexity and Gemini mention your "
           "brand, without enterprise pricing. Scope, limits and verdict.",
 meta_keywords="LLMrefs review, AI search rank tracker, LLM SEO tool, GEO tracking, "
               "AI visibility for small business, affordable GEO tool",
 overview=[
  "LLMrefs does one thing and prices it so that people who are not enterprises can afford it. You "
  "tell it which prompts matter in your category, and it tells you whether the AI engines mention "
  "you, where you sit relative to competitors, and how that changes over time. It is rank tracking "
  "for the answer-engine era, and the mental model transfers directly from traditional SEO tools.",
  "That familiarity is a real advantage. GEO is new enough that plenty of platforms are still "
  "explaining their own concepts to buyers; LLMrefs skips that by mapping onto a workflow marketers "
  "already run. You add prompts the way you added keywords, you watch positions the way you watched "
  "rankings, and the reporting looks like reporting you already know how to read.",
  "It is deliberately narrower than Profound or Goodie. There is no source page attribution telling "
  "you exactly which content engines cite, and no content generation. For an independent publisher, "
  "a consultant or a small SaaS company, the honest question is whether the deeper analysis would "
  "change what you do — and frequently the answer is no, because the response to being absent from "
  "AI answers is to write better content either way.",
 ],
 features=[
  ("search", "Prompt-Level Rank Tracking",
   "Track specific prompts rather than keywords, which is the correct unit of measurement for answer "
   "engines."),
  ("activity", "Visibility Over Time",
   "Trend data showing whether your presence in AI answers is improving, which is what makes the "
   "measurement worth taking."),
  ("users", "Competitor Comparison",
   "See which competitors get cited on the prompts you care about, and how consistently."),
  ("globe", "Multi-Engine Coverage",
   "Tracks across the major AI answer engines rather than a single platform."),
  ("check", "Self-Serve Onboarding",
   "Sign up and start tracking without a sales call, which is not a given in this category."),
  ("book", "Straightforward Reporting",
   "Reports a marketer can read and share without a training session."),
 ],
 pros=[
  "Genuinely accessible pricing in a category dominated by enterprise deals",
  "Familiar rank-tracking mental model — no new concepts to learn",
  "Self-serve rather than sales-gated",
  "Covers the core question most small teams actually have",
  "Trend data over time rather than a one-off audit",
 ],
 cons=[
  "No source page attribution — you learn that you are absent, not why",
  "No optimisation or content tooling",
  "Smaller vendor with less certain longevity",
  "Shallow analysis compared with enterprise platforms",
 ],
 pricing=[
  ("Starter", "Subscription", "Prompt tracking for a single brand"),
  ("Pro", "Subscription", "More prompts, competitors and engines"),
  ("Agency", "Subscription", "Multiple client brands under one account"),
 ],
 excels=[
  "Independent publishers and small SaaS companies",
  "Consultants and agencies tracking client visibility affordably",
  "Answering whether AI engines mention you at all",
  "Measuring whether content changes moved the needle",
 ],
 not_ideal=[
  "Enterprises needing deep competitive and attribution analysis",
  "Teams that want the tool to help produce content",
  "Anyone needing source page attribution to direct their content work",
 ],
 comparisons=[
  ("LLMrefs vs Profound",
   "Profound is a far deeper platform at enterprise pricing; LLMrefs answers the basic visibility "
   "question at a price independents can pay. The gap in capability is real, and so is the gap in "
   "cost — pick based on whether you could act on the extra depth."),
  ("LLMrefs vs checking manually",
   "Plenty of people ask ChatGPT about their own brand occasionally and call it research. That is not "
   "measurement: answers vary by session, phrasing and time. Systematic tracking across prompts and "
   "engines is the difference between an anecdote and a trend."),
 ],
 verdict="LLMrefs is the sensible entry point into AI search visibility for anyone who is not an "
         "enterprise. It answers the question that actually matters first — are the engines "
         "mentioning us, and is that improving — using a mental model marketers already have, at a "
         "price that does not require a business case. It will not tell you which source pages "
         "engines cite, and it will not write anything for you. For an independent publisher or a "
         "small SaaS company, that is usually fine, because the response to poor AI visibility is "
         "better content regardless of how precisely the problem was diagnosed.",
 faq=[
  ("What does LLMrefs actually track?",
   "Whether AI answer engines mention your brand on the prompts you specify, how you compare with "
   "competitors, and how that changes over time."),
  ("Why track prompts instead of keywords?",
   "Answer engines respond to questions, not queries. The unit of measurement that matters is the "
   "prompt a real buyer would type, which is why rank tracking has to be rebuilt for this era."),
  ("Is it a replacement for Profound?",
   "No. Profound offers far deeper analytics including source page attribution, at enterprise "
   "pricing. LLMrefs covers the core visibility question affordably."),
  ("Can I just ask ChatGPT about my brand myself?",
   "You can, but answers vary by session, phrasing and time, so a single check tells you very little. "
   "Systematic tracking across prompts and engines is what turns that into usable data."),
 ],
 breakdown=[("Affordability", 9.5), ("Ease of Use", 9.0),
            ("Analysis Depth", 6.5), ("Engine Coverage", 8.0), ("Vendor Maturity", 6.5)],
 related=[("profound", "Profound", "4.5", "Enterprise GEO Analytics"),
          ("goodie-ai", "Goodie AI", "4.2", "AEO Platform"),
          ("mangools-ai-search-grader", "Mangools AI Search Grader", "4.0", "Free AI Visibility")],
),

]
