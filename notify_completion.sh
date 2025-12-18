#!/bin/bash

echo "⏳ Surveillance en cours... Je te préviendrai quand c'est terminé."
echo ""

# Attendre que le processus se termine
while ps aux | grep -q "[t]ranslate_image.py"; do
    sleep 30
done

# C'est terminé!
clear
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║                                                           ║"
echo "║              🎉 GÉNÉRATION IMAGE TERMINÉE ! 🎉            ║"
echo "║                                                           ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""
echo ""

# Vérifier le fichier
if [ -f "image_translations.json" ]; then
    SIZE=$(du -h image_translations.json | cut -f1)
    KEYS=$(jq '.en | keys | length' image_translations.json 2>/dev/null)
    LANGS=$(jq 'keys | length' image_translations.json 2>/dev/null)
    
    echo "✅ SUCCÈS - Fichier créé avec succès!"
    echo ""
    echo "📁 Fichier: image_translations.json"
    echo "📊 Taille: ${SIZE}"
    echo "🔢 Clés traduites: ${KEYS}"
    echo "🌍 Langues: ${LANGS}"
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "🔍 VÉRIFICATION RAPIDE:"
    echo ""
    echo "Aperçu des 3 premières clés en français:"
    jq '.fr | to_entries | .[0:3] | .[] | "  • \(.key): \(.value)"' image_translations.json 2>/dev/null | sed 's/"//g'
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "🎯 PROCHAINE ÉTAPE:"
    echo ""
    echo "   Vérifier le fichier si tu veux:"
    echo "   → cat image_translations.json | jq '.fr | to_entries | .[0:10]'"
    echo ""
    echo "   Puis lancer l'intégration:"
    echo "   → python3 step2_integrate_translations.py image"
    echo ""
else
    echo "❌ ERREUR - Le fichier n'a pas été créé"
    echo ""
    echo "Vérifier les logs du processus:"
    echo "→ cat /tmp/claude/tasks/baeb260.output"
    echo ""
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
