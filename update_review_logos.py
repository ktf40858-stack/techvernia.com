#!/usr/bin/env python3
"""
Script to update review logos from text initials to official logo images
"""

import os
import re
from pathlib import Path

# Base directory
BASE_DIR = Path("/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai")
REVIEWS_DIR = BASE_DIR / "pages" / "reviews"
LOGOS_DIR = BASE_DIR / "assets" / "images" / "logos"

# Mapping of review files to their logo files
# Format: filename (without .html) -> logo filename
LOGO_MAPPING = {
    # Cybersecurity
    "crowdstrike": "crowdstrike.png",
    "darktrace": "darktrace.png",
    "sentinelone": "sentinelone-new.png",
    "cybereason": "cybereason.png",
    "cylance": "cylance-new.svg",
    "fortinet": "fortinet.png",
    "abnormal-security": "abnormal-security.png",
    "recorded-future": "recorded-future.png",
    "zerofox": "zerofox.png",
    "splunk-security": "splunk-enterprise-security.png",
    "microsoft-sentinel": "microsoft-defender-ai.png",
    "exabeam": "exabeam.png",
    "cortex-xdr": "palo-alto.png",

    # Image Generation
    "canva-ai": "canva.png",
    "ideogram": "ideogram.png",
    "stable-diffusion": "stable-diffusion.png",
    "leonardo-ai": "leonardoai.png",
    "nightcafe": "nightcafe.png",
    "playground-ai": "playground-ai.png",
    "adobe-firefly": "adobe-firefly.png",
    "dreamstudio": "dreamstudio.png",
    "artbreeder": "artbreeder.png",

    # Writing
    "grammarly": "grammarly.png",
    "jasper-ai": "jasper.png",
    "rytr": "rytr-new.png",
    "wordtune": "wordtune.png",
    "writesonic": "writesonic.png",
    "quillbot": "quillbot.png",
    "prowritingaid": "prowritingaid.png",

    # Chatbots
    "chatgpt": "chatgpt.png",
    "claude": "claude.png",
    "gemini": "gemini.svg",
    "perplexity-ai": "perplexity-ai.png",
    "character-ai": "characterai.png",
    "poe": "poe.svg",
    "grok": "grok.png",
    "deepseek": "deepseek.png",
    "huggingchat": "huggingchat.svg",

    # Coding
    "cursor": "cursor.png",
    "github-copilot": "github-copilot.png",
    "tabnine": "tabnine.png",
    "codeium": "codeium.png",
    "amazon-codewhisperer": "amazon-codewhisperer.png",
    "sourcegraph-cody": "sourcegraph-cody.svg",
    "askcodi": "askcodi.png",
    "cohere": "cohere.png",

    # Video
    "runway-ml": "runway.png",
    "heygen": "heygen.png",
    "invideo-ai": "invideo-ai.png",
    "fliki": "fliki.png",
    "capcut": "capcut.png",
    "pika-labs": "pika-labs.png",

    # Audio
    "elevenlabs": "elevenlabs.png",
    "suno-ai": "suno-ai.png",
    "murf-ai": "murf.png",
    "speechify": "speechify.png",
    "play-ht": "playht.png",

    # SEO
    "clearscope": "clearscope.png",
    "surfer-seo": "surfer.png",
    "marketmuse": "marketmuse.png",
    "frase": "frase.png",
    "neuronwriter": "neuronwriter.png",
    "wordlift": "wordlift.png",
    "growthbar": "growthbar.png",
    "rankiq": "rankiq.png",
    "ink": "ink.png",

    # Productivity
    "notion-ai": "notion-ai.png",
    "clickup-ai": "clickup-ai.png",
    "fireflies-ai": "firefliesai.png",
    "otter-ai": "otterai.png",
    "motion": "motion.png",
    "taskade": "taskade.png",
    "sanebox": "sanebox.png",

    # Business
    "hubspot-ai": "hubspot-ai.png",
    "salesforce-einstein": "salesforce-einstein.svg",
    "ibm-watson": "ibm-watson.png",
    "datarobot": "datarobot.png",
    "h2o-ai": "h2oai.png",
    "power-bi-ai": "power-bi-ai.svg",
    "tableau-ai": "tableau-ai.png",
    "thoughtspot": "thoughtspot.png",
    "zoho-zia": "zoho-zia.png",

    # Networking
    "cisco-dna-center": "cisco-dna-center.png",
    "fortinet-fortiai": "fortinet-fortiai.png",
    "datadog": "datadog.png",
    "dynatrace": "dynatrace.png",
    "splunk": "splunk.png",
    "new-relic-ai": "new-relic-ai.png",
    "solarwinds-ai": "solarwinds-ai.png",
    "thousandeyes": "thousandeyes.png",
    "servicenow-ai": "servicenow-ai.png",

    # Medical
    "ibm-watson-health": "ibm-watson-health.png",
    "paige-ai": "paigeai.png",
    "path-ai": "pathai.png",
    "qure-ai": "qureai.png",
    "ada-health": "ada-health.png",
    "k-health": "k-health.png",

    # Architecture
    "autodesk-forma": "autodesk-forma.png",
    "spacemaker": "spacemaker.png",
    "hypar": "hypar.png",
    "openspace": "openspace.png",
    "reconstruct": "reconstruct.png",
}

def get_logo_path(filename, category):
    """Get the relative path to the logo from a review file"""
    logo_file = LOGO_MAPPING.get(filename)
    if not logo_file:
        return None

    # Check if logo exists
    logo_path = LOGOS_DIR / logo_file
    if not logo_path.exists():
        return None

    # Return relative path from review file to logo
    return f"../../../assets/images/logos/{logo_file}"

def update_review_logo(file_path):
    """Update the logo in a review file"""
    category = file_path.parent.name
    filename = file_path.stem

    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if already has an image logo
    if '<img' in content and 'review-logo' in content:
        print(f"  ⏭️  {filename} already has an image logo")
        return False

    # Find the review-logo div with text content
    logo_pattern = r'<div class="review-logo">([A-Z]{1,4})</div>'
    match = re.search(logo_pattern, content)

    if not match:
        print(f"  ⚠️  {filename} - No logo div found")
        return False

    # Get logo path
    logo_path = get_logo_path(filename, category)

    if not logo_path:
        print(f"  ⚠️  {filename} - No logo mapping found")
        return False

    # Create new logo HTML with fallback to initials
    initials = match.group(1)
    new_logo_html = f'<div class="review-logo"><img src="{logo_path}" alt="{filename} logo" style="width: 100%; height: 100%; object-fit: contain; padding: 10px;" onerror="this.outerHTML=\'<div style=\\\'display:flex;align-items:center;justify-content:center;width:100%;height:100%;font-size:2rem;font-weight:800;color:white;\\\'>{initials}</div>\'"></div>'

    # Replace the logo
    new_content = re.sub(logo_pattern, new_logo_html, content)

    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"  ✅ {filename} - Logo updated")
    return True

def main():
    """Main function to update all review logos"""
    print("🔄 Starting logo update process...\n")

    updated_count = 0
    skipped_count = 0
    error_count = 0

    # Process each category
    for category_dir in REVIEWS_DIR.iterdir():
        if not category_dir.is_dir():
            continue

        print(f"📁 Processing {category_dir.name}/")

        # Process each review file
        for review_file in category_dir.glob("*.html"):
            try:
                if update_review_logo(review_file):
                    updated_count += 1
                else:
                    skipped_count += 1
            except Exception as e:
                print(f"  ❌ {review_file.stem} - Error: {e}")
                error_count += 1

        print()

    print("=" * 50)
    print(f"✅ Updated: {updated_count} files")
    print(f"⏭️  Skipped: {skipped_count} files")
    print(f"❌ Errors: {error_count} files")
    print("=" * 50)

if __name__ == "__main__":
    main()
