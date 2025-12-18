#!/bin/bash
# Script pour reformater toutes les 37 certifications au format CCNA

echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║   🔄 REFORMATAGE DE TOUTES LES CERTIFICATIONS AU FORMAT CCNA ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""
echo "Ce script va reformater les 37 pages de certification pour utiliser:"
echo "  • Le background du website (thème sombre)"
echo "  • Le format simplifié de la page CCNA"
echo "  • CSS inline complet"
echo "  • Navigation simplifiée"
echo ""
echo "⚠️  ATTENTION: Cette opération va écraser les fichiers existants!"
echo ""
read -p "Voulez-vous continuer? (oui/non): " response

if [ "$response" != "oui" ]; then
    echo "❌ Opération annulée"
    exit 0
fi

echo ""
echo "🚀 Démarrage du reformatage..."
echo ""

# Le script Python sera appelé ici
python3 format_all_certs_ccna.py

echo ""
echo "✅ Reformatage terminé!"

