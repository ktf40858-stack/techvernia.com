# 🎯 GUIDE: Traduction en 2 ÉTAPES (avec vérification)

## 📋 NOUVEAU PROCESSUS SÉCURISÉ

Au lieu de tout faire d'un coup, le processus est maintenant divisé en **2 étapes distinctes** pour que vous puissiez **vérifier les traductions** avant de les intégrer dans i18n.js.

---

## ⚙️ ÉTAPE 1: GÉNÉRATION DES TRADUCTIONS

Cette étape va:
- ✅ Extraire les FAQ des fichiers HTML
- ✅ Ajouter data-i18n aux FAQ
- ✅ Extraire le contenu existant de i18n.js
- ✅ Générer les traductions en 9 langues
- ✅ **SAUVEGARDER dans un fichier JSON** (sans toucher à i18n.js)

### Commande:

```bash
cd "/home/komet/Desktop/Projekt/AI Tools"
python3 step1_generate_translations.py <category>
```

### Exemples:

```bash
# Générer traductions IMAGE
python3 step1_generate_translations.py image

# Générer traductions VIDEO
python3 step1_generate_translations.py video
```

### Résultat:

Un fichier sera créé: `<category>_translations.json`

Exemple pour IMAGE: `image_translations.json`

### Structure du fichier JSON:

```json
{
  "en": {
    "review.midjourney.title": "Midjourney Review",
    "review.midjourney.faq1.question": "What is Midjourney?",
    "review.midjourney.faq1.answer": "Midjourney is an AI..."
  },
  "fr": {
    "review.midjourney.title": "Examen de Midjourney",
    "review.midjourney.faq1.question": "Qu'est-ce que Midjourney?",
    "review.midjourney.faq1.answer": "Midjourney est une IA..."
  },
  "es": { ... },
  "de": { ... },
  "pt": { ... },
  "zh": { ... },
  "ja": { ... },
  "ko": { ... },
  "ar": { ... },
  "hi": { ... }
}
```

---

## 🔍 VÉRIFICATION DES TRADUCTIONS

**Avant de passer à l'étape 2**, vous pouvez:

### 1. Inspecter le fichier JSON:

```bash
# Voir le contenu du fichier
cat image_translations.json | head -100

# Compter le nombre de clés
cat image_translations.json | jq '.en | keys | length'

# Voir quelques exemples de traductions françaises
cat image_translations.json | jq '.fr | to_entries | .[0:5]'
```

### 2. Vérifier des traductions spécifiques:

```bash
# Voir toutes les traductions d'une clé spécifique
cat image_translations.json | jq '. | to_entries | map({lang: .key, value: .value["review.midjourney.title"]})'
```

### 3. Comparer EN vs FR:

```bash
cat image_translations.json | jq '{en: .en["review.midjourney.faq1.question"], fr: .fr["review.midjourney.faq1.question"]}'
```

---

## ⚙️ ÉTAPE 2: INTÉGRATION DANS i18n.js

**Seulement après vérification**, cette étape va:
- ✅ Créer une **sauvegarde de i18n.js**
- ✅ Intégrer les traductions dans i18n.js
- ✅ **Vérifier la syntaxe JavaScript**
- ✅ Restaurer automatiquement en cas d'erreur

### Commande:

```bash
python3 step2_integrate_translations.py <category>
```

### Exemples:

```bash
# Intégrer IMAGE dans i18n.js
python3 step2_integrate_translations.py image

# Intégrer VIDEO dans i18n.js
python3 step2_integrate_translations.py video
```

### Sécurité:

- Une sauvegarde est créée: `i18n.js.backup-YYYYMMDD-HHMMSS`
- Si erreur de syntaxe → restauration automatique
- Vous pouvez toujours revenir en arrière manuellement

---

## 📊 WORKFLOW COMPLET POUR IMAGE + VIDEO

### Pour IMAGE:

```bash
# 1. Générer les traductions
python3 step1_generate_translations.py image

# 2. Vérifier image_translations.json
cat image_translations.json | jq '.en | keys | length'
# Doit afficher le nombre de clés (exemple: 280)

# 3. Vérifier quelques traductions FR
cat image_translations.json | jq '.fr | to_entries | .[0:3]'

# 4. Si OK, intégrer
python3 step2_integrate_translations.py image
```

### Pour VIDEO:

```bash
# 1. Générer les traductions
python3 step1_generate_translations.py video

# 2. Vérifier video_translations.json
cat video_translations.json | jq '.en | keys | length'

# 3. Vérifier quelques traductions FR
cat video_translations.json | jq '.fr | to_entries | .[0:3]'

# 4. Si OK, intégrer
python3 step2_integrate_translations.py video
```

---

## ⏱️ DURÉE ESTIMÉE

### ÉTAPE 1 (Génération):
- **IMAGE** (8 outils): ~8-12 minutes
- **VIDEO** (8 outils): ~8-12 minutes

### ÉTAPE 2 (Intégration):
- **Quasi instantané** (~5 secondes)

**Total pour IMAGE + VIDEO**: ~20-25 minutes

---

## 🆚 COMPARAISON: ANCIEN vs NOUVEAU PROCESSUS

### ❌ Ancien processus (process_category.py):
```
Génération + Intégration → Tout ou rien
Si problème → Restauration manuelle requise
Pas de vérification possible avant intégration
```

### ✅ Nouveau processus (2 étapes):
```
ÉTAPE 1: Génération → Fichier JSON
         ↓
    VÉRIFICATION
         ↓
ÉTAPE 2: Intégration → i18n.js (avec backup auto)
```

**Avantages**:
- ✅ Vérification avant intégration
- ✅ Sauvegarde automatique
- ✅ Restauration automatique si erreur
- ✅ Possibilité de modifier le JSON manuellement
- ✅ Possibilité de réutiliser le JSON sans regénérer

---

## 🔧 COMMANDES UTILES

### Vérifier le nombre de clés par outil:

```bash
# Exemple pour Midjourney dans IMAGE
cat image_translations.json | jq '.en | keys | map(select(startswith("review.midjourney"))) | length'
```

### Exporter les traductions d'un outil spécifique:

```bash
# Toutes les clés Midjourney EN
cat image_translations.json | jq '.en | to_entries | map(select(.key | startswith("review.midjourney")))'

# Toutes les clés Midjourney FR
cat image_translations.json | jq '.fr | to_entries | map(select(.key | startswith("review.midjourney")))'
```

### Compter le total de traductions:

```bash
# Total de clés EN
cat image_translations.json | jq '.en | keys | length'

# Doit être le même pour toutes les langues
cat image_translations.json | jq '. | to_entries | map({lang: .key, count: (.value | keys | length)})'
```

---

## ⚠️ EN CAS DE PROBLÈME

### Si erreur pendant ÉTAPE 1:
```
Le fichier JSON ne sera pas créé ou sera incomplet.
i18n.js n'est PAS modifié → Aucun risque
Solution: Corriger l'erreur et relancer step1
```

### Si erreur pendant ÉTAPE 2:
```
Restauration automatique de i18n.js depuis la sauvegarde
Le fichier JSON reste intact → Peut être réutilisé
Solution: Corriger l'erreur et relancer step2
```

### Restauration manuelle:

```bash
# Lister les sauvegardes
ls -lth GenuisNet.ai/js/i18n.js.backup-*

# Restaurer une sauvegarde spécifique
cp GenuisNet.ai/js/i18n.js.backup-20251217-143000 GenuisNet.ai/js/i18n.js
```

---

## 📝 FICHIERS GÉNÉRÉS

Après traitement complet de IMAGE + VIDEO:

```
image_translations.json           ← Traductions IMAGE (10 langues)
video_translations.json           ← Traductions VIDEO (10 langues)
GenuisNet.ai/js/i18n.js.backup-*  ← Sauvegardes automatiques
/tmp/image_all_data.json          ← Fichier temporaire (peut être supprimé)
/tmp/video_all_data.json          ← Fichier temporaire (peut être supprimé)
/tmp/translate_image.py           ← Script temporaire (peut être supprimé)
/tmp/translate_video.py           ← Script temporaire (peut être supprimé)
```

---

## ✅ PRÊT À COMMENCER?

```bash
cd "/home/komet/Desktop/Projekt/AI Tools"

# ÉTAPE 1: Générer traductions IMAGE
python3 step1_generate_translations.py image

# Attendre la fin (8-12 minutes)
# Puis vérifier le fichier JSON

# ÉTAPE 2: Intégrer IMAGE
python3 step2_integrate_translations.py image

# Répéter pour VIDEO
python3 step1_generate_translations.py video
python3 step2_integrate_translations.py video
```

**Bonne chance! 🚀**
