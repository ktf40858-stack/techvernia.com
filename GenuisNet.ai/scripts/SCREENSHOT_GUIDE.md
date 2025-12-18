# Guide pour obtenir des screenshots d'outils IA

## 📋 Vue d'ensemble

Votre projet contient **252 outils IA** répartis dans **23 catégories**. Ce guide vous explique comment obtenir des screenshots de qualité pour chaque outil.

## 🎯 Stratégies recommandées

### Option 1: Screenshots automatiques via Playwright (Recommandé)

Utilisez le script Python fourni qui automatise la capture de screenshots en visitant les sites officiels.

```bash
cd GenuisNet.ai
python3 scripts/screenshot_automation_playwright.py
```

### Option 2: Sources publiques d'images

#### A. Unsplash (Images gratuites de haute qualité)
```bash
# Installer l'outil unsplash-api
pip install unsplash-api
# Utiliser le script fourni
python3 scripts/download_from_unsplash.py
```

#### B. Recherche manuelle sur:
- **Product Hunt**: https://www.producthunt.com/ (captures d'écran officielles)
- **G2**: https://www.g2.com/ (screenshots de reviews)
- **Capterra**: https://www.capterra.com/ (screenshots de produits)
- **AlternativeTo**: https://alternativeto.net/ (screenshots comparatifs)

### Option 3: Utiliser les sites officiels

Pour chaque outil, visitez le site officiel et capturez l'interface:

#### Outils recommandés pour la capture:
1. **Firefox/Chrome DevTools**
   - Ouvrir DevTools (F12)
   - Ctrl+Shift+P → "Screenshot" → "Capture full size screenshot"

2. **Extension Chrome: Awesome Screenshot**
   - Capture de page complète
   - Annotations possibles
   - Export en PNG haute qualité

3. **Linux: Flameshot**
   ```bash
   sudo apt install flameshot
   flameshot gui
   ```

## 📂 Structure des dossiers

Les screenshots doivent être organisés ainsi:

```
assets/screenshots/
├── chatbots/
│   ├── chatgpt.png
│   ├── claude.png
│   ├── gemini.png
│   └── ...
├── image/
│   ├── midjourney.png
│   ├── stable-diffusion.png
│   └── ...
├── coding/
│   ├── github-copilot.png
│   ├── cursor.png
│   └── ...
└── [other categories]/
```

## 🔗 URLs officielles des principaux outils

### Chatbots
- **ChatGPT**: https://chat.openai.com/
- **Claude**: https://claude.ai/
- **Gemini**: https://gemini.google.com/
- **Perplexity**: https://www.perplexity.ai/
- **Poe**: https://poe.com/

### Image Generation
- **Midjourney**: https://www.midjourney.com/
- **Stable Diffusion**: https://stability.ai/
- **DALL-E**: https://openai.com/dall-e-3
- **Leonardo AI**: https://leonardo.ai/
- **Ideogram**: https://ideogram.ai/

### Coding
- **GitHub Copilot**: https://github.com/features/copilot
- **Cursor**: https://cursor.com/
- **Codeium**: https://codeium.com/
- **Tabnine**: https://www.tabnine.com/
- **AWS CodeWhisperer**: https://aws.amazon.com/codewhisperer/

### Video
- **Runway**: https://runwayml.com/
- **Synthesia**: https://www.synthesia.io/
- **Pictory**: https://pictory.ai/
- **Descript**: https://www.descript.com/

### Audio
- **ElevenLabs**: https://elevenlabs.io/
- **Murf AI**: https://murf.ai/
- **Play.ht**: https://play.ht/
- **Speechify**: https://speechify.com/

### Productivity
- **Notion AI**: https://www.notion.so/product/ai
- **ClickUp AI**: https://clickup.com/ai
- **Motion**: https://www.usemotion.com/
- **Fireflies.ai**: https://fireflies.ai/
- **Otter.ai**: https://otter.ai/

### Writing
- **Jasper AI**: https://www.jasper.ai/
- **Copy.ai**: https://www.copy.ai/
- **Grammarly**: https://www.grammarly.com/
- **Writesonic**: https://writesonic.com/
- **QuillBot**: https://quillbot.com/

### Research
- **Consensus**: https://consensus.app/
- **Elicit**: https://elicit.com/
- **SciSpace**: https://scispace.com/
- **ResearchRabbit**: https://www.researchrabbit.ai/
- **Scite**: https://scite.ai/

## ⚙️ Scripts disponibles

### 1. screenshot_automation_playwright.py
Automatise la capture via Playwright (nécessite installation)

```bash
pip install playwright
playwright install
python3 scripts/screenshot_automation_playwright.py
```

### 2. generate_screenshot_list.py
Génère une liste complète de tous les outils avec leurs URLs

```bash
python3 scripts/generate_screenshot_list.py
```

### 3. batch_download_screenshots.sh
Script bash pour télécharger en batch

```bash
chmod +x scripts/batch_download_screenshots.sh
./scripts/batch_download_screenshots.sh
```

## 📏 Spécifications des screenshots

### Dimensions recommandées:
- **Largeur**: 1920px (Full HD)
- **Hauteur**: 1080px ou plus
- **Format**: PNG (meilleure qualité)
- **Poids**: < 500KB si possible (optimiser avec TinyPNG)

### Contenu à capturer:
1. **Interface principale** de l'outil
2. **Vue d'ensemble** du dashboard
3. **Fonctionnalité signature** de l'outil
4. Éviter les données personnelles/sensibles

## 🚀 Méthode rapide (Top 50 outils)

Si vous voulez commencer rapidement avec les outils les plus populaires:

```bash
python3 scripts/download_top_50_screenshots.py
```

Cela téléchargera automatiquement les screenshots des 50 outils les plus populaires via des sources vérifiées.

## 📊 Progression

Utilisez le script de rapport pour suivre votre progression:

```bash
python3 scripts/check_screenshot_progress.py
```

Cela affichera:
- Nombre total d'outils: 252
- Screenshots disponibles: X
- Screenshots manquants: Y
- Pourcentage de completion: Z%

## 💡 Conseils

1. **Prioriser par catégorie**: Commencez par les catégories les plus importantes (chatbots, image, coding)
2. **Qualité > Quantité**: Mieux vaut 50 screenshots de qualité que 252 screenshots médiocres
3. **Vérifier les licences**: Assurez-vous d'avoir le droit d'utiliser les images
4. **Optimiser les images**: Utilisez TinyPNG ou ImageOptim pour réduire la taille
5. **Nommer correctement**: Utilisez le nom exact du fichier HTML (sans extension)

## 🔍 Ressources supplémentaires

- **Screenshot API**: https://pagepixels.com/ (service payant mais automatique)
- **Screely**: https://screely.com/ (ajout de cadres/mockups)
- **CloudApp**: https://www.getcloudapp.com/ (capture + annotation)

## 📝 Template pour liste CSV

Un fichier CSV `tools_list.csv` a été généré avec:
- Nom de l'outil
- Catégorie
- URL officielle
- Statut du screenshot (✓/✗)

Vous pouvez l'importer dans Google Sheets pour suivre votre progression.

---

**Dernière mise à jour**: Décembre 2025
**Nombre total d'outils**: 252
**Catégories**: 23
