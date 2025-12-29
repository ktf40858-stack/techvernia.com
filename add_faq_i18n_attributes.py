import re
from pathlib import Path

TOOLS_WITH_FAQS = [
    'cortex-xdr', 'cisco-securex', 'crowdstrike', 'cyberark',
    'darktrace', 'fortinet', 'ibm-qradar', 'microsoft-sentinel',
    'okta', 'palo-alto-ngfw', 'qualys', 'rapid7', 'sentinelone',
    'sophos-interceptx', 'splunk-security', 'tenable',
    'trend-micro-vision-one'
]

base_dir = Path('GenuisNet.ai/pages/reviews/cybersecurity')

for tool in TOOLS_WITH_FAQS:
    html_file = base_dir / f'{tool}.html'
    if not html_file.exists():
        print(f'SKIP {tool}: File not found')
        continue
    
    content = html_file.read_text(encoding='utf-8')
    tool_key = tool.replace('-', '.')
    
    # Check if FAQs already have data-i18n
    if f'review.{tool_key}.faq.q1' in content:
        print(f'SKIP {tool}: FAQs already have data-i18n')
        continue
    
    # Find and replace FAQ items one by one
    modified = False
    faq_num = 1
    
    while True:
        # Look for FAQ pattern without data-i18n
        pattern = rf'<div class="feature-card"[^>]*>\s*<h4>([^<]+)</h4>\s*<p>([^<]+)</p>'
        match = re.search(pattern, content)
        
        if not match or faq_num > 10:
            break
        
        question = match.group(1)
        answer = match.group(2)
        
        # Create replacement with data-i18n
        q_key = f'review.{tool_key}.faq.q{faq_num}'
        a_key = f'review.{tool_key}.faq.a{faq_num}'
        
        replacement = f'<div class="feature-card" style="margin-bottom: var(--space-md);">\n<h4><span data-i18n="{q_key}">{question}</span></h4>\n<p><span data-i18n="{a_key}">{answer}</span></p>'
        
        # Replace only the first occurrence
        content = content.replace(match.group(0), replacement, 1)
        modified = True
        faq_num += 1
    
    if modified:
        html_file.write_text(content, encoding='utf-8')
        print(f'UPDATED {tool}: Added data-i18n to {faq_num-1} FAQs')
    else:
        print(f'SKIP {tool}: No FAQ items to update')

print('\nDone!')
