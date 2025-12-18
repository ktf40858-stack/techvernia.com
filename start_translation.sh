#!/bin/bash
# Script de lancement de la traduction automatique

cd "/home/komet/Desktop/Projekt/AI Tools"

echo "=========================================="
echo "🤖 TRADUCTEUR AUTOMATIQUE"
echo "=========================================="
echo ""

# Vérifier si la clé API est définie
if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "⚠️  CLÉ API NON DÉFINIE"
    echo ""
    echo "Pour obtenir une clé API gratuite ($5 de crédits):"
    echo "1. Allez sur: https://console.anthropic.com/"
    echo "2. Créez un compte"
    echo "3. Créez une clé API"
    echo ""
    echo "Puis définissez-la avec:"
    echo "export ANTHROPIC_API_KEY='votre-clé-ici'"
    echo ""
    read -p "Avez-vous une clé API? (o/n): " has_key

    if [ "$has_key" = "o" ] || [ "$has_key" = "O" ]; then
        echo ""
        read -p "Entrez votre clé API: " api_key
        export ANTHROPIC_API_KEY="$api_key"
        echo "✅ Clé API définie pour cette session"
        echo ""
    else
        echo ""
        echo "❌ Impossible de continuer sans clé API"
        exit 1
    fi
fi

# Activer l'environnement virtuel et lancer le script
source venv/bin/activate
python3 auto_translate_api.py
