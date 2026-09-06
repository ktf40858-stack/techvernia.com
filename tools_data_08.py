# -*- coding: utf-8 -*-
"""Lot 8 - Agents d'entreprise (business/) et verticales finance / sante."""

BU = dict(category="business", cat_href="../../categories/ai-business.html",
          cat_label="AI Business Tools", app_category="BusinessApplication")
ME = dict(category="medical", cat_href="../../categories/ai-medical.html",
          cat_label="AI Medical Tools", app_category="HealthApplication")

TOOLS = [

dict(BU,
 slug="dust", name="Dust", company="Dust",
 domain="dust.tt", url="https://dust.tt/",
 cta2_url="https://dust.tt/", cta2_label="Start Free Trial",
 flag="&#127467;&#127479;", country="France", founded="2023", hq="Paris, France",
 rating=4.4, date="2026-09-06",
 badges=["$40M Series B", "Sequoia Backed", "European"],
 quick_stats=[("$40M", "Series B"), ("Sequoia", "Lead Investor"),
              ("May 2026", "Latest Round"), ("Company knowledge", "Grounding"),
              ("2023", "Founded")],
 title="Dust Review 2026: Custom AI Agents Grounded in Company Knowledge | TechVernia",
 meta_desc="Dust review 2026. The European platform for building custom AI agents "
           "grounded in your company's own knowledge, backed by a $40M Sequoia-led "
           "Series B. Architecture, data residency and honest limits.",
 meta_keywords="Dust AI review, custom AI agents, enterprise knowledge agents, "
               "Dust.tt, European AI platform, internal AI assistant",
 overview=[
  "Dust builds the layer between a company's scattered internal knowledge and the people who need it. "
  "Agents are grounded in your own sources — Notion, Slack, Google Drive, GitHub, Confluence and the "
  "rest — so an answer about the refund policy comes from your refund policy rather than from a "
  "model's general impression of how refund policies usually work. Sequoia led a $40 million Series B "
  "in May 2026, which is a meaningful vote for a European company in a market dominated by American "
  "incumbents.",
  "The product's better idea is that agents should be specific. Rather than one company assistant "
  "that vaguely knows everything, teams build purpose-built agents — one that answers support "
  "questions from the help centre and past tickets, one that helps sales find the right case study, "
  "one that onboards engineers into a codebase. Narrow agents with clear sources are dramatically "
  "more reliable than broad ones, and Dust's structure pushes teams toward that.",
  "Being European is not incidental. For organisations in the EU where data residency and GDPR are "
  "board-level concerns rather than checkboxes, a Paris-headquartered vendor is a materially easier "
  "conversation than an American one. That, plus a genuine focus on making agent building accessible "
  "to non-engineers, is the position it occupies against Glean and the Microsoft ecosystem.",
 ],
 features=[
  ("layers", "Purpose-Built Agents",
   "Teams create narrow agents for specific jobs with specific sources, which is far more reliable "
   "than one assistant expected to know everything."),
  ("link", "Broad Knowledge Connectors",
   "Notion, Slack, Google Drive, GitHub, Confluence and more, so agents answer from your actual "
   "documentation rather than from model priors."),
  ("users", "Accessible to Non-Engineers",
   "Agent building does not require a developer, which is what determines whether adoption spreads "
   "beyond the team that bought it."),
  ("lock", "European Data Residency",
   "A Paris-headquartered vendor, which is a substantially simpler GDPR and data residency "
   "conversation for EU organisations."),
  ("brain", "Model-Agnostic",
   "Works across frontier model providers rather than locking you to one vendor's roadmap."),
  ("check", "Source Citation",
   "Answers cite the internal documents they came from, so people can verify rather than trust."),
 ],
 pros=[
  "Grounding in company knowledge makes answers verifiable",
  "Narrow purpose-built agents are more reliable than one broad assistant",
  "European base simplifies GDPR and data residency questions",
  "Non-engineers can build agents, which drives real adoption",
  "Sequoia-backed with $40M raised — reasonable continuity confidence",
 ],
 cons=[
  "Answer quality is capped by how good your internal documentation is",
  "Smaller than Glean and the Microsoft ecosystem it competes with",
  "Connector coverage is good but not exhaustive",
  "Requires someone to own agent curation or agents go stale",
 ],
 pricing=[
  ("Free Trial", "$0", "Evaluation period with core features"),
  ("Pro", "From ~$29 / user / month", "Agent building, connectors, team workspace"),
  ("Enterprise", "Custom", "SSO, advanced security, data residency, support"),
 ],
 excels=[
  "European organisations with data residency requirements",
  "Companies whose knowledge is scattered across many tools",
  "Teams wanting business users to build their own agents",
  "Onboarding, internal support and knowledge retrieval use cases",
 ],
 not_ideal=[
  "Organisations with poor or non-existent internal documentation",
  "Companies fully standardised on Microsoft who will use Copilot anyway",
  "Teams unwilling to maintain agents after launch",
 ],
 comparisons=[
  ("Dust vs Glean",
   "Glean is the enterprise search incumbent with over $100 million ARR and deeper large-enterprise "
   "features; Dust is more agent-centric, easier for business users to build in, and European. Data "
   "residency and team size usually decide it."),
  ("Dust vs Microsoft Copilot",
   "If your company runs entirely on Microsoft 365, Copilot's integration is hard to argue with. Dust "
   "wins on multi-tool environments, agent specificity and EU data residency."),
 ],
 verdict="Dust is the strongest European answer in the enterprise agent category, and the "
         "Sequoia-led round says the market agrees. The design instinct — many narrow agents with "
         "clear sources rather than one omniscient assistant — is correct, and it is the single "
         "biggest predictor of whether internal AI actually gets used past month two. Two honest "
         "caveats: the agents are only as good as the documentation behind them, so this rewards "
         "companies that already write things down, and someone has to own keeping agents current. "
         "For EU organisations with data residency constraints, it should be on the shortlist.",
 faq=[
  ("Where is Dust's data hosted?",
   "Dust is headquartered in Paris and offers European data residency, which is a materially simpler "
   "GDPR conversation than with US-based competitors."),
  ("Do I need developers to build agents?",
   "No. Agent creation is designed for business users, which is what determines whether adoption "
   "spreads beyond the original buying team."),
  ("What sources can agents use?",
   "Notion, Slack, Google Drive, GitHub, Confluence and other common workplace tools, so agents "
   "answer from your documentation rather than general model knowledge."),
  ("How does it compare to Glean?",
   "Glean is larger with deeper enterprise search features; Dust is more agent-focused, easier for "
   "non-engineers, and European. Data residency requirements often decide it."),
 ],
 breakdown=[("Knowledge Grounding", 9.0), ("Ease of Agent Building", 9.2),
            ("Data Residency", 9.5), ("Connector Coverage", 8.2), ("Enterprise Depth", 7.5)],
 related=[("glean", "Glean", "4.6", "Enterprise AI Search"),
          ("agentforce", "Agentforce", "4.3", "Salesforce Agent Platform"),
          ("moveworks", "Moveworks", "4.4", "Internal IT Support AI")],
),

dict(BU,
 slug="agentforce", name="Salesforce Agentforce", company="Salesforce",
 domain="salesforce.com", url="https://www.salesforce.com/agentforce/",
 cta2_url="https://www.salesforce.com/agentforce/", cta2_label="Explore Agentforce",
 flag="&#127482;&#127480;", country="USA", founded="1999", hq="San Francisco, California, USA",
 rating=4.3, date="2026-09-06",
 badges=["CRM Native", "Enterprise Scale", "Data Cloud"],
 quick_stats=[("Salesforce", "Platform"), ("Data Cloud", "Grounding"),
              ("Per-conversation", "Pricing Model"), ("Enterprise", "Scale"),
              ("1999", "Salesforce Founded")],
 title="Salesforce Agentforce Review 2026: Agents Inside the CRM | TechVernia",
 meta_desc="Salesforce Agentforce review 2026. Autonomous agents built on Salesforce "
           "data and Data Cloud grounding, acting inside the CRM your business already "
           "runs on. Pricing model, real limits and who it actually suits.",
 meta_keywords="Agentforce review, Salesforce AI agents, CRM AI automation, Data Cloud "
               "grounding, Einstein successor, enterprise AI agents",
 overview=[
  "Agentforce is Salesforce's agent platform, and its advantage is unglamorous but decisive: the "
  "agents live where the data and the processes already are. An agent that can read the account "
  "record, check the entitlement, update the case and trigger the workflow does not need "
  "integrations to be useful — it needs permissions. For organisations that run their business on "
  "Salesforce, that removes most of what makes enterprise agent projects fail.",
  "Grounding comes through Data Cloud, which unifies customer data across systems, so an agent "
  "answers from the actual customer record rather than a stale copy. The agents can be deployed "
  "across service, sales and internal operations, and because they act within the Salesforce "
  "permission model, the governance question that stops most agent deployments — what is this thing "
  "allowed to do — has an existing answer.",
  "The two honest problems are cost and prerequisites. Agentforce is priced per conversation, which "
  "makes forecasting hard and gets expensive at consumer support volumes; several large customers "
  "have said so publicly. And the value depends entirely on your Salesforce data being clean and "
  "your processes being properly modelled. An agent built on messy CRM data will confidently do the "
  "wrong thing at scale.",
 ],
 features=[
  ("database", "Data Cloud Grounding",
   "Agents answer from unified customer data rather than a stale extract, which is the difference "
   "between a useful agent and a plausible one."),
  ("layers", "Native CRM Actions",
   "Agents update records, trigger workflows and act inside the system of record — no integration "
   "layer required."),
  ("lock", "Inherited Permission Model",
   "Agents operate within existing Salesforce permissions, so the governance question has an answer "
   "before you start."),
  ("users", "Service, Sales and Internal Agents",
   "One platform across customer-facing and internal use cases rather than separate tools per "
   "function."),
  ("check", "Guardrails and Topic Scoping",
   "Explicit boundaries on what agents may discuss and do, which is what makes customer-facing "
   "deployment defensible."),
  ("activity", "Testing and Observability",
   "Tooling to test agent behaviour before release and monitor it afterwards."),
 ],
 pros=[
  "Agents act inside the system of record with no integration project",
  "Data Cloud grounding makes answers current rather than approximate",
  "Existing permission model solves agent governance",
  "Enterprise-grade testing, guardrails and observability",
  "Backed by a vendor that will still exist in five years",
 ],
 cons=[
  "Per-conversation pricing is hard to forecast and expensive at volume",
  "Value depends entirely on Salesforce data quality and process modelling",
  "Only makes sense if you are already committed to Salesforce",
  "Implementation typically needs partner help, adding real cost",
 ],
 pricing=[
  ("Agentforce", "Per conversation", "Consumption-based, priced per agent conversation"),
  ("Enterprise Bundles", "Custom", "Bundled with Salesforce licensing and Data Cloud"),
 ],
 excels=[
  "Organisations already running their business on Salesforce",
  "Customer service automation with access to the real customer record",
  "Internal process agents acting on CRM data",
  "Enterprises needing governance and auditability from day one",
 ],
 not_ideal=[
  "Companies not standardised on Salesforce",
  "High-volume consumer support where per-conversation pricing hurts",
  "Organisations with poor CRM data hygiene",
 ],
 comparisons=[
  ("Agentforce vs Salesforce Einstein",
   "Einstein was predictive intelligence layered onto the CRM — scoring, forecasting, suggestions. "
   "Agentforce is autonomous action. If your reference point is Einstein, this is a different "
   "category of product rather than a version increment."),
  ("Agentforce vs Sierra or Decagon",
   "The specialists frequently deliver better customer service conversations; Agentforce delivers "
   "deeper native access to Salesforce data and actions. Conversation quality versus system "
   "integration, and the right answer depends on which is your bottleneck."),
 ],
 verdict="Agentforce is the obvious choice for Salesforce-committed enterprises and irrelevant to "
         "everyone else, which is a cleaner recommendation than most products in this category "
         "manage. Native access to the system of record removes the integration work that kills "
         "agent projects, and inheriting the permission model answers the governance question before "
         "it is asked. Go in with two things settled: a realistic model of per-conversation costs at "
         "your actual volume, and an honest assessment of your CRM data quality — because an agent "
         "grounded in bad data does the wrong thing faster than a human would.",
 faq=[
  ("How is Agentforce priced?",
   "Per conversation, on a consumption basis. That is difficult to forecast and becomes expensive at "
   "high support volumes, which several large customers have said publicly. Model it against your "
   "real volume before committing."),
  ("Is Agentforce the same as Einstein?",
   "No. Einstein was predictive intelligence — scoring and suggestions. Agentforce is autonomous "
   "action inside the CRM. Different category, not a version upgrade."),
  ("Do I need Data Cloud?",
   "Data Cloud grounding is what makes agents answer from current unified customer data. Without it "
   "you lose most of the platform's advantage over a generic agent."),
  ("Can Agentforce work if we do not use Salesforce?",
   "Not meaningfully. The entire value proposition is native access to Salesforce data and actions."),
 ],
 breakdown=[("CRM Integration", 9.8), ("Governance", 9.3),
            ("Conversation Quality", 8.0), ("Cost Predictability", 5.5), ("Flexibility", 6.5)],
 related=[("salesforce-einstein", "Salesforce Einstein", "4.4", "Predictive CRM AI"),
          ("moveworks", "Moveworks", "4.4", "Internal IT Support AI"),
          ("dust", "Dust", "4.4", "Company Knowledge Agents")],
),

dict(BU,
 slug="moveworks", name="Moveworks", company="Moveworks (ServiceNow)",
 domain="moveworks.com", url="https://www.moveworks.com/",
 cta2_url="https://www.moveworks.com/", cta2_label="Request a Demo",
 flag="&#127482;&#127480;", country="USA", founded="2016", hq="Mountain View, California, USA",
 rating=4.4, date="2026-09-06",
 badges=["Employee Support", "ServiceNow Owned", "Ticket Deflection"],
 quick_stats=[("Employee support", "Category"), ("ServiceNow", "Parent Company"),
              ("Ticket deflection", "Core Metric"), ("Enterprise", "Scale"),
              ("2016", "Founded")],
 title="Moveworks Review 2026: AI for Internal Employee Support | TechVernia",
 meta_desc="Moveworks review 2026. The AI assistant that resolves employee IT and HR "
           "requests before they become tickets, now part of ServiceNow. Deflection "
           "economics, integration requirements and honest limits.",
 meta_keywords="Moveworks review, employee support AI, IT ticket deflection, internal "
               "helpdesk AI, ServiceNow Moveworks, HR service automation",
 overview=[
  "Moveworks automates the internal support requests that consume enormous amounts of organisational "
  "time and create no value whatsoever: password resets, software access, VPN problems, where-do-I-"
  "find-the-policy questions. An employee asks in Slack or Teams and the assistant resolves it, "
  "usually by actually doing the thing rather than by linking to an article about how to do it.",
  "The distinction between answering and resolving is the entire product. A chatbot that returns the "
  "knowledge base article on requesting software access has saved nobody any time. Moveworks "
  "integrates with identity, ITSM and HR systems so it can provision the access, reset the "
  "credential, or file and route the request — which is why deflection rates are meaningful rather "
  "than cosmetic.",
  "ServiceNow acquired Moveworks, which is the strategic context to hold in mind. It resolves the "
  "long-term viability question and deepens the ITSM integration story; it also means the product's "
  "roadmap now serves ServiceNow's platform strategy. For organisations already on ServiceNow that "
  "is an advantage. For those on other ITSM platforms, it is worth asking pointed questions about "
  "long-term support.",
 ],
 features=[
  ("check", "Resolution, Not Deflection Theatre",
   "Provisions access, resets credentials and files requests rather than returning a knowledge base "
   "article — which is the difference between real and cosmetic deflection."),
  ("link", "Deep System Integration",
   "Connects to identity, ITSM, HR and collaboration platforms, which is what allows it to act rather "
   "than only advise."),
  ("users", "Slack and Teams Native",
   "Employees ask where they already are, removing the portal nobody visits from the process."),
  ("layers", "IT and HR Coverage",
   "Handles both technology and people-operations requests from one assistant."),
  ("book", "Knowledge Gap Reporting",
   "Surfaces what employees ask that documentation does not answer, which is quietly one of its more "
   "valuable outputs."),
  ("activity", "Deflection Analytics",
   "Measures what was resolved without human involvement, so the business case can be verified "
   "rather than assumed."),
 ],
 pros=[
  "Resolves requests rather than routing them, so deflection is real",
  "Meets employees in Slack and Teams instead of a portal",
  "Covers IT and HR from a single assistant",
  "ServiceNow ownership removes vendor continuity risk",
  "Knowledge gap reporting improves documentation as a side effect",
 ],
 cons=[
  "Integration depth means a substantial implementation project",
  "Enterprise pricing that only makes sense above a certain headcount",
  "Roadmap now serves ServiceNow's platform strategy",
  "Value depends on having documented, well-defined internal processes",
 ],
 pricing=[
  ("Enterprise", "Custom", "Priced on employee count and integration scope"),
 ],
 excels=[
  "Large organisations with high internal ticket volumes",
  "IT and HR teams buried in repetitive access and reset requests",
  "Companies already invested in ServiceNow",
  "Improving employee experience for routine internal requests",
 ],
 not_ideal=[
  "Organisations under a few thousand employees",
  "Companies with undocumented or ad-hoc internal processes",
  "Teams on ITSM platforms outside the ServiceNow ecosystem",
 ],
 comparisons=[
  ("Moveworks vs a knowledge base chatbot",
   "A chatbot answers questions; Moveworks completes tasks. Employees do not want to be told how to "
   "request access, they want the access. That distinction is the entire value gap between the two "
   "categories."),
  ("Moveworks vs Agentforce",
   "Moveworks is purpose-built for employee support with deep identity and ITSM integration; "
   "Agentforce is a general agent platform strongest where Salesforce data is central. Internal "
   "support favours Moveworks."),
 ],
 verdict="Moveworks is the mature answer to internal support automation, and it earns that by "
         "resolving requests rather than deflecting them into a knowledge base. The integration work "
         "is genuinely substantial — this is a project, not a subscription — and the economics only "
         "work above a certain headcount, but for large organisations the repetitive request volume "
         "is large enough that the maths is usually straightforward. The ServiceNow acquisition "
         "settles the continuity question and tilts the roadmap; factor that in if your ITSM stack "
         "sits elsewhere.",
 faq=[
  ("Who owns Moveworks?",
   "ServiceNow acquired the company. That removes vendor continuity risk and deepens ITSM "
   "integration, while tying the roadmap to ServiceNow's platform strategy."),
  ("How is it different from an internal chatbot?",
   "It completes the task — provisioning access, resetting credentials, filing and routing requests — "
   "rather than returning an article explaining how. That is why its deflection numbers mean "
   "something."),
  ("How long does implementation take?",
   "It is a project rather than a subscription. Integration with identity, ITSM and HR systems is "
   "what makes it work, and that depth takes time to configure properly."),
  ("What size company does it suit?",
   "Large ones. Below a few thousand employees the internal ticket volume rarely justifies the "
   "implementation effort and enterprise pricing."),
 ],
 breakdown=[("Resolution Rate", 9.2), ("Integration Depth", 9.4),
            ("Employee Experience", 9.0), ("Implementation Effort", 6.0), ("Accessibility", 5.8)],
 related=[("agentforce", "Agentforce", "4.3", "Salesforce Agent Platform"),
          ("dust", "Dust", "4.4", "Company Knowledge Agents"),
          ("glean", "Glean", "4.6", "Enterprise AI Search")],
),

dict(BU,
 slug="rogo", name="Rogo", company="Rogo",
 domain="rogo.com", url="https://rogo.com/",
 cta2_url="https://rogo.com/", cta2_label="Request a Demo",
 flag="&#127482;&#127480;", country="USA", founded="2021", hq="New York, New York, USA",
 rating=4.5, date="2026-09-06",
 badges=["$2B Valuation", "35,000+ Users", "Investment Banking"],
 quick_stats=[("$2B", "Valuation"), ("35,000+", "Finance Professionals"),
              ("250+", "Firms"), ("Excel/PPT/Word", "Native Output"), ("2021", "Founded")],
 title="Rogo Review 2026: The AI Analyst Built for Investment Banking | TechVernia",
 meta_desc="Rogo review 2026. The $2B-valuation AI analyst used by 35,000+ finance "
           "professionals at 250+ firms, producing Excel models, PowerPoint decks and "
           "Word memos in firm templates. What it does well and where humans stay.",
 meta_keywords="Rogo AI review, investment banking AI, AI financial analyst, finance "
               "automation, Rogo vs Hebbia, private equity AI tools",
 overview=[
  "Rogo understood something most vertical AI products miss: in investment banking, the format is "
  "the deliverable. An answer in a chat window is worthless to an associate who needs a model in the "
  "firm's Excel template, a deck in the firm's PowerPoint style, and a memo in the firm's Word "
  "format. Rogo produces those directly, which is why it reached 35,000 finance professionals across "
  "more than 250 firms and a $2 billion valuation.",
  "The workflows are calibrated to investment banking conventions rather than generalised. Comparable "
  "company analysis, precedent transactions, market research, document review across a data room — "
  "the actual task list of a deal team, executed the way that team expects. An April 2026 partnership "
  "with Daloopa strengthened the underlying financial data, which matters because in finance a "
  "confidently wrong number is worse than no answer at all.",
  "The obvious question is what happens to junior analyst work, and the honest answer is that a "
  "meaningful portion of it — the formatting, the comp table assembly, the first-pass document "
  "review — is exactly what this automates. Firms adopting it are not eliminating analysts so much "
  "as changing what the first two years look like. Whether that produces better senior bankers or "
  "hollows out the apprenticeship is a genuinely open question.",
 ],
 features=[
  ("book", "Firm-Template Native Output",
   "Excel models, PowerPoint decks and Word memos produced in your firm's own templates, which is "
   "what makes output usable rather than a starting point."),
  ("search", "Comparable and Precedent Analysis",
   "Builds comp tables and precedent transaction analyses following investment banking convention "
   "rather than generic financial summarisation."),
  ("database", "Verified Financial Data",
   "Underpinned by financial data partnerships, including Daloopa from April 2026, because accuracy "
   "is non-negotiable in this domain."),
  ("layers", "Data Room Document Review",
   "Works across large document sets in diligence, which is where the most punishing hours go."),
  ("lock", "Firm-Grade Security",
   "Built for an industry where a data leak is an existential rather than reputational event."),
  ("users", "Deal Team Workflows",
   "Structured around how deal teams actually work rather than around a general chat interface."),
 ],
 pros=[
  "Output arrives in usable firm formats, not as chat text to reformat",
  "Workflows follow banking convention rather than generic finance",
  "Very strong adoption — 35,000+ professionals at 250+ firms",
  "Financial data partnerships address the accuracy problem directly",
  "$2B valuation reflects real revenue rather than promise",
 ],
 cons=[
  "Extremely narrow — useless outside financial services",
  "Enterprise pricing aimed at firms, not individuals",
  "Output still requires expert review before it reaches a client",
  "Raises real questions about how junior analysts learn the trade",
 ],
 pricing=[
  ("Enterprise", "Custom", "Firm-level licensing priced on seats and deployment scope"),
 ],
 excels=[
  "Investment banking deal teams under time pressure",
  "Private equity diligence across large document sets",
  "Comparable company and precedent transaction analysis",
  "Any finance workflow where template compliance is mandatory",
 ],
 not_ideal=[
  "Anyone outside financial services",
  "Individual analysts without firm licensing",
  "Work where the reasoning, not the assembly, is the hard part",
 ],
 comparisons=[
  ("Rogo vs Hebbia",
   "Hebbia bets the bottleneck is reading — its Matrix product answers questions across hundreds of "
   "documents in parallel. Rogo bets it is the whole task list and produces finished deliverables. "
   "Diligence-heavy work leans Hebbia; deal execution leans Rogo."),
  ("Rogo vs a general AI assistant",
   "A general assistant can discuss a DCF; it cannot produce one in your firm's template with your "
   "firm's conventions. In an industry where the format is the deliverable, that gap is the entire "
   "product."),
 ],
 verdict="Rogo is the clearest example of vertical AI done properly. It succeeded by recognising that "
         "the last mile in finance is formatting and convention, not reasoning, and by building for "
         "that rather than around it — which is why 250 firms adopted it while general assistants "
         "sat unused. Output still needs expert review before it reaches a client, and it is useless "
         "outside financial services. Firms should also think seriously about what happens to the "
         "apprenticeship model when the work juniors learned from is the work being automated.",
 faq=[
  ("What does Rogo actually produce?",
   "Excel models, PowerPoint decks and Word memos in your firm's own templates, following investment "
   "banking conventions — not chat answers you then have to reformat."),
  ("How widely is Rogo used?",
   "Reported at more than 35,000 finance professionals across over 250 firms, at a $2 billion "
   "valuation."),
  ("How does Rogo handle data accuracy?",
   "Through financial data partnerships, including one with Daloopa announced in April 2026. Accuracy "
   "matters more here than in most domains because a confidently wrong number is worse than no "
   "answer."),
  ("Does Rogo replace junior analysts?",
   "It automates a substantial part of what junior analysts do — formatting, comp assembly, "
   "first-pass document review. Firms are changing what the first two years look like rather than "
   "eliminating the role outright."),
 ],
 breakdown=[("Output Usability", 9.6), ("Domain Fit", 9.7),
            ("Data Accuracy", 9.0), ("Breadth of Application", 4.5), ("Adoption Evidence", 9.5)],
 related=[("hebbia", "Hebbia", "4.4", "Document Analysis at Scale"),
          ("harvey-ai", "Harvey AI", "4.6", "Legal AI Platform"),
          ("glean", "Glean", "4.6", "Enterprise AI Search")],
),

dict(BU,
 slug="hebbia", name="Hebbia", company="Hebbia",
 domain="hebbia.com", url="https://www.hebbia.com/",
 cta2_url="https://www.hebbia.com/", cta2_label="Request a Demo",
 flag="&#127482;&#127480;", country="USA", founded="2020", hq="New York, New York, USA",
 rating=4.4, date="2026-09-06",
 badges=["Matrix", "Parallel Document Analysis", "Fortune 100"],
 quick_stats=[("Matrix", "Flagship Product"), ("$130M", "Series B"),
              ("Sub-agents", "2025 Architecture"), ("Fortune 100", "Deployments"),
              ("2020", "Founded")],
 title="Hebbia Review 2026: Matrix and Parallel Document Analysis | TechVernia",
 meta_desc="Hebbia review 2026. Matrix processes hundreds of documents in parallel and "
           "answers structured questions across all of them at once. Architecture, "
           "sub-agent redesign, use cases in finance and law, and honest limits.",
 meta_keywords="Hebbia review, Matrix document analysis, AI for due diligence, parallel "
               "document processing, Hebbia vs Rogo, legal document AI",
 overview=[
  "Hebbia's core insight is that the hard problem in professional services is not answering a "
  "question about one document — it is answering the same question about four hundred documents and "
  "being able to defend every answer. Its flagship product, Matrix, is built for exactly that: a "
  "grid where rows are documents and columns are questions, filled in parallel with the source for "
  "each cell.",
  "That interface choice does more work than it appears to. A chat interface forces sequential "
  "questioning and hides what was not asked; a matrix makes coverage visible. You can see "
  "immediately which contracts have the unusual indemnity clause, which filings mention the "
  "contingency, and which cells the system could not answer — and the last of those is often the "
  "most valuable output.",
  "The architecture was redesigned in 2025 around specialised sub-agents, separating retrieval from "
  "output formatting to improve precision on complex queries. Hebbia raised $130 million in Series B "
  "funding and is deployed at asset managers, law firms, banks and Fortune 100 companies — "
  "environments where being confidently wrong has consequences measured in litigation rather than "
  "user complaints.",
 ],
 features=[
  ("layers", "Matrix Grid Interface",
   "Documents as rows, questions as columns, answers filled in parallel — coverage becomes visible "
   "rather than implicit."),
  ("check", "Cell-Level Source Attribution",
   "Every answer cites the specific passage it came from, which is the minimum standard for legal and "
   "financial work."),
  ("cpu", "Specialised Sub-Agent Architecture",
   "Retrieval and output formatting handled by separate agents, improving precision on complex "
   "multi-part queries."),
  ("search", "Hundreds of Documents at Once",
   "Built for corpus-scale analysis rather than one-document question answering."),
  ("lock", "Regulated-Industry Security",
   "Deployed at banks, law firms and Fortune 100 companies, with the controls those environments "
   "require."),
  ("book", "Explicit Coverage Gaps",
   "Shows which questions it could not answer for which documents, which is frequently the most "
   "important finding in diligence."),
 ],
 pros=[
  "The matrix interface makes coverage visible in a way chat never can",
  "Cell-level attribution meets professional evidentiary standards",
  "Genuinely built for corpus scale rather than scaled up from single documents",
  "Sub-agent redesign improved precision on complex queries",
  "Proven in the most demanding regulated environments",
 ],
 cons=[
  "Enterprise pricing well beyond individual practitioners",
  "Learning curve — the matrix model is unfamiliar at first",
  "Answer quality depends heavily on question formulation",
  "Narrow: designed for document-heavy professional work",
 ],
 pricing=[
  ("Enterprise", "Custom", "Priced on seats, document volume and deployment scope"),
 ],
 excels=[
  "Due diligence across large document sets",
  "Contract review at portfolio scale",
  "Regulatory and litigation discovery",
  "Any work where you must answer the same question across hundreds of documents",
 ],
 not_ideal=[
  "Single-document analysis, where a general assistant suffices",
  "Small firms without enterprise budget",
  "Work where the difficulty is judgement rather than volume",
 ],
 comparisons=[
  ("Hebbia vs Rogo",
   "Hebbia bets the bottleneck is reading across a corpus; Rogo bets it is the whole deal-team task "
   "list and produces finished banker deliverables. Diligence-heavy work favours Hebbia; execution "
   "and formatting favour Rogo. Several firms run both."),
  ("Hebbia vs a general AI assistant",
   "General assistants handle one document at a time and hide what they did not check. Matrix makes "
   "coverage explicit across hundreds of documents with per-cell sources — which is the difference "
   "between a useful tool and a defensible one."),
 ],
 verdict="Hebbia solves a real and expensive problem: reading everything, and proving you did. The "
         "matrix interface is a genuinely better abstraction than chat for corpus-scale work, because "
         "it makes gaps visible instead of leaving them unasked, and per-cell source attribution "
         "meets the evidentiary bar that legal and financial work actually requires. It is expensive "
         "and narrow, and it rewards careful question design more than most tools. For diligence, "
         "discovery and portfolio-scale contract review, it is the strongest option available.",
 faq=[
  ("What is Matrix?",
   "Hebbia's flagship product: a grid with documents as rows and questions as columns, answered in "
   "parallel with a source for every cell. It replaces sequential chat questioning with visible "
   "coverage."),
  ("How many documents can it handle?",
   "Hundreds at once — it is built for corpus-scale analysis rather than adapted from single-document "
   "question answering."),
  ("Can I verify its answers?",
   "Yes, and this is central to the product. Every cell cites the specific source passage, which is "
   "the minimum standard for legal and financial use."),
  ("Who uses Hebbia?",
   "Asset managers, law firms, banks and Fortune 100 companies — environments where an unverifiable "
   "answer is not usable regardless of how good it sounds."),
 ],
 breakdown=[("Corpus Scale", 9.6), ("Source Attribution", 9.5),
            ("Interface Design", 9.0), ("Accessibility", 5.5), ("Domain Breadth", 7.0)],
 related=[("rogo", "Rogo", "4.5", "AI Analyst for Finance"),
          ("harvey-ai", "Harvey AI", "4.6", "Legal AI Platform"),
          ("everlaw", "Everlaw", "4.5", "Litigation Discovery")],
),

dict(ME,
 slug="nabla", name="Nabla", company="Nabla",
 domain="nabla.com", url="https://www.nabla.com/",
 cta2_url="https://www.nabla.com/", cta2_label="Request a Demo",
 flag="&#127467;&#127479;", country="France", founded="2018", hq="Paris, France / New York, USA",
 rating=4.5, date="2026-09-06",
 badges=["Ambient Scribe", "EHR Integrated", "Specialty Coverage"],
 quick_stats=[("Ambient", "Documentation"), ("EHR", "Integrated"),
              ("Ambulatory", "Primary Setting"), ("Multilingual", "Support"),
              ("2018", "Founded")],
 title="Nabla Review 2026: Ambient AI Clinical Documentation | TechVernia",
 meta_desc="Nabla review 2026. The ambient AI scribe that turns a consultation into a "
           "structured clinical note without a clinician touching a keyboard. EHR "
           "integration, specialty accuracy, and where the human still has to check.",
 meta_keywords="Nabla review, ambient AI scribe, clinical documentation AI, medical "
               "scribe software, Nabla vs Abridge, EHR AI integration",
 overview=[
  "Clinical documentation is the reason a great many doctors describe themselves as data entry "
  "clerks with a medical degree. Studies through 2025 and 2026 consistently put documentation burden "
  "at the top of the burnout causes, and ambient AI scribes are the intervention that has actually "
  "moved the number: health systems report clinicians saving two to three hours a day. By 2026, over "
  "40 per cent of US physicians use some form of AI documentation, and at UCSF the figure reached 70 "
  "per cent.",
  "Nabla listens to the consultation and produces a structured clinical note — history, examination, "
  "assessment, plan — without the clinician touching a keyboard. It is positioned in the ambulatory "
  "and specialty segment rather than competing head-on for enterprise health system contracts, which "
  "is a sensible read of where the market splits: Abridge and Ambience chase health systems, "
  "Microsoft Dragon Copilot holds the incumbent position, and the ambulatory space rewards workflow "
  "fit and specialty accuracy over Epic integration depth.",
  "The distinction that is starting to matter in 2026 is between systems that transcribe and systems "
  "that support clinical reasoning. Nabla sits toward the structured-documentation end: it produces "
  "an accurate, well-organised note. Every note still requires clinician review and sign-off — this "
  "is a documentation tool, not a clinical decision system, and treating it as the latter would be a "
  "serious error.",
 ],
 features=[
  ("mic", "Ambient Consultation Capture",
   "Listens to the natural conversation rather than requiring dictation, so the clinician talks to "
   "the patient instead of to the software."),
  ("book", "Structured Clinical Notes",
   "Produces properly organised notes — history, examination, assessment, plan — rather than a raw "
   "transcript someone has to restructure."),
  ("link", "EHR Integration",
   "Notes flow into the electronic health record, because a note that requires copy-paste has saved "
   "considerably less time than it appears to."),
  ("layers", "Specialty Adaptation",
   "Tuned for the vocabulary and note structure of different specialties, which is where generic "
   "transcription falls down."),
  ("globe", "Multilingual Consultations",
   "Handles consultations in multiple languages, reflecting the company's European origins and "
   "genuine clinical need."),
  ("lock", "Healthcare Compliance",
   "Built for regulated clinical environments with the data protection requirements they carry."),
 ],
 pros=[
  "Addresses the documented leading cause of clinician burnout",
  "Reported time savings of two to three hours per day are substantial and consistent",
  "Specialty adaptation beats generic transcription meaningfully",
  "Multilingual support is genuinely differentiated",
  "EHR integration means the time saving is real, not theoretical",
 ],
 cons=[
  "Every note requires clinician review and sign-off — non-negotiable",
  "Accuracy varies with accent, background noise and consultation style",
  "Less deep Epic integration than enterprise-focused competitors",
  "Adds a subscription cost to already-pressured practice economics",
 ],
 pricing=[
  ("Individual", "Subscription", "Per-clinician pricing for independent practice"),
  ("Practice", "Custom", "Group pricing with EHR integration"),
  ("Enterprise", "Custom", "Health system deployment, compliance review, support"),
 ],
 excels=[
  "Ambulatory and outpatient clinical settings",
  "Specialties where note structure and vocabulary are distinctive",
  "Multilingual practice environments",
  "Individual clinicians and small practices priced out of enterprise platforms",
 ],
 not_ideal=[
  "Large health systems wanting the deepest Epic integration",
  "Any use as a clinical decision support system",
  "Consultation settings with heavy background noise",
 ],
 comparisons=[
  ("Nabla vs Abridge",
   "Abridge is the enterprise health system player with deeper Epic integration and system-wide "
   "contracts; Nabla is stronger in ambulatory and specialty settings and on multilingual "
   "consultations. Health systems lean Abridge, individual practices lean Nabla."),
  ("Nabla vs Microsoft Dragon Copilot",
   "Dragon Copilot, formerly Nuance DAX, is the incumbent with the deepest hospital footprint and "
   "enterprise pricing to match. Nabla is more accessible to smaller practices and more agile on "
   "specialty and language coverage."),
 ],
 verdict="Nabla is a strong option in the segment ambient scribes actually help most — ambulatory and "
         "specialty practice, where clinicians carry the documentation burden personally rather than "
         "having it absorbed by a health system's IT budget. Specialty adaptation and multilingual "
         "support are real differentiators against generic transcription. Two things are "
         "non-negotiable in evaluation: trial it on your own consultations rather than trusting a "
         "demo, because accuracy varies with accent and setting, and hold the line that every note "
         "gets clinician review. This documents care; it does not decide it.",
 faq=[
  ("Does Nabla replace clinical documentation review?",
   "No, and this is not negotiable. Every note requires clinician review and sign-off. Nabla produces "
   "the draft; the clinician remains responsible for what enters the record."),
  ("How much time do clinicians actually save?",
   "Health systems using ambient scribes report two to three hours per day. Your result depends on "
   "consultation type, specialty and how well the tool fits your existing workflow."),
  ("Does it integrate with our EHR?",
   "Yes, EHR integration is supported, and it matters — a note requiring copy-paste captures far less "
   "of the theoretical time saving."),
  ("How does it compare to Abridge?",
   "Abridge targets large health systems with deep Epic integration; Nabla is stronger in ambulatory "
   "and specialty settings and on multilingual consultations."),
 ],
 breakdown=[("Note Quality", 9.0), ("Time Saved", 9.3),
            ("Specialty Fit", 8.8), ("EHR Depth", 7.8), ("Accessibility", 8.5)],
 related=[("abridge", "Abridge", "4.6", "Enterprise Ambient Scribe"),
          ("suki-ai", "Suki AI", "4.4", "Voice Clinical Assistant"),
          ("nuance-dragon", "Nuance Dragon", "4.5", "Clinical Speech Recognition")],
),

]
