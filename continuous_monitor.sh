#!/bin/bash

while ps aux | grep -q "[t]ranslate_image.py"; do
    clear
    echo "╔═══════════════════════════════════════════════════════════╗"
    echo "║         GÉNÉRATION IMAGE EN COURS - SURVEILLANCE          ║"
    echo "╚═══════════════════════════════════════════════════════════╝"
    echo ""
    
    CPU_TIME=$(ps aux | grep "[t]ranslate_image.py" | awk '{print $10}')
    MEM=$(ps aux | grep "[t]ranslate_image.py" | awk '{print $4}')
    
    echo "⏱️  Temps CPU: ${CPU_TIME}"
    echo "💾 Mémoire: ${MEM}%"
    echo ""
    
    # Calcul progression
    IFS=':' read -ra ADDR <<< "$CPU_TIME"
    MINUTES=${ADDR[0]}
    SECONDS=${ADDR[1]}
    TOTAL_SECONDS=$((MINUTES * 60 + SECONDS))
    
    ESTIMATED_TOTAL=3600
    PERCENTAGE=$((TOTAL_SECONDS * 100 / ESTIMATED_TOTAL))
    if [ $PERCENTAGE -gt 99 ]; then
        PERCENTAGE=99
    fi
    
    echo "📊 Progression: ${PERCENTAGE}%"
    
    # Barre
    FILLED=$((PERCENTAGE / 2))
    EMPTY=$((50 - FILLED))
    echo -n "["
    for i in $(seq 1 $FILLED); do echo -n "█"; done
    for i in $(seq 1 $EMPTY); do echo -n "░"; done
    echo "] ${PERCENTAGE}%"
    echo ""
    
    REMAINING=$((ESTIMATED_TOTAL - TOTAL_SECONDS))
    if [ $REMAINING -lt 0 ]; then
        REMAINING=180
    fi
    REMAINING_MIN=$((REMAINING / 60))
    
    echo "⏳ Temps restant estimé: ~${REMAINING_MIN} minutes"
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "Mise à jour dans 30 secondes..."
    
    sleep 30
done

# Terminé!
clear
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║              🎉 GÉNÉRATION IMAGE TERMINÉE ! 🎉            ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""

if [ -f "image_translations.json" ]; then
    SIZE=$(du -h image_translations.json | cut -f1)
    KEYS=$(jq '.en | keys | length' image_translations.json 2>/dev/null)
    LANGS=$(jq 'keys | length' image_translations.json 2>/dev/null)
    
    echo "✅ Fichier créé: image_translations.json (${SIZE})"
    echo "📊 Clés: ${KEYS} | Langues: ${LANGS}"
    echo ""
    echo "🔍 Aperçu (3 premières clés FR):"
    jq '.fr | to_entries | .[0:3] | .[] | "  \(.key): \(.value)"' image_translations.json 2>/dev/null | sed 's/"//g'
    echo ""
    echo "🎯 Prochaine étape: python3 step2_integrate_translations.py image"
else
    echo "❌ Fichier non créé - Vérifier les erreurs"
fi
echo ""
