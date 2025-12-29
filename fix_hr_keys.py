#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys,io,re
if sys.platform=='win32':sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

# Lire les clés du HTML
with open('/tmp/paradox_keys.txt','r') as f:
    html_keys = [k.strip() for k in f if k.startswith('review.paradox')]

# Lire le fichier i18n actuel
with open('GenuisNet.ai/js/paradox-olivia-i18n.js','r',encoding='utf-8') as f:
    content = f.read()

# Extraire les traductions FR existantes
fr_match = re.search(r'"fr":\s*\{([^\}]+(?:\}[^\}]+)*?)\},\s*"de"',content,re.DOTALL)
if not fr_match:
    print("Erreur: Section FR non trouvée")
    sys.exit(1)

fr_section = fr_match.group(1)
existing_translations = {}
for match in re.finditer(r'"([^"]+)":\s*"([^"]+)"',fr_section):
    existing_translations[match.group(1)] = match.group(2)

print(f"Clés HTML: {len(html_keys)}")
print(f"Traductions FR: {len(existing_translations)}")
print(f"Manquantes: {len(set(html_keys)-set(existing_translations.keys()))}")
