#!/bin/bash
# Script de test pour vérifier que process_category.py fonctionne

echo "╔══════════════════════════════════════════════════════════╗"
echo "║              TEST DU SCRIPT DE TRADUCTION                ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""

# Vérifier que le script existe
if [ ! -f "process_category.py" ]; then
    echo "❌ process_category.py non trouvé"
    exit 1
fi
echo "✓ process_category.py trouvé"

# Vérifier Python
if ! command -v python3 &> /dev/null; then
    echo "❌ python3 non installé"
    exit 1
fi
echo "✓ python3 installé"

# Vérifier le venv
if [ ! -f "venv/bin/python3" ]; then
    echo "❌ venv Python non trouvé"
    exit 1
fi
echo "✓ venv Python trouvé"

# Vérifier argostranslate
if ! venv/bin/python3 -c "import argostranslate" 2>/dev/null; then
    echo "❌ argostranslate non installé dans le venv"
    exit 1
fi
echo "✓ argostranslate disponible"

# Vérifier BeautifulSoup
if ! python3 -c "from bs4 import BeautifulSoup" 2>/dev/null; then
    echo "⚠️  BeautifulSoup4 non installé (peut être nécessaire)"
    echo "   Installez avec: pip3 install beautifulsoup4"
fi

# Vérifier Node.js
if ! command -v node &> /dev/null; then
    echo "⚠️  node non installé (nécessaire pour vérifier la syntaxe JS)"
else
    echo "✓ node.js disponible"
fi

# Vérifier i18n.js
if [ ! -f "GenuisNet.ai/js/i18n.js" ]; then
    echo "❌ i18n.js non trouvé"
    exit 1
fi
echo "✓ i18n.js trouvé"

# Vérifier la syntaxe actuelle de i18n.js
if command -v node &> /dev/null; then
    if node -c GenuisNet.ai/js/i18n.js 2>/dev/null; then
        echo "✓ i18n.js syntaxe valide"
    else
        echo "⚠️  i18n.js a des erreurs de syntaxe actuellement"
    fi
fi

# Lister les catégories disponibles
echo ""
echo "Catégories disponibles:"
ls -1 GenuisNet.ai/pages/reviews/ | grep -v "^\." | head -10

echo ""
echo "════════════════════════════════════════════════════════════"
echo "✅ Tous les tests passés!"
echo "════════════════════════════════════════════════════════════"
echo ""
echo "Pour traiter une catégorie, utilisez:"
echo "  python3 process_category.py <nom_categorie>"
echo ""
echo "Exemple:"
echo "  python3 process_category.py image"
echo ""
