#!/usr/bin/env python3
"""
Generate professional SVG logos for all AI tools
Uses brand colors and initials for each tool
"""

import os
from pathlib import Path

BASE_DIR = Path("/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/assets/images/tools")

# Logo definitions with brand colors
LOGOS = {
    'architecture': {
        'arko-ai': {'name': 'Arko AI', 'color': '#0EA5E9', 'initials': 'AR'},
        'finch3d': {'name': 'Finch 3D', 'color': '#10B981', 'initials': 'F3'},
        'maket-ai': {'name': 'Maket', 'color': '#8B5CF6', 'initials': 'MK'},
        'veras-ai': {'name': 'Veras', 'color': '#F97316', 'initials': 'VR'},
        'spacemaker-ai': {'name': 'Spacemaker', 'color': '#EF4444', 'initials': 'SM'},
        'hypar': {'name': 'Hypar', 'color': '#06B6D4', 'initials': 'HP'},
        'testfit': {'name': 'TestFit', 'color': '#7C3AED', 'initials': 'TF'},
        'architechtures': {'name': 'Architechtures', 'color': '#EC4899', 'initials': 'AT'},
    },
    'medical': {
        'butterfly-iq': {'name': 'Butterfly iQ', 'color': '#3B82F6', 'initials': 'BF'},
        'paige-ai': {'name': 'Paige', 'color': '#10B981', 'initials': 'PG'},
        'zebra-medical': {'name': 'Zebra', 'color': '#8B5CF6', 'initials': 'ZM'},
        'aidoc': {'name': 'Aidoc', 'color': '#EF4444', 'initials': 'AD'},
        'tempus': {'name': 'Tempus', 'color': '#F97316', 'initials': 'TP'},
        'nuance-dragon': {'name': 'Dragon', 'color': '#06B6D4', 'initials': 'DR'},
        'pathai': {'name': 'PathAI', 'color': '#7C3AED', 'initials': 'PA'},
        'viz-ai': {'name': 'Viz.ai', 'color': '#EC4899', 'initials': 'VZ'},
    },
    'audio': {
        'descript': {'name': 'Descript', 'color': '#8B5CF6', 'initials': 'DS'},
        'elevenlabs': {'name': 'ElevenLabs', 'color': '#8B5CF6', 'initials': '11'},
        'murf-ai': {'name': 'Murf', 'color': '#3B82F6', 'initials': 'MF'},
        'playht': {'name': 'Play.ht', 'color': '#3B82F6', 'initials': 'PH'},
        'resemble-ai': {'name': 'Resemble', 'color': '#10B981', 'initials': 'RS'},
        'speechify': {'name': 'Speechify', 'color': '#F59E0B', 'initials': 'SP'},
        'suno-ai': {'name': 'Suno', 'color': '#EC4899', 'initials': 'SU'},
        'udio': {'name': 'Udio', 'color': '#8B5CF6', 'initials': 'UD'},
    },
    'video': {
        'heygen': {'name': 'HeyGen', 'color': '#F97316', 'initials': 'HG'},
        'invideo': {'name': 'InVideo', 'color': '#3B82F6', 'initials': 'IV'},
        'kapwing': {'name': 'Kapwing', 'color': '#EF4444', 'initials': 'KW'},
        'kling-ai': {'name': 'Kling', 'color': '#8B5CF6', 'initials': 'KL'},
        'lumen5': {'name': 'Lumen5', 'color': '#06B6D4', 'initials': 'L5'},
        'pictory': {'name': 'Pictory', 'color': '#10B981', 'initials': 'PT'},
        'runway': {'name': 'Runway', 'color': '#EC4899', 'initials': 'RW'},
        'synthesia': {'name': 'Synthesia', 'color': '#7C3AED', 'initials': 'SY'},
    },
    'writing': {
        'copyai': {'name': 'Copy.ai', 'color': '#8B5CF6', 'initials': 'CP'},
        'grammarly': {'name': 'Grammarly', 'color': '#10B981', 'initials': 'GR'},
        'jasper-ai': {'name': 'Jasper', 'color': '#7C3AED', 'initials': 'JP'},
        'quillbot': {'name': 'QuillBot', 'color': '#06B6D4', 'initials': 'QB'},
        'rytr': {'name': 'Rytr', 'color': '#F59E0B', 'initials': 'RY'},
        'wordtune': {'name': 'Wordtune', 'color': '#3B82F6', 'initials': 'WT'},
        'writesonic': {'name': 'Writesonic', 'color': '#EC4899', 'initials': 'WS'},
    },
    'productivity': {
        'clickup-ai': {'name': 'ClickUp', 'color': '#EC4899', 'initials': 'CU'},
        'firefliesai': {'name': 'Fireflies', 'color': '#8B5CF6', 'initials': 'FF'},
        'mem-ai': {'name': 'Mem', 'color': '#06B6D4', 'initials': 'MM'},
        'motion': {'name': 'Motion', 'color': '#7C3AED', 'initials': 'MT'},
        'notion-ai': {'name': 'Notion', 'color': '#000000', 'initials': 'NT'},
        'otterai': {'name': 'Otter.ai', 'color': '#3B82F6', 'initials': 'OT'},
        'reclaim-ai': {'name': 'Reclaim', 'color': '#10B981', 'initials': 'RC'},
        'zapier': {'name': 'Zapier', 'color': '#F59E0B', 'initials': 'ZP'},
    },
    'seo': {
        'ahrefs': {'name': 'Ahrefs', 'color': '#F97316', 'initials': 'AH'},
        'clearscope': {'name': 'Clearscope', 'color': '#10B981', 'initials': 'CS'},
        'frase': {'name': 'Frase', 'color': '#3B82F6', 'initials': 'FR'},
        'marketmuse': {'name': 'MarketMuse', 'color': '#7C3AED', 'initials': 'MM'},
        'neuronwriter': {'name': 'Neuron', 'color': '#06B6D4', 'initials': 'NW'},
        'scalenut': {'name': 'Scalenut', 'color': '#8B5CF6', 'initials': 'SN'},
        'semrush': {'name': 'Semrush', 'color': '#EF4444', 'initials': 'SR'},
        'surfer-seo': {'name': 'Surfer', 'color': '#EC4899', 'initials': 'SF'},
    },
    'business': {
        'chorusai': {'name': 'Chorus', 'color': '#8B5CF6', 'initials': 'CH'},
        'conversica': {'name': 'Conversica', 'color': '#3B82F6', 'initials': 'CV'},
        'drift': {'name': 'Drift', 'color': '#06B6D4', 'initials': 'DR'},
        'gong': {'name': 'Gong', 'color': '#EC4899', 'initials': 'GG'},
        'hubspot-ai': {'name': 'HubSpot', 'color': '#F97316', 'initials': 'HS'},
        'looker': {'name': 'Looker', 'color': '#4285F4', 'initials': 'LK'},
        'salesforce-einstein': {'name': 'Einstein', 'color': '#00A1E0', 'initials': 'SF'},
        'tableau': {'name': 'Tableau', 'color': '#E97627', 'initials': 'TB'},
    },
    'image': {
        'adobe-firefly': {'name': 'Firefly', 'color': '#FF0000', 'initials': 'AF'},
        'canva-ai': {'name': 'Canva', 'color': '#00C4CC', 'initials': 'CV'},
        'clipdrop': {'name': 'ClipDrop', 'color': '#8B5CF6', 'initials': 'CD'},
        'dall-e-3': {'name': 'DALL·E', 'color': '#10A37F', 'initials': 'DE'},
        'ideogram': {'name': 'Ideogram', 'color': '#7C3AED', 'initials': 'ID'},
        'leonardo-ai': {'name': 'Leonardo', 'color': '#8B5CF6', 'initials': 'LA'},
        'midjourney': {'name': 'Midjourney', 'color': '#000000', 'initials': 'MJ'},
        'stable-diffusion': {'name': 'Stable Diff', 'color': '#6366F1', 'initials': 'SD'},
    },
    'chatbots': {
        'chatgpt': {'name': 'ChatGPT', 'color': '#10A37F', 'initials': 'GP'},
        'claude': {'name': 'Claude', 'color': '#D97706', 'initials': 'CL'},
        'copilot': {'name': 'Copilot', 'color': '#0078D4', 'initials': 'CP'},
        'deepseek': {'name': 'DeepSeek', 'color': '#0EA5E9', 'initials': 'DS'},
        'gemini': {'name': 'Gemini', 'color': '#4285F4', 'initials': 'GM'},
        'grok': {'name': 'Grok', 'color': '#000000', 'initials': 'GK'},
        'perplexity': {'name': 'Perplexity', 'color': '#1FB6FF', 'initials': 'PX'},
        'poe': {'name': 'Poe', 'color': '#EF4444', 'initials': 'PO'},
    },
    'coding': {
        'codeium': {'name': 'Codeium', 'color': '#09B6A2', 'initials': 'CD'},
        'codewhisperer': {'name': 'CodeWhisperer', 'color': '#FF9900', 'initials': 'CW'},
        'cursor': {'name': 'Cursor', 'color': '#000000', 'initials': 'CR'},
        'deepseek-coder': {'name': 'DeepSeek', 'color': '#8B5CF6', 'initials': 'DC'},
        'github-copilot': {'name': 'Copilot', 'color': '#000000', 'initials': 'GC'},
        'replit': {'name': 'Replit', 'color': '#F26207', 'initials': 'RP'},
        'tabnine': {'name': 'Tabnine', 'color': '#3B7EBF', 'initials': 'TN'},
        'windsurf': {'name': 'Windsurf', 'color': '#06B6D4', 'initials': 'WS'},
    },
}

def create_svg_logo(name, color, initials):
    """Create a professional SVG logo"""
    # Calculate lighter color for gradient
    return f'''<svg width="120" height="120" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad-{initials}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{color};stop-opacity:1" />
      <stop offset="100%" style="stop-color:{color};stop-opacity:0.7" />
    </linearGradient>
  </defs>
  <rect width="120" height="120" rx="24" fill="url(#grad-{initials})"/>
  <text x="60" y="75" font-family="Inter, sans-serif" font-size="36" font-weight="700" fill="white" text-anchor="middle">{initials}</text>
</svg>'''

def generate_all_logos():
    """Generate logos for all tools"""
    total = 0
    for category, tools in LOGOS.items():
        category_dir = BASE_DIR / category
        category_dir.mkdir(parents=True, exist_ok=True)

        for tool_id, info in tools.items():
            svg_content = create_svg_logo(info['name'], info['color'], info['initials'])
            svg_file = category_dir / f"{tool_id}.svg"
            svg_file.write_text(svg_content)
            total += 1
            print(f"✓ Created {category}/{tool_id}.svg ({info['name']})")

    print(f"\n✅ Generated {total} logos successfully!")
    return total

if __name__ == "__main__":
    print("=" * 60)
    print("GENERATING PROFESSIONAL SVG LOGOS FOR ALL AI TOOLS")
    print("=" * 60)
    print()
    total = generate_all_logos()
    print()
    print("=" * 60)
    print(f"COMPLETE: {total} logos created")
    print("=" * 60)
