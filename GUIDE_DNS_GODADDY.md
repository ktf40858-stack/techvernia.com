# 🌐 GUIDE : Configurer votre domaine GoDaddy pour GitHub Pages

## 📋 VUE D'ENSEMBLE

Ce guide vous montre comment connecter votre domaine **techvernia.com** acheté sur GoDaddy à votre site GitHub Pages.

**Temps estimé :** 5-10 minutes de configuration + 2-24h pour la propagation DNS

---

## 🎯 ÉTAPE 1 : CRÉER LE FICHIER CNAME

### Qu'est-ce que c'est ?
Le fichier CNAME indique à GitHub Pages quel domaine personnalisé utiliser.

### Action à faire :
1. Un fichier `CNAME` va être créé automatiquement dans `techvernia.com/CNAME`
2. Ce fichier contient simplement : `techvernia.com`
3. Il sera poussé vers GitHub avec vos autres fichiers

✅ **Cette étape sera faite automatiquement par Claude**

---

## 🔧 ÉTAPE 2 : CONFIGURER LES DNS SUR GODADDY

### A. Se connecter à GoDaddy

1. Allez sur : https://www.godaddy.com
2. Cliquez sur **Sign In** (en haut à droite)
3. Connectez-vous avec vos identifiants
4. Allez dans **My Products** (Mes Produits)

### B. Accéder aux paramètres DNS

1. Trouvez votre domaine **techvernia.com** dans la liste
2. Cliquez sur les **3 points** (⋮) ou le bouton **DNS**
3. Sélectionnez **Manage DNS** (Gérer DNS)

### C. Supprimer les enregistrements existants

⚠️ **IMPORTANT** : Avant d'ajouter les nouveaux enregistrements, vous devez supprimer les anciens enregistrements A et CNAME qui pointent vers le parking GoDaddy.

1. Dans la section **Records**, cherchez les enregistrements de type **A** et **CNAME** existants
2. Cliquez sur l'icône **crayon** (✏️) ou **trash** (🗑️) pour chaque enregistrement
3. Supprimez TOUS les enregistrements A et CNAME existants

### D. Ajouter les 4 enregistrements A (pour l'apex domain)

GitHub Pages nécessite **4 adresses IP**. Ajoutez-les une par une :

#### Enregistrement A #1
- **Type** : `A`
- **Name** : `@` (représente techvernia.com)
- **Value** : `185.199.108.153`
- **TTL** : `600 seconds` (ou 1 hour)

#### Enregistrement A #2
- **Type** : `A`
- **Name** : `@`
- **Value** : `185.199.109.153`
- **TTL** : `600 seconds`

#### Enregistrement A #3
- **Type** : `A`
- **Name** : `@`
- **Value** : `185.199.110.153`
- **TTL** : `600 seconds`

#### Enregistrement A #4
- **Type** : `A`
- **Name** : `@`
- **Value** : `185.199.111.153`
- **TTL** : `600 seconds`

### E. Ajouter l'enregistrement CNAME (pour www)

Ceci permet à **www.techvernia.com** de rediriger vers **techvernia.com**.

#### Enregistrement CNAME
- **Type** : `CNAME`
- **Name** : `www`
- **Value** : `ktf40858-stack.github.io` (votre nom d'utilisateur GitHub + .github.io)
- **TTL** : `1 hour`

### F. Sauvegarder les changements

1. Vérifiez que vous avez bien :
   - ✅ 4 enregistrements A pointant vers les IPs GitHub
   - ✅ 1 enregistrement CNAME pour www
2. Cliquez sur **Save** (Sauvegarder)

---

## 🚀 ÉTAPE 3 : CONFIGURER GITHUB PAGES

### A. Aller dans les paramètres du repository

1. Allez sur : https://github.com/ktf40858-stack/techvernia.com/settings/pages
2. Cliquez sur **Settings** (Paramètres)
3. Dans le menu latéral, cliquez sur **Pages**

### B. Configurer le domaine personnalisé

1. Dans la section **Custom domain**, entrez : `techvernia.com`
2. Cliquez sur **Save**
3. ⏳ Attendez quelques secondes - GitHub va vérifier les DNS

### C. Activer HTTPS (après propagation DNS)

⚠️ **NE LE FAITES PAS TOUT DE SUITE** - attendez que les DNS soient propagés (2-24h)

Une fois les DNS propagés :
1. Retournez dans **Settings > Pages**
2. Cochez la case **Enforce HTTPS**
3. ✅ Votre site sera sécurisé avec un certificat SSL gratuit

---

## ⏱️ ÉTAPE 4 : ATTENDRE LA PROPAGATION DNS

### Qu'est-ce que c'est ?
La propagation DNS est le temps nécessaire pour que les serveurs DNS du monde entier mettent à jour leurs informations.

### Délais typiques
- **Minimum** : 30 minutes
- **Typique** : 2-6 heures
- **Maximum** : 24-48 heures

### Vérifier la propagation

#### Méthode 1 : Site web de vérification
Allez sur : https://www.whatsmydns.net

1. Entrez `techvernia.com`
2. Sélectionnez **A** dans le menu déroulant
3. Cliquez sur **Search**
4. ✅ Vous devriez voir `185.199.108.153` (ou une des 4 IPs GitHub)

#### Méthode 2 : Ligne de commande
```bash
# Vérifier les enregistrements A
nslookup techvernia.com

# Vérifier les enregistrements CNAME
nslookup www.techvernia.com
```

Vous devriez voir :
```
Server:  ...
Address:  ...

Name:    techvernia.com
Addresses:  185.199.108.153
            185.199.109.153
            185.199.110.153
            185.199.111.153
```

---

## 🎉 ÉTAPE 5 : TESTER VOTRE SITE

### Une fois les DNS propagés

1. Ouvrez votre navigateur
2. Allez sur : **https://techvernia.com**
3. Vérifiez que :
   - ✅ Le site se charge correctement
   - ✅ Les images s'affichent
   - ✅ Les traductions fonctionnent
   - ✅ L'URL affiche bien `techvernia.com`
   - ✅ Le cadenas HTTPS est présent 🔒

4. Testez aussi : **https://www.techvernia.com**
   - ✅ Doit rediriger automatiquement vers `techvernia.com`

---

## ❌ PROBLÈMES COURANTS ET SOLUTIONS

### Problème 1 : "404 - There isn't a GitHub Pages site here"

**Causes possibles :**
- Le fichier CNAME n'est pas dans le repository
- Le domaine n'est pas configuré dans GitHub Pages Settings

**Solution :**
```bash
# Vérifier que le fichier CNAME existe
ls techvernia.com/CNAME

# Si absent, le recréer et pusher
echo "techvernia.com" > techvernia.com/CNAME
git add techvernia.com/CNAME
git commit -m "Add CNAME file for custom domain"
git push origin master
```

### Problème 2 : "Domain's DNS record could not be retrieved"

**Cause :** Les DNS ne sont pas encore propagés ou mal configurés

**Solution :**
1. Attendez 2-4 heures supplémentaires
2. Vérifiez vos enregistrements DNS sur GoDaddy
3. Utilisez https://www.whatsmydns.net pour vérifier la propagation

### Problème 3 : Le site affiche "Not Secure" (pas sécurisé)

**Cause :** HTTPS n'est pas encore configuré

**Solution :**
1. Attendez que les DNS soient complètement propagés
2. Allez dans **GitHub Settings > Pages**
3. Cochez **Enforce HTTPS**
4. Attendez 5-10 minutes pour que le certificat SSL soit émis

### Problème 4 : "www.techvernia.com" ne fonctionne pas

**Cause :** L'enregistrement CNAME n'est pas correct

**Solution :**
1. Retournez dans GoDaddy DNS
2. Vérifiez que le CNAME est :
   - **Name** : `www`
   - **Value** : `ktf40858-stack.github.io`
3. Attendez la propagation

### Problème 5 : Les anciennes pages GoDaddy s'affichent encore

**Cause :** Cache DNS ou cache navigateur

**Solution :**
```bash
# Vider le cache DNS (Windows)
ipconfig /flushdns

# Vider le cache DNS (Mac/Linux)
sudo dscacheutil -flushcache

# Dans le navigateur
Ctrl + Shift + R (Windows)
Cmd + Shift + R (Mac)
```

---

## 📊 RÉCAPITULATIF CONFIGURATION DNS

### Ce que vous devez avoir sur GoDaddy :

| Type  | Name | Value              | TTL      |
|-------|------|--------------------|----------|
| A     | @    | 185.199.108.153    | 600 sec  |
| A     | @    | 185.199.109.153    | 600 sec  |
| A     | @    | 185.199.110.153    | 600 sec  |
| A     | @    | 185.199.111.153    | 600 sec  |
| CNAME | www  | ktf40858-stack.github.io | 1 hour   |

### Ce que vous devez avoir sur GitHub :

- ✅ Fichier `CNAME` dans le repository avec le contenu : `techvernia.com`
- ✅ Custom domain configuré dans Settings > Pages : `techvernia.com`
- ✅ Enforce HTTPS activé (après propagation DNS)

---

## 🔍 COMMANDES UTILES POUR DIAGNOSTIC

### Vérifier les enregistrements DNS A
```bash
nslookup techvernia.com
```

### Vérifier les enregistrements CNAME
```bash
nslookup www.techvernia.com
```

### Vérifier avec dig (plus détaillé)
```bash
# Windows - installer dig d'abord
# Mac/Linux
dig techvernia.com
dig www.techvernia.com
```

### Tester la résolution DNS depuis différents serveurs
```bash
# Serveur DNS Google
nslookup techvernia.com 8.8.8.8

# Serveur DNS Cloudflare
nslookup techvernia.com 1.1.1.1
```

---

## 📖 RESSOURCES SUPPLÉMENTAIRES

### Documentation officielle
- [GitHub Pages Custom Domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)
- [GoDaddy DNS Management](https://www.godaddy.com/help/manage-dns-680)

### Outils de vérification
- **DNS Propagation** : https://www.whatsmydns.net
- **DNS Checker** : https://dnschecker.org
- **SSL Checker** : https://www.sslshopper.com/ssl-checker.html

---

## 🆘 BESOIN D'AIDE ?

Si vous rencontrez des problèmes :

1. **Vérifiez les étapes** : Relisez chaque section de ce guide
2. **Attendez la propagation** : La plupart des problèmes se résolvent après 2-6h
3. **Vérifiez les DNS** : Utilisez https://www.whatsmydns.net
4. **Demandez à Claude** :
   ```
   "Claude, j'ai un problème avec mon DNS : [décrivez le problème]"
   "Claude, mon site affiche une erreur 404"
   "Claude, HTTPS ne fonctionne pas"
   ```

---

## ✅ CHECKLIST FINALE

Avant de considérer la configuration terminée :

- [ ] ✅ Fichier CNAME créé et poussé vers GitHub
- [ ] ✅ 4 enregistrements A configurés sur GoDaddy
- [ ] ✅ 1 enregistrement CNAME configuré sur GoDaddy
- [ ] ✅ Custom domain configuré dans GitHub Pages Settings
- [ ] ✅ DNS propagés (vérifiez avec whatsmydns.net)
- [ ] ✅ Site accessible via https://techvernia.com
- [ ] ✅ Site accessible via https://www.techvernia.com
- [ ] ✅ HTTPS activé (cadenas 🔒 visible)
- [ ] ✅ Toutes les pages se chargent correctement
- [ ] ✅ Traductions fonctionnent

---

**🎉 Félicitations ! Votre site est maintenant en ligne sur votre domaine personnalisé !**
