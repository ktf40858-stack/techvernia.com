import re
from pathlib import Path
import json

CYBERSECURITY_TOOLS = [
    'cisco-securex', 'cortex-xdr', 'crowdstrike', 'cyberark', 'darktrace',
    'fortinet', 'ibm-qradar', 'microsoft-sentinel', 'okta', 'palo-alto-ngfw',
    'qualys', 'rapid7', 'sentinelone', 'sophos-interceptx', 'splunk-security',
    'tenable', 'trend-micro-vision-one', 'abnormal-security', 'carbon-black',
    'cybereason', 'cylance', 'exabeam', 'lacework', 'mcafee-mvision',
    'recorded-future', 'snyk', 'symantec-endpoint', 'vectra-ai', 'wiz', 'zerofox'
]

base_dir = Path('GenuisNet.ai/pages/reviews/cybersecurity')

# Common section titles that need translation
common_titles = {}

for tool in CYBERSECURITY_TOOLS:
    html_file = base_dir / f'{tool}.html'
    if not html_file.exists():
        continue
    
    content = html_file.read_text(encoding='utf-8')
    
    # Find H2 titles without data-i18n (excluding those with SVG icons)
    h2_pattern = r'<h2>(?!<span data-i18n)(?!<svg)(.*?)</h2>'
    h2_matches = re.findall(h2_pattern, content)
    
    # Find H3 titles without data-i18n
    h3_pattern = r'<h3>(?!<span data-i18n)(.*?)</h3>'
    h3_matches = re.findall(h3_pattern, content)
    
    for title in h2_matches + h3_matches:
        # Clean up HTML tags and trim
        clean_title = re.sub(r'<[^>]+>', '', title).strip()
        if clean_title and len(clean_title) > 2:
            if clean_title not in common_titles:
                common_titles[clean_title] = []
            if tool not in common_titles[clean_title]:
                common_titles[clean_title].append(tool)

# Display common titles
print("COMMON SECTION TITLES FOUND:")
print("=" * 80)
for title, tools in sorted(common_titles.items(), key=lambda x: -len(x[1])):
    print(f"\n'{title}'")
    print(f"  Used in {len(tools)} tools: {', '.join(tools[:5])}")
    if len(tools) > 5:
        print(f"  ... and {len(tools)-5} more")

# Create a mapping of standard titles
standard_titles = {
    "Best Use Cases": "review.common.best.use.cases",
    "Best For:": "review.common.best.for",
    "Best For": "review.common.best.for",
    "May Not Be Ideal For:": "review.common.may.not.be.ideal.for",
    "May Not Be Ideal For": "review.common.may.not.be.ideal.for",
    "Comparison": "review.common.comparison",
    "Platform Comparison": "review.common.platform.comparison",
    "Key Advantages": "review.common.key.advantages",
    "Considerations": "review.common.considerations",
    "Final Verdict": "review.common.final.verdict",
    "Quick Stats": "review.common.quick.stats",
    "Frequently Asked Questions": "review.common.frequently.asked.questions",
}

# Create English source file for common titles
common_en = {}
for title, key in standard_titles.items():
    common_en[key] = title

# Save to JSON
output_file = Path('GenuisNet.ai/pages/reviews/cybersecurity/common-section-titles-en.json')
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(common_en, f, indent=2, ensure_ascii=False)

print(f"\n\nCreated: {output_file}")
print(f"Total common titles to translate: {len(common_en)}")

