#!/bin/bash
echo "=== COMPARAISON CHATBOTS vs WRITING ==="
echo ""

# ChatGPT (traduit avec le script)
en_gpt=$(grep -c '"review\.chatgpt\.' GenuisNet.ai/js/i18n.js)
fr_gpt=$(awk '/fr: \{/,/^    \}/' GenuisNet.ai/js/i18n.js | grep -c '"review\.chatgpt\.')
ratio_gpt=$((fr_gpt * 100 / en_gpt))
echo "ChatGPT (traduit avec script):"
echo "  EN: $en_gpt | FR: $fr_gpt | Ratio: ${ratio_gpt}%"

echo ""

# Copyai (NON traduit)
en_copy=$(grep -c '"review\.copyai\.' GenuisNet.ai/js/i18n.js)
fr_copy=$(awk '/fr: \{/,/^    \}/' GenuisNet.ai/js/i18n.js | grep -c '"review\.copyai\.')
ratio_copy=$((fr_copy * 100 / en_copy))
echo "Copyai (NON traduit):"
echo "  EN: $en_copy | FR: $fr_copy | Ratio: ${ratio_copy}%"

echo ""
echo "=== CONCLUSION ==="
echo "ChatGPT a un ratio de ~100% (presque toutes les clés EN ont leur traduction FR)"
echo "Copyai a un ratio de ~10% (seulement les clés génériques sont traduites)"
echo ""
echo "La catégorie WRITING n'est PAS complètement traduite!"
