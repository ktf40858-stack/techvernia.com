#!/bin/bash
echo "=============================================="
echo "RAPPORT SUR L'ÉTAT DES TRADUCTIONS"
echo "=============================================="
echo ""
echo "📊 CHATBOTS TRADUITS (8/8):"
for tool in chatgpt claude copilot deepseek gemini grok perplexity poe; do
    if [ -f "${tool}_translations_all_langs.json" ]; then
        echo "  ✅ $tool"
    else
        echo "  ❌ $tool"
    fi
done

echo ""
echo "📊 CATÉGORIES À TRAITER:"
echo ""

categories=("coding" "image" "video" "writing" "seo" "cybersecurity" "analytics" "business" "networking" "productivity")

for cat in "${categories[@]}"; do
    count=$(ls GenuisNet.ai/pages/reviews/$cat/*.html 2>/dev/null | wc -l)
    if [ $count -gt 0 ]; then
        echo "  📁 $cat: $count reviews"
        ls GenuisNet.ai/pages/reviews/$cat/*.html 2>/dev/null | sed 's|.*/||' | sed 's/.html$//' | sed 's/^/     - /'
        echo ""
    fi
done

echo "=============================================="
echo "📝 FICHIERS DE TRADUCTION EXISTANTS:"
echo "=============================================="
ls *_translations_all_langs.json 2>/dev/null | sed 's/_translations_all_langs.json$//'

echo ""
echo "=============================================="
echo "🎯 PROCHAINES ÉTAPES RECOMMANDÉES:"
echo "=============================================="
echo "1. Traiter les 8 outils CODING"
echo "2. Traiter les 8 outils IMAGE"
echo "3. Traiter les 8 outils VIDEO"
echo "4. Traiter les 7 outils WRITING"
echo "5. Traiter les 8 outils SEO"
echo "6. Traiter les 30 outils CYBERSECURITY"
echo ""
