#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re

categories_path = '/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/categories/'

# Le CSS à ajouter
css_fix = '''
        /* Fix: Désactiver les clics sur les overlays */
        #neural-bg, #particles-container {
            pointer-events: none !important;
        }

        /* S'assurer que les cartes sont cliquables */
        .tool-card {
            position: relative;
            z-index: 100 !important;
            cursor: pointer;
        }

        .tool-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(4, 159, 217, 0.15);
        }'''

# Parcourir tous les fichiers HTML
for filename in os.listdir(categories_path):
    if filename.endswith('.html') and filename.startswith('ai-'):
        filepath = os.path.join(categories_path, filename)

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Vérifier si le fix est déjà présent
        if 'pointer-events: none !important' in content:
            print(f'✓ {filename} - Déjà corrigé')
            continue

        # Trouver la balise </style>
        if '</style>' in content:
            # Ajouter le CSS juste avant </style>
            content = content.replace('    </style>', css_fix + '\n    </style>')

            # Écrire le fichier modifié
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            print(f'✅ {filename} - Corrigé')
        else:
            print(f'❌ {filename} - Pas de balise </style> trouvée')

print('\n✅ Toutes les pages de catégories AI ont été corrigées!')
