# 🎨 Guide pour télécharger les VRAIS logos des AI

Les logos actuellement présents ne correspondent pas toujours aux vrais logos officiels des AI.
Voici comment obtenir les VRAIS logos officiels:

---

## ✍️ AI WRITING TOOLS

### Grammarly
- **Source**: https://upload.wikimedia.org/wikipedia/commons/f/f8/Grammarly_Logo.svg
- **Ou**: https://www.grammarly.com (Clic droit sur le logo → Enregistrer l'image)
- **Fichier**: `assets/images/tools/writing/grammarly.svg`
- **Vrai logo**: Cercle vert avec "G" blanc

### Copy.ai
- **Source**: https://www.copy.ai (logo dans le header)
- **Fichier**: `assets/images/tools/writing/copyai.svg`
- **Vrai logo**: Étoile verte/bleue

### Jasper
- **Source**: https://www.jasper.ai (logo dans le header)
- **Fichier**: `assets/images/tools/writing/jasper-ai.svg`
- **Vrai logo**: Tête violette stylisée

### QuillBot
- **Source**: https://quillbot.com (logo dans le header)
- **Fichier**: `assets/images/tools/writing/quillbot.svg`
- **Vrai logo**: Plume avec dégradé vert/bleu

### Rytr
- **Source**: https://rytr.me
- **Fichier**: `assets/images/tools/writing/rytr.svg`
- **Vrai logo**: "R" stylisé violet

### Wordtune
- **Source**: https://www.wordtune.com
- **Fichier**: `assets/images/tools/writing/wordtune.svg`
- **Vrai logo**: "W" avec arc bleu

### Writesonic
- **Source**: https://writesonic.com
- **Fichier**: `assets/images/tools/writing/writesonic.svg`
- **Vrai logo**: Cercles ondulatoires violets

---

## 🎨 AI IMAGE GENERATION

### Midjourney
- **Source**: DÉJÀ OK (logo existant est correct)
- **Vrai logo**: Voilier stylisé noir/blanc

### DALL-E 3
- **Source**: https://openai.com
- **Fichier**: `assets/images/tools/image/dall-e-3.svg`
- **Vrai logo**: Logo OpenAI (même que ChatGPT)

### Stable Diffusion
- **Source**: https://stability.ai
- **Fichier**: `assets/images/tools/image/stable-diffusion.svg`
- **Vrai logo**: Flamme stylisée noire

### Leonardo.AI
- **Source**: https://leonardo.ai
- **Fichier**: `assets/images/tools/image/leonardo-ai.svg`
- **Vrai logo**: "L" dans un cercle orange/rouge

### Ideogram
- **Source**: https://ideogram.ai
- **Fichier**: `assets/images/tools/image/ideogram.svg`
- **Vrai logo**: Symbole géométrique coloré

### Canva AI
- **Source**: https://www.canva.com
- **Fichier**: `assets/images/tools/image/canva-ai.svg`
- **Vrai logo**: Logo Canva multicolore

### Adobe Firefly
- **Source**: https://firefly.adobe.com
- **Fichier**: `assets/images/tools/image/adobe-firefly.svg`
- **Vrai logo**: Luciole stylisée colorée

### Clipdrop
- **Source**: https://clipdrop.co
- **Fichier**: `assets/images/tools/image/clipdrop.svg`
- **Vrai logo**: Ciseaux avec goutte

---

## 🛡️ AI CYBERSECURITY

### CrowdStrike
- **Source**: https://www.crowdstrike.com
- **Fichier**: `assets/images/tools/cybersecurity/crowdstrike.svg`
- **Vrai logo**: Faucon rouge stylisé

### Darktrace
- **Source**: https://darktrace.com
- **Fichier**: `assets/images/tools/cybersecurity/darktrace.svg`
- **Vrai logo**: Hexagone orange/rouge

### SentinelOne
- **Source**: https://www.sentinelone.com
- **Fichier**: `assets/images/tools/cybersecurity/sentinelone.svg`
- **Vrai logo**: "S" dans bouclier violet

### Okta
- **Source**: https://www.okta.com
- **Fichier**: `assets/images/tools/cybersecurity/okta.svg`
- **Vrai logo**: Cercle bleu avec "O"

### Snyk
- **Source**: https://snyk.io
- **Fichier**: `assets/images/tools/cybersecurity/snyk.svg`
- **Vrai logo**: Chien violet stylisé

### Wiz
- **Source**: https://www.wiz.io
- **Fichier**: `assets/images/tools/cybersecurity/wiz.svg`
- **Vrai logo**: "W" violet/bleu

---

## 📋 MÉTHODE RAPIDE

### Option 1: Téléchargement manuel
1. Visitez le site officiel de l'AI
2. Clic droit sur le logo dans le header
3. "Enregistrer l'image sous..."
4. Sauvegardez avec le bon nom dans le bon dossier

### Option 2: Inspect Element
1. Visitez le site officiel
2. F12 (DevTools) → Onglet Elements
3. Cherchez `<img>` ou `<svg>` du logo
4. Copiez l'URL de l'image
5. Téléchargez avec `wget`:
```bash
wget -O assets/images/tools/writing/grammarly.svg "URL_DU_LOGO"
```

### Option 3: Brandfetch (Recommandé)
1. Allez sur https://brandfetch.com
2. Cherchez le nom de l'AI
3. Téléchargez le logo SVG officiel
4. Renommez et placez dans le bon dossier

---

## 🔍 VÉRIFICATION

Après téléchargement, vérifiez que les logos sont corrects:

```bash
# Voir les logos dans le navigateur
cd assets/images/tools/writing
xdg-open grammarly.svg  # Ouvre le logo dans le navigateur

# Ou vérifier la taille
ls -lh *.svg
```

Les vrais logos doivent:
- ✅ Être en SVG (de préférence) ou PNG haute résolution
- ✅ Avoir les bonnes couleurs de marque
- ✅ Être reconnaissables immédiatement
- ✅ Faire plus de 2KB (pas juste une lettre générique)

---

## ⚠️ IMPORTANT

**NE PAS utiliser:**
- ❌ Logos génériques (juste des lettres)
- ❌ Favicons (trop petits)
- ❌ Logos de mauvaise qualité
- ❌ Anciens logos obsolètes

**UTILISER:**
- ✅ Logos SVG officiels
- ✅ Logos depuis les press kits
- ✅ Logos depuis Brandfetch
- ✅ Logos depuis Wikipedia/Wikimedia Commons

---

*Une fois tous les logos téléchargés, lancez:*
```bash
python3 verify_tool_logos.py
```
