# -*- coding: utf-8 -*-
"""Lot 6 - SOC agentique / securite offensive (cybersecurity/) et debut agents vocaux (voice/).

Radiant Security a ete retire : sa techno AI SOC a ete rachetee par Cribl le
19 aout 2026 et son site renvoie 404. Remplace par Simbian.
"""

CS = dict(category="cybersecurity", cat_href="../../categories/ai-cybersecurity.html",
          cat_label="AI Cybersecurity", app_category="SecurityApplication")
VO = dict(category="voice", cat_href="../../categories.html",
          cat_label="AI Voice Agents", app_category="BusinessApplication")

TOOLS = [

dict(CS,
 slug="xbow", name="XBOW", company="XBOW",
 domain="xbow.com", url="https://xbow.com/",
 cta2_url="https://xbow.com/", cta2_label="Request a Demo",
 flag="&#127482;&#127480;", country="USA", founded="2023", hq="United States",
 rating=4.6, date="2026-09-06",
 badges=["Offensive Security", "$1B+ Valuation", "Autonomous Pentesting"],
 quick_stats=[("$120M", "Series C"), ("$1B+", "Valuation"),
              ("Offensive", "Security Posture"), ("Continuous", "Testing Model"),
              ("2023", "Founded")],
 title="XBOW Review 2026: Autonomous Offensive Security and AI Pentesting | TechVernia",
 meta_desc="XBOW review 2026. The autonomous offensive security platform that raised "
           "$120M at a $1B+ valuation: AI agents that find and validate exploitable "
           "vulnerabilities continuously. What it replaces, what it does not.",
 meta_keywords="XBOW review, autonomous pentesting, AI offensive security, AI red team, "
               "continuous penetration testing, XBOW valuation",
 overview=[
  "XBOW is the most consequential thing to happen to penetration testing in a decade, and the "
  "funding reflects it: $120 million in Series C at a valuation above $1 billion, with strategic "
  "investment from Accenture. The product is an autonomous offensive security platform — AI agents "
  "that probe your systems the way an attacker would, find exploitable paths, and prove them rather "
  "than listing theoretical risks.",
  "The distinction between finding and proving is the whole point, and anyone who has worked a "
  "vulnerability queue understands why. Traditional scanners produce thousands of findings ranked by "
  "CVSS, most of which are not exploitable in your specific configuration, and the security team "
  "burns its week on triage rather than on fixing. XBOW chains steps the way a human tester does and "
  "demonstrates the actual exploitation path, which turns a list of maybes into a short list of "
  "definites.",
  "The economic argument is continuity. An annual penetration test is a snapshot of a system that "
  "changes weekly; between engagements you are guessing. Autonomous testing runs continuously, which "
  "matches how software actually ships in 2026. It does not replace a skilled human red team — "
  "creative attack chains, social engineering and business logic abuse remain human territory — but "
  "it does replace the repetitive eighty per cent that consumes most of a test's hours.",
 ],
 features=[
  ("shield", "Autonomous Exploitation Chains",
   "Agents chain vulnerabilities into working attack paths rather than reporting isolated findings, "
   "which is the difference between a scanner and a tester."),
  ("check", "Validated, Not Theoretical",
   "Findings come with a demonstrated exploitation path, eliminating the false-positive triage that "
   "consumes most vulnerability management time."),
  ("clock", "Continuous Testing",
   "Runs against every change rather than annually, matching the pace at which modern systems "
   "actually ship."),
  ("layers", "Broad Attack Surface Coverage",
   "Web applications, APIs and infrastructure tested as a connected system rather than in isolation."),
  ("link", "Security Platform Integration",
   "Integrates into existing security tooling, including Microsoft Security Copilot, so findings "
   "reach the workflows teams already run."),
  ("activity", "Prioritisation by Real Exploitability",
   "Severity reflects what an attacker could actually do in your environment, not a generic CVSS "
   "score assigned without context."),
 ],
 pros=[
  "Validated exploitation paths eliminate false-positive triage",
  "Continuous testing closes the gap between annual pentest snapshots",
  "Strong funding and Accenture backing reduce vendor risk",
  "Integrates with existing security platforms rather than replacing them",
  "Frees human red teamers for the creative work only they can do",
 ],
 cons=[
  "Enterprise pricing puts it out of reach for smaller organisations",
  "Does not replace human red teaming for business logic and social engineering",
  "Autonomous testing against production requires careful scoping and authorisation",
  "Young company in a category still establishing its practices",
 ],
 pricing=[
  ("Enterprise", "Custom", "Scoped to attack surface size and testing frequency"),
 ],
 excels=[
  "Organisations shipping frequently where annual pentests are structurally inadequate",
  "Security teams drowning in unvalidated scanner output",
  "Continuous validation of web application and API attack surface",
  "Freeing scarce offensive security talent from repetitive testing",
 ],
 not_ideal=[
  "Small organisations without enterprise security budget",
  "Compliance regimes that specifically require a human-signed penetration test",
  "Business logic and social engineering assessment",
 ],
 comparisons=[
  ("XBOW vs traditional vulnerability scanners",
   "Scanners report what might be vulnerable; XBOW demonstrates what is. The practical difference is "
   "where your team's week goes — triaging theoretical findings, or fixing proven ones."),
  ("XBOW vs a human red team",
   "Complementary rather than competing. XBOW covers the repetitive, broad-surface testing "
   "continuously; humans remain irreplaceable for creative attack chains, business logic abuse and "
   "anything involving people. Using XBOW to buy back human hours is the correct framing."),
 ],
 verdict="XBOW is the clearest example of AI doing security work that was genuinely painful rather "
         "than merely tedious. Validated exploitation paths solve the single biggest failure of "
         "vulnerability management — teams spending their capacity proving findings wrong instead of "
         "fixing the ones that matter — and continuous testing fits how software actually ships. It "
         "is enterprise-priced and it is not a replacement for skilled humans; treat it as the tool "
         "that gives your red team its time back. Scope authorisation carefully before pointing "
         "autonomous testing at anything production-facing.",
 faq=[
  ("Does XBOW replace penetration testing?",
   "It replaces the repetitive majority of it and runs continuously rather than annually. Creative "
   "attack chains, business logic abuse and social engineering still need skilled humans."),
  ("What does 'validated finding' mean?",
   "XBOW demonstrates the actual exploitation path rather than reporting a theoretical vulnerability, "
   "which removes the false-positive triage that consumes most vulnerability management effort."),
  ("How much did XBOW raise?",
   "$120 million in a Series C at a valuation above $1 billion, including strategic investment from "
   "Accenture."),
  ("Is it safe to run against production?",
   "It requires careful scoping and explicit authorisation, exactly as a human penetration test does. "
   "Autonomous testing does not remove the need for rules of engagement — it makes them more "
   "important."),
 ],
 breakdown=[("Finding Validation", 9.7), ("Attack Surface Coverage", 9.0),
            ("Continuous Operation", 9.5), ("Accessibility", 5.5), ("Integration", 8.8)],
 related=[("dropzone-ai", "Dropzone AI", "4.5", "Autonomous SOC Analyst"),
          ("prophet-security", "Prophet Security", "4.4", "AI Alert Triage"),
          ("wiz", "Wiz", "4.8", "Cloud Security")],
),

dict(CS,
 slug="dropzone-ai", name="Dropzone AI", company="Dropzone AI",
 domain="dropzone.ai", url="https://www.dropzone.ai/",
 cta2_url="https://www.dropzone.ai/", cta2_label="Request a Demo",
 flag="&#127482;&#127480;", country="USA", founded="2022", hq="Seattle, Washington, USA",
 rating=4.5, date="2026-09-06",
 badges=["AI SOC Analyst", "200+ Organisations", "Fortune Cyber 60"],
 quick_stats=[("200+", "Organisations"), ("Fortune Cyber 60", "Recognition"),
              ("Pre-trained", "No tuning needed"), ("Tier 1 triage", "Primary Job"),
              ("2022", "Founded")],
 title="Dropzone AI Review 2026: The Autonomous SOC Analyst | TechVernia",
 meta_desc="Dropzone AI review 2026. Pre-trained AI agents that investigate security "
           "alerts end to end the way a human analyst would. Deployment model, "
           "trust questions and how it compares to Prophet Security and Exaforce.",
 meta_keywords="Dropzone AI review, AI SOC analyst, autonomous alert triage, agentic "
               "SOC, security automation, alert fatigue",
 overview=[
  "Alert fatigue is the defining operational failure of security operations, and it is not really "
  "about volume — it is about the fact that investigating an alert properly takes twenty minutes and "
  "a Tier 1 analyst has three hundred of them. What actually happens is that alerts get closed on "
  "pattern recognition, and eventually one that mattered gets closed the same way. Dropzone AI "
  "automates the investigation itself rather than the closing.",
  "Its agents work an alert the way a competent analyst would: pull context from the endpoint, check "
  "the user's normal behaviour, look at the destination's reputation, correlate with recent activity, "
  "and produce a written verdict with the evidence behind it. That last part is what makes it usable "
  "— the output is an investigation a human can review and disagree with, not a confidence score to "
  "take on faith.",
  "It arrives pre-trained on security investigation rather than requiring months of tuning against "
  "your environment, which is the deployment difference that matters when the team buying it is "
  "already underwater. More than 200 organisations run it, and it was named to the Fortune Cyber 60 "
  "list of fastest-growing cybersecurity companies. It integrates with the SIEM, EDR and identity "
  "tools you already have rather than asking you to replace them.",
 ],
 features=[
  ("search", "End-to-End Alert Investigation",
   "Agents gather context across endpoint, identity, network and threat intelligence, reaching a "
   "verdict rather than enriching an alert and handing it back."),
  ("book", "Written Investigation Reports",
   "Output is a readable investigation with evidence, which a human analyst can review and challenge "
   "— not an opaque score."),
  ("zap", "Pre-Trained on Security Work",
   "Deploys without months of environment-specific tuning, which matters because the teams who need "
   "it have no spare capacity to train a tool."),
  ("link", "Works with Existing Tooling",
   "Integrates with the SIEM, EDR and identity platforms already in place instead of demanding "
   "replacement."),
  ("clock", "24/7 Consistent Coverage",
   "Investigation quality does not degrade at 3am or in the last hour of a shift, which is a genuine "
   "and under-discussed advantage over human triage."),
  ("users", "Analyst Capacity Multiplier",
   "Tier 1 volume is absorbed so human analysts can work threat hunting and the investigations that "
   "actually need judgement."),
 ],
 pros=[
  "Investigates rather than merely enriching or scoring alerts",
  "Written reports with evidence make the output auditable",
  "Pre-trained, so deployment does not require spare team capacity",
  "Proven across 200+ organisations rather than in pilots",
  "Fits existing tool stacks instead of replacing them",
 ],
 cons=[
  "Trusting automated verdicts requires a validation period nobody enjoys running",
  "Novel attack patterns outside its training are where it is weakest",
  "Enterprise pricing",
  "Investigation quality depends on the telemetry it can reach",
 ],
 pricing=[
  ("Enterprise", "Custom", "Priced on alert volume and integration scope"),
 ],
 excels=[
  "SOCs where Tier 1 alert volume exceeds analyst capacity",
  "Organisations that cannot staff 24/7 coverage",
  "Reducing time-to-verdict on high-volume commodity alerts",
  "Freeing analysts for threat hunting and incident response",
 ],
 not_ideal=[
  "Organisations with low alert volume that human triage handles fine",
  "Environments with poor telemetry — the agent can only see what is logged",
  "Teams unwilling to run a proper validation period before trusting verdicts",
 ],
 comparisons=[
  ("Dropzone AI vs Prophet Security",
   "Both automate Tier 1 investigation and both are credible. Dropzone leads on deployment maturity "
   "and installed base; Prophet emphasises replicating elite analyst investigation technique. Run "
   "both against the same week of real alerts — that comparison is more useful than any feature "
   "matrix."),
  ("Dropzone AI vs SOAR playbooks",
   "SOAR executes the decision tree you wrote in advance and breaks when reality does not match it. "
   "Dropzone reasons about the specific alert. SOAR remains better for deterministic response "
   "actions; investigation is where reasoning wins."),
 ],
 verdict="Dropzone AI attacks the right problem. Alert fatigue is not solved by better filtering or "
         "smarter rules — it is solved by making investigation cheap enough to do properly every "
         "time, and that is what this does. The written report format is the detail that makes it "
         "adoptable: security teams can audit the reasoning instead of trusting a score, which is the "
         "only basis on which anyone should hand triage to a machine. Run a validation period against "
         "alerts you have already investigated, compare verdicts honestly, and expand from there.",
 faq=[
  ("Does Dropzone AI replace SOC analysts?",
   "It replaces the repetitive Tier 1 investigation load, not the analysts. The consistent outcome "
   "reported by users is analysts moving to threat hunting and incident response rather than leaving."),
  ("How long does deployment take?",
   "The agents are pre-trained on security investigation rather than requiring months of "
   "environment-specific tuning, so time to value is measured in weeks rather than quarters."),
  ("Can I see why it reached a verdict?",
   "Yes. Output is a written investigation with the evidence gathered, which is what makes the "
   "verdict auditable rather than something to accept on trust."),
  ("What are its weak spots?",
   "Novel attack patterns outside its training, and environments with poor telemetry — an agent can "
   "only investigate what your tools actually log."),
 ],
 breakdown=[("Investigation Depth", 9.2), ("Auditability", 9.4),
            ("Deployment Speed", 9.0), ("Novel Threat Handling", 7.2), ("Integration", 8.9)],
 related=[("prophet-security", "Prophet Security", "4.4", "AI Alert Triage"),
          ("exaforce", "Exaforce", "4.4", "Agentic SOC and MDR"),
          ("simbian", "Simbian", "4.2", "Autonomous Security Agents")],
),

dict(CS,
 slug="prophet-security", name="Prophet Security", company="Prophet Security",
 domain="prophetsecurity.ai", url="https://www.prophetsecurity.ai/",
 cta2_url="https://www.prophetsecurity.ai/", cta2_label="Request a Demo",
 flag="&#127482;&#127480;", country="USA", founded="2023", hq="Palo Alto, California, USA",
 rating=4.4, date="2026-09-06",
 badges=["AI SOC Analyst", "Venture Backed", "Investigation Focus"],
 quick_stats=[("$30M+", "Raised"), ("Tier 1", "Triage Focus"),
              ("Evidence-based", "Verdicts"), ("SIEM-agnostic", "Integration"),
              ("2023", "Founded")],
 title="Prophet Security Review 2026: AI SOC Analyst for Alert Triage | TechVernia",
 meta_desc="Prophet Security review 2026. An AI SOC analyst built to replicate how "
           "elite human analysts investigate: hypothesis, evidence, verdict. "
           "Deployment, honest limits and how it compares to Dropzone AI.",
 meta_keywords="Prophet Security review, AI SOC analyst, autonomous alert triage, "
               "agentic SOC platform, security operations automation",
 overview=[
  "Prophet Security builds an AI SOC analyst, and its stated design goal is more specific than the "
  "category average: replicate the way an excellent human analyst investigates, rather than "
  "automating the shortcuts a tired one takes. That distinction shows up in the product. "
  "Investigations proceed by forming a hypothesis, gathering the evidence that would confirm or "
  "refute it, and reaching a verdict that cites what it found.",
  "That method matters because the alternative — pattern-matching an alert against previous ones — is "
  "precisely the behaviour that lets a real incident get closed as routine. An investigation that "
  "explicitly asks what evidence would prove this benign, and then goes and looks, fails differently "
  "and more safely than one that scores similarity.",
  "It sits in the same competitive bracket as Dropzone AI and Exaforce: venture-backed with more than "
  "$30 million raised, purpose-built for autonomous Tier 1 triage, ingesting alerts from the tooling "
  "you already run rather than replacing your SIEM. It is a younger company than Dropzone with a "
  "smaller installed base, which is the main practical difference when you are choosing between them.",
 ],
 features=[
  ("brain", "Hypothesis-Driven Investigation",
   "Forms a hypothesis and gathers evidence to confirm or refute it, rather than scoring similarity "
   "against previously seen alerts."),
  ("check", "Evidence-Cited Verdicts",
   "Every conclusion is backed by the specific evidence gathered, so an analyst can audit the "
   "reasoning rather than accept a score."),
  ("link", "SIEM and EDR Agnostic",
   "Ingests alerts from existing detection tooling instead of requiring a platform migration."),
  ("layers", "Multi-Source Context Gathering",
   "Pulls from identity, endpoint, network and threat intelligence to build a complete picture of an "
   "alert."),
  ("clock", "Consistent Round-the-Clock Triage",
   "The same investigation depth at every hour, which human shift patterns cannot deliver."),
  ("activity", "Noise Resolution at Volume",
   "Resolves the low-severity majority autonomously so human attention concentrates on what is left."),
 ],
 pros=[
  "Investigation methodology is closer to how good analysts actually work",
  "Evidence-cited verdicts make automated conclusions auditable",
  "Works with existing detection stack — no SIEM replacement",
  "Consistent quality regardless of time of day",
  "Focused product rather than a broad platform doing this as a feature",
 ],
 cons=[
  "Smaller installed base than Dropzone AI",
  "Younger company, so continuity risk is higher",
  "Enterprise pricing with limited public transparency",
  "Effectiveness bounded by the telemetry available to it",
 ],
 pricing=[
  ("Enterprise", "Custom", "Priced on alert volume and integration scope"),
 ],
 excels=[
  "SOCs overwhelmed by Tier 1 alert volume",
  "Teams that need to audit why an alert was closed",
  "Organisations without 24/7 analyst coverage",
  "Reducing mean time to verdict on commodity alerts",
 ],
 not_ideal=[
  "Small environments where human triage is adequate",
  "Organisations with poor logging coverage",
  "Buyers who need the largest installed base for risk reasons",
 ],
 comparisons=[
  ("Prophet Security vs Dropzone AI",
   "The same job with different emphases: Dropzone has more deployment maturity and a larger "
   "installed base, Prophet leans on investigation methodology. Both should be trialled against the "
   "same historical alerts — that is the only comparison that tells you anything."),
  ("Prophet Security vs adding analysts",
   "Headcount is the honest alternative and it is expensive, slow to hire and hard to retain in a "
   "role built on repetitive triage. The realistic outcome is not fewer analysts but analysts doing "
   "work worth their salary."),
 ],
 verdict="Prophet Security is a serious entrant in the strongest new category in security operations. "
         "Building the product around how good analysts investigate — hypothesis, evidence, verdict — "
         "rather than around alert scoring is the right architectural instinct, and evidence-cited "
         "conclusions are non-negotiable for anything automating triage. It is younger and smaller "
         "than Dropzone, which is a real consideration for a tool you are trusting with alert "
         "closure. Trial both on the same week of alerts you have already worked, and let the "
         "verdicts decide.",
 faq=[
  ("What does Prophet Security automate?",
   "Tier 1 alert investigation: gathering context, testing a hypothesis, and producing a verdict with "
   "cited evidence — the work that consumes most SOC analyst time."),
  ("Does it replace my SIEM?",
   "No. It ingests alerts from your existing SIEM and EDR tooling. It sits on top of your detection "
   "stack rather than replacing it."),
  ("How is it different from Dropzone AI?",
   "Both automate Tier 1 investigation. Dropzone has a larger installed base and more deployment "
   "maturity; Prophet emphasises replicating elite analyst investigation methodology. Trial both."),
  ("Can I audit its decisions?",
   "Yes. Verdicts cite the evidence gathered, which is the minimum bar for trusting any system that "
   "closes security alerts."),
 ],
 breakdown=[("Investigation Method", 9.3), ("Auditability", 9.2),
            ("Integration Breadth", 8.6), ("Market Maturity", 7.0), ("Support Depth", 7.5)],
 related=[("dropzone-ai", "Dropzone AI", "4.5", "Autonomous SOC Analyst"),
          ("exaforce", "Exaforce", "4.4", "Agentic SOC and MDR"),
          ("simbian", "Simbian", "4.2", "Autonomous Security Agents")],
),

dict(CS,
 slug="exaforce", name="Exaforce", company="Exaforce",
 domain="exaforce.com", url="https://www.exaforce.com/",
 cta2_url="https://www.exaforce.com/", cta2_label="Request a Demo",
 flag="&#127482;&#127480;", country="USA", founded="2023", hq="United States",
 rating=4.4, date="2026-09-06",
 badges=["Agentic SOC", "MDR Included", "$125M Series B"],
 quick_stats=[("$125M", "Series B"), ("Agentic SOC", "Platform"),
              ("MDR", "Service Layer"), ("Cloud + identity", "Coverage"),
              ("2023", "Founded")],
 title="Exaforce Review 2026: Agentic SOC Platform with MDR | TechVernia",
 meta_desc="Exaforce review 2026. An agentic SOC platform that pairs autonomous "
           "investigation with a managed detection and response service. Why the "
           "hybrid model matters and where it fits against pure-software rivals.",
 meta_keywords="Exaforce review, agentic SOC, MDR service, AI security operations, "
               "managed detection response AI, Exaforce funding",
 overview=[
  "Exaforce differs from the other agentic SOC vendors in a way that matters more than its feature "
  "list: it pairs the platform with a managed detection and response service. You are not only "
  "buying agents that investigate alerts, you are buying humans who own the outcome. For "
  "organisations that lack a SOC rather than having an overloaded one, that combination answers the "
  "actual problem.",
  "It sits in the AI-native bracket alongside Dropzone and Prophet — built around autonomous "
  "investigation from the start rather than an AI layer added to a legacy SIEM — with a $125 million "
  "Series B behind it, which is among the largest raises in the category. The coverage emphasis leans "
  "toward cloud and identity, which is a defensible read of where the attack surface actually moved.",
  "The hybrid model is also the main thing to interrogate during evaluation. Software and services "
  "have very different economics and very different failure modes, and a vendor doing both needs to "
  "be clear about which one you are buying. Ask specifically what the humans do, when they do it, and "
  "what the response commitments are — the answers vary more than the marketing suggests.",
 ],
 features=[
  ("shield", "Agentic Investigation Engine",
   "Autonomous agents investigate alerts across cloud, identity and endpoint telemetry rather than "
   "enriching and escalating."),
  ("users", "Managed Detection and Response",
   "Human analysts backing the platform, which is the difference between a tool and an outcome for "
   "organisations without their own SOC."),
  ("globe", "Cloud and Identity Emphasis",
   "Detection coverage weighted toward where the modern attack surface actually is rather than "
   "toward legacy perimeter telemetry."),
  ("link", "Existing Stack Integration",
   "Works with the detection tooling already deployed instead of requiring consolidation onto a new "
   "platform."),
  ("clock", "Continuous Coverage",
   "Round-the-clock investigation without the shift-pattern quality variance of a small human team."),
  ("activity", "Verdict and Response Workflow",
   "Investigation feeds directly into response actions rather than stopping at a conclusion."),
 ],
 pros=[
  "Software plus managed service answers the whole problem for teams without a SOC",
  "Well funded at $125M Series B — the largest raise among AI-native SOC startups",
  "Cloud and identity focus matches where attacks actually happen now",
  "AI-native architecture rather than AI bolted onto legacy tooling",
  "Integrates with existing detection stack",
 ],
 cons=[
  "The hybrid software-plus-service model needs careful contractual clarity",
  "Less useful for organisations that already have a mature staffed SOC",
  "Enterprise pricing with limited public transparency",
  "Younger vendor than established MDR providers",
 ],
 pricing=[
  ("Platform", "Custom", "Agentic SOC platform priced on telemetry and alert volume"),
  ("Platform + MDR", "Custom", "Managed detection and response with human analyst coverage"),
 ],
 excels=[
  "Organisations with no SOC that need one without hiring one",
  "Cloud-first environments where identity is the primary attack surface",
  "Teams wanting AI investigation with human accountability behind it",
  "Replacing a legacy MDR contract with something AI-native",
 ],
 not_ideal=[
  "Mature SOCs that only want software and would not use the service",
  "Organisations requiring an in-house-only security model",
  "Environments dominated by legacy on-premise infrastructure",
 ],
 comparisons=[
  ("Exaforce vs Dropzone AI",
   "Dropzone sells software to teams that have analysts; Exaforce sells software plus analysts to "
   "teams that do not. If you have a SOC, Dropzone is the cleaner fit. If you are the SOC and you are "
   "one person, Exaforce answers more of the problem."),
  ("Exaforce vs traditional MDR",
   "Traditional MDR providers run human analysts over conventional tooling, and their economics limit "
   "how deeply each alert gets investigated. An AI-native platform changes that ratio. The question "
   "for any MDR buyer in 2026 is whether their provider has made that transition."),
 ],
 verdict="Exaforce is the right shape for organisations that need security operations rather than "
         "security tooling. Pairing autonomous investigation with a managed service means someone is "
         "accountable for the outcome, which is what a company without a SOC actually needs to buy. "
         "The $125 million raise and cloud-identity focus suggest a vendor reading the market "
         "correctly. During evaluation, push hard on exactly what the human layer does and what the "
         "response commitments are in writing — that is where hybrid models differ most and where "
         "the marketing is least specific.",
 faq=[
  ("Is Exaforce software or a service?",
   "Both. It is an agentic SOC platform available with a managed detection and response layer, which "
   "is its main differentiator from pure-software competitors."),
  ("How much has Exaforce raised?",
   "A $125 million Series B, among the largest raises in the AI-native SOC category."),
  ("Who is it best suited to?",
   "Organisations without a mature in-house SOC, particularly cloud-first environments where identity "
   "is the primary attack surface."),
  ("Does it replace my existing security tools?",
   "No. It integrates with the detection tooling you already run rather than requiring consolidation "
   "onto a new platform."),
 ],
 breakdown=[("Investigation Quality", 8.9), ("Managed Service Value", 9.2),
            ("Cloud Coverage", 9.0), ("Contract Clarity", 7.2), ("Vendor Maturity", 7.5)],
 related=[("dropzone-ai", "Dropzone AI", "4.5", "Autonomous SOC Analyst"),
          ("prophet-security", "Prophet Security", "4.4", "AI Alert Triage"),
          ("crowdstrike", "CrowdStrike", "4.8", "Endpoint Protection")],
),

dict(CS,
 slug="simbian", name="Simbian", company="Simbian",
 domain="simbian.ai", url="https://simbian.ai/",
 cta2_url="https://simbian.ai/", cta2_label="Request a Demo",
 flag="&#127482;&#127480;", country="USA", founded="2023", hq="Mountain View, California, USA",
 rating=4.2, date="2026-09-06",
 badges=["Multi-Agent", "Context Lake", "GRC Coverage"],
 quick_stats=[("92%", "Alerts auto-resolved"), ("$10M", "Seed Funding"),
              ("SOC + Hunt + GRC", "Agent Set"), ("Context Lake", "Reasoning Layer"),
              ("2023", "Founded")],
 title="Simbian Review 2026: Multi-Agent Autonomous Security | TechVernia",
 meta_desc="Simbian review 2026. Autonomous security agents spanning SOC triage, threat "
           "hunting and GRC, reasoning over a Context Lake of your own playbooks and "
           "analyst feedback. Reported 92% auto-resolution, and what to check.",
 meta_keywords="Simbian review, autonomous security agents, AI SOC, threat hunting AI, "
               "security GRC automation, Context Lake",
 overview=[
  "Simbian's bet is that the interesting unit is not a single AI analyst but a set of agents covering "
  "different security functions that share the same understanding of your organisation. A SOC agent "
  "triages alerts from your SIEM and XDR; a threat hunting agent works threat intelligence feeds "
  "against your environment looking for indicators; a GRC agent handles security questionnaires and "
  "vendor assessments. Three jobs, one context.",
  "That shared context is the architectural idea, marketed as the Context Lake: your own standard "
  "operating procedures, entity data and accumulated analyst feedback, which every agent reasons "
  "over. The claim it supports is meaningful — the company reports its SOC agent auto-resolving 92% "
  "of alerts in 2026 production deployments — and it explains why: an agent that knows your "
  "procedures and has learned from your analysts' corrections should outperform one reasoning from "
  "generic security knowledge.",
  "It emerged from stealth with $10 million in seed funding, which makes it the smallest of the "
  "serious AI SOC vendors by some distance. The GRC coverage is genuinely differentiated — "
  "questionnaires and vendor assessments consume enormous amounts of security team time and almost "
  "nobody is automating them well — but a $10 million company is a different risk proposition from "
  "one that raised $125 million.",
 ],
 features=[
  ("layers", "Multiple Coordinated Agents",
   "SOC triage, threat hunting and GRC agents that share one understanding of your organisation "
   "rather than three disconnected tools."),
  ("database", "Context Lake",
   "Agents reason over your own procedures, entity data and analyst feedback, which is why "
   "performance improves as the deployment matures."),
  ("check", "High Autonomous Resolution Rate",
   "Reported 92% of alerts auto-resolved in 2026 production deployments — a figure worth validating "
   "against your own alert mix during a trial."),
  ("search", "Threat Hunting Agent",
   "Processes threat intelligence feeds and hunts indicators of compromise across the environment "
   "rather than waiting for an alert."),
  ("book", "GRC Automation",
   "Security questionnaires and vendor assessments handled by an agent — a real time sink that almost "
   "no competitor addresses."),
  ("brain", "Analyst Feedback Loop",
   "Corrections from your analysts feed back into the Context Lake, so the system adapts to how your "
   "team actually works."),
 ],
 pros=[
  "Covers SOC, hunting and GRC rather than triage alone",
  "Context Lake makes agents improve with your team's feedback",
  "GRC automation addresses a genuine and widely ignored time sink",
  "Strong reported auto-resolution figures in production",
  "Unified reasoning across offensive and defensive context",
 ],
 cons=[
  "$10M seed makes it the smallest serious vendor in this category",
  "The 92% figure needs validating against your own alert mix",
  "Breadth across three functions risks less depth in each",
  "Smaller installed base and support organisation",
 ],
 pricing=[
  ("Enterprise", "Custom", "Priced on agent scope, alert volume and deployment size"),
 ],
 excels=[
  "Small security teams covering SOC, hunting and compliance with the same people",
  "Organisations drowning in security questionnaires and vendor assessments",
  "Environments with documented procedures the Context Lake can learn from",
  "Teams wanting one vendor across several security functions",
 ],
 not_ideal=[
  "Large enterprises needing maximum depth in alert triage specifically",
  "Buyers for whom vendor size and continuity are primary criteria",
  "Organisations without documented procedures to ground the agents",
 ],
 comparisons=[
  ("Simbian vs Dropzone AI",
   "Dropzone is deeper on alert investigation with a much larger installed base; Simbian is broader, "
   "covering hunting and GRC as well. A large SOC should probably prefer depth. A three-person "
   "security team covering everything may get more from breadth."),
  ("Simbian vs Prophet Security",
   "Both are young, venture-backed and focused on autonomous security work. Prophet concentrates on "
   "investigation methodology; Simbian spreads across three functions with shared context. Funding "
   "and installed base favour Prophet; scope favours Simbian."),
 ],
 verdict="Simbian is the most interesting bet in the agentic security field and the highest risk of "
         "the credible options. The Context Lake idea is right — agents reasoning over your own "
         "procedures and learning from your analysts should beat generic security reasoning — and "
         "extending agents into GRC addresses a real time sink nobody else takes seriously. It is "
         "also a $10 million seed-stage company competing against vendors that raised ten times that. "
         "Validate the auto-resolution claim against your own alerts, and weigh vendor continuity "
         "honestly for a tool you would be trusting with alert closure.",
 faq=[
  ("What is the Context Lake?",
   "Simbian's layer holding your own standard operating procedures, entity data and analyst feedback, "
   "which all its agents reason over. It is what makes the agents specific to your organisation "
   "rather than generic."),
  ("Is the 92% auto-resolution figure realistic?",
   "It is the company's reported result from 2026 production deployments. Whether it holds for you "
   "depends entirely on your alert mix, so treat it as a claim to validate in a trial rather than a "
   "guarantee."),
  ("What does the GRC agent do?",
   "Handles security questionnaires and vendor assessments — a substantial and widely ignored drain "
   "on security team time that few competitors address."),
  ("How does Simbian compare on funding?",
   "It emerged from stealth with $10 million in seed funding, considerably less than Exaforce's $125M "
   "Series B or Dropzone's position. Factor that into vendor continuity assessment."),
 ],
 breakdown=[("Functional Breadth", 9.2), ("Context Personalisation", 9.0),
            ("Alert Triage Depth", 8.0), ("Vendor Stability", 6.0), ("GRC Value", 8.8)],
 related=[("dropzone-ai", "Dropzone AI", "4.5", "Autonomous SOC Analyst"),
          ("prophet-security", "Prophet Security", "4.4", "AI Alert Triage"),
          ("exaforce", "Exaforce", "4.4", "Agentic SOC and MDR")],
),

dict(VO,
 slug="vapi", name="Vapi", company="Vapi",
 domain="vapi.ai", url="https://vapi.ai/",
 cta2_url="https://dashboard.vapi.ai/", cta2_label="Start Building",
 flag="&#127482;&#127480;", country="USA", founded="2023", hq="San Francisco, California, USA",
 rating=4.6, date="2026-09-06",
 badges=["Developer First", "Every Knob Exposed", "500-600ms"],
 quick_stats=[("500-600ms", "Optimised Latency"), ("Any model", "GPT/Claude/Gemini/Groq"),
              ("Any voice", "ElevenLabs/Cartesia/Deepgram"), ("Telephony", "Built In"),
              ("2023", "Founded")],
 title="Vapi Review 2026: The Developer Platform for Voice AI Agents | TechVernia",
 meta_desc="Vapi review 2026. The voice AI platform serious engineering teams end up "
           "on: choose your model, voice provider and telephony, tune latency to "
           "500-600ms. Architecture, pricing and when it is too much tool.",
 meta_keywords="Vapi review, voice AI platform, AI phone agent, voice agent API, Vapi "
               "vs Retell, conversational voice AI",
 overview=[
  "Vapi is the voice AI platform for teams who want control over every layer of the stack. A voice "
  "agent is really a pipeline — speech to text, a language model, text to speech, and telephony — and "
  "most platforms make those choices for you. Vapi exposes all of them: model provider (GPT, Claude, "
  "Gemini, Groq), voice provider (ElevenLabs, Cartesia, Deepgram, PlayHT), telephony, and the latency "
  "tuning that determines whether a conversation feels natural or stilted.",
  "That control is why serious voice engineering teams converge on it. Latency in voice is not a "
  "vanity metric — above roughly 800 milliseconds a caller starts talking over the agent, and the "
  "conversation degrades badly. With optimised provider pairings Vapi lands in the 500 to 600 "
  "millisecond range, and critically it gives you the knobs to get there rather than a fixed pipeline "
  "you have to accept.",
  "The corollary is that Vapi asks more of you. Every choice it exposes is a choice you have to make "
  "correctly, and a badly configured Vapi agent will perform worse than a well-configured "
  "opinionated platform. If you do not have an engineer who will care about turn-taking behaviour and "
  "provider latency characteristics, Retell's more opinionated design will serve you better.",
 ],
 features=[
  ("brain", "Model Provider Choice",
   "GPT, Claude, Gemini or Groq behind the same agent, so you can trade reasoning quality against "
   "latency and cost deliberately."),
  ("mic", "Voice Provider Choice",
   "ElevenLabs, Cartesia, Deepgram, PlayHT and others, because voice quality and latency trade off "
   "differently for every use case."),
  ("zap", "Latency Tuning",
   "Explicit control over the pipeline behaviour that determines whether a call feels like a "
   "conversation or a walkie-talkie exchange."),
  ("link", "Telephony Included",
   "Inbound and outbound phone numbers handled by the platform rather than wired up separately."),
  ("terminal", "Function Calling and Tools",
   "Agents call your APIs mid-conversation — checking availability, booking, looking up an account — "
   "which is what separates a useful agent from a voice FAQ."),
  ("activity", "Call Analytics and Recordings",
   "Transcripts, recordings and analytics for reviewing what agents actually said to customers."),
 ],
 pros=[
  "The most configurable voice platform available — every layer is yours to choose",
  "Competitive latency with optimised provider pairings",
  "Avoids lock-in to any single model or voice vendor",
  "Function calling makes agents genuinely useful rather than conversational",
  "The platform serious voice teams standardise on",
 ],
 cons=[
  "Configuration burden is real — bad choices produce a bad agent",
  "Steeper learning curve than opinionated alternatives",
  "Costs stack across model, voice and telephony providers",
  "Requires engineering ownership rather than a business user",
 ],
 pricing=[
  ("Pay as you go", "From ~$0.05 / minute", "Platform fee plus your model, voice and telephony costs"),
  ("Enterprise", "Custom", "Volume rates, dedicated support, compliance review"),
 ],
 excels=[
  "Engineering teams building voice as a core product capability",
  "Use cases where latency determines whether the product works",
  "Agents needing deep integration with internal APIs",
  "Teams that want to switch providers as the market moves",
 ],
 not_ideal=[
  "Business users wanting a no-code phone agent",
  "Simple call deflection where an opinionated platform is faster to ship",
  "Teams without engineering capacity to tune the pipeline",
 ],
 comparisons=[
  ("Vapi vs Retell AI",
   "Retell pairs a no-code builder with an SDK and transparent per-minute pricing; Vapi exposes "
   "everything and expects you to know what to do with it. Retell ships faster for standard use "
   "cases, Vapi goes further when voice is the product."),
  ("Vapi vs Bland AI",
   "Bland is cheaper at high outbound volume and tightly optimised for latency; Vapi is more flexible "
   "across providers and use cases. High-volume outbound favours Bland, complex integrated agents "
   "favour Vapi."),
 ],
 verdict="Vapi is the right platform when voice is a core capability rather than a feature. Exposing "
         "model, voice and telephony choices is what lets a team hit the latency that makes a call "
         "feel like a conversation, and function calling is what makes the agent useful once it is "
         "there. The flexibility is also the warning: every exposed knob is a decision you can get "
         "wrong, and an unconfigured Vapi agent underperforms a well-configured opinionated one. "
         "Choose it when you have an engineer who will own the pipeline, and choose Retell when you "
         "do not.",
 faq=[
  ("What latency can Vapi achieve?",
   "Around 500 to 600 milliseconds with optimised provider pairings. That matters because above "
   "roughly 800 milliseconds callers begin talking over the agent and the conversation breaks down."),
  ("Which models and voices does Vapi support?",
   "Model providers including GPT, Claude, Gemini and Groq, and voice providers including ElevenLabs, "
   "Cartesia, Deepgram and PlayHT. Mixing and matching is the point of the platform."),
  ("How does Vapi pricing work?",
   "A per-minute platform fee starting around $0.05, plus the costs of the model, voice and telephony "
   "providers you select. Model the full stack rather than the platform fee alone."),
  ("Should I use Vapi or Retell?",
   "Vapi if you have engineering ownership and voice is central to your product. Retell if you want "
   "to ship a standard voice agent quickly with predictable all-in pricing."),
 ],
 breakdown=[("Configurability", 9.8), ("Latency Control", 9.3),
            ("Integration Depth", 9.2), ("Ease of Adoption", 6.5), ("Value", 8.5)],
 related=[("retell-ai", "Retell AI", "4.5", "Production Voice Agents"),
          ("bland-ai", "Bland AI", "4.3", "High-Volume Outbound"),
          ("cartesia", "Cartesia", "4.5", "Real-Time Voice Models")],
),

]
