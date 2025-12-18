#!/bin/bash
echo "⏳ Attente de la fin de la génération IMAGE..."
echo ""

while ps aux | grep -q "[t]ranslate_image.py"; do
    echo -n "."
    sleep 5
done

echo ""
echo ""
echo "✅ Processus terminé!"
echo ""

if [ -f "image_translations.json" ]; then
    SIZE=$(du -h image_translations.json | cut -f1)
    KEYS=$(cat image_translations.json | jq '.en | keys | length' 2>/dev/null)
    echo "📁 Fichier créé: image_translations.json (${SIZE})"
    echo "📊 Nombre de clés: ${KEYS}"
else
    echo "❌ Le fichier n'a pas été créé"
fi
