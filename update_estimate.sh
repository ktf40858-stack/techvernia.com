#!/bin/bash
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║      MISE À JOUR ESTIMATION - PROGRESSION IMAGE           ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""

CPU_TIME=$(ps aux | grep "[t]ranslate_image.py" | awk '{print $10}')
MEM=$(ps aux | grep "[t]ranslate_image.py" | awk '{print $4}')

echo "⏱️  Temps CPU: ${CPU_TIME} (environ 45 minutes)"
echo "💾 Mémoire: ${MEM}%"
echo ""

# Nouvelle estimation basée sur les données réelles
# Le processus semble plus lent que prévu
ESTIMATED_TOTAL=3600  # ~60 minutes au total

IFS=':' read -ra ADDR <<< "$CPU_TIME"
MINUTES=${ADDR[0]}
SECONDS=${ADDR[1]}
TOTAL_SECONDS=$((MINUTES * 60 + SECONDS))

PERCENTAGE=$((TOTAL_SECONDS * 100 / ESTIMATED_TOTAL))
if [ $PERCENTAGE -gt 99 ]; then
    PERCENTAGE=99
fi

echo "📊 Progression révisée: ${PERCENTAGE}%"
echo ""

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
    REMAINING=300  # 5 minutes minimum
fi
REMAINING_MIN=$((REMAINING / 60))

echo "⏳ Temps restant estimé: ~${REMAINING_MIN} minutes"
echo ""
echo "📝 Note: La traduction avec argostranslate est intensive"
echo "   660 clés × 9 langues = 5,940 traductions"
echo "   Chaque traduction prend ~0.6 seconde en moyenne"
echo ""
