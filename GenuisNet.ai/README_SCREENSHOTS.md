# 📸 Guide de Téléchargement des Screenshots - GenuisNet.ai

## 📊 Vue d'ensemble du projet

- **Total d'outils IA**: 252
- **Catégories**: 23
- **Screenshots actuels**: 2 (0.8%)
- **Screenshots manquants**: 250 (99.2%)

## 🎯 Ce qui a été mis en place

### 1. Structure des dossiers
```
assets/screenshots/
├── chatbots/
├── image/
│   └── stable-diffusion.png ✓
├── coding/
│   └── cursor.png ✓
├── video/
├── audio/
├── productivity/
└── [20 autres catégories]/
```

### 2. Scripts disponibles

#### A. **screenshot_automation_playwright.py** (Recommandé)
Capture automatiquement des screenshots en visitant les sites officiels

```bash
python3 scripts/screenshot_automation_playwright.py
```

**Avantages:**
- Automatique
- Screenshots de haute qualité (1920x1080)
- 70+ outils pré-configurés

**Inconvénients:**
- Nécessite Playwright installé
- Peut être bloqué par certains sites
- Prend du temps (2-3 secondes par outil)

#### B. **generate_tools_list.py**
Génère une liste complète de tous les outils avec métadonnées

```bash
python3 scripts/generate_tools_list.py
```

**Génère:**
- `tools_list.json` - Liste complète en JSON
- `tools_list.csv` - Fichier CSV importable dans Excel/Sheets
- `TOOLS_LIST.md` - Documentation Markdown avec liens
- `screenshots_missing.txt` - Liste des screenshots manquants

#### C. **test_screenshot_capture.py**
Teste la capture sur quelques outils

```bash
python3 scripts/test_screenshot_capture.py
```

### 3. Documentation

#### 📄 SCREENSHOT_GUIDE.md
Guide complet avec:
- Différentes stratégies de téléchargement
- URLs officielles des principaux outils
- Spécifications techniques des screenshots
- Outils recommandés pour la capture

## 🚀 Démarrage rapide

### Option 1: Capture automatique (Playwright)

1. Installer Playwright (si pas déjà fait):
```bash
pip install playwright
playwright install
```

2. Lancer la capture automatique:
```bash
python3 scripts/screenshot_automation_playwright.py
```

3. Attendre que tous les screenshots soient capturés (environ 10-15 minutes pour 70 outils)

### Option 2: Capture manuelle avec un navigateur

1. Consulter la liste des outils manquants:
```bash
cat screenshots_missing.txt
```

2. Pour chaque outil, visiter le site officiel

3. Capturer le screenshot:
   - **Firefox/Chrome**: F12 → Ctrl+Shift+P → "Screenshot" → "Capture full size screenshot"
   - **Linux (Flameshot)**: `flameshot gui`

4. Sauvegarder dans le bon dossier:
```
assets/screenshots/[catégorie]/[nom-outil].png
```

### Option 3: Recherche d'images existantes

Pour certains outils populaires, chercher des screenshots sur:
- **Product Hunt**: https://www.producthunt.com/
- **G2**: https://www.g2.com/
- **Capterra**: https://www.capterra.com/

## 📋 Fichiers générés

| Fichier | Description | Usage |
|---------|-------------|-------|
| `tools_list.json` | Liste complète (JSON) | Import dans apps/scripts |
| `tools_list.csv` | Liste complète (CSV) | Excel, Google Sheets |
| `TOOLS_LIST.md` | Documentation Markdown | Référence humaine |
| `screenshots_missing.txt` | Screenshots manquants | To-do list |
| `SCREENSHOT_GUIDE.md` | Guide détaillé | Instructions complètes |

## 🎯 Progression par catégorie

| Catégorie | Outils | Screenshots | Complétion |
|-----------|--------|-------------|------------|
| analytics | 15 | 0 | 0.0% |
| architecture | 8 | 0 | 0.0% |
| audio | 8 | 0 | 0.0% |
| business | 8 | 0 | 0.0% |
| chatbots | 8 | 0 | 0.0% |
| coding | 8 | 1 | 12.5% ✓ |
| customer-service | 15 | 0 | 0.0% |
| cybersecurity | 30 | 0 | 0.0% |
| education | 14 | 0 | 0.0% |
| gaming | 11 | 0 | 0.0% |
| hr | 14 | 0 | 0.0% |
| image | 8 | 1 | 12.5% ✓ |
| legal | 12 | 0 | 0.0% |
| medical | 8 | 0 | 0.0% |
| networking | 8 | 0 | 0.0% |
| productivity | 8 | 0 | 0.0% |
| quantum | 8 | 0 | 0.0% |
| research | 12 | 0 | 0.0% |
| sales | 16 | 0 | 0.0% |
| seo | 8 | 0 | 0.0% |
| translation | 10 | 0 | 0.0% |
| video | 8 | 0 | 0.0% |
| writing | 7 | 0 | 0.0% |

**Total: 252 outils | 2 screenshots (0.8%)**

## 🔍 Vérifier la progression

Pour voir combien de screenshots ont été ajoutés:

```bash
python3 scripts/generate_tools_list.py
```

Cela affichera les statistiques à jour.

## 📏 Spécifications des screenshots

### Dimensions recommandées:
- **Largeur**: 1920px
- **Hauteur**: 1080px minimum
- **Format**: PNG (meilleure qualité)
- **Poids maximum**: 500KB

### Optimisation:
Après capture, optimiser avec:
```bash
# TinyPNG CLI
tinypng assets/screenshots/**/*.png

# ou ImageMagick
find assets/screenshots -name "*.png" -exec convert {} -quality 85 {} \;
```

## 🛠 Outils déjà configurés dans le script Playwright

Le script `screenshot_automation_playwright.py` contient déjà les URLs pour **70+ outils**:

### Chatbots (8)
- ChatGPT, Claude, Gemini, Perplexity, Poe, Character.AI, HuggingChat, Copilot

### Image Generation (7)
- Midjourney, Stable Diffusion, DALL-E, Leonardo AI, Ideogram, Adobe Firefly, Canva AI

### Coding (5)
- GitHub Copilot, Cursor, Codeium, Tabnine, CodeWhisperer

### Video (6)
- Runway, Synthesia, Pictory, Descript, InVideo, Elai

### Audio (5)
- ElevenLabs, Murf AI, Play.ht, Speechify, Descript

### Et 40+ autres...

## 💡 Conseils et bonnes pratiques

### 1. Prioriser les outils populaires
Commencez par les outils les plus connus de chaque catégorie.

### 2. Capturer l'interface principale
Montrez le dashboard ou l'interface principale, pas la page marketing.

### 3. Éviter les données sensibles
Ne capturez pas de données personnelles ou de contenu protégé.

### 4. Vérifier les licences
Assurez-vous d'avoir le droit d'utiliser les screenshots.

### 5. Batch processing
Traitez les outils par catégorie pour plus d'efficacité.

## 🐛 Dépannage

### Erreur: "Playwright not installed"
```bash
pip install playwright
playwright install
```

### Erreur: "Timeout"
Certains sites sont lents. Augmentez le timeout dans le script:
```python
await page.goto(url, wait_until='networkidle', timeout=60000)  # 60s au lieu de 30s
```

### Screenshot vide/noir
Le site utilise du lazy loading. Augmentez le délai:
```python
await asyncio.sleep(5)  # 5s au lieu de 2s
```

## 📞 Support

Pour toute question sur les screenshots:
1. Consultez `SCREENSHOT_GUIDE.md`
2. Vérifiez les exemples dans `assets/screenshots/`
3. Testez avec `test_screenshot_capture.py`

## 🎯 Prochaines étapes

1. **Immédiat**: Lancer le script Playwright pour capturer les 70+ outils configurés
2. **Court terme**: Compléter manuellement les outils les plus populaires manquants
3. **Moyen terme**: Configurer les URLs pour les 180 outils restants
4. **Long terme**: Automatiser la mise à jour périodique des screenshots

## 📊 Résumé des fichiers créés

```
GenuisNet.ai/
├── scripts/
│   ├── screenshot_automation_playwright.py  ← Script principal
│   ├── generate_tools_list.py               ← Générateur de listes
│   ├── test_screenshot_capture.py           ← Script de test
│   ├── SCREENSHOT_GUIDE.md                  ← Guide complet
│   └── screenshot_downloader_manual.py      ← Alternative (URLs fixes)
├── assets/screenshots/                      ← Dossier de destination
│   ├── chatbots/
│   ├── image/
│   │   └── stable-diffusion.png ✓
│   ├── coding/
│   │   └── cursor.png ✓
│   └── [21 autres catégories]/
├── tools_list.json                          ← Liste JSON
├── tools_list.csv                           ← Liste CSV
├── TOOLS_LIST.md                            ← Documentation
├── screenshots_missing.txt                  ← To-do list
└── README_SCREENSHOTS.md                    ← Ce fichier

---

**Créé le**: 5 Décembre 2025
**Version**: 1.0
**Outils configurés**: 70+
**Outils total**: 252
**Progression actuelle**: 0.8%
```
