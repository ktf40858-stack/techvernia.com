"""
Launch all remaining Cybersecurity translation agents
This script will be run via bash to launch agents in background
"""

# Tools already launched (first 9 tools):
# abnormal-security, carbon-black, cisco-securex (+ faqs), cortex-xdr (+ faqs),
# crowdstrike (+ faqs), cyberark (+ faqs), cybereason, cylance, darktrace (+ faqs)

# Remaining tools to launch
REMAINING_TOOLS = [
    'exabeam',
    'fortinet',  # has FAQs
    'ibm-qradar',  # has FAQs
    'lacework',
    'mcafee-mvision',
    'microsoft-sentinel',  # has FAQs
    'okta',  # has FAQs
    'palo-alto-ngfw',  # has FAQs
    'qualys',  # has FAQs
    'rapid7',  # has FAQs
    'recorded-future',
    'sentinelone',  # has FAQs
    'snyk',
    'sophos-interceptx',  # has FAQs
    'splunk-security',  # has FAQs
    'symantec-endpoint',
    'tenable',  # has FAQs
    'trend-micro-vision-one',  # has FAQs
    'vectra-ai',
    'wiz',
    'zerofox'
]

# Tools with FAQs (remaining)
TOOLS_WITH_FAQS = [
    'fortinet', 'ibm-qradar', 'microsoft-sentinel', 'okta',
    'palo-alto-ngfw', 'qualys', 'rapid7', 'sentinelone',
    'sophos-interceptx', 'splunk-security', 'tenable', 'trend-micro-vision-one'
]

print("REMAINING AGENTS TO LAUNCH")
print("=" * 60)

total_agents = 0

for tool in REMAINING_TOOLS:
    # Content batches (always 3)
    for batch in range(1, 4):
        langs = "ES/FR/DE" if batch == 1 else "PT/ZH/JA" if batch == 2 else "KO/AR/HI"
        print(f"claude_code task run --background --model haiku 'Translate GenuisNet.ai/pages/reviews/cybersecurity/{tool}-batch{batch}.json to {langs}. Add language sections. Save back.'")
        total_agents += 1

    # FAQ batches (if tool has FAQs)
    if tool in TOOLS_WITH_FAQS:
        for batch in range(1, 4):
            langs = "ES/FR/DE" if batch == 1 else "PT/ZH/JA" if batch == 2 else "KO/AR/HI"
            print(f"claude_code task run --background --model haiku 'Translate GenuisNet.ai/pages/reviews/cybersecurity/{tool}-faqs-batch{batch}.json to {langs}. Add language sections. Save back.'")
            total_agents += 1

print("\n" + "=" * 60)
print(f"Total remaining agents to launch: {total_agents}")
print("=" * 60)
