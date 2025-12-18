#!/bin/bash
echo "🔍 SURVEILLANCE DE LA GÉNÉRATION IMAGE"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

START_TIME=$(date +%s)

while true; do
    CURRENT_TIME=$(date +%s)
    ELAPSED=$((CURRENT_TIME - START_TIME))
    MINUTES=$((ELAPSED / 60))
    SECONDS=$((ELAPSED % 60))
    
    clear
    echo "╔═══════════════════════════════════════════════════════════╗"
    echo "║         SURVEILLANCE GÉNÉRATION IMAGE                     ║"
    echo "╚═══════════════════════════════════════════════════════════╝"
    echo ""
    echo "⏱️  Temps écoulé: ${MINUTES}m ${SECONDS}s"
    echo ""
    
    # Vérifier si le processus tourne
    if ps aux | grep -q "[t]ranslate_image.py"; then
        echo "✓ Processus de traduction actif"
        
        # CPU usage
        CPU=$(ps aux | grep "[t]ranslate_image.py" | awk '{print $3}')
        MEM=$(ps aux | grep "[t]ranslate_image.py" | awk '{print $4}')
        echo "  CPU: ${CPU}% | MEM: ${MEM}%"
        echo ""
        
        # Vérifier si le fichier de sortie existe
        if [ -f "image_translations.json" ]; then
            SIZE=$(du -h image_translations.json | cut -f1)
            echo "📁 Fichier en cours de création: image_translations.json (${SIZE})"
            
            # Compter les langues déjà générées
            LANGS=$(cat image_translations.json 2>/dev/null | jq 'keys | length' 2>/dev/null || echo "0")
            if [ "$LANGS" != "0" ]; then
                echo "  Langues générées: ${LANGS}/10"
            fi
        else
            echo "⏳ Traduction en cours... (fichier JSON pas encore créé)"
        fi
        
        echo ""
        echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        echo "Prochaine mise à jour dans 10 secondes..."
        echo "(Ctrl+C pour arrêter la surveillance)"
        
        sleep 10
    else
        echo "✅ PROCESSUS TERMINÉ!"
        echo ""
        
        if [ -f "image_translations.json" ]; then
            SIZE=$(du -h image_translations.json | cut -f1)
            KEYS=$(cat image_translations.json | jq '.en | keys | length' 2>/dev/null)
            LANGS=$(cat image_translations.json | jq 'keys | length' 2>/dev/null)
            
            echo "📁 Fichier créé: image_translations.json"
            echo "  Taille: ${SIZE}"
            echo "  Clés: ${KEYS}"
            echo "  Langues: ${LANGS}"
            echo ""
            echo "✅ Génération IMAGE terminée avec succès!"
        else
            echo "❌ Le fichier image_translations.json n'a pas été créé"
            echo "   Vérifier les erreurs dans la sortie du processus"
        fi
        
        break
    fi
done

echo ""
echo "🎯 PROCHAINE ÉTAPE:"
echo "   Vérifier le fichier: cat image_translations.json | jq '.en | keys | length'"
echo "   Puis lancer l'intégration: python3 step2_integrate_translations.py image"
echo ""
