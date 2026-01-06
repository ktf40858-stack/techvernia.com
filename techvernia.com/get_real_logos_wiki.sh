#!/bin/bash
# Download real AI logos from Wikipedia and Wikimedia Commons (high quality, official)

BASE_DIR="/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/assets/images/tools"

echo "🎨 Downloading REAL AI logos from Wikimedia/Wikipedia..."
echo "================================================================"

# Writing Tools - Download from Wikimedia Commons (official logos)
echo -e "\n✍️  AI WRITING TOOLS"
echo "-----------------------------------"

# Grammarly - Official logo from Wikimedia
wget -q -O "${BASE_DIR}/writing/grammarly-temp.svg" "https://upload.wikimedia.org/wikipedia/commons/f/f8/Grammarly_Logo.svg" && \
  mv "${BASE_DIR}/writing/grammarly-temp.svg" "${BASE_DIR}/writing/grammarly.svg" && \
  echo "✓ Grammarly logo downloaded"

# For other tools, let's use DuckDuckGo image search API (no API key needed)
download_from_duckduckgo() {
    local category=$1
    local tool_name=$2
    local search_term=$3

    echo "  Searching for: $tool_name..."

    # Use DuckDuckGo instant answer API to find logo
    result=$(curl -s "https://api.duckduckgo.com/?q=${search_term}+logo&format=json&t=logoscript" | \
             python3 -c "import sys, json; data=json.load(sys.stdin); print(data.get('Image', ''))" 2>/dev/null)

    if [ ! -z "$result" ] && [ "$result" != "" ]; then
        wget -q -O "${BASE_DIR}/${category}/${tool_name}-temp.png" "$result"
        if [ -s "${BASE_DIR}/${category}/${tool_name}-temp.png" ]; then
            mv "${BASE_DIR}/${category}/${tool_name}-temp.png" "${BASE_DIR}/${category}/${tool_name}.png"
            echo "  ✓ $tool_name downloaded"
        else
            rm -f "${BASE_DIR}/${category}/${tool_name}-temp.png"
            echo "  ✗ $tool_name failed"
        fi
    fi
}

# Try Wikipedia/Wikimedia for each tool
download_from_duckduckgo "writing" "copyai" "Copy.ai"
download_from_duckduckgo "writing" "jasper-ai" "Jasper AI"
download_from_duckduckgo "writing" "quillbot" "QuillBot"
download_from_duckduckgo "writing" "rytr" "Rytr"
download_from_duckduckgo "writing" "wordtune" "Wordtune"
download_from_duckduckgo "writing" "writesonic" "Writesonic"

echo -e "\n================================================================"
echo "✅ Logo download attempt completed!"
echo "================================================================"
