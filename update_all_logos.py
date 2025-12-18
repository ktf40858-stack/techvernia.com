#!/usr/bin/env python3
"""
Script to update all review logos to point to the official logos folder
"""

import os
import re
from pathlib import Path

# Base directory
BASE_DIR = Path("/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai")
REVIEWS_DIR = BASE_DIR / "pages" / "reviews"
LOGOS_DIR = BASE_DIR / "assets" / "images" / "logos"

# Mapping of tool names to their official logo files
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
    "palo-alto-cortex": "palo-alto.png",
    "vectra-ai": "vectra.png",
    "ibm-qradar": "ibm-qradar.png",

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
    "jasper": "jasper.png",
    "rytr": "rytr-new.png",
    "wordtune": "wordtune.png",
    "writesonic": "writesonic.png",
    "quillbot": "quillbot.png",
    "prowritingaid": "prowritingaid.png",
    "copyai": "copyai.png",
    "copy-ai": "copyai.png",

    # Chatbots
    "chatgpt": "chatgpt.png",
    "claude": "claude.png",
    "gemini": "gemini.svg",
    "perplexity-ai": "perplexity-ai.png",
    "perplexity": "perplexity-ai.png",
    "character-ai": "characterai.png",
    "poe": "poe.svg",
    "grok": "grok.png",
    "deepseek": "deepseek.png",
    "huggingchat": "huggingchat.svg",
    "copilot": "copilot.png",

    # Coding
    "cursor": "cursor.png",
    "github-copilot": "github-copilot.png",
    "tabnine": "tabnine.png",
    "codeium": "codeium.png",
    "amazon-codewhisperer": "amazon-codewhisperer.png",
    "codewhisperer": "amazon-codewhisperer.png",
    "sourcegraph-cody": "sourcegraph-cody.svg",
    "askcodi": "askcodi.png",
    "cohere": "cohere.png",

    # Video
    "runway": "runway.png",
    "runway-ml": "runway.png",
    "heygen": "heygen.png",
    "invideo-ai": "invideo-ai.png",
    "invideo": "invideo-ai.png",
    "fliki": "fliki.png",
    "capcut": "capcut.png",
    "pika-labs": "pika-labs.png",

    # Audio
    "elevenlabs": "elevenlabs.png",
    "suno-ai": "suno-ai.png",
    "murf-ai": "murf.png",
    "speechify": "speechify.png",
    "play-ht": "playht.png",
    "playht": "playht.png",

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
    "firefliesai": "firefliesai.png",
    "otter-ai": "otterai.png",
    "otterai": "otterai.png",
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
    "tableau": "tableau-ai.png",
    "thoughtspot": "thoughtspot.png",
    "zoho-zia": "zoho-zia.png",

    # Networking
    "cisco-dna-center": "cisco-dna-center.png",
    "cisco-ai": "cisco-dna-center.png",
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
    "pathai": "pathai.png",
    "qure-ai": "qureai.png",
    "ada-health": "ada-health.png",
    "k-health": "k-health.png",

    # Architecture
    "autodesk-forma": "autodesk-forma.png",
    "spacemaker": "spacemaker.png",
    "spacemaker-ai": "spacemaker.png",
    "hypar": "hypar.png",
    "openspace": "openspace.png",
    "reconstruct": "reconstruct.png",
}

def get_logo_filename(review_file):
    """Get the logo filename for a review file"""
    filename = review_file.stem
    return LOGO_MAPPING.get(filename)

def update_logo_path(file_path):
    """Update the logo path in a review file"""
    filename = file_path.stem

    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Get the official logo filename
    logo_file = get_logo_filename(file_path)

    if not logo_file:
        print(f"  ⚠️  {filename} - No logo mapping")
        return False

    # Check if logo exists
    logo_path = LOGOS_DIR / logo_file
    if not logo_path.exists():
        print(f"  ⚠️  {filename} - Logo file not found: {logo_file}")
        return False

    new_logo_path = f"../../../assets/images/logos/{logo_file}"

    # Pattern 1: Images in tool-logo-xl divs (most common format)
    pattern1 = r'(<div class="tool-logo-xl">\s*<img src=")([^"]+)(" alt="[^"]*"[^>]*>)'
    if re.search(pattern1, content):
        new_content = re.sub(pattern1, rf'\1{new_logo_path}\3', content)
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  ✅ {filename} - Logo path updated (tool-logo-xl)")
            return True

    # Pattern 2: Images in review-logo divs (cybersecurity format)
    pattern2 = r'(<div class="review-logo">\s*<img src=")([^"]+)(" alt="[^"]*"[^>]*>)'
    if re.search(pattern2, content):
        new_content = re.sub(pattern2, rf'\1{new_logo_path}\3', content)
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  ✅ {filename} - Logo path updated (review-logo)")
            return True

    # Pattern 3: Text-only logo divs - add image
    pattern3 = r'<div class="(tool-logo-xl|review-logo)">([A-Z]{1,4})</div>'
    match = re.search(pattern3, content)
    if match:
        class_name = match.group(1)
        initials = match.group(2)
        new_logo_html = f'<div class="{class_name}"><img src="{new_logo_path}" alt="{filename} logo" style="width: 80%; height: 80%; object-fit: contain;"></div>'
        new_content = re.sub(pattern3, new_logo_html, content)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  ✅ {filename} - Logo added (was text: {initials})")
        return True

    print(f"  ⏭️  {filename} - No logo element found")
    return False

def main():
    """Main function to update all review logos"""
    print("🔄 Starting logo path update process...\n")

    updated_count = 0
    skipped_count = 0
    error_count = 0

    # Process each category
    for category_dir in sorted(REVIEWS_DIR.iterdir()):
        if not category_dir.is_dir():
            continue

        print(f"📁 Processing {category_dir.name}/")

        # Process each review file
        for review_file in sorted(category_dir.glob("*.html")):
            try:
                if update_logo_path(review_file):
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
