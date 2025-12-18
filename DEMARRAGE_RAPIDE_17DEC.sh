#!/bin/bash
# Script de démarrage rapide pour le 17 décembre
# Traitement IMAGE + VIDEO en 2 étapes

set -e

echo "╔═══════════════════════════════════════════════════════════╗"
echo "║  TRADUCTION IMAGE + VIDEO EN 2 ÉTAPES (AVEC VÉRIFICATION) ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""

cd "/home/komet/Desktop/Projekt/AI Tools"

# ═════════════════════════════════════════════════════════════════
# PARTIE 1: CATÉGORIE IMAGE
# ═════════════════════════════════════════════════════════════════

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🖼️  CATÉGORIE IMAGE"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

echo "📥 ÉTAPE 1/4: Génération des traductions IMAGE..."
python3 step1_generate_translations.py image

echo ""
echo "🔍 Fichier généré: image_translations.json"
echo ""
echo "❓ Voulez-vous vérifier le fichier avant de continuer?"
echo "   (tapez 'v' pour vérifier, ou Entrée pour continuer)"
read -p "Votre choix: " choice

if [ "$choice" = "v" ] || [ "$choice" = "V" ]; then
    echo ""
    echo "📊 Nombre de clés:"
    cat image_translations.json | jq '.en | keys | length'
    echo ""
    echo "📝 Exemple de traductions (3 premières clés):"
    cat image_translations.json | jq '.fr | to_entries | .[0:3]'
    echo ""
    read -p "Appuyez sur Entrée pour continuer avec l'intégration..."
fi

echo ""
echo "💉 ÉTAPE 2/4: Intégration IMAGE dans i18n.js..."
python3 step2_integrate_translations.py image

echo ""
echo "✅ IMAGE TERMINÉ!"
echo ""

# ═════════════════════════════════════════════════════════════════
# PARTIE 2: CATÉGORIE VIDEO
# ═════════════════════════════════════════════════════════════════

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🎬 CATÉGORIE VIDEO"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

echo "📥 ÉTAPE 3/4: Génération des traductions VIDEO..."
python3 step1_generate_translations.py video

echo ""
echo "🔍 Fichier généré: video_translations.json"
echo ""
echo "❓ Voulez-vous vérifier le fichier avant de continuer?"
echo "   (tapez 'v' pour vérifier, ou Entrée pour continuer)"
read -p "Votre choix: " choice

if [ "$choice" = "v" ] || [ "$choice" = "V" ]; then
    echo ""
    echo "📊 Nombre de clés:"
    cat video_translations.json | jq '.en | keys | length'
    echo ""
    echo "📝 Exemple de traductions (3 premières clés):"
    cat video_translations.json | jq '.fr | to_entries | .[0:3]'
    echo ""
    read -p "Appuyez sur Entrée pour continuer avec l'intégration..."
fi

echo ""
echo "💉 ÉTAPE 4/4: Intégration VIDEO dans i18n.js..."
python3 step2_integrate_translations.py video

echo ""
echo "✅ VIDEO TERMINÉ!"
echo ""

# ═════════════════════════════════════════════════════════════════
# RÉSUMÉ FINAL
# ═════════════════════════════════════════════════════════════════

echo "╔═══════════════════════════════════════════════════════════╗"
echo "║               ✅ TRAITEMENT TERMINÉ AVEC SUCCÈS!          ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""
echo "📊 RÉSUMÉ:"
echo "  ✅ IMAGE: Traductions générées et intégrées"
echo "  ✅ VIDEO: Traductions générées et intégrées"
echo ""
echo "📁 Fichiers créés:"
echo "  - image_translations.json"
echo "  - video_translations.json"
echo "  - i18n.js.backup-* (sauvegardes)"
echo ""
echo "🧪 POUR TESTER:"
echo "  1. Ouvrir un fichier HTML (ex: pages/reviews/image/midjourney.html)"
echo "  2. Vider le cache (Ctrl+Shift+Del)"
echo "  3. Recharger (Ctrl+F5)"
echo "  4. Changer de langue et vérifier les traductions"
echo ""
echo "📈 PROGRESSION GLOBALE:"
echo "  ✅ chatbots (8 outils)"
echo "  ✅ image (8 outils)"
echo "  ✅ video (8 outils)"
echo "  📊 Total: 24 outils traduits sur 262"
echo ""

