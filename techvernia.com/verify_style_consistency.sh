#!/bin/bash

echo "========================================================================"
echo "🔍 VÉRIFICATION DE LA COHÉRENCE DU STYLE"
echo "========================================================================"
echo ""

echo "📊 Vérification des fonts dans les pages de review..."
echo ""

# Compter combien de pages ont Space Grotesk
space_grotesk_count=$(grep -r "Space+Grotesk" pages/reviews/*/*.html | wc -l)
echo "✅ Pages avec Space Grotesk: $space_grotesk_count/127"

# Compter combien de pages ont Inter
inter_count=$(grep -r "family=Inter" pages/reviews/*/*.html | wc -l)
echo "✅ Pages avec Inter: $inter_count/127"

# Compter combien de pages ont JetBrains Mono
jetbrains_count=$(grep -r "JetBrains\+Mono" pages/reviews/*/*.html | wc -l)
echo "✅ Pages avec JetBrains Mono: $jetbrains_count/127"

echo ""
echo "🎨 Vérification du CSS inline style CrowdStrike..."
echo ""

# Vérifier la présence du style .review-hero
review_hero_count=$(grep -r "\.review-hero {" pages/reviews/*/*.html | wc -l)
echo "✅ Pages avec .review-hero: $review_hero_count/127"

# Vérifier la présence du style .rating-breakdown
rating_breakdown_count=$(grep -r "\.rating-breakdown {" pages/reviews/*/*.html | wc -l)
echo "✅ Pages avec .rating-breakdown: $rating_breakdown_count/127"

# Vérifier la présence du style .pros-cons-grid
pros_cons_count=$(grep -r "\.pros-cons-grid {" pages/reviews/*/*.html | wc -l)
echo "✅ Pages avec .pros-cons-grid: $pros_cons_count/127"

# Vérifier la présence du style .verdict-box
verdict_box_count=$(grep -r "\.verdict-box {" pages/reviews/*/*.html | wc -l)
echo "✅ Pages avec .verdict-box: $verdict_box_count/127"

echo ""
echo "📂 Vérification par catégorie..."
echo ""

for category in analytics customer-service education gaming hr legal quantum research sales translation; do
    count=$(ls -1 pages/reviews/$category/*.html 2>/dev/null | wc -l)
    echo "   $category: $count pages"
done

echo ""
echo "========================================================================"
echo "✅ VÉRIFICATION TERMINÉE"
echo "========================================================================"
