"""
Check which Cybersecurity tools have all batches completed
"""
import os
import json

TOOLS = [
    'abnormal-security', 'carbon-black', 'cisco-securex', 'cortex-xdr',
    'crowdstrike', 'cyberark', 'cybereason', 'cylance', 'darktrace',
    'exabeam', 'fortinet', 'ibm-qradar', 'lacework', 'mcafee-mvision',
    'microsoft-sentinel', 'okta', 'palo-alto-ngfw', 'qualys', 'rapid7',
    'recorded-future', 'sentinelone', 'snyk', 'sophos-interceptx',
    'splunk-security', 'symantec-endpoint', 'tenable',
    'trend-micro-vision-one', 'vectra-ai', 'wiz', 'zerofox'
]

TOOLS_WITH_FAQS = [
    'cisco-securex', 'cortex-xdr', 'crowdstrike', 'cyberark', 'darktrace',
    'fortinet', 'ibm-qradar', 'microsoft-sentinel', 'okta', 'palo-alto-ngfw',
    'qualys', 'rapid7', 'sentinelone', 'sophos-interceptx', 'splunk-security',
    'tenable', 'trend-micro-vision-one'
]

def check_batch_file(file_path):
    """Check if batch file has translations (file size > 5KB and has language sections)"""
    if not os.path.exists(file_path):
        return False

    file_size = os.path.getsize(file_path)
    if file_size < 5000:  # Less than 5KB
        return False

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Check if it has at least 2 language sections (en + 1 translated)
        if len(data) < 2:
            return False

        # Check if non-English sections have content
        for lang in ['es', 'fr', 'de', 'pt', 'zh', 'ja', 'ko', 'ar', 'hi']:
            if lang in data and len(data[lang]) > 10:  # Has at least 10 translations
                return True

        return False
    except:
        return False

def check_tool_completion(tool_name):
    """Check if all batches for a tool are completed"""
    base_path = "GenuisNet.ai/pages/reviews/cybersecurity"
    has_faqs = tool_name in TOOLS_WITH_FAQS

    # Check content batches
    batches_done = 0
    for batch_num in range(1, 4):
        batch_file = f"{base_path}/{tool_name}-batch{batch_num}.json"
        if check_batch_file(batch_file):
            batches_done += 1

    content_complete = (batches_done == 3)

    # Check FAQ batches if applicable
    faq_complete = True
    faq_batches_done = 0
    if has_faqs:
        for batch_num in range(1, 4):
            faq_file = f"{base_path}/{tool_name}-faqs-batch{batch_num}.json"
            if check_batch_file(faq_file):
                faq_batches_done += 1
        faq_complete = (faq_batches_done == 3)

    return {
        'content_batches': batches_done,
        'content_complete': content_complete,
        'faq_batches': faq_batches_done if has_faqs else 0,
        'faq_complete': faq_complete,
        'fully_complete': content_complete and faq_complete
    }

# Check all tools
print("\n" + "=" * 70)
print("CYBERSECURITY TOOLS - COMPLETION STATUS")
print("=" * 70)

completed_tools = []
partial_tools = []
not_started = []

for tool in TOOLS:
    status = check_tool_completion(tool)
    has_faqs = tool in TOOLS_WITH_FAQS

    if status['fully_complete']:
        completed_tools.append(tool)
        status_icon = "[OK]"
    elif status['content_batches'] > 0 or status['faq_batches'] > 0:
        partial_tools.append(tool)
        status_icon = "[..]"
    else:
        not_started.append(tool)
        status_icon = "[XX]"

    if has_faqs:
        print(f"{status_icon} {tool}: Content {status['content_batches']}/3, FAQs {status['faq_batches']}/3")
    else:
        print(f"{status_icon} {tool}: Content {status['content_batches']}/3")

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"[OK] Fully completed: {len(completed_tools)}")
print(f"[..] Partially completed: {len(partial_tools)}")
print(f"[XX] Not started: {len(not_started)}")

if completed_tools:
    print(f"\nREADY TO GENERATE I18N FILES ({len(completed_tools)} tools):")
    for tool in completed_tools:
        print(f"   - {tool}")

if partial_tools:
    print(f"\nIN PROGRESS ({len(partial_tools)} tools):")
    for tool in partial_tools:
        status = check_tool_completion(tool)
        has_faqs = tool in TOOLS_WITH_FAQS
        if has_faqs:
            print(f"   - {tool}: {status['content_batches']}/3 content, {status['faq_batches']}/3 FAQs")
        else:
            print(f"   - {tool}: {status['content_batches']}/3 batches")

print("\n" + "=" * 70)
