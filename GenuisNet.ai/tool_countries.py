#!/usr/bin/env python3
"""
Database of AI tool countries of origin.
Maps tool slugs to their country with flag emoji.
"""

TOOL_COUNTRIES = {
    # Chatbots
    'chatgpt': {'country': 'United States', 'flag': '🇺🇸'},
    'claude': {'country': 'United States', 'flag': '🇺🇸'},
    'gemini': {'country': 'United States', 'flag': '🇺🇸'},
    'copilot': {'country': 'United States', 'flag': '🇺🇸'},
    'perplexity': {'country': 'United States', 'flag': '🇺🇸'},
    'you-com': {'country': 'United States', 'flag': '🇺🇸'},
    'deepseek': {'country': 'China', 'flag': '🇨🇳'},
    'grok': {'country': 'United States', 'flag': '🇺🇸'},

    # Writing
    'jasper-ai': {'country': 'United States', 'flag': '🇺🇸'},
    'copy-ai': {'country': 'United States', 'flag': '🇺🇸'},
    'writesonic': {'country': 'United States', 'flag': '🇺🇸'},
    'rytr': {'country': 'United States', 'flag': '🇺🇸'},
    'anyword': {'country': 'Israel', 'flag': '🇮🇱'},
    'wordtune': {'country': 'Israel', 'flag': '🇮🇱'},
    'quillbot': {'country': 'United States', 'flag': '🇺🇸'},

    # Image
    'midjourney': {'country': 'United States', 'flag': '🇺🇸'},
    'dall-e-3': {'country': 'United States', 'flag': '🇺🇸'},
    'stable-diffusion': {'country': 'United Kingdom', 'flag': '🇬🇧'},
    'leonardo-ai': {'country': 'Australia', 'flag': '🇦🇺'},
    'ideogram': {'country': 'United States', 'flag': '🇺🇸'},
    'adobe-firefly': {'country': 'United States', 'flag': '🇺🇸'},
    'canva-ai': {'country': 'Australia', 'flag': '🇦🇺'},
    'clipdrop': {'country': 'France', 'flag': '🇫🇷'},

    # Video
    'runway': {'country': 'United States', 'flag': '🇺🇸'},
    'synthesia': {'country': 'United Kingdom', 'flag': '🇬🇧'},
    'heygen': {'country': 'United States', 'flag': '🇺🇸'},
    'kling-ai': {'country': 'China', 'flag': '🇨🇳'},
    'invideo': {'country': 'United States', 'flag': '🇺🇸'},
    'kapwing': {'country': 'United States', 'flag': '🇺🇸'},
    'lumen5': {'country': 'Canada', 'flag': '🇨🇦'},
    'pictory': {'country': 'United States', 'flag': '🇺🇸'},

    # Audio
    'elevenlabs': {'country': 'United States', 'flag': '🇺🇸'},
    'murf-ai': {'country': 'United States', 'flag': '🇺🇸'},
    'resemble-ai': {'country': 'Canada', 'flag': '🇨🇦'},
    'playht': {'country': 'United States', 'flag': '🇺🇸'},
    'speechify': {'country': 'United States', 'flag': '🇺🇸'},
    'descript': {'country': 'United States', 'flag': '🇺🇸'},
    'suno-ai': {'country': 'United States', 'flag': '🇺🇸'},
    'udio': {'country': 'United States', 'flag': '🇺🇸'},

    # Coding
    'github-copilot': {'country': 'United States', 'flag': '🇺🇸'},
    'cursor': {'country': 'United States', 'flag': '🇺🇸'},
    'tabnine': {'country': 'Israel', 'flag': '🇮🇱'},
    'codeium': {'country': 'United States', 'flag': '🇺🇸'},
    'replit': {'country': 'United States', 'flag': '🇺🇸'},
    'amazon-q': {'country': 'United States', 'flag': '🇺🇸'},
    'cody': {'country': 'United States', 'flag': '🇺🇸'},
    'windsurf': {'country': 'United States', 'flag': '🇺🇸'},

    # Productivity
    'notion-ai': {'country': 'United States', 'flag': '🇺🇸'},
    'otter-ai': {'country': 'United States', 'flag': '🇺🇸'},
    'fireflies-ai': {'country': 'United States', 'flag': '🇺🇸'},
    'mem-ai': {'country': 'United States', 'flag': '🇺🇸'},
    'motion': {'country': 'United States', 'flag': '🇺🇸'},
    'reclaim-ai': {'country': 'United States', 'flag': '🇺🇸'},
    'clickup': {'country': 'United States', 'flag': '🇺🇸'},
    'clockwise': {'country': 'United States', 'flag': '🇺🇸'},

    # SEO
    'surfer-seo': {'country': 'Poland', 'flag': '🇵🇱'},
    'jasper': {'country': 'United States', 'flag': '🇺🇸'},
    'frase': {'country': 'United States', 'flag': '🇺🇸'},
    'marketmuse': {'country': 'United States', 'flag': '🇺🇸'},
    'semrush': {'country': 'United States', 'flag': '🇺🇸'},
    'ahrefs': {'country': 'Singapore', 'flag': '🇸🇬'},
    'clearscope': {'country': 'United States', 'flag': '🇺🇸'},
    'neuronwriter': {'country': 'Poland', 'flag': '🇵🇱'},

    # Business
    'salesforce-einstein': {'country': 'United States', 'flag': '🇺🇸'},
    'hubspot-ai': {'country': 'United States', 'flag': '🇺🇸'},
    'gong': {'country': 'United States', 'flag': '🇺🇸'},
    'drift': {'country': 'United States', 'flag': '🇺🇸'},
    'conversica': {'country': 'United States', 'flag': '🇺🇸'},
    'looker': {'country': 'United States', 'flag': '🇺🇸'},
    'tableau': {'country': 'United States', 'flag': '🇺🇸'},
    'powerbi': {'country': 'United States', 'flag': '🇺🇸'},

    # Cybersecurity
    'crowdstrike': {'country': 'United States', 'flag': '🇺🇸'},
    'darktrace': {'country': 'United Kingdom', 'flag': '🇬🇧'},
    'sentinelone': {'country': 'United States', 'flag': '🇺🇸'},
    'palo-alto-ngfw': {'country': 'United States', 'flag': '🇺🇸'},
    'cortex-xdr': {'country': 'United States', 'flag': '🇺🇸'},
    'splunk-security': {'country': 'United States', 'flag': '🇺🇸'},
    'microsoft-sentinel': {'country': 'United States', 'flag': '🇺🇸'},
    'ibm-qradar': {'country': 'United States', 'flag': '🇺🇸'},
    'fortinet': {'country': 'United States', 'flag': '🇺🇸'},
    'cisco-securex': {'country': 'United States', 'flag': '🇺🇸'},
    'vectra-ai': {'country': 'United States', 'flag': '🇺🇸'},
    'cyberark': {'country': 'Israel', 'flag': '🇮🇱'},
    'okta': {'country': 'United States', 'flag': '🇺🇸'},
    'abnormal-security': {'country': 'United States', 'flag': '🇺🇸'},
    'wiz': {'country': 'United States', 'flag': '🇺🇸'},
    'lacework': {'country': 'United States', 'flag': '🇺🇸'},
    'snyk': {'country': 'United Kingdom', 'flag': '🇬🇧'},
    'tenable': {'country': 'United States', 'flag': '🇺🇸'},
    'qualys': {'country': 'United States', 'flag': '🇺🇸'},
    'rapid7': {'country': 'United States', 'flag': '🇺🇸'},
    'cylance': {'country': 'United States', 'flag': '🇺🇸'},

    # Architecture
    'finch3d': {'country': 'United States', 'flag': '🇺🇸'},
    'maket-ai': {'country': 'United States', 'flag': '🇺🇸'},
    'arko-ai': {'country': 'United States', 'flag': '🇺🇸'},
    'testfit': {'country': 'United States', 'flag': '🇺🇸'},
    'spacemaker': {'country': 'Norway', 'flag': '🇳🇴'},
    'hypar': {'country': 'United States', 'flag': '🇺🇸'},
    'veras': {'country': 'United States', 'flag': '🇺🇸'},
    'gendo-ai': {'country': 'United Kingdom', 'flag': '🇬🇧'},

    # Medical
    'tempus': {'country': 'United States', 'flag': '🇺🇸'},
    'paige-ai': {'country': 'United States', 'flag': '🇺🇸'},
    'butterfly-iq': {'country': 'United States', 'flag': '🇺🇸'},
    'nuance-dragon': {'country': 'United States', 'flag': '🇺🇸'},
    'aidoc': {'country': 'Israel', 'flag': '🇮🇱'},
    'pathfinder': {'country': 'United States', 'flag': '🇺🇸'},
    'viz-ai': {'country': 'United States', 'flag': '🇺🇸'},
    'enlitic': {'country': 'United States', 'flag': '🇺🇸'},
}

def get_country_info(tool_slug):
    """Get country information for a tool."""
    return TOOL_COUNTRIES.get(tool_slug, {'country': 'International', 'flag': '🌐'})
