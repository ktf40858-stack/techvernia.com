# -*- coding: utf-8 -*-
"""Lot 5 - Base vectorielle, observabilite LLM (llmops/) et memoire d'agents (agents/)."""

DA = dict(category="data", cat_href="../../categories.html",
          cat_label="AI Data Infrastructure", app_category="DeveloperApplication")
OP = dict(category="llmops", cat_href="../../categories.html",
          cat_label="LLMOps & Evaluation", app_category="DeveloperApplication")
AG = dict(category="agents", cat_href="../../categories/ai-agents.html",
          cat_label="AI Agents", app_category="DeveloperApplication")

TOOLS = [

dict(DA,
 slug="weaviate", name="Weaviate", company="Weaviate",
 domain="weaviate.io", url="https://weaviate.io/",
 cta2_url="https://console.weaviate.cloud/", cta2_label="Try Weaviate Cloud",
 flag="&#127475;&#127473;", country="Netherlands", founded="2019", hq="Amsterdam, Netherlands",
 rating=4.5, date="2026-09-06",
 badges=["Open Source", "AI-Native", "Built-In Vectorisation"],
 quick_stats=[("BSD-3", "Licence"), ("Go", "Written In"),
              ("Modules", "Built-in Vectorisers"), ("GraphQL + REST", "APIs"), ("2019", "Founded")],
 title="Weaviate Review 2026: The AI-Native Vector Database | TechVernia",
 meta_desc="Weaviate review 2026. The open-source AI-native database with built-in "
           "vectorisation modules, hybrid search and generative feedback loops. When "
           "bundling more of the stack helps, and when it gets in the way.",
 meta_keywords="Weaviate review, AI-native database, open source vector database, hybrid "
               "search, Weaviate vs Qdrant, RAG database",
 overview=[
  "Weaviate takes the opposite design position to a lean vector engine: instead of expecting you to "
  "generate embeddings and hand it vectors, it can do the embedding itself. Its module system plugs "
  "in vectorisers and generative models directly, so you insert text objects and the database "
  "handles turning them into vectors and, if you want, generating answers from what it retrieves.",
  "That bundling is the whole argument, and it cuts both ways. It removes an entire moving part from "
  "your pipeline — no separate embedding service to deploy, version and keep in sync with your index "
  "— which is a real simplification for teams building their first serious retrieval system. It also "
  "couples your database to your embedding strategy, and changing embedding models later is more "
  "entangled than it would be with a database that only stores vectors.",
  "Technically it is solid: open source under BSD-3, written in Go, with genuinely good hybrid search "
  "combining vector similarity and BM25 keyword matching, plus multi-tenancy designed for it rather "
  "than approximated with metadata filters. It runs self-hosted or as managed Weaviate Cloud, and "
  "the self-hosted version is not artificially limited.",
 ],
 features=[
  ("layers", "Built-In Vectorisation Modules",
   "The database generates embeddings itself through pluggable modules, removing a separate embedding "
   "service from your architecture."),
  ("search", "Hybrid Search",
   "Vector similarity fused with BM25 keyword matching, tunable per query — the reliable answer to "
   "retrieval failures on exact terms."),
  ("brain", "Generative Feedback Loops",
   "Retrieval and generation can happen in one call, with the database passing retrieved context "
   "straight to a configured model."),
  ("users", "First-Class Multi-Tenancy",
   "Tenant isolation is a designed feature rather than a metadata-filtering convention, which matters "
   "for SaaS products built on retrieval."),
  ("git", "BSD-3 Open Source",
   "Permissive licensing with a self-hosted version that is not deliberately crippled."),
  ("link", "GraphQL and REST APIs",
   "A GraphQL interface that suits complex filtered queries, alongside conventional REST."),
 ],
 pros=[
  "Built-in vectorisation removes a whole component from your stack",
  "Hybrid search is mature and well tuned",
  "Multi-tenancy designed in, not approximated",
  "Permissive open-source licence with a real self-hosted product",
  "Generative feedback loops shorten simple RAG applications considerably",
 ],
 cons=[
  "More moving parts than a lean vector engine, and more to learn",
  "Coupling the database to your embedding strategy complicates later changes",
  "Heavier resource footprint than Qdrant for equivalent workloads",
  "GraphQL is a barrier for teams unfamiliar with it",
 ],
 pricing=[
  ("Open Source", "Free", "BSD-3, self-hosted, no feature restrictions"),
  ("Serverless Cloud", "Usage-based", "Managed, priced on stored dimensions and queries"),
  ("Enterprise Cloud", "Custom", "Dedicated resources, SLAs, compliance controls"),
 ],
 excels=[
  "Teams that want the database to handle embedding as well as storage",
  "Multi-tenant SaaS products built on retrieval",
  "Applications needing carefully tuned hybrid search",
  "Reducing the number of services in a first production RAG system",
 ],
 not_ideal=[
  "Teams that already run their own embedding pipeline",
  "Minimal-footprint deployments where Qdrant is leaner",
  "Workloads where embedding strategy changes frequently",
 ],
 comparisons=[
  ("Weaviate vs Qdrant",
   "Qdrant is the leaner, faster engine that stores vectors and does that superbly; Weaviate bundles "
   "vectorisation and generation. If you have an embedding pipeline, Qdrant. If you want fewer "
   "services to run, Weaviate."),
  ("Weaviate vs Pinecone",
   "Weaviate can be self-hosted and is open source; Pinecone is managed-only with less operational "
   "burden. The decision is the familiar one between data control and outsourced operations."),
 ],
 verdict="Weaviate is the vector database for teams who would rather run one system than three. "
         "Built-in vectorisation and generative feedback loops genuinely shorten the path from "
         "documents to a working RAG application, and the hybrid search and multi-tenancy "
         "implementations are among the best available. The cost is coupling: your database now has "
         "opinions about your embedding strategy, and unpicking that later is real work. Choose it "
         "when simplicity of architecture matters more than modularity, and choose Qdrant when the "
         "reverse is true.",
 faq=[
  ("What does AI-native mean here?",
   "Weaviate can generate embeddings and call generative models itself through pluggable modules, "
   "rather than only storing vectors you produced elsewhere."),
  ("Is Weaviate free?",
   "The self-hosted version is BSD-3 licensed and free with no feature restrictions. Weaviate Cloud "
   "is a paid managed service."),
  ("Should I choose Weaviate or Qdrant?",
   "Weaviate if you want the database to handle embedding and generation too; Qdrant if you already "
   "have an embedding pipeline and want a lean, fast vector engine."),
  ("How does multi-tenancy work?",
   "Tenants are a first-class concept with real isolation, rather than being approximated through "
   "metadata filters — which matters for SaaS products serving many customers from one deployment."),
 ],
 breakdown=[("Feature Breadth", 9.3), ("Hybrid Search", 9.4),
            ("Multi-Tenancy", 9.2), ("Simplicity", 7.0), ("Openness", 9.0)],
 related=[("qdrant", "Qdrant", "4.7", "Open-Source Vector DB"),
          ("pinecone", "Pinecone", "4.5", "Managed Vector DB"),
          ("obviously-ai", "Obviously AI", "4.2", "No-Code Data Science")],
),

dict(OP,
 slug="langfuse", name="Langfuse", company="Langfuse",
 domain="langfuse.com", url="https://langfuse.com/",
 cta2_url="https://cloud.langfuse.com/", cta2_label="Start Free",
 flag="&#127465;&#127466;", country="Germany", founded="2022", hq="Berlin, Germany",
 rating=4.7, date="2026-09-06",
 badges=["MIT Licence", "Self-Hostable", "Category Default"],
 quick_stats=[("MIT", "Licence"), ("Traces + Evals", "Scope"),
              ("Self-host", "Full Product"), ("Framework-agnostic", "Integration"),
              ("2022", "Founded")],
 title="Langfuse Review 2026: Open-Source LLM Observability | TechVernia",
 meta_desc="Langfuse review 2026. The MIT-licensed LLM observability platform teams "
           "self-host: tracing, evaluations, datasets and prompt management in one "
           "product. Deployment, limits and how it compares to LangSmith.",
 meta_keywords="Langfuse review, LLM observability, open source LLM tracing, LLM "
               "evaluation platform, Langfuse vs LangSmith, self-hosted LLMOps",
 overview=[
  "Langfuse solves the problem every team hits about three weeks after their LLM feature reaches "
  "production: something is wrong, and you have no idea which step of a multi-agent, multi-tool call "
  "chain caused it. Conventional application monitoring shows you a slow request. Langfuse shows you "
  "the nested spans — every model call, retrieval, tool invocation and their inputs and outputs — so "
  "the failure becomes an ordinary debugging problem instead of a guessing game.",
  "It goes further than tracing. Datasets, evaluations and prompt management live in the same "
  "product, which means the loop from 'this trace looks wrong' to 'add it to a test set' to 'verify "
  "the fix did not break something else' happens without exporting data between tools. That "
  "integration is why teams consolidate on it rather than assembling three separate services.",
  "The decisive feature for many organisations is the licence. Langfuse is MIT-licensed and fully "
  "self-hostable, so LLM traces — which routinely contain customer data, internal documents and "
  "prompts you would rather not hand to a third party — can stay on your infrastructure. Managed "
  "cloud exists for teams that do not need that; the self-hosted version is the complete product, "
  "not a teaser.",
 ],
 features=[
  ("activity", "Nested Trace Capture",
   "Full spans across agents, retrievers and tool calls with inputs and outputs, turning opaque LLM "
   "failures into readable execution traces."),
  ("check", "Evaluations on Production Traffic",
   "Attach automated or human evaluation scores to real traces, not only to a curated offline test "
   "set."),
  ("book", "Datasets from Real Failures",
   "Promote a failing production trace into a regression dataset in one step, which is how LLM test "
   "suites actually get built."),
  ("layers", "Prompt Management",
   "Version prompts, deploy them without a code release, and see which version produced which trace."),
  ("git", "MIT Licence, Fully Self-Hostable",
   "The complete product runs on your infrastructure, which matters because traces contain your most "
   "sensitive data."),
  ("link", "Framework-Agnostic SDKs",
   "Works with LangChain, LlamaIndex, raw SDK calls and custom stacks, rather than assuming one "
   "framework."),
 ],
 pros=[
  "MIT-licensed and genuinely self-hostable — the whole product, not a limited edition",
  "Tracing, evaluation, datasets and prompts in one place",
  "Framework-agnostic rather than tied to one orchestration library",
  "Keeps sensitive trace data on your own infrastructure",
  "Active development and a strong community",
 ],
 cons=[
  "Self-hosting means running a database and a service you must maintain",
  "High-volume trace storage grows quickly and needs a retention policy",
  "Evaluation tooling is less opinionated than dedicated eval platforms",
  "Instrumentation still has to be added to your code",
 ],
 pricing=[
  ("Self-Hosted", "Free", "MIT licence, complete feature set, your infrastructure"),
  ("Cloud Hobby", "Free", "Limited monthly events on managed cloud"),
  ("Cloud Pro", "From $59 / month", "Higher volumes, longer retention, team features"),
  ("Enterprise", "Custom", "SSO, compliance, support, dedicated deployment"),
 ],
 excels=[
  "Debugging multi-step agent and RAG failures in production",
  "Teams that cannot send prompts and traces to a third party",
  "Building regression test suites from real production failures",
  "Consolidating tracing, evals and prompt versioning in one tool",
 ],
 not_ideal=[
  "Teams with no capacity to run infrastructure who also cannot use cloud",
  "Very high trace volumes without a storage strategy",
  "Organisations wanting the deepest LangGraph-specific visualisations",
 ],
 comparisons=[
  ("Langfuse vs LangSmith",
   "LangSmith has the deepest integration with LangChain and LangGraph and is the natural pick if you "
   "live inside that stack. Langfuse is framework-agnostic and self-hostable under MIT. Data "
   "residency usually decides it."),
  ("Langfuse vs Braintrust",
   "Braintrust is stronger on prompt-centric evaluation workflows and experiment management; Langfuse "
   "is stronger on open, self-hosted tracing. Teams focused on shipping quality improvements lean "
   "Braintrust, teams focused on understanding production lean Langfuse."),
 ],
 verdict="Langfuse is the default LLM observability platform for good reasons. The MIT licence and "
         "complete self-hosted product remove the objection that kills most observability purchases "
         "in regulated environments — traces contain your most sensitive data, and here they never "
         "leave. Having tracing, evaluation, datasets and prompt management in one tool means the "
         "loop from production failure to regression test is short enough that teams actually close "
         "it. Plan trace retention before you scale, and accept that you still have to instrument "
         "your code.",
 faq=[
  ("Is Langfuse really free to self-host?",
   "Yes. It is MIT-licensed and the self-hosted deployment is the complete product with no feature "
   "gating. The managed cloud is a convenience, not an unlock."),
  ("Does it only work with LangChain?",
   "No. Langfuse is framework-agnostic, with SDKs for LangChain, LlamaIndex, raw provider SDKs and "
   "custom stacks."),
  ("Why does self-hosting matter for observability?",
   "LLM traces contain prompts, retrieved documents and model outputs — frequently customer data and "
   "internal information. Self-hosting keeps that on your infrastructure instead of a vendor's."),
  ("What is the difference between tracing and evaluation here?",
   "Tracing records what happened; evaluation scores whether it was any good. Langfuse does both and "
   "lets you promote a bad trace into a dataset to test future changes against."),
 ],
 breakdown=[("Trace Depth", 9.4), ("Self-Hosting", 9.9),
            ("Evaluation Tooling", 8.5), ("Framework Coverage", 9.2), ("Value", 9.6)],
 related=[("langsmith", "LangSmith", "4.5", "LangChain Observability"),
          ("braintrust", "Braintrust", "4.5", "Eval-First Platform"),
          ("langchain", "LangChain", "4.4", "Agent Framework")],
),

dict(OP,
 slug="langsmith", name="LangSmith", company="LangChain",
 domain="langchain.com", url="https://www.langchain.com/langsmith",
 cta2_url="https://smith.langchain.com/", cta2_label="Start Free",
 flag="&#127482;&#127480;", country="USA", founded="2022", hq="San Francisco, California, USA",
 rating=4.5, date="2026-09-06",
 badges=["LangChain Native", "Agent Visualisation", "Annotation Queues"],
 quick_stats=[("LangGraph", "Deep Integration"), ("Annotation queues", "Human Review"),
              ("Managed", "Primary Model"), ("Free tier", "Entry"), ("2022", "Founded")],
 title="LangSmith Review 2026: Observability for LangChain and LangGraph | TechVernia",
 meta_desc="LangSmith review 2026. The observability platform from the LangChain team: "
           "high-detail agent traces, annotation queues and dataset workflows. Where "
           "its LangGraph integration wins and where Langfuse is the better choice.",
 meta_keywords="LangSmith review, LangChain observability, LangGraph tracing, LLM "
               "monitoring, LangSmith vs Langfuse, agent debugging",
 overview=[
  "LangSmith is the observability platform built by the team behind LangChain, and its advantage is "
  "exactly what you would expect: nothing else understands a LangGraph execution as well. Agent "
  "graphs are visualised as graphs, with the branches taken, the state at each node and the loops "
  "that ran — a level of structural detail that framework-agnostic tools cannot reconstruct from "
  "generic spans.",
  "The second distinctive feature is annotation queues. Traces are routed to human reviewers who "
  "label them, and those labels become datasets for evaluation. It sounds procedural, but it is the "
  "mechanism that turns a domain expert's judgement into a repeatable test — the step most teams skip "
  "and then wonder why their evaluation set does not reflect what users actually care about.",
  "The trade-off is that LangSmith is primarily a managed service and works best inside the LangChain "
  "ecosystem. It does support other stacks, but the further you move from LangChain and LangGraph the "
  "smaller the advantage becomes, and at that point the self-hosting question favours alternatives.",
 ],
 features=[
  ("layers", "LangGraph Graph Visualisation",
   "Agent executions rendered as the graphs they are, with branches, state and loops visible — not "
   "reconstructed from generic spans."),
  ("users", "Annotation Queues",
   "Route traces to human reviewers for labelling, converting expert judgement into evaluation "
   "datasets systematically."),
  ("activity", "High-Detail Tracing",
   "Deep capture of inputs, outputs, token usage and latency at every step of a chain or agent."),
  ("check", "Dataset and Experiment Management",
   "Build test sets from real traces and compare prompt or model changes against them."),
  ("book", "Prompt Hub",
   "Versioned prompt storage and sharing integrated with the traces that used each version."),
  ("link", "Native LangChain Integration",
   "Instrumentation is close to automatic if you already use LangChain or LangGraph."),
 ],
 pros=[
  "Unmatched visibility into LangGraph agent executions",
  "Annotation queues are the best human-in-the-loop evaluation workflow available",
  "Near-zero instrumentation effort inside the LangChain stack",
  "Mature dataset and experiment tooling",
  "Backed by the team that maintains the framework",
 ],
 cons=[
  "Advantage shrinks considerably outside LangChain and LangGraph",
  "Primarily managed — self-hosting is an enterprise arrangement",
  "Traces leave your infrastructure on standard plans",
  "Pricing scales with trace volume and can climb quickly",
 ],
 pricing=[
  ("Developer", "Free", "Single user with a monthly trace allowance"),
  ("Plus", "From $39 / user / month", "Team features, higher trace volumes, longer retention"),
  ("Enterprise", "Custom", "Self-hosted deployment, SSO, compliance, support"),
 ],
 excels=[
  "Teams building on LangChain and LangGraph",
  "Debugging complex agent graphs with branching and loops",
  "Human-in-the-loop evaluation with domain experts",
  "Getting observability running with minimal instrumentation work",
 ],
 not_ideal=[
  "Stacks that do not use LangChain",
  "Organisations that must self-host without an enterprise contract",
  "High-volume tracing on a tight budget",
 ],
 comparisons=[
  ("LangSmith vs Langfuse",
   "If you live in LangChain and LangGraph, LangSmith's graph visualisation and near-zero "
   "instrumentation are worth real money. If you need self-hosting or run a mixed stack, Langfuse's "
   "MIT licence settles it."),
  ("LangSmith vs Braintrust",
   "LangSmith is oriented around understanding what your agents did; Braintrust around systematically "
   "improving quality through evaluation. The two overlap but answer different primary questions."),
 ],
 verdict="LangSmith is the obvious choice for teams committed to LangChain and LangGraph, and a "
         "harder sell for everyone else. The graph visualisation is genuinely better than what "
         "framework-agnostic tools can produce, because it works from structure rather than inferring "
         "it, and annotation queues are the most practical answer anyone ships to getting expert "
         "judgement into an evaluation set. Outside that ecosystem the advantage narrows and the "
         "managed-only posture starts to matter. Judge it on how deep you are in LangChain — that is "
         "the whole decision.",
 faq=[
  ("Do I need to use LangChain to use LangSmith?",
   "No, it supports other stacks, but the advantage over framework-agnostic alternatives shrinks the "
   "further you move from LangChain and LangGraph."),
  ("Can LangSmith be self-hosted?",
   "Self-hosted deployment is available as part of an enterprise arrangement. On standard plans it is "
   "a managed service and traces leave your infrastructure."),
  ("What are annotation queues?",
   "A workflow that routes traces to human reviewers for labelling, so expert judgement becomes "
   "reusable evaluation data rather than a one-off opinion."),
  ("How does pricing work?",
   "A free developer tier, then per-user pricing from around $39 per month with allowances that scale "
   "on trace volume. High-volume applications should model this before committing."),
 ],
 breakdown=[("LangGraph Visibility", 9.8), ("Human-in-the-Loop", 9.4),
            ("Instrumentation Effort", 9.2), ("Stack Independence", 6.5), ("Data Control", 6.0)],
 related=[("langfuse", "Langfuse", "4.7", "Open-Source Observability"),
          ("braintrust", "Braintrust", "4.5", "Eval-First Platform"),
          ("langchain", "LangChain", "4.4", "Agent Framework")],
),

dict(OP,
 slug="braintrust", name="Braintrust", company="Braintrust Data",
 domain="braintrust.dev", url="https://www.braintrust.dev/",
 cta2_url="https://www.braintrust.dev/signup", cta2_label="Start Free",
 flag="&#127482;&#127480;", country="USA", founded="2023", hq="San Francisco, California, USA",
 rating=4.5, date="2026-09-06",
 badges=["Eval First", "Experiment Tracking", "Prompt Playground"],
 quick_stats=[("Evaluation", "Primary Focus"), ("Experiments", "Core Workflow"),
              ("Playground", "Prompt Iteration"), ("Free tier", "Entry"), ("2023", "Founded")],
 title="Braintrust Review 2026: Evaluation-First LLM Development | TechVernia",
 meta_desc="Braintrust review 2026. The platform that treats LLM quality as an "
           "experiment problem: evaluation harnesses, side-by-side comparisons, prompt "
           "playground and traces tied to scores. Who it suits and who it does not.",
 meta_keywords="Braintrust review, LLM evaluation, prompt experimentation, AI quality "
               "management, Braintrust vs Langfuse, LLM testing",
 overview=[
  "Braintrust starts from a different question than the tracing platforms. Instead of 'what happened "
  "in production', it asks 'is this change actually better', and builds everything around answering "
  "that reliably. The core object is the experiment: a prompt or model variant, run against a "
  "dataset, scored by evaluators, and compared side by side against what you shipped last week.",
  "That framing matters because LLM development has a specific failure mode — a change that fixes the "
  "example someone complained about and quietly breaks four others nobody looks at. Vibes-based "
  "iteration cannot catch that. Braintrust's comparison views make regressions visible before they "
  "reach users, which is the difference between engineering and hoping.",
  "It also captures production traces and attaches evaluation scores to live traffic, so the same "
  "quality measures apply before and after release. The prompt playground closes the loop for the "
  "fast part of the work: try variants, see scores across the dataset immediately, promote what wins. "
  "It is a commercial platform rather than an open-source one, which is the main structural "
  "difference from Langfuse.",
 ],
 features=[
  ("check", "Experiment-Centred Evaluation",
   "Run prompt and model variants against datasets with scoring, and compare results side by side "
   "rather than judging by impression."),
  ("activity", "Regression Detection",
   "Surfaces which specific cases got worse when a change improved the average — the failure mode "
   "that eyeballing outputs always misses."),
  ("terminal", "Prompt Playground",
   "Iterate on prompts with immediate scoring across a whole dataset instead of one hand-picked "
   "example."),
  ("eye", "Production Traces with Scores",
   "The same evaluators run against live traffic, so pre-release and post-release quality are "
   "measured the same way."),
  ("layers", "Custom and Model-Graded Scorers",
   "Write deterministic scorers or use model-graded evaluation, depending on whether the quality "
   "criterion is checkable or judgemental."),
  ("users", "Human Review Workflows",
   "Route outputs for human scoring where automated evaluation cannot capture the criterion."),
 ],
 pros=[
  "The most rigorous evaluation workflow of the major platforms",
  "Catches regressions that average-score comparisons hide",
  "Prompt playground with dataset-wide scoring speeds iteration substantially",
  "Same evaluators run offline and on production traffic",
  "Good developer experience and clear documentation",
 ],
 cons=[
  "Commercial platform, not open source or freely self-hostable",
  "Requires investment in building datasets and scorers to pay off",
  "Tracing is less of a focus than in Langfuse or LangSmith",
  "Costs scale with evaluation volume, which grows fast when it works",
 ],
 pricing=[
  ("Free", "$0", "Limited monthly scores and traces for evaluation"),
  ("Pro", "From $249 / month", "Team features, higher volumes, longer retention"),
  ("Enterprise", "Custom", "Dedicated deployment options, SSO, compliance, support"),
 ],
 excels=[
  "Teams shipping frequent prompt and model changes",
  "Preventing quality regressions before release",
  "Comparing models honestly on your own data rather than public benchmarks",
  "Organisations treating LLM quality as an engineering discipline",
 ],
 not_ideal=[
  "Teams that have not yet built any evaluation datasets",
  "Organisations requiring open-source, self-hosted tooling",
  "Projects where the primary need is production debugging",
 ],
 comparisons=[
  ("Braintrust vs Langfuse",
   "Langfuse answers 'what happened'; Braintrust answers 'is this better'. Langfuse is open source "
   "and self-hostable; Braintrust is commercial with deeper evaluation tooling. Mature teams often "
   "want both, and pick based on which question hurts more today."),
  ("Braintrust vs manual spreadsheet evaluation",
   "Most teams start with a spreadsheet of test prompts and manual review. That works up to about "
   "thirty cases, then collapses. Braintrust is what replaces it, and the migration is easier before "
   "the spreadsheet has become load-bearing."),
 ],
 verdict="Braintrust is for teams that have accepted LLM quality is an engineering problem rather "
         "than a matter of taste. The experiment-centred workflow and regression detection catch the "
         "specific failure that ruins LLM products — a change that improves the average while "
         "quietly breaking cases nobody is watching. It demands real investment in datasets and "
         "scorers before it pays off, and it is commercial rather than open source. If you ship "
         "prompt changes weekly and cannot currently prove they help, this is the tool that fixes "
         "that.",
 faq=[
  ("How is Braintrust different from Langfuse?",
   "Langfuse centres on tracing what happened in production; Braintrust centres on evaluating whether "
   "a change is an improvement. Langfuse is open source and self-hostable, Braintrust is commercial "
   "with deeper evaluation tooling."),
  ("Do I need evaluation datasets before using it?",
   "You need to build them, and that is the main adoption cost. Braintrust helps by letting you "
   "promote real production traces into datasets, so you can start small and grow the set."),
  ("What is a model-graded scorer?",
   "Using a language model to judge output quality against a criterion, for cases where correctness "
   "is judgemental rather than checkable. Braintrust supports both these and deterministic scorers."),
  ("Is there a free tier?",
   "Yes, with limited monthly scores and traces. Paid plans start around $249 per month, and costs "
   "scale with evaluation volume."),
 ],
 breakdown=[("Evaluation Rigour", 9.7), ("Regression Detection", 9.5),
            ("Iteration Speed", 9.0), ("Openness", 5.0), ("Tracing Depth", 7.8)],
 related=[("langfuse", "Langfuse", "4.7", "Open-Source Observability"),
          ("langsmith", "LangSmith", "4.5", "LangChain Observability"),
          ("qodo", "Qodo", "4.3", "AI Code Testing")],
),

dict(AG,
 slug="mem0", name="Mem0", company="Mem0",
 domain="mem0.ai", url="https://mem0.ai/",
 cta2_url="https://github.com/mem0ai/mem0", cta2_label="View on GitHub",
 flag="&#127482;&#127480;", country="USA", founded="2023", hq="San Francisco, California, USA",
 rating=4.4, date="2026-09-06",
 badges=["Memory Layer", "Open Source", "Widely Adopted"],
 quick_stats=[("Memory", "Category"), ("Open source + Cloud", "Deployment"),
              ("Extract + Retrieve", "Approach"), ("Any vector store", "Backend"),
              ("2023", "Founded")],
 title="Mem0 Review 2026: The Memory Layer for AI Agents | TechVernia",
 meta_desc="Mem0 review 2026. The most widely adopted memory layer for AI agents: "
           "extracts durable facts from conversations, stores them and retrieves what "
           "matters. Architecture, privacy questions and honest limits.",
 meta_keywords="Mem0 review, AI agent memory, LLM long-term memory, personalised AI, "
               "Mem0 vs Letta, conversational memory layer",
 overview=[
  "Mem0 addresses the flaw users notice fastest in AI products: the assistant forgets everything. "
  "Stuffing the entire conversation history back into the context window is the naive fix, and it "
  "fails on both cost and quality — long contexts are expensive and models reason worse when buried "
  "in irrelevant history. Mem0 sits between the conversation and the model, extracting the facts "
  "worth keeping and retrieving only what is relevant to the current turn.",
  "The extraction step is the interesting part. Rather than storing raw transcripts, Mem0 identifies "
  "durable information — preferences, constraints, decisions, facts about the user — and maintains "
  "it as structured memories that can be updated or contradicted later. A user who changes their mind "
  "should not have both statements retrieved as equally true, and handling that is harder than it "
  "looks.",
  "It is open source with a managed cloud, works with whichever vector store you already run, and by "
  "2026 is the most widely adopted option in this category. The trade-off is scope: Mem0 is a memory "
  "layer you add to an agent, not an agent runtime. If you want memory as a first-class part of the "
  "agent's architecture, Letta is the other design worth evaluating.",
 ],
 features=[
  ("brain", "Fact Extraction",
   "Identifies durable information worth remembering rather than storing raw transcripts, which is "
   "what keeps retrieval relevant as history grows."),
  ("layers", "Memory Update and Contradiction Handling",
   "Memories can be revised when a user changes their mind, instead of accumulating contradictory "
   "statements that all retrieve as true."),
  ("search", "Relevance-Based Retrieval",
   "Pulls only memories relevant to the current turn, keeping context windows small and model "
   "reasoning sharp."),
  ("database", "Backend-Agnostic Storage",
   "Works with Qdrant, Pinecone, Chroma and others, so it fits the infrastructure you already run."),
  ("git", "Open Source Core",
   "Self-hostable, which matters because memory stores accumulate exactly the personal data you must "
   "be careful with."),
  ("users", "Per-User and Per-Agent Scoping",
   "Memories are scoped so one user's information never surfaces in another's session."),
 ],
 pros=[
  "Solves a problem users feel immediately and complain about loudly",
  "Extraction keeps retrieval relevant where naive history-stuffing degrades",
  "Cheaper than long-context approaches at conversation scale",
  "Open source and backend-agnostic",
  "The most adopted option, so integration examples are plentiful",
 ],
 cons=[
  "Extraction quality varies — it sometimes keeps trivia and drops what mattered",
  "Memory stores accumulate personal data, creating real GDPR obligations",
  "Adds a layer and therefore latency to every turn",
  "Debugging wrong retrieved memories is harder than debugging a prompt",
 ],
 pricing=[
  ("Open Source", "Free", "Self-hosted, bring your own vector store and models"),
  ("Cloud Free", "$0", "Limited monthly memory operations"),
  ("Cloud Pro", "Usage-based", "Production volumes with managed storage"),
  ("Enterprise", "Custom", "Compliance controls, support, dedicated deployment"),
 ],
 excels=[
  "Consumer assistants where personalisation drives retention",
  "Support agents that must remember prior tickets and preferences",
  "Long-running agents where full history is too expensive to resend",
  "Teams that want memory without redesigning their agent architecture",
 ],
 not_ideal=[
  "Stateless single-turn applications",
  "Regulated contexts where storing user facts creates unacceptable obligations",
  "Teams wanting memory built into the agent runtime rather than added beside it",
 ],
 comparisons=[
  ("Mem0 vs Letta",
   "Mem0 is a memory layer you bolt onto an existing agent; Letta is an agent runtime with memory "
   "management as a core design principle. Mem0 is easier to adopt, Letta is more principled about "
   "what stays in context."),
  ("Mem0 vs long context windows",
   "Million-token contexts make memory look unnecessary until you count the bill and notice models "
   "reason worse when the relevant fact is buried in irrelevant history. Retrieval beats brute force "
   "on both cost and quality."),
 ],
 verdict="Mem0 is the pragmatic answer to agent memory. It solves a problem users notice on day one, "
         "it does so more cheaply and more accurately than resending entire conversation histories, "
         "and it adds to your existing architecture rather than replacing it. Two things deserve "
         "attention before deploying it: extraction quality is imperfect, so evaluate it against your "
         "own conversations rather than the demo, and a memory store is by definition a personal data "
         "store, which brings deletion and retention obligations you need a plan for.",
 faq=[
  ("How is Mem0 different from just using a long context window?",
   "Long contexts are expensive and degrade reasoning when the relevant fact is buried in irrelevant "
   "history. Mem0 extracts what matters and retrieves only that, which is cheaper and usually more "
   "accurate."),
  ("Is Mem0 open source?",
   "Yes, with a managed cloud option. Self-hosting matters here because memory stores accumulate "
   "personal data."),
  ("What happens when a user changes their mind?",
   "Mem0 supports updating and contradicting existing memories rather than accumulating conflicting "
   "statements — one of the harder parts of memory systems to get right."),
  ("Does storing memories create GDPR obligations?",
   "Yes. A memory store holds personal data, so deletion, retention and access rights apply. Plan for "
   "that before deploying rather than after a request arrives."),
 ],
 breakdown=[("Retrieval Relevance", 8.6), ("Ease of Integration", 9.3),
            ("Cost Efficiency", 9.0), ("Extraction Accuracy", 7.8), ("Openness", 9.0)],
 related=[("letta", "Letta", "4.3", "Stateful Agent Runtime"),
          ("qdrant", "Qdrant", "4.7", "Vector Database"),
          ("langchain", "LangChain", "4.4", "Agent Framework")],
),

dict(AG,
 slug="letta", name="Letta", company="Letta",
 domain="letta.com", url="https://www.letta.com/",
 cta2_url="https://github.com/letta-ai/letta", cta2_label="View on GitHub",
 flag="&#127482;&#127480;", country="USA", founded="2023", hq="Berkeley, California, USA",
 rating=4.3, date="2026-09-06",
 badges=["Stateful Agents", "MemGPT Lineage", "Open Source"],
 quick_stats=[("MemGPT", "Research Origin"), ("Stateful", "Agent Model"),
              ("Context tiering", "Core Idea"), ("Open source", "Licence"), ("2023", "Founded")],
 title="Letta Review 2026: Stateful Agents with Managed Memory | TechVernia",
 meta_desc="Letta review 2026. The agent runtime from the MemGPT research team where "
           "agents manage their own context: what stays in the window, what moves to "
           "storage, what gets recalled. Architecture, learning curve and verdict.",
 meta_keywords="Letta review, MemGPT, stateful AI agents, agent memory management, "
               "Letta vs Mem0, long-running agents",
 overview=[
  "Letta comes out of the MemGPT research, which proposed treating a language model's context window "
  "the way an operating system treats RAM: a scarce resource with an explicit hierarchy, where "
  "something decides what stays resident and what gets paged out to storage and recalled later. "
  "Letta is that idea as a working agent runtime.",
  "The consequence is a different architecture from bolt-on memory. Agents are stateful objects that "
  "persist between sessions and manage their own context — deciding what belongs in the active "
  "window, what moves to long-term storage, and what to pull back when it becomes relevant again. "
  "For an agent that runs for weeks across hundreds of interactions, that self-management is a more "
  "principled answer than retrieving from an external store on every turn.",
  "The cost is conceptual. Letta asks you to think about agents as persistent processes with memory "
  "hierarchies, which is a genuine shift from the request-response mental model most teams start "
  "with. It is open source and the research pedigree is real, but it is a more demanding tool than a "
  "memory layer you add to an agent you already have.",
 ],
 features=[
  ("brain", "Agent-Managed Context",
   "Agents decide what stays in the active context window and what moves to storage, rather than a "
   "framework guessing on their behalf."),
  ("layers", "Tiered Memory Hierarchy",
   "Explicit tiers between active context and long-term storage, borrowed conceptually from operating "
   "system memory management."),
  ("clock", "Persistent Stateful Agents",
   "Agents exist between sessions as durable objects, which is the right model for assistants that "
   "run for weeks rather than minutes."),
  ("git", "Open Source with Research Lineage",
   "Built by the MemGPT team, with the underlying approach published and inspectable rather than "
   "proprietary."),
  ("eye", "Inspectable Memory State",
   "You can examine what an agent currently believes and remembers, which makes debugging long-lived "
   "agents tractable."),
  ("link", "Tool and Framework Integration",
   "Agents call external tools and integrate with the surrounding stack rather than being a closed "
   "system."),
 ],
 pros=[
  "The most principled architecture for genuinely long-running agents",
  "Research foundations rather than a memory feature retrofitted onto a framework",
  "Inspectable memory state makes long-lived agents debuggable",
  "Open source",
  "Stateful agents match how assistants are actually used",
 ],
 cons=[
  "Steeper conceptual learning curve than a bolt-on memory layer",
  "Requires adopting Letta's agent model rather than adding to your own",
  "Smaller ecosystem than Mem0",
  "Overkill for short-lived or single-session agents",
 ],
 pricing=[
  ("Open Source", "Free", "Self-hosted runtime, bring your own models"),
  ("Cloud", "Usage-based", "Managed hosting for stateful agents"),
  ("Enterprise", "Custom", "Support, compliance and deployment assistance"),
 ],
 excels=[
  "Assistants that run for weeks or months across many sessions",
  "Agents where context management is the actual engineering problem",
  "Teams who want to reason explicitly about what an agent remembers",
  "Research and advanced agent work",
 ],
 not_ideal=[
  "Simple single-session assistants",
  "Teams that want to add memory to an existing agent without restructuring",
  "Projects needing the largest possible ecosystem",
 ],
 comparisons=[
  ("Letta vs Mem0",
   "Mem0 adds memory to the agent you already have; Letta asks you to build the agent its way and "
   "gives you a much more principled memory model in return. Mem0 for pragmatism, Letta when context "
   "management is the core problem."),
  ("Letta vs a framework plus vector store",
   "Assembling memory from a framework and a vector database gives you control and a lot of "
   "decisions to make correctly. Letta encodes those decisions, which is valuable if you agree with "
   "them and constraining if you do not."),
 ],
 verdict="Letta is the thoughtful choice for agents that genuinely live a long time. Treating the "
         "context window as a managed resource with an explicit hierarchy is the right abstraction, "
         "and the MemGPT lineage means it comes from people who studied the problem rather than "
         "patched around it. It asks more of you than Mem0 — a different mental model and a "
         "commitment to its agent runtime — so it earns its place when context management is the hard "
         "part of your system rather than an afterthought. For a chatbot that needs to remember a "
         "user's name, it is more machinery than the job needs.",
 faq=[
  ("What is MemGPT?",
   "The research that Letta grew out of, proposing that agents manage their context window the way an "
   "operating system manages memory — with explicit tiers and paging between them."),
  ("How is Letta different from Mem0?",
   "Mem0 is a memory layer added to an existing agent; Letta is an agent runtime built around memory "
   "management. Letta is more principled and more demanding."),
  ("Is Letta open source?",
   "Yes, with a managed cloud option for teams that would rather not host stateful agents themselves."),
  ("When is Letta overkill?",
   "For short-lived, single-session agents. Its value appears when agents run for weeks across many "
   "interactions and context management becomes the binding constraint."),
 ],
 breakdown=[("Memory Architecture", 9.5), ("Long-Run Agent Fit", 9.3),
            ("Debuggability", 8.8), ("Learning Curve", 6.2), ("Ecosystem", 7.0)],
 related=[("mem0", "Mem0", "4.4", "Agent Memory Layer"),
          ("langchain", "LangChain", "4.4", "Agent Framework"),
          ("crewai", "CrewAI", "4.3", "Multi-Agent Framework")],
),

]
