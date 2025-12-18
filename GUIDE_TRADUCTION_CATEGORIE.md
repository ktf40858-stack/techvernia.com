# 📋 GUIDE: Traduction Automatique d'une Catégorie

## 🚀 Script de Traduction Automatique

Le script `process_category.py` traduit automatiquement **tout le contenu + FAQ** d'une catégorie.

### ✅ Ce que le script fait automatiquement:

1. **Identifie** tous les outils de la catégorie
2. **Extrait** toutes les FAQ des HTML
3. **Ajoute** data-i18n aux FAQ
4. **Extrait** le contenu existant de i18n.js
5. **Génère** toutes les traductions (9 langues)
6. **Injecte** tout dans i18n.js
7. **Vérifie** la syntaxe JavaScript

---

## 📖 UTILISATION

### Commande de base:

```bash
cd "/home/komet/Desktop/Projekt/AI Tools"
python3 process_category.py <nom_categorie>
```

### Exemples:

```bash
# Traduire la catégorie "image"
python3 process_category.py image

# Traduire la catégorie "video"
python3 process_category.py video

# Traduire la catégorie "coding"
python3 process_category.py coding

# Traduire la catégorie "seo"
python3 process_category.py seo
```

---

## 📂 CATÉGORIES DISPONIBLES

Voici l'ordre suggéré pour traiter les catégories:

### ✅ Déjà fait:
- [x] **chatbots** (8 outils) - Claude, ChatGPT, Gemini, etc.
- [x] **writing** (7 outils) - Copy.ai, Grammarly, Jasper, etc.

### 🔜 À faire (par ordre de priorité):

1. **image** - Outils de génération d'images
2. **video** - Outils vidéo
3. **coding** - Outils de développement
4. **seo** - Outils SEO
5. **productivity** - Productivité
6. **sales** (16 outils) - Outils de vente
7. **customer-service** (15 outils) - Service client
8. **analytics** (15 outils) - Analyse de données
9. **education** (14 outils) - Éducation
10. **hr** (14 outils) - Ressources humaines
11. **legal** (12 outils) - Juridique
12. **research** (12 outils) - Recherche
13. **gaming** (11 outils) - Jeux vidéo
14. **cybersecurity** (30 outils) - Sécurité informatique
15. **architecture** - Architecture
16. **audio** - Audio
17. **business** - Business
18. **medical** - Médical
19. **networking** - Réseaux
20. **quantum** - Quantique
21. **translation** - Traduction

---

## ⏱️ TEMPS D'EXÉCUTION ESTIMÉ

Le temps dépend du nombre d'outils et de clés:

- **Petite catégorie** (5-7 outils, ~500 clés): 3-5 minutes
- **Moyenne catégorie** (10-15 outils, ~1000 clés): 6-10 minutes
- **Grande catégorie** (20-30 outils, ~2000 clés): 15-25 minutes

⚠️ **Important:** Le script peut prendre du temps car il traduit TOUTES les clés dans 9 langues!

---

## 📊 SORTIE DU SCRIPT

Le script affiche:

```
╔══════════════════════════════════════════════════════════╗
║  TRAITEMENT AUTOMATIQUE DE LA CATÉGORIE: IMAGE          ║
╚══════════════════════════════════════════════════════════╝

[PROCESS] ✓ Trouvé 8 outils dans image
[PROCESS]   midjourney: 6 FAQ extraites
[PROCESS]   dalle: 6 FAQ extraites
...

[1/6] Extraction des FAQ...
[2/6] Ajout de data-i18n aux FAQ...
[3/6] Extraction du contenu existant...
[4/6] Préparation des données pour traduction...
[5/6] Génération des traductions...
  Traduction vers ES... ✓ 523 clés traduites
  Traduction vers FR... ✓ 523 clés traduites
  ...
[6/6] Injection dans i18n.js...
[VÉRIFICATION] Validation de la syntaxe...

✅ CATÉGORIE IMAGE TRAITÉE AVEC SUCCÈS!
```

---

## 🔍 VÉRIFICATIONS APRÈS TRAITEMENT

Après l'exécution du script:

### 1. Vérifier le fichier i18n.js:

```bash
cd "/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/js"
node -c i18n.js
```

Si aucune erreur → ✅ Syntaxe valide

### 2. Vérifier les traductions:

```bash
python3 << 'SCRIPT'
import re

with open('GenuisNet.ai/js/i18n.js', 'r') as f:
    content = f.read()

# Vérifier FR
fr_match = re.search(r'fr:\s*\{(.*?)\n\s*\},\s*\n\s*// ==+ SPANISH', content, re.DOTALL)
if fr_match:
    # Compter les clés de la catégorie
    category_keys = re.findall(r'"review\.CATEGORY\.[^"]+"', fr_match.group(1))
    print(f"Clés FR pour CATEGORY: {len(set(category_keys))}")
SCRIPT
```

### 3. Tester dans le navigateur:

1. **Vider le cache** (Ctrl+Shift+Del)
2. Ouvrir un fichier HTML de la catégorie
3. **Recharger** (Ctrl+F5)
4. **Changer de langue** et vérifier que tout est traduit

---

## ⚠️ EN CAS D'ERREUR

### Erreur de syntaxe JavaScript:

```bash
# Restaurer depuis une sauvegarde
cp GenuisNet.ai/js/i18n.js.backup GenuisNet.ai/js/i18n.js
```

### Le script plante pendant la traduction:

Les fichiers temporaires sont dans `/tmp/`:
- `/tmp/CATEGORY_all_data.json` - Données à traduire
- `/tmp/translate_CATEGORY.py` - Script de traduction
- `CATEGORY_translations.json` - Traductions générées

Vous pouvez relancer juste la partie injection:

```python
import subprocess
subprocess.run(['python3', '-c', '''
from process_category import inject_translations_into_i18n, verify_syntax
inject_translations_into_i18n("CATEGORY")
verify_syntax()
'''])
```

---

## 💾 SAUVEGARDES AUTOMATIQUES

Le script ne fait PAS de sauvegarde automatique. **Créez-en une avant:**

```bash
cp GenuisNet.ai/js/i18n.js GenuisNet.ai/js/i18n.js.backup-$(date +%Y%m%d)
```

---

## 🎯 PROCHAINES ÉTAPES SUGGÉRÉES

### Pour demain (16 décembre):

```bash
# 1. Créer une sauvegarde
cp GenuisNet.ai/js/i18n.js GenuisNet.ai/js/i18n.js.backup-20251216

# 2. Traiter la catégorie "image"
python3 process_category.py image

# 3. Tester le résultat

# 4. Si OK, continuer avec "video"
python3 process_category.py video
```

### Traiter plusieurs catégories d'affilée:

```bash
#!/bin/bash
categories=("image" "video" "coding" "seo" "productivity")

for cat in "${categories[@]}"; do
    echo "═══════════════════════════════════════"
    echo "Traitement de: $cat"
    echo "═══════════════════════════════════════"
    
    python3 process_category.py "$cat"
    
    if [ $? -eq 0 ]; then
        echo "✓ $cat terminé avec succès"
    else
        echo "✗ $cat a échoué, arrêt"
        break
    fi
    
    echo ""
done
```

---

## 📞 AIDE

### Le script ne fonctionne pas:

Vérifiez:
1. Vous êtes dans le bon répertoire: `/home/komet/Desktop/Projekt/AI Tools`
2. Le venv Python existe: `ls venv/bin/python3`
3. argostranslate est installé: `venv/bin/python3 -c "import argostranslate"`

### Questions fréquentes:

**Q: Combien de temps ça prend?**
A: 3-25 minutes selon la taille de la catégorie

**Q: Puis-je arrêter le script et reprendre?**
A: Non, il faut le relancer depuis le début. Mais les traductions partielles sont dans les fichiers JSON.

**Q: Le script gère-t-il les doublons?**
A: Oui, il met à jour les clés existantes sans créer de doublons.

**Q: Que faire si une traduction est mauvaise?**
A: Vous pouvez éditer manuellement `i18n.js` après l'exécution.

---

Bon courage! 🚀
