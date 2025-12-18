#!/bin/bash
echo "========================================================"
echo "VÉRIFICATION COMPLÈTE DES TRADUCTIONS"
echo "========================================================"
echo ""

# Liste des catégories avec exemples d'outils
declare -A categories=(
    ["writing"]="copyai grammarly jasper-ai"
    ["coding"]="cursor github-copilot windsurf"
    ["image"]="midjourney dall-e-3 stable-diffusion"
    ["video"]="runway heygen synthesia"
    ["seo"]="ahrefs semrush surfer-seo"
)

for cat in "${!categories[@]}"; do
    echo "=== CATÉGORIE: ${cat^^} ==="
    for tool in ${categories[$cat]}; do
        # Compte dans section EN
        en_count=$(grep -c "\"review\.${tool}\." GenuisNet.ai/js/i18n.js)
        # Compte dans section FR
        fr_count=$(awk '/fr: \{/,/^    \}/' GenuisNet.ai/js/i18n.js | grep -c "\"review\.${tool}\.")
        
        if [ $en_count -gt 0 ]; then
            ratio=$((fr_count * 100 / en_count))
            echo "  $tool: EN=$en_count | FR=$fr_count (${ratio}%)"
        else
            echo "  $tool: ❌ Aucune clé trouvée"
        fi
    done
    echo ""
done

echo "========================================================"
