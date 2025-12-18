#!/bin/bash
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║           VÉRIFICATION DU FICHIER IMAGE                   ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""

if [ ! -f "image_translations.json" ]; then
    echo "❌ Fichier non trouvé!"
    exit 1
fi

SIZE=$(du -h image_translations.json | cut -f1)
echo "📁 Fichier: image_translations.json"
echo "📊 Taille: ${SIZE}"
echo ""

echo "🌍 LANGUES DISPONIBLES:"
jq 'keys' image_translations.json | grep -v '\[' | grep -v '\]' | sed 's/[",]//g' | sed 's/^/  • /'
echo ""

echo "🔢 NOMBRE DE CLÉS PAR LANGUE:"
jq '. | to_entries | .[] | "  \(.key): \(.value | keys | length) clés"' image_translations.json | sed 's/"//g'
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📝 EXEMPLES DE TRADUCTIONS"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

echo "Clé: review.midjourney.title"
echo "  EN: $(jq -r '.en["review.midjourney.title"]' image_translations.json 2>/dev/null || echo 'N/A')"
echo "  FR: $(jq -r '.fr["review.midjourney.title"]' image_translations.json 2>/dev/null || echo 'N/A')"
echo "  ES: $(jq -r '.es["review.midjourney.title"]' image_translations.json 2>/dev/null || echo 'N/A')"
echo "  DE: $(jq -r '.de["review.midjourney.title"]' image_translations.json 2>/dev/null || echo 'N/A')"
echo ""

echo "Clé: review.dall-e-3.pricing.free"
echo "  EN: $(jq -r '.en["review.dalle3.pricing.free"]' image_translations.json 2>/dev/null || echo 'N/A')"
echo "  FR: $(jq -r '.fr["review.dalle3.pricing.free"]' image_translations.json 2>/dev/null || echo 'N/A')"
echo "  ES: $(jq -r '.es["review.dalle3.pricing.free"]' image_translations.json 2>/dev/null || echo 'N/A')"
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "✅ VÉRIFICATION TERMINÉE"
echo ""
echo "🎯 Si tout est OK, lancer l'intégration:"
echo "   python3 step2_integrate_translations.py image"
echo ""
