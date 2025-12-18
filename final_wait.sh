#!/bin/bash
echo "🎯 Attente des dernières minutes (progression à 90%)..."
echo ""

COUNTER=0
while ps aux | grep -q "[t]ranslate_image.py"; do
    COUNTER=$((COUNTER + 1))
    if [ $((COUNTER % 6)) -eq 0 ]; then
        ELAPSED=$((COUNTER / 6))
        echo "⏱️  ${ELAPSED} minute(s) écoulée(s)..."
    fi
    echo -n "."
    sleep 10
done

echo ""
echo ""
echo "🎉 GÉNÉRATION TERMINÉE!"
echo ""

if [ -f "image_translations.json" ]; then
    echo "✅ Fichier créé avec succès!"
    SIZE=$(du -h image_translations.json | cut -f1)
    echo "   Taille: ${SIZE}"
    
    if command -v jq &> /dev/null; then
        KEYS=$(jq '.en | keys | length' image_translations.json 2>/dev/null)
        LANGS=$(jq 'keys | length' image_translations.json 2>/dev/null)
        echo "   Clés: ${KEYS}"
        echo "   Langues: ${LANGS}"
    fi
else
    echo "⚠️  Le fichier n'a pas été créé"
fi
