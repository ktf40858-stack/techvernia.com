# -*- coding: utf-8 -*-
"""Lot 4 - LLM local (local-llm/) et bases vectorielles (data/)."""

LL = dict(category="local-llm", cat_href="../../categories.html",
          cat_label="Local LLM Tools", app_category="DeveloperApplication")
DA = dict(category="data", cat_href="../../categories.html",
          cat_label="AI Data Infrastructure", app_category="DeveloperApplication")

TOOLS = [

dict(LL,
 slug="jan", name="Jan", company="Menlo Research",
 domain="jan.ai", url="https://jan.ai/",
 cta2_url="https://github.com/menloresearch/jan", cta2_label="View on GitHub",
 flag="&#127480;&#127468;", country="Singapore", founded="2023", hq="Singapore",
 rating=4.4, date="2026-09-06",
 badges=["Open Source", "Offline First", "Free"],
 quick_stats=[("AGPL", "Licence"), ("100% offline", "Capable"),
              ("Free", "Forever"), ("Cross-platform", "Desktop"), ("2023", "Founded")],
 title="Jan Review 2026: The Open-Source Offline ChatGPT Alternative | TechVernia",
 meta_desc="Jan review 2026. A fully open-source desktop AI assistant that runs models "
           "entirely offline on your own machine. Architecture, extension model, "
           "hardware requirements and how it compares to LM Studio.",
 meta_keywords="Jan AI review, open source ChatGPT alternative, offline AI assistant, "
               "local LLM desktop, Jan vs LM Studio, private AI",
 overview=[
  "Jan is an open-source desktop assistant built on a simple premise: you should be able to read the "
  "code of the software you trust with your private conversations. It runs language models entirely "
  "on your machine, works with the network cable unplugged, and ships under an open licence — which "
  "makes it the natural pick for anyone whose interest in local AI is driven by verifiable privacy "
  "rather than convenience.",
  "The interface deliberately resembles the hosted assistants people already know, which lowers the "
  "adoption barrier for non-technical colleagues who need a private assistant but have no interest in "
  "learning a new paradigm. Underneath, it is more flexible than it looks: an extension system, "
  "support for multiple inference backends, and the option to connect to remote APIs when you "
  "explicitly want to, rather than by default.",
  "Compared with LM Studio, Jan is less polished and more auditable. The model discovery experience "
  "and hardware guidance are weaker, the community is smaller, and you will occasionally meet rough "
  "edges. In exchange, nothing about it is a black box. For a security-conscious user that is not a "
  "close call.",
 ],
 features=[
  ("git", "Fully Open Source",
   "Source is public and auditable, which is the entire argument for using it over a closed "
   "alternative on a privacy-motivated workflow."),
  ("lock", "Genuinely Offline",
   "Runs with no network connection at all. Nothing is sent anywhere unless you deliberately "
   "configure a remote provider."),
  ("monitor", "Familiar Assistant Interface",
   "Deliberately resembles hosted chat assistants, which matters when rolling out a private "
   "assistant to colleagues who did not ask for a new tool."),
  ("layers", "Extension System",
   "Extensible architecture for adding capabilities and backends rather than being a fixed "
   "single-purpose app."),
  ("link", "Optional Remote Providers",
   "Can connect to hosted APIs when you want frontier quality, as an explicit choice rather than a "
   "silent default."),
  ("cpu", "Multiple Inference Backends",
   "Supports different local engines under the hood, so it adapts to what your hardware does best."),
 ],
 pros=[
  "Open source, so the privacy claims are verifiable rather than promised",
  "Works fully offline including on air-gapped machines",
  "Free with no account and no commercial licensing questions",
  "Interface familiar enough to deploy to non-technical users",
  "Optional remote providers give an escape hatch when you need frontier quality",
 ],
 cons=[
  "Less polished than LM Studio",
  "Weaker model discovery and hardware guidance",
  "Smaller community, so fewer answers when something breaks",
  "Same hardware ceiling as every local tool",
 ],
 pricing=[
  ("Jan", "Free", "Full open-source application, unlimited local use"),
 ],
 excels=[
  "Security and privacy work where auditability is a requirement",
  "Air-gapped and offline environments",
  "Organisations that must avoid closed-source software on sensitive workflows",
  "Giving non-technical staff a private assistant",
 ],
 not_ideal=[
  "Users who want the smoothest possible first-run experience",
  "Low-spec machines without GPU acceleration",
  "Teams needing multi-user serving infrastructure",
 ],
 comparisons=[
  ("Jan vs LM Studio",
   "LM Studio is more polished with better hardware guidance; Jan is open source. If you are choosing "
   "a local assistant because you do not want to trust a vendor, choosing a closed-source app to do "
   "it is an odd position — which is Jan's whole case."),
  ("Jan vs Open WebUI",
   "Jan is a desktop application for one person. Open WebUI is a self-hosted server for a team. "
   "Different deployment shapes for the same underlying privacy motivation."),
 ],
 verdict="Jan is the local assistant to pick when the reason you want local is verifiable privacy "
         "rather than convenience. Open source, genuinely offline, free, and familiar enough that you "
         "can hand it to a colleague without a training session. It is rougher than LM Studio and the "
         "community is smaller, so expect to solve the occasional problem yourself. For security "
         "teams, journalists, legal work and anyone in a regulated environment, that trade is "
         "obviously worth making.",
 faq=[
  ("Is Jan completely free?",
   "Yes. It is open source and free with no account, no usage limits and no commercial licensing "
   "questions."),
  ("Does Jan work without internet?",
   "Yes, fully. Once a model is downloaded, Jan runs with no network connection at all, which is why "
   "it appears in air-gapped environments."),
  ("How is Jan different from LM Studio?",
   "Jan is open source and auditable; LM Studio is closed source but more polished, with better model "
   "discovery and hardware guidance. Choose on whether auditability matters to you."),
  ("Can Jan use hosted models too?",
   "Yes, optionally. You can connect remote providers when you want frontier quality, but that is an "
   "explicit configuration step, not a default."),
 ],
 breakdown=[("Privacy", 10.0), ("Openness", 9.8),
            ("Ease of Use", 8.2), ("Polish", 7.5), ("Value", 9.6)],
 related=[("lm-studio", "LM Studio", "4.6", "Local LLM Desktop App"),
          ("open-webui", "Open WebUI", "4.5", "Self-Hosted AI Interface"),
          ("anythingllm", "AnythingLLM", "4.3", "Local RAG Workspace")],
),

dict(LL,
 slug="open-webui", name="Open WebUI", company="Open WebUI",
 domain="openwebui.com", url="https://openwebui.com/",
 cta2_url="https://github.com/open-webui/open-webui", cta2_label="View on GitHub",
 flag="&#127482;&#127480;", country="Community", founded="2023", hq="Distributed / open source",
 rating=4.5, date="2026-09-06",
 badges=["Self-Hosted", "Multi-User", "Open Source"],
 quick_stats=[("Self-hosted", "Deployment"), ("Multi-user", "Accounts + RBAC"),
              ("Docker", "Install"), ("Free", "Open Source"), ("2023", "First Release")],
 title="Open WebUI Review 2026: Self-Hosted AI for Teams | TechVernia",
 meta_desc="Open WebUI review 2026. The self-hosted AI platform teams deploy instead of "
           "ChatGPT Enterprise: multi-user accounts, RBAC, RAG over internal documents "
           "and any model backend. Deployment, limits and verdict.",
 meta_keywords="Open WebUI review, self-hosted ChatGPT, private AI for teams, Ollama "
               "web interface, on-premise LLM, open source AI platform",
 overview=[
  "Open WebUI is what most local-AI tools are not: built for more than one person. It is a "
  "self-hosted platform you deploy on your own server, with user accounts, role-based access control "
  "and administration — the pieces that turn a personal local model into something an organisation "
  "can actually run. For teams that want a private ChatGPT rather than an individual private chat, "
  "this is the reference implementation.",
  "It is backend-agnostic, which is its second strength. Point it at local models through Ollama or "
  "vLLM, at hosted APIs, or at both simultaneously with different models available to different user "
  "groups. A team can run a confidential local model for sensitive work and a frontier hosted model "
  "for everything else, behind one interface with one access policy.",
  "The RAG layer is included rather than sold separately: upload internal documents, and users query "
  "them through the same interface. It is not the most sophisticated retrieval stack available, but "
  "it is present, self-hosted and adequate for the common case of making a team's own documents "
  "queryable without a vendor holding them.",
 ],
 features=[
  ("users", "Multi-User with RBAC",
   "Accounts, groups and role-based access control — the difference between a personal tool and "
   "something an organisation can deploy."),
  ("link", "Backend-Agnostic",
   "Works with Ollama, vLLM, OpenAI-compatible endpoints and hosted APIs, including several at once "
   "with per-group access."),
  ("book", "Built-In RAG",
   "Upload internal documents and query them through the same interface, entirely on your own "
   "infrastructure."),
  ("cube", "Docker Deployment",
   "A single container gets you running, which keeps the barrier low for a team without dedicated "
   "platform engineers."),
  ("git", "Open Source",
   "Auditable and self-hostable, with a large and active community behind it."),
  ("lock", "Data Stays on Your Infrastructure",
   "Conversations, documents and user data live on your server. Nothing is shared with a vendor by "
   "default."),
 ],
 pros=[
  "The best self-hosted multi-user AI platform available, free",
  "Works with any model backend, local or hosted, simultaneously",
  "Built-in RAG covers the common internal-documents use case",
  "Docker deployment is genuinely straightforward",
  "Active community and frequent releases",
 ],
 cons=[
  "You own the deployment: updates, backups, scaling, security",
  "RAG is adequate rather than best-in-class",
  "No commercial support contract to fall back on",
  "Quality depends entirely on the backend model you configure",
 ],
 pricing=[
  ("Open Source", "Free", "Full platform, self-hosted, unlimited users"),
 ],
 excels=[
  "Teams that need private AI but cannot use hosted enterprise plans",
  "Regulated organisations keeping conversations on their own infrastructure",
  "Mixing local and hosted models under one access policy",
  "Making internal documentation queryable without a vendor",
 ],
 not_ideal=[
  "Organisations without anyone to operate a server",
  "Teams that need a support contract and an SLA",
  "Use cases requiring sophisticated retrieval tuning",
 ],
 comparisons=[
  ("Open WebUI vs ChatGPT Enterprise",
   "ChatGPT Enterprise gives you frontier models and a vendor to call; Open WebUI gives you complete "
   "data control and costs nothing. For organisations where data residency is the binding constraint "
   "rather than model quality, it is not a close comparison."),
  ("Open WebUI vs AnythingLLM",
   "Both self-host and both do RAG. AnythingLLM is more focused on the document workspace experience; "
   "Open WebUI is stronger on multi-user administration and backend flexibility."),
 ],
 verdict="Open WebUI is the answer for organisations that need private AI for a team rather than a "
         "person. Multi-user accounts, RBAC and backend flexibility are the features that matter at "
         "that scale, and it has all three without a licence fee. The catch is the usual "
         "self-hosting catch: you own updates, backups, security and the pager. If you have someone "
         "who can run a Docker service competently, this replaces a five-figure enterprise "
         "subscription with a server. If you do not, buy the subscription.",
 faq=[
  ("Is Open WebUI free?",
   "Yes, fully open source and free with unlimited users. Your costs are the server and whatever "
   "model backend you run."),
  ("Which model backends does it support?",
   "Ollama, vLLM, OpenAI-compatible endpoints and hosted APIs — including several at once, with "
   "different models exposed to different user groups."),
  ("Can it do RAG over our internal documents?",
   "Yes. Document upload and retrieval are built in and run entirely on your infrastructure, though "
   "the retrieval stack is adequate rather than best-in-class."),
  ("How hard is it to deploy?",
   "A Docker container gets a working instance quickly. Running it properly in production — updates, "
   "backups, TLS, authentication — is ordinary sysadmin work you need to own."),
 ],
 breakdown=[("Multi-User Features", 9.3), ("Backend Flexibility", 9.5),
            ("Data Control", 9.8), ("RAG Quality", 7.5), ("Operational Burden", 6.8)],
 related=[("anythingllm", "AnythingLLM", "4.3", "Local RAG Workspace"),
          ("lm-studio", "LM Studio", "4.6", "Local LLM Desktop App"),
          ("vllm", "vLLM", "4.7", "Production Inference Engine")],
),

dict(LL,
 slug="anythingllm", name="AnythingLLM", company="Mintplex Labs",
 domain="anythingllm.com", url="https://anythingllm.com/",
 cta2_url="https://github.com/Mintplex-Labs/anything-llm", cta2_label="View on GitHub",
 flag="&#127482;&#127480;", country="USA", founded="2023", hq="United States",
 rating=4.3, date="2026-09-06",
 badges=["Local RAG", "Desktop + Server", "Open Source"],
 quick_stats=[("Workspaces", "Core Concept"), ("Desktop + Docker", "Deployment"),
              ("On-device", "Option"), ("Free", "Open Source"), ("2023", "Founded")],
 title="AnythingLLM Review 2026: Private RAG Over Your Own Documents | TechVernia",
 meta_desc="AnythingLLM review 2026. Turn your own documents into a private, queryable "
           "knowledge base that runs on your machine or your server. Workspaces, "
           "embedded vector store, limits and verdict.",
 meta_keywords="AnythingLLM review, private RAG, chat with documents locally, on-device "
               "AI, local knowledge base, AnythingLLM vs Open WebUI",
 overview=[
  "AnythingLLM answers a question a lot of small organisations have and few tools answer well: how do "
  "we make our own documents queryable without handing them to anyone? It bundles document ingestion, "
  "embedding, a vector store and a chat interface into one application that runs on a laptop or a "
  "server. There is no pipeline to assemble and no vector database to procure.",
  "The organising idea is the workspace. Each workspace has its own documents and its own "
  "conversational context, so the contract archive, the engineering documentation and the HR handbook "
  "stay separate instead of blending into one confused index. It is a small design decision that "
  "makes the difference between a demo and something a team keeps using after month two.",
  "It ships in two shapes: a desktop application for individuals that can run entirely on-device, and "
  "a Docker deployment for teams. Both are open source. The retrieval quality will not match a "
  "purpose-built stack tuned by someone who does this for a living, but it is a fraction of the "
  "effort and it keeps everything inside your walls.",
 ],
 features=[
  ("layers", "Workspace Isolation",
   "Separate document sets and conversation contexts per workspace, so different bodies of knowledge "
   "do not contaminate each other."),
  ("database", "Embedded Vector Store",
   "Vector storage is included. No separate database to procure, deploy or pay for on the way to a "
   "working system."),
  ("book", "Broad Document Ingestion",
   "PDFs, Office documents, text, web pages and more, handled by the application rather than by a "
   "preprocessing script you maintain."),
  ("lock", "Fully On-Device Option",
   "The desktop application can run with local models and local embeddings, so documents never leave "
   "the machine at all."),
  ("users", "Multi-User Server Mode",
   "The Docker deployment adds accounts and permissions for teams that have outgrown the desktop app."),
  ("link", "Flexible Model Backends",
   "Works with local models or hosted APIs, so you can start hosted and move local, or split by "
   "workspace sensitivity."),
 ],
 pros=[
  "Complete private RAG stack in one install — no assembly required",
  "Workspace model keeps different knowledge bases genuinely separate",
  "Runs fully on-device for confidential material",
  "Open source with both desktop and server deployments",
  "Free",
 ],
 cons=[
  "Retrieval quality trails a purpose-built, tuned RAG stack",
  "Large document collections strain the embedded vector store",
  "Fewer tuning controls than assembling the pieces yourself",
  "Smaller community than Open WebUI",
 ],
 pricing=[
  ("Desktop", "Free", "Full application, on-device, unlimited documents"),
  ("Self-Hosted", "Free", "Docker deployment with multi-user support"),
  ("Cloud", "Subscription", "Hosted option for teams that do not want to self-host"),
 ],
 excels=[
  "Making contracts, policies or documentation queryable without a vendor",
  "Consultants and small firms handling client-confidential material",
  "Getting a private RAG system working in an afternoon",
  "Separating multiple distinct knowledge bases cleanly",
 ],
 not_ideal=[
  "Very large corpora where a dedicated vector database is required",
  "Teams needing fine-grained retrieval tuning",
  "Organisations wanting a commercial support contract",
 ],
 comparisons=[
  ("AnythingLLM vs Open WebUI",
   "AnythingLLM is better at the document workspace experience; Open WebUI is better at multi-user "
   "administration and backend flexibility. If documents are the point, start here. If team access "
   "control is the point, start there."),
  ("AnythingLLM vs a custom RAG stack",
   "A custom stack with a dedicated vector database gives better retrieval and full control, at the "
   "cost of weeks of work and ongoing maintenance. AnythingLLM gets you eighty per cent of the value "
   "in an afternoon, which is the right trade for most small organisations."),
 ],
 verdict="AnythingLLM is the pragmatic choice for private document intelligence at small scale. It "
         "removes the entire assembly problem — no vector database to choose, no embedding pipeline "
         "to write, no orchestration framework to learn — and the workspace model keeps things "
         "organised as you add more material. Retrieval is good rather than excellent, and very large "
         "corpora will outgrow it. For a firm that wants to ask questions of its own contracts "
         "without those contracts leaving the building, it is hard to beat for the effort involved.",
 faq=[
  ("Can AnythingLLM run entirely offline?",
   "Yes. The desktop application can use local models and local embeddings, keeping documents and "
   "queries entirely on your machine."),
  ("Do I need a separate vector database?",
   "No. Vector storage is embedded in the application, which is the main reason it is quick to get "
   "running. Very large collections may eventually justify a dedicated database."),
  ("What document types does it handle?",
   "PDFs, Office documents, plain text, web pages and more, with ingestion handled by the application "
   "rather than by scripts you maintain."),
  ("How is it different from Open WebUI?",
   "AnythingLLM centres on the document workspace; Open WebUI centres on multi-user chat "
   "administration with RAG attached. Choose based on which of those is your actual problem."),
 ],
 breakdown=[("Setup Speed", 9.4), ("Privacy", 9.6),
            ("Retrieval Quality", 7.6), ("Scalability", 6.8), ("Value", 9.3)],
 related=[("open-webui", "Open WebUI", "4.5", "Self-Hosted AI Interface"),
          ("jan", "Jan", "4.4", "Open-Source Local AI"),
          ("qdrant", "Qdrant", "4.7", "Vector Database")],
),

dict(LL,
 slug="vllm", name="vLLM", company="vLLM Project",
 domain="vllm.ai", url="https://docs.vllm.ai/en/latest/",
 cta2_url="https://github.com/vllm-project/vllm", cta2_label="View on GitHub",
 flag="&#127482;&#127480;", country="Community", founded="2023", hq="UC Berkeley origin / open source",
 rating=4.7, date="2026-09-06",
 badges=["Production Serving", "PagedAttention", "Apache 2.0"],
 quick_stats=[("PagedAttention", "Core Innovation"), ("Apache 2.0", "Licence"),
              ("OpenAI-compatible", "Server"), ("Multi-GPU", "Scaling"), ("2023", "First Release")],
 title="vLLM Review 2026: The Standard Engine for Serving LLMs | TechVernia",
 meta_desc="vLLM review 2026. The open-source inference engine behind most self-hosted "
           "LLM deployments: PagedAttention, continuous batching, multi-GPU serving and "
           "an OpenAI-compatible API. When you need it and when you do not.",
 meta_keywords="vLLM review, LLM inference engine, PagedAttention, self-hosted model "
               "serving, continuous batching, vLLM vs Ollama",
 overview=[
  "vLLM is the engine, not the application. When an organisation decides to serve an open-weight "
  "model to real users at real volume, this is overwhelmingly what runs underneath — the layer that "
  "turns a set of model weights into an endpoint that can answer thousands of concurrent requests "
  "without falling over or wasting most of the GPU it is running on.",
  "Its reputation rests on PagedAttention, a memory-management technique borrowed conceptually from "
  "operating system virtual memory. Naive inference servers waste enormous amounts of GPU memory on "
  "fragmented key-value cache; PagedAttention allocates it in pages, which raises the number of "
  "concurrent requests a given GPU can serve by a large multiple. Continuous batching does the "
  "complementary job on the scheduling side, keeping the GPU fed rather than idling between requests.",
  "It is emphatically infrastructure. There is no interface, no model browser, no chat window — you "
  "get an OpenAI-compatible API server and a set of flags, and you are expected to know what you are "
  "doing with GPUs. That is the correct design for what it is, and it is why the recommendation is "
  "sharply bimodal: essential if you are serving a model to many users, entirely unnecessary if you "
  "are not.",
 ],
 features=[
  ("cpu", "PagedAttention Memory Management",
   "Allocates key-value cache in pages rather than contiguous blocks, dramatically raising the "
   "concurrent requests a single GPU can handle."),
  ("zap", "Continuous Batching",
   "Requests join and leave batches dynamically instead of waiting for a batch boundary, which keeps "
   "the GPU busy and latency predictable under load."),
  ("link", "OpenAI-Compatible Server",
   "Exposes the OpenAI API shape, so existing clients and tooling work against your self-hosted "
   "model without a rewrite."),
  ("layers", "Multi-GPU and Distributed Serving",
   "Tensor and pipeline parallelism for models too large for one card, which is most frontier "
   "open-weight models in 2026."),
  ("git", "Apache 2.0 Licence",
   "Permissive licensing with no commercial restrictions, which matters for products built on top."),
  ("check", "Broad Model Support",
   "Supports the major open-weight families quickly after release, so new models are usually "
   "deployable within days."),
 ],
 pros=[
  "Order-of-magnitude better GPU utilisation than naive serving",
  "The de-facto standard, so documentation and deployment recipes are everywhere",
  "OpenAI-compatible API means no client rewrites",
  "Apache 2.0 with no commercial restrictions",
  "New open-weight models are supported quickly",
 ],
 cons=[
  "Requires real GPU and distributed systems knowledge",
  "No user interface at all — it is infrastructure",
  "Configuration and tuning have a steep learning curve",
  "Complete overkill for single-user local inference",
 ],
 pricing=[
  ("Open Source", "Free", "Apache 2.0, self-hosted; you pay for GPUs"),
 ],
 excels=[
  "Serving an open-weight model to many concurrent users",
  "Cutting inference cost versus per-token hosted APIs at volume",
  "Deployments where model weights must stay on your infrastructure",
  "Backing a self-hosted platform such as Open WebUI at team scale",
 ],
 not_ideal=[
  "Single-user local inference — LM Studio or Ollama are the right tools",
  "Teams without GPU infrastructure expertise",
  "Low request volumes where a hosted API is cheaper all-in",
 ],
 comparisons=[
  ("vLLM vs Ollama",
   "Ollama is for running a model on your machine; vLLM is for serving a model to your users. They "
   "are not alternatives — most teams end up using Ollama locally and vLLM in production."),
  ("vLLM vs a hosted API",
   "Below a certain volume, a hosted API is cheaper once you count GPU rental and engineering time. "
   "Above it, vLLM wins decisively — which is why cost modelling should come before the deployment "
   "decision, not after."),
 ],
 verdict="vLLM is the correct answer to a specific question: how do we serve an open-weight model in "
         "production without wasting most of our GPU budget? PagedAttention and continuous batching "
         "are genuine engineering advances, not marketing, and the resulting utilisation gap over "
         "naive serving is what makes self-hosting economically viable at all. It demands real "
         "infrastructure competence and gives you nothing resembling a product. Model the cost "
         "against a hosted API honestly before committing — including engineer time — and if "
         "self-hosting wins, this is what you run.",
 faq=[
  ("What is PagedAttention?",
   "A memory management technique that allocates the attention key-value cache in pages rather than "
   "contiguous blocks, borrowed conceptually from operating system virtual memory. It substantially "
   "increases how many concurrent requests one GPU can serve."),
  ("Do I need vLLM to run a local model?",
   "No. For single-user local use, LM Studio or Ollama are far simpler. vLLM is for serving many "
   "concurrent users."),
  ("Is vLLM free for commercial use?",
   "Yes. It is Apache 2.0 licensed with no commercial restrictions. Your costs are GPUs and "
   "engineering time."),
  ("Does vLLM work with existing OpenAI SDK code?",
   "Yes. It exposes an OpenAI-compatible API server, so most clients work by changing the base URL."),
 ],
 breakdown=[("Throughput", 9.8), ("GPU Efficiency", 9.7),
            ("Model Coverage", 9.2), ("Ease of Use", 5.5), ("Value", 9.5)],
 related=[("open-webui", "Open WebUI", "4.5", "Self-Hosted AI Interface"),
          ("lm-studio", "LM Studio", "4.6", "Local LLM Desktop App"),
          ("jan", "Jan", "4.4", "Open-Source Local AI")],
),

dict(DA,
 slug="pinecone", name="Pinecone", company="Pinecone Systems",
 domain="pinecone.io", url="https://www.pinecone.io/",
 cta2_url="https://app.pinecone.io/", cta2_label="Start Free",
 flag="&#127482;&#127480;", country="USA", founded="2019", hq="New York, New York, USA",
 rating=4.5, date="2026-09-06",
 badges=["Fully Managed", "Serverless", "Category Leader"],
 quick_stats=[("Serverless", "Architecture"), ("Managed", "No ops"),
              ("Free tier", "Entry"), ("Hybrid search", "Supported"), ("2019", "Founded")],
 title="Pinecone Review 2026: The Managed Vector Database | TechVernia",
 meta_desc="Pinecone review 2026. The fully managed vector database for production RAG: "
           "serverless scaling, hybrid search, metadata filtering and zero operations. "
           "Pricing model, lock-in risk and how it compares to Qdrant.",
 meta_keywords="Pinecone review, vector database, managed vector search, RAG "
               "infrastructure, Pinecone vs Qdrant, serverless vector DB",
 overview=[
  "Pinecone is the vector database that made vector databases a normal purchase. It is fully managed "
  "and serverless: you send vectors, you query them, and at no point do you think about shards, "
  "replicas, index rebuilds or what happens when a node dies. For teams whose actual product is the "
  "application rather than the retrieval infrastructure, that is the entire proposition and it is a "
  "strong one.",
  "Beyond raw similarity search, the features that matter in production are metadata filtering and "
  "hybrid search. Filtering by tenant, document type or date at query time is what makes "
  "multi-tenant RAG safe; combining dense vectors with sparse keyword matching is what stops "
  "retrieval failing on exact terms — product codes, error identifiers, names — that embeddings "
  "handle poorly. Both are first-class rather than bolted on.",
  "The trade-offs are the ones any managed proprietary service carries. Consumption-based pricing is "
  "hard to forecast before you have production traffic and has a habit of surprising teams as usage "
  "grows. Your vectors live on Pinecone's infrastructure, which is a data residency conversation in "
  "regulated sectors. And there is no self-hosted option, so migration means a real project rather "
  "than a config change.",
 ],
 features=[
  ("cube", "Serverless Architecture",
   "Capacity scales with usage and you pay for what you consume rather than provisioning clusters "
   "against a traffic guess."),
  ("search", "Hybrid Search",
   "Dense vector similarity combined with sparse keyword matching, which fixes the classic RAG "
   "failure on exact identifiers and product codes."),
  ("layers", "Metadata Filtering",
   "Filter by tenant, type or date at query time — the mechanism that makes multi-tenant retrieval "
   "safe rather than hopeful."),
  ("zap", "Low-Latency Queries",
   "Consistent query latency at scale without tuning, which is the practical benefit of someone else "
   "operating the index."),
  ("check", "Namespaces",
   "Logical partitioning inside an index for clean separation between customers or document sets."),
  ("link", "Broad Framework Integration",
   "First-class support across the common orchestration frameworks, so it drops into an existing "
   "pipeline quickly."),
 ],
 pros=[
  "Zero operational burden — genuinely no infrastructure to run",
  "Hybrid search and metadata filtering are production-grade",
  "Scales without capacity planning",
  "Mature integrations across the RAG ecosystem",
  "Free tier is adequate for prototyping",
 ],
 cons=[
  "Consumption pricing is hard to forecast and grows quickly",
  "No self-hosted option — your vectors live on their infrastructure",
  "Proprietary, so migration away is a project",
  "Overkill for small collections a simpler store would handle",
 ],
 pricing=[
  ("Starter", "Free", "Limited storage and queries for prototyping"),
  ("Standard", "Usage-based", "Production workloads billed on storage, reads and writes"),
  ("Enterprise", "Custom", "Higher limits, compliance controls, dedicated support"),
 ],
 excels=[
  "Production RAG where nobody wants to operate a database",
  "Multi-tenant applications needing metadata isolation",
  "Workloads with unpredictable or spiky query volume",
  "Teams that need to ship retrieval, not run infrastructure",
 ],
 not_ideal=[
  "Regulated data that cannot leave your own infrastructure",
  "Small collections where an embedded store is sufficient",
  "Cost-sensitive high-volume workloads",
 ],
 comparisons=[
  ("Pinecone vs Qdrant",
   "Qdrant is open source and self-hostable with excellent performance and a managed cloud option; "
   "Pinecone is managed-only with a more mature ecosystem. If data residency or cost control matters, "
   "Qdrant. If shipping speed matters most, Pinecone."),
  ("Pinecone vs pgvector",
   "If you already run PostgreSQL and your collection is modest, pgvector avoids a new system "
   "entirely and keeps vectors next to your relational data. Pinecone earns its place at scale, "
   "where a general-purpose database starts to struggle."),
 ],
 verdict="Pinecone is the right choice when your constraint is engineering time rather than budget or "
         "data residency. The managed serverless model genuinely removes vector infrastructure from "
         "your problem list, and hybrid search plus metadata filtering are the two features that "
         "separate a production retrieval system from a demo. Go in with a cost model, because "
         "consumption pricing surprises teams as they scale, and understand that there is no "
         "self-hosted escape hatch. If either of those is a blocker, Qdrant is the alternative worth "
         "evaluating first.",
 faq=[
  ("Can Pinecone be self-hosted?",
   "No. It is managed-only, which is both the product's main advantage and its main limitation. Teams "
   "needing on-premise deployment should look at Qdrant or Weaviate."),
  ("What is hybrid search and why does it matter?",
   "Combining dense vector similarity with sparse keyword matching. It fixes the common RAG failure "
   "where a query containing an exact product code or error identifier retrieves semantically similar "
   "but wrong documents."),
  ("How does Pinecone pricing work?",
   "Consumption-based on storage, reads and writes, with a free starter tier. Model your expected "
   "query volume before committing, as costs scale faster than teams typically expect."),
  ("Do I need a vector database at all?",
   "Not always. For small collections, pgvector inside an existing PostgreSQL database or an embedded "
   "store is simpler and cheaper. A dedicated vector database earns its place at scale."),
 ],
 breakdown=[("Ease of Operation", 9.8), ("Query Performance", 9.2),
            ("Feature Depth", 8.8), ("Cost Predictability", 6.5), ("Data Control", 5.5)],
 related=[("qdrant", "Qdrant", "4.7", "Open-Source Vector DB"),
          ("weaviate", "Weaviate", "4.5", "AI-Native Database"),
          ("firecrawl", "Firecrawl", "4.6", "Web-to-LLM Context API")],
),

dict(DA,
 slug="qdrant", name="Qdrant", company="Qdrant",
 domain="qdrant.tech", url="https://qdrant.tech/",
 cta2_url="https://cloud.qdrant.io/", cta2_label="Try Qdrant Cloud",
 flag="&#127465;&#127466;", country="Germany", founded="2021", hq="Berlin, Germany",
 rating=4.7, date="2026-09-06",
 badges=["Open Source", "Rust Built", "Self-Hostable"],
 quick_stats=[("Rust", "Written In"), ("Apache 2.0", "Licence"),
              ("Self-host + Cloud", "Deployment"), ("MCP", "Agent Memory"), ("2021", "Founded")],
 title="Qdrant Review 2026: The Open-Source Vector Database | TechVernia",
 meta_desc="Qdrant review 2026. The Rust-built open-source vector database powering "
           "agent memory across frameworks: filtering, quantisation, self-hosting and "
           "an MCP server. Performance, deployment options and verdict.",
 meta_keywords="Qdrant review, open source vector database, Rust vector search, agent "
               "memory, Qdrant vs Pinecone, self-hosted vector DB",
 overview=[
  "Qdrant is the vector database for teams who want production performance without surrendering "
  "control of their data. It is written in Rust, Apache 2.0 licensed, and runs either on your own "
  "infrastructure or in a managed cloud — and crucially the self-hosted version is the real product "
  "rather than a crippled community edition designed to push you toward the paid tier.",
  "Two engineering choices define it. Filtering is integrated into the vector search itself rather "
  "than applied afterwards, which avoids the common failure where a heavily filtered query returns "
  "far fewer results than requested because the filter was applied to an already-truncated candidate "
  "set. And quantisation options let you trade a small amount of accuracy for dramatic memory "
  "reductions, which is often the difference between one server and five.",
  "In 2026 Qdrant has become one of the default memory layers for agent frameworks, largely through "
  "its MCP server: agents can store and recall semantically similar context as a native tool call. "
  "That positioning — infrastructure that agent frameworks assume rather than integrate with — is "
  "quietly the strongest thing about it.",
 ],
 features=[
  ("cpu", "Rust Performance",
   "Written in Rust for predictable memory behaviour and throughput, without the garbage collection "
   "pauses that complicate latency-sensitive serving."),
  ("search", "Filterable Vector Search",
   "Filters are applied inside the search rather than after it, so a heavily filtered query still "
   "returns the number of results you asked for."),
  ("layers", "Quantisation",
   "Scalar and binary quantisation trade a little accuracy for large memory savings — frequently the "
   "difference between one machine and a cluster."),
  ("git", "Apache 2.0 Open Source",
   "The self-hosted version is the real product, not a limited edition designed to push you to a "
   "paid tier."),
  ("link", "MCP Server for Agent Memory",
   "Exposed over the Model Context Protocol, which is why it turns up as the memory layer across "
   "agent frameworks in 2026."),
  ("cube", "Cloud or Self-Hosted",
   "Managed Qdrant Cloud when you want it, your own servers when you need it, same engine either way."),
 ],
 pros=[
  "Open source with no meaningful self-hosted limitations",
  "Excellent performance and predictable memory behaviour",
  "Filtering that actually works correctly under load",
  "Quantisation substantially cuts infrastructure cost",
  "MCP support makes it a first-class agent memory layer",
 ],
 cons=[
  "Self-hosting means you own operations, backups and upgrades",
  "Smaller ecosystem than Pinecone in some frameworks",
  "Tuning quantisation and indexing requires understanding the trade-offs",
  "Cloud pricing is competitive but not the cheapest option",
 ],
 pricing=[
  ("Open Source", "Free", "Apache 2.0, self-hosted, no feature restrictions"),
  ("Cloud Free", "$0", "Small managed cluster for evaluation"),
  ("Cloud", "Usage-based", "Managed clusters sized to your workload"),
  ("Hybrid Cloud", "Custom", "Managed control plane over your own infrastructure"),
 ],
 excels=[
  "Production RAG where data must stay on your infrastructure",
  "Agent memory via MCP across frameworks",
  "Cost-sensitive workloads where quantisation pays for itself",
  "Multi-tenant retrieval needing correct filtered results",
 ],
 not_ideal=[
  "Teams with no capacity to operate a database",
  "Very small collections where an embedded store suffices",
  "Organisations that specifically want a single managed vendor",
 ],
 comparisons=[
  ("Qdrant vs Pinecone",
   "Pinecone removes operations entirely; Qdrant gives you data control, a genuine open-source "
   "licence and lower cost at scale. For regulated data or cost-sensitive volume, Qdrant. For "
   "shipping fastest with the smallest team, Pinecone."),
  ("Qdrant vs Weaviate",
   "Both are open source and strong. Weaviate bundles more AI-native features such as built-in "
   "vectorisation modules; Qdrant is leaner and focused on being an excellent vector engine. Qdrant "
   "if you want a fast component, Weaviate if you want more of the stack included."),
 ],
 verdict="Qdrant is the vector database recommendation for most engineering teams in 2026. It is "
         "genuinely open source, fast, and gets the details right — particularly filtering, where "
         "several competitors quietly return wrong result counts under filtered load. Quantisation "
         "makes real infrastructure savings, and the MCP server has made it the default memory layer "
         "for agent work. The cost is that self-hosting is your responsibility. If your team can "
         "operate a database, this is the one to operate; if not, the managed cloud is competitive "
         "and you keep the option to move.",
 faq=[
  ("Is Qdrant free?",
   "The self-hosted version is Apache 2.0 licensed and free, with no feature restrictions. Qdrant "
   "Cloud is a paid managed service with a free evaluation tier."),
  ("Why does filtering matter in a vector database?",
   "Systems that filter after searching can return far fewer results than requested, because the "
   "filter is applied to an already-truncated candidate set. Qdrant filters inside the search, so "
   "filtered queries return correct results."),
  ("What is quantisation used for?",
   "Compressing vectors to reduce memory use, trading a small amount of accuracy for large "
   "infrastructure savings. It frequently determines whether a workload needs one server or several."),
  ("Can agents use Qdrant as memory?",
   "Yes. Qdrant ships an MCP server, so agent frameworks can store and recall semantically similar "
   "context as a native tool call — one of the main reasons for its 2026 adoption."),
 ],
 breakdown=[("Performance", 9.5), ("Openness", 9.7),
            ("Filtering Correctness", 9.6), ("Operational Burden", 7.0), ("Value", 9.4)],
 related=[("pinecone", "Pinecone", "4.5", "Managed Vector DB"),
          ("weaviate", "Weaviate", "4.5", "AI-Native Database"),
          ("mem0", "Mem0", "4.4", "Agent Memory Layer")],
),

]
