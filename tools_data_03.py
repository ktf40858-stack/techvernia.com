# -*- coding: utf-8 -*-
"""Lot 3 - Agents de code (coding/) et LLM local (local-llm/)."""

CO = dict(category="coding", cat_href="../../categories/ai-coding.html",
          cat_label="AI Coding", app_category="DeveloperApplication")
LL = dict(category="local-llm", cat_href="../../categories.html",
          cat_label="Local LLM Tools", app_category="DeveloperApplication")

TOOLS = [

dict(CO,
 slug="openai-codex", name="OpenAI Codex", company="OpenAI",
 domain="openai.com", url="https://openai.com/codex/",
 cta2_url="https://developers.openai.com/codex/", cta2_label="Read the Docs",
 flag="&#127482;&#127480;", country="USA", founded="2015", hq="San Francisco, California, USA",
 rating=4.4, date="2026-09-06",
 badges=["OpenAI Native", "Cloud + CLI", "Included in ChatGPT"],
 quick_stats=[("Cloud + CLI + IDE", "Surfaces"), ("GPT", "Models"),
              ("ChatGPT plans", "Included"), ("Sandboxed", "Execution"), ("2015", "OpenAI Founded")],
 title="OpenAI Codex Review 2026: The Coding Agent Inside ChatGPT | TechVernia",
 meta_desc="OpenAI Codex review 2026. OpenAI's coding agent across cloud, CLI and IDE, "
           "bundled with ChatGPT plans. Sandboxed execution, parallel tasks, real "
           "limits and how it stacks up against Claude Code and Cursor.",
 meta_keywords="OpenAI Codex review, ChatGPT coding agent, Codex CLI, AI pair "
               "programmer, Codex vs Claude Code",
 overview=[
  "Codex is OpenAI's coding agent, and its defining characteristic is that most of its users did not "
  "go looking for it. It comes bundled with ChatGPT paid plans, which means a very large population "
  "of developers already has a capable coding agent sitting behind a subscription they bought for "
  "something else. Distribution beats marketing, and Codex has it.",
  "It runs across three surfaces: a cloud environment where tasks execute in a sandbox against your "
  "repository, a CLI for people who live in the terminal, and IDE integration. The cloud surface is "
  "the distinctive one — you delegate a task, it works in an isolated container, and you review a "
  "diff when it is done. Several tasks can run in parallel, which changes the interaction model from "
  "pair programming to something closer to reviewing junior work.",
  "The sandbox is the underrated safety feature. Code executes in an isolated environment with "
  "controlled network access rather than directly on your machine, which is a meaningfully different "
  "risk profile from agents that run shell commands against your working directory. For teams "
  "nervous about autonomous agents touching a real filesystem, that isolation is the argument.",
 ],
 features=[
  ("cube", "Sandboxed Cloud Execution",
   "Tasks run in isolated containers against a copy of your repository, with controlled network "
   "access, rather than executing shell commands on your laptop."),
  ("layers", "Parallel Task Delegation",
   "Hand off several independent pieces of work at once and review the resulting diffs, instead of "
   "supervising one conversation at a time."),
  ("terminal", "CLI and IDE Surfaces",
   "The same agent is reachable from the terminal and inside the editor, so the workflow does not "
   "depend on staying in a browser tab."),
  ("check", "Diff-First Review",
   "Output arrives as a reviewable change set, which fits normal code review habits rather than "
   "asking you to trust an agent's summary."),
  ("git", "Repository Awareness",
   "Works against your actual repository structure, tests and conventions rather than isolated "
   "snippets pasted into a chat."),
  ("users", "Bundled with ChatGPT Plans",
   "Included with paid ChatGPT tiers, so for many teams the marginal cost of trying it is zero."),
 ],
 pros=[
  "Already included with ChatGPT paid plans — near-zero adoption friction",
  "Sandboxed execution is a genuinely safer model than local shell access",
  "Parallel task delegation suits reviewing rather than supervising",
  "Backed by OpenAI, so continuity risk is low",
  "Diff-first output fits existing code review process",
 ],
 cons=[
  "Locked to OpenAI models — no bring-your-own-model option",
  "Sandbox isolation limits tasks needing unusual local tooling",
  "Weaker than the best agents on very large, sprawling codebases",
  "Usage limits on lower ChatGPT tiers bite quickly on real work",
 ],
 pricing=[
  ("ChatGPT Plus", "$20 / month", "Codex access with standard usage limits"),
  ("ChatGPT Pro", "$200 / month", "Substantially higher limits for heavy agent use"),
  ("ChatGPT Business", "From $25 / user / month", "Team administration and shared workspace"),
  ("API", "Usage-based", "Programmatic access billed per token"),
 ],
 excels=[
  "Teams already paying for ChatGPT who want a coding agent for free",
  "Delegating well-specified, independent tasks in parallel",
  "Organisations that prefer sandboxed execution over local shell access",
  "Reviewing agent work as diffs rather than watching it type",
 ],
 not_ideal=[
  "Teams with model procurement constraints ruling out OpenAI",
  "Very large monorepos where context limits show",
  "Workflows needing unusual local toolchains inside the sandbox",
 ],
 comparisons=[
  ("OpenAI Codex vs Claude Code",
   "Claude Code generally leads on large-codebase reasoning and agentic depth, and is the tool most "
   "2026 rankings put first. Codex's advantages are the sandbox and the fact that it is already "
   "included in a subscription many teams hold. Try Codex first because it costs nothing extra; "
   "reach for Claude Code when the task is genuinely hard."),
  ("OpenAI Codex vs OpenCode",
   "Codex is polished and locked to OpenAI models; OpenCode is rough and works with anything. The "
   "decision is almost entirely about whether model choice and data path are constraints for you."),
 ],
 verdict="Codex is the coding agent most teams should evaluate first, not because it is the best but "
         "because they are already paying for it. The sandboxed cloud execution model is genuinely "
         "well designed — isolating agent work from your actual machine is the right default, and "
         "reviewing diffs fits how software teams already operate. Where it falls behind is deep "
         "reasoning over large codebases, and there is no way around the OpenAI model lock-in. Use it "
         "for well-specified, parallelisable work, and keep a stronger agent for the tasks that "
         "require understanding an entire system.",
 faq=[
  ("Do I need to pay extra for Codex?",
   "No. Codex is included with paid ChatGPT plans. Usage limits vary by tier, and heavy agent work "
   "hits the lower tiers' limits quickly."),
  ("Where does Codex run my code?",
   "In sandboxed cloud containers with controlled network access, working against a copy of your "
   "repository — not directly on your local machine."),
  ("Can Codex use models other than OpenAI's?",
   "No. That is the main structural trade-off compared with open agents like OpenCode, which let you "
   "bring any model."),
  ("Is Codex the same as the old Codex model from 2021?",
   "No. The name is reused. The 2021 Codex was a code-generation model behind early Copilot; the "
   "current Codex is an agentic coding product spanning cloud, CLI and IDE."),
 ],
 breakdown=[("Code Quality", 8.6), ("Execution Safety", 9.3),
            ("Large Codebase Reasoning", 7.8), ("Model Flexibility", 4.0), ("Value", 9.0)],
 related=[("opencode", "OpenCode", "4.6", "Open-Source Coding Agent"),
          ("cursor", "Cursor", "4.7", "AI-First Code Editor"),
          ("github-copilot", "GitHub Copilot", "4.6", "IDE Coding Assistant")],
),

dict(CO,
 slug="google-antigravity", name="Google Antigravity", company="Google",
 domain="antigravity.google", url="https://antigravity.google/",
 cta2_url="https://antigravity.google/", cta2_label="Get Started",
 flag="&#127482;&#127480;", country="USA", founded="1998", hq="Mountain View, California, USA",
 rating=4.2, date="2026-09-06",
 badges=["Agent-First IDE", "Gemini Powered", "New in 2026"],
 quick_stats=[("Agent-first", "Design"), ("Gemini", "Models"),
              ("2026", "Launch Year"), ("Free tier", "Entry"), ("Google", "Vendor")],
 title="Google Antigravity Review 2026: The Agent-First Development Platform | TechVernia",
 meta_desc="Google Antigravity review 2026. Google's agent-first development platform "
           "built around Gemini: a mission-control surface for parallel coding agents "
           "rather than an editor with autocomplete. Strengths, gaps and verdict.",
 meta_keywords="Google Antigravity review, agent-first IDE, Gemini coding agent, "
               "Antigravity vs Cursor, AI development platform",
 overview=[
  "Antigravity is Google's answer to a question most AI coding tools avoid: what should the "
  "development environment look like if agents, not humans, write most of the code? The conventional "
  "answer has been to bolt an assistant onto an editor. Antigravity starts from the other end — the "
  "primary surface is closer to mission control for a set of agents working in parallel than to a "
  "text editor with suggestions.",
  "That reframing is the product's whole reason to exist. You dispatch work, watch agents progress "
  "across tasks, inspect what each one did and why, and intervene where needed. The editor is still "
  "there when you need to write code yourself, but it is no longer the centre of gravity. For "
  "developers who have already shifted to reviewing agent output more than typing, the layout matches "
  "how they actually work.",
  "It is new, and it shows. The agent-first model is unfamiliar enough that the learning curve is "
  "real, the ecosystem around it is thin compared with a mature editor, and Google's history with "
  "developer products means reasonable people will wait to see whether it is still here in two years. "
  "It is genuinely worth trying, and it is not yet where you should move a team's daily work.",
 ],
 features=[
  ("layers", "Agent Mission Control",
   "The primary interface manages multiple agents working in parallel rather than presenting a single "
   "file with suggestions in the margin."),
  ("brain", "Gemini Models Throughout",
   "Built on Gemini, with the long context windows that make whole-repository reasoning practical."),
  ("eye", "Agent Trace Inspection",
   "See what each agent did and why, which is the difference between trusting agent output and "
   "auditing it."),
  ("git", "Repository-Level Tasks",
   "Work is dispatched at the level of a task against a codebase rather than a prompt against a file."),
  ("terminal", "Integrated Editor",
   "A conventional editing surface is still available for the work you want to do yourself."),
  ("check", "Review-Centred Workflow",
   "The workflow assumes you approve and refine agent output, which is the honest description of how "
   "most agentic coding actually goes."),
 ],
 pros=[
  "The most coherent attempt yet at an agent-first development environment",
  "Gemini's long context makes whole-repository reasoning realistic",
  "Agent traces make output auditable rather than magical",
  "Free tier lets you evaluate it properly",
  "Google resources behind it",
 ],
 cons=[
  "Genuinely new — rough edges and a shifting feature set",
  "Thin ecosystem compared with established editors",
  "Real learning curve: the mental model is unfamiliar",
  "Google's record on sustaining developer products invites caution",
 ],
 pricing=[
  ("Free", "$0", "Evaluation access with usage limits"),
  ("Google AI Pro", "$19.99 / month", "Higher limits and expanded model access"),
  ("Google AI Ultra", "$249.99 / month", "Highest limits and earliest feature access"),
 ],
 excels=[
  "Developers who already delegate most coding to agents",
  "Parallel work across several independent tasks",
  "Teams standardised on Gemini models",
  "Anyone wanting to see where agentic development environments are heading",
 ],
 not_ideal=[
  "Teams that need a stable, mature daily editor now",
  "Developers who want incremental AI assistance rather than delegation",
  "Organisations that cannot use Google models",
 ],
 comparisons=[
  ("Google Antigravity vs Cursor",
   "Cursor is a mature editor that added excellent agents; Antigravity is an agent platform that "
   "includes an editor. Cursor is the safer choice for daily work today. Antigravity is the more "
   "interesting bet on where the category is going."),
  ("Google Antigravity vs Gemini CLI",
   "Same models, opposite ergonomics. Gemini CLI is a terminal agent that fits into existing "
   "workflows; Antigravity asks you to adopt a new surface. Start with the CLI, graduate to "
   "Antigravity if parallel agent management is genuinely your bottleneck."),
 ],
 verdict="Antigravity is the most intellectually honest product in the agentic coding field: it "
         "accepts that if agents write most of the code, the environment should be built for managing "
         "agents rather than for typing. The mission-control surface and trace inspection are the "
         "right ideas. It is also new, unfinished, and from a company whose developer product "
         "graveyard is well populated. Try it on a side project to understand where this category is "
         "going. Do not move your team onto it until it has a couple more releases and a clearer "
         "commitment behind it.",
 faq=[
  ("What makes Antigravity different from an AI code editor?",
   "The primary surface manages multiple agents working in parallel rather than presenting a file "
   "with inline suggestions. The editor is a component, not the centre."),
  ("Is Antigravity free?",
   "There is a free tier with usage limits. Higher limits come with Google AI Pro and AI Ultra "
   "subscriptions."),
  ("Which models does it use?",
   "Gemini models. There is no bring-your-own-model path, so it is a fit only if Gemini works for "
   "your organisation."),
  ("Should I switch from Cursor to Antigravity?",
   "Not yet for daily production work. Cursor is mature and stable; Antigravity is new and shifting. "
   "Run it alongside on a side project first."),
 ],
 breakdown=[("Agent Orchestration", 9.0), ("Context Handling", 8.8),
            ("Auditability", 8.5), ("Maturity", 6.0), ("Ecosystem", 5.8)],
 related=[("cursor", "Cursor", "4.7", "AI-First Code Editor"),
          ("gemini-cli", "Gemini CLI", "4.3", "Terminal Coding Agent"),
          ("windsurf", "Windsurf", "4.5", "Agentic IDE")],
),

dict(CO,
 slug="gemini-cli", name="Gemini CLI", company="Google",
 domain="github.com/google-gemini/gemini-cli", url="https://github.com/google-gemini/gemini-cli",
 cta2_url="https://github.com/google-gemini/gemini-cli", cta2_label="Install from GitHub",
 flag="&#127482;&#127480;", country="USA", founded="1998", hq="Mountain View, California, USA",
 rating=4.3, date="2026-09-06",
 badges=["Open Source", "Generous Free Tier", "Terminal Agent"],
 quick_stats=[("Apache 2.0", "Licence"), ("Terminal", "Interface"),
              ("Gemini", "Models"), ("Free tier", "With Google account"), ("Google", "Vendor")],
 title="Gemini CLI Review 2026: Google's Open-Source Terminal Coding Agent | TechVernia",
 meta_desc="Gemini CLI review 2026. Google's open-source terminal AI agent: Apache 2.0 "
           "licensed, a genuinely generous free tier with a Google account, and long "
           "context. How it compares to Claude Code and OpenCode.",
 meta_keywords="Gemini CLI review, terminal AI agent, open source coding agent, Google "
               "Gemini CLI free tier, Gemini CLI vs Claude Code",
 overview=[
  "Gemini CLI is Google's terminal coding agent, and its most disruptive feature is the price. It is "
  "open source under Apache 2.0 and ships with a free tier attached to a personal Google account that "
  "is generous enough for real daily work — not a trial that runs out mid-afternoon. In a market "
  "where the good agents cost $20 to $200 a month, giving one away changes the calculation for a lot "
  "of developers and, more pointedly, for a lot of students and people in markets where those "
  "subscriptions are not realistic.",
  "Functionally it is what you would expect and want: a terminal agent that reads your codebase, "
  "plans multi-step changes, runs commands, and iterates against test results. Gemini's long context "
  "window is the technical advantage — it can hold more of a repository in view at once than most "
  "competitors, which matters on the tasks where understanding the whole system is the hard part.",
  "Being open source means the agent loop is inspectable, forkable and extensible, and the project "
  "has attracted genuine community contribution rather than being a source-available marketing "
  "gesture. The trade-off is the one every Google developer product carries: excellent while it has "
  "attention, and nobody can promise it keeps it.",
 ],
 features=[
  ("terminal", "Terminal-Native Agent",
   "Runs where developers work — over SSH, in containers, on build machines — without depending on "
   "a particular editor."),
  ("git", "Apache 2.0 Open Source",
   "The full agent loop is readable and forkable, with real community contribution behind it."),
  ("brain", "Long Context Windows",
   "Gemini's context length lets it hold more of a codebase in view at once, which is where "
   "whole-system reasoning tasks are won or lost."),
  ("zap", "Substantial Free Tier",
   "A personal Google account unlocks enough daily usage for genuine work, not a demo allowance."),
  ("link", "MCP Support",
   "Connects to Model Context Protocol servers, so it can reach your tools and data sources as "
   "native capabilities."),
  ("check", "Command Execution with Confirmation",
   "Runs build and test commands and iterates on the results, with confirmation gates on the actions "
   "that matter."),
 ],
 pros=[
  "Free tier is genuinely usable for daily development",
  "Apache 2.0 licensed with an active contributor community",
  "Long context handles large codebases well",
  "Terminal-native, so it works over SSH and in CI",
  "MCP support fits the wider 2026 tooling ecosystem",
 ],
 cons=[
  "Locked to Gemini models",
  "Trails Claude Code on the hardest agentic coding tasks",
  "Free tier terms can change at Google's discretion",
  "Less polished than commercial competitors",
 ],
 pricing=[
  ("Free", "$0", "Personal Google account, substantial daily usage allowance"),
  ("Google AI Pro", "$19.99 / month", "Higher limits and expanded model access"),
  ("Vertex AI", "Usage-based", "Enterprise deployment with governance and billing controls"),
 ],
 excels=[
  "Developers who want a capable coding agent at no cost",
  "Large codebases where context length is the binding constraint",
  "Remote and containerised development over SSH",
  "Teams already using Google Cloud and Vertex AI",
 ],
 not_ideal=[
  "Organisations that cannot send code to Google",
  "Teams wanting model choice",
  "Work at the very top of task difficulty where Claude Code leads",
 ],
 comparisons=[
  ("Gemini CLI vs Claude Code",
   "Claude Code is the stronger agent on hard, multi-step work and most 2026 rankings put it first. "
   "Gemini CLI is free and open source. For a great many developers that is the whole comparison — "
   "run Gemini CLI daily, and escalate the genuinely hard problems."),
  ("Gemini CLI vs OpenCode",
   "Both are open-source terminal agents. OpenCode works with any model; Gemini CLI is tied to Gemini "
   "but comes with free inference. If you have no model budget, Gemini CLI wins. If you need control "
   "over the data path, OpenCode does."),
 ],
 verdict="Gemini CLI is the best free coding agent available, and that sentence does most of the work. "
         "It is not the most capable — Claude Code holds that position — but the gap is smaller than "
         "the price gap, and for students, independent developers and anyone in a market where a $20 "
         "monthly subscription is a real decision, it is transformative. Apache 2.0 licensing and MCP "
         "support mean it fits properly into a modern toolchain rather than sitting beside it. The "
         "risk is Google's attention span, and the mitigation is that the code is open.",
 faq=[
  ("Is Gemini CLI really free?",
   "Yes, with a personal Google account, and the allowance is generous enough for daily development "
   "rather than being a trial. Higher limits come with Google AI Pro or Vertex AI billing."),
  ("Is Gemini CLI open source?",
   "Yes, under Apache 2.0, with an active community. The agent loop is readable and forkable."),
  ("Can it use models other than Gemini?",
   "No. For model flexibility, OpenCode is the alternative in the same terminal-agent category."),
  ("Does it support MCP?",
   "Yes. It connects to Model Context Protocol servers, so your own tools and data sources appear as "
   "native capabilities to the agent."),
 ],
 breakdown=[("Code Quality", 8.3), ("Context Handling", 9.2),
            ("Openness", 9.4), ("Polish", 7.2), ("Value", 9.9)],
 related=[("opencode", "OpenCode", "4.6", "Open-Source Coding Agent"),
          ("google-antigravity", "Google Antigravity", "4.2", "Agent-First Platform"),
          ("openai-codex", "OpenAI Codex", "4.4", "OpenAI Coding Agent")],
),

dict(CO,
 slug="warp", name="Warp", company="Warp",
 domain="warp.dev", url="https://www.warp.dev/",
 cta2_url="https://www.warp.dev/download", cta2_label="Download Warp",
 flag="&#127482;&#127480;", country="USA", founded="2020", hq="New York, New York, USA",
 rating=4.4, date="2026-09-06",
 badges=["Agentic Terminal", "Rust Built", "Free Tier"],
 quick_stats=[("Terminal", "Category"), ("Rust", "Built In"),
              ("Agent Mode", "Core Feature"), ("Free tier", "Entry"), ("2020", "Founded")],
 title="Warp Review 2026: The Agentic Terminal for Development | TechVernia",
 meta_desc="Warp review 2026. The Rust-built terminal that became an agentic "
           "development platform: natural-language commands, agent mode, shared "
           "workflows. Pricing, privacy questions and honest verdict.",
 meta_keywords="Warp terminal review, agentic terminal, AI terminal, Warp pricing, "
               "Warp vs iTerm, developer automation platform",
 overview=[
  "Warp started as an attempt to fix the terminal — a Rust-built replacement with block-based output, "
  "proper text editing, and the sort of interface work that command-line tools have gone without for "
  "forty years. In 2026 it positions itself as an open platform for automating development, and the "
  "agent is now the centre of the product rather than a feature attached to it.",
  "The practical value is that Warp meets you where the friction actually is. Nobody remembers the "
  "right `find` invocation or the exact flags for a `ffmpeg` conversion; describing the goal and "
  "getting a correct command is a small win that repeats twenty times a day. Agent mode goes further, "
  "executing multi-step work — debugging a failing build, working through a deployment, chasing an "
  "error across logs — with the terminal as the workspace.",
  "The trade-off is the one every hosted terminal faces: your commands, and potentially their output, "
  "involve a third party. Warp has invested in addressing this and offers controls, but a terminal is "
  "the most sensitive surface a developer has — it is where credentials, production hosts and "
  "customer data all pass through. That is a decision to make deliberately rather than by clicking "
  "through onboarding.",
 ],
 features=[
  ("terminal", "Natural-Language to Command",
   "Describe the goal and get the correct invocation, which removes the constant flag-lookup tax on "
   "tools you use occasionally."),
  ("zap", "Agent Mode",
   "Multi-step execution in the terminal: debugging failing builds, working through deployments, "
   "chasing errors across logs."),
  ("layers", "Block-Based Output",
   "Commands and their output are discrete blocks you can navigate, copy and share, rather than an "
   "undifferentiated scrollback."),
  ("users", "Shared Workflows",
   "Team-shared saved commands and workflows, which is quietly one of the better onboarding tools a "
   "team can have."),
  ("cpu", "Rust Performance",
   "GPU-accelerated rendering and a Rust core keep it fast even with heavy output."),
  ("lock", "Configurable AI Boundaries",
   "Controls over what is sent for AI processing, which matters given how sensitive terminal content "
   "is."),
 ],
 pros=[
  "Genuinely better terminal ergonomics, agent aside",
  "Natural-language commands remove a real daily friction",
  "Shared workflows help new team members enormously",
  "Fast — Rust and GPU rendering, not an Electron app",
  "Usable free tier",
 ],
 cons=[
  "A terminal that talks to a vendor is a serious trust decision",
  "Account requirement irritates developers who expect a local tool",
  "Paid tiers add up across a team",
  "Agent mode can execute destructive commands if you are careless",
 ],
 pricing=[
  ("Free", "$0", "Terminal, limited AI requests per month"),
  ("Pro", "From $18 / month", "Higher AI limits, advanced agent features"),
  ("Team", "From $40 / user / month", "Shared workflows, team management"),
  ("Enterprise", "Custom", "SSO, compliance controls, deployment support"),
 ],
 excels=[
  "Developers who spend most of their day in a terminal",
  "Teams wanting to share operational knowledge as runnable workflows",
  "Debugging sessions where the loop is command, read, adjust, repeat",
  "Onboarding engineers onto unfamiliar toolchains",
 ],
 not_ideal=[
  "Environments where terminal content cannot reach a third party",
  "Air-gapped or heavily restricted networks",
  "Developers who want a purely local, accountless tool",
 ],
 comparisons=[
  ("Warp vs iTerm2 or Alacritty",
   "Traditional terminals are local, free and ask nothing of you. Warp adds an agent, shared "
   "workflows and modern ergonomics, in exchange for an account and a network dependency. If the AI "
   "features are not the draw, the traditional tools remain excellent."),
  ("Warp vs Claude Code",
   "Different jobs that overlap. Claude Code is a coding agent that runs in a terminal; Warp is a "
   "terminal with an agent for operational work. Many developers run Claude Code inside Warp, which "
   "is the honest answer to the comparison."),
 ],
 verdict="Warp is a better terminal before you count the AI, and that is the strongest thing you can "
         "say about it. Block-based output, real text editing and shared team workflows would justify "
         "adoption on their own; natural-language commands and agent mode are a genuine daily "
         "time-saver on top. The reservation is structural rather than about quality: the terminal is "
         "where credentials and production systems live, and routing any of that through a vendor "
         "deserves a deliberate decision and a look at the enterprise controls. Make that decision "
         "consciously and Warp is an easy recommendation.",
 faq=[
  ("Is Warp free?",
   "There is a free tier with a monthly AI request allowance. Pro starts around $18 per month and "
   "team plans around $40 per user per month."),
  ("Does Warp send my terminal contents to the cloud?",
   "AI features require sending relevant context for processing. Warp provides controls over what is "
   "shared, and enterprise plans add stricter boundaries — worth configuring before use on sensitive "
   "systems."),
  ("Do I need an account?",
   "Yes, which is a common complaint from developers who expect a terminal to be a purely local tool."),
  ("Can Warp run destructive commands?",
   "Agent mode executes commands, so yes if you approve them carelessly. Review what the agent "
   "proposes, particularly against production systems."),
 ],
 breakdown=[("Terminal Ergonomics", 9.4), ("Agent Usefulness", 8.6),
            ("Team Features", 8.8), ("Privacy Posture", 6.5), ("Performance", 9.2)],
 related=[("gemini-cli", "Gemini CLI", "4.3", "Terminal Coding Agent"),
          ("opencode", "OpenCode", "4.6", "Open-Source Coding Agent"),
          ("cursor", "Cursor", "4.7", "AI-First Code Editor")],
),

dict(LL,
 slug="lm-studio", name="LM Studio", company="LM Studio",
 domain="lmstudio.ai", url="https://lmstudio.ai/",
 cta2_url="https://lmstudio.ai/download", cta2_label="Download Free",
 flag="&#127482;&#127480;", country="USA", founded="2023", hq="United States",
 rating=4.6, date="2026-09-06",
 badges=["Free", "Fully Local", "No Account"],
 quick_stats=[("100% local", "Inference"), ("Free", "Personal Use"),
              ("GGUF + MLX", "Model Formats"), ("OpenAI-compatible", "Local API"),
              ("2023", "Founded")],
 title="LM Studio Review 2026: The Easiest Way to Run LLMs Locally | TechVernia",
 meta_desc="LM Studio review 2026. The desktop app that made running local LLMs "
           "genuinely easy: model discovery, GPU offload, an OpenAI-compatible local "
           "server and zero data leaving your machine. Hardware needs and verdict.",
 meta_keywords="LM Studio review, run LLM locally, local AI, offline ChatGPT, GGUF, "
               "LM Studio vs Ollama, private AI",
 overview=[
  "LM Studio is the application that turned running a language model on your own hardware from a "
  "weekend project into a ten-minute download. It is a desktop app: you browse models, it tells you "
  "honestly whether your machine can run each one, you click download, and you are chatting with a "
  "model that never sends a byte anywhere. For a category that spent years gatekeeping itself behind "
  "command-line quantisation flags, that is a significant piece of work.",
  "The feature that matters most to developers is the local server. LM Studio exposes an "
  "OpenAI-compatible API endpoint on localhost, which means any application already written against "
  "the OpenAI SDK can be pointed at a local model by changing a base URL. Prototyping against a "
  "frontier API and deploying against a local model stops being a rewrite and becomes a config "
  "change.",
  "The constraint is hardware, and no software can argue with it. Small models run on any modern "
  "laptop; the ones that genuinely compete with hosted frontier models want a lot of VRAM or an Apple "
  "Silicon machine with substantial unified memory. LM Studio is honest about this — it grades models "
  "against your actual machine — which is more than most of this category manages.",
 ],
 features=[
  ("cpu", "One-Click Local Inference",
   "Browse, download and run models without touching a command line, with clear guidance on what "
   "your hardware can actually handle."),
  ("link", "OpenAI-Compatible Local Server",
   "Exposes a localhost endpoint matching the OpenAI API, so existing applications switch to a local "
   "model by changing one URL."),
  ("lock", "Nothing Leaves the Machine",
   "Inference is entirely local. No account, no telemetry on your prompts, no vendor in the data "
   "path — the reason regulated teams use it."),
  ("layers", "GGUF and MLX Support",
   "Broad model format support including Apple Silicon-optimised MLX, which makes Macs unusually "
   "good local inference machines."),
  ("zap", "GPU Offload Control",
   "Tune how many layers run on the GPU to trade speed against memory, with the app suggesting sane "
   "defaults."),
  ("book", "Local Document Chat",
   "Attach documents and query them locally, giving a private alternative to uploading files to a "
   "hosted assistant."),
 ],
 pros=[
  "The lowest-friction entry point to local LLMs, by a wide margin",
  "OpenAI-compatible endpoint makes migration nearly free",
  "Complete privacy — no account, no data leaving the device",
  "Honest hardware guidance instead of letting you download a model that will not run",
  "Free for personal use",
 ],
 cons=[
  "Capable models need serious hardware — there is no way around this",
  "Closed source, unlike Jan and Open WebUI",
  "Single-machine tool: not a serving platform for a team",
  "Local models still trail frontier hosted models on hard reasoning",
 ],
 pricing=[
  ("Personal", "Free", "Full application, unlimited local use"),
  ("Business", "Contact vendor", "Commercial use licensing for organisations"),
 ],
 excels=[
  "Working with confidential material that cannot reach a vendor",
  "Developers prototyping against a local OpenAI-compatible endpoint",
  "Offline environments and air-gapped networks",
  "Cutting API spend on high-volume, low-difficulty tasks",
 ],
 not_ideal=[
  "Machines without a capable GPU or substantial unified memory",
  "Multi-user serving — vLLM is the right tool there",
  "Tasks needing frontier-model reasoning quality",
 ],
 comparisons=[
  ("LM Studio vs Ollama",
   "Ollama is a command-line-first runtime that developers embed in scripts and services; LM Studio "
   "is a graphical application with model discovery and hardware guidance. Most people should start "
   "with LM Studio and move to Ollama when they want automation."),
  ("LM Studio vs Jan",
   "Jan is open source and LM Studio is not, which for some organisations settles it. LM Studio is "
   "the more polished product with better hardware guidance; Jan is the one you can audit."),
 ],
 verdict="LM Studio is the right first step into local LLMs for almost everyone. It removed the "
         "quantisation-flag gatekeeping that kept this category niche, and the OpenAI-compatible "
         "local server quietly makes it a serious developer tool rather than a hobbyist toy — "
         "switching an application from a hosted API to a local model becomes a one-line change. "
         "Be realistic about hardware, and be aware you are running closed-source software on a "
         "privacy-motivated workflow, which is a slight irony worth noting. If that bothers you, "
         "Jan does the same job with source you can read.",
 faq=[
  ("Is LM Studio free?",
   "Free for personal use. Commercial use inside an organisation requires contacting the vendor about "
   "business licensing."),
  ("What hardware do I need?",
   "Small models run on any modern laptop. Models that genuinely compete with hosted frontier models "
   "want substantial GPU VRAM or an Apple Silicon machine with a lot of unified memory. The app "
   "grades each model against your actual hardware."),
  ("Does LM Studio send my data anywhere?",
   "No. Inference runs entirely on your machine, with no account required and no prompts leaving the "
   "device — which is the main reason it appears in regulated environments."),
  ("Can I use LM Studio as an API for my own app?",
   "Yes. It exposes an OpenAI-compatible endpoint on localhost, so applications written against the "
   "OpenAI SDK work by changing the base URL."),
 ],
 breakdown=[("Ease of Use", 9.6), ("Privacy", 10.0),
            ("Developer Integration", 9.0), ("Model Quality Ceiling", 7.0), ("Value", 9.7)],
 related=[("jan", "Jan", "4.4", "Open-Source Local AI"),
          ("open-webui", "Open WebUI", "4.5", "Self-Hosted AI Interface"),
          ("vllm", "vLLM", "4.7", "Production Inference Engine")],
),

]
