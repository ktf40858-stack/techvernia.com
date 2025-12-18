#!/bin/bash
echo "=============================================="
echo "📊 STATISTIQUES COMPLÈTES:"
echo "=============================================="
echo ""
total=0
for cat in GenuisNet.ai/pages/reviews/*/; do
    catname=$(basename "$cat")
    count=$(ls "$cat"*.html 2>/dev/null | wc -l)
    total=$((total + count))
    if [ $count -gt 0 ]; then
        printf "  %-20s %3d reviews\n" "$catname:" "$count"
    fi
done
echo "  ────────────────────────────────"
printf "  %-20s %3d reviews\n" "TOTAL:" "$total"
echo ""
echo "✅ Traduits: 8 chatbots"
echo "⏳ Restants: $((total - 8)) reviews"
echo ""
