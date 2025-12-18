# Rapport de Sauvegarde - Traduction GenuisNet.ai
**Date**: 15 décembre 2025
**Projet**: Traduction multi-langues des reviews de chatbots IA

---

## 📊 ÉTAT ACTUEL

### ✅ Traductions Complétées (8 outils)
1. **ChatGPT** - 216 clés → 1,944 traductions (COMPLET ✅)
2. **Claude** - 83 clés → 747 traductions (PARTIEL ⚠️)
3. **Gemini** - 61 clés → 549 traductions (PARTIEL ⚠️)
4. **Copilot** - 57 clés → 513 traductions (PARTIEL ⚠️)
5. **DeepSeek** - 120 clés → 1,080 traductions (PARTIEL ⚠️)
6. **Grok** - 122 clés → 1,098 traductions (PARTIEL ⚠️)
7. **Perplexity** - 59 clés → 531 traductions (PARTIEL ⚠️)
8. **Poe** - 60 clés → 540 traductions (PARTIEL ⚠️)

**Total actuel**: ~6,000 traductions injectées dans `i18n.js`

---

## ⚠️ PROBLÈME DÉCOUVERT

### Seul ChatGPT a une traduction COMPLÈTE

**Raison**: Les fichiers HTML des autres outils ne sont pas complètement annotés avec `data-i18n`.

#### Exemple de la différence:

**ChatGPT (complet)**:
```html
<h4><span data-i18n="review.chatgpt.feature.vision.title">Vision Capabilities</span></h4>
<p><span data-i18n="review.chatgpt.feature.vision.desc">Upload images...</span></p>
```

**Claude, Gemini, etc. (incomplet)**:
```html
<h4>200K Context Window</h4> <!-- ❌ PAS de data-i18n -->
<p><span data-i18n="review.claude.process...">Process up to...</span></p>
```

### Éléments manquants dans les HTML:
- Titres `<h4>` des features
- Certains titres de sections
- Éléments de tableau
- Certaines listes
- Textes dans les boutons

---

## 🔧 FICHIERS IMPORTANTS

### Scripts Python (dans `/home/komet/Desktop/Projekt/AI Tools/`)
- **`process_tool.py`** - Script générique pour traiter un outil (extraction → traduction → injection)
- **`inject_copilot_translations.py`** - Script d'injection spécifique (obsolète, remplacé par process_tool.py)
- **`translate_copilot.py`** - Script de traduction spécifique (obsolète)

### Fichiers HTML (dans `GenuisNet.ai/pages/reviews/chatbots/`)
- `chatgpt.html` (1,688 lignes, 216 data-i18n) ✅
- `claude.html` (974 lignes, 83 data-i18n) ⚠️
- `gemini.html` (591 lignes, 61 data-i18n) ⚠️
- `copilot.html` (582 lignes, 57 data-i18n) ⚠️
- `deepseek.html` (1,058 lignes, 120 data-i18n) ⚠️
- `grok.html` (1,058 lignes, 122 data-i18n) ⚠️
- `perplexity.html` (584 lignes, 59 data-i18n) ⚠️
- `poe.html` (614 lignes, 60 data-i18n) ⚠️

### Fichier de traductions
- **`GenuisNet.ai/js/i18n.js`** - Fichier principal contenant toutes les traductions

### Fichiers JSON générés (pour chaque outil)
- `{tool}_content_to_translate.json` - Contenu extrait de l'HTML
- `{tool}_translations_all_langs.json` - Traductions dans les 9 langues

---

## 🌍 LANGUES SUPPORTÉES (9 langues)

| Code | Langue | Constante JS |
|------|--------|--------------|
| `es` | Espagnol | `SPANISH` |
| `fr` | Français | `FRENCH` |
| `de` | Allemand | `GERMAN` |
| `pt` | Portugais | `PORTUGUESE` |
| `zh` | Chinois | `CHINESE` |
| `ja` | Japonais | `JAPANESE` |
| `ko` | Coréen | `KOREAN` |
| `ar` | Arabe | `ARABIC` |
| `hi` | Hindi | `HINDI` |

---

## 📋 PLAN D'ACTION POUR DEMAIN

### Étape 1: Préparer les fichiers HTML
Pour chaque outil (Claude, Gemini, Copilot, DeepSeek, Grok, Perplexity, Poe), ajouter les attributs `data-i18n` manquants:

1. **Titres de features** (`<h4>`)
2. **Éléments de tableaux**
3. **Items de listes**
4. **Textes de boutons**
5. **Autres textes visibles**

### Étape 2: Re-traduire les outils incomplets
Utiliser le script `process_tool.py` pour chaque outil:

```bash
# Activer l'environnement virtuel
source venv/bin/activate

# Pour chaque outil
python3 process_tool.py claude
python3 process_tool.py gemini
python3 process_tool.py copilot
python3 process_tool.py deepseek
python3 process_tool.py grok
python3 process_tool.py perplexity
python3 process_tool.py poe
```

### Étape 3: Vérifier les traductions
Compter le nombre de clés traduites pour s'assurer que c'est complet.

---

## 🛠️ COMMANDES UTILES

### Compter les data-i18n dans un fichier HTML
```bash
grep -c 'data-i18n' GenuisNet.ai/pages/reviews/chatbots/{tool}.html
```

### Lancer une traduction
```bash
source venv/bin/activate
python3 process_tool.py {tool_name}
```

### Vérifier les traductions générées
```bash
ls -lh *_translations_all_langs.json
```

### Compter les lignes dans i18n.js
```bash
wc -l GenuisNet.ai/js/i18n.js
```

---

## 📝 NOTES TECHNIQUES

### Structure du script process_tool.py

**Phase 1 - Extraction**:
- Lit le fichier HTML
- Trouve tous les éléments avec `data-i18n`
- Extrait les clés et le texte
- Sauvegarde dans `{tool}_content_to_translate.json`

**Phase 2 - Traduction**:
- Utilise Argos Translate (traduction offline)
- Traduit chaque clé dans 9 langues
- Sauvegarde dans `{tool}_translations_all_langs.json`
- Temps: ~10-20 minutes selon le nombre de clés

**Phase 3 - Injection**:
- Lit `i18n.js`
- Trouve les sections de chaque langue
- Insère les traductions avec marqueurs
- Format: `// ===== {Tool} Review Translations =====`

### Fonction d'échappement JavaScript
```python
def escape_js_string(s):
    s = s.replace('\\', '\\\\')
    s = s.replace('"', '\\"')
    s = s.replace("'", "\\'")
    s = s.replace('\n', '\\n')
    s = s.replace('\r', '\\r')
    s = s.replace('\t', '\\t')
    return s
```

---

## 🎯 OBJECTIF FINAL

Avoir **tous les 8 outils avec des traductions complètes** comme ChatGPT:
- Environ **150-200 clés par outil**
- **1,350-1,800 traductions par outil** (9 langues)
- **Total estimé: ~12,000-14,000 traductions**

---

## ⚙️ ENVIRONNEMENT

- **Python**: Python 3 + virtualenv dans `venv/`
- **Dépendances**:
  - `beautifulsoup4` - Parsing HTML
  - `argostranslate` - Traduction offline
  - `tqdm` - Barres de progression
- **Activation**: `source venv/bin/activate`

---

## 🔄 PROCESSUS DE REPRISE DEMAIN

1. Lire ce rapport
2. Commencer par **Claude** (le plus gros après ChatGPT)
3. Ajouter les `data-i18n` manquants dans `claude.html`
4. Lancer `python3 process_tool.py claude`
5. Vérifier le résultat
6. Répéter pour les 6 autres outils

---

**Auteur**: Claude Sonnet 4.5 via Claude Code
**Dernière mise à jour**: 15 décembre 2025, 22:35
