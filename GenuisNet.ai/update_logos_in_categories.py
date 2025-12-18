#!/usr/bin/env python3
"""
Update category pages to use SVG logos in tool cards
"""

import re
from pathlib import Path

BASE_DIR = Path("/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai")
CATEGORIES_DIR = BASE_DIR / "pages" / "categories"

# Map of tool names to their file names
TOOL_MAPPINGS = {
    'ai-architecture.html': [
        ('Arko AI', 'arko-ai'),
        ('Finch 3D', 'finch3d'),
        ('Maket AI', 'maket-ai'),
        ('Veras AI', 'veras-ai'),
        ('Spacemaker AI', 'spacemaker-ai'),
        ('Hypar', 'hypar'),
        ('TestFit', 'testfit'),
        ('Architechtures', 'architechtures'),
    ],
    'ai-medical.html': [
        ('Butterfly iQ', 'butterfly-iq'),
        ('Paige AI', 'paige-ai'),
        ('Zebra Medical', 'zebra-medical'),
        ('Aidoc', 'aidoc'),
        ('Tempus', 'tempus'),
        ('Dragon Medical', 'nuance-dragon'),
        ('PathAI', 'pathai'),
        ('Viz.ai', 'viz-ai'),
    ],
    'ai-audio.html': [
        ('Descript', 'descript'),
        ('ElevenLabs', 'elevenlabs'),
        ('Murf AI', 'murf-ai'),
        ('Play.ht', 'playht'),
        ('Resemble AI', 'resemble-ai'),
        ('Speechify', 'speechify'),
        ('Suno AI', 'suno-ai'),
        ('Udio', 'udio'),
    ],
    'ai-video.html': [
        ('HeyGen', 'heygen'),
        ('InVideo', 'invideo'),
        ('Kapwing', 'kapwing'),
        ('Kling AI', 'kling-ai'),
        ('Lumen5', 'lumen5'),
        ('Pictory', 'pictory'),
        ('Runway', 'runway'),
        ('Synthesia', 'synthesia'),
    ],
    'ai-writing.html': [
        ('Copy.ai', 'copyai'),
        ('Grammarly', 'grammarly'),
        ('Jasper AI', 'jasper-ai'),
        ('QuillBot', 'quillbot'),
        ('Rytr', 'rytr'),
        ('Wordtune', 'wordtune'),
        ('Writesonic', 'writesonic'),
    ],
    'ai-productivity.html': [
        ('ClickUp AI', 'clickup-ai'),
        ('Fireflies.ai', 'firefliesai'),
        ('Mem', 'mem-ai'),
        ('Motion', 'motion'),
        ('Notion AI', 'notion-ai'),
        ('Otter.ai', 'otterai'),
        ('Reclaim.ai', 'reclaim-ai'),
        ('Zapier', 'zapier'),
    ],
    'ai-seo.html': [
        ('Ahrefs', 'ahrefs'),
        ('Clearscope', 'clearscope'),
        ('Frase', 'frase'),
        ('MarketMuse', 'marketmuse'),
        ('Neuron Writer', 'neuronwriter'),
        ('Scalenut', 'scalenut'),
        ('Semrush', 'semrush'),
        ('Surfer SEO', 'surfer-seo'),
    ],
    'ai-business.html': [
        ('Chorus.ai', 'chorusai'),
        ('Conversica', 'conversica'),
        ('Drift', 'drift'),
        ('Gong', 'gong'),
        ('HubSpot AI', 'hubspot-ai'),
        ('Looker', 'looker'),
        ('Salesforce Einstein', 'salesforce-einstein'),
        ('Tableau', 'tableau'),
    ],
    'ai-image.html': [
        ('Adobe Firefly', 'adobe-firefly'),
        ('Canva AI', 'canva-ai'),
        ('ClipDrop', 'clipdrop'),
        ('DALL-E 3', 'dall-e-3'),
        ('Ideogram', 'ideogram'),
        ('Leonardo AI', 'leonardo-ai'),
        ('Midjourney', 'midjourney'),
        ('Stable Diffusion', 'stable-diffusion'),
    ],
    'ai-chatbots.html': [
        ('ChatGPT', 'chatgpt'),
        ('Claude', 'claude'),
        ('Copilot', 'copilot'),
        ('DeepSeek', 'deepseek'),
        ('Gemini', 'gemini'),
        ('Grok', 'grok'),
        ('Perplexity', 'perplexity'),
        ('Poe', 'poe'),
    ],
    'ai-coding.html': [
        ('Codeium', 'codeium'),
        ('CodeWhisperer', 'codewhisperer'),
        ('Cursor', 'cursor'),
        ('DeepSeek Coder', 'deepseek-coder'),
        ('GitHub Copilot', 'github-copilot'),
        ('Replit', 'replit'),
        ('Tabnine', 'tabnine'),
        ('Windsurf', 'windsurf'),
    ],
}

def update_category_page(cat_file):
    """Update a category page to use SVG logos"""
    try:
        content = cat_file.read_text(encoding='utf-8')
        original_content = content

        # Get category name
        cat_name = cat_file.stem.replace('ai-', '')

        if cat_file.name not in TOOL_MAPPINGS:
            return False

        # Update each tool's logo
        for tool_display, tool_file in TOOL_MAPPINGS[cat_file.name]:
            logo_path = f"../../assets/images/tools/{cat_name}/{tool_file}.svg"

            # Pattern: Find tool-icon divs and replace with img
            # Look for the tool name and update nearby logo
            pattern = rf'<div class="tool-icon">([^<]*)</div>'

            def replacer(match):
                return f'<div class="tool-icon">\n                        <img src="{logo_path}" alt="{tool_display} Logo" style="width: 100%; height: 100%; object-fit: contain;">\n                    </div>'

            # Only replace within the context of this specific tool
            # Find the tool card section
            tool_section_pattern = rf'(<div class="tool-card"[^>]*>.*?){pattern}(.*?</div>\s*</div>\s*</a>)'
            if tool_display in content:
                # More targeted replacement
                pass

        # Generic approach: replace all tool-icon divs with empty content with img tags
        # But we need to know which tool it is... Let's use a different approach

        # Find all tool cards and update them
        updated = 0
        for tool_display, tool_file in TOOL_MAPPINGS[cat_file.name]:
            if tool_display in content:
                logo_path = f"../../assets/images/tools/{cat_name}/{tool_file}.svg"

                # Find the tool card containing this tool name
                # Look for pattern: <div class="tool-icon"> followed by just letters/numbers or empty
                old_pattern = rf'(<a[^>]*href="\.\.\/reviews\/{cat_name}\/{tool_file}\.html"[^>]*>.*?<div class="tool-icon">)([^<]*)(</div>)'

                if re.search(old_pattern, content, re.DOTALL):
                    content = re.sub(
                        old_pattern,
                        rf'\1<img src="{logo_path}" alt="{tool_display} Logo" style="width: 48px; height: 48px; object-fit: contain;">\3',
                        content,
                        flags=re.DOTALL
                    )
                    updated += 1

        if content != original_content:
            cat_file.write_text(content, encoding='utf-8')
            return True

        return False

    except Exception as e:
        print(f"Error updating {cat_file}: {e}")
        import traceback
        traceback.print_exc()
        return False

def update_all_categories():
    """Update all category pages"""
    updated = 0

    for cat_file in CATEGORIES_DIR.glob('ai-*.html'):
        if '.bak' not in cat_file.name and 'backup' not in cat_file.name:
            print(f"Processing {cat_file.name}...")
            if update_category_page(cat_file):
                print(f"  ✓ Updated {cat_file.name}")
                updated += 1
            else:
                print(f"  ⊘ Skipped {cat_file.name}")

    return updated

if __name__ == "__main__":
    print("=" * 70)
    print("UPDATING CATEGORY PAGES TO USE SVG LOGOS")
    print("=" * 70)
    print()

    updated = update_all_categories()

    print()
    print("=" * 70)
    print(f"✅ Updated: {updated} category pages")
    print("=" * 70)
