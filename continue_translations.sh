#!/bin/bash
# Script automatique pour continuer les traductions
# Exécutez ce script pour traiter IMAGE et VIDEO

set -e  # Arrêter en cas d'erreur

echo "╔══════════════════════════════════════════════════════════╗"
echo "║     TRAITEMENT AUTOMATIQUE DES CATÉGORIES IMAGE+VIDEO    ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""

# Définir le répertoire de travail
cd "/home/komet/Desktop/Projekt/AI Tools"

# ═══════════════════════════════════════════════════════════════
# ÉTAPE 1: VÉRIFICATION DES DÉPENDANCES
# ═══════════════════════════════════════════════════════════════
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "1/6 VÉRIFICATION DES DÉPENDANCES"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if [ ! -f "process_category.py" ]; then
    echo "❌ process_category.py non trouvé"
    exit 1
fi
echo "✓ process_category.py trouvé"

if ! command -v python3 &> /dev/null; then
    echo "❌ python3 non installé"
    exit 1
fi
echo "✓ python3 installé"

if [ ! -f "venv/bin/python3" ]; then
    echo "❌ venv Python non trouvé"
    exit 1
fi
echo "✓ venv Python trouvé"

if ! venv/bin/python3 -c "import argostranslate" 2>/dev/null; then
    echo "❌ argostranslate non installé"
    exit 1
fi
echo "✓ argostranslate disponible"

if ! command -v node &> /dev/null; then
    echo "⚠️  node non installé (recommandé pour vérifier la syntaxe)"
else
    echo "✓ node.js disponible"
fi

echo ""

# ═══════════════════════════════════════════════════════════════
# ÉTAPE 2: SAUVEGARDE SUPPLÉMENTAIRE (SÉCURITÉ)
# ═══════════════════════════════════════════════════════════════
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "2/6 CRÉATION DE SAUVEGARDE DE SÉCURITÉ"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

BACKUP_FILE="GenuisNet.ai/js/i18n.js.backup-$(date +%Y%m%d-%H%M%S)"
cp GenuisNet.ai/js/i18n.js "$BACKUP_FILE"
echo "✓ Sauvegarde créée: $BACKUP_FILE"
echo ""

# ═══════════════════════════════════════════════════════════════
# ÉTAPE 3: VÉRIFICATION SYNTAXE ACTUELLE
# ═══════════════════════════════════════════════════════════════
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "3/6 VÉRIFICATION SYNTAXE i18n.js ACTUELLE"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if command -v node &> /dev/null; then
    if node -c GenuisNet.ai/js/i18n.js 2>/dev/null; then
        echo "✓ i18n.js syntaxe valide avant traitement"
    else
        echo "⚠️  i18n.js a des erreurs de syntaxe actuellement"
        echo "   Voulez-vous continuer quand même? (Ctrl+C pour annuler)"
        read -p "   Appuyez sur Entrée pour continuer..."
    fi
fi
echo ""

# ═══════════════════════════════════════════════════════════════
# ÉTAPE 4: TRAITEMENT DE LA CATÉGORIE IMAGE
# ═══════════════════════════════════════════════════════════════
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "4/6 TRAITEMENT DE LA CATÉGORIE IMAGE"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

python3 process_category.py image

if [ $? -eq 0 ]; then
    echo "✅ Catégorie IMAGE traitée avec succès"
else
    echo "❌ Erreur lors du traitement de IMAGE"
    echo "   Restauration de la sauvegarde..."
    cp "$BACKUP_FILE" GenuisNet.ai/js/i18n.js
    exit 1
fi

# Vérifier la syntaxe après IMAGE
if command -v node &> /dev/null; then
    if ! node -c GenuisNet.ai/js/i18n.js 2>/dev/null; then
        echo "❌ Erreur de syntaxe après IMAGE"
        echo "   Restauration de la sauvegarde..."
        cp "$BACKUP_FILE" GenuisNet.ai/js/i18n.js
        exit 1
    fi
    echo "✓ Syntaxe valide après IMAGE"
fi
echo ""

# ═══════════════════════════════════════════════════════════════
# ÉTAPE 5: TRAITEMENT DE LA CATÉGORIE VIDEO
# ═══════════════════════════════════════════════════════════════
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "5/6 TRAITEMENT DE LA CATÉGORIE VIDEO"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

python3 process_category.py video

if [ $? -eq 0 ]; then
    echo "✅ Catégorie VIDEO traitée avec succès"
else
    echo "❌ Erreur lors du traitement de VIDEO"
    echo "   Restauration de la sauvegarde..."
    cp "$BACKUP_FILE" GenuisNet.ai/js/i18n.js
    exit 1
fi

# Vérifier la syntaxe après VIDEO
if command -v node &> /dev/null; then
    if ! node -c GenuisNet.ai/js/i18n.js 2>/dev/null; then
        echo "❌ Erreur de syntaxe après VIDEO"
        echo "   Restauration de la sauvegarde..."
        cp "$BACKUP_FILE" GenuisNet.ai/js/i18n.js
        exit 1
    fi
    echo "✓ Syntaxe valide après VIDEO"
fi
echo ""

# ═══════════════════════════════════════════════════════════════
# ÉTAPE 6: VÉRIFICATION FINALE
# ═══════════════════════════════════════════════════════════════
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "6/6 VÉRIFICATION FINALE"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Taille du fichier
FILE_SIZE=$(du -h GenuisNet.ai/js/i18n.js | cut -f1)
echo "✓ Taille de i18n.js: $FILE_SIZE"

# Nombre de catégories traitées
CATEGORIES_DONE=$(ls -1 GenuisNet.ai/pages/reviews/ | wc -l)
echo "✓ Catégories disponibles: $CATEGORIES_DONE"

echo ""
echo "════════════════════════════════════════════════════════════"
echo "✅ TRAITEMENT TERMINÉ AVEC SUCCÈS!"
echo "════════════════════════════════════════════════════════════"
echo ""
echo "Catégories complètes:"
echo "  ✅ chatbots (8 outils)"
echo "  ✅ writing (7 outils)"
echo "  ✅ image (traité aujourd'hui)"
echo "  ✅ video (traité aujourd'hui)"
echo ""
echo "Prochaines catégories suggérées:"
echo "  ⬜ coding"
echo "  ⬜ seo"
echo "  ⬜ productivity"
echo ""
echo "📂 Fichiers de sauvegarde:"
echo "  - $BACKUP_FILE"
echo "  - GenuisNet.ai/js/i18n.js.backup-20251216"
echo ""
echo "🔍 POUR TESTER:"
echo "  1. Ouvrir GenuisNet.ai/pages/reviews/image/<un-fichier>.html"
echo "  2. Vider le cache (Ctrl+Shift+Del)"
echo "  3. Recharger (Ctrl+F5)"
echo "  4. Changer de langue et vérifier les traductions"
echo ""
echo "💾 Pour sauvegarder votre travail:"
echo "  git add GenuisNet.ai/js/i18n.js"
echo "  git add GenuisNet.ai/pages/reviews/image/*.html"
echo "  git add GenuisNet.ai/pages/reviews/video/*.html"
echo "  git commit -m 'Add translations for image and video categories'"
echo ""
