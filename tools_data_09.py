# -*- coding: utf-8 -*-
"""Lot 9 - Image, world models et productivite."""

IM = dict(category="image", cat_href="../../categories/ai-image.html",
          cat_label="AI Image Generation", app_category="MultimediaApplication")
SP = dict(category="specialized", cat_href="../../categories/ai-specialized.html",
          cat_label="Specialized AI Tools", app_category="MultimediaApplication")
PR = dict(category="productivity", cat_href="../../categories/ai-productivity.html",
          cat_label="AI Productivity", app_category="BusinessApplication")

TOOLS = [

dict(IM,
 slug="nano-banana", name="Nano Banana 2", company="Google DeepMind",
 domain="deepmind.google", url="https://gemini.google/overview/image-generation/",
 cta2_url="https://aistudio.google.com/", cta2_label="Try in AI Studio",
 flag="&#127482;&#127480;", country="USA", founded="2010", hq="London, UK / Mountain View, USA",
 rating=4.8, date="2026-09-06",
 badges=["Best in Class", "4K Output", "14 Reference Images"],
 quick_stats=[("26 Feb 2026", "Release Date"), ("0.5K to 4K", "Output Resolution"),
              ("14", "Reference Images"), ("Gemini 3.1 Flash Image", "Base Model"),
              ("2010", "DeepMind Founded")],
 title="Nano Banana 2 Review 2026: Google's Best Image Model | TechVernia",
 meta_desc="Nano Banana 2 review 2026. Google DeepMind's image model released 26 "
           "February 2026: up to 14 reference images, 4K output, live web grounding "
           "and the best text rendering available. Where to use it and its limits.",
 meta_keywords="Nano Banana 2 review, Google image AI, Gemini image generation, "
               "Nano Banana vs Seedream, AI image model 2026, 4K AI images",
 overview=[
  "Nano Banana 2 is Google DeepMind's image model, released on 26 February 2026 and built on Gemini "
  "3.1 Flash Image. It is worth being precise about the naming, because a great deal of confusion "
  "circulates: this is Google's model. Platforms like Krea integrate it, but they did not build it. "
  "On release day it became the default image model across the Gemini app, Google Search and "
  "Google's Flow video platform.",
  "The capability jump that matters most is reference handling. Up to fourteen reference images means "
  "you can hold a character, a product and a style consistent across an entire set of generations — "
  "which is the difference between a model that makes nice pictures and one you can actually run a "
  "campaign on. Output spans 0.5K to 4K, and the text rendering is the best available, finally making "
  "generated images with legible words a normal rather than lucky outcome.",
  "The genuinely novel feature is live web grounding: the model can search the web for current "
  "context while generating. That sounds like a gimmick until you need an image that reflects "
  "something that happened this week, or a product that changed appearance since the training "
  "cutoff. It is the sort of capability only a company that owns a search index could ship.",
 ],
 features=[
  ("image", "Fourteen Reference Images",
   "Hold characters, products and styles consistent across a whole set of generations, which is what "
   "makes commercial work possible rather than merely pretty."),
  ("layers", "0.5K to 4K Output",
   "Resolution from quick drafts to print-usable output from the same model, without switching tools "
   "for the final render."),
  ("book", "Best-in-Class Text Rendering",
   "Legible, correctly spelled text in generated images — the failure that made AI images unusable "
   "for most marketing work is largely solved."),
  ("search", "Live Web Grounding",
   "Searches the web for current context during generation, which no competitor can match at the "
   "same depth."),
  ("users", "Character Consistency",
   "The same person or product across many images, which is the requirement almost every commercial "
   "brief actually has."),
  ("zap", "Fast Generation",
   "Built on a Flash-class model, so iteration is quick enough to explore rather than commit to the "
   "first result."),
 ],
 pros=[
  "The strongest all-round image model available in 2026",
  "Fourteen reference images solves consistency properly",
  "Text rendering finally reliable enough for marketing use",
  "Live web grounding is genuinely unique",
  "4K output removes the need for a separate upscaling step",
 ],
 cons=[
  "Google ecosystem gravity — best experience is inside Google surfaces",
  "Higher tiers needed for volume work",
  "More literal than Seedream on abstract and artistic briefs",
  "Content policies are stricter than some competitors",
 ],
 pricing=[
  ("Gemini Free", "$0", "Limited generations in the Gemini app"),
  ("Google AI Pro", "$19.99 / month", "Higher generation limits and priority access"),
  ("Google AI Ultra", "$249.99 / month", "Highest limits and earliest feature access"),
  ("API", "Usage-based", "Per-image pricing through AI Studio and Vertex AI"),
 ],
 excels=[
  "Marketing images that need legible, correct text",
  "Campaigns requiring the same character or product across many images",
  "Anything needing current real-world context",
  "Print-resolution output without a separate upscaling pipeline",
 ],
 not_ideal=[
  "Abstract and artistic work where Seedream interprets more freely",
  "Teams that need permissive content policies",
  "Users committed to staying outside Google's ecosystem",
 ],
 comparisons=[
  ("Nano Banana 2 vs Seedream 5.0",
   "Nano Banana 2 prioritises speed, photorealistic accuracy and instruction following; Seedream 5 "
   "emphasises deeper reasoning and creative interpretation. For a brief with exact requirements, "
   "Nano Banana. For a brief that wants an interesting reading, Seedream."),
  ("Nano Banana 2 vs Midjourney",
   "Midjourney retains a distinctive aesthetic sensibility that many creatives still prefer. Nano "
   "Banana 2 wins decisively on instruction following, text rendering and consistency across a set. "
   "Art direction versus production reliability."),
 ],
 verdict="Nano Banana 2 is the image model to reach for first in 2026. Fourteen reference images and "
         "reliable text rendering address the two failures that kept AI images out of professional "
         "workflows, and live web grounding is a capability nobody else can copy easily. It is more "
         "literal than Seedream, which makes it better for briefs with requirements and worse for "
         "briefs that want interpretation. Know which of the two you are working on — that is the "
         "whole selection criterion, and the smart move in 2026 is keeping both available.",
 faq=[
  ("Who makes Nano Banana 2?",
   "Google DeepMind. It was released on 26 February 2026 and is built on Gemini 3.1 Flash Image. "
   "Platforms such as Krea integrate it, but they did not create it — a point frequently reported "
   "incorrectly."),
  ("How many reference images can it use?",
   "Up to fourteen, which is what makes consistent characters, products and styles across a whole "
   "set of generations practical."),
  ("What resolution can it output?",
   "From 0.5K up to 4K, so the same model covers quick drafts and print-usable finals."),
  ("What is live web grounding?",
   "The model can search the web for current context while generating, letting it reflect recent "
   "events or products that changed after the training cutoff."),
 ],
 breakdown=[("Instruction Following", 9.7), ("Text Rendering", 9.8),
            ("Consistency", 9.6), ("Artistic Interpretation", 8.0), ("Value", 8.5)],
 related=[("seedream-5", "Seedream 5.0", "4.6", "Creative Reasoning Model"),
          ("midjourney", "Midjourney", "4.7", "Artistic Image Generation"),
          ("flux", "Flux", "4.5", "Open-Weight Image Model")],
),

dict(IM,
 slug="seedream-5", name="Seedream 5.0", company="ByteDance",
 domain="bytedance.com", url="https://www.volcengine.com/",
 cta2_url="https://www.volcengine.com/", cta2_label="Access via Volcano Engine",
 flag="&#127464;&#127475;", country="China", founded="2012", hq="Beijing, China",
 rating=4.6, date="2026-09-06",
 badges=["Creative Reasoning", "ByteDance", "Artistic Depth"],
 quick_stats=[("Early 2026", "Release"), ("Seedream 4.5", "Predecessor"),
              ("Deep reasoning", "Design Emphasis"), ("ByteDance", "Developer"),
              ("2012", "ByteDance Founded")],
 title="Seedream 5.0 Review 2026: ByteDance's Creative Image Model | TechVernia",
 meta_desc="Seedream 5.0 review 2026. ByteDance's image model built for deep reasoning "
           "and creative interpretation rather than literal execution. Where it beats "
           "Nano Banana 2, and the access and governance questions to weigh.",
 meta_keywords="Seedream 5 review, ByteDance image AI, Seedream vs Nano Banana, "
               "creative AI image model, Chinese AI image generation",
 overview=[
  "Seedream 5.0 is ByteDance's image model, released in early 2026 as the successor to the well "
  "regarded Seedream 4.5, and it makes a deliberately different bet from Google's. Where Nano Banana "
  "2 optimises for speed and literal instruction following, Seedream emphasises deep reasoning and "
  "creative interpretation — it thinks about what the prompt is reaching for rather than executing "
  "the words as specified.",
  "In practice that produces a distinct working relationship. Give Seedream a vague, evocative brief "
  "and it frequently returns something better than you described; give it a precise specification "
  "and it may take liberties you did not want. For concept work, mood exploration and anything where "
  "you are trying to discover the image rather than reproduce one already in your head, that is "
  "exactly the right behaviour.",
  "The considerations that come with it are not primarily technical. Access runs through ByteDance's "
  "Volcano Engine platform, which is a less frictionless path for Western teams than an OpenAI or "
  "Google API. Some organisations have explicit policies about Chinese AI infrastructure, and "
  "regulatory attitudes toward ByteDance have been volatile. Those are procurement questions, and "
  "they will decide adoption for many teams regardless of how good the model is.",
 ],
 features=[
  ("brain", "Reasoning-Led Generation",
   "Interprets intent rather than executing wording literally, which produces stronger results from "
   "loose, evocative briefs."),
  ("image", "Artistic Flexibility",
   "Broad stylistic range with a genuine aesthetic sensibility rather than a single house style."),
  ("layers", "High-Resolution Output",
   "Production-grade resolution suitable for commercial work."),
  ("check", "Complex Scene Composition",
   "Handles multi-element scenes and unusual compositional requests that trip more literal models."),
  ("globe", "Strong Multilingual Prompting",
   "Handles prompts in multiple languages well, reflecting its origins and a genuinely global user "
   "base."),
  ("zap", "Rapid Iteration",
   "Fast enough to explore a direction across many variations rather than committing early."),
 ],
 pros=[
  "Best creative interpretation of any current image model",
  "Turns vague briefs into stronger results than they deserved",
  "Distinctive aesthetic range rather than one recognisable style",
  "Strong multilingual prompt handling",
  "Genuine competitive pressure on Google's dominance",
 ],
 cons=[
  "Interpretation cuts both ways — less reliable when you need exactness",
  "Access through Volcano Engine is less convenient for Western teams",
  "Organisational policies on Chinese AI infrastructure block many buyers",
  "Text rendering trails Nano Banana 2",
 ],
 pricing=[
  ("Volcano Engine API", "Usage-based", "Per-image pricing through ByteDance's cloud platform"),
  ("Third-party platforms", "Varies", "Available inside several Western creative tools"),
 ],
 excels=[
  "Concept art and mood exploration",
  "Briefs that are evocative rather than specified",
  "Complex scenes with multiple interacting elements",
  "Creative work where surprise is a feature rather than a defect",
 ],
 not_ideal=[
  "Work requiring exact adherence to a specification",
  "Images needing reliable rendered text",
  "Organisations with policies restricting Chinese AI platforms",
 ],
 comparisons=[
  ("Seedream 5.0 vs Nano Banana 2",
   "Nano Banana 2 executes precisely, renders text reliably and grounds in live web context; Seedream "
   "interprets more deeply and produces more interesting results from loose briefs. Precision versus "
   "interpretation — most creative teams benefit from having both."),
  ("Seedream 5.0 vs Seedance",
   "Different products from the same company and frequently confused. Seedream is the image model; "
   "Seedance is ByteDance's video generation model. The names are unhelpfully similar."),
 ],
 verdict="Seedream 5.0 is the image model for the part of the process where you do not yet know what "
         "you want. Its reasoning-led approach turns thin briefs into strong images more reliably "
         "than any competitor, which makes it excellent for concept and exploration work and less "
         "suitable when a client has specified exactly what they are expecting. The real barrier for "
         "most Western teams is not quality but access and procurement policy — Volcano Engine is a "
         "less comfortable path than a Google or OpenAI API, and some organisations will not take it "
         "at all.",
 faq=[
  ("Who makes Seedream 5.0?",
   "ByteDance, released in early 2026 as the successor to Seedream 4.5. Access is primarily through "
   "the Volcano Engine cloud platform."),
  ("Is Seedream the same as Seedance?",
   "No, and the names cause constant confusion. Seedream is ByteDance's image model; Seedance is its "
   "video generation model."),
  ("How does it compare to Nano Banana 2?",
   "Nano Banana 2 is faster, more literal, better at text rendering and grounded in live web search. "
   "Seedream reasons more deeply and interprets creative intent better. Different tools for different "
   "stages of work."),
  ("Are there concerns about using a ByteDance model?",
   "Many organisations have explicit policies on Chinese AI infrastructure, and regulatory attitudes "
   "toward ByteDance have been volatile. That is a procurement decision rather than a technical one, "
   "but it decides adoption for a lot of teams."),
 ],
 breakdown=[("Creative Interpretation", 9.6), ("Image Quality", 9.2),
            ("Instruction Precision", 7.8), ("Text Rendering", 7.5), ("Accessibility", 6.5)],
 related=[("nano-banana", "Nano Banana 2", "4.8", "Google Image Model"),
          ("midjourney", "Midjourney", "4.7", "Artistic Image Generation"),
          ("krea-ai", "Krea AI", "4.4", "Real-Time Creative Suite")],
),

dict(SP,
 slug="odyssey", name="Odyssey", company="Odyssey",
 domain="odyssey.ml", url="https://odyssey.ml/",
 cta2_url="https://odyssey.ml/", cta2_label="Try the Demo",
 flag="&#127482;&#127480;", country="USA", founded="2022", hq="United States",
 rating=4.2, date="2026-09-06",
 badges=["World Models", "Interactive", "Free Demos"],
 quick_stats=[("Odyssey-2", "Current Model"), ("Minutes-long", "Simulation Length"),
              ("Interactive", "Not Just Video"), ("Free demos", "Access"),
              ("2022", "Founded")],
 title="Odyssey Review 2026: Interactive World Models You Can Enter | TechVernia",
 meta_desc="Odyssey review 2026. An AI lab building general world models: Odyssey-2 "
           "turns a text or image prompt into a minutes-long interactive simulation "
           "you can move through. What works, what does not, and why it matters.",
 meta_keywords="Odyssey AI review, world models, interactive AI simulation, generative "
               "environments, Odyssey-2, AI world generation",
 overview=[
  "World models are the most interesting frontier in generative AI and the least understood, so it is "
  "worth being clear about what makes them different. A video model generates a clip you watch. A "
  "world model generates an environment you move through, deciding what you would see if you turned "
  "left — which requires maintaining a coherent internal representation of a space that was never "
  "actually built.",
  "Odyssey is a lab building general world models, and its current system, Odyssey-2, turns a text or "
  "image prompt into a minutes-long interactive simulation. The company makes free demos available, "
  "which is unusually confident in a field where most results arrive as curated videos. Trying it "
  "yourself is genuinely the only way to understand the category — the difference between watching a "
  "generated world and steering through one does not survive being described.",
  "It sits in a race that accelerated sharply through late 2025 and 2026: Google DeepMind's Genie 3 "
  "generating playable 3D worlds at 24 frames per second, World Labs shipping Marble as a commercial "
  "product. Odyssey is a smaller player among well-funded rivals, and none of these systems is "
  "production-ready for commercial work. What they are is a credible early look at how interactive "
  "environments get made in a few years.",
 ],
 features=[
  ("globe", "Interactive Generated Environments",
   "Move through a generated world rather than watching a clip — the model maintains a coherent space "
   "as your viewpoint changes."),
  ("clock", "Minutes-Long Coherence",
   "Simulations hold together over minutes rather than seconds, which is the hard part of the "
   "problem."),
  ("image", "Text or Image Prompting",
   "Start from a written description or a reference image, the same entry points creative teams "
   "already use."),
  ("zap", "Real-Time Response",
   "The environment responds to input as you explore rather than pre-rendering a path."),
  ("users", "Free Public Demos",
   "Try it directly rather than judging from a curated reel — genuinely rare in this field."),
  ("brain", "General World Model Research",
   "A research lab pursuing world models broadly rather than a single narrow product."),
 ],
 pros=[
  "Interactive rather than passive — a genuinely different category from video generation",
  "Free demos let you evaluate honestly instead of trusting a showreel",
  "Minutes-long coherence is real technical progress",
  "Text and image prompting fit existing creative workflows",
  "Early access to a category that will matter",
 ],
 cons=[
  "Not production-ready for commercial work",
  "Visual fidelity trails dedicated 3D pipelines substantially",
  "Smaller and less funded than DeepMind and World Labs",
  "Unclear commercial model compared with rivals shipping products",
 ],
 pricing=[
  ("Demo", "Free", "Public interactive demos"),
  ("Research and Commercial", "Contact vendor", "Access arrangements for professional use"),
 ],
 excels=[
  "Understanding what world models actually are, first-hand",
  "Early concept and previsualisation exploration",
  "Research into interactive generative environments",
  "Teams tracking where interactive media is heading",
 ],
 not_ideal=[
  "Production game or film environments today",
  "Work requiring precise control over a scene",
  "Teams needing a commercially supported product now",
 ],
 comparisons=[
  ("Odyssey vs Google DeepMind Genie 3",
   "Genie 3 generates playable 3D worlds at 24 frames per second and reached Google AI Ultra "
   "subscribers in January 2026, with DeepMind's resources behind it. Odyssey is smaller but openly "
   "accessible, which for evaluation purposes counts for a lot."),
  ("Odyssey vs World Labs Marble",
   "Marble is the commercial product in this space — it exports editable, downloadable 3D "
   "environments from prompts, photos or panoramas. Odyssey is more research-forward and more "
   "interactive. Marble for output you can use, Odyssey for exploring the frontier."),
 ],
 verdict="Odyssey is worth an afternoon rather than a budget line. World models are a genuinely "
         "different thing from video generation — an environment you steer through rather than a clip "
         "you watch — and the free demos make this the easiest way to understand that difference "
         "first-hand. It is not production-ready and it competes against DeepMind and a "
         "well-capitalised World Labs. Treat it as the clearest available window onto a category "
         "that will reshape games, film previsualisation and simulation within a few years, and "
         "revisit it in twelve months.",
 faq=[
  ("What is a world model?",
   "A system that generates an environment you can move through, maintaining a coherent internal "
   "representation of space — as opposed to a video model, which generates a fixed clip you watch."),
  ("Can I try Odyssey for free?",
   "Yes. Free public demos are available, which is unusual in a field where most results are shown as "
   "curated videos."),
  ("Is it ready for production use?",
   "No. Visual fidelity trails dedicated 3D pipelines and control is limited. It is an early look at "
   "a category rather than a tool for shipping work."),
  ("How does it compare to Genie 3 and Marble?",
   "Genie 3 has DeepMind's resources and generates playable worlds at 24fps; Marble from World Labs "
   "is the commercial product with exportable 3D output. Odyssey is smaller and more research-"
   "forward, but openly accessible."),
 ],
 breakdown=[("Interactivity", 9.0), ("Coherence Duration", 8.5),
            ("Visual Fidelity", 7.0), ("Accessibility", 9.2), ("Production Readiness", 4.5)],
 related=[("world-labs", "World Labs", "4.4", "Spatial Intelligence"),
          ("mcpcore", "MCPCore", "4.2", "Agent Infrastructure"),
          ("glide", "Glide", "4.3", "No-Code App Builder")],
),

dict(PR,
 slug="granola", name="Granola", company="Granola",
 domain="granola.ai", url="https://www.granola.ai/",
 cta2_url="https://www.granola.ai/", cta2_label="Download Granola",
 flag="&#127468;&#127463;", country="United Kingdom", founded="2023", hq="London, UK",
 rating=4.6, date="2026-09-06",
 badges=["No Bot Joins", "$14/user/mo", "Notes + AI"],
 quick_stats=[("$14/user/mo", "Entry Price"), ("No meeting bot", "Key Difference"),
              ("Your notes + AI", "Hybrid Model"), ("Desktop + mobile", "Platforms"),
              ("2023", "Founded")],
 title="Granola Review 2026: The AI Notepad Without a Meeting Bot | TechVernia",
 meta_desc="Granola review 2026. The AI notepad for back-to-back meetings that merges "
           "your own scrappy notes with AI-generated detail — and never adds a bot to "
           "the participant list. Pricing, privacy posture and verdict.",
 meta_keywords="Granola review, AI meeting notes, AI notepad, no bot meeting "
               "transcription, Granola vs Otter, meeting notes app",
 overview=[
  "Granola gets one social detail right that the rest of the category gets wrong: nobody wants a bot "
  "in their meeting. A named recording assistant appearing in the participant list changes the "
  "conversation, prompts a discussion about consent before the actual agenda, and in some client and "
  "legal contexts is simply not acceptable. Granola captures audio on your device instead, so the "
  "meeting looks exactly as it would have anyway.",
  "The second good idea is the hybrid note. You type your own scrappy notes during the call the way "
  "you always have — half sentences, an arrow, a name — and afterwards Granola merges them with what "
  "was actually said to produce something coherent. That is meaningfully better than a pure "
  "transcript summary, because your fragments encode what you thought mattered, and a summariser "
  "working from audio alone has no access to that judgement.",
  "It is priced from around $14 per user per month, at the lower end of the category, and aimed "
  "squarely at people whose calendars are wall-to-wall calls. The trade-off is scope: because it "
  "records on your device rather than joining as a participant, it does not cover meetings you are "
  "not in, and it will not produce the compliance-grade recording archive that some regulated "
  "environments require.",
 ],
 features=[
  ("mic", "No Bot in the Participant List",
   "Captures on your device rather than joining the call, so meetings stay socially normal and "
   "client-appropriate."),
  ("book", "Your Notes Merged with AI Detail",
   "Combines what you typed with what was said, so the output reflects your judgement about what "
   "mattered rather than a generic summary."),
  ("zap", "Built for Back-to-Back Days",
   "Designed for people whose calendars leave no gap between calls, which is who actually needs this "
   "category."),
  ("search", "Searchable Meeting History",
   "Find what was decided across past meetings rather than scrolling a transcript archive."),
  ("layers", "Template-Based Outputs",
   "Shape notes into consistent formats for recurring meeting types."),
  ("check", "Editable Output",
   "Notes are a working document you keep editing, not a locked artefact you file and never open."),
 ],
 pros=[
  "No bot means no awkward consent conversation and no client objections",
  "Hybrid notes are genuinely better than transcript-only summaries",
  "Among the most affordable in the category at around $14 per user per month",
  "Editable working notes rather than a filed artefact",
  "Fast and unobtrusive during the call itself",
 ],
 cons=[
  "Only covers meetings you personally attend",
  "No compliance-grade recording archive for regulated environments",
  "Device-side capture means audio quality depends on your setup",
  "Less useful if you do not take any notes yourself",
 ],
 pricing=[
  ("Free", "$0", "Limited monthly meetings"),
  ("Individual", "From $14 / user / month", "Unlimited meetings, templates, search"),
  ("Team", "Custom", "Shared workspace and administration"),
 ],
 excels=[
  "Consultants, founders and executives in back-to-back calls",
  "Client meetings where a recording bot would be inappropriate",
  "People who already take notes and want them made coherent",
  "Fast personal recall of what was decided and by whom",
 ],
 not_ideal=[
  "Compliance environments needing formal recording archives",
  "Capturing meetings you do not attend",
  "Users who take no notes at all — the hybrid advantage disappears",
 ],
 comparisons=[
  ("Granola vs Otter.ai",
   "Otter is the transcript-and-archive tool with a bot that joins and a fuller compliance story. "
   "Granola is the private working notepad. If you need the record, Otter. If you need to remember "
   "and act, Granola is far more pleasant to live with."),
  ("Granola vs Fireflies or Fathom",
   "Both join meetings as bots and target team-wide capture with CRM integration. Granola is "
   "deliberately personal and bot-free. Team process favours the bots; individual professionals in "
   "client-facing work favour Granola."),
 ],
 verdict="Granola wins on a social insight rather than a technical one: the bot in the participant "
         "list is a real cost, and removing it makes the tool usable in client and legal contexts "
         "where the alternatives are not. Merging your own notes with the transcript produces "
         "genuinely better output than summarisation alone, because your fragments carry judgement "
         "the audio does not. Understand the scope limits before adopting — only your meetings, no "
         "compliance archive — and if those fit, this is the most pleasant tool in a crowded "
         "category.",
 faq=[
  ("Does Granola join my meetings as a bot?",
   "No, and this is the point of the product. It captures on your device, so nothing appears in the "
   "participant list and the meeting proceeds as it would have anyway."),
  ("How much does Granola cost?",
   "From around $14 per user per month, with a free tier covering a limited number of meetings. That "
   "is at the lower end of the category."),
  ("Do I still need to take notes?",
   "You do not have to, but the product is better if you do. Granola merges your notes with the "
   "transcript, and your fragments tell it what you thought mattered."),
  ("Is it suitable for regulated environments?",
   "Generally not as a system of record. It does not provide the compliance-grade recording archive "
   "some regulated contexts require — it is a personal working notepad."),
 ],
 breakdown=[("Meeting Experience", 9.7), ("Note Quality", 9.2),
            ("Value", 9.3), ("Team Features", 7.0), ("Compliance Fit", 6.0)],
 related=[("limitless", "Limitless", "4.2", "Continuous Personal Memory"),
          ("otterai", "Otter.ai", "4.5", "Meeting Transcription"),
          ("fathom", "Fathom", "4.5", "AI Meeting Assistant")],
),

dict(PR,
 slug="limitless", name="Limitless", company="Limitless",
 domain="limitless.ai", url="https://www.limitless.ai/",
 cta2_url="https://www.limitless.ai/", cta2_label="Learn More",
 flag="&#127482;&#127480;", country="USA", founded="2020", hq="San Francisco, California, USA",
 rating=4.2, date="2026-09-06",
 badges=["Continuous Capture", "Wearable", "Personal AI"],
 quick_stats=[("Continuous", "Capture Model"), ("Pendant + app", "Form Factors"),
              ("Personal AI", "Query Interface"), ("Consent", "Critical Issue"),
              ("2020", "Founded")],
 title="Limitless Review 2026: Continuous Personal Memory and AI Recall | TechVernia",
 meta_desc="Limitless review 2026. Continuous capture of your conversations with a "
           "personal AI you can ask anything about them. What it enables, and the "
           "consent and privacy questions you must settle before using it.",
 meta_keywords="Limitless review, AI pendant, personal memory AI, continuous "
               "conversation capture, wearable AI, Limitless vs Granola",
 overview=[
  "Limitless takes the idea of AI note-taking to its logical conclusion: instead of capturing "
  "meetings, capture everything. Through a wearable pendant and companion apps, it records your "
  "conversations continuously and gives you a personal AI you can question about any of them. What "
  "did the client say about the timeline in March. Who suggested that approach. What did I promise "
  "and to whom.",
  "When it works, the capability is genuinely striking. Human memory of conversations is far worse "
  "than we believe, and having a searchable record of what was actually said — rather than what you "
  "remember being said — changes how you work. For people whose job is largely conversations, that "
  "is a real advantage rather than a novelty.",
  "It also raises the sharpest consent problem in consumer AI, and it should not be glossed over. "
  "The people you talk to have not agreed to be recorded and stored in a searchable archive. In "
  "many jurisdictions, recording a conversation without all-party consent is illegal, not merely "
  "impolite. Anyone considering this needs to settle two questions before switching it on: what the "
  "law says where they are, and how they will tell people. Both answers are more demanding than the "
  "product's marketing suggests.",
 ],
 features=[
  ("mic", "Continuous Conversation Capture",
   "Records throughout the day via a wearable rather than per-meeting, so nothing depends on "
   "remembering to start a recording."),
  ("brain", "Query Your Own Past",
   "Ask the personal AI what was said, decided or promised across everything it has captured."),
  ("search", "Searchable Conversation Archive",
   "Find a specific exchange from weeks ago in seconds — the capability human memory simply does not "
   "have."),
  ("clock", "Timeline Recall",
   "Reconstruct when things were discussed and how a position evolved over time."),
  ("layers", "Automatic Summarisation",
   "Daily and per-conversation summaries so the archive stays usable rather than becoming a "
   "haystack."),
  ("lock", "Privacy Controls",
   "Controls over what is captured and retained, which the product's premise makes essential rather "
   "than optional."),
 ],
 pros=[
  "Genuinely novel capability — searchable memory of your own conversations",
  "Captures everything, so nothing depends on remembering to record",
  "Timeline recall reconstructs how decisions actually evolved",
  "Strong for roles that are mostly conversations",
  "Summarisation keeps the archive navigable",
 ],
 cons=[
  "Serious consent problem — the people you record did not agree",
  "All-party consent laws make it illegal in many jurisdictions without permission",
  "A continuous archive of your conversations is a significant breach risk",
  "Hardware dependency and battery management add friction",
 ],
 pricing=[
  ("Hardware", "One-off purchase", "Pendant device"),
  ("Subscription", "Monthly", "AI features, storage and retention"),
 ],
 excels=[
  "Roles where the work is overwhelmingly conversational",
  "Recalling commitments and decisions made verbally",
  "People with memory difficulties or accessibility needs",
  "Reconstructing how a decision evolved over weeks",
 ],
 not_ideal=[
  "Jurisdictions requiring all-party consent to record",
  "Client-confidential, legal or medical conversations",
  "Anyone unwilling to tell every person they speak to",
 ],
 comparisons=[
  ("Limitless vs Granola",
   "Granola captures meetings you are in, with no bot and a clear scope. Limitless captures "
   "everything, which is more powerful and vastly more fraught. Most professionals should start with "
   "Granola and only consider Limitless with a clear legal and social answer in hand."),
  ("Limitless vs taking notes",
   "Notes capture what you judged important; Limitless captures everything including what you did not "
   "notice. That is the advantage and the problem — an exhaustive archive is more useful and more "
   "dangerous than a selective one."),
 ],
 verdict="Limitless is the most technically interesting and ethically demanding product in this "
         "list. Searchable memory of your own conversations is a real capability that human recall "
         "cannot approach, and for conversation-heavy roles it changes what is possible. But the "
         "premise requires recording people who did not ask to be recorded, and in many "
         "jurisdictions all-party consent is a legal requirement rather than a courtesy. Settle the "
         "legal position where you live and decide how you will tell people, before you buy the "
         "device — not after.",
 faq=[
  ("Is it legal to use Limitless?",
   "It depends entirely on your jurisdiction. Many places require all-party consent to record a "
   "conversation, making covert use illegal rather than merely rude. Check your local law before "
   "purchase, not after."),
  ("Do I have to tell people I am recording?",
   "Ethically yes, and in many jurisdictions legally yes. Anyone considering this product needs a "
   "plan for how they will tell people, because that conversation happens repeatedly."),
  ("How is it different from Granola?",
   "Granola captures meetings you attend, with no bot and a clearly bounded scope. Limitless captures "
   "everything continuously via a wearable — far more powerful and far more sensitive."),
  ("What are the security implications?",
   "A continuous archive of your conversations is among the most sensitive datasets you could create. "
   "Evaluate the vendor's security posture, retention policy and breach history seriously before "
   "committing to it."),
 ],
 breakdown=[("Recall Capability", 9.4), ("Novelty", 9.5),
            ("Privacy Posture", 5.5), ("Legal Risk", 4.0), ("Daily Practicality", 7.0)],
 related=[("granola", "Granola", "4.6", "AI Meeting Notepad"),
          ("mem-ai", "Mem AI", "4.3", "Self-Organising Notes"),
          ("otterai", "Otter.ai", "4.5", "Meeting Transcription")],
),

]
