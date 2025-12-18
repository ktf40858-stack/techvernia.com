#!/bin/bash
# Script to download official logos for all AI tools from Google Images / Official sources

BASE_DIR="/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/assets/images/tools"

echo "🔽 Starting logo download process..."
echo "=================================="

# Function to download logo
download_logo() {
    local category=$1
    local tool_name=$2
    local search_query=$3
    local output_file="${BASE_DIR}/${category}/${tool_name}.svg"

    echo "📥 Downloading: $tool_name ($category)..."

    # Try multiple sources in order
    # 1. Try Brandfetch API (free tier)
    curl -s "https://api.brandfetch.io/v2/brands/${search_query}" | jq -r '.logos[0].formats[] | select(.format=="svg") | .src' | head -1 | xargs -I {} curl -s -o "$output_file" {}

    # 2. If failed, try logo.dev
    if [ ! -s "$output_file" ]; then
        curl -s -o "$output_file" "https://img.logo.dev/${search_query}?token=pk_X-1ZO13CRaadr0E7e2bMvQ&format=svg"
    fi

    # 3. If still failed, use clearbit (fallback to PNG)
    if [ ! -s "$output_file" ]; then
        rm -f "$output_file"
        curl -s -o "${BASE_DIR}/${category}/${tool_name}.png" "https://logo.clearbit.com/${search_query}"
    fi

    # Check if download successful
    if [ -s "${BASE_DIR}/${category}/${tool_name}.svg" ] || [ -s "${BASE_DIR}/${category}/${tool_name}.png" ]; then
        echo "  ✓ Success"
    else
        echo "  ✗ Failed"
    fi
}

# WRITING TOOLS
echo -e "\n✍️  AI WRITING TOOLS"
echo "-----------------------------------"
download_logo "writing" "copyai" "copy.ai"
download_logo "writing" "grammarly" "grammarly.com"
download_logo "writing" "jasper-ai" "jasper.ai"
download_logo "writing" "quillbot" "quillbot.com"
download_logo "writing" "rytr" "rytr.me"
download_logo "writing" "wordtune" "wordtune.com"
download_logo "writing" "writesonic" "writesonic.com"

# IMAGE TOOLS
echo -e "\n🎨 AI IMAGE GENERATION"
echo "-----------------------------------"
download_logo "image" "adobe-firefly" "adobe.com"
download_logo "image" "canva-ai" "canva.com"
download_logo "image" "clipdrop" "clipdrop.co"
download_logo "image" "dall-e-3" "openai.com"
download_logo "image" "ideogram" "ideogram.ai"
download_logo "image" "leonardo-ai" "leonardo.ai"
download_logo "image" "midjourney" "midjourney.com"
download_logo "image" "stable-diffusion" "stability.ai"

# VIDEO TOOLS
echo -e "\n🎬 AI VIDEO TOOLS"
echo "-----------------------------------"
download_logo "video" "heygen" "heygen.com"
download_logo "video" "invideo" "invideo.io"
download_logo "video" "kapwing" "kapwing.com"
download_logo "video" "kling-ai" "klingai.com"
download_logo "video" "lumen5" "lumen5.com"
download_logo "video" "pictory" "pictory.ai"
download_logo "video" "runway" "runwayml.com"
download_logo "video" "synthesia" "synthesia.io"

# CYBERSECURITY TOOLS
echo -e "\n🛡️  AI CYBERSECURITY"
echo "-----------------------------------"
download_logo "cybersecurity" "abnormal-security" "abnormalsecurity.com"
download_logo "cybersecurity" "cisco-securex" "cisco.com"
download_logo "cybersecurity" "cortex-xdr" "paloaltonetworks.com"
download_logo "cybersecurity" "crowdstrike" "crowdstrike.com"
download_logo "cybersecurity" "cyberark" "cyberark.com"
download_logo "cybersecurity" "cylance" "blackberry.com"
download_logo "cybersecurity" "darktrace" "darktrace.com"
download_logo "cybersecurity" "fortinet" "fortinet.com"
download_logo "cybersecurity" "ibm-qradar" "ibm.com"
download_logo "cybersecurity" "lacework" "lacework.com"
download_logo "cybersecurity" "microsoft-sentinel" "microsoft.com"
download_logo "cybersecurity" "okta" "okta.com"
download_logo "cybersecurity" "palo-alto-ngfw" "paloaltonetworks.com"
download_logo "cybersecurity" "qualys" "qualys.com"
download_logo "cybersecurity" "rapid7" "rapid7.com"
download_logo "cybersecurity" "sentinelone" "sentinelone.com"
download_logo "cybersecurity" "snyk" "snyk.io"
download_logo "cybersecurity" "splunk-security" "splunk.com"
download_logo "cybersecurity" "tenable" "tenable.com"
download_logo "cybersecurity" "vectra-ai" "vectra.ai"
download_logo "cybersecurity" "wiz" "wiz.io"

echo -e "\n=================================="
echo "✅ Logo download process completed!"
echo "=================================="
echo ""
echo "📊 Run this to verify:"
echo "python3 verify_tool_logos.py"
