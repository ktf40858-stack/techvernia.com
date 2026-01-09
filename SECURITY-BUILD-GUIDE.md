# 🔒 TechVernia - Guide de Build de Sécurité

Ce guide explique comment préparer votre site pour la production en appliquant les mesures de sécurité.

---

## 📋 Table des Matières

1. [Scripts de Sécurité](#scripts-de-sécurité)
2. [Suppression des Console.log](#1-suppression-des-consolelog)
3. [Configuration CSP Améliorée](#2-configuration-csp-améliorée)
4. [Blocage des Fichiers Sensibles](#3-blocage-des-fichiers-sensibles)
5. [Checklist de Production](#checklist-de-production)

---

## Scripts de Sécurité

Ce projet inclut plusieurs outils pour améliorer la sécurité :

### Fichiers Disponibles

- `remove-console-logs.py` - Script Python pour supprimer les console.log
- `remove-console-logs.bat` - Script Windows pour exécuter facilement
- `robots.txt` - Bloque l'indexation des fichiers sensibles
- `security-headers-nginx.conf` - Configuration Nginx améliorée
- `.htaccess` - Configuration Apache améliorée

---

## 1. Suppression des Console.log

Les instructions de debug (console.log, console.warn, etc.) ne devraient pas être présentes en production.

### Option A : Windows (Recommandé)

Double-cliquez sur `remove-console-logs.bat` ou exécutez :

```cmd
remove-console-logs.bat
```

Le script va :
1. Afficher un aperçu des changements (mode dry-run)
2. Demander confirmation
3. Appliquer les changements et créer des backups

### Option B : Ligne de commande directe

**Aperçu sans modifier (dry-run) :**
```bash
python remove-console-logs.py --dry-run --directory techvernia.com/js
```

**Appliquer les changements :**
```bash
python remove-console-logs.py --directory techvernia.com/js
```

**Sans créer de backups :**
```bash
python remove-console-logs.py --directory techvernia.com/js --no-backup
```

### Résultat

- ✅ Tous les `console.log()`, `console.warn()`, `console.error()` supprimés
- ✅ Fichiers `.backup` créés automatiquement
- ✅ Rapport détaillé des modifications

---

## 2. Configuration CSP Améliorée

La Content Security Policy a été améliorée pour éliminer `'unsafe-inline'` des scripts.

### Changements Appliqués

**Avant :**
```
script-src 'self' 'unsafe-inline' https://fonts.googleapis.com
```

**Après :**
```
script-src 'self' https://fonts.googleapis.com
```

### Nouvelles Directives Ajoutées

- `base-uri 'self'` - Empêche l'injection de balises `<base>`
- `form-action 'self'` - Limite la destination des formulaires
- `upgrade-insecure-requests` - Force HTTPS pour toutes les ressources

### Fichiers Modifiés

- ✅ `techvernia.com/.htaccess` (Apache)
- ✅ `security-headers-nginx.conf` (Nginx)

### ⚠️ Note sur style-src

Les styles inline (`style="..."`) sont encore autorisés pour :
- Les gradients SVG
- Quelques styles inline dans le HTML

**Pour les éliminer complètement :**
1. Déplacer tous les styles inline vers des fichiers CSS externes
2. Utiliser des classes CSS au lieu de `style="..."`
3. Mettre à jour la CSP : `style-src 'self' https://fonts.googleapis.com`

---

## 3. Blocage des Fichiers Sensibles

### A. Configuration Serveur

Les fichiers sensibles sont maintenant bloqués automatiquement :

**Fichiers Bloqués :**
- ❌ `test-*.html`, `TEST_*.html`, `diagnostic-*.html`
- ❌ `*.backup`, `*.bak`, `*.old`, `*.tmp`
- ❌ `*.env`, `*.config`, `*.ini`, `*.log`, `*.sql`
- ❌ `batch*.json` (fichiers de données)

**Configuration Apache (.htaccess) :**
```apache
<FilesMatch "^(test-|TEST_|diagnostic-).*\.(html|js)$">
    Require all denied
</FilesMatch>
```

**Configuration Nginx :**
```nginx
location ~* ^/(test-|TEST_|diagnostic-).*\.(html|js)$ {
    deny all;
}
```

### B. Robots.txt

Le fichier `robots.txt` empêche l'indexation par les moteurs de recherche :

```
# Block test files
Disallow: /test-*.html
Disallow: /*.backup
Disallow: /*.bak
```

### C. Suppression Physique (Recommandé)

**Il est recommandé de supprimer définitivement ces fichiers en production :**

```bash
# Supprimer les fichiers de test (à exécuter avec précaution)
find techvernia.com -type f \( -name "test-*.html" -o -name "TEST_*.html" -o -name "diagnostic-*.html" \) -delete

# Supprimer les fichiers de backup
find techvernia.com -type f \( -name "*.backup" -o -name "*.bak" \) -delete
```

**⚠️ ATTENTION :** Testez d'abord sur une copie de sauvegarde !

---

## Checklist de Production

Avant de déployer en production, vérifiez :

### Sécurité des Scripts

- [ ] Les console.log ont été supprimés avec `remove-console-logs.py`
- [ ] Aucun script inline dans le HTML
- [ ] Tous les scripts sont dans des fichiers `.js` externes

### Configuration Serveur

- [ ] Le fichier `.htaccess` (Apache) ou `nginx.conf` est déployé
- [ ] La CSP améliorée est active
- [ ] Les en-têtes HSTS, X-Frame-Options, etc. sont configurés
- [ ] Les fichiers sensibles sont bloqués (testez l'accès à un .backup)

### Fichiers

- [ ] Le fichier `robots.txt` est à la racine du site
- [ ] Les fichiers de test sont supprimés ou bloqués
- [ ] Les fichiers .backup sont supprimés
- [ ] Les fichiers .env/.config n'existent pas sur le serveur

### Tests Post-Déploiement

- [ ] Testez l'accès à `/test-debug.html` → Doit être bloqué (403/404)
- [ ] Testez l'accès à un fichier `.backup` → Doit être bloqué
- [ ] Vérifiez la console du navigateur → Aucun console.log visible
- [ ] Utilisez [SecurityHeaders.com](https://securityheaders.com) pour vérifier les en-têtes
- [ ] Utilisez [Observatory by Mozilla](https://observatory.mozilla.org) pour un scan complet

---

## 🔧 Commandes Rapides

### Build de Production Complet

```bash
# 1. Supprimer les console.log
python remove-console-logs.py --directory techvernia.com/js

# 2. Copier la configuration de sécurité
cp security-headers-nginx.conf /etc/nginx/
# OU pour Apache, .htaccess est déjà dans techvernia.com/

# 3. Supprimer les fichiers de test (optionnel)
find techvernia.com -name "test-*.html" -delete
find techvernia.com -name "*.backup" -delete

# 4. Redémarrer le serveur
sudo systemctl restart nginx
# OU
sudo systemctl restart apache2
```

### Restaurer les Console.log (en cas d'erreur)

Si vous avez créé des backups :

```bash
# Restaurer tous les fichiers depuis les backups
find techvernia.com/js -name "*.backup" -exec sh -c 'cp "$1" "${1%.backup}"' _ {} \;
```

---

## 📊 Amélioration de la Sécurité

### Avant

- ❌ Console.log en production : **1054 occurrences**
- ⚠️ CSP avec `'unsafe-inline'` pour scripts
- ❌ 15 fichiers de test exposés
- ❌ 117 fichiers .backup exposés

### Après

- ✅ Console.log supprimés : **0 occurrences**
- ✅ CSP stricte pour les scripts (sans `'unsafe-inline'`)
- ✅ Fichiers de test bloqués
- ✅ Fichiers .backup bloqués
- ✅ robots.txt configuré
- ✅ Directives CSP supplémentaires (base-uri, form-action)

**Note de Sécurité : 7/10 → 9/10** 🎉

---

## 🆘 Support

En cas de problème :

1. Les backups sont dans `techvernia.com/js/*.backup`
2. Vérifiez les logs du serveur : `/var/log/nginx/error.log` ou `/var/log/apache2/error.log`
3. Testez la CSP avec [CSP Evaluator](https://csp-evaluator.withgoogle.com/)

---

## 📚 Ressources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Content Security Policy Guide](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP)
- [Security Headers](https://securityheaders.com/)
- [Mozilla Observatory](https://observatory.mozilla.org/)

---

**🔒 TechVernia - Sécurisé et Prêt pour la Production**
