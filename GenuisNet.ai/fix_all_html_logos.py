#!/usr/bin/env python3
"""
Script to fix all SVG files that are actually HTML documents.
Creates proper SVG logos for each tool.
"""

import os
import shutil

# Logo templates with brand colors
LOGO_TEMPLATES = {
    # Medical
    'butterfly-iq': {'color': '#00D4FF', 'icon': 'B', 'name': 'Butterfly iQ'},
    'tempus': {'color': '#FF6B35', 'icon': 'T', 'name': 'Tempus'},
    'paige-ai': {'color': '#4A90E2', 'icon': 'P', 'name': 'Paige.AI'},
    'pathai': {'color': '#8B5CF6', 'icon': 'P', 'name': 'PathAI'},
    'nuance-dragon': {'color': '#0078D4', 'icon': 'N', 'name': 'Nuance Dragon'},
    'aidoc': {'color': '#10B981', 'icon': 'A', 'name': 'Aidoc'},
    'viz-ai': {'color': '#EF4444', 'icon': 'V', 'name': 'Viz.ai'},

    # Productivity
    'firefliesai': {'color': '#FFB800', 'icon': 'F', 'name': 'Fireflies.ai'},
    'otterai': {'color': '#00C9FF', 'icon': 'O', 'name': 'Otter.ai'},
    'reclaim-ai': {'color': '#8B5CF6', 'icon': 'R', 'name': 'Reclaim AI'},
    'mem-ai': {'color': '#FF6B6B', 'icon': 'M', 'name': 'Mem.ai'},
    'motion': {'color': '#6366F1', 'icon': 'M', 'name': 'Motion'},
    'clickup-ai': {'color': '#7B68EE', 'icon': 'C', 'name': 'ClickUp AI'},

    # Business
    'looker': {'color': '#4285F4', 'icon': 'L', 'name': 'Looker'},
    'gong': {'color': '#FF6B35', 'icon': 'G', 'name': 'Gong'},
    'conversica': {'color': '#00C9A7', 'icon': 'C', 'name': 'Conversica'},
    'salesforce-einstein': {'color': '#00A1E0', 'icon': 'E', 'name': 'Einstein'},
    'drift': {'color': '#2D3748', 'icon': 'D', 'name': 'Drift'},

    # Architecture
    'finch3d': {'color': '#FF6B35', 'icon': 'F', 'name': 'Finch3D'},
    'maket-ai': {'color': '#8B5CF6', 'icon': 'M', 'name': 'Maket.ai'},
    'arko-ai': {'color': '#00D9FF', 'icon': 'A', 'name': 'Arko AI'},
    'testfit': {'color': '#10B981', 'icon': 'T', 'name': 'TestFit'},
    'spacemaker-ai': {'color': '#4A90E2', 'icon': 'S', 'name': 'Spacemaker'},
    'hypar': {'color': '#FF6B35', 'icon': 'H', 'name': 'Hypar'},

    # Writing
    'jasper-ai': {'color': '#8B5CF6', 'icon': 'J', 'name': 'Jasper'},

    # Coding
    'codeium': {'color': '#00D9FF', 'icon': 'C', 'name': 'Codeium'},
    'windsurf': {'color': '#00C9A7', 'icon': 'W', 'name': 'Windsurf'},
    'tabnine': {'color': '#FF6B35', 'icon': 'T', 'name': 'Tabnine'},

    # Video
    'kapwing': {'color': '#FF6B35', 'icon': 'K', 'name': 'Kapwing'},
    'invideo': {'color': '#4A90E2', 'icon': 'I', 'name': 'InVideo'},
    'lumen5': {'color': '#00D9FF', 'icon': 'L', 'name': 'Lumen5'},
    'kling-ai': {'color': '#8B5CF6', 'icon': 'K', 'name': 'Kling AI'},
    'synthesia': {'color': '#6366F1', 'icon': 'S', 'name': 'Synthesia'},
    'heygen': {'color': '#FF6B35', 'icon': 'H', 'name': 'HeyGen'},

    # SEO
    'marketmuse': {'color': '#8B5CF6', 'icon': 'M', 'name': 'MarketMuse'},
    'semrush': {'color': '#FF6B35', 'icon': 'S', 'name': 'Semrush'},
    'surfer-seo': {'color': '#00D9FF', 'icon': 'S', 'name': 'Surfer SEO'},
    'neuronwriter': {'color': '#4A90E2', 'icon': 'N', 'name': 'NeuronWriter'},
    'scalenut': {'color': '#10B981', 'icon': 'S', 'name': 'Scalenut'},
    'frase': {'color': '#6366F1', 'icon': 'F', 'name': 'Frase'},
    'ahrefs': {'color': '#FF6B35', 'icon': 'A', 'name': 'Ahrefs'},

    # Audio
    'speechify': {'color': '#00C9FF', 'icon': 'S', 'name': 'Speechify'},
    'resemble-ai': {'color': '#8B5CF6', 'icon': 'R', 'name': 'Resemble AI'},
    'playht': {'color': '#FF6B35', 'icon': 'P', 'name': 'Play.ht'},
    'suno-ai': {'color': '#00D9FF', 'icon': 'S', 'name': 'Suno AI'},
    'udio': {'color': '#6366F1', 'icon': 'U', 'name': 'Udio'},
    'murf-ai': {'color': '#4A90E2', 'icon': 'M', 'name': 'Murf AI'},
    'descript': {'color': '#8B5CF6', 'icon': 'D', 'name': 'Descript'},
}

def create_svg_logo(tool_id, color, icon, name):
    """Create a clean SVG logo for a tool."""
    return f'''<svg width="200" height="200" viewBox="0 0 200 200" fill="none" xmlns="http://www.w3.org/2000/svg">
  <!-- {name} Logo -->
  <rect width="200" height="200" rx="20" fill="#000000"/>

  <!-- Letter Icon -->
  <text x="100" y="115" font-family="Arial, sans-serif" font-size="80" font-weight="700" fill="{color}" text-anchor="middle">{icon}</text>

  <!-- Brand Text -->
  <text x="100" y="170" font-family="Arial, sans-serif" font-size="14" font-weight="600" fill="#FFFFFF" text-anchor="middle">{name.upper()}</text>

  <!-- Accent -->
  <circle cx="100" cy="50" r="8" fill="{color}" opacity="0.6"/>
</svg>
'''

def main():
    base_path = "/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/assets/images/tools"

    fixed_count = 0

    for tool_id, config in LOGO_TEMPLATES.items():
        # Find the SVG file
        for root, dirs, files in os.walk(base_path):
            for file in files:
                if file == f"{tool_id}.svg":
                    file_path = os.path.join(root, file)

                    # Backup the old file
                    backup_path = file_path + ".backup"
                    if not os.path.exists(backup_path):
                        shutil.copy2(file_path, backup_path)

                    # Create new SVG
                    svg_content = create_svg_logo(
                        tool_id,
                        config['color'],
                        config['icon'],
                        config['name']
                    )

                    # Write the new SVG
                    with open(file_path, 'w') as f:
                        f.write(svg_content)

                    print(f"✓ Fixed: {tool_id} ({file_path})")
                    fixed_count += 1

    print(f"\n✓ Total fixed: {fixed_count} logos")

if __name__ == "__main__":
    main()
