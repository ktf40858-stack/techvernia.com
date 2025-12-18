#!/bin/bash
# Lance la traduction espagnole automatiquement

cd "/home/komet/Desktop/Projekt/AI Tools"

echo "=========================================="
echo "🇪🇸 TRADUCTION AUTOMATIQUE - ESPAGNOL"
echo "=========================================="
echo ""

# Vérifier la clé API
if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "⚠️  Clé API non définie"
    echo ""
    echo "Entrez votre clé API Anthropic:"
    read -r api_key
    export ANTHROPIC_API_KEY="$api_key"
fi

echo "✅ Clé API configurée"
echo ""
echo "🚀 Lancement de la traduction..."
echo "   - Langue: Espagnol (37 chunks)"
echo "   - Modèle: Claude 3.5 Haiku (rapide et économique)"
echo "   - Temps estimé: 5-10 minutes"
echo ""

# Activer venv et lancer avec espagnol par défaut
source venv/bin/activate
echo "es" | python3 auto_translate_api.py
