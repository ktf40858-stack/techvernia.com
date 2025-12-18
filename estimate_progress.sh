#!/bin/bash
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║         ESTIMATION DE LA PROGRESSION IMAGE                ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""

# Temps total de CPU utilisé
CPU_TIME=$(ps aux | grep "[t]ranslate_image.py" | awk '{print $10}')
echo "⏱️  Temps CPU utilisé: ${CPU_TIME}"

# Calcul estimation
# 660 clés × 9 langues = 5940 traductions
# Estimation: ~0.4 seconde par traduction
# Total estimé: 5940 × 0.4 = 2376 secondes = 39.6 minutes

# Convertir CPU_TIME en secondes
if [[ $CPU_TIME == *:* ]]; then
    IFS=':' read -ra ADDR <<< "$CPU_TIME"
    MINUTES=${ADDR[0]}
    SECONDS=${ADDR[1]}
    TOTAL_SECONDS=$((MINUTES * 60 + SECONDS))
else
    TOTAL_SECONDS=$CPU_TIME
fi

echo "   → ${TOTAL_SECONDS} secondes"
echo ""

# Estimation du pourcentage
ESTIMATED_TOTAL=2400  # ~40 minutes en secondes
PERCENTAGE=$((TOTAL_SECONDS * 100 / ESTIMATED_TOTAL))

if [ $PERCENTAGE -gt 100 ]; then
    PERCENTAGE=99
fi

echo "📊 Progression estimée: ${PERCENTAGE}%"
echo ""

# Barre de progression
FILLED=$((PERCENTAGE / 2))
EMPTY=$((50 - FILLED))
echo -n "["
for i in $(seq 1 $FILLED); do echo -n "█"; done
for i in $(seq 1 $EMPTY); do echo -n "░"; done
echo "] ${PERCENTAGE}%"
echo ""

# Temps restant estimé
REMAINING=$((ESTIMATED_TOTAL - TOTAL_SECONDS))
if [ $REMAINING -lt 0 ]; then
    REMAINING=60  # Au moins 1 minute
fi
REMAINING_MIN=$((REMAINING / 60))
REMAINING_SEC=$((REMAINING % 60))

echo "⏳ Temps restant estimé: ${REMAINING_MIN}m ${REMAINING_SEC}s"
echo ""
echo "📝 Note: Ce sont des estimations basées sur argostranslate"
echo "   Le temps réel peut varier."
echo ""
