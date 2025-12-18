#!/usr/bin/env python3
"""
Fix category pages to use actual logo images instead of CSS backgrounds
"""

import re
from pathlib import Path

BASE_DIR = Path("/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai")
CATEGORIES_DIR = BASE_DIR / "pages" / "categories"

# Map of tool class names to their file names and categories
TOOL_MAPPINGS = {
    'ai-chatbots.html': {
        'chatgpt': ('chatbots', 'chatgpt'),
        'claude': ('chatbots', 'claude'),
        'gemini': ('chatbots', 'gemini'),
        'perplexity': ('chatbots', 'perplexity'),
        'copilot': ('chatbots', 'copilot'),
        'poe': ('chatbots', 'poe'),
        'grok': ('chatbots', 'grok'),
        'deepseek': ('chatbots', 'deepseek'),
    },
    'ai-coding.html': {
        'github-copilot': ('coding', 'github-copilot'),
        'cursor': ('coding', 'cursor'),
        'codeium': ('coding', 'codeium'),
        'tabnine': ('coding', 'tabnine'),
        'replit': ('coding', 'replit'),
        'codewhisperer': ('coding', 'codewhisperer'),
        'windsurf': ('coding', 'windsurf'),
        'deepseek-coder': ('coding', 'deepseek-coder'),
    },
    'ai-image.html': {
        'midjourney': ('image', 'midjourney'),
        'dall-e-3': ('image', 'dall-e-3'),
        'stable-diffusion': ('image', 'stable-diffusion'),
        'leonardo-ai': ('image', 'leonardo-ai'),
        'adobe-firefly': ('image', 'adobe-firefly'),
        'canva-ai': ('image', 'canva-ai'),
        'ideogram': ('image', 'ideogram'),
        'clipdrop': ('image', 'clipdrop'),
    },
    'ai-audio.html': {
        'elevenlabs': ('audio', 'elevenlabs'),
        'murf-ai': ('audio', 'murf-ai'),
        'descript': ('audio', 'descript'),
        'speechify': ('audio', 'speechify'),
        'playht': ('audio', 'playht'),
        'resemble-ai': ('audio', 'resemble-ai'),
        'suno-ai': ('audio', 'suno-ai'),
        'udio': ('audio', 'udio'),
    },
    'ai-video.html': {
        'runway': ('video', 'runway'),
        'heygen': ('video', 'heygen'),
        'synthesia': ('video', 'synthesia'),
        'pictory': ('video', 'pictory'),
        'invideo': ('video', 'invideo'),
        'lumen5': ('video', 'lumen5'),
        'kapwing': ('video', 'kapwing'),
        'kling-ai': ('video', 'kling-ai'),
    },
    'ai-writing.html': {
        'grammarly': ('writing', 'grammarly'),
        'jasper-ai': ('writing', 'jasper-ai'),
        'copyai': ('writing', 'copyai'),
        'writesonic': ('writing', 'writesonic'),
        'rytr': ('writing', 'rytr'),
        'quillbot': ('writing', 'quillbot'),
        'wordtune': ('writing', 'wordtune'),
    },
    'ai-productivity.html': {
        'notion-ai': ('productivity', 'notion-ai'),
        'clickup-ai': ('productivity', 'clickup-ai'),
        'motion': ('productivity', 'motion'),
        'zapier': ('productivity', 'zapier'),
        'otterai': ('productivity', 'otterai'),
        'firefliesai': ('productivity', 'firefliesai'),
        'reclaim-ai': ('productivity', 'reclaim-ai'),
        'mem-ai': ('productivity', 'mem-ai'),
    },
    'ai-seo.html': {
        'semrush': ('seo', 'semrush'),
        'ahrefs': ('seo', 'ahrefs'),
        'surfer-seo': ('seo', 'surfer-seo'),
        'frase': ('seo', 'frase'),
        'clearscope': ('seo', 'clearscope'),
        'marketmuse': ('seo', 'marketmuse'),
        'neuronwriter': ('seo', 'neuronwriter'),
        'scalenut': ('seo', 'scalenut'),
    },
    'ai-business.html': {
        'hubspot-ai': ('business', 'hubspot-ai'),
        'salesforce-einstein': ('business', 'salesforce-einstein'),
        'gong': ('business', 'gong'),
        'drift': ('business', 'drift'),
        'tableau': ('business', 'tableau'),
        'looker': ('business', 'looker'),
        'conversica': ('business', 'conversica'),
        'chorusai': ('business', 'chorusai'),
    },
    'ai-architecture.html': {
        'arko-ai': ('architecture', 'arko-ai'),
        'finch3d': ('architecture', 'finch3d'),
        'maket-ai': ('architecture', 'maket-ai'),
        'veras-ai': ('architecture', 'veras-ai'),
        'spacemaker-ai': ('architecture', 'spacemaker-ai'),
        'hypar': ('architecture', 'hypar'),
        'testfit': ('architecture', 'testfit'),
        'architechtures': ('architecture', 'architechtures'),
    },
    'ai-medical.html': {
        'butterfly-iq': ('medical', 'butterfly-iq'),
        'paige-ai': ('medical', 'paige-ai'),
        'zebra-medical': ('medical', 'zebra-medical'),
        'aidoc': ('medical', 'aidoc'),
        'tempus': ('medical', 'tempus'),
        'nuance-dragon': ('medical', 'nuance-dragon'),
        'pathai': ('medical', 'pathai'),
        'viz-ai': ('medical', 'viz-ai'),
    },
}

def find_logo_file(category, tool_name):
    """Find the actual logo file (PNG or SVG)"""
    assets_dir = BASE_DIR / "assets" / "images" / "tools"
    category_dir = assets_dir / category

    # Check for PNG first
    png_file = category_dir / f"{tool_name}.png"
    if png_file.exists():
        return f"{tool_name}.png"

    # Then check for SVG
    svg_file = category_dir / f"{tool_name}.svg"
    if svg_file.exists():
        return f"{tool_name}.svg"

    return None

def update_category_file(cat_file):
    """Update a category file to use img tags instead of CSS backgrounds"""
    try:
        content = cat_file.read_text(encoding='utf-8')
        original_content = content

        if cat_file.name not in TOOL_MAPPINGS:
            return False, "No mapping found"

        tools = TOOL_MAPPINGS[cat_file.name]
        updated = 0

        # Remove old CSS definitions for tool-logo-large.{tool}
        for tool_class in tools.keys():
            # Remove CSS background definitions
            css_pattern = rf'\s*\.tool-logo-large\.{re.escape(tool_class)}\s*\{{[^}}]+\}}\s*'
            content = re.sub(css_pattern, '', content)

        # Replace each div.tool-logo-large with img tag
        for tool_class, (category, tool_file) in tools.items():
            logo_file = find_logo_file(category, tool_file)
            if not logo_file:
                print(f"  Warning: No logo found for {tool_file}")
                continue

            logo_path = f"../../assets/images/tools/{category}/{logo_file}"

            # Pattern: <div class="tool-logo-large TOOLNAME"></div>
            # or <div class="tool-logo-large TOOLNAME" style="...">TEXT</div>
            old_pattern = rf'<div class="tool-logo-large {re.escape(tool_class)}"[^>]*>.*?</div>'
            new_tag = f'<img src="{logo_path}" alt="{tool_class} Logo" class="tool-logo-large" style="width: 80px; height: 80px; object-fit: contain; border-radius: 12px;">'

            if re.search(old_pattern, content):
                content = re.sub(old_pattern, new_tag, content)
                updated += 1

        if content != original_content:
            cat_file.write_text(content, encoding='utf-8')
            return True, f"Updated {updated} logos"

        return False, "No changes needed"

    except Exception as e:
        import traceback
        traceback.print_exc()
        return False, f"Error: {e}"

def update_all_categories():
    """Update all category pages"""
    total_updated = 0
    total_skipped = 0

    for cat_file in sorted(CATEGORIES_DIR.glob('ai-*.html')):
        if '.bak' not in cat_file.name:
            print(f"\nProcessing {cat_file.name}...")
            success, message = update_category_file(cat_file)

            if success:
                print(f"  ✓ {message}")
                total_updated += 1
            else:
                print(f"  ⊘ {message}")
                total_skipped += 1

    return total_updated, total_skipped

if __name__ == "__main__":
    print("=" * 70)
    print("UPDATING CATEGORY PAGES TO USE OFFICIAL LOGO IMAGES")
    print("=" * 70)

    updated, skipped = update_all_categories()

    print()
    print("=" * 70)
    print(f"Summary:")
    print(f"  ✅ Updated: {updated} category pages")
    print(f"  ⊘  Skipped: {skipped} category pages")
    print("=" * 70)
