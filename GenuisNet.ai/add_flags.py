#!/usr/bin/env python3
import re
import sys

def add_flags_to_file(filepath):
    """Add country flags next to ratings in HTML file"""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Mapping of companies to flags and their AI tools
    company_flags = {
        'by OpenAI': '🇺🇸',
        'by Anthropic': '🇺🇸',
        'by Google': '🇺🇸',
        'by Perplexity': '🇺🇸',
        'by Microsoft': '🇺🇸',
        'by Quora': '🇺🇸',
        'GitHub': '🇺🇸',
        'Cursor': '🇺🇸',
        'Codeium': '🇺🇸',
        'Tabnine': '🇮🇱',
        'Replit': '🇺🇸',
        'Amazon': '🇺🇸',
        'Stability AI': '🇬🇧',
        'Midjourney': '🇺🇸',
        'Runway': '🇺🇸',
        'HeyGen': '🇨🇳',
        'Synthesia': '🇬🇧',
        'ElevenLabs': '🇺🇸',
        'Suno': '🇺🇸',
        'Cisco': '🇺🇸',
        'Juniper': '🇺🇸',
        'CrowdStrike': '🇺🇸',
        'Darktrace': '🇬🇧',
        'Palo Alto': '🇺🇸',
        'Fortinet': '🇺🇸',
        'SentinelOne': '🇺🇸',
    }

    # Find all tool sections and add flags
    modified = False
    for company, flag in company_flags.items():
        # Pattern: company name followed by rating badge (without flag already)
        pattern = f'(by {company}.*?)<span class="badge badge-rating">([^<]+)</span>(?!\s*<span class="country-flag")'

        if company in content:
            # Check if flag doesn't already exist
            if f'badge-rating">{company.split()[-1]}' not in content or 'country-flag' not in content[content.find(company):content.find(company)+500]:
                replacement = r'\1<span class="badge badge-rating">\2</span>\n                                <span class="country-flag" style="font-size: 1.2em; opacity: 0.7;">' + flag + '</span>'
                new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
                if new_content != content:
                    content = new_content
                    modified = True
                    print(f"✓ Added flag {flag} for {company}")

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"\n✅ File updated: {filepath}")
        return True
    else:
        print(f"⚠️  No changes made to: {filepath}")
        return False

if __name__ == '__main__':
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        filepath = 'pages/categories/ai-chatbots.html'

    add_flags_to_file(filepath)
